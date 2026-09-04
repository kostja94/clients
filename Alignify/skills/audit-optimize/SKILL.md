# Audit & Optimize — Alignify 已发稿审核与优化

> **版本**：v1.0 · 2026-09-03  
> **用途**：已存在于部署仓的页面——健康检查、内链优化、事实/SERP/结构刷新；本 skill **自包含**质检，不调用 create-article 的 SKILL。  
> **部署仓**：`E:\自有部署项目\alignify production`  
> **上下文仓**：`E:\clients\Alignify`

---

## 何时使用

- 已发稿季度 / 重大变更后的 **retro** 健康检查
- 存量页 **内链** 审计、修复、反向互链
- 已发稿 **局部刷新**（事实过期、SERP 落后、仅 Meta、结构微调）
- 刷新后的 **page-audit** 验收（≥80 + P0 Pass）

**不适用**：

| 场景 | 改用 |
|------|------|
| 从零写新 slug / 整篇重写 | [`../create-article/SKILL.md`](../create-article/SKILL.md) |
| 新稿 Step 10 后的发布前终审 | create-article [`11-final-audit.md`](../create-article/11-final-audit.md)（**新会话**） |
| 知识块选题 / 关键词 / 产品池 | [`../knowledge-block/SKILL.md`](../knowledge-block/SKILL.md) |
| 发布后 SEO 运维（sitemap / IndexNow / GSC / OG） | [`../ops/README.md`](../ops/README.md) |

---

## 模式分流

未指定模式时，先问用户一句再分流。

| 模式 | 文档 | 说明 |
|------|------|------|
| **retro** | [`01-retro.md`](./01-retro.md) | P0 快扫 + Retain / Refresh / Merge / Deprecate；可只出建议不改文 |
| **links** | [`02-links.md`](./02-links.md) → [`workflow.md`](./workflow.md) | 单页 loop / baseline / 反向互链 / 刷新快照 |
| **refresh** | [`03-refresh.md`](./03-refresh.md) | 改正文 / Meta / 双语 / `modifiedDate`；**禁止**改 `publishDate` |

改文后（links 写入、refresh 完成，或 retro 决定 Refresh 并落地）→ [`rules/page-audit.md`](./rules/page-audit.md)。

---

## 触发语

```
按 Alignify audit-optimize skill：
- 模式：retro | links | refresh
- 文件：content/{channel}/zh/{slug}.md（+ en）
- Primary keyword：{kw}（可选）
```

**Links 单页**：

```
按 Alignify audit-optimize links：
- slug：{slug}
- channel：blog | tools | seo | marketing | insights
```

**Refresh**：

```
按 Alignify audit-optimize refresh：
- slug：{slug}
- 范围：事实 | SERP | Meta | 结构 | 双语（勾选）
```

---

## 按需点读规则（非 create-article SKILL）

写作 / 内链 / Meta **规则正文**仍在 `create-article/rules/`（SSOT）。本 skill **禁止**要求先读 create-article 的 `SKILL.md`。一次最多再读 **2** 个 rules 文件。

| 场景 | 点读 |
|------|------|
| 内链 R 规则 / Marketing M1–M11 | [`../create-article/rules/internal-links.md`](../create-article/rules/internal-links.md)（对应 Part）· 速查 [`references/rules-quickref.md`](./references/rules-quickref.md) |
| Meta title / description | [`../create-article/rules/meta.md`](../create-article/rules/meta.md) |
| 结构 / frontmatter 禁项 | [`../create-article/rules/anatomy.md`](../create-article/rules/anatomy.md) |
| 双语地道 | [`../create-article/rules/content-locale.md`](../create-article/rules/content-locale.md) 对应 Part |
| 质检打分 | **本目录** [`rules/page-audit.md`](./rules/page-audit.md)（完整自包含） |

---

## 文档索引

| 文件 | 用途 |
|------|------|
| [`01-retro.md`](./01-retro.md) | 已发稿回溯 |
| [`02-links.md`](./02-links.md) | 内链模式入口 |
| [`workflow.md`](./workflow.md) | 全站 baseline + 单页 loop |
| [`reverse-links.md`](./reverse-links.md) | Phase 4 反向互链 |
| [`03-refresh.md`](./03-refresh.md) | 内容刷新 |
| [`rules/page-audit.md`](./rules/page-audit.md) | 老文 P0 + 十维 + 处置建议 |
| [`references/site-structure-internal-links.md`](./references/site-structure-internal-links.md) | 全站内链快照 |
| [`references/marketing-internal-links-backlog.md`](./references/marketing-internal-links-backlog.md) | Marketing cluster 批次 |
| [`references/rules-quickref.md`](./references/rules-quickref.md) | 内链规则跳转 stub |

---

## 脚本（部署仓根目录）

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
python ../../clients/Alignify/scripts/audit/build-site-internal-links-doc.py   # 刷新快照 → audit-optimize/references/
python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py --slug {slug}
python ../../clients/Alignify/scripts/audit/audit-frontmatter.py
npm run verify:content-json && npm run build
```

---

*audit-optimize · v1.0 · 2026-09-03 · 合并自 audit-article + optimize-internal-links*
