# SKILL.md vs templates/ 对比审核报告

**审核日期**: 2026-06-15  
**SKILL.md**: `D:\项目文档\clients\thetawave\skills\blog-article\SKILL.md` (757 lines, ~28KB)  
**templates/**: `D:\项目文档\templates\` (14 files, ~152KB, v3.2)  
**定位**: SKILL.md 是创作 skill（写作阶段），templates/ 是审核体系（发布前终审阶段）

---

## 一、总体评估

SKILL.md 作为创作 skill 是结构良好的，§0–§10 覆盖了从 intake 到交付的完整流程。但与 templates/ 审核体系对比后，暴露出**系统性的覆盖度不足**：SKILL.md 的 Phase 6 SelfCheck（12 维）与 templates/ 的 10 维评分体系（A–J）+ P0 Gate（G1–G7）之间存在严重的深度不对等——templates/ 每个维度都有 100–350 行的详细评分标准、检测方法、checklist，而 SKILL.md 的 SelfCheck 每个维度仅 1 行描述。

**核心结论**: SKILL.md 创作出的文章在通过 SelfCheck 后，大概率无法通过 templates/ 的 P0 Gate 和 9 维评分。创作阶段缺少足够的前置规则来预防 templates 审核会发现的缺陷。

---

## 二、架构层差异

### 2.1 维度数量错配

| | SKILL.md SelfCheck | templates/ 评分体系 |
|---|---|---|
| 维度数 | 12（含 2 个 ThetaWave 专用） | 10 维（A–J）+ P0 Gate（G1–G7） |
| 评分制 | Pass/Fail 二元 | 0–10 分 + 加权 100 分制 |
| 每个维度的文档 | 1 行描述 | 独立 .md 文件，100–400 行 |

### 2.2 Phase 7 审核指令的引用错误

SKILL.md Phase 7（Line 466）说：

> 逐维评分（02–13）

但 templates/README.md §二 明确是 **10 维评分（A–J）**，不是按文件编号 02–13 评分。文件 01 是 Gate，文件 02–10 各对应 1–2 个维度，文件 11–13 是补充项（不在十维中）。且 13-slug-design.md §一 明确说 "不在十维评分中占权重"。

**正确引用应为**: "按 README.md §二 的 A–J 十维评分，参考 01-publishability.md 做 P0 Gate，02–10 各维文档打分，11–13 做补充检查。"

---

## 三、覆盖度差距：SKILL.md SelfCheck vs Templates 逐维对比

### 3.1 差距最大维度（落差 >80%）

| SKILL.md SelfCheck 维度 | SKILL.md 覆盖 | Templates 对应文档 | Templates 覆盖 |
|---|---|---|---|
| **Presentation**（"长中短段交替；列表不过载"） | ~10 words | `10-presentation-rhythm.md` (350 lines) | 段落类型分类(长/中/短)、节奏健康标准(5 项阈值)、列表使用决策框架(7 项质量检查)、碎片化反模式检测(6 类)、多媒体策略(表格/图片/代码/引用)、段间衔接率(70% 健康线)、12 项 Master Checklist |
| **Fact/E-E-A-T**（"教育/认知科学来源；竞品 nofollow"） | ~12 words | `02-fact-eeat.md` (170 lines) + `11-evidence-citation.md` (160 lines) | 6 类检查(产品能力/竞品/数据/行业事实/选择性遗漏/对比表二元化)、Claim 类型×证据要求矩阵、引用优先级(6 级)、Source Map 模板、EEAT 6 项信号、引用分级(P0/P1/P2)、跨篇数字一致性、政策时效标注 |
| **Objectivity**（"≥1 非 ThetaWave 更适合场景；Comparison 公平"） | ~15 words | `06-objectivity.md` (220 lines) | 漏斗结构透明度检测、产品提及比例(按 5 种文章类型分别设限)、贬低性措辞检测、定位语言 vs 功能事实区分、署名诚信(5 类评估)、利益声明(6 种文章类型声明要求)、Research 方法论声明、分类准确性 |
| **Differentiation**（"与 §4 重复 <30%；独有框架/表"） | ~12 words | `03-differentiation.md` (140 lines) | 逐段信息冗余度标注(量化 <60%)、独特框架/对比维度/论点识别、Canonical Concept Map、6 项差异化检查(D1–D6)、跨文章产品描述重复率、核心概念跨篇重复检测 |

### 3.2 中覆盖度差距（落差 50–80%）

| SKILL.md SelfCheck 维度 | SKILL.md 覆盖 | Templates 对应文档 | 差距描述 |
|---|---|---|---|
| **Structure/Links** | 中等：§2.2 定义了最小模块集（Key takeaways + FAQ + Related），§6.4 定义了内外链规则 | `07-structure-links.md` (207 lines) + `13-slug-design.md` (400+ lines) | SKILL.md 缺少：死链逐点检测流程、forthcoming 上限(≤1)、锚文本质量检查、内容网络双向一致性、Intro/Conclusion 模板化检测("删定义和路标句"测试)、slug 的 12 项反模式(A1–A12)、slug 设计 7 原则 |
| **SEO/SERP** | 中等：§2.8 有 title/description 规则，Phase 3 有 SERP Fit mini-audit | `08-seo-serp.md` (177 lines) | SKILL.md 缺少：关键词竞争强度评估、Featured Snippet 友好度、结构化数据潜力(5 种 Schema)、Meta 描述与正文一致性检查、标题 5 项评分 |
| **Writing/Voice** | 中等：§8 有正向 5 维 + 禁止词列表 + 按类型的语气 | `05-writing-style.md` (180 lines) | SKILL.md 缺少：10 项空泛句检测清单、段落句子客观化写作指标(平均段长 60–90 词/句长 15–24 词/单段上限 130 词)、AI Risk Checklist(原创性 4 项)、Master Checklist 写作 8 项 |

### 3.3 低覆盖度差距（落差 <50%）

| SKILL.md SelfCheck 维度 | 差距描述 |
|---|---|
| **Depth** | SKILL.md §2.2 有词数范围，templates `04-depth-density.md` 有更细的空壳段落检测、"表格+一句话"反模式、FAQ 独立性验证、Why vs What 比例、分析性段落长度(4–8 句)。差距较小，但检测方法不够系统。 |
| **Conversion** | SKILL.md 有 CTA 分散规则(≤2 次)，templates `09-conversion.md` 有读者阶段×CTA 匹配表、CTA 质量 5 项检查、禁止 CTA 模式、跨篇 CTA 模板化检测。差距中等。 |
| **Slug** | SKILL.md §2.8 有基础规则，但 templates `13-slug-design.md` 是 400+ 行的独立审计文档。差距巨大。 |

### 3.4 SKILL.md 有但 Templates 没有的维度（Thetawave 专用）

| SKILL.md SelfCheck 维度 | 说明 |
|---|---|
| **Publishability G1–G7** | Templates 01 完整定义了 G1–G7。SKILL.md 引用但未定义——这是本次审核的阻断缺陷 B1。 |
| **Dual-core lane** | Thetawave 独有的 NoteTaker/NotesGenerator 路线检查。Templates 没有此维度，是合理的——这是产品特定维度。 |
| **Study hub-spoke** | Thetawave 独有的 hub-spoke 去重检查。Templates 的 03-differentiation.md 有 Canonical Map 和 12-cross-article-consistency.md 的重复检测，可以部分覆盖但不如 SKILL.md 的专用规则精确。 |

---

## 四、Templates 有但 SKILL.md 完全缺失的维度

### 4.1 证据链与引用标准（`11-evidence-citation.md`）

SKILL.md Phase 5 事实与合规表要求 "量化 claim | [Source: URL]"、"竞品 | nofollow noopener"，但**完全没有**以下内容：

- **引用分级**（P0 必须引用 / P1 应当引用 / P2 可不引用）——SKILL.md 所有引用规则都是二元的（有来源 / 无来源），缺少按读者怀疑程度的优先级分层
- **内部数据声明格式**: "based on internal analysis of [N] [data type] across [time period]"
- **跨篇数字一致性**: 同一数字在多篇文章中出现时必须每条都引用，精度统一
- **政策时效标注**: 涉及定价、准入门槛等高频变动信息的 "as of [date]" 规范
- **"怀疑测试"和"竞争对手测试"**: 灰色地带判断框架

**影响**: SKILL.md 创作的文章如果引用了内部数据（如 "300,000+ registered students"），按 templates 标准会因为格式不规范或缺少 `n=` 标注而被扣 E-E-A-T 分。

### 4.2 利益声明与署名诚信（`06-objectivity.md` §五、§六）

SKILL.md 设定作者为 "Kostja"（真实人名），但没有**任何**关于利益声明的规则。Templates 要求：

- Comparison 文 **必须**在文首有利益声明
- Research 文 **必须**有方法论声明（测试环境、时间范围、数据来源）
- Glossary 文 **建议**在文末有利益声明
- 署名优先真人名，虚构署名需加 "Reviewed by [真实人名]"

**影响**: SKILL.md 创作的文章发布后，如果被 templates 审核，会在 Objectivity 维度因缺少利益声明而被扣分。

### 4.3 漏斗结构透明度检测（`06-objectivity.md` §二）

SKILL.md §8 有 "Category-building" 要求（自有产品首次出现前提供独立价值），但**没有**系统性的漏斗检测方法：

- 叙事弧提取：教育→中立→"but X changes everything"→产品答案
- 转折点位置检测：出现在前 30% → 漏斗过于明显
- 按文章类型的接受标准（Research/Glossary 不可见漏斗，Product 文可接受）

**影响**: SKILL.md 创作的 Commercial/Alternative 文章可能在 templates 审核时被判定为漏斗过于透明。

### 4.4 表现形式碎片化检测（`10-presentation-rhythm.md` §四）

SKILL.md §2.2 有列表比例限制（Commercial ≤30% 等），但**完全没有**：

- 连续短段落集群检测（≥3 个连续 ≤2 句段落 → 标记碎片化）
- 片段拼贴检测（打乱段落顺序后语义是否仍然通顺）
- 列表轰炸检测（相邻 H2 section 各含列表、中间无分析性段落）
- 段落长度标准差检测（<1.0 → 无节奏变化）
- 段间衔接率检测（连续 10 段衔接率 <50% → Fail）
- 多媒体元素裸奔检测（表格/图片前后无分析性段落）

**影响**: AI 生成的文章最常见的缺陷就是碎片化——bullet point 堆砌、段落节奏单一。SKILL.md 对此的防护极其薄弱，仅有 "长中短段交替" 和列表比例上限两条模糊规则。

### 4.5 跨文章一致性审计（`12-cross-article-consistency.md`）

SKILL.md §4 有内容图谱和 Canonical Concept Registry，Phase 1 有简单的关键词冲突检查。但**完全没有**：

- **矛盾检测**: 同一 cluster 内，文章 A 说 "X"，文章 B 说 "not X" → 硬矛盾
- **跨篇重复检测**: 同一概念在 ≥3 篇文章中 ≥3 句展开 → 重度重复
- **Hub-spoke 链接完整性**: Hub 是否链向所有 spoke，spoke 是否回链 hub，是否双向
- **Cannibalization 审计**: 两篇文章 targeting 高度重叠的搜索意图，在 SERP 中互抢排名
- **段落级重复检测**: 互换测试——文章 A 的段落插入文章 B 是否毫无违和？

**影响**: Thetawave 目前有 12 篇文章，且 SKILL.md 正在创作第 13 篇。没有跨篇审计规则，新增文章可能引入与已有 12 篇的事实矛盾、段落重复、或关键词 cannibalization。

---

## 五、具体规则冲突

### 5.1 "Key takeaways" vs "TL;DR"

- **SKILL.md §2.2**: 明确要求 "Key takeaways"（不用 TL;DR），"与现有 12 篇一致"（Line 138）
- **Templates 07-structure-links.md S1**: "有 ## TL;DR"、"3–5 bullet；独立传达 80% 价值"
- **Templates README.md §二 C 维度**: 10 分标准包含 "TL;DR"

**冲突**: 如果创作者遵循 SKILL.md 使用 "Key takeaways"，templates 审核会因不符合 S1 标准（TL;DR）扣 Structure 分。如果创作者遵循 templates 使用 "TL;DR"，会与现有 12 篇文章不一致。**SKILL.md 的立场是优先与现有文章一致**，但 templates 的立场是优先**结构标准化**。

**建议**: 要么 templates 将 S1 改为 "Key takeaways / TL;DR" 以兼容两个命名，要么 SKILL.md 在 Phase 7 交付时提示人类统一历史文章的标题。

### 5.2 文章类型分类体系不一致

| SKILL.md 类型 | Templates category |
|---|---|
| Commercial Roundup | Comparison |
| Alternative / VS | Comparison |
| Study Method Hub | Research(?) / Comparison |
| Study Method Spoke | Research / Glossary(?) |
| How-To | Product tutorial |

SKILL.md 用的是面向 Thetawave 读者意图的类型系统（5 类），templates 用的是面向 SEO 分类的系统（Research / Comparison / Product / Glossary / Case Study，5 类）。两套体系不完全对应。创作者在 Phase 2 Brief 中填的类型和 templates 审核时代入的 category 可能不匹配。

**建议**: SKILL.md 在 Phase 2 Brief 或 Phase 3 frontmatter 中增加一个字段，将内部类型映射到 templates 的 category。

### 5.3 词数标准不一致

| 文章类型 | SKILL.md 词数 | Templates 04 词数（对应类型） |
|---|---|---|
| Commercial Roundup | 2500–3500 | Comparison: 2500–4000 |
| Alternative | 2000–3000 | Comparison: 2500–4000 |
| Study Method Hub | 2500–3200 | Research: 2400–3500 |
| Study Method Spoke | 1800–2500 | Research/Glossary: 1800–2600（Deep glossary） |
| How-To | 2000–2800 | Product tutorial: 1500–2500 |

差距不大，但 Commercial/Alternative 在 templates 中的基准（2500）高于 SKILL.md 的下限（2000）。一篇 2000 词的 Alternative 文通过 SKILL.md SelfCheck 后，在 templates 深度审核中可能因字数偏低被扣分。

---

## 六、结构性缺陷总结

### 6.1 已在前一份审核报告中标识（不再重复）

- B1: G1–G7 未定义
- C1: `templates` 拼写错误
- C2: Search Intent 概念混淆
- M1–M4: 4 个中危缺陷
- m1–m6: 6 个低危缺陷

### 6.2 新增: 与 templates 对齐的缺陷

| ID | 等级 | 描述 |
|----|:----:|------|
| **N1** | 🔴 Blocker | SelfCheck 维度深度严重不足。12 个维度中 8 个维度仅 1 行描述，对应 templates 的独立文档（100–400 行）。创作阶段缺少足够的规则来预防审核阶段的 Fail。 |
| **N2** | 🟠 Critical | Phase 7 审核指令引用错误。"逐维评分（02–13）" 应为 "按 A–J 十维评分"。文件 11–13 不在十维中。 |
| **N3** | 🟠 Critical | 缺少利益声明规则。所有 Comparison 和 Alternative 文都需要利益声明，但 SKILL.md 未提及。 |
| **N4** | 🟠 Critical | "Key takeaways" vs "TL;DR" 命名冲突。SKILL.md 和 templates 对同一模块使用不同名称。 |
| **N5** | 🟡 Major | 缺少证据链引用分级（P0/P1/P2）。内部数据（30 万用户等）缺少标准的 `n=` 声明格式。 |
| **N6** | 🟡 Major | 缺少漏斗结构透明度检测规则。创作阶段没有规则防止叙事弧过于透明。 |
| **N7** | 🟡 Major | 缺少碎片化检测规则。SKILL.md 对 AI 生成内容最常见的碎片化缺陷防护不足。 |
| **N8** | 🟡 Major | 缺少跨文章一致性审计。12 篇已有文章 + 新增文章之间可能出现事实矛盾、段落重复、cannibalization。 |
| **N9** | 🟡 Major | 文章类型分类体系与 templates category 不直接对应。需要在创作阶段做映射。 |
| **N10** | 🔵 Minor | 缺少署名策略讨论（真实人名 vs 虚构署名，EEAT 影响）。虽然已设 author=Kostja，但未说明为什么。 |
| **N11** | 🔵 Minor | 缺少 SEO 结构化数据潜力评估（FAQPage / HowTo / DefinedTerm 等 5 种 Schema）。 |

---

## 七、修复优先级总览（合并前次 + 本次）

| 优先级 | ID | 来源 | 描述 | 工作量 |
|:---:|-----|------|------|:---:|
| P0 | B1 | 前次 | 定义 G1–G7 规则 | 中 |
| P0 | N1 | 本次 | SelfCheck 12 维需大幅扩展（每维扩展至 15–30 行，嵌入 templates 关键阈值） | 大 |
| P0 | N2 | 本次 | Phase 7 审核指令修正 | 小 |
| P0 | C1 | 前次 | `templates` → `templates` 全文替换 | 小 |
| P1 | N3 | 本次 | 在 Phase 5 或 §8 增加利益声明模板和方法论声明规则 | 中 |
| P1 | N4 | 本次 | 解决 "Key takeaways" vs "TL;DR" 冲突（协商 templates 或更新历史文章） | 小 |
| P1 | C2 | 前次 | Brief 中 Search intent → Article type | 小 |
| P1 | M1 | 前次 | 补全 Phase 1 快查表至 12 篇 | 中 |
| P1 | N5 | 本次 | 在 Phase 5 增加引用分级（P0/P1/P2）和内部数据格式 | 中 |
| P1 | N6 | 本次 | 在 §8 或 Phase 5 增加漏斗透明度自检 | 中 |
| P1 | N7 | 本次 | 在 §2.2 或 Phase 6 增加碎片化反模式检测规则 | 大 |
| P2 | N8 | 本次 | 在 Phase 1 或新增 Phase 新增跨文章一致性检查（至少轻量版） | 大 |
| P2 | N9 | 本次 | 在 Phase 2 Brief 或 Phase 3 增加类型→category 映射字段 | 小 |
| P2 | M2–M4, m1–m6 | 前次 | 6 个中/低危修复 | 小–中 |
| P3 | N10, N11 | 本次 | 署名策略、结构化数据评估 | 小 |

---

## 八、建议的 SelfCheck 扩展结构

当前 SelfCheck（Line 418–432）每个维度仅 1 行。建议参照 templates 各文档的关键阈值，扩展为：

```
### Phase 6 — 创作自检（12 维 Pass/Fail）

#### 1. Publishability G1–G7
（需先定义 G1–G7，每项附判断标准，见 B1 修复）

#### 2. Fact/E-E-A-T
- 所有量化 claim 有可追溯来源（P0 级）或内部数据标注格式
- 竞品描述基于官方资料；pricing 有时效标注
- 引用分级：P0 数字必链 / P1 行业趋势有来源或限定词 / P2 原创框架不要求外链
- ≥1 场景推荐非自有产品（EEAT E6）

#### 3. Differentiation
- 逐段标记冗余度：<60% 段落可在竞品中找到等效内容
- 独有框架/表格/论点；canonical concept 只引述不展开
- 与 §4 Canonical Registry 对照通过

#### 4. Depth
- 词数达标（按 §2.1 类型阈值）；叙事词数排除 frontmatter/表格/FAQ
- 无"表格+一句话"空壳（<3 处）
- FAQ ≥3 且 ≥1 覆盖正文未涉及角度
- ≥3 个分析性段落达 4–8 句

#### 5. Presentation & Rhythm
- 列表占比 ≤ 类型上限（≤25% Commercial/Alternative，≤25% Study Method，≤35% How-To）
- 长段落(≥4句) ≥3 个；连续短段落(≤2句) ≤2 个
- 每个列表有前导句 + 列表后有 ≥2 句分析
- 无连续 2 个 H2 section 各含列表无分析段落（列表轰炸）
- 表格前后各有 ≥2 句分析段落
- 抽样 10 段衔接率 ≥70%

#### 6. Writing/Voice
- §8 正向 5 项全满足
- 五禁词(revolutionary/game-changing/unlock/seamless/magic/best-in-class/only solution) 0 次
- 空泛句 ≤2 处（in today's world / let's dive in / it's important to note...）
- 每 300–500 词出现 1 次具体对象

#### 7. Objectivity
- 叙事弧转折点在全文 ≥30% 位置
- 产品提及比例 ≤ 类型上限
- 竞品描述无贬低性措辞（just/merely/only/simplistic）
- 定位语言 vs 功能事实明确区分
- Comparison 文含利益声明

#### 8. Structure/Links
- 必备模块完整：Key takeaways + FAQ≥3 + Related(2–6)
- 首段 ≥1 blog 或 feature 内链；Body blog 1–4
- 内链锚文本描述性（无 click here）
- Frontmatter 与文末 Related 双向一致
- Forthcoming ≤1（仅 Related 脚注）

#### 9. SEO/SERP
- title 含 primary keyword（45–65 字符）
- description 120–160 字符；含 keyword + value prop
- slug 常青、无年份、无数量、无内部架构词(framework/strategy/guide)
- keywords ≥5；slug 通过"大声读"测试

#### 10. Conversion
- CTA 与读者阶段匹配（Awareness→内链 / Consideration→demo / Activation→tutorial）
- signup + feature 分散，全文 ≤2 次直接 CTA
- 无空泛 CTA（start your journey / unlock your potential）

#### 11. Slug（对齐 templates/13-slug-design.md）
- 无年份/数量/连续重复词/下划线/内部架构词
- 与 primary keyword 近似对齐
- 人可读（去掉连字符大声读通顺）
- ≤60 字符；与同簇命名模式一致

#### 12. Thetawave-specific
- Dual-core lane: NoteTaker/NotesGenerator 链到正确 feature
- Study hub-spoke: spoke 未完整重定义 hub 表格内容
```

---

## 九、总结

SKILL.md 的核心问题是**创作阶段规则与审核阶段标准之间的深度不对等**。757 行的创作 skill 产出的文章需要面对 152KB 的审核体系——但创作阶段大部分的防护规则只有 1 行宽度，审核阶段对应维度有 100–400 行深度。

这不是说 SKILL.md 需要膨胀到 152KB，而是说关键阈值和反模式必须在创作阶段前置。目前最大的三类缺失是：碎片化防护、引用标准、跨文章一致性。这三类缺失意味着按照 SKILL.md 创作的优质文章，在 templates 审核中仍可能在 Presentation (12% 权重)、E-E-A-T (20% 权重)、Cross-article consistency (not scored but gate-blocking) 三个维度翻车。
