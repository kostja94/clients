# Agentic Payments Protocol — Web Deep Search Index

> 检索基准日：2026-08-24 · 规范：`web-deep-search-spec.md` v1.3  
> 5 篇 definition 成稿：`clink/blog/agentic-payments/`（26–29, 33）  
> **2026-08-24 同步**：五篇成稿已吸收 subagent 增量事实（ACP 2026-03 pivot 等）

| 协议 | 成稿 | subagent | Loop | 报告状态 |
|------|------|----------|------|----------|
| AP2 | 26-what-is-ap2-agent-payments-protocol.md | [Web deep search AP2](036cd904-6a1d-4f8c-8324-555eaa4ddc14) | 7 | ✅ 已吸收：SD-JWT、VI、FIDO 双 TWG、五角色 |
| x402 | 27-what-is-x402.md | [Web deep search x402](26e030a3-7e5c-496e-abe7-e23ff5d39bfc) | 6 | ✅ 已吸收：V2 headers、100M+ 笔数 caveat、AgentCore GA |
| MPP | 28-what-is-machine-payments-protocol.md | [Web deep search MPP](1b56dbc4-29c3-4afc-9b1b-8d9142f68284) | 6 | ✅ 已吸收：session intent、SPT 最低额、mppx validate |
| ACP | 29-what-is-agentic-commerce-protocol.md | [Web deep search ACP](e3f2dbe8-a762-4d8d-a570-148e22785a69) | 7 | ✅ 已吸收：2026-03 discovery pivot、12–30 Shopify live |
| UCP | 33-what-is-universal-commerce-protocol.md | [Web deep search UCP](0cf0d284-7bbf-492c-ba6e-cb6afc624b5c) | 6 | ✅ 已吸收：Tech Council 扩员、Native vs ECP、Google waitlist |

## 栈关系（五 agent 共识）

```
Commerce:  UCP (Google/Shopify) · ACP (OpenAI/Stripe)
Transport: x402 (LF Foundation) · MPP (Stripe/Tempo)
Trust:     AP2 + Verifiable Intent (FIDO Alliance)
```

## 关键增量（subagent → 成稿）

| 主题 | 增量 | 来源 agent |
|------|------|-----------|
| ACP | Instant Checkout 2026-03 deprioritize；discovery-first | ACP |
| ACP | Shopify pipeline 1M+ vs ~12–30 in-chat live | ACP |
| AP2 | Intent/Cart → Checkout/Payment Open/Closed；SD-JWT | AP2 |
| x402 | V2 头字段；CoinDesk 采用质疑 | x402 |
| MPP | session intent + Metronome；subscription intent 未 GA | MPP |
| UCP | 2026-04 Tech Council + Amazon/Meta/MSFT | UCP |

## 完整报告

完整 §3 结构报告见各 subagent 会话输出（transcript JSONL）。如需独立 markdown 归档，可从 subagent 最终 response 导出至本目录 `{slug}-web-search-2026-08-24.md`。
