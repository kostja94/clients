# AI Math LLM / 数学向大模型 · 知识块（非线性笔记）

**材料范围**：公开网络检索（AIME / USAMO、BenchLM math、Epoch AI **FrontierMath**、MathArena）；**未**引用 Alignify 站内正文或本站实测。网摘整理日期 **2026-06-23**。

**站内对照**：正式页 **`/tools/llm-for-math`**、**`/zh/tools/llm-for-math`** · `content/tools/en|zh/llm-for-math.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#llm-for-math-tools`

**Hub · 五轴分流**：[llm.md](./llm.md) · **排行快照**：[llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) §Math

**站内相邻**：[llm-for-reasoning.md](./llm-for-reasoning.md)（GPQA/HLE ≠ 奥数）· [llm-for-coding.md](./llm-for-coding.md)（HumanEval ≠ 数学）

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **竞赛短答**：**AIME**（整数答案）、**AMC** 管线——2025–2026 前沿模型 **接近满分**，BenchLM 常标 **display-only**（[benchlm.ai/math](https://benchlm.ai/math)）。
- **证明题 / USAMO**：步骤级人审或陪审（**MathArena** 等）——自动化判分难度高。
- **MATH-500 / BRUMO**：BenchLM 2026 叙事中 **仍参与 math 子分加权**，较 AIME 更有区分度。
- **FrontierMath（Epoch AI）**：未公开研究级题 + Python 验证；**Tier 4** 极难——与 AIME 满分 **不等价**（[epoch.ai/frontiermath](https://epoch.ai/frontiermath/tiers-1-4/the-benchmark) · [arXiv:2411.04872](https://arxiv.org/abs/2411.04872)）。
- **工具使用**：FrontierMath 官方 harness 允许 Python——厂商内部评测工具权限不同则 **分数不可对齐**。

---

## 专题对照：数学评测族

| 类型 | 代表 | 区分度（2026 前后公开材料） |
|------|------|------------------------------|
| 高中竞赛短答 | AIME 各年 | **饱和**；display-only |
| 证明 | USAMO、MathArena | 闭源 vs 开源差距大 |
| 研究级 | FrontierMath T1–4 | 绝对准确率低 |
| 课内风格 | MATH-500、BRUMO | 教辅场景更近 |

---

## 问题域

- **泄题与污染**：赛季题可能已在训练语料——FrontierMath 用私有集缓解。
- **「奥数强」≠「企业 FP&A 强」**：须用 **业务试算** 实测。
- **与 reasoning 轴**：多步演绎见 [llm-for-reasoning.md](./llm-for-reasoning.md)；本轴聚焦 **数值/证明/研究数学**。
- **饱和与区分度**：AIME 等竞赛基准已严重饱和——2026 年多家厂商 claim >95%——从 display-only 的 AIME 到真正有区分度的 FrontierMath 的迁移是读榜必修课。
- **推理成本 vs 精度**：数学 reasoning SKU 的推理 token 消耗巨大——同一道题 chat vs thinking 模式成本可能差 50×——选型决策需同时评估分数与 $/题 成本。

---

## 形态谱系

- **Type A — 竞赛短答型**：AIME/AMC——模式识别强，**区分度下降**。
- **Type B — 证明推理型**：USAMO——需自洽逻辑链；开源短板常在此。
- **Type C — 研究级**：FrontierMath——最佳模型 Tier 4 仍低分。
- **Type D — 教学辅助型**：MATH-500/BRUMO——逐步解释比竞速更重要。

---

## 落地碎片

- **教辅 / 题库**：优先 MATH-500/BRUMO + **自建错题**；追 AIME 满分对教辅价值有限。
- **证明辅助**：须 **人类终审**；引理幻觉仍常见。
- **量化/工程计算**：用 **蒙特卡洛、PDE、优化** 等业务题 blind test——勿依赖竞赛榜。

---

## 排行快照

AIME26 Top 行（display-only、常不足 5 家 provider）及 FrontierMath 指针见 **[llm-leaderboard-snapshots.md §Math](./llm-leaderboard-snapshots.md)**（2026-06-23）。

**轴内解读**：2026 年中 AIME 前排 **96% 档** 挤作一团——选型应看 **FrontierMath / BRUMO** 而非 display-only AIME；厂商 self-reported 常高于第三方 **2–5pt**（读 [llm.md](./llm.md) §读榜检查清单）。

---

## FrontierMath · 分层读榜（成稿块）

| Tier | 题意（公开材料） | 与 AIME 关系 | 选型含义 |
|------|------------------|--------------|----------|
| **T1–T2** | 研究生级、可程序验证 | AIME 96% **不蕴含** T3+ 高分 | 研究辅助仍须 **试跑** |
| **T3** | 组合研究题 | 开源常落后闭源 **轴内 gap** | 自托管需 golden set |
| **T4** | 极难、长证明链 | 最佳模型 **极低分** | 「奥数满分的模型」仍可能 T4 接近零 |

**快照指针**：Tier 格局叙述见 **[llm-leaderboard-snapshots.md §FrontierMath](./llm-leaderboard-snapshots.md)**——**勿在专轴复制完整 % 表**。

**Python 工具公平性**：FrontierMath 官方 harness **允许 Python**——厂商内部若禁工具，分数 **不可与官方行并列**。

---

## BRUMO / MATH-500 · 教辅与日常数学（成稿块）

- **MATH-500**：经典多步题集——BenchLM math **子分仍加权**；较 AIME 更接近 **课内/教辅** 难度分布。
- **BRUMO**：2026 BenchLM 叙事中参与 math 加权——用于 **区分「会做题」与「会讲步骤」** 的产品叙事。
- **与 AIME**：AIME **display-only**——媒体标题「AIME 满分」**信息增量低**；成稿应转向 FrontierMath 或业务试算。

---

## MathArena / USAMO · 证明线（成稿块）

- **USAMO**：步骤证明、人审——**自动化榜难统一**。
- **MathArena**：社区/平台化证明评测——**闭源 vs 开源** 差距常 **大于** AIME 短答轴。
- **落地**：证明辅助 **必须人类终审**——AI 引理 **plausible 但错误** 仍常见。

---

## 场景 → 基准映射（成稿块）

| 场景 | 优先信号 | 次选 | 勿依赖 |
|------|----------|------|--------|
| K12 教辅 | MATH-500、BRUMO | 自建错题库 | AIME 排名 |
| 竞赛培训 | AIME + **人审证明** | MathArena | MMLU |
| 大学作业辅导 | MATH-500 | Thinking SKU | GPQA alone |
| 量化 / 风险建模 | **蒙特卡洛、PDE 业务集** | FrontierMath 叙事 | AIME |
| 科研数学辅助 | FrontierMath T3+ | 内部证明检查 | Arena |
| 财务 FP&A | Excel/模型 **盲测** | — | 任何公开数学榜 |

---

## 开源 vs 闭源 · 数学轴（成稿块）

| 维度 | 开源 / 开放权重 | 闭源 |
|------|-----------------|------|
| **AIME display** | GLM、Qwen、Kimi **95%+ 档** 可并列 | 同档挤作一团 |
| **FrontierMath tail** | 公开材料常 **落后** | Opus/GPT 叙事领先 |
| **证明（USAMO）** | 短板更明显 | MathArena 叙事领先 |
| **采购** | 自托管 + 微调 | API Thinking 档 |

---

## 常见误读 FAQ（数学轴 · 成稿块）

| 误读 | 纠正 |
|------|------|
| 「AIME 满分 = 数学 AGI」 | display-only + **饱和**——看 FrontierMath |
| 「FrontierMath 低分 = 模型不会数学」 | T4 **设计为极难**——绝对分低是常态 |
| 「GPQA 高 = 奥数强」 | GPQA 是 **科学专家 MCQ**——见 [llm-for-reasoning.md](./llm-for-reasoning.md) |
| 「允许 Python = 作弊」 | FrontierMath **官方 harness** 含工具——跨厂商须对齐 |
| 「竞赛强 = Excel 财务强」 | 分布完全不同——**业务试算** |
| 「MATH-500 高 = 证明题强」 | Type A/D **≠** Type B 证明 |
| 「开源 AIME 高 = FrontierMath 同序」 | tail **常分化**——读 snapshots §FrontierMath |

---

## Golden set 试跑模板（数学轴 · 成稿块）

| 步骤 | 动作 | 输出 |
|------|------|------|
| 1 | 从业务抽 **50 题**（含 FP&A、统计、证明草图） | 题面 + 标准答案 |
| 2 | 对齐 **工具政策**（是否允许 Python） | 与 FrontierMath harness 文档对照 |
| 3 | 跑 **2–3 模型**（如 Opus thinking、GPT、开源 V4） | 正确率、步骤 hallucination 率 |
| 4 | 记录 **$/正确题** 与 **人审时长** | 采购 memo |
| 5 | 公开榜只作 **背景**——引用 snapshots §Math / §FrontierMath **带日期** | 脚注 URL |

**成稿 TLDR**：「数学选型 = **业务试算 + FrontierMath 叙事 + 禁止 AIME 标题党**。」

---

## 风险 · 合规 · 治理（数学轴特有）

- **基准饱和**：AIME display-only 后排名信息价值趋零。
- **证明幻觉**：AI 引理可能 plausible 但错误——人类终审必须。
- **工具公平性**：FrontierMath 官方允许 Python——跨厂商对比须读 harness。

共享治理见 [llm.md](./llm.md) §风险 · 合规 · 治理。

---

## 工具与产品类型（评测基准）

| 基准类型 | 代表基准 | 任务特点 |
|---------|---------|----------|
| 研究级数学 | FrontierMath, USAMO | 定理证明/竞赛题 |
| 竞赛数学 | AIME 2024/2025, MathArena | 高中竞赛题 |
| 课程数学 | BRUMO, MATH-500 | 本科及以下 |
| 跨学科 | GSM8K, MMLU-Math | 应用数学 |

### 对比与测评（第三方；观点非官方）

2026 年中数学 LLM 共识：GPT-5 Pro 在 FrontierMath Tier 4 领先；Claude 4 Opus 在证明类任务有深度优势；DeepSeek-R1 在开源社区贡献了显著的数学推理能力。AIME 基准趋于饱和（高分模型 >90%），区分度向 FrontierMath 与 MathArena 转移。实时排行见 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)。

---

## 外链索引

| 名称 | URL |
|------|-----|
| FrontierMath | [epoch.ai/frontiermath](https://epoch.ai/frontiermath/tiers-1-4/the-benchmark) |
| BenchLM · Math | [benchlm.ai/math](https://benchlm.ai/math) |
| BenchLM · AIME26 | [benchlm.ai/benchmarks/aime2026](https://benchlm.ai/benchmarks/aime2026) |
| MathArena | [matharena.ai](https://matharena.ai/) |

---

## 延伸阅读

- [llm.md](./llm.md) · [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) · [llm-for-reasoning.md](./llm-for-reasoning.md)
