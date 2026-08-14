# §2 文章类型路由

收到任务后**先匹配类型**，再跳转对应 H2 模板。

## 2.1 路由表

| 类型 | 典型 intent | 词数 | 产品提及上限 | 参考 slug |
|------|------------|------|-------------|-----------|
| **Technical Deep Dive** | 技术原理 / 架构解析 | 2500–4000 | ≤25% | `mcp-qveris` |
| **Field Test & Audit** | 实测 / 计费审计 | 2500–3800 | ≤35% | `ai-finance-agent-cost-audit` |
| **Workflow Guide** | 教程 / 集成步骤 | 2200–3500 | ≤40% | `qveris-in-cursor` |
| **Market Analysis** | 市场 / 事件点评 | 2000–3000 | ≤20% | `a-share-realtime-quotes-agent` |
| **Comparison** | 对比 / 替代选型 | 2500–3500 | ≤45% | `openclaw-vs-hermes` |
| **Product Story** | 产品 / 生态叙事 | 2000–3200 | ≤45% | `qveris-fmp-60` |

**路由规则**：

- `how it works` / 架构 / 原理 / 协议 → **TechnicalDeepDive**
- `field test` / `audit` / 计费实测 / `I tested` → **FieldTest**
- `how to` / `guide` / 集成 / `set up` → **WorkflowGuide**
- `market` / `stock` / 行情 / 事件点评 → **MarketAnalysis**
- `vs` / `alternative` / `compared` / 选型 → **Comparison**
- `product update` / 生态 / 案例 / `what is qveris` → **ProductStory**

**产品提及上限**：文中直接出现 QVeris（含 CLI/MCP/SDK 引用）的正文占比。超出上限 → 降为更克制类型或缩减。

## 2.2 全类型通用模块（QVeris 成稿惯例）

| 模块 | 要求 |
|------|------|
| **frontmatter** | 完整 Schema 见 `frontmatter-schema.md`；仅 7 字段（slug/metaTitle/description/author/publishedAt/updatedAt/readTime） |
| **TL;DR** | **正文** excerpt 后的 `## TL;DR` H2 区块：3–5 条 `- **label** — body` bullet；首条 "Fast answer" BLUF ≥40 字符；不进 frontmatter；无内链 |
| **发布日期** | `publishedAt` 全库唯一；一天一篇；新稿 = 当前最晚日期 +1 天（见 `content-graph.md`） |
| **H2** | 英文描述性标题；**不编号**（推荐，对齐多数官网文如 mcp-qveris）；编号 `## 1.`… 亦可接受（01 已发稿用编号，见 4.1） |
| **Conclusion / FAQ** | **建议**（SEO 最佳实践）但非强制：QVeris CMS 通过 frontmatter `tocExtra` 渲染 FAQ；正文末节缺 Conclusion/FAQ 不算 Fail（工具标 WARN）。两者皆有时用 `## Conclusion` → `## Frequently asked questions` 收尾 |
| **内链** | 正文 ≥2 其他 blog slug；guides/docs 按语境；**自然优先**；同 slug 同篇 ≤2 次；TL;DR/FAQ 无内链；禁 G6 |
| **外链** | 权威 2–8；竞品/数据源 `rel="nofollow noopener"` HTML |
| **列表比例** | TechnicalDeepDive ≤20%；MarketAnalysis ≤25%；其余 ≤30% |
| **表格预算** | Comparison/Technical ≤3 张；Field Test/Benchmark ≤5 张（优先合并同构表、删冗余表）；每张表前后 ≥2 句分析 |
| **长段落** | ≥3 段 4–8 句（80–200 words）；避免连续 3+ 短段簇 |
| **CTA** | 单一主行动（/plugins 或 /cli 或 /pricing）；全文 ≤2 次；正文内链承担导流 |
| **无 Related** | QVeris 博客不用 `## Related articles` 模块（内链分布在正文） |

**结构顺序（全类型）**：frontmatter → 正文 `# H1` title → `*excerpt*` → `## TL;DR`（3–5 bullets）→ 正文 H2… → `## Conclusion` → `## Frequently asked questions`

## 2.3 Technical Deep Dive — H2 模板

**叙事弧线**：问题背景 → 概念拆解（分层/分机制）→ 工程细节 → 与既有方案的对比 → QVeris 的定位（克制）→ 结论。

参考样板：`mcp-qveris`（四层问题拆解 + QVeris 解决什么）

```
{首段：问题定位，不用 Lead 段标题}
## What {topic} actually means in {year}
## The real problem behind {topic}
   ### Layer/Part 1: …
   ### Layer/Part 2: …
## {N} engineering details that change the outcome
## Why a unified capability layer matters here   ← QVeris 出现（克制，≤25%）
## What QVeris is solving
## Conclusion
## Frequently asked questions
```

**专属要求**：核心机制必须用原文语言定义（如 Discover→Inspect→Probe→Call 协议）；每个 Layer 配 ≥1 具体场景；禁"空谈概念"。

## 2.4 Field Test & Audit — H2 模板

**叙事弧线**：问题（成本/效率痛点）→ 实测设计 → 数据呈现（表）→ 结果解读 → 隐藏成本 → 局限。

参考样板：`ai-finance-agent-cost-audit`

```
{首段：一个具体痛点故事/数字钩子}
## The {N}-vendor problem: what a self-built data layer costs
## Test design: {tools/methods}, n≈{X}, window {date–date}
## Field results: {measurements}
   ### Real-time quotes: {sources}, {N} credits
   ### Historical + fundamentals: about {N} credits
   ### {Category}: empty result, {N} credits
## The math: {outcome} vs commercial APIs
## Three hidden costs nobody quotes
## How it works: {dialogue/workflow walkthrough}
## Limits
## Conclusion
## Frequently asked questions
```

**专属要求**（F3 强制）：实测必须含方法（调用数、时间窗、数据源）+ "QVeris Data Test" 标注 + 空返回/异常如实呈现。数字表格须先于解读出现。

## 2.5 Workflow Guide — H2 模板

**叙事弧线**：目标 → 前置条件 → 分步（代码/命令）→ 验证 → 生产化 → 备选方案。

参考样板：`qveris-in-cursor`、`qveris-hosted-mcp-coding-agent-guide`

```
{首段：读者将从本文得到什么}
## What you'll build
## Prerequisites: {account/API key/环境}
## Step 1: {install/configure}
## Step 2: {discover + inspect}
## Step 3: {call + verify}
## Going further: {codegen / probe / usage audit}
## Alternatives: {MCP vs CLI vs SDK 按环境选择}
## Conclusion
## Frequently asked questions
```

**专属要求**：命令/代码必须来自官方 docs（`/docs/{slug}`）；每个 Step 配预期输出；涉及版本号须标注（如 CLI v0.10.0）。

## 2.6 Market Analysis — H2 模板

**叙事弧线**：事件/现象 → 数据佐证（表）→ 多空解读 → Agent/数据工具视角。

参考样板：`a-share-realtime-quotes-agent`、`ai-tech-stock-selloff`

```
{首段：事件 + 数据钩子}
## What happened: {event} in numbers
## Reading the data layer
   ### {Dimension 1}: …
   ### {Dimension 2}: …
## What the market is pricing in
## Why agents change how you watch {segment}   ← QVeris 出现（≤20%，克制）
## Conclusion
## Frequently asked questions
```

**专属要求**（F1/F2 强制）：所有价格/涨跌数据带 `as of {date}` + 来源；不加投资建议；QVeris 出现占比最低（≤20%）。

## 2.7 Comparison — H2 模板

**叙事弧线**：选型问题 → 对比维度表 → 逐维度分析 → 按用例推荐 → 公平收尾。

参考样板：`openclaw-vs-hermes`、`fmp-vs-alpha-vantage` 系列

```
{首段：为什么这个对比值得做}
## {A} vs {B}: what each actually is
## Comparison table: {维度 × A/B/QVeris}
## Dimension 1: {接入方式/数据广度/成本…}
## Dimension 2: …
## Which fits your {workload/use case}
## When neither is the right choice
## Conclusion
## Frequently asked questions
```

**专属要求**（G7）：每竞品 ≥1 优势；对比表 ≤3 张且表后 ≥2 句分析；QVeris 出现 ≤45% 且必须公平。

## 2.8 Product Story — H2 模板

**叙事弧线**：背景 → 能力 → 场景 → 结果 → 生态。

参考样板：`qveris-fmp-60`、`qveris-ai-options-assistant`

```
{首段：故事钩子}
## The problem that led here
## What {capability/partnership} brings
## A real workflow: {场景走查}
## What changed for {user type}
## Where this fits in the ecosystem
## Conclusion
## Frequently asked questions
```

**专属要求**：产品 claim 必须可核实（官网/docs）；不得夸大（G5）。

## 2.9 Who / How / Why（FieldTest / MarketAnalysis 强制）

| 模块 | 内容 |
|------|------|
| **Who** | 作者/团队语境（如 "Two weeks ago, I went through our team's AI agent API bill."） |
| **How** | 研究方法（调用数、时间窗、数据源、方法限定） |
| **Why** | 帮读者做决策（选型、成本判断），非推销 QVeris |

## 2.10 产品提及样例

```
✅ 克制：QVeris is a capability routing network — one unified protocol for discovering and calling tens of thousands of real-time data tools.
✅ 公平：Commercial APIs have this trap too: call an endpoint intraday that only updates after market close, and empty returns are still billed.
❌ 夸大：QVeris is the only platform that can do this. / QVeris is the best in the world.
❌ 投资建议：Seres is a good buy right now.
```
