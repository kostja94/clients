# Create Article — Alignify 统一文章创建 Skill

> **版本**：v2.5 · 2026-08-27  
> **质量档位**：**每篇均为 flagship** — 无 lite/standard 降级；Research、Moat、BLUF、SelfCheck、终审全链路必过。  
> **部署仓**：`E:\自有部署项目\alignify production`  
> **上下文仓**：`E:\clients\Alignify`  
> **终审**：Step 10 → audit-ready → [`../audit-article/SKILL.md`](../audit-article/SKILL.md) → publish-ready

---

## 核心原则

1. **Flagship 固定** — 每篇须 Moat、Answer Blocks、完整 Research、BLUF、12 维 SelfCheck；发布线终审 **≥80**，目标 **S 级 ≥90**。  
2. **内容决定架构** — 章节**纯粹由题材与读者任务决定**；[`templates.md`](./rules/templates.md) Part 0 与 [`sections.md`](./rules/sections.md) 仅为**建议**，**禁止**一比一复刻存量骨架。A 层硬底线不变。新文统一 **`content/blog/`**。  
3. **双轨 native 成稿** — ZH/EN **各自独立撰写**（可并行 Subagent），共享 Brief + 锚点 id；**禁止**先写一语种再翻译另一语种。Step 09c 做信息对等对比。见 [`rules/content-locale.md`](./rules/content-locale.md)。  
4. **知识块 ≠ 文章** — 素材须重写，禁止整段复制。  
5. **创作 / 终审分离** — Step 10 自审 → audit-ready；**另一 Agent 或人类** 跑 audit-article → publish-ready。  
6. **素材源可外置** — 个人知识库为 campaign SSOT；Brief 登记路径即可。  
7. **TL;DR/FAQ/Refs → JSON** — Brief 采用则 Step 08 注册三 JSON 侧车（E10）；**不写 md**；见 `anatomy.md` §二·一。  
8. **不清楚就问用户** — 对主叙事、中文主称、slug、结构、是否写 Author POV 等**任何不确定项**，在聊天中问用户后再继续；禁止静默假设。见 [`rules/intake-questions.md`](./rules/intake-questions.md)。  
9. **垂类 + 产品独占** — Tools 新文 **3 款 H3 深度足够**（≥2 硬底线）；**同一产品仅一篇 canonical Best H3**；选题偏窄意图 spoke。见 [`rules/product-coverage.md`](./rules/product-coverage.md)。

---

## 何时使用

- [ ] 素材 SSOT 就绪，满足其一即可：
  - Alignify 知识块：`knowledge/{tools,seo,marketing,insights}/{slug}.md`
  - **外部知识库**（如 `E:\个人知识库\…\{slug}.md`）— 在 Brief 中登记路径，**不强制**迁入 `knowledge/`
- [ ] 新建或重写正式页；slug 未注册

**不适用**：素材未完成 · 仅内链优化 · 仅 Meta 微调 · 已 audit-ready 仅需终审（→ audit-article）

---

## 类型决策

| 知识块目录 | `articleType` | **新文** 路由 | **新文** 正文路径 | **存量**（不重迁） |
|-----------|---------------|-------------|-----------------|-------------------|
| `knowledge/tools/` | `best-ranking` | `/blog/{slug}` | `content/blog/` | `/tools/{slug}` · `content/tools/` |
| `knowledge/seo/` | `seo-guide` | `/blog/{slug}` | `content/blog/` | `/seo/{slug}` · `content/seo/` |
| `knowledge/marketing/` | `marketing-strategy` | `/blog/{slug}` | `content/blog/` | `/marketing/{slug}` · `content/marketing/` |
| `knowledge/insights/` | `insights-analysis` | `/blog/{slug}` | `content/blog/` | `/insights/{slug}` · `content/insights/` |

> **路由约定（2026-08-28）**：**所有新文章**（任意类型）统一 **`content/blog/` + `/blog/{slug}`**（中文 `/zh/blog/{slug}`）。存量旧路径**仅维护更新，不重迁 URL**。详见 [`rules/article-types.md`](./rules/article-types.md)。

---

## 流程总览（Flagship）

```
01 Intake — Gate A（KEEP/MERGE/STOP）+ 大纲草案（有不确定项 → 先聊天问用户）
    ↓ PASS
02 Research — Gate 0R（全类型必做）+ Article Brief 定稿
    ↓ PASS
03 Keywords + README（Brief primary keyword → 关键词表 + Hub README）
04 Screenshots — **仅** best-ranking / legacy；其余 **跳过** → 05
    ├─ [Outline 3.5] — **同批 ≥2 篇**；单篇标 N/A（Step 05 前）
    ├─ Subagent ZH：05 起草 → 06 地道化（content-locale Part 2–3）
    └─ Subagent EN：09 独立成稿 → 09b Pass（Part 4）— **可与 ZH 并行**
07 内链 + Internal Link Plan（按 articleType 选 internal-links Part）
08 Meta + Config + Final CTA + publishDate/modifiedDate
09c 双语对等对比（Part 5）
10 SelfCheck — Gate C → audit-ready
    └─ [Cross-Article 5.5] — **同批 ≥2 篇** audit-ready；单篇标 N/A
    ↓
audit-article — Final ≥80 → publish-ready
    ↓
[可选] article-zh-locale-pass — 中文地道化后置轮 → [`../../article-zh-locale-pass-spec.md`](../../article-zh-locale-pass-spec.md)
    ↓
人类发布（发布前复核 Step 08 日期字段）
OG 封面（Step 08 后 / publish 前）— fal GPT Image 2，EN/ZH 分图 → [`../ops/og-covers.md`](../ops/og-covers.md)
```

**Phase 0 首行强制输出**：

```
## QualityTier: flagship（固定）
## ArticleType: {type}
## BatchCount: {1 | N≥2} — {slug 或 slug 列表}
## InvestmentScore: {X.X} — {摘要}
## Gate A: KEEP | MERGE → {slug} | STOP
```

---

## 步骤文档

| 步骤 | 文档 | 产出 |
|------|------|------|
| 01 | [`01-intake.md`](./01-intake.md) | Gate A + 大纲草案 |
| 02 | [`02-research.md`](./02-research.md) | Research Log + Brief + Gate 0R |
| 03 | [`03-keywords.md`](./03-keywords.md) | Brief → 关键词表 + Hub README |
| 04 | [`04-screenshots.md`](./04-screenshots.md) | 截图（**仅** best-ranking / legacy） |
| 05–06 | [`rules/content-locale.md`](./rules/content-locale.md) Part 2–3 | ZH md + 地道化 |
| 07 | [`07-internal-links.md`](./07-internal-links.md) | 内链 + Link Plan |
| 08 | [`08-meta-config.md`](./08-meta-config.md) | Meta + config + Final CTA + **publishDate/modifiedDate** |
| 09–09c | [`rules/content-locale.md`](./rules/content-locale.md) Part 4–5 | EN 独立成稿 + 对等对比 |
| 10 | [`10-quality-gates.md`](./10-quality-gates.md) | Gate C → audit-ready |
| — | [`../audit-article/SKILL.md`](../audit-article/SKILL.md) | publish-ready |
| —（可选） | [`../../article-zh-locale-pass-spec.md`](../../article-zh-locale-pass-spec.md) | ZH 地道化后置轮 |

> **步骤编号说明**：01–04 独立文档 · 05–06 / 09–09c → [`content-locale.md`](./rules/content-locale.md) · 07 内链 · **08 = Meta + 日期 + CTA**（无 Step 11/12）· 10 自审 · 终审后人类发布。

---

| 主题 | 文档 |
|------|------|
| Gate 语义 | [`rules/gates.md`](./rules/gates.md) |
| Gate 回溯 | [`rules/gate-rollback.md`](./rules/gate-rollback.md) |
| Intake 问答 | [`rules/intake-questions.md`](./rules/intake-questions.md) |
| Article Brief | [`rules/article-brief.md`](./rules/article-brief.md) |
| Research 三角 | [`rules/research-triangle.md`](./rules/research-triangle.md) |
| SelfCheck 12 维 | [`rules/selfcheck.md`](./rules/selfcheck.md) |
| 双语正文 | [`rules/content-locale.md`](./rules/content-locale.md)（05–06 ZH · 09–09c EN · 双轨成稿） |
| 双语术语 | [`rules/locale-glossary.md`](./rules/locale-glossary.md) · [`locale-glossary.json`](./rules/locale-glossary.json) |
| GTM 禁腔 | [`rules/gtm-prose-voice.md`](./rules/gtm-prose-voice.md) |
| 中文英混 | [`rules/zh-en-mixing.md`](./rules/zh-en-mixing.md) |
| BLUF / 段落 | [`rules/presentation.md`](./rules/presentation.md) |
| 文案质量 · Swap Test | [`rules/copy-quality.md`](./rules/copy-quality.md)（M1/M2/M3 · 五维） |
| **产品覆盖 · 垂类独占** | [`rules/product-coverage.md`](./rules/product-coverage.md) |
| Extractability | [`rules/extractability-checklist.md`](./rules/extractability-checklist.md) |
| S 级清单（**可选**，非 Gate C） | [`rules/perfect-article-checklist.md`](./rules/perfect-article-checklist.md) |
| 结构原则 | [`rules/anatomy.md`](./rules/anatomy.md) |
| 章节规范 | [`rules/sections.md`](./rules/sections.md) |
| 质量检查 | [`rules/quality-checklist.md`](./rules/quality-checklist.md) |
| Final CTA | [`rules/sections.md`](./rules/sections.md) Part 5 |
| 内链 | [`07-internal-links.md`](./07-internal-links.md) → [`rules/internal-links.md`](./rules/internal-links.md)（Part 1–2 + **按类型** Part 3/4/4.5/5 + Part 8） |
| **Marketing slug 锁定** | [`rules/marketing-slug-notes/`](./rules/marketing-slug-notes/)（User 确认边界 · 如 `creator-challenge-program`） |
| **SEO slug 锁定** | [`rules/seo-slug-notes/`](./rules/seo-slug-notes/)（GSC 提交 · Platform properties 等 · 外部 KB SSOT） |

完整索引：[`rules/README.md`](./rules/README.md)

---

## 渐进式加载

默认只读本 `SKILL.md` + 当前 Step 文档。**双语正文**（05–06 / 09–09c）读 [`rules/content-locale.md`](./rules/content-locale.md) **对应 Part**；术语查 [`rules/locale-glossary.md`](./rules/locale-glossary.md) Part 1–3。**一次最多再读 2 个** 其他 `rules/` 文件。禁止一次性加载全部 references。

**文档层级**（避免把可选当 Gate）：

| 层级 | 含义 | 示例 |
|------|------|------|
| **Gate 必过** | Step checklist + H0–H4 / 12 维 Fail 线 | `selfcheck.md` · `quality-checklist.md` · `word-counts.md`（H4 下限）· [`copy-quality.md`](./rules/copy-quality.md) **Part 2**（Swap Test · L0 阻断 Step 06） |
| **Step 必读** | 当前 Step 文档头注 SSOT | Step 07 → `internal-links` 对应 Part |
| **C 层参考** | 篇幅软建议 · M1/M2/M3 验收清单；L2 为 flagship 目标 | [`copy-quality.md`](./rules/copy-quality.md) **Part 3–4** |
| **参考菜单** | 禁止一比一复刻存量骨架 | [`templates.md`](./rules/templates.md) Part 0 + 当前类型 Part 2–5 **一节** |
| **索引** | 查表用，非步骤 | [`rules/README.md`](./rules/README.md) |

---

## Gotchas

- ❌ Gate 未 Pass 交付 · ❌ 跳过 Step 02 Research · ❌ 无 Moat 动笔 · ❌ FAQ 复制正文  
- ❌ blog md 用 GFM 表格或 `-`/`1.` 列表（须 `childrenHtml` HTML；见 `anatomy.md` §四·一 · E33/E34）
- ❌ frontmatter `heroHtml:` / `heroContent:` / `howTo:`（E44 — 全站禁止）
- ❌ Brief 采用 TL;DR/FAQ/Refs 但未注册 JSON，或 Brief 省略但 JSON 仍留键（E10）
- ❌ 表前短桥接 / 孤立标签 / 免责声明独段（E40–E42；须跑 `audit-marketing-md-render.py`）
- ❌ 自审后直接发布（须 audit-article）· ❌ Investment Score <3.0 仍 KEEP（须 MERGE/STOP 或改角）  
- ❌ P0 数字无 Source Map 行 · ❌ 为凑节加空章
- ❌ **新 slug** publishDate 与全站已有 slug 重复（须 Step 08 跑 `next-publish-date.mjs --check`；见 `08-meta-config.md` §发布日期）
- ❌ 把 skill 示例日期当「今天」——以执行 Step 08 的实际 UTC+8 日历日为准
- ❌ References 收录与本文类似的第三方策略文；策略/Blog 文仅 **事件相关**引用（[`sections.md` Part 2.3 §3.2](./rules/sections.md#part-23-references--参考文献)）
- ❌ 中文英译腔 / 英文逐句翻译 ZH / 先写一语种再译另一语种（须 `content-locale.md` Part 3·4 Pass + Part 5 09c + `locale-glossary`）
- ❌ Marketing/Blog 无 Kostja 第一人称判断（Brief **Author POV** 须在某节内兑现；**不要求**独立 `#author-take`）
- ❌ 正文 meta 预告未发布 skills/runbook（E49）
- ❌ Insights/架构文默认套 `#should-you-do-this` + `#author-take` 双收束（E50）
- ❌ 个人知识库已有 SSOT 仍创建 `knowledge/marketing/{slug}.md` 副本（E32）
- ❌ `git commit attribution` 中文译成「Git 提交归因 / 提交归因」（须 **AI 提交署名**；E39 · `locale-glossary.md` Part 2.1）
- ❌ 未在聊天中确认用户已明示的禁忌或主叙事就动笔（见 [`intake-questions.md`](./rules/intake-questions.md)）
- ❌ 把 SSOT 文件名默认当文章主线（角度不清楚时必须问用户）
- ❌ 新 slug 未写 `cta-config.json` 的 `slugs.{slug}`（页底落入 fallback 通用文案；E43）
- ❌ Swap Test 失败仍过 Step 06（L0 模板壳 · 见 [`copy-quality.md`](./rules/copy-quality.md) Part 2）
- ❌ M2 cluster 无 Brief `swap neighbors` 仍批量送审
- ❌ Tools 新文 Best H3 **>5 款**无 Brief + 用户确认（见 [`product-coverage.md`](./rules/product-coverage.md)）
- ❌ 同一产品在多篇拥有 **完整 Best H3**（须保留 1 篇 canonical，他文链回 · E51）
- ❌ Step 02 无 `Product roster` / `Product dedup check` 仍开写 best-ranking

---

*create-article · v2.5 · 2026-08-27 · complements audit-article*
