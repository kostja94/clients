# Knowledge Block — Alignify 知识块维护

> **版本**：v1.0 · 2026-08-28  
> **用途**：维护 `knowledge/tools/`、`knowledge/marketing/` 等 **KB only** 非线性笔记——选题分流、关键词映射、SSOT 去重、站内相邻；**不是**正式文章成稿流程。  
> **成文分离**：发文走 [`../create-article/SKILL.md`](../create-article/SKILL.md)；KB 定 **slug / 意图 / 分流**，Brief 不得与 KB 关键词 SSOT 静默冲突。

---

## 何时使用

- 新建或刷新 **Tools slug 知识块**（含主题簇如 `website-builder/`、`cms/`）
- 两个候选词 **同意图**、需快判谁更「头」、归 Hub 还是 Spoke
- 评估新 spoke 时：**产品池是否与已有 slug 独占冲突**（见 [`../create-article/rules/product-coverage.md`](../create-article/rules/product-coverage.md)）
- 维护 README §SSOT 地图、文首 `keywordEn`、站内相邻（builder/CMS 簇 + 跨频道）

**不适用**：

| 场景 | 改用 |
|------|------|
| 写 `/blog/` 或 `/tools/` 正式正文 | create-article |
| 存量页内链优化 | optimize-internal-links |
| 仅 Marketing 长文（非 KB） | create-article + `knowledge/marketing/` 长文 |
| SEO 专册 + 外部 GSC KB | create-article + [`seo-slug-notes/`](../create-article/rules/seo-slug-notes/) · Brief 登记 `E:\个人知识库\…` 路径 |

---

## 参考文档（按需加载）

| 主题 | 文档 |
|------|------|
| **同意图关键词 · 搜索量快判** | [`references/intent-near-keyword-volume.md`](./references/intent-near-keyword-volume.md) |
| 知识块结构模板 | [`knowledge/tools/_TEMPLATE.md`](../../knowledge/tools/_TEMPLATE.md) |
| 全目录约定 | [`knowledge/tools/README.md`](../../knowledge/tools/README.md) |
| 主题簇索引 | [README §主题簇物理路径](../../knowledge/tools/README.md#主题簇物理路径2026-08-28) · [`territory-map.md`](../../knowledge/tools/territory-map.md) |
| 用途建站 **builder/CMS 簇** SSOT | [`knowledge/tools/website-builder/README.md`](../../knowledge/tools/website-builder/README.md) · [`knowledge/tools/cms/README.md`](../../knowledge/tools/cms/README.md) |
| **Open Source · 部署/许可（跨品类维度）** | [`references/open-source-deployment-dimension.md`](./references/open-source-deployment-dimension.md) |
| **产品覆盖 · 垂类 · 独占** | [`../create-article/rules/product-coverage.md`](../create-article/rules/product-coverage.md) |
| 关键词研究概念 KB | [`knowledge/marketing/keyword-research.md`](../../knowledge/marketing/keyword-research.md) |

---

## 知识块文首最低集（Tools）

1. **材料范围** · **站内对照** · **Tools 关键词与 slug 映射**
2. **站内相邻**（builder/CMS 簇 Tools KB + **跨频道 · 已发布** blog/seo/marketing）
3. **`## 与相邻 slug 分流`**（Spoke：2–3 列 + ≤5 本轴 FAQ；全表链 Hub）

---

## 垂类 spoke 与产品池

新建 Tools spoke 时，除 SERP/资源/≥2 vertical 产品外，还须：

1. **产品独占**：拟选产品在全站 **尚无** canonical Best H3（查 deploy 仓 `content/blog/` + `content/tools/`）
2. **窄意图**：slug 能对应 **独立产品池**（例：`portfolio-website-builder` 用 Format/Squarespace 系，不与 `ecommerce-website-builder` 抢 Shopify 深度位）
3. **Hub 不写 H3**：概念/分流 Hub（如 `content-management-system`）**禁止** Best 产品榜单节

成文时默认 **3 款 H3** → [`../create-article/rules/product-coverage.md`](../create-article/rules/product-coverage.md)

---

*Alignify knowledge-block skill · 与 create-article 并列，不嵌套在其 rules 下*
