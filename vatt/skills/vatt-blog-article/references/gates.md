# Vatt — Gates 细则

> 加载时机：Phase 0（Gate A）· Phase 2（Gate B）· Phase 0R（Gate 0R）· Phase 5（Gate C）
> 主文件：SKILL.md §3 各 Phase 指针

---

## 1. Phase 0 Intake — 六必问

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 决定类型路由 |
| 2 | 目标受众？（TikTok reaction 创作者 / YouTube 频道主 / 内容团队 / 新手创作者） | 决定深度与例子 |
| 3 | 发布目的？SEO / 品牌 / 转化 / 社区 | 决定产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 判断信息增量 |
| 5 | 文中内链指向的页面是否已上线？ | G6 预检 |
| 6 | 与已有文章的关系？Pillar 拆文 / 新 Cluster / 竞品拦截 | 确定 hub-spoke 定位 |

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
相对 SERP Top 3，本篇须至少提供 **1 项** Vatt 独有增量（**Phase 0R 须用 R2+R3 验证**，不得仅凭推断）：
- Reaction 真人编辑 vs AI 生成器路线之争的框架化对比
- 官方 11 步任务流拆解的可执行工作流（editable timeline 信任机制）
- Editor-vs-Generator 双路线决策树
- Wirecutter 式对比表（≥1 竞品优势 + ≥1 非 Vatt 更合适场景）
- 版权意识剪辑的教育框架（不承诺 Fair Use）

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

---

## 3. Gate 0R — Research 完整性

| # | 检查项 | 标准 |
|---|--------|------|
| G0R-1 | SSOT 已读 | project-config + product-competitors + content-graph |
| G0R-2 | SERP 已搜 | R2 WebSearch primary keyword → Top 5 + PAA |
| G0R-3 | 原文已 Fetch | R3 官方页 ≥1（vatt.ai）+ SERP Top 3 |
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
| 6 | 长度合规 | 5–8 词，≤60 字符 |

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
| types-of-reaction-videos | reaction video, types of reaction videos | 品类全景 Hub；不深入单类型实操 |
| try-not-to-laugh-reaction-videos | try not to laugh | 具体格式玩法；引用 Hub 定义 |
| how-to-edit-reaction-videos-faster | edit reaction videos faster | 效率工作流；不重复品类定义 |
| ai-reaction-editor-vs-generator | ai reaction editor vs generator | 路线对比 canonical；他文只引用 |

---

*gates · v2.0.0 · 2026-07-06 · vatt 定制 2026-08-14*
