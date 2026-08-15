# NeoDrop — 应用场景

> 遵循 [客户文档规范](../../client-template.md)
> **本文档职责**：人物画像、典型场景、使用旅程；链至 Features。  
> **引用**：[neodrop.md](./neodrop.md) 概览 | [neodrop-features.md](./neodrop-features.md) 功能 | [neodrop-keywords.md](./neodrop-keywords.md) 关键词

**最近更新**：2026-05-22

---

## 一、人物画像（Personas）

### P1：信息过载的 AI/科技从业者

- **身份**：工程师、产品经理、投资人、分析师
- **场景**：每日追踪 AI Agent、大模型、芯片、开源项目动态
- **痛点**：Twitter/X 噪音大、Newsletter 太多、RSS 维护成本高
- **关键诉求**：**一条 Feed 覆盖我的主题**，且内容有深度（Research Brief 级）
- **触发搜索**：*AI news digest*、*personalized tech newsletter*、*AI agent news*
- **产品触点**：订阅「AI News Tonight」「Global AI Coding Tools Update」或自建 Channel

### P2：垂直兴趣订阅者（娱乐 / 生活）

- **身份**：流媒体爱好者、本地生活关注者、体育迷
- **场景**：追 Netflix/HBO 新剧、World Cup、旧金山租房信息
- **痛点**：信息分散在多个 App 和群组
- **关键诉求**：**被动接收**精选更新，无需主动搜索
- **触发搜索**：*Netflix new releases alert*、*personalized entertainment feed*
- **产品触点**：Discover → Subscribe（如 Netflix / HBO / Apple TV+ New Releases）

### P3：个人创作者 / Solo Publisher

- **身份**：独立写作者、Newsletter 作者、自媒体
- **场景**：维持一个垂直栏目（SEO 指南、半导体周报、UI Teardown）
- **痛点**：写作产能不足，难以保持更新频率
- **关键诉求**：**AI 代劳研究与初稿**，自己只做策展与发布
- **触发搜索**：*AI newsletter generator*、*automated content channel*
- **产品触点**：Create Channel + Pro（Deep Research）+ 公开 Channel 获订阅

### P4：Side Hustle / 副业学习者

- **身份**：副业探索者、电商/Deals 关注者
- **场景**：追踪 Side Hustle 技巧、Deals & Savings、Crypto 市场
- **痛点**：教程碎片化，难以系统跟进
- **关键诉求**：**主题 Channel** 按节奏推送可行动情报
- **触发搜索**：*side hustle AI tools*、*deals digest*
- **产品触点**：Discover Side Hustle 分类 + 自建 Channel

### P5：小型内容团队 / MCN

- **身份**：MCN、品牌内容矩阵、小型工作室
- **场景**：同时运营多个主题 Channel（文/图/音/视频）
- **痛点**：多账号产能与队列优先级
- **关键诉求**：**高 credits、最高优先级队列、并发**
- **触发搜索**：*AI content studio*、*team content automation*
- **产品触点**：Studio 档 + 企业定制（SSO、合规、私有部署洽谈）

---

## 二、典型使用旅程

### 旅程 A：订阅者发现并开始阅读

1. 访问 neodrop.ai → 看到 Feed 空状态
2. 点击 **Discover channels** → 浏览 Editor's Picks / Most Subscribed
3. 订阅「AI News Tonight」「Daily AI R&B」等 Channel
4. 返回 Feed → Subscribed  Tab 出现新 Drop
5. 阅读 Article Drop（如 AI Agent 生态速报）→ 点击文内引用源
6. 每日打开 Feed 消费更新

### 旅程 B：创作者创建首个 Channel

1. 点击 **Create Channel** → 跳转 `/create/agent`
2. **Sign in or sign up** 完成认证
3. 用自然语言描述：*Weekly digest of Google Search Console SEO pitfalls for indie developers*
4. Channel Agent 分步引导完成配置
5. Free 档 credits 生成首批 Drop → 在 Channel 页公开展示
6. 升级 Starter（$3.99）维持每月 10–15 篇稳定更新

### 旅程 C：深度研究者使用 Pro

1. 已有 Starter Channel，需要更长 Research Brief
2. 升级 **Pro**（$20）→ 获得 Deep Research + Wide Research + Priority 队列
3. 同时运营 3 个 Channel（AI / Finance / Local News）
4. 首月获得 10,000 + 5,000 bonus credits
5. 在 Discover Fastest Growth 获得曝光 → 订阅数上升

### 旅程 D：团队 Studio 矩阵

1. MCN 评估 Studio（$200/月，100,000 credits）
2. 为 10+ 创作者各建 Channel，混排 Article + Podcast + Video
3. 利用 Highest-priority 队列保障发布窗口
4. 通过反馈渠道洽谈 SSO / 合规 / 专属配额

---

## 三、场景-功能-关键词映射

| 场景 | 功能模块 | 典型关键词 | 主承接载体 |
|------|----------|------------|------------|
| AI 资讯订阅 | Feed + Discover | AI news digest | `/discover`、Channel 页 |
| 自建 Newsletter | Channel Agent + Drop | AI newsletter generator | `/create/agent` |
| 深度研报 | Deep Research | AI research briefing | Pro Channel Drop |
| 娱乐追踪 | Discover 分类 | streaming new releases alert | 公开 Channel |
| 副业情报 | Side Hustle 分类 | side hustle digest | Discover 筛选 |
| 团队产能 | Studio credits | AI content studio | `/pricing` Studio 档 |

---

## 四、场景覆盖度评估

| 场景 | 产品匹配度 | 内容/产品缺口 |
|------|-----------|---------------|
| 个人 AI 资讯订阅 | 高（Feed + 高质量官方 Drop） | 推荐算法冷启动、中文 Channel 密度 |
| 创作者自建 Channel | 中高（Agent 向导 + Credits） | Channel 编辑/暂停/删除流程未在文档中详述 |
| 多模态内容（音乐/视频） | 中（标签已支持） | Video/Music Drop 公开样例较少 |
| 企业团队 | 中低（Studio + FAQ 提及 enterprise） | SSO、审计、API 未公开 |
| RSS/第三方源导入 | 低 | ⚠️ 待验证是否支持 RSS 作为输入源 |
| 移动端推送 | 低 | ⚠️ 未见 App 或 Push 说明 |

---

*文档创建日期：2026-05-22 | 模式：冷启动*
