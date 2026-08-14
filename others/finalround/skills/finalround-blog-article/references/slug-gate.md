# FinalRound Slug Gate（Skill reference）

> **Slug 6 问 + 12 反模式。** Phase 2 加载。

---

## 1. Slug 设计原则

| 原则 | 说明 |
|------|------|
| **常青** | slug 不含年份（title 可含 `for 2026`） |
| **含主关键词** | 完整核心词优先，可读性其次 |
| **kebab-case** | 全小写 + 连字符；≤60 字符 |
| **语义余量** | 30% 内容变化后 slug 仍合适 |
| **无架构词** | 不含 framework / strategy / diagnosis / guide / complete |
| **大声读测试** | 去掉连字符读出来通顺 → 通过 |

## 2. Slug 6 问（Gate B）

| # | 问题 |
|---|------|
| 1 | 是否含 primary keyword 完整核心词？ |
| 2 | 是否常青（无年份/无数量/无内部架构词）？ |
| 3 | 是否 kebab-case、全小写、≤60 字符？ |
| 4 | 是否有语义余量？ |
| 5 | "大声读"测试通过？ |
| 6 | 与既有文章/官网无冲突？ |

## 3. 12 反模式

| # | 反模式 | 错误示例 | 正确示例 |
|---|--------|---------|---------|
| 1 | 含年份 | whats-new-2026 | whats-new-interview-copilot |
| 2 | 含数量/序数 | top-5-ai-interview-tools | best-ai-interview-tools |
| 3 | 连续重复词 | interview-interview-help | interview-help |
| 4 | 内部架构词 | interview-prep-framework | how-to-prepare-for-interviews |
| 5 | 下划线/大写/空格 | ai_interview_tools | ai-interview-tools |
| 6 | 分类前缀沉积 | 多篇 ai-interview-xxx 开头 | 各篇以搜索词开头 |
| 7 | 与既有 slug 重复 | — | 查 content-graph |
| 8 | >60 字符 | — | ≤60 |
| 9 | 不含主关键词 | — | 含完整核心词 |
| 10 | 人不可读 | — | 大声读通顺 |
| 11 | 缩写模糊 | fr-ai-copilot | finalround-interview-copilot |
| 12 | 非 kebab-case | — | kebab-case |

## 4. 竞品基准检查

搜 Google → 对比前 5 竞品 slug，确保差异定位（Phase 2 步骤 3）。

---

*slug-gate · FinalRound · v1.0.0*
