# Alignify 项目上下文 / Project Context

> 本文件是 Alignify 上下文仓库的唯一入口。  
> 最后更新：2026-09-03

---

## 一、双仓模型

| | 部署仓 | 上下文仓 |
|---|--------|----------|
| **路径** | `E:\自有部署项目\alignify production` | `E:\clients\Alignify` |
| **Git** | `github.com/kostja94/alignify-by-kostja` | clients 工作区 |
| **职责** | 站点源码、Markdown 正文、`public/` | 知识块、创作规范、Skills、审计脚本 |
| **入口** | 部署仓 `README.md` | 本文件 |

---

## 二、目录结构（2026-08-26 重组）

```
Alignify/
├── seo-weekly-report/         ← GSC + GA4 + Bing 周报引擎（替代原 /dash）
├── skills/
│   ├── create-article/        ← 构建新文章（含 Step 11 终审）
│   ├── audit-optimize/        ← 审核并优化老文章 · 含 references/site-structure-internal-links.md
│   ├── knowledge-block/
│   └── ops/
```

**已合并/移除**：`content/` · `technical/` · `create-tools-article/` · `create-blog-article/` · `localize-content-zh/` → 并入 `skills/create-article/`；`audit-article` / `optimize-internal-links` → `create-article` Step 11 + `audit-optimize`。

---

## 三、创作入口

| 任务 | 入口 |
|------|------|
| 新建任意频道文章 | [`skills/create-article/SKILL.md`](skills/create-article/SKILL.md) |
| 新稿发布前终审 | [`skills/create-article/11-final-audit.md`](skills/create-article/11-final-audit.md)（**新会话**） |
| 审核并优化老文章 | [`skills/audit-optimize/SKILL.md`](skills/audit-optimize/SKILL.md) |
| **全站内链快照** | [`skills/audit-optimize/references/site-structure-internal-links.md`](skills/audit-optimize/references/site-structure-internal-links.md) |
| 发布后 SEO | [`skills/ops/README.md`](skills/ops/README.md) |
| **全站发布/更新日期** | [`skills/ops/article-dates.md`](skills/ops/article-dates.md) |
| **SEO 周报 / 分析数据** | [`seo-weekly-report/README.md`](seo-weekly-report/README.md) |
| 规范 SSOT | [`skills/create-article/rules/README.md`](skills/create-article/rules/README.md) |
| 路径修复脚本 | [`scripts/ref/fix-rules-section-links.py`](scripts/ref/fix-rules-section-links.py) |

**质量档位**：Alignify **每篇均为 flagship** — Research + Moat + SelfCheck + 终审（≥80 发布，≥90 标杆）。

**流程**：create-article Step 10 → **audit-ready** → Step 11 Final Audit（新会话）→ **publish-ready** → 人类发布（Step 08 已注册 publishDate/modifiedDate）。存量优化走 [`audit-optimize`](skills/audit-optimize/SKILL.md)。

**正文格式**：`content/{channel}/{locale}/{slug}.md` — TL;DR / FAQ / References **inline**，不再使用集中 JSON。

**架构原则**：正文节数与顺序由**内容**决定；`rules/anatomy.md` 与 [`templates.md`](skills/create-article/rules/templates.md) 为参考菜单，A 层硬底线（结论在 FAQ 前、FAQ 7 问等）见 [`anatomy.md`](skills/create-article/rules/anatomy.md) §〇。

**部署仓说明**：渲染层若仍从 `tldr-data.json` / `faq-data.json` 注入，需单独在部署仓迁移；上下文规范与审计脚本已按 inline md 对齐。

---

## 四、Knowledge 细分

| 子目录 | 文件数 | 完成度 |
|--------|--------|--------|
| `knowledge/tools/` | 145 | 100% |
| `knowledge/seo/` | 42 | ~21% |
| `knowledge/marketing/` | 14 | ~7% |
| `knowledge/insights/` | 10 | ~30% |

---

*Alignify README · v2.0 · 2026-08-26*
