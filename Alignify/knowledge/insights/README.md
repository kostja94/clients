# knowledgehub / insights · Insights 知识块分册

本目录存放与 **`/insights/[slug]`**、**`/zh/insights/[slug]`** 长文配套的非线性知识块：词汇锚点、专题对照、行业研究笔记与站外索引。**命名速查**：[README.md](../../../README.md) §十一（命名规范）。

---

## 与 [`knowledgehub/tools/`](../tools/README.md)、[`knowledgehub/seo/`](../seo/README.md) 的关系

| 位置 | 用途 |
|------|------|
| **`knowledge/tools/`** | 与 **`src/data/tools-pages-config.ts`** 中 **`slug` 同名**的 `*.md` 知识块，便于与 **`/tools/[slug]`** 对照。 |
| **`knowledge/seo/`** | **不绑定** Tools slug 的 SEO 专册（经典 Web 搜索、technical SEO 等）。 |
| **`knowledge/marketing/`** | 增长与 GTM 专册；与已上线的 `/marketing/[slug]` 配套。 |
| **`knowledge/insights/`（本目录）** | 与 **`content/insights/en|zh/[slug].md`** → **`/insights/[slug]`**、**`/zh/insights/[slug]`** 配套；basename **必须**等于 Insights 文章 `slug`（全小写 kebab-case）。 |
| **`skills/create-article/rules/`** | 站点内容与模板规范；本目录为**网摘与概念整理**，二者互补。 |

---

## 文档结构

新建 `*.md` 时，章节骨架与文首声明沿用 [`../README.md`](../README.md) 中「知识块文档结构」；本专册**有**站内 Insight 页对照时，文首元信息需含：

- `**文件名与 slug**：…`（声明 basename 与 `content/insights/{locale}/[slug].md` 的对齐关系）
- `**站内对照**：…`（链到已发布的 Insight 长文 URL 与仓库 JSON 路径）
- `**规范对照**：…`（链到 [`skills/create-article/rules/`](../../skills/create-article/rules/) 或其他分册知识块，按需）

**正式文章创作**：[`skills/create-article/SKILL.md`](../../skills/create-article/SKILL.md)

若某主题**尚无**独立 Insights JSON/路由（如 web-directories-and-portals），可暂用描述性 kebab 名，并在文首明确声明路由状态，上线长文后**重命名**为 slug 同名。

---

## 交叉引用（按需维护）

| 文档 | 状态 | 分工 |
|------|------|------|
| [ai-logo-design.md](./ai-logo-design.md) | ✅ 完整 | AI Logo 设计：词汇锚点、行业趋势（A Color Bright 框架）、商标风险提示、外链索引。配套: `/insights/ai-logo-design` |
| [reasons-you-need-seo.md](./reasons-you-need-seo.md) | ✅ 完整 | SEO 重要性的多维视角：多口径基准对照、增长/产品/内部知识库三视角、zero-click 与 AI Overviews 冲击。配套: `/insights/reasons-you-need-seo` |
| [directory-submission-sites.md](./directory-submission-sites.md) | 🔶 入门 | slug 对齐入口；详补见 [web-directories-and-portals.md](./web-directories-and-portals.md)（历史谱系、政策分析等）。配套: `/insights/directory-submission-sites` |
| [indie-hackers.md](./indie-hackers.md) | 🔶 入门 | slug 对齐入口；详补见 [marketing/indie-hackers.md](../marketing/indie-hackers.md)（词汇锚点、渠道矩阵、外链索引）。配套: `/insights/indie-hackers` |
| [generative-ai-landscape.md](./generative-ai-landscape.md) | 🔲 待补充 | 生成式 AI 全景：模型谱系、应用层、基础设施、监管与伦理。配套: `/insights/generative-ai-landscape` |
| [google.md](./google.md) | 🔲 待补充 | Google 深度分析：搜索/AI/云/硬件等多线战略、反垄断与竞争格局。配套: `/insights/google` |
| [openai.md](./openai.md) | 🔲 待补充 | OpenAI 深度分析：GPT/o 系列、商业化路径、治理结构与竞合。配套: `/insights/openai` |
| [ai-product-naming.md](./ai-product-naming.md) | 🔶 入门 | AI 产品命名全景：六大策略、命名 agency 案例（Lexicon/A Hundred Monkeys/Igor/Catchword 等）、全球 50 个知名 AI 产品命名溯源。配套: `/insights/ai-product-naming`（待上线） |
| `_briefs/ai-terminology-batch-emergence.md` | ✅ Brief | AI 术语批量出现：九轨 taxonomy、Loop 72h 案例。配套: `/blog/ai-terminology-batch-emergence` |

另有 [web-directories-and-portals.md](./web-directories-and-portals.md)（辅文，site 暂无对应 Insight 页，覆盖历史谱系与政策分析）。

- 全站知识块总说明：[knowledgehub/README.md](../README.md)
- 与 SEO 主题交叉的条目：[seo/README.md](../seo/README.md)
- 与增长叙事交叉的条目：[marketing/README.md](../marketing/README.md)
- 视觉美学与 hero/OG 参考：[design/aesthetic-references.md](../design/aesthetic-references.md)

---

*本 README 随 `knowledgehub/insights` 约定变更而更新。*
