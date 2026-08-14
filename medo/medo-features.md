# MeDo 功能与产品能力

> **本文档职责**：产品**能做什么**、构建流程、集成与发布；情境见 [medo-use-cases.md](./medo-use-cases.md)。  
> **引用**：[medo.md](./medo.md) | [medo-keywords.md](./medo-keywords.md) | [medo-competitors.md](./medo-competitors.md)

**Last updated**: 2026-06-04 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [medo.md](./medo.md) |
| 关键词 | [medo-keywords.md](./medo-keywords.md) |
| 使用场景 | [medo-use-cases.md](./medo-use-cases.md) |
| 竞品 | [medo-competitors.md](./medo-competitors.md) |
| 网站结构 | [medo-site-structure.md](./medo-site-structure.md) |
| 增长策略 | [medo-growth-strategy.md](./archive/medo-growth-strategy.md) |

---

## 一、功能概览与建议 URL

| 产品线 | 线上/文档路径 | 目标关键词（示例） |
|--------|---------------|-------------------|
| **对话构建** | 产品内 Chat | AI app builder, natural language development |
| **全栈生成** | 预览 + 发布 | full stack no code, AI backend generator |
| **多 Agent** | 文档 Overview | multi agent app development |
| **插件市场** | 文档 Plugins | stripe plugin no code, API integration |
| **应用广场** | medo.dev 首页 | AI app examples, vibe coding gallery |
| **PRD 快捷流** | *Skip chat → requirements doc* | AI PRD generator, generate app from spec |
| **运营** | Hackathon / Affiliate Banner | AI hackathon, affiliate SaaS |

---

## 二、核心构建流程

### 2.1 自然语言对话（Conversational Build）

来源：[Overview — MeDo](https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en)

| 能力 | 说明 |
|------|------|
| **零代码描述** | 拖拽 + 自然语言描述即可搭建 |
| **持续上下文** | 多轮对话在同一项目上下文内迭代（社区评测一致） |
| **截图驱动修改** | 标注截图请求精确 UI 调整（About Us 文档） |
| **Prompt 优化** | 内置工具结构化需求，提升生成质量（第三方教程） |

### 2.2 多 Agent 协作（Multi-Agent）

| 能力 | 说明 |
|------|------|
| **角色分工** | 智能体按角色协作，将传统数日开发压缩为数分钟（官方文档） |
| **Agentic 全栈** | Product Hunt：自动化代码、基础设施与连线（frontend / backend / DB / integrations） |

### 2.3 全栈交付物（Full-Stack Output）

| 层 | 自动生成内容（文档 + 社区验证） |
|----|--------------------------------|
| **前端** | 响应式 UI、状态与交互 |
| **后端** | API、业务逻辑 |
| **数据** | 表结构、查询；常见栈含 **Supabase** 自动配置（DEV 案例） |
| **认证** | 用户体系（案例中出现，**待验证** 全模板覆盖） |
| **资产** | 图片/音效等（游戏类案例） |
| **部署** | 可发布至线上 URL 的结构 |

---

## 三、差异化能力（≥6 条）

| # | 能力 | 用户价值 | 对外表达簇 |
|---|------|----------|------------|
| 1 | **真全栈，非 Demo UI** | 订阅管理、排行榜等需持久化场景可开箱 | *working system, not mockup* |
| 2 | **多 Agent** | 复杂 App 分解并行，缩短等待 | *days → minutes* |
| 3 | **插件一键集成** | Stripe 收款等无需手写 API | *monetize without wiring APIs* |
| 4 | **对话式迭代** | 改文案/布局/逻辑均用自然语言 | *preview, ask, refine* |
| 5 | **跳过闲聊 → PRD** | 直接生成需求文档再 Generate APP | *Skip chat and generate requirements* |
| 6 | **大规模作品广场** | 降低「能不能做出来」的顾虑 | *17k+ apps*（站内数字 **待验证**） |
| 7 | **低成本 credits** | 降低试错成本 | *$5 for 2000 credits*（PH，**待验证** 官网） |

---

## 四、插件与集成

基于官方文档与公开评测：

| 类别 | 能力 |
|------|------|
| **支付** | Stripe 插件：订阅/付费计划扩展（教程叙事） |
| **数据/backend** | Supabase：表、API、环境变量自动配置（DEV 案例） |
| **通用** | 文档称可连接**数百** API 与第三方服务，一键完成业务流 |
| **云** | Baidu AI Cloud 企业级支持叙事（PH / About） |

---

## 五、发布、发现与运营功能

| 功能 | 说明 |
|------|------|
| **Publish** | 从预览到可分享 Live URL |
| **Gallery** | 首页分类浏览 UGC（Education、Game、E-commerce 等） |
| **Hackathon** | Build with MeDo Hackathon，$50,000 奖池（首页 Banner） |
| **Affiliate** | 官方联盟：30% recurring 佣金（首页 Banner） |
| **移动端预览** | 预览内切换 mobile 布局（教程） |

---

## 六、支持的应用类型（官方 + 首页）

| 类型 | 示例（广场可见） |
|------|------------------|
| **营销/网站** | Landing、品牌站、Affiliate 落地页 |
| **电商** | 时尚电商、贺卡店、电子产品店 |
| **游戏** | 2048、寿司店模拟、像素冒险、圣诞接礼物 |
| **工具** | 函数绘图、时钟、股票分析、CRM、待办 |
| **教育** | 语言学习、伊斯兰教学、院校 Chatbot |
| **问卷/调研** | EV 调研、美学需求调研 |
| **其他** | 医疗助手、漫画生成、Webhook 门锁 demo 等 |

---

## 七、定价与 credits（公开信息有限）

| 项 | 来源 | 备注 |
|----|------|------|
| 入门包 | Product Hunt：$5 → 2000 credits | **待验证** medo.dev 定价页 |
| 免费额度 | 每日 100 free credits | **待验证** |
| 存储 | 百万级数据存储叙事 | **待验证** 套餐边界 |
| 消耗规则 | 按生成/迭代扣 credits | **待验证** 明细表 |

---

## 八、功能 ↔ 关键词承接

| 功能模块 | 用户口语 | 主承接载体 |
|----------|----------|------------|
| 全栈生成 | build app without coding | / + docs Overview |
| 游戏 | AI game maker | /?category=Game |
| 落地页 | AI landing page builder | /?category=Website |
| Stripe | no code payment app | docs Plugins + 教程 |
| 对比选型 | lovable alternative | /vs/lovable（建议新建） |
| 联盟 | AI builder affiliate | Affiliate landing |

---

*与 [medo-keywords.md](./medo-keywords.md) 交叉引用*
