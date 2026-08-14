---
title: "How to Build a DeepSeek Agent: From API Key to Your First Agent"
description: "Step-by-step guide to building a DeepSeek Agent with V4 Pro and V4 Flash. Covers API setup, model selection, tool calling, the agent loop, thinking mode, and production error handling — with Python and Node.js examples."
slug: "how-to-build-deepseek-agent"
date: 2026-08-05
author: "Kostja"
category: "DeepSeek"
secondaryCategory: "Product"
---

## TL;DR

- Building a DeepSeek Agent takes three practical steps: get an API key from platform.deepseek.com, pick `deepseek-v4-pro` for complex reasoning or `deepseek-v4-flash` for speed and cost, and implement the agent loop — the pattern that feeds tool call results back into context so the model can decide the next step.
- The agent loop is the part most tutorials skip. You define tools, the model returns a tool call, your code executes it, you append the result as a `tool` role message, and you send the updated history back. Repeat until the model produces a final answer.
- If you are building a coding agent, you probably do not need to write this loop from scratch — tools like DeepSeek-TUI and Reasonix already implement it. But understanding the loop is essential for debugging, customizing, and building agents for non-coding tasks. For an overview of what types of DeepSeek Agents exist, see [What Is a DeepSeek Agent](/blog/what-is-deepseek-agent).
- This tutorial uses the OpenAI Python SDK (`pip install openai`) pointed at `https://api.deepseek.com`. The Node.js examples use the same SDK. If your code already calls OpenAI's API, the migration is a one-line base URL change.

---

## 1. Before You Start: What You Need

You need three things and about fifteen minutes. Of course, there is also the option of not building at all — tools like [Floatboat DeepSeek Agent](https://deepseek-agent.com) ship the agent loop, tool wiring, and a desktop workspace preconfigured, so you skip straight to using the agent rather than engineering one. This tutorial covers the DIY path for those who want full control over the tool surface or are building agents for domain-specific tasks that off-the-shelf clients do not cover.

A Python environment — Python 3.10 or later with `pip` installed, or Node.js 18 or later. The OpenAI SDK (`pip install openai` or `npm install openai`) handles the API communication. DeepSeek's API is fully OpenAI-compatible at the wire level, so no specialized SDK is required.

A terminal and a text editor. The agent loop examples in this tutorial are under fifty lines each. You can type them into a single file and run it from the command line. If you want to see the full picture before building, [What Is a DeepSeek Agent](/blog/what-is-deepseek-agent) maps out the four archetypes and helps you decide whether you even need a custom agent or should use an existing tool.

A DeepSeek API key. The next section walks through getting one. If you already have a key, skip to Step 2.

---

## 2. Step 1: Get Your DeepSeek API Key

Go to [platform.deepseek.com](https://platform.deepseek.com) and sign up. After logging in, navigate to the API Keys section and create a new key. DeepSeek requires a minimum top-up before the key becomes active — typically $5 to $10, which is enough for tens of thousands of agent turns at V4 Flash pricing.

Store the key as an environment variable. Do not hard-code it in your source files.

```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```

On Windows PowerShell, use `$env:DEEPSEEK_API_KEY="sk-your-key-here"`.

Once the key is set, verify it works with a minimal chat completion. This call confirms your key is active and the API is reachable — it also tells you which model names are current, which matters because the old aliases are gone.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello. Confirm you are DeepSeek V4."}],
)

print(response.choices[0].message.content)
```

If you see a response identifying itself as DeepSeek V4, the key works. If you get an authentication error, double-check that your account has an active top-up — an empty balance returns a 401 even if the key is valid.

A warning about legacy model names: as of July 24, 2026, `deepseek-chat` and `deepseek-reasoner` are inaccessible. If your code references either alias, replace them with `deepseek-v4-flash` (with thinking mode explicitly enabled or disabled via the API parameter). Applications that still use the old names will receive errors, as documented in [DeepSeek's API documentation](https://api-docs.deepseek.com).

---

## 3. Step 2: Choose Your Model — V4 Pro or V4 Flash

DeepSeek offers two models through the API, and the choice matters for agent performance and cost.

| | V4 Pro | V4 Flash |
|---|--------|----------|
| **Architecture** | 1.6T total / 49B active (MoE) | 284B total / 13B active (MoE) |
| **Context window** | 1M tokens | 1M tokens |
| **Input price (cache miss)** | $0.435 / 1M tokens | $0.14 / 1M tokens |
| **Output price** | $0.87 / 1M tokens | $0.28 / 1M tokens |
| **Speed** | ~45 tok/s | ~120 tok/s |
| **Best for** | Complex multi-step planning, code refactoring, reasoning-heavy agent loops | High-volume tool calls, classification, routing, simple debugging |

For an agent that makes dozens or hundreds of API calls per task, the price gap compounds quickly. A single agent run that burns 80,000 input tokens and 20,000 output tokens costs roughly $0.052 on V4 Pro and $0.017 on V4 Flash. Five thousand such tasks per month: $260 versus $85, as priced on [DeepSeek's pricing page](https://api-docs.deepseek.com/quick_start/pricing).

The practical rule that has emerged from developer discussions in mid-2026: default to V4 Flash for the agent loop, and promote individual turns to V4 Pro when the model's response quality matters — typically the planning step at the start of a task and the synthesis step at the end. The two models share the same API surface, so the promotion is a single-line model name change.

The code examples in this tutorial use `deepseek-v4-flash` as the default and annotate where upgrading to Pro is recommended.

---

## 4. Step 3: Write Your First Agent Loop

This is the section most tutorials skip. They show you how to define a tool and get a tool call back — and then stop. But a single tool call is not an agent. An agent runs a loop: the model requests a tool, your code executes it, the result goes back into the conversation, and the model decides the next action. This section builds that loop from scratch.

Start with a simple weather agent. The model will decide when to call `get_weather`, your code will run it (or simulate running it), and the loop will continue until the model produces a final answer.

```python
import os, json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

# Define tools the agent can call
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"],
        },
    },
}]

# Simulated tool — in production, call a real weather API
def get_weather(city: str) -> str:
    weather_data = {
        "beijing": "Sunny, 28°C",
        "london": "Cloudy, 15°C",
        "tokyo": "Rainy, 22°C",
    }
    return weather_data.get(city.lower(), f"No data for {city}")

def run_agent(user_message: str, max_turns: int = 5) -> str:
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )
        assistant_msg = response.choices[0].message

        # No tool call → final answer
        if not assistant_msg.tool_calls:
            return assistant_msg.content

        # Append assistant message (with tool_calls) to history
        messages.append({
            "role": "assistant",
            "content": assistant_msg.content,
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": tc.type,
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in assistant_msg.tool_calls
            ],
        })

        # Execute each tool call and feed results back
        for tc in assistant_msg.tool_calls:
            args = json.loads(tc.function.arguments)
            result = get_weather(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })

    return "Agent reached max turns without final answer."

# Run it
print(run_agent("What's the weather in Beijing and London?"))
```

The loop logic, line by line:

1. **Send the user message** with the tools definitions attached. The model sees the query and decides whether to answer directly or call a tool.
2. **Check for tool calls.** If `tool_calls` is empty, the model produced a final answer — the loop exits.
3. **Append the assistant message** to the conversation history. This is critical: you must preserve the `tool_calls` array exactly as the model returned it, including the `id` fields. The `tool_call_id` in the next step must match.
4. **Execute the tool** in your local code — in this case, `get_weather` with the city argument the model chose. In production, this is where you call your database, file system, external API, or shell command.
5. **Append the tool result** as a `role: "tool"` message with the matching `tool_call_id`. The model uses this ID to associate the result with the correct tool call.
6. **Loop back** to step 1. The model now sees the full history — user question, its own tool call, and the tool's response — and decides the next action.

The `max_turns` parameter is a safety net for production. Agent loops can get stuck if the model repeatedly calls a tool that always returns the same answer, or if the task requires more turns than practical. Five turns is usually enough for simple tasks; coding agents frequently run 20+ turns. Always bound your loop.

For Node.js, the pattern is identical. Replace the Python client setup:

```javascript
import OpenAI from "openai";
import process from "node:process";

const client = new OpenAI({
    apiKey: process.env.DEEPSEEK_API_KEY,
    baseURL: "https://api.deepseek.com",
});
```

The rest of the loop — tools definition, `tool_calls` inspection, tool execution, result feeding — follows the same shape. The OpenAI SDK handles the wire format identically across languages because DeepSeek's API is OpenAI-compatible at every level.

A note on model choice within the loop: if your task requires planning (the model needs to think about which tools to call in which order), swap `deepseek-v4-flash` for `deepseek-v4-pro` on the first call. Once the plan is established, the subsequent tool execution and synthesis turns can stay on Flash. The model name is a string — you can change it per turn.

Once your agent loop is solid, the next step is refining how it calls tools — [DeepSeek Agent Function Calling](/blog/deepseek-agent-function-calling) covers strict mode, 128 parallel calls, and MCP integration for scaling beyond a single-tool agent.

---

## 5. Adding Thinking Mode: When Reasoning Matters

DeepSeek V4 supports a thinking mode that reveals the model's chain-of-thought reasoning before it produces a tool call or final answer. This is useful when the task requires multi-step planning or reasoning through contradictory constraints.

Enable thinking mode by passing `extra_body` with the `thinking` parameter:

```python
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=messages,
    tools=tools,
    extra_body={
        "thinking": {"type": "enabled"},
        "reasoning_effort": "high",
    },
)
```

Three `reasoning_effort` levels are available:

| Level | Description | When to use |
|-------|-------------|-------------|
| **low** | Minimal chain-of-thought, fast | Simple classification, single-tool calls |
| **high** | Full reasoning, balanced speed | Multi-step planning, code review |
| **max** | Maximum reasoning depth | Complex refactors, debugging subtle logic errors |

When thinking mode is enabled, the model returns its reasoning in a `reasoning_content` field on the message object — separate from the final `content` that the user sees. You do not need to parse or act on this field; it is diagnostic, not functional. In an agent loop, the reasoning is automatically included in the message history and the model uses it to inform the next turn.

The cost trade-off: thinking mode consumes additional output tokens for the reasoning chain, and those tokens are billed at the same rate as regular output. A `reasoning_effort: "high"` call might produce 500 extra reasoning tokens before the final 100-token answer — that is an additional $0.00014 on V4 Flash or $0.00044 on V4 Pro. For agent loops that run hundreds of turns, enable thinking only on the planning turns where the reasoning adds measurable value. The rest of the loop — executing tools, processing results — does not benefit from chain-of-thought.

One common gotcha: if you are using strict mode (`"strict": true` on your function definitions via the `/beta` endpoint), thinking mode must use `"type": "enabled"` (not `"type": "thinking"`). The parameter changed between V3 and V4, and older tutorials may reference the deprecated format, as documented in [DeepSeek's function calling guide](https://api-docs.deepseek.com/guides/function_calling).

---

## 6. From Demo to Production: Error Handling and Repair

The weather agent works because the model always returns valid JSON arguments for a function with a single string parameter. Production agents are messier. The model can hallucinate parameter names, pass the wrong type, or call tools that do not exist. A production-grade agent loop needs a repair layer.

**Validate tool arguments before execution.** Treat the model's output as untrusted user input — because in an agent architecture, that is exactly what it is.

```python
def safe_execute_tool(tool_call):
    function_name = tool_call.function.name
    try:
        args = json.loads(tool_call.function.arguments)
    except json.JSONDecodeError:
        return json.dumps({
            "error": f"Invalid JSON arguments: {tool_call.function.arguments}"
        })

    if function_name not in TOOL_REGISTRY:
        return json.dumps({
            "error": f"Unknown tool: {function_name}. Available: {list(TOOL_REGISTRY.keys())}"
        })

    try:
        result = TOOL_REGISTRY[function_name](**args)
        return json.dumps({"result": result})
    except TypeError as e:
        return json.dumps({
            "error": f"Invalid arguments for {function_name}: {str(e)}",
            "expected": get_tool_signature(function_name),
        })
```

The critical insight: when you return an error message formatted as JSON, the model reads it and often corrects itself on the next turn. This self-correction pattern works reliably on V4 models — far more reliably than on V3 — because the model can parse structured error feedback and adjust its tool call accordingly.

**Watch your context budget.** Every tool call result appends tokens to the message history. The 1M context window is generous, but a coding agent running 50+ turns with large file content in tool results can still approach the limit. If your agent needs to process large documents or entire repositories, implement a summarization step — periodically ask the model to compress the conversation history into a concise state summary, then continue the loop from that summary.

**Add rate limiting.** DeepSeek's API does not hard-throttle requests, but sending hundreds of `tool_choice: "auto"` calls per second can trigger transient errors. A simple exponential backoff wrapper around the API call covers most production scenarios:

```python
import time

def call_with_backoff(messages, tools, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="deepseek-v4-flash",
                messages=messages,
                tools=tools,
                tool_choice="auto",
            )
        except Exception as e:
            if "rate" in str(e).lower() and attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise
```

---

## Conclusion

You just built a DeepSeek Agent. Not a chatbot — an agent. The difference is the loop: the model does not just answer your question, it decides what information it needs, requests it through tool calls, and uses the results to determine the next step. The loop pattern you implemented here — define tools, inspect tool calls, execute, feed back, repeat — is the same architecture that powers DeepSeek-TUI's coding agent and Reasonix's cache-first assistant.

The weather agent is a toy. But the pattern scales. Swap `get_weather` for `search_codebase`, `run_tests`, `query_database`, `read_file`, `write_file`, or `create_calendar_event` — and the same fifty-line loop becomes a coding agent, a data analysis agent, or a scheduling agent. The tool definitions change; the loop architecture does not.

---

## FAQ

### Why build a custom agent instead of using DeepSeek-TUI or Reasonix?

DeepSeek-TUI and Reasonix are excellent terminal coding agents, but they are purpose-built for developer workflows. If your agent needs to do something other than edit code — query a proprietary database, interact with internal APIs, automate a business process — a custom agent loop gives you complete control over the tool surface. The loop pattern in this tutorial is the foundation for any domain-specific agent. If you are weighing the cost and capability trade-offs between coding with DeepSeek versus staying with Claude Code, [DeepSeek Agent vs Claude Code](/blog/deepseek-agent-vs-claude-code) covers that comparison in detail.

### Can I use DeepSeek with LangChain or LangGraph?

Yes. Both frameworks support DeepSeek as a drop-in OpenAI-compatible provider. Set `OPENAI_API_BASE=https://api.deepseek.com` and `OPENAI_API_KEY=your-deepseek-key` in the environment, then use the standard `ChatOpenAI` class with `model="deepseek-v4-pro"`. The agent loop pattern described in this tutorial is what LangChain's `AgentExecutor` does under the hood — understanding the raw loop helps when LangChain's abstractions break, which they do.

### What happens if the model calls a tool that doesn't exist?

The repair pattern in §6 catches this. Return a structured error — `{"error": "Unknown tool: X. Available: [list]"}` — and the model will typically correct itself on the next turn. V4 models are significantly better at self-correction than V3, but you should still validate every tool call before executing it.

### How much will this cost in production?

Back-of-envelope: a typical agent task uses 5–15 turns. At V4 Flash pricing ($0.14/M in, $0.28/M out), a task averaging 10 turns with 2,000 input tokens and 500 output tokens per turn costs roughly $0.004 — less than half a cent. A thousand such tasks per month: $4. At V4 Pro pricing: roughly $0.013 per task, or $13 for a thousand. The economics are favorable enough that the main cost concern is not the API bill but the engineering time spent tuning the agent loop.

### What exactly is the agent loop?

The agent loop is what separates an agent from a chatbot. You send the user message with tool definitions attached; the model either answers directly or returns a tool call; your code executes that call; you append the result as a `role: "tool"` message with the matching `tool_call_id`; and you send the full history back for the model to decide the next step. The loop repeats until the model produces a final answer — bounded by a `max_turns` safety net in production.

### Should I use V4 Pro or V4 Flash for my agent?

Default to V4 Flash for the agent loop — at $0.14/M input and $0.28/M output, the cost compounds favorably across dozens of calls per task. Promote individual turns to V4 Pro when response quality matters most: the planning step at the start of a task and the synthesis step at the end. The two models share the same API surface, so promotion is a one-line model name change, and it can save 60–70% on a typical multi-turn agent run.
