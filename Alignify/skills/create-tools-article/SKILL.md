# Create Tools Article — Alignify 文章创建 Skill

> **用途**：从知识块（`knowledge/tools/{slug}.md`）到发布就绪的正式文章（中文 Markdown + 英文 Markdown + Meta 注册 + 集中 JSON 块）的完整流程。
> **版本**：v2.6 · 2026-08-23
> **适用范围**：Alignify 新文章创建（**新文章统一走 `/blog/{slug}` 路由**；旧 `/tools/{slug}` 保持不变）。
> **部署仓**：`E:\自有部署项目\alignify production`
> **上下文仓**：`E:\clients\Alignify`（本 Skill 所在目录）
> **正文格式**：`content/blog/{locale}/{slug}.md`（YAML frontmatter + `<!-- block:section -->` 正文）
> **集中 JSON**：TL;DR → `src/data/tldr-data.json`；FAQ → `faq-data.json`；References → `references-data.json`
> **HowTo**：仅正文 `## 如何选择…` section；**禁止** frontmatter `howTo:` 与 HowTo JSON-LD

---

## 路由决策（先读此节）

| 场景 | 路由 | 内容目录 | Meta 注册 | Config 注册 |
|------|------|---------|-----------|-------------|
| **新文章（默认）** | `/blog/{slug}` | `content/blog/{en,zh}/{slug}.md` | `src/data/blog-meta.ts` | `src/data/blog-pages-config.ts` |
| 旧文章（保持不变） | `/tools/{slug}` | `content/tools/{en,zh}/{slug}.md` | `src/data/tools-meta.ts` | `src/data/tools-pages-config.ts` |

**架构说明**：
- 单一路由文件 + `generateStaticParams`；**不存在**每 slug 一个 `page.tsx`。
- Meta 由 `generateMetadata()` 从 `BLOG_META[slug]`（或 `TOOLS_META[slug]`）读取。
- 正文由 `getPageData("blog"|"tools", slug, locale)` 加载 Markdown（遗留 JSON 仅 glossary/media-kit 等）。
- 模式 B 迁移：`/tools/{slug}` 可 redirect 到 `/blog/{slug}`。

---

## 何时使用本 Skill

当以下条件**全部满足**时加载本 Skill：

- [ ] `knowledge/tools/{slug}.md` 知识块已创建并通过 `_TEMPLATE.md` 逐项核对
- [ ] 需要创建对应的正式页面
- [ ] 该 slug 尚未在 `blog-pages-config.ts` 中注册

**不适用场景**：
- 知识块尚未完成 → 先完成知识块
- 仅为已有文章做局部优化 → `content/sections/content-rules/section-optimization-playbook.md` 或 Skill **`optimize-tools-internal-links`**
- 非 Tools 频道（纯 Marketing/SEO/Insights 长文）→ 优先 **`create-blog-article`**

---

## 流程总览

```
Step 1 — 知识块就绪检查 + 关键词注册
        ↓
Step 2a — 产品截图（Best Ranking 必做）
        ↓
Step 2 — 创建中文 Markdown + 写入 tldr/faq/references JSON
        ↓
Step 2b — 中文本地化（localize-content-zh）
        ↓
Step 3 — Meta + blog-pages-config + blog-article-images 注册
        ↓
Step 4 — 创建英文 Markdown + 同步集中 JSON 英文键
        ↓
Step 5 — 质量检查（verify + audit + build）
        ↓
Step 6 — Blog publishDate 错开（成批上线前）
        ↓
Step 7 — Tools modifiedDate 维护（仅更新旧 /tools/ 页时）
```

**关键原则**：
- **新文走 `/blog/`**：Markdown 在 `content/blog/`；Meta 在 `blog-meta.ts`
- **先中文，后英文**
- **知识块 ≠ 文章**：知识块是笔记，文章是叙事体例
- **HowTo 只在正文**：见 `content/sections/section-how-to.md`；frontmatter 禁止 `howTo:`

---

## 各步骤详细文档

| 步骤 | 文档 | 产出 |
|------|------|------|
| 1 | [`01-knowledge-to-keywords.md`](./01-knowledge-to-keywords.md) | 关键词注册 + README 条目 |
| 2a | [`references/product-screenshot-pages.md`](./references/product-screenshot-pages.md) | `public/blog/{slug}/*.jpg` |
| 2 | [`02-article-structure.md`](./02-article-structure.md) | `content/blog/zh/{slug}.md` + 集中 JSON |
| 2c | [`02c-internal-links-drafting.md`](./02c-internal-links-drafting.md) | 内链初稿 |
| 2b | [`../localize-content-zh/SKILL.md`](../localize-content-zh/SKILL.md) | 中文润色 |
| 3 | [`03-meta-and-config.md`](./03-meta-and-config.md) | meta + config + images |
| 4 | [`04-english-localization.md`](./04-english-localization.md) | `content/blog/en/{slug}.md` |
| 5 | [`05-quality-gates.md`](./05-quality-gates.md) | 审计通过 + build |
| 6 | [`06-publish-date-stagger.md`](./06-publish-date-stagger.md) | publishDate 错开 |
| 7 | [`07-tools-modified-date.md`](./07-tools-modified-date.md) | Tools modifiedDate |

---

## 核心引用

| 引用 | 路径（相对本仓库根） |
|------|---------------------|
| 知识块模板 | `knowledge/tools/_TEMPLATE.md` |
| 10 节 anatomy | `skills/create-tools-article/references/tools-article-anatomy.md` |
| Section 规范 | `content/sections/` |
| 内链 SSOT | `content/alignify-internal-links.md` |
| HowTo 正文规范 | `content/sections/section-how-to.md` |
| TL;DR 规范 | `content/sections/section-tldr.md` |

部署仓路径（写作时 Read/Write）：
- `E:\自有部署项目\alignify production\content\blog\{locale}\{slug}.md`
- `E:\自有部署项目\alignify production\src\data\{blog-meta,blog-pages-config,tldr-data,faq-data,references-data}.*`

---

## 文章结构顺序（不可变）

```
TL;DR（JSON）→ 什么是XXX → 如何工作 → 各类型工具详细介绍 → 对比表格 → 应用场景 → 如何选择（正文 section）→ 结论 → FAQ（JSON）→ References（JSON）
```

---

## 质量检查

**部署仓**（在 `alignify production` 根目录执行）：

```bash
npm run verify:content-json   # 校验 md frontmatter + block 标记；禁止 frontmatter howTo:
npm run build
node scripts/permanent/audit-howto-tools.mjs   # Tools HowTo 正文质量（可选）
```

**上下文仓**（从部署仓根目录，相对路径）：

```bash
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/audit-tools-page-fields.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

> **已废弃**：`npm run audit:howto-choose`、frontmatter `howTo:`、JSON `howToChoose` block。HowTo 质量以 `section-how-to.md` + 正文 section 为准。

---

## 参考速查表

| 文档 | 内容 |
|------|------|
| [`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md) | 10 节结构 × Markdown 区块映射 |
| [`references/meta-requirements.md`](./references/meta-requirements.md) | Meta 四要素 |
| [`references/quality-checklist.md`](./references/quality-checklist.md) | 综合检查表 |
| [`references/common-errors.md`](./references/common-errors.md) | 常见错误归档 |

---

*create-tools-article · v2.6 · 2026-08-23*
