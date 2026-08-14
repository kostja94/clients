# Vofy Blog SKILL.md — 严苛审核报告

**审核日期**: 2026-06-15  
**文件**: `D:\项目文档\clients\vofy\blog\skills\vofy-blog-article\SKILL.md`  
**对比基准**: ThetaWave SKILL.md v2.0（同日重写）+ templates/ 12 维审核体系  
**版本**: v1.0.0 · 750 行  
**辅助文件**: `D:\项目文档\clients\vofy\blog\README.md`（151 行，入口文档）

---

## 总评

**Overall: CONDITIONAL PASS** — 无阻断级缺陷，但存在 9 个与 ThetaWave v2.0 标准的差距和 4 个具体 bug。750 行对于 7 种文章类型的创作 skill 来说覆盖度偏薄（ThetaWave 5 种类型用了 1020 行）。建议**针对性升级**而非全量重写，优先修复 Phase 6 SelfCheck 展开和 Phase 7 引用错误。

---

## 一、Vofy SKILL.md 的独特优势（值得保留并强化）

| 特性 | 说明 |
|------|------|
| **敏感类目合规模板 (§1.3)** | 5 类敏感内容 + 模板句，AI 视频生成领域的独创规则，ThetaWave 无对应需求 |
| **作者 Persona 池 (§1.2)** | 9 人作者池按主题分配，比单一作者更灵活 |
| **模型→studio 映射 (§6.2)** | 8 个模型的 id/studio/models 路径三元组，创作内链实操必备 |
| **Credits 撰写规则 (§6.3)** | 浮动消费单位的写作纪律，防止硬编码 |
| **7 种文章类型** | ModelGuide/PromptGuide/AppHowTo/Comparison/StyleGuide/Campaign/Announcement 覆盖 AI 创意工具的完整内容矩阵 |
| **现网 59 篇登记表 (§4.1)** | 按 cluster 分组，比 ThetaWave 的 12 篇表格更系统 |
| **Hub-Spoke 缺口标识 (§4.2)** | 明确标注 Grok Imagine、Veo 3.1、Motion Control 等缺失簇 |

---

## 二、缺陷分级

### 🔴 阻断级 (Blocker) — 0 个

无阻断缺陷。G1–G7 已定义（§1.4），核心工作流完整。

### 🟠 高危 (Critical) — 1 个

#### C1. Phase 6 SelfCheck 严重不足（Line 446–462）

当前 SelfCheck 仅一行引用：

> 对照 G1–G7 + §2.2 全模块 + 词数区间 + cluster 内链 + 敏感类目声明 + slug 规则

对比 ThetaWave v2.0 Phase 6：12 个维度，每维 4–10 个具体 checkbox，总计约 60 个检查项。Vofy 版本等于把 Agent 推回各 section 自行组织自检——Agent 的上下文窗口有限，大概率漏检。

**缺失的关键自检维度**：
- 碎片化检测（段落节奏/列表轰炸/衔接率）
- 漏斗透明度（每种类型的接受标准）
- 竞品公平性逐项（贬低措辞检测）
- SEO/SERP 专项（title 字符数/slug 反模式/snippet-ready）
- Conversion 匹配（CTA vs 读者阶段）
- 跨文章一致性（canonical 引用是否正确）

**建议**: 参照 ThetaWave v2.0 Phase 6 结构，为 Vofy 定制 12 维 SelfCheck（其中部分维度如敏感类目合规是 Vofy 独有）。

### 🟡 中危 (Major) — 5 个

#### M1. Phase 7 审核指令引用错误（Line 484）

```
逐维评分（02–13）
```

与旧版 ThetaWave 相同的 bug。templates/ 是 **A–J 十维评分体系**，不是按文件编号评分。文件 11–13 不在十维中。

**修复**: 改为 `按 A–J 十维评分（参考 02–10 维度文档）`。

#### M2. Phase 2 Brief 中 "Search intent" 概念混淆（Line 379）

```
**Search intent**: Definition / Tutorial / Comparison / Tool / Campaign / Announcement
```

枚举值实际是文章类型，不是 SEO 的 search intent（informational/commercial/transactional/navigational）。

**修复**: 改为 `**Article type**`（与 Phase 0 §2.1 对齐），或保留 search intent 但改用标准四分类。

#### M3. G1–G7 定义不完整（Lines 134–145）

当前只有 8 行表格（阻断条件 + 说明），缺少 **判定方法** 列。ThetaWave v2.0 的 G1–G7 有 4 列表格（阻断条件/说明/判定方法），Agent 知道具体怎么判。

| Vofy 当前 | ThetaWave v2.0 |
|-----------|---------------|
| G1: 事实错误 — 模型能力、Credits、studio 参数与现网矛盾 | G1: 事实错误 — … — **判定方法**: 逐 claim 对照 §6.1 产品事实表。功能不在当前版本 → 不能声称"已发布"。 |

缺少判定方法使 G1–G7 从"可执行规则"退化为"提醒列表"。

**修复**: 给 G1–G7 加第三列"判定方法"，特别是 G3（无来源数字）需明确内部数据标注格式、G5（产品夸大）需区分定位语言 vs 功能事实。

#### M4. 缺少引用分级体系（Phase 5）

Vofy 文章涉及大量量化数据：Credits 消耗、模型 benchmark、竞品定价、"2M+ users"。但 Phase 5 没有 P0/P1/P2 引用分级：

- P0 必须引用：竞品定价、benchmark 分数、市场份额
- P1 应当引用：行业趋势、"fastest/cheapest" 类声明
- P2 可不引用：原创 prompt 框架、作者自己测试的效果对比

ThetaWave v2.0 Phase 5.2 有完整的引用分级表和内部数据声明格式模板。

**修复**: 在 Phase 5 新增"引用分级与内部数据格式"小节。

#### M5. 缺少碎片化防护规则（Phase 5）

§2.2 有列表比例和长段落数量要求，但缺少：
- 连续短段落集群检测（≥3 个连续 ≤2 句段落 → 碎片化）
- 列表轰炸检测（连续 H2 section 各含列表无分析段落）
- 段间衔接率（连续 10 段 ≥7 对有衔接手段）
- "表格+一句话然后跳到下一节"反模式

AI 生成的 blog 在此类缺陷上尤其容易翻车。

**修复**: 在 Phase 5 新增"碎片化防护"小节，嵌入关键阈值（列表后必有 ≥2 句分析、H2 后首段为引导段落等）。

### 🔵 低危 (Minor) — 4 个

#### m1. slug 规则缺少反模式速查表（§2.8）

当前有 P1–P6 原则 + 禁词列表，但缺少 ThetaWave v2.0 的**反模式速查表**（含年份/连续重复词/内部架构词等 5 种错误示例+正确示例）。

**影响**: Agent 可能写出 `nanobanana-2-prompts-complete-guide`（含 `complete`，已在禁词列表，OK）但难以检测 `nano-banana-2-guide-guide` 等重复词问题。

**修复**: 加一个 5–6 行的反模式速查表。

#### m2. SelfCheck 输出模板不完整（Line 452–461）

仅有 5 行占位模板，`...` 代替了 9 个维度。缺少完整示例。

**修复**: 参照 ThetaWave v2.0 Phase 6 输出格式，列出 12 维维度表 + Overall 判定行。

#### m3. 缺少漏斗透明度规则（Phase 5 / §8）

Vofy 文章（特别是 Comparison 和 ModelGuide）同样存在漏斗过于透明的问题——叙事弧"教育→中立→'but Vofy makes it easy'→Vofy 是答案"。

**修复**: 在 Phase 5 新增漏斗自检（按文章类型分别设定接受标准）。

#### m4. 缺少利益声明放置规则

frontmatter 有 `disclosure` 字段，路由表标注了哪些类型 "必填" disclosure。但 Phase 5 没有说明 disclosure 在正文中的放置位置（开篇后？文末？）。

**修复**: Phase 5 新增一行：Comparison/StyleGuide/Campaign/AppHowTo 文在开篇后放置 1–2 句 disclosure 段。

---

## 三、与 ThetaWave v2.0 的功能差距总览

| 维度 | ThetaWave v2.0（1020 行） | Vofy v1.0.0（750 行） | 差距 |
|------|--------------------------|----------------------|:----:|
| G1–G7 定义 | 4 列表格（阻断+说明+判定+补充） | 2 列表格（阻断+说明） | 中 |
| Phase 6 SelfCheck | 12 维 × 4–10 项 = ~60 检查项 | 1 行引用 | **大** |
| 引用分级 | P0/P1/P2 + 内部数据格式模板 | 无 | 大 |
| 碎片化防护 | 段落节奏/列表轰炸/衔接率/多媒体 | 仅列表比例+长段数量 | **大** |
| 漏斗透明度 | 按 5 种类型的接受标准 | 无 | 中 |
| 竞品公平性 | 贬低措辞检测+二元化表检查 | 仅"≥1 优势" | 中 |
| Slug 规则 | 原则+反模式表+大声读测试 | 原则+禁词列表 | 小 |
| Phase 7 审核指令 | "按 A–J 十维评分" | "逐维评分（02–13）" ❌ | 小 |
| 利益声明 | 按类型的放置规则 | 仅 frontmatter 字段 | 小 |
| Conclusion 示例 | 3 种收束方式 | 无 | 小 |
| 敏感类目合规 | 无 | 5 类+模板句 ✅ | Vofy 独有 |
| Persona 池 | 无（单作者） | 9 人 ✅ | Vofy 独有 |
| 模型→studio 映射 | 无 | 8 模型 ✅ | Vofy 独有 |

---

## 四、README.md 问题（辅助文件）

`D:\项目文档\clients\vofy\blog\README.md` 整体质量良好——清晰的入口索引、主题簇图、frontmatter 示例。发现 1 个问题：

#### R1. 现网 slug 命名不一致（Line 71）

> Nano Banana 系列统一 `nanobanana-2-*`

但 §4.1 登记表中同一 cluster 同时存在 `nanobanana-2-*` 和 `nano-banana-2-*` 两种前缀（如 `nanobanana-2-prompts-complete-guide` vs `nano-banana-2-ecommerce-product-images`）。命名模式尚未统一。

**建议**: 要么统一为一种（推荐 `nano-banana-2-*`，因首篇 slug 即用此格式），要么在 README 中明确说明不一致的原因和历史遗留。

---

## 五、Vofy 专属的升级建议

除了以上缺陷修复，以下升级可进一步提升 Vofy SKILL.md 的创作质量：

### 5.1 新增维度：敏感类目合规自检

当前 §1.3 有规则但 Phase 6 SelfCheck 没有对应维度。建议在 12 维 SelfCheck 中新增一维：

**13. Sensitive Content Compliance**
- [ ] 文章是否涉及 §1.3 五类敏感内容？
- [ ] 如涉及：FAQ 或开篇后是否有用途与授权声明？
- [ ] 是否使用了模板句（Use only photos you own...）？
- [ ] celebrity/政治类：是否标注 satire/editorial？

### 5.2 新增维度：模型时效标注

Vofy 文章的时效性比 ThetaWave 更强（AI 模型每月更新）。

**14. Model Freshness**
- [ ] frontmatter `model_version_note` 已填且日期为审计当月
- [ ] 正文所有 Credits / 模型能力声明标注 "as of {month} {year}"
- [ ] 无写死的 "fastest / cheapest / always" 等时效敏感声明
- [ ] studio_url 参数在 vofy.art 现网已验证可用

### 5.3 建议的升级路径

| 优先级 | 动作 | 预计增量 |
|:---:|------|:---:|
| P0 | 修复 C1：展开 Phase 6 SelfCheck 至 12 维详细检查项 | +120 行 |
| P0 | 修复 M1：Phase 7 审核指令 "逐维评分（02–13）" → "按 A–J 十维评分" | 1 行 |
| P1 | 修复 M2：Phase 2 Brief "Search intent" → "Article type" | 1 行 |
| P1 | 修复 M3：G1–G7 加"判定方法"列 | +15 行 |
| P1 | 修复 M4：Phase 5 新增引用分级 + 内部数据格式 | +40 行 |
| P1 | 修复 M5：Phase 5 新增碎片化防护规则 | +30 行 |
| P2 | 修复 m1–m4：slug 反模式表、SelfCheck 模板、漏斗透明度、disclosure 放置 | +35 行 |
| P3 | 新增敏感类目合规自检 + 模型时效自检 | +30 行 |
| P3 | README 命名统一（nanobanana-2 vs nano-banana-2） | 1 处 |

**预计最终行数**: 750 → ~1070 行，与 ThetaWave v2.0（1020 行）相当。

---

## 六、对比总结

Vofy SKILL.md 在**领域专业性**上优于 ThetaWave（敏感类目合规、模型时效、Credits 规则、Persona 池），但在**创作自检体系**的完整度上明显弱于 ThetaWave v2.0。核心问题是 Phase 6 SelfCheck 退化为一句引用——这是两个 skill 之间 270 行差距的主要来源。

建议采用**针对性升级**（非全量重写）：保留 §1–§2 的领域专业性内容，重点扩展 Phase 5（引用分级 + 碎片化防护）和 Phase 6（12 维自检展开），修复 Phase 7 引用错误。升级后两套 skill 在结构深度上对齐，但各自保留领域特色。
