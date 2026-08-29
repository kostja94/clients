# Nova Scientia 项目上下文

> **Updated**: 2026-08-29

本目录是 Nova Scientia 的**文档与运维脚本单一来源**，不进入 Vercel 构建。

| | 路径 |
|---|------|
| **部署仓** | `E:\自有部署项目\nova-scientia-main` |
| **GitHub** | https://github.com/kostja94/nova-scientia |
| **本目录** | `E:\clients\Nova-Scientia` |
| **生产站点** | https://novascientia.com.br |

---

## 两仓分工

| 仓 | 放什么 | 不放什么 |
|----|--------|----------|
| **部署仓** | Next.js 源码、`content/products|companies/*.json`、`content/topics/*.md`、`scripts/permanent/`、`CLAUDE.md` | `docs/`、一次性脚本 |
| **上下文仓** | 全站规范、知识库、审计脚本 | Next.js 路由、`app/` 源码 |

---

## 最快定位

| 你要 | 看这里 |
|------|--------|
| 全站内容/SEO 规则 | [specs/reference.md](specs/reference.md) |
| 页面类型与区块顺序 | [specs/page-types.md](specs/page-types.md) |
| JSON 字段 | [specs/content-model.md](specs/content-model.md) |
| 编辑 → deploy 流程 | [specs/content-workflow.md](specs/content-workflow.md) |
| 多语言翻译流程 | [specs/i18n-content-workflow.md](specs/i18n-content-workflow.md) |
| 多语言路由规划 | [specs/i18n-route-plan.md](specs/i18n-route-plan.md) |
| 产品定位 / ICP | [specs/project-context.md](specs/project-context.md) |
| Topic 关键词 | [specs/keyword-map.md](specs/keyword-map.md) |
| 品牌视觉 | [specs/brand.md](specs/brand.md) |
| 命名 / Slug | [specs/slug-breadcrumb.md](specs/slug-breadcrumb.md) |
| 区块怎么写 | [templates/sections/README.md](templates/sections/README.md) |
| Topic 版本追踪 | [knowledge/topics/README.md](knowledge/topics/README.md) |
| 内链策略与清单 | [knowledge/internal-links.md](knowledge/internal-links.md) |
| 语言变体差异对照 | [knowledge/locale-vocabulary.md](knowledge/locale-vocabulary.md) |
| 任务进度 | [operations/task-tracker.md](operations/task-tracker.md) |
| 审计脚本 | [scripts/README.md](scripts/README.md) |
| 部署仓架构 | `E:\自有部署项目\nova-scientia-main\CLAUDE.md` |

---

## 目录结构

```
Nova-Scientia/
├── README.md                 ← 本文件（唯一入口）
├── specs/                    全站规范
│   ├── reference.md          总则
│   ├── page-types.md         页面结构
│   ├── content-model.md      JSON 字段
│   ├── content-workflow.md   编辑流程
│   ├── i18n-content-workflow.md  多语言翻译流程
│   ├── i18n-route-plan.md    多语言路由规划
│   ├── project-context.md    产品/ICP
│   ├── keyword-map.md        SEO 关键词
│   ├── slug-breadcrumb.md    命名规则
│   └── brand.md              品牌视觉
├── templates/sections/       区块写作规则
├── knowledge/
│   ├── topics/               版本追踪笔记
│   ├── internal-links.md     内链
│   └── locale-vocabulary.md  多语言变体差异对照表
├── operations/
│   ├── task-tracker.md       任务
│   └── indexnow-troubleshooting.md
└── scripts/                  审计 / 归档 / 工具
```

---

## 待办

| # | 事项 | 动作 |
|---|------|------|
| GAP-1 | 22/35 topic 缺版本笔记 | 见 [knowledge/topics/README.md](knowledge/topics/README.md) |

---

## Agent 协作

```text
完整规范：E:\clients\Nova-Scientia\README.md
内容任务：先读 specs/；改 products/companies → 部署仓 `content/*.json`；改 topics → 部署仓 `content/topics/*.md`。
```

**维护约定**：增删文件后同步更新本 README；状态标记 ✅ 当前 | ⚠️ 需关注 | 🔲 缺失。
