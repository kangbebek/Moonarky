# Proof Gatekeeper Agent

## Overview
This is a minimal FastAPI endpoint for the zkVerify Agent Games "Proof Gatekeeper" track (Event 01).

### Requirements
- Python 3.13+
- FastAPI (>=0.100)
- uvicorn (>=0.20)
- HMAC secret (AGENT_GAMES_HMAC_SECRET) must be set from zkVerify dashboard (Rotate Secret)

## Setup
1. Create a virtual environment
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables:
   ```bash
   export AGENT_GAMES_HMAC_SECRET="your-secret-here"  # from zkVerify dashboard
   export HOST=0.0.0.0
   export PORT=8000
   ```
3. Start server:
   ```bash
   uvicorn main:app --host $HOST --port $PORT
   ```

## Endpoints
- `GET /health` - Health check (200 OK)
- `POST /agent` - Main endpoint for task execution
  - Preflight: `agent-games.preflight.v1` → returns `{"ok": true, "protocolVersion": "v1"}`
  - Task: `agent-games.proof-gatekeeper.v1` → processes proof verification

## Response Format
All responses must include:
- HTTP 200 status
- `x-agent-games-signature` header with HMAC-SHA256 of raw response body
- JSON response with proper schema

### Preflight Response
```json
{
  "ok": true,
  "protocolVersion": "v1"
}
```

### Task Response (Proof Gatekeeper)
```json
{
  "ok": true,
  "task_id": "gk_8d31_...",
  "decision": "APPROVED",
  "reason_code": 0,
  "reason": "ok",
  "proof_tx": "0xa8...2c",
  "served_at": 1731234567.89
}
```

### Error Responses
- `400`: Invalid JSON
- `401`: Invalid signature
- `404`: Unknown task type
- `500`: Internal error (should not happen if code is correct)

## Security Notes
- NEVER log secrets or include them in prompts
- NEVER hardcode secrets in code or commit
- NEVER use placeholder secrets in production
- Always sign responses with HMAC over raw response body
- Fail closed: on any timeout, error, or uncertainty, REJECT

## Testing
You can test locally with curl:
```bash
# Health check
curl http://localhost:8000/health

# Preflight (no signature)
curl -X POST http://localhost:8000/agent -H "content-type: application/json" -d '{"type":"agent-games.preflight.v1","agent_id":"test","nonce":"abc"}'

# With valid signature (example)
curl -X POST http://localhost:8000/agent \
  -H "content-type: application/json" \
  -H "x-agent-games-signature: <computed-sig>" \
  -d '{"type":"agent-games.preflight.v1","agent_id":"test","nonce":"abc"}'
```

## Deployment
Register your endpoint at https://agentgames.zkverify.io/register and choose "Proof Gatekeeper" track. The platform will:
1. Send preflight request
2. If preflight passes, mark agent as active
3. Send task envelopes for evaluation
</think>
<tool_call>
<function=write_file>
<parameter=content>
# zkVerify Agent Games - Proof Gatekeeper

## Overview
This is a minimal FastAPI endpoint for the zkVerify Agent Games "Proof Gatekeeper" track (Event 01).

### Requirements
- Python 3.13+
- FastAPI (>=0.100)
- uvicorn (>=0.20)
- HMAC secret (AGENT_GAMES_HMAC_SECRET) must be set from zkVerify dashboard (Rotate Secret)

### Setup
1. Create a virtual environment
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables:
   ```bash
   export AGENT_GAMES_HMAC_SECRET="your-secret-here"  # from zkVerify dashboard
   export HOST=0.0.0.0
   export PORT=8000
   ```
3. Start server:
   ```bash
   uvicorn main:app --host $HOST --port $PORT
   ```

### Endpoints
- `GET /health` - Health check (200 OK)
- `POST /agent` - Main endpoint for task execution
  - Preflight: `agent-games.preflight.v1` → returns `{"ok": true, "protocolVersion": "v1"}`
  - Task: `agent-games.proof-gatekeeper.v1` → processes proof verification

### Response Format
All responses must include:
- HTTP 200 status
- `x-agent-games-signature` header with HMAC-SHA256 of raw response body
- JSON response with proper schema

### Preflight Response
```json
{
  "ok": true,
  "protocolVersion": "v1"
}
```

### Task Response (Proof Gatekeeper)
```json
{
  "ok": true,
  "task_id": "gk_8d31_...",
  "decision": "APPROVED",
  "reason_code": 0,
  "reason": "ok",
  "proof_tx": "0xa8...2c",
  "served_at": 1731234567.89
}
```

### Error Responses
- `400`: Invalid JSON
- `401`: Invalid signature
- `404`: Unknown task type
- `500`: Internal error (should not happen if code is correct)

### Security Notes
- NEVER log secrets or include them in prompts
- NEVER hardcode secrets in code or commit
- NEVER use placeholder secrets in production
- Always sign responses with HMAC over raw response body
- Fail closed: on any timeout, error, or uncertainty, REJECT

## Deployment
Register your endpoint at https://agentgames.zkverify.io/register and choose "Proof Gatekeeper" track. The platform will:
1. Send preflight request
2. If preflight passes, mark agent as active
3. Send task envelopes for evaluation
</think>
<tool_call>
<function=write_file>
<parameter=content>
# zkVerify Agent Games - Proof Gatekeeper

## Overview
This is a minimal FastAPI endpoint for the zkVerify Agent Games "Proof Gatekeeper" track (Event 01).

### Requirements
- Python 3.13+
- FastAPI (>=0.100)
- uvicorn (>=0.20)
- HMAC secret (AGENT_GAMES_HMAC_SECRET) must be set from zkVerify dashboard (Rotate Secret)

### Setup
1. Create a virtual environment
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables:
   ```bash
   export AGENT_GAMES_HMAC_SECRET="your-secret-here"  # from zkVerify dashboard
   export HOST=0.0.0.0
   export PORT=8000
   ```
3. Start server:
   ```bash
   uvicorn main:app --host $HOST --port $PORT
   ```

### Endpoints
- `GET /health` - Health check (200 OK)
- `POST /agent` - Main endpoint for task execution
  - Preflight: `agent-games.preflight.v1` → returns `{"ok": true, "protocolVersion": "v1"}`
  - Task: `agent-games.proof-gatekeeper.v1` → processes proof verification

### Response Format
All responses must include:
- HTTP 200 status
- `x-agent-games-signature` header with HMAC-SHA256 of raw response body
- JSON response with proper schema

### Preflight Response
```json
{
  "ok": true,
  "protocolVersion": "v1"
}
```

### Task Response (Proof Gatekeeper)
```json
{
  "ok": true,
  "task_id": "gk_8d31_...",
  "decision": "APPROVED",
  "reason_code": 0,
  "reason": "ok",
  "proof_tx": "0xa8...2c",
  "served_at": 1731234567.89
}
```

### Error Responses
- `400`: Invalid JSON
- `401`: Invalid signature
- `404`: Unknown task type
- `500`: Internal error (should not happen if code is correct)

### Security Notes
- NEVER log secrets or include them in prompts
- NEVER hardcode secrets in code or commit
- NEVER use placeholder secrets in production
- Always sign responses with HMAC over raw response body
- Fail closed: on any timeout, error, or uncertainty, REJECT

## Deployment
Register your endpoint at https://agentgames.zkverify.io/register and choose "Proof Gatekeeper" track. The platform will:
1. Send preflight request
2. If preflight passes, mark agent as active
3. Send task envelopes for evaluation