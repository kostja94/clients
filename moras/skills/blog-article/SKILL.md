---
name: moras-blog-article
description: >
  Load when user asks to create, draft, or outline a Moras blog article
  for moras.ai/blog — any topic (TikTok Shop affiliates, product updates,
  industry trends, company news, e-commerce guides, etc.).
  Also load for blog-only title/description optimization
  (references/meta-title-description.md). Do NOT load for TVG landing pages
  or non-blog site metadata.
metadata:
  version: 1.3.1
  project: moras.ai
  locale: en
  market: US TikTok Shop (default; overridable per article topic)
  load-rule: progressive-disclosure
  max-primary-lines: 460
  self-contained: true
---

# Moras Blog Article Creation

为 **https://moras.ai/blog/** 从选题到英文成稿。**本 skill 文件夹可单独分发**：通用 Research / 终审在 `references/portable/`。**范围**：仅英文 `/blog/{slug}`。

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
按 moras-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Pillar|Setup|Production|Research|Framework|Strategy|SideHustle|Diagnosis} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 已有完整稿，仅需发布前终审 | `references/portable/final-audit.md` |
| TVG 落地页长文（`/tiktok-video-generator/*`） | TVG 模板体系 |
| 非博客页 metadata（首页 / TVG / 工具 / 法务） | 见 `_archive/meta-title-description/` 历史稿或产品仓 SEO |
| 非 moras.ai 博客 | 通用 blog skill |
| 非英文内容 | 另建 ZH skill |

### 仅优化 title / description

加载本 skill 后 **只读** `references/meta-title-description.md`，按其中独立任务工作流执行；**禁止**改 H2 / TL;DR / FAQ / 正文，**禁止**跑完整 Phase 0–6。

### Agent 执行顺序

```
§2 类型路由 → §3 Phase 0–6 顺序执行 → 缺信息时先问 Phase 0 五必问 → Gate 不过则 STOP
```

与用户沟通可用中文；正文必须为英文。

---

## §1 项目配置与 Gate 清单

> **完整配置 + G1–G7 + Income Claim Gate + URL 白名单 → `references/project-config.md`**

**Phase 0 / Phase 5 前加载。** 核心阻断项速查：

| Gate | 项数 | 阻断条件 |
|------|:---:|------|
| **G1–G7** | 7 | 事实错误 / 死链 / 无来源数字 / 竞品状态错误 / 产品夸大 / 内链未上线 / 品牌风险 |
| **I1–I5** | 5 | 收入承诺 / 证言滥用 / 政策无时效 / Who-How-Why 缺失 / 复述 SERP |

G1–G7 + I1–I5 全部 Pass 方可进入健康分评估。任一 Fail = 不得交付。

---

## §2 文章类型路由

> **8 类路由表 + H2 模板 + Frontmatter Schema + Voice/合规 + Who/How/Why → `references/article-types.md`**

**Phase 0 / Phase 3 前加载。** 速查：

| 类型 | 词数 | 产品提及上限 | 参考 slug |
|------|------|-------------|-----------|
| Pillar | 3500–5000 | ≤20% | `how-to-make-money-on-tiktok` |
| Setup | 2500–3500 | ≤25% | `tiktok-shop-setup` |
| Production | 2800–3800 | ≤35% | `faceless-tiktok-shop-videos` |
| Research | 2800–3500 | ≤30% | `tiktok-product-research` |
| Framework | 2500–3200 | ≤25% | `tiktok-video-hooks` |
| Strategy | 2500–3200 | ≤30% | `tiktok-captions-hashtags` |
| Side Hustle | 2200–3000 | ≤30% | `tiktok-affiliate-side-hustle` |
| Diagnosis | 2500–3200 | ≤25% | `tiktok-shop-no-sales` |

**路由规则**：`how to make money` / monetization map → Pillar；`setup` / seller vs affiliate → Setup；`without filming` / faceless → Production；`product research` / AI 选品 → Research；`hooks` + framework → Framework；`captions` / `hashtags` → Strategy；`side hustle` / 90-day → Side Hustle；`no sales` / diagnosis → Diagnosis。

**非 TikTok Shop 话题**（产品更新 / 公司动态 / 行业趋势 / 通用电商等）：以上 8 类为 TikTok Shop affiliate 簇专用。若文章主题不属此簇，Agent 在 Phase 0 声明 topic scope ≠ TikTok Shop affiliate，然后按最接近的类型模板创作——跳过 TikTok-Shop-only 约束（如 I3），保持 Moras Voice 和通用规则（G1–G7、引用标准、表现形式）。

---

## §3 创作工作流（7 Phase + 3 Gate）

### 流程总览

```
Phase 0 — Intake & Gate A ─── 不通过 → STOP
Phase 1 — Article Brief
Phase 2 — Slug Design & Gate B ─── 不通过 → 重选 slug
Phase 3 — Outline
Phase 4 — Draft
Phase 5 — SelfCheck & Gate C ─── 不通过 → 修复
Phase 6 — Delivery
```

---

### Phase 0 — Intake & Gate A（选题门禁）

#### 0.0 话题范围判定（先于一切）

Agent 在收到创作任务后，第一步判定话题范围：

| 话题范围 | 判定信号 | 适用规则 |
|---------|---------|---------|
| **TikTok Shop affiliate**（默认） | 关键词含 TikTok Shop/affiliate/佣金/选品/视频/带货 | 全部规则生效（G1–G7 + I1–I5 + TikTok 2026 事实 + affiliate-first） |
| **Moras 产品/公司** | 关键词含 Moras update/changelog/company/team | 跳过 I3/I5（非 TikTok 政策）；Who/How/Why 简化；Voice 仍适用 |
| **通用电商/AI 行业** | 关键词含 e-commerce/AI trends/industry | 跳过 I1–I3（非收入/证言/TikTok 政策）；保留 G1–G7 + 引用标准 + 表现形式 |
| **其他** | 不匹配以上 | Agent 声明 topic scope；Phase 0 五必问补问 #6「此文的 ICP 和 market 是什么？」 |

**硬规则**：Agent 在 Phase 0 第一行输出 `## Topic Scope: {scope}`，后续 Phase 据此决定加载哪些 references 和 Gate。

#### 0.1 快速 Gate：独立成文 + 信息增量

**Step 1 — KEEP/MERGE（3 条件满足 ≥2 → KEEP）**：

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与已有文章关键词重叠 ≤50%（对照 `references/content-graph.md` §4.1 冲突表） |
| 读者阶段不同 | Awareness / Setup / Production / Optimization / Diagnosis |
| 深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**Step 2 — 信息增量 Gate（KEEP 后强制）**：

相对 SERP Top 3，本篇须至少提供 **2 项** 以下之一，否则 **STOP**：

- 独有分析框架（如三机制钩子、五瓶颈诊断）
- 可执行决策表（persona × lane × 预期区间）
- 带方法论的内部观察（n + 时间窗 + 限定语）
- 跨篇 canonical 引用 + 新边界声明（非复制粘贴）

**输出**：KEEP/MERGE 判定 + Information Gain Statement（3 句话：相对 SERP Top3 新增什么）。

#### 0.2 五必问（KEEP 通过后）

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 类型路由确认 |
| 2 | 目标读者？（无受众 affiliate / 小达人 / 卖家） | 深度与 persona |
| 3 | 发布目的？SEO / 品牌 / 转化 | 产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 信息增量交叉验证 |
| 5 | Intent lane：Video / Research / Both？ | 内链目标 |

---

### Phase 1 — Article Brief

> **完整模板 → `references/article-types.md` §2.12 / `references/mini-example.md`**

```markdown
## Article Brief
**Working title**:
**Primary keyword**:
**Search intent**: [ ] Informational  [ ] Commercial  [ ] Transactional
**Article type**: {from §2 route}
**Intent lane**: Video | Research | Both
**Reader stage**: Awareness / Setup / Production / Optimization / Diagnosis
**Publish goal**: SEO / Brand / Conversion
**Target audience**:
**Word count target**:
**Cluster role**: Pillar / Spoke / Standalone
**Pillar link**: /blog/how-to-make-money-on-tiktok（如适用）
**Differentiation angle** (vs SERP top 3):
**Competitor gap**:
**Information Gain Statement** (from Phase 0):
**Canonical concepts to reference** (link only, do not redefine):
**Primary product link(s)**:
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Compliance notes**: {based on topic scope — US-only if TikTok Shop; affiliate-first if TikTok Shop; no TikTok official if references TikTok; testimonial rules if contains GMV claims}
```

---

### Phase 2 — Slug Design & Gate B（Slug 门禁）

> **7 原则 + 12 反模式 + 竞品基准 + Design-Time 6 问 → `references/slug-gate.md`**

1. 生成 2–3 个 slug 候选（`/blog/...`）+ 推荐项
2. 跑 §13 Design-Time 决策框架 6 问
3. 对照 12 项反模式速查
4. 竞品基准检查（搜 Google → 对比前 5 竞品 slug）

**Gate B**：全部 6 问通过 + 0 项反模式命中 → 定 slug。任一项不通过 → 重选。**禁止 Flag 过关。**

同步：SERP Fit 快速对照 + 完整 frontmatter（title、description、slug、date）；`isoDate` 须与 portfolio 内已有日期不重复（一天一篇，取最晚 date +1 天）。title/description 计字符与自检 → `references/meta-title-description.md`。

---

### Phase 3 — Outline

按 references/article-types.md 对应类型的 H2 模板展开。每节标注：目标词数、关键词位置、内链占位、Moras 出现计划。

---

### Phase 4 — Draft

> **Voice 正向/禁止 → `references/article-types.md` §8 · 引用分级 → `references/citations.md` · 表现形式 → `references/presentation.md`**

**Phase 4 加载顺序**：article-types.md（Voice）+ citations.md（引用格式）+ presentation.md（节奏标准）。

**核心约束**：
- Affiliate-first（commission、showcase、product link）；seller 次之
- P0 数字有来源链接；P1 趋势有官方 docs + as of date
- 长段落 ≥3 个（≥4 句）；列表占比 ≤ 类型上限；无连续短段集群
- 漏斗符合类型标准（Pillar: 后 40%+ 出现 Moras；Research: 工具公平对比）
- CTA ≤2 次；US-only

---

### Phase 5 — SelfCheck（创作自检）

创作完成后、交付前的自检。**这是写作质量检查，不是独立审核——发布前终审用 `references/portable/final-audit.md`。**

#### 5.1 Hard Gates（全部 Pass 方可交付）

逐项对照 `references/project-config.md`：

| Gate | 项 | Pass? | 任一 Fail → STOP |
|------|----|:---:|------|
| **G1–G7** | 事实错误 / 死链 / 无来源数字 / 竞品状态 / 产品夸大 / 内链未上线 / 品牌风险 | | 修复后重检 |
| **I1–I5** | 收入承诺 / 证言滥用 / 政策无时效 / Who-How-Why / 复述SERP（非 TikTok Shop 话题自动 Pass） | | 修复后重检 |
| **Slug** | 通过 §13 全部 6 问 + 0 项反模式 | | 重选 slug |

#### 5.2 轻量健康分（1–5，Gate 全部 Pass 后评估）

每个维度快速打分——**这是创作反馈，不是审核等级**。分数含义：
- **5**: 满足该维度全部标准，无明显瑕疵
- **4**: 基本满足，有 1–2 处可改进（交付后人工修）
- **3**: 部分满足，有明显缺口但非阻断（标注 P1）
- **2**: 不满足核心标准（标注 P1，建议修复后交付）
- **1**: 严重不满足（等同 Hard Gate Fail，不得交付）

| # | 维度 | 分 | 快速判据 |
|---|------|:---:|------|
| 1 | **Fact / E-E-A-T** | /5 | P0 数字全有来源？政策有时效？竞品≥1优势？≥1场景非Moras更合适？ |
| 2 | **Differentiation** | /5 | 独有框架/表格≥1？句级重复<30%？信息增量2项已验证？ |
| 3 | **Presentation** | /5 | 长段落≥3？列表占比≤上限？0碎片化集群？表格前后有分析？ |
| 4 | **Writing / Voice** | /5 | 五正向全满足？禁词0？空泛句≤2？≥1具体scenario？ |
| 5 | **Objectivity** | /5 | 漏斗符合类型标准？产品≤上限？无贬低措辞？Who/How/Why齐备？ |
| 6 | **Structure / Links** | /5 | TL;DR 置顶（长描述+bullets）+Conclusion+FAQ？blog互链≥2？forthcoming≤1？锚文本语义化？ |
| 7 | **SEO** | /5 | title含P1？description 140–160？keywords≥5？snippet-ready定义？ |
| 8 | **Depth** | /5 | 词数在区间？每~500词≥1例子？FAQ 固定 6 题 + ≥1 题独立？ |
| 9 | **Moras + Compliance** | /5 | US-only？品牌正确？Cannibalization清晰？无TikTok暗示/GMV承诺？ |
| 10 | **Conversion** | /5 | CTA≤2？匹配读者阶段？CTA前有独立价值？ |

**整体**: __/5.0（10维平均）　🟢≥4.0 / 🟡3.0–3.9 / 🔴<3.0

**交付标准**：Hard Gates 全部 Pass + 无 🔴 维度（<3.0）。🟡 维度标注 P1 修复项。

#### 5.3 SelfCheck 输出格式

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| G1–G7 | Pass | |
| I1–I5 | Pass | (or: I3 skipped — non-TikTok-Shop topic) |
| Slug | Pass | |

### Health Check
| # | Dimension | Score | Notes |
|---|-----------|:---:|-------|
| 1 | Fact/E-E-A-T | 4/5 | P0数字全有来源；竞品优势已承认；可补1处时效标注 |
| 2 | Differentiation | 5/5 | 独有三机制框架+品类匹配表 |
| ... | ... | ... | ... |
**Overall**: 4.2/5.0 🟢

### Information Gain Statement
{3 sentences vs SERP Top3}

### Source Map (internal)
| Claim | § | Source | Checked | Confidence |
|------|------|------|------|:---:|
| ... | ... | ... | 2026-06-15 | High/Med/Low |

### Cannibalization Check
| vs | Boundary | Clear? |
|----|----------|:---:|
| /blog/{slug-01} | ... | ✅ |
| /tiktok-video-generator | blog=教育, TVG=交易 | ✅ |

**🟡 P1 fixes** (from Health Check):
- [ ] ...

**Human decisions** (⚠️ items):
- [ ] ...
```

---

### Phase 6 — Delivery

1. **写入文件** `blog/NN-{working-slug}.md`（Agent 据工作目录推断）
2. **Article Brief 摘要**（Phase 1 最终版）
3. **SelfCheck 自检表**（Phase 5 完整输出：Hard Gates + Health Check + Info Gain + Source Map + Cannibalization）
4. **Meta 复核**（可选）：按 `references/meta-title-description.md` 计字符并跑四条自检；只改 frontmatter `title`/`description`。
5. **Human handoff**：提示更新 `blog/README.md` 文件表 + planned/live 标注。

---

## §4 已有内容图谱

> **文件表 + Hub-Spoke + Cluster B 发布看板 + Canonical Registry + 跨篇边界声明 → `references/content-graph.md`**

**Phase 0 / Phase 5 加载。** 速查：下一序号 **25**（#15/#17/#23/#24 已删/合并）。Pillar: `how-to-make-money-on-tiktok` → Cluster A spoke + Cluster B Platform Ops。

---

## §5 关键词速查

> **P0/P1/P2 + 市场策略 → `references/keywords.md`**

**Phase 0 加载。**

---

## §6 产品、竞品与 TikTok Shop 2026 事实

> **产品事实 + 竞品公平摘要 + TVG 白名单 + 合规红线 + Cannibalization + TikTok 2026 硬事实 → `references/product-competitors.md`**

**Phase 4 / Phase 5 加载。**

---

## §9 创作 vs 审核 vs Meta（严格边界）

| | **moras-blog-article** | **references/portable/final-audit.md** | **references/meta-title-description.md** |
|------|:---:|:---:|:---:|
| 做什么 | **生成**文章 | **审核**文章（打分+报告） | **生成/优化** title/description |
| 产出 | .md 成稿 + SelfCheck | 审核报告 (S/A/B/C/D 等级) | frontmatter metadata |
| 时机 | 选题→成稿 | 成稿后，发布前 | Phase 2 或独立任务 |
| 评分 | 轻量健康分 (1–5, 🟢🟡🔴) | 加权评分 (0–100, S-D) | 计字符 + 四条自检 |

**硬规则**：
- blog-article Phase 5 SelfCheck = **创作质量自检**，健康分供人类快速判断文章状态，不等同审核等级
- `references/portable/final-audit.md` 的加权评分（S/A/B/C/D）= **独立发布终审**，是最终质量判定
- 两者不可互相替代

| 任务 | 入口 | 严格边界 |
|------|-------|---------|
| 写正文 | **blog-article** Phase 0–6 | 禁止一次加载全部 references |
| title/description 专项 | 本 skill → **`references/meta-title-description.md`** | 禁止改 H2 / TL;DR / FAQ / 正文 |
| 博客 metadata 初稿 | Phase 2 + 同上 reference | 45–65 / 140–160；P1 见 content-graph |
| 发布前终审 | **`references/portable/final-audit.md`** | 十维加权 + P0 Gate |
| Phase 0R | **`references/portable/research-triangle.md`** | R1–R3 |

---

## Gotchas — 禁止项清单（34 条）

创作时逐条对照。任一项触发 = 对应维 Fail。

**结构与格式**：
1. ❌ 不要在 `## TL;DR` 前放独立 Lead 段（hook 并入 TL;DR 长描述）
2. ❌ 不要 TL;DR 仅 bullet、无长描述段（须 60–110 词 BLUF + 3–6 bullets）
3. ❌ 不要用 `## Related articles` 模块（内链分布在正文）
4. ❌ 不要两篇共用同一 `isoDate`（发布日期一天一篇，新稿取最晚 date +1 天）
5. ❌ 不要编号 H2（`## 1.` `## 2.`）——用描述性标题
6. ❌ 不要把 Framework 文写成 "50 hooks you can copy" 列表
7. ❌ 不要连续 3+ 短段落（≤2 句）集群
8. ❌ 不要"表格+一句话然后跳下节"——表格后 ≥2 句分析
9. ❌ 不要 H2 后直接列表/表格——先写引导段

**Slug 与链接**：
10. ❌ 不要 slug 缺 `/blog/` 前缀
11. ❌ 不要文件名 slug 当 URL slug（`hooks-framework` ≠ `tiktok-video-hooks`）
12. ❌ 不要 slug 含内部架构词（framework/strategy/diagnosis/guide/two-paths）
13. ❌ 不要链 `/use-cases/*` `/app/*` `/auth/*` `/admin/*`（G6）
14. ❌ 不要 forthcoming >1 个
15. ❌ 不要锚文本 "click here" / "learn more" / "this article"
16. ❌ 不要为凑内链数量在无关段落硬插 blog 链（自然优先；入链 0 的 spoke 仅在确有语境时补 1 条）
17. ❌ 不要同篇对同一 slug 链超过 2 次（除非结论段有独立强语境）
18. ❌ 不要在 `## TL;DR` 或 FAQ 内放内链

**品牌与受众**：
19. ❌ 不要写 Morris（统一 **Moras**）
20. ❌ 不要 seller 作 title 主称谓——当文章面向 TikTok Shop affiliate 时（非 TikTok Shop 话题可依实际 ICP 调整）
21. ❌ 不要声称 TikTok / ByteDance 官方合作或认证（非 TikTok 话题自动跳过）
22. ❌ 不要用 `| K2 Lab` / `| K2LAB` 作品牌后缀（统一 `| Moras`）

**数据与引用**：
23. ❌ 不要裸引 $15.8B / 73% creators 无来源 URL（G3）
24. ❌ 不要 "studies show" / "industry reports indicate" 泛引（I5）
25. ❌ 不要把证言 GMV 写成普适收入保证（I1 / I2）
26. ❌ 不要 TikTok Shop 政策无 "as of {date}" + 官方链（I3；非 TikTok Shop 话题自动跳过）
27. ❌ 不要用 Low confidence 来源支撑核心论证
28. ❌ 不要内部数据无 "based on internal analysis, n≈X"

**Cannibalization**：
29. ❌ 不要 Production 文抢 TVG vertical 的 `{category} AI TikTok generator` P1
30. ❌ 不要 product-research 博客抢 `/product-research` 工具页 P1
31. ❌ 不要 Vertical vs Vertical 品类词可互换（toiletry-bag ≠ mattress）
32. ❌ 不要 Pillar 完整展开 Spoke 核心内容（引述 1–2 句 + link）

**流程与合规**：
33. ❌ 不要 G/I/Slug Gate 未全部 Pass 就交付
34. ❌ 不要为凑字数写偏离 ICP 的长篇（TikTok Shop 文 ICP = affiliate；其他话题依实际 ICP）
35. ❌ 不要 "Imagine you're…" 虚构开头
36. ❌ 不要一次加载全部 references（渐进式加载，一次 ≤2 个）
37. ❌ 不要混淆创作自检与独立审核——本 skill 的 SelfCheck 是写作质量检查（1–5 健康分），发布前终审用 `references/portable/final-audit.md`

---

## Reference Index

创作时按需加载（一次最多 2 个）：

| 文件 | 内容 | 加载时机 |
|------|------|------|
| `references/project-config.md` | §1 配置 + G1–G7 + I1–I5 + URL 白名单 | Phase 0 / Phase 5 |
| `references/article-types.md` | §2 八类路由 + H2 模板 + §8 Voice + Who/How/Why | Phase 0 / Phase 3 / Phase 4 |
| `references/content-graph.md` | §4 Pillar–Spoke + Cluster B Tier/SuccessMetric + Canonical + §7 命名 | Phase 0 / Phase 5 |
| `references/keywords.md` | §5 P0/P1/P2 关键词 | Phase 0 |
| `references/product-competitors.md` | §6 产品/竞品/合规/TVG + TikTok 2026 事实 | Phase 4 / Phase 5 |
| `references/presentation.md` | §11 表现形式与表达节奏 | Phase 4 |
| `references/citations.md` | §12 证据链 + Source Map 模板 | Phase 4 / Phase 5 |
| `references/slug-gate.md` | §13 Slug 设计审查（7 原则 + 12 反模式 + 决策框架） | Phase 2 |
| `references/meta-title-description.md` | 博客 title/description 长度、自检、独立优化工作流 | Phase 2 / title-only 任务 |
| `references/mini-example.md` | §10 Framework Brief + Outline 范例 | Phase 1 / Phase 3（参考） |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.3.1** | 2026-08-04 | 吸收原 `moras-meta-title-description` 博客规则 → `references/meta-title-description.md`；title-only 任务改走本 skill；全站 meta skill 归档至 `_archive/` |
| **1.3.0** | 2026-06-15 | 定位修正：Phase 5 从"11维加权评分（S/A/B/C/D）"改为"Hard Gates (Pass/Fail) + 轻量健康分 (1-5, 🟢🟡🔴)"；删除 ≥80 硬线、S-D 等级、权重体系；明确创作skill≠审核skill（§9 角色表）；措辞统一：评分→自检/健康分；evals 改用 Gate 断言；references 清除评分权重残留 |
| **1.2.0** | 2026-06-15 | 架构重构：1252 行单文件→主文件 ≤450 行 + 9 个 references/；新增 3 Gate 体系（Gate A 选题 / Gate B Slug / Gate C 发布）；新增 Income Claim Gate I1–I5；Phase 0 新增信息增量 Gate（≥2 项独有）；新增 Gotchas 30 条；新增 eval/ 回归套件；TikTok Shop 2026 硬事实表；Who/How/Why 强制模块；渐进式加载规则 |
| **1.1.0** | 2026-06-15 | +§11 表现形式、§12 证据链、§13 Slug Gate；Phase 6 加权评分；引用格式模板；品牌色 hex；文件表+主站状态列 |
| **1.0.0** | 2026-06-15 | 初版：8 类路由 + 7 Phase + 13 维自检 + Pillar–Spoke 图谱 + Canonical Registry |

---

*moras-blog-article · v1.3.1 · 2026-08-04 · US TikTok Shop*
