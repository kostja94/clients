# MeDo

> 基于 [medo.dev](https://medo.dev/)（**复核 2026-06-04**）

**Last updated**: 2026-06-04

---

## 文档体系（六主文档）

| 文档 | 职责 | 引用 |
|------|------|------|
| **medo.md**（本文） | 产品概览、定位、ICP、摘要 | 详述见各专项 |
| [medo-features.md](./medo-features.md) | 对话构建、全栈、插件、发布 | keywords、use-cases |
| [medo-use-cases.md](./medo-use-cases.md) | Persona、情境、分类场景 | features |
| [medo-keywords.md](./medo-keywords.md) | 关键词、目标页、承接载体 | site-structure |
| [medo-competitors.md](./medo-competitors.md) | 竞品矩阵、差异化 | features |
| [medo-site-structure.md](./medo-site-structure.md) | URL、IA、分阶段落地 | keywords、growth-strategy |
| [medo-growth-strategy.md](./archive/medo-growth-strategy.md) | 渠道、Hackathon、联盟、内容 | keywords、site-structure |

**原则**：每条重要信息**一处详述**、他处摘要 + 链接。

*产品入口*：Web [medo.dev](https://medo.dev/) | 文档 [Baidu AI Cloud — MeDo](https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en)（MIAODA 文档体系）

---

## 1. 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C/B2B / **AI App Builder / Vibe Coding / No-Code** |
| 网站 | https://medo.dev/ |
| 文档 | https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en |
| 当前阶段 | 增长期（应用广场规模极大、Product Hunt #1、Hackathon 与联盟计划运营中） |
| 核心产品 | **MeDo**：用自然语言与多 Agent 协作，在数分钟内生成并发布**生产级全栈应用**（前端、后端、数据库、业务逻辑与第三方集成） |
| Slogan（首页 Title） | **Build full-stack Apps With No-Code AI Platform** |
| 公司/运营 | 文档披露 **Sailai Private Limited**；产品与 **Baidu AI Cloud（MIAODA）** 文档体系关联；Product Hunt 叙事为 **MeDo by Baidu** |
| 目标市场 | 全球创作者、Indie、小团队、教育/营销场景、非技术产品经理 |
| 产品形态 | **Web 对话式 IDE + 可视化预览 + 一键发布**；应用广场展示 UGC 作品 |
| 关键差异化 | **全栈一次生成**（非仅 UI）+ **多 Agent 分工** + **插件/ API 一键集成** + **极低入门 credits 定价叙事**（公开渠道） |
| 更新日期 | 2026-06-04 |

### 能力与边界（Scope）

| 维度 | 说明 |
|------|------|
| **提供** | 对话/拖拽描述需求、需求文档生成、全栈代码与数据层、预览迭代、插件（如 Stripe）、发布至可访问 URL、应用分类浏览 |
| **典型产出** | Landing、问卷、小游戏、电商页、工具类 SaaS、教育应用、内部看板等（见官网分类与文档 Supported use cases） |
| **不提供/待验证** | 企业私有化部署 SLA、完整源码导出许可、自有域名绑定策略需以官方文档为准 |
| **生态** | Hackathon（$50,000 奖池宣传）、官方 Affiliate（30%  recurring 佣金宣传）、每日免费 credits（Product Hunt 叙事） |

*功能详表* → [medo-features.md](./medo-features.md)

---

## 2. 产品定位

### 产品摘要

**MeDo** 将「描述想法 → 可运行全栈产品」压缩到一次对话循环：用户用自然语言（可配合截图标注、拖拽）说明需求，平台通过 **Agent 协作** 自动生成前端界面、后端 API、数据库结构与第三方集成，并支持持续对话式迭代与一键发布。首页以**海量用户作品广场**建立「任何人都能做 App」的社会证明。

### 一句话定位

> **用对话造全栈** — 不写代码、不配服务器，把想法变成可上线、可接支付、可存数据的真实应用。

### 首页观察要点（2026-06-04）

| 元素 | 说明 |
|------|------|
| 分类筛选 | Recommended、Education、Website、Marketing、Productivity、E-commerce、Tool、Game、Survey、Others |
| 作品卡片 | 展示用户生成应用标题与描述（游戏、落地页、CRM、电商等） |
| 运营 Banner | Build with MeDo Hackathon（$50,000）；Affiliate Program（30% 佣金） |
| 分页 | 广场分页浏览（站内标注 **17,317+ apps** 量级，**待验证** 实时计数） |
| 生成入口 | 部分卡片含 *Skip chat and generate a requirements document* / *Generate APP* 流程暗示 |

*Persona* → [medo-use-cases.md](./medo-use-cases.md)

---

## 3. 目标受众 / ICP

- **非技术创作者 / 学生**：要快速做落地页、小游戏、问卷、作品集
- **Indie / Solo 创始人**：要验证 MVP、接 Stripe、上线可分享链接
- **产品经理 / 设计师**：要可点击原型升级为带后端的真实 Demo
- **小团队 / 教培机构**：要批量产出互动课件、营销页、活动 H5
- **推广伙伴**：Affiliate 推广 MeDo 获 recurring 佣金（官网 Banner）

---

## 4. 核心产品线（摘要）

| 模块 | 说明 |
|------|------|
| **Conversational Build** | 自然语言 + 对话上下文持续改 App |
| **Multi-Agent** | 角色化 Agent 分工，缩短传统开发周期（官方文档） |
| **Full-Stack Runtime** | UI + API + DB + 逻辑 + 部署结构一体生成 |
| **Plugins** | 数百 API / 第三方服务；Stripe 等一键接入（文档与评测） |
| **Publish & Gallery** | 发布至线上 URL；广场发现与 Remix 文化（**待验证** Remix 产品名） |
| **Prompt / PRD 工具** | 跳过闲聊直接生成需求文档再 *Generate APP* |

*完整能力* → [medo-features.md](./medo-features.md)

---

## 5. 关键词摘要

| 类型 | 示例 |
|------|------|
| **品牌** | MeDo, medo.dev, MeDo by Baidu, MIAODA |
| **Primary** | AI app builder, no-code full stack, vibe coding platform |
| **Secondary** | natural language app development, AI website builder |
| **Long-tail** | build full stack app without coding, AI generate SaaS MVP |
| **场景** | AI landing page generator, AI game maker, AI survey builder |

*完整映射* → [medo-keywords.md](./medo-keywords.md)

---

## 6. 竞品摘要

- **全栈 AI Builder**：Lovable、Bolt.new、Replit Agent、Firebase Studio（**待验证** 边界）
- **UI / 前端偏重**：v0 (Vercel)、Framer AI
- **传统低代码**：Bubble、Glide、FlutterFlow
- **国内同类**：妙搭/百度系文档、通义/其他厂商 App Builder（**待验证** 功能对齐）

**差异化（一句）**：MeDo 强调 **Agent 协作的全栈交付 + Baidu 云背书 + 极低 credits 入门 + 超大规模作品广场**，而非单页静态生成。

*矩阵* → [medo-competitors.md](./medo-competitors.md)

---

## 7. 网站结构（摘要）

| 路径/模块 | 说明 |
|-----------|------|
| `/` | 首页：分类 + 应用广场网格 + 运营 Banner |
| 应用详情 | 各 UGC App 独立页（**待验证** URL 模式 `/app/{id}`） |
| Hackathon | 站内 Hackathon 落地（Banner 链出） |
| Affiliate | 联盟计划落地页 |
| 文档 | Baidu AI Cloud `MIAODA` 英文文档树 |

*分阶段规划* → [medo-site-structure.md](./medo-site-structure.md)

---

## 8. 社会证明（公开渠道，2026-06-04）

| 来源 | 要点 |
|------|------|
| **应用广场** | 首页展示大量真实 UGC（游戏、电商、教育、工具等） |
| **Product Hunt** | 2025-11-05 发布，**#1 Product of the Day**；514 upvotes、146 comments（第三方归档 [hunted.space](https://www.hunted.space/product/medo-2/launches/medo-by-baidu)） |
| **定价叙事** | $5 / 2000 credits、每日 100 免费 credits、百万级数据存储（PH 文案，**待验证** 官网定价页） |
| **社区内容** | DEV、YouTube 等存在全栈游戏/订阅管理类深度评测 |

*对外引用建议标注来源与日期*

---

## 9. 优化建议

1. **独立 /pricing**：拦截 *AI app builder pricing*；与 PH 叙事对齐并 FAQ credits 消耗。
2. **分类 SEO 落地页**：`/templates/education`、`/templates/e-commerce` 承接分类词。
3. **对比内容**：`/vs/lovable`、`/vs/bolt` 承接商业意图。
4. **开发者枢纽**：链到 MIAODA docs、Quickstart、插件目录。
5. **中文市场**（可选）：百度系背书可做 `/zh` 信任与案例页。

---

## 10. 调研 Backlog

| ID | 需查证 | 优先级 |
|----|--------|--------|
| R1 | 官网公开定价与 credits 计费表 | P0 |
| R2 | 代码导出、GitHub 同步、自有域名 | P0 |
| R3 | 与 Supabase/Stripe 集成的默认栈与限制 | P1 |
| R4 | Remix / Fork 他人 App 的产品规则 | P1 |
| R5 | 企业版、团队席位、合规与数据驻留 | P2 |
| R6 | medo.dev 与 MIAODA 品牌关系对外口径 | P2 |

---

*文档创建：2026-06-04 | 来源： [medo.dev](https://medo.dev/)、[MeDo Overview — Baidu AI Cloud](https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en)、[Product Hunt 归档](https://www.hunted.space/product/medo-2/launches/medo-by-baidu)*
