---
name: dubbingai-blog-article
description: >
  Load when user asks to create, draft, or outline a Dubbing AI blog article
  for dubbingai.io/blog — voice changer comparisons, how-tos, platform setup,
  alternatives, meme soundboards, sound effects, voice actors, pop culture, etc.
  Covers Track S (2026 strategic) and Track C (cms-export long-tail).
  Do NOT load for title/description-only tasks (future dubbingai-meta-title-description).
metadata:
  version: 1.2.1
  project: dubbingai.io
  locale: en
  market: B2C gaming/streaming (US/global)
  load-rule: progressive-disclosure
  max-primary-lines: 500
  self-contained: true
  forbidden-reads:
    - dubbingai.md
    - dubbingai-*.md
    - ../../blog/README.md
    - ../../blog/internal-external-links-checklist.md
---

# Dubbing AI Blog Article Creation

为 **https://dubbingai.io/blog/** 从选题到英文成稿。**范围**：英文 `/blog/{slug}` + Track C `cms-export/{slug}.md`。**硬性规则**：Agent 执行本 skill 时只读本文件夹内文件，禁止读取仓库内 `dubbingai.md`、`dubbingai-*.md`、`blog/README.md` 或其他外部文档。

---

## 渐进式加载规则（硬性）

```
Agent 默认只读本文件。
Phase 需要细节时，按指针读取 references/{file}.md（一次最多 2 个）。
禁止一次性加载全部 references。
读完用完即弃——不跨 Phase 保留 reference 上下文。
```

---

## §0 如何使用

### 触发语

```
按 dubbingai-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Comparison|HowTo|IntentSplit|Alternative|PlatformGuide|SoundboardPick|SoundEffectPick|VoiceActorProfile|PopCultureExplain|CharacterBridge|HardwareGuide|Diagnosis} 文章。
Track：{S|C|auto}。CMS category（Track C）：{category}。
发布目的：{SEO|品牌|转化|趋势}。目标读者：{描述}。
```

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `dubbingai-meta-title-description` |
| 韩国 Naver 韩文成稿 | `localization/` 独立 skill |
| HTML→MD CMS 迁移 | `blog/cms-export/scripts/` |
| 非 dubbingai.io 博客 | 通用 blog skill |
| 非英文内容 | 另建 ZH skill |

### 输出（Phase 6 交付物）

**Track S**：Article Brief · 完整稿 `dubbingai/blog/NN-{slug}-2026.md` · SelfCheck（12 维）· Source Map · 提示人类更新 blog/README

**Track C**：Article Brief · 完整稿 `dubbingai/blog/cms-export/{slug}.md` · SelfCheck（8 维）· Source Map · 提示人类更新 manifest.csv

与用户沟通可用中文；**正文必须为英文**。

---

## §1 双轨交付与 Gate 清单

> **完整配置 + G1–G7 → `references/project-config.md`**
> **P1–P6 Proof Gate → `references/proof-gate.md`**
> **C1–C4 CMS Overlap → `references/cms-overlap-gate.md`**

**Phase 0 / Phase 5 前加载 project-config + proof-gate + cms-overlap-gate（Track C 或 slug 冲突时）。**

| Gate | 项数 | 阻断条件 |
|------|:---:|------|
| **G1–G7** | 7 | 事实错误 / 死链 / 无来源数字 / 竞品错误 / 产品夸大 / 内链未上线 / 品牌风险 |
| **P1–P6** | 6 | 产品数字无 as-of / Live-File 混淆 / Intent 混用 / SFX 分流错误 / Dubbing Box 夸大 / 竞品不公平 |
| **C1–C4** | 4 | slug 冲突未声明 / Hub 抢词 / 程序化页 duplicate / 301 目标冲突 |

G1–G7 + P1–P6 +（适用时）C1–C4 全部 Pass 方可交付。

### Track S vs Track C

| 项 | Track S（战略） | Track C（CMS 长尾） |
|----|----------------|---------------------|
| 路径 | `blog/NN-{slug}-2026.md` | `blog/cms-export/{slug}.md` |
| 下一序号 | **05**（见 content-graph） | 无 NN |
| frontmatter slug | 不含 `/blog/`、不含年份 | 与 URL 1:1 + `source: cms` |
| 结构 | 无编号 H2；At a glance / 30-second answer | 允许 Key Takeaways |
| 词数 | 见 article-types | 1200–2200（VoiceActor 1500–2500） |
| SelfCheck | 12 维加权 ≥70 | 8 维 Pass/Fail |

### Phase 0 Track 路由

```
IF 主意图 ∈ {best/compare/alternative, intent split, pillar refresh}
   OR slug 在 content-graph §P0 战略队列
   OR 需与 01–04 四向互链（4-Spoke）→ Track S

IF 主意图 ∈ {meme soundboard, sfx download, voice actor, pop culture}
   OR CMS category 匹配五类之一
   OR 用户明确 cms 风格 → Track C

IF slug 已存在于 cms-export 且用户要重写升级
→ RefreshMode: RefreshInPlace | PromoteToStrategic
```

---

## §2 文章类型路由

> **12 类路由表 + H2 模板 + Voice → `references/article-types.md`**
> **CTA 分层 → `references/platform-routing.md`**

**Phase 0 / Phase 3 前加载。** 速查：

| 类型 | Track | 词数 | 产品提及上限 |
|------|-------|------|-------------|
| Comparison | S | 2500–3500 | ≤35% |
| HowTo | S/C | S:2200–3200 / C:1500–2200 | ≤40% |
| IntentSplit | S | 1800–2600 | ≤25% |
| Alternative | S/C | 2200–3000 | ≤45% |
| PlatformGuide | S/C | 2000–2800 | ≤40% |
| SoundboardPick | C | 1200–2000 | ≤50% |
| SoundEffectPick | C | 1200–2000 | ≤45% |
| VoiceActorProfile | C | 1500–2500 | ≤20% |
| PopCultureExplain | C | 1000–1800 | ≤30% |
| CharacterBridge | C | 1200–1800 | ≤35% |
| HardwareGuide | S | 1800–2600 | ≤40% |
| Diagnosis | S/C | 1800–2600 | ≤30% |

**路由**：`best`→Comparison · `how to`+live mic→HowTo · Google Assistant→IntentSplit · `vs`→Alternative · meme soundboard→SoundboardPick · voice actor→VoiceActorProfile · 角色名→CharacterBridge（链 `/voice-changer/{slug}`）

---

## §3 创作工作流（8 Phase + 3 Gate）

```
Phase 0 — Intake & Gate A ─── 不通过 → STOP
Phase 1 — Article Brief
Phase 2 — Slug Design & Gate B ─── 不通过 → 重选 slug
Phase 3 — Outline
Phase 4 — Draft
Phase 5 — SelfCheck & Gate C ─── 不通过 → 修复
Phase 5.5 — Cross-Article Audit（同批 ≥2 篇）
Phase 6 — Delivery
```

### Phase 0 — Intake & Gate A

第一行输出：`## Topic Scope: {scope}` · `## Track: S|C` · `## CMS category`（Track C）

**加载**：`project-config` + `content-graph` + `cms-overlap-gate`

0.0 **独立成文必要性 Gate**（先于 SERP Fit）— 三条件满足**任意两个** → KEEP 独立成文：

| 条件 | 含义 | 判断方法 |
|------|------|------|
| **搜索意图独立** | 搜这个词的人，搜相邻词不会满足需求 | primary keyword 与已有文章搜索池重叠 <50% |
| **读者阶段不同** | Awareness→Consideration→Evaluation→Activation | 新稿与最接近的已有文章读者阶段不同 |
| **内容深度不可压缩** | 核心论证 >800 词，无法压缩为其他文章的 ≤3 段 | 删掉此稿，核心论点能否在已有文章中讲清？ |

合并决策树：
```
新文章提案
  ├── 搜索意图是否与已有文章重叠 >50%？
  │     ├── 是 → 读者阶段是否不同？
  │     │     ├── 是 → 核心论证 >800 词独立内容？
  │     │     │     ├── 是 → KEEP
  │     │     │     └── 否 → MERGE（核心论证并入已有文章新 H2）
  │     │     └── 否 → MERGE
  │     └── 否 → KEEP
```
**MERGE 执行**：被合并文章核心内容→目标文章新 H2 · 关键词→目标 keywords · 301 到目标 · 更新 README

0.1 SERP Fit 审计 → `references/serp-audit.md` §1

0.2 KEEP/MERGE + 信息增量：Track S ≥2 项独有 / Track C ≥1 项

0.3 **用户确认**（必执行 — Agent 向用户确认后才能进入 Phase 1）：
- 目标 SEO 关键词？目标受众技术水平？
- 发布目的：品牌认知 / SEO 占位 / 产品转化 / 社区讨论
- 竞品内容 URL（2–3 个）— 用于判断信息增量
- 引用的内部页面（如 /discord-voice-changer）是否已上线？

**降级规则**：
```
若触发语已含：主关键词 + 发布目的 + Track +（Track C）category
→ 输出「## User Confirm: inferred from prompt」并列出推断值
→ 用户 1 轮内未纠正则继续
若缺：竞品 URL 或 hub 关系
→ 必须 AskQuestion（最多 2 题）
```

0.4 五必问（Agent 自答）：主关键词 · 发布目的 · 读者 persona · 内链目标 · 相对 SERP 增量

0.5 Gate A：对照 content-graph 冲突表；301 slug → STOP（C4）；独立成文必要性 MERGE 判定

### Phase 1 — Article Brief

> **模板 → `references/mini-example.md`**

### Phase 2 — Slug & Gate B

> **7 原则 + 13 反模式 + 7 问 → `references/slug-gate.md`**

Track S：slug **无年份**；frontmatter `slug` 不含 `/blog/` 前缀。
Track C：slug 与 canonical URL 一致。

### Phase 3 — Outline

按 `article-types.md` H2 模板；Track S 标注 #01–#04 互链。

### Phase 4 — Draft

**加载顺序**（每次 ≤2 文件）：
1. `article-types` + `eeat-framework`
2. `citations` + `presentation-rhythm`（Track S）或 `presentation-cms`（Track C）
3. `writing-style` + `platform-routing`
4. `product-competitors`（对比/产品文）

**核心约束**：
- 产品数字 as of {month} {year}（P1）
- Live vs File 边界（P2）；Assistant vs Mic 分流（P3）
- CTA ≤2；内链白名单见 platform-routing
- 竞品外链 `rel="nofollow noopener"`

### Phase 5 — SelfCheck

#### Track S — 12 维加权（100%）

| # | 维度 | 权重 | 10 分标准 | 参考文档 |
|---|------|:---:|------|------|
| 1 | EEAT & Fact | 20% | 每个可验证 claim 有来源；竞品描述基于官方资料；产品数字 as-of；≥1 竞品优势段 | `eeat-framework` · `citations` · `proof-gate` |
| 2 | Information Gain | 14% | 核心论点在 SERP top 5 找不到等效替代；≥40% 内容为独有框架/分类法/对比维度 | `serp-audit` §8 |
| 3 | Presentation & Rhythm | 12% | 长/中/短段落自然交替；列表占比 ≤类型上限；衔接率 ≥70%；0 处碎片化 | `presentation-rhythm` |
| 4 | Writing & Voice | 11% | 品牌 Voice 5 项全满足；空泛句 ≤2(S)/≤3(C)；≥1 具名竞品+workflow；句段达标 | `writing-style` |
| 5 | SERP Fit | 8% | title 45–65 chars 含主词；desc 140–160 chars 主词前 80；snippet-ready 定义 | `serp-audit` |
| 6 | SEO & Hub-Spoke | 7% | 正文 blog 互链 ≥2；Hub 4-Spoke 四向互链；Related 双向一致（正文）；keywords 仅规划不入 frontmatter | `project-config` §1.8 · `platform-routing` |
| 7 | Structure | 7% | Lead ≤250w + summary block + 描述性 H2 + Conclusion + FAQ（固定 6 题）；无编号 H2 (Track S) | `article-types` |
| 8 | Objectivity | 7% | Comparison/Alternative: Disclosure + ≥1 竞品优势段 · SoundboardPick/CharacterBridge: 产品钩透明，第三方来源≥2 · VoiceActorProfile: 产品≤20%，禁每节CTA · 署名真实 | `proof-gate` P2/P5/P6 |
| 9 | Internal Links | 5% | 内链白名单；无死链；无 forthcoming >1；锚文本描述性；外链 nofollow | `project-config` §1.4 · `platform-routing` |
| 10 | CTA / Conversion | 4% | CTA ≤2；匹配读者阶段；无虚假承诺；Track C Key Takeaways 后 1 次 | `platform-routing` |
| 11 | Depth | 3% | 每 500 词 ≥1 具体例子；无"表格+一句话"空壳；FAQ 非正文复制 | `presentation-rhythm` §4 |
| 12 | Slug / H1 | 2% | 常青无年份；7 原则全 Pass；Gate B 7 问全 Pass；frontmatter slug 格式正确 | `slug-gate` |

**评分细则**（每维 1–10）:
- **10**: 对标 Wirecutter / 行业标杆稿
- **7**: 合格，minor 修订 1–3 处
- **4**: 有明显缺口，不修不能发
- **1**: 系统性失败

Gate Checks：FAQ 固定 6 题 · Intent Boundary (P3) · Stats as-of (P1)

**交付**：Hard Gates 全 Pass + 总分 ≥70 + 无维度 <3/10

**总分等级**:

| 等级 | 分数 | 含义 | 发布建议 |
|------|:---:|------|------|
| **S** | 90–100 | 标杆稿 | 立即发布 |
| **A** | 80–89 | 质量扎实，minor 修订 | 修 1–3 处后发布 |
| **B** | 70–79 | 内容可用，需一轮精修 | 完成 P1 清单后发布 |
| **C** | 60–69 | 结构或可信度有明显缺口 | 不建议发布 |
| **D** | <60 | 需重写 | 退回重写 |

**Track C 等级**：A = 8/8 Pass · B = 7/8 Pass · Fail = ≤6/8 Pass（见 `selfcheck-track-c.md`）

**优化决策矩阵**（分数不够时，指导修复优先级）:

| 问题类型 | 修不修 | 原因 |
|---------|:---:|------|
| 事实错误 | **必修** | 信用不可逆 |
| 死链接 | **必修** | 用户一碰就发现 |
| 字数不达标 | **必修** | 低于阈值 = 核心问题展开不足 |
| 竞品选择性遗漏 | **必修** | 会被竞品或社区抓住 |
| 信息深度不足（空壳段落） | **修** | 用户得不到答案→不会回来 |
| 信息增量不足（拥挤品类） | 取决于 SEO 目标 | 竞争激烈且无独特角度→不如不发布；竞争低→合格概述有价值 |
| 署名问题 | 低成本高收益，**建议修** | 改 author 字段是零成本 EEAT 提升 |
| FAQ 重复正文 | **修** | FAQ 的 SEO 价值取决于独立内容 |
| 漏斗结构太透明 | 部分修 | 不需推翻重建——加利益声明即可 |
| 产品内链指向不存在页面 | **不要加** | 等页面存在后再补 |
| Intro/Conclusion 模板化 | **修** | 连续阅读时 3 篇内可识别模板→信任崩塌 |
| 碎片化表现形式 | **修** | 连续短段+列表轰炸→不像 blog |

#### Track C — 8 维 Pass/Fail

> **执行 rubric、按类型重点、输出格式 → `references/selfcheck-track-c.md`**

Publishability (G+P+C) · Fact · Differentiation · CMS Category Match · Product Tie-in · Links · Voice (CMS) · No Cannibalization (C3)

### Phase 5.5 — Cross-Article Audit

> **完整方法论 + 10 项检查 + 输出格式 → `references/cross-article-audit.md`**

同批 ≥2 篇：CA1–CA10（叙事雷同 · 互链双向 · 产品描述重复率 >30% · Intro 模板化 · Conclusion 模板化 · 核心概念跨篇重复 · 事实矛盾 · 关键词 Cannibalization · 表现形式雷同 · 署名一致性）。任一项 ❌ → 批量交付前必修。

### Phase 6 — Delivery

1. 写入目标路径
2. Article Brief 最终版
3. SelfCheck 报告（按 §5 输出格式）
4. Cross-Article Audit（如有）
5. 提示人类：Track S → 更新 blog/README + content-graph 序号；Track C → 更新 manifest.csv
6. **Meta 预留**：Title 45–65 chars · Description 140–160 chars · 主关键词在前 80 chars

**SelfCheck 输出格式**:

```
## SelfCheck — {slug}

**Track**: S | C  **总分**: XX/100（等级）

| # | 维度 | 权重 | 得分 | 说明 |
|---|------|:---:|:---:|------|
| 1 | EEAT & Fact | 20% | X | ... |
| 2 | Information Gain | 14% | X | ... |
| ... | ... | ... | ... | ... |

**Gate**: G1–G7 [✅/❌] · P1–P6 [✅/❌] · C1–C4 [✅/❌ if Track C]
**Fragmentation Check**: [见 presentation-rhythm §8]

**Source Map**:
| Claim | § | Source | Checked | Confidence |
|------|---|--------|---------|:---:|
| ... | §2 | dubbingai.io | 2026-06-16 | High |

**亮点**: ...
**P1**: [ ] ...
**P2**: [ ] ...
```

---

## §4 内容图谱

> **`references/content-graph.md`** — Phase 0 / Phase 5 加载

Hub：`best-ai-voice-changer`（#01）。Spokes：#02 IntentSplit · #03 HowTo · #04 Alternative。**下一序号 05**。

---

## §5 关键词

> **`references/keywords.md`** — Phase 0 加载

---

## Gotchas — 禁止项（精选）

**结构**：❌ Medo 式编号 H2 · ❌ Track S 用 Key Takeaways 替代 Lead · ❌ 连续 3+ 短段 · ❌ 衔接率 <50% · ❌ 列表占比 > 类型上限

**写作**：❌ 空泛句 Track S >2 / Track C >3 处 · ❌ 禁止措辞（revolutionary/game-changing/seamless/magic） · ❌ 全文 0 长段落 · ❌ 平均句长 <15 或 >24 words

**Slug/链接**：❌ Track S slug 含年份 · ❌ slug 含内部架构词（framework/strategy/diagnosis/complete-guide） · ❌ 链 `/faq`（用 `/questions`）· ❌ 链未上线 `/alternatives/*` · ❌ CharacterBridge 复制程序化页全文

**产品/Proof**：❌ 1000 tones（应为 500+ as of 官网）· ❌ Murf 当 live Discord 工具 · ❌ Voicemod 定价无来源 · ❌ 名人声音教唆冒充

**意图**：❌ Assistant 教程无链 `#how-to-change-google-assistant-voice` · ❌ SFX 生成链 community-sounds · ❌ `top-5-voice-changers` 新稿（301 到 hub）

**流程**：❌ Gate 未全 Pass 交付 · ❌ 一次加载全部 references · ❌ 运行时读 dubbingai-*.md · ❌ 加载整个 cms-export 目录 · ❌ 跨篇 ≥2 篇但未跑 Phase 5.5

---

## Reference Index

| 文件 | 内容 | 加载时机 |
|------|------|----------|
| `references/project-config.md` | 配置 + G1–G7 + frontmatter 双轨 | Phase 0 / 5 |
| `references/proof-gate.md` | P1–P6 | Phase 0 / 5 |
| `references/cms-overlap-gate.md` | C1–C4 + Refresh 模式 | Phase 0 / 2 |
| `references/platform-routing.md` | CTA + 意图→落地页 | Phase 0 / 4 |
| `references/article-types.md` | 12 类 + H2 + Voice | Phase 0 / 3 / 4 |
| `references/content-graph.md` | Hub-Spoke + 冲突表 | Phase 0 / 5 |
| `references/keywords.md` | 主题桶 + 禁抢词 | Phase 0 |
| `references/product-competitors.md` | 竞品 battlecard | Phase 4 / 5 |
| `references/citations.md` | P0/P1/P2 + Source Map | Phase 4 / 5 |
| `references/slug-gate.md` | Gate B · 7 原则 + 13 反模式 | Phase 2 |
| `references/serp-audit.md` | SERP Fit + PAA · IG 审计 §8 · Meta 清单 §7 | Phase 0 / 5 |
| `references/eeat-framework.md` | EEAT 四信号 + 类型来源数 | Phase 4 / 5 |
| `references/presentation-rhythm.md` | 段落节奏 · 碎片化检测 · 列表质量 · 衔接 · 12 项 Checklist | Phase 4 / 5 |
| `references/writing-style.md` | Voice 标准 · 禁止措辞 · 空泛句 10 项 · 句段指标 · AI 原创性 | Phase 4 / 5 |
| `references/presentation-cms.md` | Track C Key Takeaways 等 | Phase 4 / 5 |
| `references/cross-article-audit.md` | CA1–CA10 · 叙事雷同 · 矛盾检测 · Cannibalization | Phase 5.5 |
| `references/selfcheck-track-c.md` | **NEW v1.2** Track C 8 维 Pass/Fail rubric + 等级 | Phase 5 |
| `references/retro-audit.md` | **NEW v1.2** 已发布稿回溯审计 12 维 · Phase 6 Retro mode | Phase 6 / 独立 |
| `references/mini-example.md` | Brief 双范例 | Phase 1 / 3 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.2.1** | 2026-06-16 | 文档自洽 patch：三角→4-Spoke 措辞 · Gate B 7 问 · dim2 IG→serp-audit §8 · CA2→content-graph §4.6 · AskQuestion · project-config/README 版本同步 · Phase 5 Track C 指向 selfcheck-track-c |
| **1.2.0** | 2026-06-16 | P0 SSOT 修复：序号 04→05 · 反模式 12→13 · SelfCheck dim2→serp-audit · Hub→4-Spoke · Objectivity Dubbing 化 · serp-audit IG 审计 §8 · CA6 #02/#03 修正 · content-graph P0 队列 · selfcheck-track-c + cms-overlap §6 Refresh · retro-audit · evals 18→22 · 等级 S/A/B/C/D |
| **1.0.1** | 2026-06-16 | dogfood #04 dubbing-ai-vs-voicemod；content-graph 下一序号 05 |
| **1.0.0** | 2026-06-16 | 初版：双轨 Track S/C · 12 类路由 · G1–G7 + P1–P6 + C1–C4 · 8 Phase · evals |

---

## v1.1 Backlog

| # | 项目 | 优先级 |
|---|------|:---:|
| 1 | `dubbingai-meta-title-description` skill | P1 |
| 2 | 韩文 Naver skill | P2 |
| 3 | manifest slug 冲突 script | P3 |

---

*dubbingai-blog-article · v1.2.1 · 2026-06-16 · B2C gaming/streaming*
