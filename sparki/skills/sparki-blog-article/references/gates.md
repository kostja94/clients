# Sparki — Gates 细则

> 加载时机：Phase 0（Gate A）· Phase 2（Gate B）· Phase 0R（Gate 0R）· Phase 5（Gate C）
> 主文件：SKILL.md §3 各 Phase 指针

---

## 1. Phase 0 Intake — 六必问

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 决定类型路由 |
| 2 | 目标受众？（普通创作者 / 内容团队 / 品牌 MCN / 播客团队） | 决定深度与例子 |
| 3 | 发布目的？SEO / 品牌 / 转化 | 决定产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 判断信息增量 |
| 5 | 文中内链页面是否已上线（project-config §2 白名单）？ | G6 预检 |
| 6 | CreatorClone：红人 + ≥2 公开素材 URL？ | 决定能否写素材级拆解 |

用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

---

## 2. Gate A — KEEP/MERGE 判定

**三条件满足 ≥2 → KEEP**；否则 **MERGE** 或 **STOP**。

| 条件 | 判断方法 |
|------|---------|
| 搜索意图独立 | 与 content-graph.md 既有文章关键词重叠 ≤50% |
| 读者阶段不同 | Awareness / Consideration / Evaluation / Activation 不重叠 |
| 内容深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**信息增量 Gate**（KEEP 后预检）：
相对 SERP Top 3，本篇须至少提供 **1 项** Sparki/本仓独有增量（**Phase 0R 须用 R2+R3 验证**）：
- 素材级拆解观察（CreatorClone：切点/转场/字幕节奏）
- 原创决策框架 / 对照表（何种工作流用工具 vs 手动 vs Agent）
- 一手工作流步骤（非复述 SERP 列表）
- 功能边界澄清（某功能能/不能做什么的真相）

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

---

## 3. Gate 0R — Research 完整性

| # | 检查项 | 标准 |
|---|--------|------|
| G0R-1 | SSOT 已读 | project-config + product-competitors + content-graph |
| G0R-2 | SERP 已搜 | R2 WebSearch primary keyword → Top 5 + PAA |
| G0R-3 | 原文已 Fetch | R3 官方页（sparki.io 相关功能页）+ SERP Top 3；CreatorClone 另抓红人公开素材 ≥2 |
| G0R-4 | Synthesis 已填 | 三要素完整（SERP 未说 + 一句话论点 + 读者改变） |
| G0R-5 | IG 三问 | 核心 claim 独有、删文减少信息、前 30% 可独立成段 |
| G0R-6 | 无未验证 P0 claim | Degraded 模式不写 P0 claim；CreatorClone 无素材则不写切点断言 |

**Gate 0R 阻断**：R2 未搜 / R3 未 Fetch / 无 Synthesis / 事实不可验证且需写 P0 claim / CreatorClone 无素材证据 → 回退补 R2/R3 或 STOP。

---

## 4. Gate B — Slug 6-Point Check

> 细则见 `references/slug-gate.md`

| # | 检查项 | 标准 |
|---|--------|------|
| 1 | 常青 | 无年份、版本号 |
| 2 | Intent-first | 含 primary keyword 核心词 |
| 3 | 可读 | 通过"大声读"测试 |
| 4 | 语义余量 | 描述主题非观点；30% 内容变化后仍适用 |
| 5 | 无禁词 | 不含 guide/complete/ultimate/diagnosis/年份 |
| 6 | 长度合规 | 4–9 词，≤60 字符 |

**额外硬性（sparki）**：文件名 = slug（无 NN）；不与 content-graph 61 篇 slug 混淆。
6 项 + 额外全 Pass → 继续；任一 Fail → 重选 slug。

**Gate B 附加**：确定 `date`（发布日 UTC），对照 content-graph.md 日期占用，每自然日 ≤1 篇。

---

## 5. Gate C — SelfCheck 通过标准

**H0–H4 Hard Gates + 12 维 Pass/Fail 全部 Pass → audit-ready。**

> 细则见 `references/selfcheck.md`

---

## 6. 关键词冲突快查（示例）

| 建议 slug | 主关键词 | 边界 |
|-----------|---------|------|
| 任一 "edit like {creator}" | 红人风格 | 新红人/新 format 才 KEEP；对照 2A |
| 长改短新变体 | long to short | 引用 canonical `long-video-to-short-video`，聚焦新源类型 |

完整冲突见 `content-graph.md` §6。

---

*gates · sparki v1.0.0 · 2026-09-04*
