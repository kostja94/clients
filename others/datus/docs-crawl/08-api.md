# API

## API Introduction

Datus REST API exposes the agentic chat loop, knowledge-base explorer, database catalog, and semantic-model management as HTTP endpoints.

### Entry Points Comparison
| Entry point | Best for |
|-------------|----------|
| CLI (`datus`) | Local interactive development |
| MCP (`datus-mcp`) | Embedding tools in another agent |
| REST API (`datus-api`) | Web frontends, services, automation |

### Authentication Model
The open-source build uses header-based identification:
```
X-Datus-User-Id: alice
```
No token required; the caller identifies itself by sending a `X-Datus-User-Id` header matching `^[A-Za-z0-9_-]+$`.

### Response Envelope
```json
{
  "success": true,
  "data": { ... },
  "errorCode": null,
  "errorMessage": null
}
```

### URL Prefix
All v1 endpoints live under `/api/v1`. Health check and Swagger UI sit at the application root.

---

## Chat API

### Endpoints

**POST /api/v1/chat/stream** — Send a chat message and stream the response as SSE.

Body:
| Field | Type | Notes |
|-------|------|-------|
| `message` | string | Required. User message |
| `session_id` | string? | Reuse to continue an existing session |
| `subagent_id` | string? | Built-in name or custom subagent id |
| `plan_mode` | bool | Enable plan mode |
| `catalog`/`database`/`db_schema` | string? | Database context |
| `table_paths`/`metric_paths`/`sql_paths`/`knowledge_paths` | string[]? | `@`-reference paths |
| `max_turns` | int | Default `30` |
| `prompt_language` | string | `en` (default) or `zh` |
| `stream_response` | bool? | Stream thinking deltas token-by-token |

**POST /api/v1/chat/resume** — Reconnect to a still-running task.
**POST /api/v1/chat/stop** — Interrupt a running session.
**POST /api/v1/chat/sessions/{session_id}/compact** — Summarize and compress session history.
**GET /api/v1/chat/sessions** — List all chat sessions for current user.
**DELETE /api/v1/chat/sessions/{session_id}** — Delete a session.
**GET /api/v1/chat/history?session_id=...** — Return full conversation messages.
**POST /api/v1/chat/user_interaction** — Submit answer to an interactive prompt.

### SSE Streaming Format
```
id: <sequential int>
event: <event type>
data: <JSON payload>
```

### Event Types
| Event | When | Description |
|-------|------|-------------|
| `session` | Once, immediately after session creation | `{session_id, llm_session_id}` |
| `message` | Repeatedly, for every agent action | `MessageData` with content items |
| `error` | Once, on fatal failure (terminates task) | `ErrorData` |
| `ping` | Every ~10s while idle but running | `{}` |
| `end` | Once, final event of successful run | `EndData` |

### Content Item Types within MessageData
| Type | Purpose |
|------|---------|
| `markdown` | Plain text/markdown from assistant |
| `thinking` | Intermediate reasoning (collapsed in UI) |
| `code` | Code block, typically generated SQL |
| `call-tool` | Agent calling a tool |
| `call-tool-result` | Tool execution result |
| `error` | Action-level error (task may continue) |
| `user-interaction` | Agent needs user decision |
| `subagent-complete` | Sub-agent finished delegated task |

### Thinking-Delta Streaming
When `stream_response: true`:
1. `createMessage` — first delta, creates message container
2. `appendMessage` — subsequent deltas, incremental text
3. `updateMessage` — final response, replaces all deltas with complete content

### End-to-End Demo
```bash
# 1. Start new conversation
curl -N -X POST http://127.0.0.1:8000/api/v1/chat/stream \
  -H 'Content-Type: application/json' \
  -H 'X-Datus-User-Id: alice' \
  -d '{ "message": "Show top 5 customers last month" }'

# 2. Resume after disconnect
curl -N -X POST http://127.0.0.1:8000/api/v1/chat/resume \
  -H 'Content-Type: application/json' \
  -H 'X-Datus-User-Id: alice' \
  -d '{ "session_id": "chat_session_a1b2c3d4", "from_event_id": 18 }'

# 3. Follow-up turn
curl -N -X POST http://127.0.0.1:8000/api/v1/chat/stream \
  -H 'Content-Type: application/json' \
  -H 'X-Datus-User-Id: alice' \
  -d '{ "session_id": "chat_session_a1b2c3d4", "message": "Break that down by region" }'

# 4. Respond to interaction request
curl -X POST http://127.0.0.1:8000/api/v1/chat/user_interaction \
  -H 'Content-Type: application/json' \
  -H 'X-Datus-User-Id: alice' \
  -d '{ "session_id": "chat_session_a1b2c3d4", "interaction_key": "act_0007", "input": ["1"] }'
```

### Python Client
```python
import json, httpx

async def stream_chat(message: str, user_id: str = "alice"):
    headers = {"X-Datus-User-Id": user_id}
    payload = {"message": message}
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", "http://127.0.0.1:8000/api/v1/chat/stream",
                                 json=payload, headers=headers) as resp:
            event = {}
            async for line in resp.aiter_lines():
                if line == "":
                    if event:
                        yield event
                        event = {}
                    continue
                key, _, value = line.partition(": ")
                if key == "data":
                    event["data"] = json.loads(value)
                else:
                    event[key] = value
```

---

## API Deployment

### Install
```bash
uv sync  # registers datus-api console script
```

### Launch
```bash
datus-api --host 0.0.0.0 --port 8000
```

### CLI Arguments
| Flag | Default | Description |
|------|---------|-------------|
| `--config` | (auto-resolved) | Path to `agent.yml` |
| `--database` | `default` | Namespace from `agent.yml` |
| `--output-dir` | `./output` | Directory for generated artifacts |
| `--log-level` | `INFO` | `DEBUG`/`INFO`/`WARNING`/`ERROR`/`CRITICAL` |
| `--host` | `127.0.0.1` | Bind address |
| `--port` | `8000` | Bind port |
| `--reload` | off | Auto-reload on file change (dev only) |
| `--workers` | `1` | Number of uvicorn worker processes |

### Environment Variables
| Variable | Equivalent flag |
|----------|-----------------|
| `DATUS_CONFIG` | `--config` |
| `DATUS_NAMESPACE` | `--database` |
| `DATUS_OUTPUT_DIR` | `--output-dir` |
| `DATUS_LOG_LEVEL` | `--log-level` |
| `DATUS_CORS_ORIGINS` | CORS origins, default `*` |

### Config Resolution Priority
1. `--config` flag (or `DATUS_CONFIG`) if explicitly set
2. `./conf/agent.yml` in current working directory
3. `~/.datus/conf/agent.yml`

### Built-in Endpoints
| Path | Description |
|------|-------------|
| `GET /` | Service banner with version pointer |
| `GET /health` | Health check (no auth required) |
| `GET /docs` | Swagger UI |
| `GET /openapi.json` | OpenAPI 3 spec |

### Quickstart
```bash
# Start server
datus-api --port 8000 &

# Health check
curl http://127.0.0.1:8000/health

# List catalogs (identifies as user "alice")
curl -H 'X-Datus-User-Id: alice' 'http://127.0.0.1:8000/api/v1/catalog/list'

# Send a streaming chat
curl -N -X POST http://127.0.0.1:8000/api/v1/chat/stream \
  -H 'Content-Type: application/json' \
  -H 'X-Datus-User-Id: alice' \
  -d '{"message": "How many users signed up last week?"}'
```

### Production Notes
- Run behind a reverse proxy (nginx/traefik) and terminate TLS upstream
- Disable response buffering for SSE endpoints on your reverse proxy
- When running multiple workers, enable sticky sessions at proxy level
