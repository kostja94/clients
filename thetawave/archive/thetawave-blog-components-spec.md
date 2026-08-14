# ThetaWave Blog 与共享组件规范

> **Blog 结构与 frontmatter（2026-07 起）**：以 [skills/blog-article/SKILL.md](../skills/blog-article/SKILL.md) **v2.2.3** 为准——`## Key takeaways` → `## Introduction` → 正文 H2；FAQ **仅写在正文**；YAML **禁止** `faq`、`keywords`、`related`、`final_cta`、`faq_subtitle`；**必填** `category`。

> **本文档职责**：Blog 详情页作者页、上下文内链、全站 FAQ（`<SiteFAQ />`）与 Final CTA（`<FinalCTA />`）的统一架构与内容规则；供实现者、编辑与 Agent 生成/审核/迁移 blog 使用。  
> **引用**：[thetawave.md](./thetawave.md) | [blog/readme.md](./blog/readme.md) | [internal-external-links-checklist.md](./blog/internal-external-links-checklist.md) | [thetawave-project-tasks.md](./thetawave-project-tasks.md) | [skills/blog-article/SKILL.md](./skills/blog-article/SKILL.md)  
> **参考页（线上）**：[AI Study Assistant](https://thetawave.ai/feature/ai-study-assistant)（FAQ 组件）· [For Pre-Med Students](https://thetawave.ai/use-case/for-pre-med-students)（Final CTA 组件）· [turn-notes-into-podcast](https://thetawave.ai/blog/turn-notes-into-podcast)（Pilot 迁移对象）

**最近更新**：2026-06-22 · v1.0.0

---

## §0 文档职责与范围

### 0.1 职责

| 层 | 说明 |
|----|------|
| **作者体系** | 注册作者、作者页 URL、可点击 byline、Person schema |
| **内链策略** | 废弃文末 Related / Recent；改为正文上下文内链 |
| **共享组件** | `<SiteFAQ />`、`<FinalCTA />` 全站统一布局与文案规则 |
| **Blog 成稿** | Frontmatter 字段、Markdown 模块顺序、迁移验收 |

### 0.2 范围

| 在范围内 | 不在范围内 |
|----------|------------|
| `/blog/{slug}` 详情页 | `/blog` 索引页的 Recent 卡片（**保留**） |
| `/feature/*` 功能页 FAQ + Final CTA | 全局 Header / Footer / Newsletter |
| `/use-case/*` Use Case 页 FAQ + Final CTA | Study 聚合页（按需后续扩展） |
| 作者页 `/blog/author/{author_slug}` | 前端组件实现代码（本文档仅定义 props 与 copy） |

### 0.3 文档优先级

当本文档与 [blog-article SKILL](./skills/blog-article/SKILL.md) 冲突时，**以本文档为准**（尤其是 Related 废弃、FAQ/FinalCTA 组件化）。Skill 须按 §10 下游清单同步更新。

---

## §1 现状分析与目标态

### 1.1 三页面对比

| 维度 | turn-notes-into-podcast（当前线上） | ai-study-assistant（FAQ 目标） | how-to-study-for-finals（仓库稿） |
|------|-------------------------------------|--------------------------------|-----------------------------------|
| **作者** | Thetawave Team，不可点击 | — | Kostja，不可点击 |
| **FAQ** | 有，纯 H3 列表，无副标题 | H2 + subtitle + accordion | `## FAQ` + `**Q:**` 文本 |
| **Final CTA** | 「Try Thetawave on your own materials」 | Start Studying Smarter Today + 3 badge + 双按钮 | Conclusion 后单行 signup |
| **Related Reading** | 有（3 条） | 无 | 无 |
| **Recent articles** | 有（卡片） | 无 | 无 |
| **内链** | 功能名为纯文本 | feature 页内链丰富 | 正文上下文内链 |

### 1.2 目标态：Blog 详情页模块顺序

```
Hero（title · description · category）
  └── AuthorByline（Avatar + 可点击作者名 · date · read time）
## Key takeaways（TL;DR）
## Introduction（首段 ≥1 内链）
正文 H2（Step / 方法 / 工具 — 上下文内链分布在此）
## How ThetaWave fits the workflow   ← How-To 类保留；Study Spoke 可为 AI connection
## Common mistakes                    ← 可选
## Frequently Asked Questions         ← <SiteFAQ /> 组件
<FinalCTA />                          ← 全站统一组件（headline 可定制）
（无 Related Reading）
（无 Recent articles）
Newsletter                              ← 站点全局 footer，不改
```

### 1.3 废弃模块

以下模块 **不得** 再出现在 `/blog/{slug}` 详情页：

- `## Related Reading` / `## Related reading`
- `## Recent articles` / `Keep reading` 卡片区块
- frontmatter `related:` 数组
- 独立旧式 CTA：「Try Thetawave on your own materials」整块（并入 `<FinalCTA />`）
- Conclusion 后的 `---` + 单行 signup 链接（并入 `<FinalCTA />` 或 FinalCTA 上方一段收束）

---

## §2 作者页（Author Page）

### 2.1 URL 与注册作者（v1）

| author（显示名） | author_slug | URL | 适用稿件 |
|------------------|-------------|-----|----------|
| **Kostja** | `kostja` | `/blog/author/kostja` | Commercial、Alternative、Study Method、部分 How-To |
| **Thetawave Team** | `thetawave-team` | `/blog/author/thetawave-team` | Study Tips、产品工作流、官方 editorial |

**规则**：新建 blog 必须选用上表之一；禁止无 `author_slug` 的裸 `author` 字符串。

### 2.2 `<AuthorByline />` 组件

```
AuthorByline
├── avatar          // 可选；默认首字母圆形占位
├── author_name     // 链到 /blog/author/{author_slug}
├── publish_date
└── read_time       // 可选，如 "10 min read"
```

**HTML 语义**：作者名使用 `<a href="/blog/author/{slug}">`；文章页 `BlogPosting.author` 指向同一 `@id`。

### 2.3 作者页内容

每页 `/blog/author/{author_slug}` 包含：

| 区块 | 内容 |
|------|------|
| **Header** | 姓名、角色（jobTitle）、头像 |
| **Bio** | 2–4 句英文；说明 editorial 角色，不虚构未验证 credentials |
| **Social** | 可选 sameAs（LinkedIn、X 等） |
| **Article list** | 该作者文章，分页；链至 `/blog/{slug}` |

**Bio 示例（英文，上线前可微调）**：

- **Kostja**：*Kostja writes comparison guides and study-method deep dives for ThetaWave. Articles focus on tool selection, cognitive science, and workflows that hold up during exam season.*
- **Thetawave Team**：*The Thetawave Team publishes practical study workflows for college students—turning lectures, PDFs, and videos into notes, flashcards, quizzes, and audio review.*

### 2.4 Frontmatter

```yaml
author: "Thetawave Team"      # 显示名
author_slug: "thetawave-team" # 必填；与 URL 一致
```

### 2.5 Schema

- **作者页**：`ProfilePage` + `Person`（`@id`: `https://thetawave.ai/blog/author/kostja#person`）
- **文章页**：`BlogPosting.author` → `{ "@id": "https://thetawave.ai/blog/author/{author_slug}#person" }`

---

## §3 内链策略（上下文内链）

### 3.1 删除项

| 删除 | 替代 |
|------|------|
| `## Related Reading` | 正文 + FAQ 内 contextual 链接 |
| `## Recent articles` | `/blog` 索引页保留 Recent；详情页不展示 |
| frontmatter `related:` | 删除；用内链审计表记录 |

### 3.2 上下文内链配额

| 位置 | 最低 | 最高 | 目标 URL 类型 |
|------|:----:|:----:|---------------|
| **Opening（首段）** | 1 | 2 | `/blog/{slug}` 或 `/feature/*` |
| **正文 Body** | 1 | 4 | `/blog/{slug}` 互链 |
| **正文 Body** | 0 | 2 | `/feature/*` 或 `/use-case/*`（与主题强相关） |
| **FAQ 答案** | 0 | 2 | feature 或 signup（描述性锚文本） |
| **FinalCTA 前** | 0 | 1 | 可选一句 + 最相关 feature |

**锚文本**：描述性（如 `our finals study plan guide`）；禁止 `click here`、`learn more`。

**外链**：权威来源 2–8 条；竞品 `rel="nofollow noopener"`。规则不变，见 [internal-external-links-checklist.md](./blog/internal-external-links-checklist.md)。

### 3.3 主题 → Feature 映射（Blog 常用）

| 文章主题 | 优先内链 |
|----------|----------|
| 播客 / 音频复习 / 通勤 | `/feature/podcast-generator` |
| 闪卡 / 间隔重复 | `/feature/flashcard-maker` |
| 自测 / 测验 | `/feature/quiz-maker` |
| PDF / 教材 | `/feature/pdf-to-notes` |
| YouTube / 视频课 | `/feature/youtube-to-notes` |
| 讲座 / 实时捕获 | `/feature/lecture-to-notes` |
| 通用上传→笔记 | `/feature/notes-generator` |
| 期末 / 模拟考 | `/feature/exam-generator`、[/blog/how-to-study-for-finals](/blog/how-to-study-for-finals) |
| 工具选型 | [/blog/best-ai-note-takers](/blog/best-ai-note-takers) |

### 3.4 与旧 Skill 对照

| blog-article SKILL（旧） | 本规范（新） |
|--------------------------|--------------|
| `## Related Reading` 2–6 条 | **删除** |
| frontmatter `related` | **废弃** |
| Related 即自然 CTA | FinalCTA 组件 + 正文内链 |
| 首段 ≥1 内链 | **保留** |
| Body blog 1–4 | **保留** |

---

## §4 FAQ 组件（`<SiteFAQ />`）

**参考实现**：[ai-study-assistant](https://thetawave.ai/feature/ai-study-assistant) — `Frequently Asked Questions` 区块。

### 4.1 组件架构

| 层 | 职责 |
|----|------|
| **`<SiteFAQ />` UI** | 全站复用：H2、subtitle、accordion、a11y、JSON-LD |
| **页级内容** | 每页独立 Q&A；不在组件内硬编码 |

**注入方式**（择一，实现统一即可）：

| 来源 | 适用 |
|------|------|
| 正文 `## Frequently Asked Questions`（构建时解析） | **Blog Markdown（v2.2.1 起）** |
| CMS 字段 `faq` | Feature / Use Case |
| 静态 JSON | SSG |

### 4.2 组件 DOM 结构

```
<section id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Frequently Asked Questions</h2>
  <p class="faq-subtitle">Everything you need to know about {page_topic}.</p>
  <div class="faq-accordion">
    <details> or <button>+panel</button>  <!-- 与 feature 页一致 -->
      <h3>{question}</h3>
      <div>{answer HTML}</div>
    </details>
  </div>
</section>
```

**subtitle 规则**：`page_topic` 为小写短语，描述本页主题。Blog 示例：*turning notes into a study podcast*；Feature 示例：*ai study assistant*。

### 4.3 内容规则

| 维度 | Blog | Feature / Use Case |
|------|:----:|:------------------:|
| **题量** | 3–6（推荐 5） | 5–7 |
| **答案长度** | 40–80 英文词 | 40–80 英文词 |
| **首句** | Answer-first，直接答题 | 同左 |
| **与正文** | 相似度 <30%；≥1 题覆盖边界/异议 | 同左 |
| **Blog Markdown** | `## Frequently Asked Questions` + `### {question}` | CMS 数组 |

**禁止**：hidden FAQ schema；从 Key takeaways 整段复制；同一 Q 出现在多个 canonical URL。

### 4.4 FAQPage Schema

- 每页 **至多一个** `FAQPage`
- `@id`: `https://thetawave.ai/{path}/#faq`
- `mainEntity` 与可见 DOM **逐字一致**
- 至少 2 题（推荐 ≥3）

模板见 §8。

---

## §5 Final CTA 组件（`<FinalCTA />`）

**参考实现**：[for-pre-med-students](https://thetawave.ai/use-case/for-pre-med-students) — 文末转化区块。

### 5.1 固定结构（布局全站统一）

```
<FinalCTA>
  headline           // 页面专属，≤10 词
  subheadline        // 1–2 句价值主张；可含 300,000+ students
  trust_badges[3]    // 固定，不可删改顺序
  primary_button     // 默认文案见下表
  secondary_button
  mobile_links       // App Store + Google Play
</FinalCTA>
```

### 5.2 固定 trust badges（英文，顺序固定）

1. **Free to Start**
2. **No Credit Card Required**
3. **Results in Under 2 Minutes**

### 5.3 默认按钮

| 按钮 | 默认 label | 默认 href |
|------|------------|-----------|
| **primary** | Start Studying Free | `https://thetawave.ai/auth/signup` |
| **secondary** | Open App | `https://thetawave.ai/app` |

**移动端链接**（与全站一致）：

- [App Store](https://apps.apple.com/app/id6744060956)
- [Google Play](https://play.google.com/store/apps/details?id=ai.thetawave.app)

### 5.4 页面类型 → copy 公式

| 页面类型 | headline 模式 | primary 可变 |
|----------|---------------|--------------|
| **Blog How-To** | `Turn {topic} Into {outcome}` 或动作型 | 默认 |
| **Blog Commercial** | `Compare Tools on Your Own Materials` | 默认 |
| **Feature** | 与 ai-study-assistant：`Start Studying Smarter Today` | 默认 |
| **Use Case** | 痛点型：`Ace Orgo, Crush the MCAT` | `Try Free for {Persona}` |

**frontmatter 注入**：

```yaml
final_cta:
  headline: "Turn Your Notes Into Audio You Will Actually Replay"
  subheadline: "Upload structured notes, generate a short study podcast, then test yourself with flashcards and quizzes from the same source. Join 300,000+ students using Thetawave."
  primary_label: "Start Studying Free"   # 可选覆盖
  secondary_label: "Open App"            # 可选覆盖
```

`trust_badges` 与按钮 href **不在 frontmatter 覆盖**（全站一致）。

### 5.5 Blog 迁移：删除的旧 CTA 形态

- `## Try Thetawave on your own materials` 独立 section
- `---` + `**Stop re-reading...** [Create a free account](signup)`
- Conclusion H2 后单独 signup 段落（收束句可保留在 FinalCTA 上方一段，无 H2）

---

## §6 Blog 页面模板

### 6.1 模块顺序（Agent 成稿）

```
YAML frontmatter
→ ## Key takeaways（TL;DR；正文第一块）
→ ## Introduction（开篇；首段 ≥1 内链）
→ 正文 H2（按文章类型：Step / 方法 / 对比）
→ ## How ThetaWave fits the workflow  （How-To；Study Spoke 用 ## AI connection）
→ ## Common mistakes                  （推荐）
→ ## Frequently Asked Questions       （→ SiteFAQ）
→ （FinalCTA 由 CMS 注入，Markdown 不写 HTML）
```

**不再包含**：`## Conclusion`（可选：最后正文 H2 内收束，或 FinalCTA 上方一段）、`## Related Reading`。

### 6.2 Frontmatter 完整示例

见附录 A Pilot 或 [blog/13-turn-notes-into-podcast-2026.md](./blog/13-turn-notes-into-podcast-2026.md)。

### 6.3 构建管道

| 输入 | 输出 |
|------|------|
| `author` + `author_slug` | `<AuthorByline />` + BlogPosting.author |
| 正文 Markdown | 文章 body |
| 正文 FAQ 节（`## Frequently Asked Questions`） | `<SiteFAQ subtitle={...} items={parsed} />` + FAQPage JSON-LD |
| `final_cta{}`（Feature/Use Case；Blog 由站点注入） | `<FinalCTA {...} />` |
| — | **不**渲染 Related / Recent on detail |

---

## §7 Frontmatter 字段变更

| 字段 | 状态 | 说明 |
|------|------|------|
| `title` | 保留 | SEO 标题 |
| `description` | 保留 | 150–160 chars |
| `slug` | 保留 | 常青 kebab-case，无年份 |
| `date` | 保留 | YYYY-MM-DD |
| `author` | 保留 | 显示名 |
| `author_slug` | **新增必填** | `kostja` \| `thetawave-team` |
| `image` | 保留 | `/blog/images/{slug}-2026.jpg` |
| `keywords` | 保留 | ≥5 |
| `faq` | **新增必填** | `[{ question, answer }]`，3–6 条 |
| `final_cta` | **新增必填** | `{ headline, subheadline, primary_label?, secondary_label? }` |
| `related` | **废弃** | 删除；勿在新稿中使用 |

---

## §8 Schema JSON-LD 模板

### 8.1 BlogPosting（节选）

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://thetawave.ai/blog/{slug}/#article",
  "headline": "{title}",
  "description": "{description}",
  "datePublished": "{date}",
  "author": {
    "@type": "Person",
    "@id": "https://thetawave.ai/blog/author/{author_slug}#person"
  },
  "image": "https://thetawave.ai/blog/images/{slug}-2026.jpg",
  "publisher": {
    "@type": "Organization",
    "name": "Thetawave AI",
    "url": "https://thetawave.ai/"
  }
}
```

### 8.2 FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://thetawave.ai/blog/{slug}/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION TEXT EXACTLY AS ON PAGE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Answer-first paragraph, 40-80 words, matches visible content.</p>"
      }
    }
  ]
}
```

### 8.3 Person（作者页）

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "@id": "https://thetawave.ai/blog/author/kostja/#profile",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://thetawave.ai/blog/author/kostja#person",
    "name": "Kostja",
    "jobTitle": "Editorial Contributor",
    "url": "https://thetawave.ai/blog/author/kostja",
    "worksFor": {
      "@type": "Organization",
      "name": "Thetawave AI"
    }
  }
}
```

与 [thetawave-project-tasks.md Task 6](./thetawave-project-tasks.md) 对齐：BreadcrumbList 若页面已有则不改。

---

## §9 迁移与验收

### 9.1 Phase 1 — Pilot

| 项 | 值 |
|----|-----|
| **slug** | `turn-notes-into-podcast` |
| **镜像文件** | [blog/13-turn-notes-into-podcast-2026.md](./blog/13-turn-notes-into-podcast-2026.md) |
| **作者** | Thetawave Team / `thetawave-team` |
| **删除** | Related Reading、Recent articles、旧 Final CTA 区块 |

### 9.2 Phase 2 — 存量 12 篇（优先级）

| 优先级 | 文件 | 理由 |
|:------:|------|------|
| **P0** | 05, 06 | How-To；已有 FAQ，CTA 需组件化 |
| **P1** | 04, 08–12 | Study spokes；AI connection + FAQ |
| **P2** | 01–03 | Commercial/Alternative；disclosure 保留 |

每篇迁移：补 `author_slug`、`faq` 数组、`final_cta`；删除 Conclusion 后 signup；内链审计。

### 9.3 验收清单（人机共用）

- [ ] 详情页无 Related Reading / Recent articles
- [ ] Byline 作者名可点击，`/blog/author/{slug}` 返回 200
- [ ] FAQ：H2 + subtitle + accordion 与 [ai-study-assistant](https://thetawave.ai/feature/ai-study-assistant) 视觉一致
- [ ] FinalCTA：3 badge + 双按钮 + App links 与 [for-pre-med-students](https://thetawave.ai/use-case/for-pre-med-students) 一致
- [ ] FAQPage schema 与可见 FAQ 逐字一致
- [ ] 首段 ≥1 内链；正文 blog 互链 1–4
- [ ] G1–G7：定价 $118.80/年、300,000+ 注册、**无 SOC 2 claim**（见 Skill）
- [ ] frontmatter 无 `related`

---

## §10 下游同步清单

| 文件 | 变更 |
|------|------|
| [skills/blog-article/SKILL.md](./skills/blog-article/SKILL.md) | 删除 Related 模块；新增 author_slug / faq / final_cta；更新 Phase 6 |
| [blog/internal-external-links-checklist.md](./blog/internal-external-links-checklist.md) | 移除 Related 列；增上下文内链列 |
| [blog/readme.md](./blog/readme.md) | Frontmatter 示例；登记 #13 |
| [thetawave/readme.md](./readme.md) | 索引本文档 |
| **前端/CMS** | 实现 AuthorByline、SiteFAQ、FinalCTA；Blog 详情去掉 Recent |

---

## 附录 A — Pilot：`turn-notes-into-podcast` 迁移样例

### A.1 删除清单（相对现网）

- [ ] `## Related Reading`（3 条）
- [ ] `## Recent articles` / `Keep reading`
- [ ] `## Try Thetawave on your own materials` 独立 CTA 块
- [ ] FAQ 标题 `## FAQ` → 改为 `## Frequently Asked Questions`（组件 H2）
- [ ] 功能名纯文本 → 改为 Markdown/HTML 内链

### A.2 上下文内链表

| # | 段落位置 | 锚文本（建议） | 目标 URL |
|---|----------|----------------|----------|
| 1 | Opening 首段 | Podcast Generator | `/feature/podcast-generator` |
| 2 | Why audio review（第二段） | retrieval practice in our finals study plan | `/blog/how-to-study-for-finals` |
| 3 | Step 1 | YouTube to Notes | `/feature/youtube-to-notes` |
| 4 | Step 1 | PDF to Notes | `/feature/pdf-to-notes` |
| 5 | Step 1 | AI Notes Generator | `/feature/notes-generator` |
| 6 | Step 4 | Flashcard Maker | `/feature/flashcard-maker` |
| 7 | Step 4 | Quiz Maker | `/feature/quiz-maker` |
| 8 | How ThetaWave fits | Lecture to Notes | `/feature/lecture-to-notes` |
| 9 | How ThetaWave fits | Podcast Generator | `/feature/podcast-generator` |
| 10 | FAQ Q5 答案 | PDF to Notes / Lecture to Notes | 同上 feature |
| 11 | 外链 | Roediger and Karpicke (2006) | Sage DOI，`nofollow` |
| 12 | 外链 | The Learning Scientists — retrieval practice | learning scientists.org，`nofollow` |

### A.3 SiteFAQ 配置

**subtitle**：`Everything you need to know about turning notes into a study podcast.`

**5 题（40–80 词，answer-first）** — 已写入 [13-turn-notes-into-podcast-2026.md](./blog/13-turn-notes-into-podcast-2026.md) frontmatter 与正文 FAQ 节。

### A.4 FinalCTA 配置

```yaml
final_cta:
  headline: "Turn Your Notes Into Audio You Will Actually Replay"
  subheadline: "Upload structured notes, generate a short study podcast, then test yourself with flashcards and quizzes from the same source. Join 300,000+ students using Thetawave."
  primary_label: "Start Studying Free"
  secondary_label: "Open App"
```

### A.5 完整镜像稿

见 **[blog/13-turn-notes-into-podcast-2026.md](./blog/13-turn-notes-into-podcast-2026.md)**（仓库 canonical Markdown，供 CMS 导入与 Agent 参照）。

---

## 附录 B — Agent 机器可读摘要

```yaml
thetawave_blog_components:
  doc_version: "1.0.0"
  doc_path: "thetawave/thetawave-blog-components-spec.md"
  author_pages:
    base_path: "/blog/author/{author_slug}"
    authors:
      - slug: kostja
        display_name: Kostja
      - slug: thetawave-team
        display_name: Thetawave Team
    byline_clickable: true
  removed_modules:
    - RelatedReading
    - RecentArticlesOnDetail
    - frontmatter.related
    - legacy_cta_try_thetawave_block
  inline_links:
    opening_min: 1
    body_blog: 1-4
    body_feature: 0-2
    faq_max: 2
  components:
    AuthorByline:
      href: "/blog/author/{author_slug}"
    SiteFAQ:
      h2: "Frequently Asked Questions"
      subtitle_template: "Everything you need to know about {topic}."
      count_min: 3
      count_max: 6
      answer_words: 40-80
      schema: FAQPage
      schema_id_suffix: "/#faq"
    FinalCTA:
      badges:
        - "Free to Start"
        - "No Credit Card Required"
        - "Results in Under 2 Minutes"
      primary_default:
        label: "Start Studying Free"
        href: "https://thetawave.ai/auth/signup"
      secondary_default:
        label: "Open App"
        href: "https://thetawave.ai/app"
      mobile:
        app_store: "https://apps.apple.com/app/id6744060956"
        google_play: "https://play.google.com/store/apps/details?id=ai.thetawave.app"
  frontmatter:
    deprecated: [related]
    required: [title, description, slug, date, author, author_slug, image, keywords, faq, final_cta]
  blog_module_order:
    - opening
    - key_takeaways
    - body_h2
    - how_thetawave_fits_or_ai_connection
    - common_mistakes
    - frequently_asked_questions
    - final_cta_injected
  pilot_slug: turn-notes-into-podcast
  pilot_file: "blog/13-turn-notes-into-podcast-2026.md"
  reference_pages:
    faq: "https://thetawave.ai/feature/ai-study-assistant"
    final_cta: "https://thetawave.ai/use-case/for-pre-med-students"
  agent_workflow:
    - read_this_spec_first
    - draft_with_contextual_links_not_related_section
    - emit_faq_in_frontmatter_and_markdown
    - emit_final_cta_in_frontmatter_only
    - verify_against_section_9_3_checklist
```

### B.1 Agent 生成指令（复制即用）

```
按 thetawave-blog-components-spec.md（v1.0.0）创建或迁移 Blog 稿：
1. author_slug 必填；禁止 related 字段
2. 首段 + 正文上下文内链（见 §3.2）
3. faq 3–6 题写入 frontmatter 与 ## Frequently Asked Questions
4. final_cta 写入 frontmatter；不写 Related Reading / Recent articles
5. FAQ subtitle 使用模板；FinalCTA badges 使用固定三句
6. 成稿后对照 §9.3 验收清单
```

---

*ThetaWave Blog 与共享组件规范 · v1.0.0 · https://thetawave.ai/*
