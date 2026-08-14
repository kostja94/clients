# VOMO — Gates 细则

> 加载时机：Phase 0（Gate A）· Phase 2（Gate B）· Phase 0R（Gate 0R）· Phase 5（Gate C）
> 主文件：SKILL.md §3 各 Phase 指针

---

## 1. Phase 0 Intake — 五必问

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 决定类型路由 |
| 2 | 目标受众？（知识工作者 / 销售 / 创作者 / 学生 / 专业人士） | 决定深度与例子 |
| 3 | 发布目的？SEO / 品牌 / 转化 / 社区 | 决定产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 判断信息增量 |
| 5 | 文中内链指向的页面是否已上线？（G6 预检 + Tools 主链） | 内链规划 |

用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

---

## 2. Gate A — KEEP/MERGE 判定

**三条件满足 ≥2 → KEEP**；否则 **MERGE** 或 **STOP**。

| 条件 | 判断方法 |
|------|---------|
| 搜索意图独立 | 与 content-graph.md 已有文章关键词重叠 ≤50% |
| 读者阶段不同 | Awareness / Consideration / Evaluation / Activation 不重叠 |
| 内容深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**信息增量 Gate**（KEEP 后预检）：
相对 SERP Top 3，本篇须至少提供 **1 项** VOMO 独有增量（**Phase 0R 须用 R2+R3 验证**，不得仅凭推断）：
- Bot-free 视角（不加入会议）的转录对比框架
- 双引擎 ASR（Whisper+Nova-2）的准确率叙事（95–99%）
- Ask AI（GPT-4o）对话式查询转录内容的工作流
- VOMO CLI 对接 AI Agent 工作流（Claude Code 等）
- Wirecutter 式对比表（≥1 竞品优势 + ≥1 非 VOMO 更合适场景）

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

---

## 3. Gate 0R — Research 完整性

| # | 检查项 | 标准 |
|---|--------|------|
| G0R-1 | SSOT 已读 | project-config + product-competitors + content-graph |
| G0R-2 | SERP 已搜 | R2 WebSearch primary keyword → Top 5 + PAA |
| G0R-3 | 原文已 Fetch | R3 官方页 ≥1 + SERP Top 3 |
| G0R-4 | Synthesis 已填 | 三要素完整（SERP 未说 + 一句话论点 + 读者改变） |
| G0R-5 | IG 三问 | 核心 claim 独有、删文减少信息、前 30% 可独立成段 |
| G0R-6 | 无未验证 P0 claim | Degraded 模式不写 P0 claim |

**Gate 0R 阻断**：R2 未搜 / R3 未 Fetch / 无 Synthesis / 事实不可验证且需写 P0 claim → 回退补 R2/R3 或 STOP。

---

## 4. Gate B — Slug 6-Point Check

> 细则见 `references/slug-gate.md`

| # | 检查项 | 标准 |
|---|--------|------|
| 1 | 常青 | 无年份、版本号 |
| 2 | Intent-first | 含 primary keyword 核心词 |
| 3 | 可读 | 通过"大声读"测试 |
| 4 | 语义余量 | 描述主题非观点；30% 内容变化后仍适用 |
| 5 | 无禁词 | 不含 framework/strategy/guide/diagnosis/complete/年份 |
| 6 | 长度合规 | 5–8 词，≤60 字符（HowTo 类可 7–8 词保留完整关键词） |

6 项全 Pass → 继续；任一 Fail → 重选 slug。

**Gate B 额外**：确定 publishDate，对照 content-graph.md 已有日期表，每自然日 ≤1 篇。

---

## 5. Gate C — SelfCheck 通过标准

**H0–H4 Hard Gates + 12 维 Pass/Fail 全部 Pass → audit-ready。**

> 细则见 `references/selfcheck.md`

---

## 6. 关键词冲突快查

| slug | 主关键词 | 边界 |
|------|---------|------|
| vomo-vs-otter-ai | VOMO vs Otter, Otter alternative | 横向对比；Otter 功能不全面展开 |
| best-audio-to-text-apps | best audio to text apps | 榜单评测；每工具 ≥1 优势 |
| how-to-convert-audio-to-text | how to convert audio to text | 教程实操；不覆盖竞品选型 |
| how-to-convert-podcast-to-blog-post（本地 #01） | how to convert podcast to blog post | 场景工作流；关键词完整前缀；不覆盖竞品选型 |

> 完整冲突表见 `references/content-graph.md`

---

## 7. 信息增量 Gate 验证要求

- 相对 SERP Top 3，每篇须 ≥1 项 VOMO 独有增量
- 独有增量必须在正文**兑现**（非仅在 Brief 声明）
- Phase 0R 的 R2/R3 须验证增量确实非 SERP 已有
- 增量类型：Bot-free 视角 / 双引擎准确率数据 / Ask AI 工作流 / VOMO CLI / Wirecutter 对比表

---

*gates · v1.0.0 · 2026-08-03*
