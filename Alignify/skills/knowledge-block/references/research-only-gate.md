# 仅调研 · 显式成文门槛（Research-Only Gate）

> **版本**：2026-09-02 · 被 [`../SKILL.md`](../SKILL.md) 引用

---

## 1. 适用场景

用户或任务明确要求 **「只调研 / 深度搜索 / 了解是什么」**，且**未**说「写 KB」「写知识块」「写文」「create-article」「更新 agentic-payments」等成稿指令时，启用本门槛。

典型触发语：

- 「调研 XXX 是什么」
- 「按 web-deep-search-spec 搜索…」
- 「Paid 相关场景和产品，只需要调研」
- 「我说写才写」

---

## 2. 允许做的

| 动作 | 说明 |
|------|------|
| 公开网络检索 | 按 `clients/web-deep-search-spec.md` |
| **对话内**输出结构化调研报告 | 执行摘要、产品地图、竞品、场景、链接 |
| 写入 **`clients/temp/`** 临时调研稿 | 文件名 `{topic}-web-search-{YYYY-MM-DD}.md`；**非** KB SSOT |
| **用户点名**更新已有 KB 的缺失条目 | 如「把 Skyfire 补进 agentic-payments」 |

---

## 3. 禁止做的（除非用户显式要求）

| 禁止 | 替代 |
|------|------|
| 新建 `knowledge/tools/{slug}.md` 或 `knowledge/marketing/{slug}.md` | 调研结论留在对话或 `temp/` |
| 新建 `knowledge/*/_briefs/{slug}.md` 发文 Brief | 等用户说「写 KB / 写文」 |
| 调用 create-article 流程写部署仓 `content/` | 等用户确认 slug 与成文 |
| 更新 `knowledge/tools/README.md` / `territory-map.md` 登记**新 slug** | 仅用户要求「建 KB / 注册 slug」时 |
| 把调研报告默认当作 KB 正文粘贴 | KB 须按 `_TEMPLATE` + 分流表重写 |

**显式成文指令示例**（满足后可建 KB / 走 create-article）：

- 「把调研写进知识块 `agent-billing`」
- 「创建 agent-billing KB」
- 「按 create-article 写 /blog/agent-billing」

---

## 4. 与 web-deep-search-spec 的关系

- 调研阶段：**禁止**为「补充背景」读取 `clients/` 下客户业务文档（规范 §0.4）；**允许**读 Alignify **skills** 与**用户点名**的 KB 文件。
- 调研产出默认 **不进** `knowledge/`；用户后续说「写」时，再按 knowledge-block 或 create-article 流程落盘。

---

## 5. Agent 商业化 / 计费（Paid 轴）当前状态

| 项 | 状态 |
|----|------|
| **slug（已定）** | **`agent-billing`** · KB：`knowledge/tools/agent-billing.md` |
| **keywordEn Primary** | **AI agent billing**（Secondary：`AI agent billing software` · `agent monetization`） |
| 与 `agentic-payments` | **分流**：payments = Agent **买方**动钱；agent-billing = Agent **卖方**定价/计费/价值证明 |
| 与 `vibe-coding-payments` | **分流**：后者 = **人类开发者**给 Vibe 产品接 Stripe/Paddle |
| 2026-09-03 | KB 已建；正式 `/blog` 文 **未**写（等用户显式 create-article） |

---

*Alignify knowledge-block · research-only-gate v1.0 · 2026-09-02*
