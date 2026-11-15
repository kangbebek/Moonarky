"""Proof Gatekeeper agent for zkVerify Agent Games.

Contract (from https://agentgames.zkverify.io/build):
- Platform POSTs signed task envelopes to /agent.
- Every response carries x-agent-games-signature = HMAC-SHA256(SECRET, raw response body).
- Preflight must answer {"ok": true, "protocolVersion": "v1"}.
- Fail closed: on any timeout, error, or uncertainty, REJECT. Never approve by default.
- Secrets come from env only (AGENT_GAMES_HMAC_SECRET). Never logged, never committed.
"""

import os
import hmac
import hashlib
import json
import time

from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

SECRET = os.environ.get("AGENT_GAMES_HMAC_SECRET", "").encode()
VERSION = "v1"


def sign_raw(raw: bytes) -> str:
    return hmac.new(SECRET, raw, hashlib.sha256).hexdigest()


def json_response(obj, status=200):
    raw = json.dumps(obj, separators=(",", ":")).encode()
    return Response(content=raw, status_code=status, media_type="application/json",
                    headers={"x-agent-games-signature": sign_raw(raw)})


@app.get("/health")
async def health():
    return json_response({"status": "ok", "version": VERSION})


@app.post("/agent")
async def agent_task(request: Request):
    raw = await request.body()

    sig = request.headers.get("x-agent-games-signature", "")
    expected = sign_raw(raw)
    if not hmac.compare_digest(sig, expected):
        return json_response({"ok": False, "error": "invalid signature"}, status=401)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return json_response({"ok": False, "error": "invalid JSON"}, status=400)

    kind = data.get("type", "")

    if kind == "agent-games.preflight.v1":
        return json_response({"ok": True, "protocolVersion": VERSION})

    if kind == "agent-games.proof-gatekeeper.v1":
        return handle_gatekeeper(data)

    return json_response({"ok": False, "error": "unknown task type", "type": kind}, status=400)


def handle_gatekeeper(data):
    inp = data.get("input", {})

    required = ["registered_vk", "proof_vk", "minimum", "public_balance",
                "expiry_block", "current_block", "recipient", "condition_recipient",
                "amount", "max_transfer", "proof_tx"]
    missing = [k for k in required if k not in inp or inp[k] in (None, "")]
    if missing:
        return decide(data, False, "missing_fields:" + ",".join(missing), reason_code=2)

    try:
        amount = int(inp["amount"])
        max_transfer = int(inp["max_transfer"])
        minimum = int(inp["minimum"])
        balance = int(inp["public_balance"])
        expiry = int(inp["expiry_block"])
        current = int(inp["current_block"])
    except (ValueError, TypeError):
        return decide(data, False, "non_integer_amounts", reason_code=3)

    # Deterministic policy checks (fail closed on any violation)
    if inp["proof_vk"] != inp["registered_vk"]:
        return decide(data, False, "vk_mismatch", reason_code=4)
    if amount > max_transfer:
        return decide(data, False, "amount_over_max_transfer", reason_code=5)
    if balance < minimum:
        return decide(data, False, "balance_below_minimum", reason_code=6)
    if current >= expiry:
        return decide(data, False, "proof_expired", reason_code=7)
    if inp["recipient"] != inp["condition_recipient"]:
        return decide(data, False, "recipient_mismatch", reason_code=8)

    return decide(data, True, "ok", reason_code=0)


def decide(data, approved, reason, reason_code):
    return json_response({
        "ok": True,
        "task_id": data.get("task_id"),
        "decision": "APPROVED" if approved else "REJECTED",
        "reason_code": reason_code,
        "reason": reason,
        "proof_tx": data.get("input", {}).get("proof_tx"),
        "served_at": int(time.time()),
    })
