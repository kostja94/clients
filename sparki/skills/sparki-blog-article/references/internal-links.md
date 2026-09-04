# Sparki — Internal Links Rules

> 加载时机：Phase 3（Outline 内链规划）· Phase 4（Draft 内链执行）· Phase 5（SelfCheck 内链复核）
> 主文件：SKILL.md §1 → project-config §2（白名单 SSOT）

---

## R1 — 链接数量与形式

| 规则 | 标准 |
|------|------|
| **blog 互链** | ≥2（全文上下文分布，非集中末尾） |
| **主站页面** | 1–3（用**绝对 URL** `https://sparki.io/...`，见 R2） |
| **外链** | 2–6（权威来源；竞品 `rel="nofollow noopener"`） |

## R2 — 绝对 URL vs 相对路径（sparki 特有！）

> **部署形态**：blog 是独立 OpenBlog 部署（`E:\客户部署项目\sparki-blog`），主站对 `/blog/*` 做 Rewrite 透传。**blog 站点内部不存在 `/features`、`/creators` 等主站路由。**

| 目标 | 写法 | 示例 |
|------|------|------|
| 主站页面（features/solutions/creators/industries/video-editor/pricing/use-cases/api） | **绝对 URL** | `[Copy Style](https://sparki.io/features/copy-style)` |
| 博客文章（61 篇 + 新稿） | 相对 `/blog/{slug}` | `[our long-to-short guide](/blog/long-video-to-short-video)` |
| 外链 | 完整 URL | `[CapCut](https://www.capcut.com)`（HTML 加 rel） |
| 锚点/站内非路由 | 避免 | 不用 `#` 伪链、不用 `relative /features`（会 404） |

**G6 判定**：相对路径 `/features/...`、`/creators/...` 一律视为**无效内链**（该路由不在 blog 站）；必须改写绝对 URL。`/blog/{slug}` 必须是**已存在或本批创建**的 slug。

## R3 — 锚文本标准

| 规则 | 标准 |
|------|------|
| 描述性 | "our guide to converting long video to short"、"the AI commentary workflow" |
| 禁止 | "click here"、"learn more"、"read more"、裸 URL 做锚文本 |
| 竞品 | HTML `<a href="URL" rel="nofollow noopener">Company Name</a>` |
| 主站功能页锚文本 | 自然句内嵌（"Sparki's Copy Style feature"），不堆砌产品词 |

## R4 — Canonical Concept 引用

每概念只在一篇完整定义（见 `content-graph.md` §4），其他文章引用 1–2 句 + link：

| 概念 | 引用 |
|------|------|
| 长改短 | "Converting long footage into shorts follows a workflow we covered here." → `/blog/long-video-to-short-video` |
| Caption / Commentary | 引用对应 canonical，不重定义 |

## R5 — Hub-Spoke 双向互链

- 簇 hub（如长改短家族）→ 链接主要 spoke
- Spoke → 必须回链 hub
- Spoke ↔ Spoke：语义相关时互链
- CreatorClone：正文顺带链到相关功能页（绝对 URL，≤2 次）与同风格其他 creator 文

## R6 — 禁止链接

- 未上线页面（G6）
- Forthcoming 作正文核心流程（脚注 ≤1）
- 死链（G2）
- 相对路径的主站路由（会 404）

---

## 内链验证清单（Phase 5 对照）

- [ ] ≥2 blog 互链（`/blog/{slug}` 相对），分布全文
- [ ] 主站页面链接均为 `https://sparki.io/...` 绝对 URL
- [ ] 无相对 `/features`、`/creators` 等失效内链
- [ ] 锚文本描述性（无 "click here"）
- [ ] 竞品外链 `rel="nofollow noopener"`
- [ ] 无未上线页面链接；Forthcoming ≤1（脚注）
- [ ] Canonical 概念 1–2 句 + link（非重定义）

---

*internal-links · sparki v1.0.0 · 2026-09-04*
