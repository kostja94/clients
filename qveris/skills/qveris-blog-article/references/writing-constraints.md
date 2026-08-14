# §11 表现形式与表达节奏

> 对齐官网已发博客（`mcp-qveris`、`ai-finance-agent-cost-audit`）的行文风格。

## Voice 正向（五正向）

1. **具体**：给数字、名字、时间、来源（`Seres 601127`、`194ms, 1 credit`）
2. **诚实**：呈现数据与事实，不粉饰（空返回如实写："7.2 credits bought an empty JSON"）
3. **克制**：QVeris 出现靠后且克制；不喊口号（"Every capability, one call away" 仅首页定位可用，正文少用）
4. **专业**：术语准确（Discover→Inspect→Probe→Call 协议名；credits 计费单位）
5. **结构化**：长段落 + 表格 + 短句穿插，避免碎片化

## 禁词 / 空泛表述

| 禁 | 替代 |
|----|------|
| "game-changing" / "revolutionary" | 具体指标（"cuts prompt-token overhead by up to 80%"） |
| "best in the world" | 限定语（"the most generous recurring budget in this list"） |
| "studies show" | 具体来源（"per the provider's official pricing page"） |
| "imagine you're…" | 直接进入场景 |
| 过度感叹号 | 陈述句 |
| "seamless" / "powerful" / "robust" | 删除或换具体描述 |

## 段落与列表节奏

| 项 | 标准 |
|----|------|
| 长段落 | ≥3 段（每段 4–8 句 / 80–200 words） |
| 短段集群 | 禁止连续 3+ 短段（≤2 句） |
| 列表占比 | TechnicalDeepDive ≤20%；MarketAnalysis ≤25%；其余 ≤30% |
| 表格 | Comparison/Technical ≤3 张；**Field Test/Benchmark 类 ≤5 张**（数据密集型豁免，但需优先合并同构表、删冗余表）；每张表前后 ≥2 句分析；禁止"裸表" |
| 代码块 | 只放可运行的命令/代码；标注语言；短块优先 |

## BLUF 三处

| # | 位置 | 要求 |
|---|------|------|
| B1 | 正文 `## TL;DR` 区块第 1 条 | 60–110 词，直接回答 primary intent |
| B2 | 每个 major H2 首段 | 段首一句给本节结论 |
| B3 | FAQ 每问首句 | 直接给答案再展开 |

## 数字与引用格式

- 金额：`$19/月`、`RMB 6,000`（中文语境保留 RMB）
- credits：`1–100 credits/次`、`28 credits`
- 时间：`as of {month} {day}, {year}`（金融数据强制）
- 引用：`[Source: URL]` 或脚注；站外 `rel="nofollow noopener"`
- 版本：`CLI v0.10.0`、`@qverisai/mcp v0.13.0`（用 §6.1 产品事实表）

## 金融数据呈现

- 行情表格：`| 数据点 | 值 | 来源 | 时间 |`
- 实测结果：标注 n + 时间窗 + 数据源（F3）
