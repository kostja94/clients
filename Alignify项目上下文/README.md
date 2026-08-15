# Alignify 项目上下文 / Project Context

> 本文件是 Alignify 项目上下文仓库的唯一入口文档，整合了原 README.md、INDEX.md、NAMING.md 的全部内容。
> 最后更新：2026-07-12

---

## 一、双仓模型 / Two-Repo Model

Alignify 采用「部署仓 + 上下文仓」分离架构（2026-05 迁移完成）。

| | 部署仓 | 上下文仓 |
|---|--------|----------|
| **路径** | `D:\部署项目\alignify-by-kostja` | `D:\项目文档\Alignify项目上下文`（本目录） |
| **Git** | `github.com/kostja94/alignify-by-kostja` | 本地目录 |
| **职责** | 站点源码、354 JSON、`public/`、IndexNow 脚本 | 规范、模板、knowledgehub、审计脚本 |
| **入口** | `CLAUDE.md`、`README.md` | 本文件 |

**判定口诀**：「删掉它，Vercel 上的站点还能正常 build 和运行吗？」若 **能**，且不是 Agent 入口，则放上下文仓。

---

## 二、站点规模 / Site Scale

> 更新于 2026-06-09

| 类别 | EN | ZH | 路由 |
|------|----|----|------|
| Hub / 静态页 | 16 | 17 | `/[locale]/...` |
| Tools | 107 | 107 | `/[locale]/tools/[slug]` |
| SEO | 38 | 38 | `/[locale]/seo/[slug]` |
| Marketing | 15 | 15 | `/[locale]/marketing/[slug]` |
| Insights | 7 | 7 | `/[locale]/insights/[slug]` |
| Glossary | 3 | 3 | `/[locale]/glossary/[slug]` |
| Events | 4 | 4 | `/[locale]/events/[slug]` |
| **合计** | **~190** | **~191** | ~381 静态页 |

技术栈：Next.js 15 · TypeScript · Tailwind CSS · shadcn/ui · next-intl
EN 在根路径（`/tools/...`），ZH 在 `/zh/tools/...`。Skills 页面使用 `(landing)` route group（无 Header/Footer chrome）。

---

## 三、目录结构 / Directory Structure

```
Alignify项目上下文/
├── README.md                  ← 本文件（项目唯一入口）
├── product/                   ← 产品策略：定位、关键词、站点结构、竞品、品牌
├── knowledge/                 ← 知识块：tools(145) / seo(42) / marketing(14) / insights(10)
├── content/                   ← 内容规范：sections(28) / templates(11) / links(7)
├── technical/                 ← 技术 SEO：sitemap、robots、canonical、IndexNow、GSC
├── scripts/                   ← 运维 & 审计脚本：ops / audit / reports
├── skills/                    ← 技能工作流：创建文章、本地化、内链优化、质量审查
└── ppt/                       ← 演示文稿文件（空目录——待整理）
```

---

## 四、状态仪表盘 / Status Dashboard

| 区域 Area | 位置 Location | 文件数 Files | 完成度 | 待办 |
|---|---|---|---|---|
| [产品策略](#五产品策略-product) Product | `product/` | 14 | ✅ 90%+ | P0 关键词待办 |
| [知识块](#六知识块-knowledge) Knowledge | `knowledge/` | 211 | 🔶 ~65% | 见 Knowledge 细分 |
| [内容规范](#七内容规范-content) Content | `content/` | ~49 | ✅ 90%+ | use-cases 6 批次 |
| [技术实现](#八技术实现-technical) Technical | `technical/` | 19 | ✅ 90%+ | GSC 监控阶段 4-6 |
| [工作流技能](skills/) Skills | `skills/` | 25 | ✅ 就绪 | — |
| [脚本](scripts/) Scripts | `scripts/` | 68 | ✅ 就绪 | — |

### Knowledge 细分 / Knowledge Detail

| 子目录 | 文件数 | 完成 | 骨架 | 完成度 |
|---|---|---|---|---|
| `knowledge/insights/` | 10 | 3 | 7 | 30% |
| `knowledge/marketing/` | 14 | 1 | 13 | 7% |
| `knowledge/seo/` | 42 | 8 | 30+ | 21% |
| `knowledge/tools/` | 145 | 145 | 0 | 100% |

### 全局待办 / Global TODO

| 优先级 | 事项 | 涉及范围 |
|---|---|---|
| P0 | 添加 4 个缺失页面到 sitemap（pricing-strategy, email-marketing, competitive-analysis, growth-case-studies） | 部署仓库（需确认是否已完成） |
| 