# Datus — 任务跟踪

> **归档说明**：本文档已于 2026-06-21 移入 `_archive/`，不再维护。活跃文档见 [_archive/README.md](./README.md)。

> **本文档职责**：记录项目执行任务、优先级、状态、交付物。
> **引用**：[datus.md](../datus.md) 概览 | [datus-keywords.md](../datus-keywords.md) 关键词 | [datus-site-structure.md](../datus-site-structure.md) 站点结构

**最近更新**：2026-05-24（初建）

---

## 任务列表

### Task 1：核心关键词页面搭建 — `/agent` + 两个 Use Case 页面

| 项目 | 内容 |
|------|------|
| **状态** | 📋 待开始 |
| **优先级** | 🔴 高 |
| **关联文档** | [datus-keywords.md](../datus-keywords.md) §一、§四；[datus-site-structure.md](../datus-site-structure.md) §三、§五 |

#### 子任务

| # | 子任务 | 页面 | 关键词 | 预计输出 |
|---|--------|------|--------|---------|
| 1.1 | **品类锚点页** | `/agent` | `data engineering agent` / `data agent` | 1 个独立页面，定义品类 + Datus 在品类中的位置 + 关联功能/场景。与首页解耦，防方向变动 |
| 1.2 | **场景页 A** | `/use-cases/full-stack-data-engineer` | `full stack data engineer` | 1 个 use case 页面，描述 full stack data engineer 的痛点与 Datus 解决方案 |
| 1.3 | **场景页 B** | `/use-cases/one-person-data-team` | `one-person data team` | 1 个 use case 页面，对应 v0.3 "From one-man data teams to enterprise agent teams" 定位 |

#### 设计原则

- **/agent 页**：品类定义为主，不过度绑定 Datus 当前产品名——允许未来方向调整时首页不受影响
- **两个 Use Case 页**：对应 v0.3 两条价值路径——个人端（one-person data team）× 企业端（full stack data engineer 是团队缩影）
- 每页需包含：H1 含目标关键词、结构化数据（Product / TechArticle Schema）、CTA 指向 Cloud Personal 免费版或 GitHub

#### 依赖

- [x] 关键词目标页已确认（`datus-keywords.md`）
- [x] URL 路径已规划（`datus-site-structure.md`）
- [ ] Datus.ai 线上实际路由确认（`datus-site-structure.md` 待办）
- [ ] 内容素材：从 `datus-features.md` 抽取功能描述、从 `datus-use-cases.md` 抽取场景描述

---

### Task 2：待规划

---

*任务文档 · Datus · https://datus.ai/ · 已归档*
