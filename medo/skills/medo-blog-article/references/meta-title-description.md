# MeDo Blog — Meta Title & Description

> **何时用**：Phase 2（生成 frontmatter）或独立「只改 title / description」任务。**硬性规则**：独立任务只读本文件；**禁止**改 H2 / TL;DR / FAQ / 正文；**禁止**跑完整 Phase 0–6 创作流程。
> Slug 规则不在此处——见 `slug-gate.md`。关键词优先级见 `keywords.md`。

---

## 1. 硬性长度（输出前必计字符）

| 字段 | 目标 | 硬上限 | 说明 |
|------|------|--------|------|
| **title** | 45–65 | 65 | editorial；可含年份（slug 不含） |
| **description** | 120–160 | 160 | benefit + 主意图关键词 |

超限 = 未完成。输出时标注实际字符数。

---

## 2. Title / Description 公式（按类型）

| 类型 | Title 公式 | Description 要点 |
|------|-----------|-------------------|
| PillarTutorial | How to {action} with AI — {audience qualifier} for 2026 | benefit + primary keyword + native iOS/Android |
| GlossaryGuide | What Is {term}? A 2026 Guide for Non-Developers | definition + who it's for + link to mobile |
| Comparison | Best {category} in 2026: An Honest Comparison | compared dimensions + non-developer |
| Alternative | MeDo vs {Competitor}: Which {outcome}? | both products named + decision frame |
| PublishGuide | How to Publish an AI-Built App to the App Store in 2026 | steps + TestFlight + rejections |
| DecisionGuide | {A} vs {B}: Which Path for AI-Built Apps? | objective trade-offs |
| Diagnosis | {Problem} for AI-Built Apps (and How to Fix Them) | pain point + actionable fixes |
| UseCase | How to Build a {app type} with AI | end-to-end + weekend feasible |
| Announcement | {Product update} — What It Means for Your AI-Built Apps | change + user impact |

**Title 公式另见 `article-types.md` §3**（各类型 H2 模板首行；meta 与正文措辞互补，不复制）。

---

## 3. 核心原则

| 规则 | 说明 |
|------|------|
| **一页一词一组** | title/description 的主关键词来自 `keywords.md` 或 Brief |
| **主题词入 title** | 文章核心主题必须在 title 中显性出现 |
| **description 展开** | 写该文独有角度/价值，**不整句重复 title** |
| **与 H1 同主题** | frontmatter `title` = 正文 H1（模块顺序 YAML → H1 → TL;DR）；SERP 与正文同一件事 |
| **native 限定** | 泛 `AI app builder` 词须加 mobile/native 限定（A4 防护） |
| **品牌** | 不加 `\| MeDo` 后缀（品牌词在正文自然出现即可） |
| **唯一性** | 全站无 duplicate title/description（对照 `content-graph.md`） |

### 禁抢词提醒（A4）

以下词的 **H1 / title 主位** 保留给工具页/首页（`keywords.md` §7）：`ai mobile app builder`（工具页 `/ai-mobile-app-builder`）、泛 `AI app builder`、`no code full stack app`、`vibe coding platform`。Blog 用长尾/场景词。**允许进 title 的对比词**：`MeDo vs Lovable`、`lovable alternative`、`best AI mobile app builders`（已有 canonical #03）。

---

## 4. 自检（四条）

1. 若去掉品牌名，title 能否让人猜出 **这是哪一篇**？
2. description 是否至少含 **1 个该文专属主题词**？
3. 主关键词是否在 title 中出现？读者收益是否在 description 中？
4. title ≤65、description ≤160？

---

## 5. 独立任务工作流（只改 title/description）

1. 读目标 `.md` 的 frontmatter + H1/TL;DR（确认主题与结论）
2. 查 `content-graph.md` 主关键词 + 对照 cannibalization / 禁抢词
3. 按 §2 公式产出 2–3 组候选（title + description）；每组标注字符数
4. 跑 §4 四条自检 + A4 禁抢词检查
5. **只改** frontmatter `title` / `description`（及必要时 `updated`）；禁止改 H2 / TL;DR / FAQ / 正文——输出建议后**等用户确认**才写入

### 输出格式

```markdown
## Meta — {slug}

**Primary keyword**: …

**Recommended title** ({n} chars)
> …

**Recommended meta description** ({n} chars)
> …

**Self-check**: 四条全 Pass / {Fail 项}
**Notes**: {cannibalization / A4 / updated 日期}
```

批量：表格列 `slug | Title (chars) | Description (chars)`。

### GSC 驱动（可选）

高展示低 CTR → 优先改 title/description → 2–4 周再看；用实际 query 校正主词，避免频繁改动。

---

*medo meta-title-description · v2.1 · 2026-09-09 · 吸收 keywords.md §8 + clink/moras meta-title-description 模式*
