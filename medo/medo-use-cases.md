# MeDo — 应用场景

> **本文档职责**：人物画像、典型场景、使用旅程；链至 Features。  
> **引用**：[medo.md](./medo.md) | [medo-features.md](./medo-features.md) | [medo-keywords.md](./medo-keywords.md)

**最近更新**：2026-06-04

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [medo.md](./medo.md) |
| 功能 | [medo-features.md](./medo-features.md) |
| 关键词 | [medo-keywords.md](./medo-keywords.md) |
| 竞品 | [medo-competitors.md](./medo-competitors.md) |
| 网站结构 | [medo-site-structure.md](./medo-site-structure.md) |
| 增长策略 | [medo-growth-strategy.md](./archive/medo-growth-strategy.md) |

---

## 一、人物画像（Personas）

### P1：非技术创作者 / 学生

- **身份**：自媒体、学生、副业探索者
- **场景**：要做活动页、小游戏、问卷、个人作品集
- **痛点**：不会写代码、不懂部署与数据库
- **关键诉求**：**说人话就能上线**，且作品能分享链接
- **触发搜索**：*AI website builder no code*、*make a game without coding*
- **产品触点**：首页 Recommended → 对话描述 → Publish → 广场展示

### P2：Indie / Solo 创始人

- **身份**：独立开发者、一人公司
- **场景**：48 小时内验证 SaaS、订阅工具、目录站 MVP
- **痛点**：前后端拼接耗时长；支付与数据层门槛高
- **关键诉求**：**可收费、可存用户数据** 的真实 MVP
- **触发搜索**：*AI full stack MVP builder*、*build SaaS with AI*
- **产品触点**：对话迭代 + Stripe 插件 + Supabase 自动库表

### P3：产品经理 / 设计师

- **身份**：PM、UX、增长
- **场景**：把 PRD/线框变成可点击、可录 Demo 的全栈原型
- **痛点**：Figma 原型无法演示真实登录、支付、列表筛选
- **关键诉求**：**截图标注 + 对话** 快速改 UI，保留业务逻辑
- **触发搜索**：*AI prototype with backend*、*PRD to app*
- **产品触点**：*Skip chat and generate a requirements document* → Generate APP

### P4：教育工作者 / 教培机构

- **身份**：老师、训练营运营
- **场景**：互动课件、语言学习小游戏、校园服务 Bot
- **痛点**：外包开发贵、迭代慢
- **关键诉求**：**分类模板**（Education）+ 低 credits 成本
- **触发搜索**：*AI education app builder*、*interactive learning game AI*
- **产品触点**：Education 分类广场案例 + Hackathon 主题营

### P5：推广者 / 技术 KOL

- **身份**：Affiliate、教程博主、开发者社区作者
- **场景**：推广 MeDo 获 recurring 佣金；产出「从零到全栈」内容
- **痛点**：需要可复现案例与官方激励
- **关键诉求**：**30% 联盟** + 高传播作品（PH #1、广场规模）
- **触发搜索**：*AI app builder affiliate*、*vibe coding tutorial*
- **产品触点**：Affiliate Banner、Hackathon、DEV/YouTube 评测链回 medo.dev

---

## 二、典型使用旅程

### 旅程 A：从零对话到发布落地页

1. 访问 [medo.dev](https://medo.dev/) → 点击创建 / 进入对话（**待验证** 精确 CTA 文案）
2. 描述：*Production-ready dark glassmorphism landing with React + Tailwind v4*
3. 预览桌面与 mobile → 对话修改 Hero 文案与 CTA
4. 点击 **Publish** → 获得可分享 URL
5. 可选：作品出现在广场 **Website / Marketing** 分类

### 旅程 B：带支付与数据的 SaaS 工具

1. 描述订阅管理或 CRM 类需求（参考广场 *Personal Schedule Dashboard*、*Real Estate CRM*）
2. MeDo 自动建表、API 与状态联动（评测：无需手配 DB）
3. 启用 **Stripe 插件** → 配置付费档（教程路径）
4. 多轮对话增加筛选、导出、权限（**待验证**）
5. 发布并用于早期付费验证

### 旅程 C：PRD 优先的 PM 工作流

1. 选择 **Skip chat and generate a requirements document**
2. 审阅/编辑结构化 PRD
3. **Generate APP** 一次性生成基线版本
4. 截图标注修改表单与仪表盘布局
5. 分享给研发评估「是否接代码导出」（**待验证**）

### 旅程 D：游戏 / 互动内容创作者

1. 浏览广场 **Game** 分类获取灵感（2048、寿司店、像素冒险等）
2. 上传角色/场景资源（部分案例含图片附件描述）
3. 对话增加关卡、音效、排行榜（DEV：Hangul 游戏 + 每日 AI 挑战）
4. 发布并投稿 **Build with MeDo Hackathon**

---

## 三、场景 ↔ 首页分类映射

| 首页分类 | 典型场景 | 广场示例（2026-06-04 可见） |
|----------|----------|------------------------------|
| Education | 课件、语言学习、校园 Bot | SpeakEasy English、Bhavik Studies |
| Website | 品牌站、作品集 | Rotin Official Website、Jurassic Portfolio |
| Marketing | 活动页、联盟页 | Affiliate Program landing、Unlock AI for Business |
| Productivity | 待办、日程、CRM | Todo List、Personal Schedule Dashboard |
| E-commerce | 店铺、促销 | SCREP \| ZEN、Electro Shop、BITE RUSH |
| Tool | 实用工具、仪表盘 | Function Graphing、Stock Market Analyzer |
| Game | 休闲/教育游戏 | 2048、Let's Make Sushi、Pixel Monster Hunter |
| Survey | 调研、反馈 | EV Preference Survey、Aesthetics Demand Research |
| Others | 垂直长尾 | Med Mama、Lafaek Check、Fabric recreation |

---

## 四、场景 ↔ 功能映射

| 场景 | 关键功能 | 详见 |
|------|----------|------|
| 快速落地页 | 对话迭代、Publish、分类曝光 | [medo-features.md §2](./medo-features.md) |
| 收费 MVP | Stripe 插件、全栈数据层 | [medo-features.md §4](./medo-features.md) |
| 复杂 App | 多 Agent、PRD 流 | [medo-features.md §2.2](./medo-features.md) |
| 获客/裂变 | Hackathon、Affiliate | [medo-growth-strategy.md](./archive/medo-growth-strategy.md) |

---

*与 [medo-keywords.md](./medo-keywords.md) 场景词簇联动维护*
