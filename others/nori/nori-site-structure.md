# Nori — 网站结构（URL 与优先级）

> **本文档职责（⑥ 网站结构）**：必备页与优先级、层级与导航逻辑、与关键词 / Use Cases / 增长的映射。**不重复**全量路径表——详表见 [nori-keywords.md](./nori-keywords.md) §11、[nori-features.md](./nori-features.md) §一；对比 slug 见 [nori-comparison-brand-interception.md](./nori-comparison-brand-interception.md) §5。  
> **维护**：与 通用-多文件文档联动精炼与增量循环.md §4 联动；改 URL 必查 keywords、features、use-cases、blog。

**Last updated**: 2026-03-24

---

## 1. 与「六主文档」的对应

| 六主文档角色 | Nori 文件 | 本站结构相关章节 |
|--------------|-----------|------------------|
| 关键词 | [nori-keywords.md](./nori-keywords.md) | §11 URL 模式、§12 程序化扩展 |
| 功能 | [nori-features.md](./nori-features.md) | §一 功能页概览、§二 页面结构策略 |
| 使用场景 | [nori-use-cases.md](./nori-use-cases.md) | `/use-cases/*` 与内链树 §五 |
| 增长策略 | [nori-blog.md](./nori-blog.md) | 博客主题 → 着陆页 |
| 竞品/截流 | [nori-comparison-brand-interception.md](./nori-comparison-brand-interception.md) | 对比页 slug 草案 |
| 杂项明细 | [nori-others.md](./nori-others.md) | 全量路由备忘（可选扩充） |

---

## 2. 层级原则

| 层级 | 内容 | 说明 |
|------|------|------|
| **L0** | `/`、`/app`、`/download` | 转化入口 |
| **L1 功能** | `/automatic-scheduling`（Hub）、各 `/*-to-calendar`、`/meal-planning`、`/recipe-manager` 等 | 一意图主承接一页；Hub 链出子能力 |
| **L1 场景** | `/use-cases/for-parents` 等 | Persona 里程碑；场景维度见 use-cases §1.1，不单开爆炸 URL |
| **L2 增长** | `/blog/*`、待建 `/comparison/*` | 流量 → 功能页或 /app |
| **L2 程序化** | `/schedules/...` | 见 [nori-schedules.md](./nori-schedules.md) |

---

## 3. 优先级（实施顺序摘要）

| 优先级 | 路径类型 | 依据 |
|--------|----------|------|
| **P0** | 首页、核心免输入链（photo/email/voice→calendar）、call-alert、餐食/recipe 主线、automatic-scheduling Hub | 与 [nori-keywords.md](./nori-keywords.md) §1 P0 一致 |
| **P0** | 高意向对比与替代（规划） | [nori-comparison-brand-interception.md](./nori-comparison-brand-interception.md) §0、§5 |
| **P1** | Use Cases 四页、trip planning、ai-generated-tasks | use-cases §七、features 表 |
| **P2** | 赛程程序化、长尾 blog | nori-schedules、nori-blog |

---

## 4. 避免孤儿页

- 新功能页须从 **Hub（如 automatic-scheduling）**、**首页** 或 **至少一篇博客 / Use Case** 获得内链。
- 改 URL 时同步：[nori-keywords.md](./nori-keywords.md) §11、[nori-features.md](./nori-features.md) 内链、[nori-use-cases.md](./nori-use-cases.md) §五。

---

## 5. 文档导航

| 文档 | 职责 |
|------|------|
| [nori.md](./nori.md) | 入口、产品一句话 |
| [nori-site-structure.md](./nori-site-structure.md) | **本文**：结构策略与优先级 |
| [nori-keywords.md](./nori-keywords.md) | URL 模式详表、意图 |
| [nori-features.md](./nori-features.md) | 单页 Title/Meta 与结构 |
| [nori-others.md](./nori-others.md) | Proof、CHANGELOG 索引、杂项 |
