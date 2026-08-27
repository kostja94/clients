# Alignify 项目上下文 / Project Context

> 本文件是 Alignify 上下文仓库的唯一入口。  
> 最后更新：2026-08-26

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
├── skills/
│   ├── create-article/
│   ├── audit-article/
│   ├── optimize-internal-links/   ← 含 references/site-structure-internal-links.md
│   └── ops/
```

**已合并/移除**：`content/` · `technical/` · `create-tools-article/` · `create-blog-article/` · `localize-content-zh/` → 并入 `skills/create-article/`。

---

## 三、创作入口

| 任务 | 入口 |
|------|------|
| 新建任意频道文章 | [`skills/create-article/SKILL.md`](skills/create-article/SKILL.md) |
| 发布前终审 | [`skills/audit-article/SKILL.md`](skills/audit-article/SKILL.md) |
| 存量内链优化 | [`skills/optimize-internal-links/SKILL.md`](skills/optimize-internal-links/SKILL.md) |
| **全站内链快照** | [`skills/optimize-internal-links/references/site-structure-internal-links.md`](skills/optimize-internal-links/references/site-structure-internal-links.md) |
| 发布后 SEO | [`skills/ops/README.md`](skills/ops/README.md) |
| 规范 SSOT | [`skills/create-article/rules/README.md`](skills/create-article/rules/README.md) |
| 路径修复脚本 | [`scripts/ref/fix-rules-section-links.py`](scripts/ref/fix-rules-section-links.py) |

**质量档位**：Alignify **每篇均为 flagship** — Research + Moat + SelfCheck + 终审（≥80 发布，≥90 标杆）。

**流程**：create-article Step 10 → **audit-ready** → audit-article → **publish-ready** → Step 11 日期 → 发布。

**正文格式**：`content/{channel}/{locale}/{slug}.md` — TL;DR / FAQ / References **inline**，不再使用集中 JSON。

**架构原则**：正文节数与顺序由**内容**决定；`rules/anatomy.md` 与 `templates/` 为参考菜单，A 层硬底线（结论在 FAQ 前、FAQ 7 问等）见 [`anatomy.md`](skills/create-article/rules/anatomy.md) §〇。

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
