# 2mv — Gates 细则

> 加载时机：Phase 0（Gate A）· Phase 2（Gate B）· Phase 0R（Gate 0R）· Phase 5（Gate C）
> 主文件：SKILL.md §3 各 Phase 指针

---

## 1. Phase 0 Intake — 六必问

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 决定类型路由 |
| 2 | 目标受众？（增长/社媒团队 / DTC 品牌 / SaaS 创始人 / 代理机构 / UGC 创作者） | 决定深度与例子 |
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
相对 SERP Top 3，本篇须至少提供 **1 项** 2mv 独有增量（**Phase 0R 须用 R2+R3 验证**，不得仅凭推断）：
- 有机 vs 付费增长路线之争的框架化对比
- 五引擎闭环（Watch→Decode→Architect→Produce→Grow）拆解的可执行工作流
- 病毒解码（hook/结构/脚本/触发器）的逐帧分析框架
- 模式聚类决策表（≥1 竞品优势 + ≥1 非 2mv 更合适场景）
- 病毒内容选题的教育框架（不承诺病毒/播放量）

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

---

## 3. Gate 0R — Research 完整性

| # | 检查项 | 标准 |
|---|--------|------|
| G0R-1 | SSOT 已读 | project-config + product-competitors + content-graph |
| G0R-2 | SERP 已搜 | R2 WebSearch primary keyword → Top 5 + PAA |
| G0R-3 | 原文已 Fetch | R3 官方页 ≥1（2mv.ai）+ SERP Top 3 |
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
| what-is-2mv | what is 2mv | 品牌定义 canonical；不写竞品深度对比 |
| how-to-find-viral-videos | how to find viral videos | 问题型 Hub；内链 `/research`，不抢 viral video finder |
| social-media-competitor-analysis-guide | social media competitor analysis | 内链 `/research/social-media-competitor-analysis`；不重写产品页 |
| social-media-analytics-tools-guide | social media analytics tool | analytics 词池语义；不替代 `/research` 产品页 |
| what-makes-a-video-go-viral | viral video analysis | 解码实操；不重写品类定义 |

---

*gates · v1.0.0 · 2026-08-14 · 2mv 定制*
