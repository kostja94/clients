# Knowledge Block — Alignify 知识块维护

> **版本**：v1.3 · 2026-09-03  
> **用途**：维护 `knowledge/tools/`、`knowledge/marketing/` 等 **KB only** 非线性笔记——选题分流、关键词映射、SSOT 去重、站内相邻；**不是**正式文章成稿流程。  
> **成文分离**：发文走 [`../create-article/SKILL.md`](../create-article/SKILL.md)；KB 定 **slug / 意图 / 分流**，Brief 不得与 KB 关键词 SSOT 静默冲突。  
> **仅调研门槛**：用户说「只调研 / 我说写才写」时，**禁止**擅自新建 KB 或走 create-article — 见 [`references/research-only-gate.md`](./references/research-only-gate.md)。

---

## 何时使用

- 新建或刷新 **Tools slug 知识块**（含主题簇如 `website-builder/`、`cms/`、`agent/`）
- 两个候选词 **同意图**、需快判谁更「头」、归 Hub 还是 Spoke
- 评估新 spoke 时：**产品池是否与已有 slug 独占冲突**（见 [`../create-article/rules/product-coverage.md`](../create-article/rules/product-coverage.md)）
- 维护 README §SSOT 地图、文首 `keywordEn`、站内相邻（builder/CMS 簇 + 跨频道）
- **新建 Tools 主题簇**（多 slug 一次规划，如 work-agent + workspace-agent）

**不适用**：

| 场景 | 改用 |
|------|------|
| 写 `/blog/` 或 `/tools/` 正式正文 | create-article |
| 存量页内链优化 | optimize-internal-links |
| 仅 Marketing 长文（非 KB） | create-article + `knowledge/marketing/` 长文 |
| SEO 专册 + 外部 GSC KB | create-article + [`seo-slug-notes/`](../create-article/rules/seo-slug-notes/) · Brief 登记路径 |

---

## Tools 主题簇 · 临时 Brief（硬性）

> 全文：[`references/tools-cluster-ephemeral-brief.md`](./references/tools-cluster-ephemeral-brief.md)

1. **会话中可选**创建 `knowledge/tools/{cluster}/_briefs/{name}.md` 作簇规划草稿（边界、Hub/Spoke、产品独占）。
2. **KB 正文全部完成后必须删除**该 brief——**不保留** `_briefs` 作为长期 SSOT。
3. 持久边界与产品独占 → 写入各 slug KB 的 **`## 与相邻 slug 分流`** + skills **`references/{cluster}.md`**（例：[work-agent-cluster.md](./references/work-agent-cluster.md)）。
4. 与 **create-article** 的 `_briefs/{slug}.md`（marketing/seo/发文）**无关**；后者按 article-brief 流程保留至成文完成。

**完成定义（可删 brief）**：Hub + Spoke KB 已写、README + territory-map 已更新、相邻 slug 互链已改。

---

## Tools 主题簇 · 标准流程

```
读 SKILL + _TEMPLATE + README §战略原则
  → （可选）写 _briefs/{cluster}.md
  → 写 Hub KB → 写 Spoke KB → 改相邻 slug
  → 更新 README + territory-map
  → 删除 _briefs/{cluster}.md
  → （可选）create-article 发文
```

**Work Agent 簇范例**（边界 / 产品独占）：[`references/work-agent-cluster.md`](./references/work-agent-cluster.md)

**AI Employee 簇范例**（IM 协作三分法 / 产品独占）：[`references/ai-employee-cluster.md`](./references/ai-employee-cluster.md)

---

## 参考文档（按需加载）

| 主题 | 文档 |
|------|------|
| **Tools 簇临时 Brief + 删除规则** | [`references/tools-cluster-ephemeral-brief.md`](./references/tools-cluster-ephemeral-brief.md) |
| **Work Agent 簇 SSOT** | [`references/work-agent-cluster.md`](./references/work-agent-cluster.md) |
| **AI Employee 簇 SSOT** | [`references/ai-employee-cluster.md`](./references/ai-employee-cluster.md) |
| **同意图关键词 · 搜索量快判** | [`references/intent-near-keyword-volume.md`](./references/intent-near-keyword-volume.md) |
| 知识块结构模板 | [`knowledge/tools/_TEMPLATE.md`](../../knowledge/tools/_TEMPLATE.md) |
| 全目录约定 | [`knowledge/tools/README.md`](../../knowledge/tools/README.md) |
| 主题簇索引 | [README §主题簇物理路径](../../knowledge/tools/README.md#主题簇物理路径2026-08-28) · [`territory-map.md`](../../knowledge/tools/territory-map.md) |
| 用途建站 **builder/CMS 簇** SSOT | [`knowledge/tools/website-builder/README.md`](../../knowledge/tools/website-builder/README.md) · [`knowledge/tools/cms/README.md`](../../knowledge/tools/cms/README.md) |
| **Open Source · 部署/许可** | [`references/open-source-deployment-dimension.md`](./references/open-source-deployment-dimension.md) |
| **产品覆盖 · 垂类 · 独占** | [`../create-article/rules/product-coverage.md`](../create-article/rules/product-coverage.md) |
| 关键词研究概念 KB | [`knowledge/marketing/keyword-research.md`](../../knowledge/marketing/keyword-research.md) |
| **仅调研 · 显式成文门槛** | [`references/research-only-gate.md`](./references/research-only-gate.md) |

---

## 知识块文首最低集（Tools）

1. **材料范围** · **站内对照** · **Tools 关键词与 slug 映射**
2. **叙述主词 · 勿与…混买**（一行；相邻 slug 指针，不重复 §分流表）
3. **站内相邻**（builder/CMS 簇 Tools KB + **跨频道 · 已发布** blog/seo/marketing）
4. **`## 与相邻 slug 分流`**（Spoke：2–3 列 + ≤5 本轴 FAQ；全表链 Hub）

---

## 单篇去重门禁（Tools KB）

与 [`knowledge-dedupe-spec.md`](../../../knowledge-dedupe-spec.md) · [`_TEMPLATE.md`](../../knowledge/tools/_TEMPLATE.md) §单篇去重 SSOT 一致：

1. **产品事实**（URL、定价、份额、benchmark 数值）→ 仅 `## 外链索引`
2. **对比与测评** → 观点-only；产品名勿 **加粗** 重复索引（≤2 项重叠可接受，≥3 触发审计）
3. **延伸阅读 · 站内外** → 不重复产品门户 URL；旧节名 `延伸阅读与参考材料` 已废弃
4. **能力栈** → 无产品名；用「见 §外链索引 Type X」
5. 提交前运行：`python temp/audit_kb_dedupe.py`（仓库根 `clients/temp/`）→ **0 HIGH / 0 MEDIUM / 0 LOW**

---

## 垂类 spoke 与产品池

新建 Tools spoke 时，除 SERP/资源/≥2 vertical 产品外，还须：

1. **产品独占**：拟选产品在全站 **尚无** canonical Best H3（查 deploy 仓 `content/blog/` + `content/tools/`）
2. **窄意图**：slug 能对应 **独立产品池**
3. **Hub 不写 H3**：概念/分流 Hub **禁止** Best 产品榜单节

成文时默认 **3 款 H3** → [`../create-article/rules/product-coverage.md`](../create-article/rules/product-coverage.md)

---

*Alignify knowledge-block skill v1.3 · 与 create-article 并列*
