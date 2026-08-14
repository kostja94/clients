# Floatboat Gates — Intake, KEEP/MERGE, Info Gain, Slug

> 加载时机：Phase 0（Gate A）· Phase 1（KEEP/MERGE）· Phase 2/3（Gate B）
> 主文件：SKILL.md §3 Phase 0–3 指针

---

## 1. Phase 0 Intake — 四必问 + 条件必问

### 必问

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent 类型？ | 决定类型路由与客观性标准 |
| 2 | 目标受众 + 技术水平？ | 决定深度及格线 |
| 3 | 发布目的？品牌 / SEO / 转化 / 社区 / 招聘 | 决定产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 判断信息增量 |

### 条件必问

| # | 条件 | 问题 |
|---|------|------|
| 5 | Research 文 | 署名是否用创始人真实姓名（Tan Shaoqing）？ |
| 6 | 文内链产品页 | 列出所有内链 URL，逐一确认可达 |
| 7 | 含量化 claim | 第三方数据是否可验证？ |
| 8 | 系列文 | Hub-spoke 角色（Hub / Spoke / Standalone）？ |

**Phase 0 第一行强制输出**：
```
## Topic Scope: scheduling-agent | floatim | combo-skills
```

---

## 2. Gate A — 信息增量 Gate

**位置**：Phase 0 Step 2 — KEEP 判定后强制执行。

相对 SERP Top 3，本篇须至少满足 **2 项**独有增量，否则 **STOP**：

| # | 增量维度 | 判定 |
|---|---------|------|
| 1 | **独有框架** | 四代 Scheduling / Calendar-as-Runtime 决策表 / 品类定义三属性 等 |
| 2 | **独有对比维度** | 触发模型、事件 workspace 持久性、Combo Skills 复用 等 |
| 3 | **独有可执行 pipeline** | 可复现的 prep / follow-up / workflow 步骤 |
| 4 | **独有受众视角** | Solopreneur / solo founder 特有场景叙事 |
| 5 | **独有生态视角** | Combo Skills / Agent Skills Store / Skills Leaderboard |

**冗余度快检**：逐段标记「竞品可找到等效内容？」→ 冗余段 >60% → **STOP**。

**Gate A 判定**：Topic Scope + KEEP/MERGE + 信息增量（≥2 项独有 + 冗余 ≤60%）→ 不通过 **STOP**，不得进入 Phase 1。

---

## 3. Phase 1 — 独立成文 Gate（KEEP/MERGE）

**三条件满足 ≥2 → KEEP**；否则 **MERGE** 并输出合并方案，**停止创作**。

| 条件 | 判断 |
|------|------|
| **搜索意图独立** | 与 content-graph.md 已有文章关键词重叠 ≤50% |
| **读者阶段不同** | Awareness / Consideration / Evaluation / Activation 不重叠 |
| **内容深度不可压缩** | 核心论证 >800 词，无法压入他文 ≤3 段 |

**合并时输出**：目标文章 slug、移入的 H2、keywords 合并、301 提醒。

---

## 4. 关键词冲突快查（Scheduling Agent 簇）

| 文章 slug | 主关键词 | 与谁边界 |
|-----------|---------|---------|
| `what-is-agentic-calendar` | agentic calendar | vs `calendar-driven-ai-vs-chat-ai`：定义 vs 范式对比 |
| `calendar-driven-ai-vs-chat-ai` | calendar-driven AI vs chat AI | 见上 |
| `ai-meeting-preparation` | AI meeting preparation | vs follow-up：prep vs post |
| `ai-follow-up-automation` | AI follow-up automation | 见上 |
| `best-ai-scheduling-assistants` | best AI scheduling assistant | vs agentic calendar：调查 vs 定义 |

---

## 5. Gate B — Slug 6-Point Check

**位置**：Phase 3，产出 slug 候选后。

| # | 检查项 | 标准 |
|---|--------|------|
| 1 | **常青** | 无年份、版本号 |
| 2 | **Intent-first** | 含 primary keyword 核心词 |
| 3 | **集群一致** | 同 cluster 命名模式一致 |
| 4 | **语义余量** | 描述主题非观点；30% 内容变化后仍适用 |
| 5 | **无禁词** | 不含 framework/strategy/guide/diagnosis/complete/年份 |
| 6 | **大声读** | 去掉连字符大声读 → 通顺 |

对照 article-types.md §9 反模式表：0 命中 → 通过。

**Gate B 判定**：6 项全 Pass → 进入 Phase 4；任一 Fail → 重选 slug。
