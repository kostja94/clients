# Lucius AI 全站面包屑（Breadcrumb）优化方案

> **本文职责**：梳理 luciusai.com 全站面包屑现状问题（视觉层 + BreadcrumbList JSON-LD），评估重要性，给出符合 Google 结构化数据最佳实践的优化方向与页面级目标面包屑。
> **审计基线**：2026-08-13 实站抓取（34 个英文页面 + 8 个中文页面，含 Blog 文章样本，逐 URL 验证）
> **创建日期**：2026-08-13
> **状态**：待评审

---

## 1. 方案概述

### 1.1 目标

全站面包屑达到以下标准：

- **视觉层**：从「仅 Blog/Discover 单级返回链接」升级为全站统一的语义化面包屑（`<nav aria-label="Breadcrumb">` + `ol/li`），3 级及以上页面必须有可见返回路径
- **结构化数据层**：BreadcrumbList JSON-LD **100% 覆盖**所有非首页页面，`position` 连续、`item` 指向规范可访问 URL（**不得指向 301 重定向页**）、`name` 与页面显示名一致
- **本地化**：中英文面包屑完全本地化，无英中混排；中文页 `Home` → `首页`、`item` 指向 `/zh`
- **一致性**：视觉面包屑与 JSON-LD 由同一数据源渲染，杜绝两者漂移
- **显性修复**：Blog 文章页 `Back to Blog`、Discover 子页 `Back to Discover` 替换为完整面包屑

### 1.2 审计范围

| 组 | 页面数 | 说明 |
|----|--------|------|
| 核心页 | 10 | `/` `/features` `/pricing` `/solutions` `/discover` `/blog` `/docs` `/privacy` `/terms` `/security/dpa` |
| 角色页 | 6 | `/roles` `/customer-support*` `/community-moderation` `/administrator` |
| 渠道页 | 7 | `/channels/*` |
| 功能页 | 5 | `/features/*` |
| 用例/案例 | 7 | `/use-cases/*` `/resources/use-cases/*` `/solutions/*` `/case-studies/*` |
| Discover | 4 | `/discover` + 3 子页 |
| Blog | 2 样本 | `/blog` 列表 + `/blog/{slug}`（38 篇同模板） |
| 法律页 | 3 | `/privacy` `/terms` `/security/dpa` |
| 中文版 | 8 | `/zh` `/zh/features` `/zh/pricing` `/zh/solutions` `/zh/docs` `/zh/blog` `/zh/blog/{slug}` `/zh/discover` |

### 1.3 Google 面包屑富结果要点（优化依据）

- **BreadcrumbList** 是 Google 面包屑富结果的唯一数据源；页面同时存在**可见面包屑**可帮助 Google 校验数据与页面内容的一致性，并降低误判风险
- `item` 必须是**规范、可直接访问**的 URL——指向 301 重定向 URL 的节点会被搜索引擎忽略或导致整条链失效
- `name` 应简洁（Google 会截断超长名称）且与页面内可见文字一致；最后一节点（当前页）通常不带链接或指向自身
- `position` 从 1 连续递增，Home 恒为 position 1
- 多语言：每种语言的 BreadcrumbList 使用该语言的 `name`，Home 节点 `item` 指向该语言首页（如 `/zh`）

---

## 2. 现状诊断

### 2.1 视觉层现状

| 页面组 | 现状 | 位置 |
|--------|------|------|
| Blog 文章页（英文） | `<a class="blog-back-link" href="/blog">Back to Blog</a>` | 文章 hero 顶部 |
| Blog 文章页（中文） | `<a class="blog-back-link" href="/zh/blog">返回 Blog</a>`（**残留英文 "Blog"**） | 文章 hero 顶部 |
| Discover 子页 | `<a class="discover-back-link" href="/discover">Back to Discover</a>` | 内容区顶部 |
| 其余全部页面 | **无语义化视觉面包屑**（无 `nav[aria-label="Breadcrumb"]`） | — |

- 全站导航为 JS 注入（`<div data-site-nav>`），静态 HTML 无可抓取的导航层级 → 深层页面的返回路径依赖面包屑，UX 缺口实际存在
- 单级 `Back to X` 链接只解决「回列表」一种意图，无法表达 `Home > Blog > 文章` 的层级关系

### 2.2 JSON-LD 层现状

> 以下为逐 URL 抓取 `<script type="application/ld+json">` 的 `BreadcrumbList` 实际内容。`✅` 表示结构、名称、链接均正确；其余为问题项（编号对应 §2.3）。

#### 英文页面

| 路径 | BreadcrumbList 内容 | 判定 |
|------|--------------------|------|
| `/` | 无（首页，正常） | ✅ |
| `/features` | Home > **How Lucius works** | ❌ #6 |
| `/features/knowledge` | Home > Features > Knowledge engine | ✅ |
| `/features/tasks` | Home > Features > Tasks and handoff | ✅ |
| `/pricing` | Home > Pricing | ✅ |
| `/solutions` | Home > **Case Studies and Use Cases** | ❌ #8 |
| `/roles` | Home > Roles | ✅ |
| `/customer-support/community` | Home > Customer Support > Community Customer Support | ⚠ #15 |
| `/customer-support/email` | Home > Customer Support > Email Customer Support | ⚠ #15 |
| `/community-moderation` | Home > **Community Moderator** | ⚠ #9 |
| `/administrator` | Home > Administrator | ✅ |
| `/channels/discord` | Home > **Channels** > Discord（Channels → `/channels`，**301**） | ❌ #10 |
| `/channels/slack` | Home > **Channels** > Slack（同上） | ❌ #10 |
| `/docs` | Home > **产品文档**（英文页用中文名） | ❌ #1 |
| `/blog` | Home > Blog | ✅ |
| `/blog/{slug}` | Home > Blog > 文章完整标题 | ✅ |
| `/use-cases/admin-governance` | Home > Use Cases > AI Team Governance | ⚠ #11 |
| `/resources/use-cases/ai-sales-assistant` | Home > Use Cases > AI Sales Assistant | ⚠ #11 |
| `/case-studies/utell` | Home > **Use Cases** > Utell | ❌ #11 |
| `/discover` | **无 BreadcrumbList**（仅 WebPage） | ❌ #13 |
| `/discover/social-content-community` | **无 BreadcrumbList** | ❌ #13 |
| `/discover/automate-refund-email` | **无 BreadcrumbList** | ❌ #13 |
| `/discover/smart-welcome-guide` | **无 BreadcrumbList** | ❌ #13 |
| `/privacy` | Home > Privacy Policy | ✅ |
| `/terms` | 未抓取（与 privacy 同模板，预计 ✅） | — |
| `/security/dpa` | Home > **Legal** > DPA（Legal → `/privacy`） | ❌ #12 |

#### 中文页面

| 路径 | BreadcrumbList 内容 | 判定 |
|------|--------------------|------|
| `/zh` | 无（首页，正常） | ✅ |
| `/zh/features` | **Home**（英文） > **Lucius 如何工作**；Home `item` = `https://luciusai.com` | ❌ #3 |
| `/zh/pricing` | **Home**（英文） > 价格；Home `item` = `https://luciusai.com` | ❌ #4 |
| `/zh/solutions` | **Home**（英文） > **Case Studies and Use Cases**（英文残留） | ❌ #5 |
| `/zh/docs` | **Home**（英文） > 产品文档；Home `item` = `https://luciusai.com` | ❌ #3 |
| `/zh/blog` | 首页 > 博客（`item` = `/zh`，**正确范式**） | ✅ |
| `/zh/blog/{slug}` | 首页 > 博客 > 中文标题（正确范式） | ✅ |
| `/zh/discover` | **无 BreadcrumbList** | ❌ #14 |
| `/zh/discover/automate-refund-email` | **无 BreadcrumbList** | ❌ #14 |

### 2.3 问题清单

#### P0 — 本地化错误（必须立即修复）

| # | 问题 | 证据 | 影响 |
|---|------|------|------|
| 1 | **英文页用中文 name** | `/docs` BreadcrumbList = "Home > **产品文档**" | 英文页面在 SERP 面包屑展示中文，品牌专业度受损 |
| 2 | **中文页 Home 未本地化** | `/zh/features` `/zh/pricing` `/zh/docs` 的 position1 `name` = "Home" 而非 "首页" | 与 `/zh/blog` 已正确使用「首页」的范式不一致，中文 SERP 展示混乱 |
| 3 | **中文页 Home 链接指向英文首页** | 上述 3 页 Home `item` = `https://luciusai.com`（应为 `https://luciusai.com/zh`） | 用户/搜索引擎从中文面包屑跳到英文首页，破坏语言一致性 |
| 4 | **中文页 name 英中混排** | `/zh/solutions` = "Home > **Case Studies and Use Cases**" | 与 [luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) P1-3 记录一致——**该问题至今仍在线上** |

#### P1 — 名称不一致 / 链接错误 / 覆盖缺失

| # | 问题 | 证据 | 影响 |
|---|------|------|------|
| 5 | **`/features` 面包屑名残留旧标题** | 页面自身 = "Home > **How Lucius works**"，但其子页父级 = "Features"，同一页面两个名字 | 名称不一致削弱结构化数据可信度 |
| 6 | **`/zh/features` 同名问题** | "Home > **Lucius 如何工作**" | 同上（旧标题） |
| 7 | **`/solutions` 面包屑名残留旧标题** | "Home > **Case Studies and Use Cases**"（URL 已为 `/solutions`） | 与 URL/导航不一致（meta 方案 P1-4 同类问题） |
| 8 | **面包屑名与页面 title 不一致** | `/community-moderation` 面包屑 = "Community Moderator"，title = "Moderator" | 两处命名打架，影响一致性 |
| 9 | **`/channels/*` 父级指向 301 重定向页** | 第二级 "Channels" `item` = `/channels`，实际 **301 → `/channels/website`**，且 `/channels` 无总览页 | 违反 Google Guidelines（item 必须为规范可访问 URL），面包屑富结果可能失效 |
| 10 | **`/case-studies/*` 父级命名与 URL 分组不符** | 第二级 "Use Cases" `item` = `/solutions`，与自身 `/case-studies/{slug}` URL 分组语义不符 | 用户对 URL 与面包屑的预期错位 |
| 11 | **`/security/dpa` 父级 "Legal" 指向错误页面** | 第二级 "Legal" `item` = `/privacy`（不存在 `/legal` 页） | 语义错位，面包屑层级误导 |
| 12 | **Discover 全部页面缺失 BreadcrumbList** | `/discover` + 3 个英文子页仅输出 WebPage，无面包屑 | 4 个独立关键词页（automate refund email 等）丢失富结果机会 |
| 13 | **中文 Discover 页面同样缺失** | `/zh/discover` + 中文子页无 BreadcrumbList | 中文版同样丢失富结果 |

#### P2 — 弱项（顺带统一）

| # | 问题 | 说明 |
|---|------|------|
| 14 | CS 子页面包屑名与页面 title 不一致 | 面包屑 "Community Customer Support" / title "Community Operator"；站点结构文档称 "Community Support"，三处三个名 |
| 15 | 中文 Blog 文章 `Back to Blog` 残留英文 | 视觉文案 "返回 **Blog**"，应全中文 |
| 16 | 无视觉面包屑，深层页 UX 缺口 | 导航 JS 注入，3 级页（features 子页 / case-studies / use-cases）返回路径弱 |

---

## 3. 优化方案

### 3.1 视觉面包屑组件（含 Back to Blog → 面包屑替换）

**组件规格**（全站统一，替换现有 `.blog-back-link` / `.discover-back-link`）：

```html
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/blog">Blog</a></li>
    <li aria-current="page">Human in the Loop AI: A Control Model You Can Audit</li>
  </ol>
</nav>
```

**中文版**：

```html
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/zh">首页</a></li>
    <li><a href="/zh/blog">博客</a></li>
    <li aria-current="page">Human in the Loop AI：一套可以审计的控制模型</li>
  </ol>
</nav>
```

**替换对照**：

| 页面组 | 替换前 | 替换后 |
|--------|--------|--------|
| Blog 文章页（38 篇 + 中文版） | `<a class="blog-back-link" href="/blog">Back to Blog</a>` | 面包屑 `Home > Blog > {文章标题}`（中文 `首页 > 博客 > {标题}`） |
| Discover 子页（3 + 中文版） | `<a class="discover-back-link" href="/discover">Back to Discover</a>` | 面包屑 `Home > Discover > {标题}`（中文 `首页 > 发现 > {标题}`） |

> 样式可复用 `.blog-back-link` 的视觉基线（小号、弱化、左对齐于 hero 顶部），新增分隔符样式（`/` 或 `›`）。

**展示策略**：

| 层级 | 页面 | 视觉面包屑 |
|------|------|-----------|
| 1 级 | `/` `/zh` 首页 | 不加 |
| 2 级 | `/features` `/pricing` `/solutions` `/blog` `/docs` `/roles` `/privacy` 等 | **加**（低成本全站统一，帮助 Google 校验） |
| 3 级 | `/features/knowledge` `/channels/*` `/customer-support/community` `/case-studies/*` `/use-cases/*` `/blog/{slug}` `/discover/{slug}` | **必须加**（本次核心） |

### 3.2 JSON-LD 修复

#### P0 修复（5 处）

| # | 页面 | 修复前 | 修复后 |
|---|------|--------|--------|
| 1 | `/docs` | position2 `name` = `产品文档` | `Documentation` |
| 2 | `/zh/features` | position1 `name` = `Home` | `首页`；`item` = `https://luciusai.com/zh` |
| 3 | `/zh/pricing` | position1 `name` = `Home` | `首页`；`item` = `https://luciusai.com/zh` |
| 4 | `/zh/docs` | position1 `name` = `Home` | `首页`；`item` = `https://luciusai.com/zh` |
| 5 | `/zh/solutions` | position1 `name` = `Home`；position2 = `Case Studies and Use Cases` | `首页`（`item` = `/zh`）> `案例与使用场景` |

> 正确范式参考：`/zh/blog` 与 `/zh/blog/{slug}` 已实现「首页 + /zh」的完整本地化，P0-2/3/4 仅为照搬该模板。

#### P1 修复

| # | 页面 | 修复 |
|---|------|------|
| 6 | `/features` | 自身 name `How Lucius works` → `Features`（与子页父级、URL 一致） |
| 7 | `/zh/features` | `Lucius 如何工作` → `功能` |
| 8 | `/solutions` | name → `Solutions`（与 URL 对齐；若产品最终命名不同，以导航文案为准统一） |
| 9 | `/community-moderation` | name 统一为 `Community Moderator`（或 title `Moderator`，**二选一全站定稿**，推荐用描述性更强的 `Community Moderator`） |
| 10 | `/channels/*`（7 页） | **删除不存在的 "Channels" 父级**，改为 2 级 `Home > {Platform}`（`item` = 该渠道页自身）；若未来新建 `/channels` 总览页再恢复 3 级 |
| 11 | `/use-cases/*` `/resources/use-cases/*` `/case-studies/*` `/solutions/ai-spam-defense` | 父级统一 `Home > Solutions > {页面}`（`item` = `/solutions`），消除 "Use Cases" / "Case Studies" 两种父级并存 |
| 12 | `/security/dpa` | 删除 "Legal" 中间级，改为 2 级 `Home > Data Processing Agreement`（无 `/legal` 页） |
| 13 | `/discover` + 3 子页（英文） | 补齐 BreadcrumbList：`Home > Discover > {标题}`；`/discover` 自身 `Home > Discover` |
| 14 | `/zh/discover` + 中文子页 | 补齐：`首页 > 发现 > {标题}` |

#### P2 统一

| # | 项目 | 建议 |
|---|------|------|
| 15 | CS 子页面包屑名 | 全站定稿一个：推荐按站点结构文档用 `Community Support` / `Email Support`（或对齐各页 title），**与页面 title 同步改**，避免三处三名 |
| 16 | 中文 Blog `Back to Blog` | 视觉层随 §3.1 一并解决（`返回 Blog` → 面包屑「首页 > 博客 > 标题」） |

### 3.3 页面级目标面包屑（英文版）

> 命名以 §3.2 定稿为准；`item` 均为规范 URL（无 301）。Blog 38 篇统一模板，示例 1 篇。

| 路径 | 目标 BreadcrumbList |
|------|--------------------|
| `/` | 无 |
| `/features` | Home › Features |
| `/features/knowledge` | Home › Features › Knowledge Engine |
| `/features/customer-profile` | Home › Features › Customer Profile |
| `/features/tasks` | Home › Features › Tasks and Handoff |
| `/features/data-analysis` | Home › Features › Data Analysis |
| `/features/automation` | Home › Features › Automation |
| `/pricing` | Home › Pricing |
| `/roles` | Home › Roles |
| `/customer-support` | Home › Customer Support |
| `/customer-support/community` | Home › Customer Support › Community Support |
| `/customer-support/email` | Home › Customer Support › Email Support |
| `/community-moderation` | Home › Community Moderator |
| `/administrator` | Home › Administrator |
| `/channels/discord` | Home › Discord |
| `/channels/telegram` | Home › Telegram |
| `/channels/feishu` | Home › Feishu |
| `/channels/website` | Home › Website |
| `/channels/slack` | Home › Slack |
| `/channels/email` | Home › Email |
| `/channels/whatsapp` | Home › WhatsApp |
| `/solutions` | Home › Solutions |
| `/use-cases/admin-governance` | Home › Solutions › AI Team Governance |
| `/use-cases/operations-analytics` | Home › Solutions › Operations Analytics |
| `/resources/use-cases/ai-sales-assistant` | Home › Solutions › AI Sales Assistant |
| `/solutions/ai-spam-defense` | Home › Solutions › AI Spam Defense |
| `/case-studies/utell` | Home › Solutions › Utell |
| `/case-studies/museon` | Home › Solutions › Museon |
| `/case-studies/jarsy` | Home › Solutions › Jarsy |
| `/discover` | Home › Discover |
| `/discover/social-content-community` | Home › Discover › Social Content Community |
| `/discover/automate-refund-email` | Home › Discover › Automate Refund Email |
| `/discover/smart-welcome-guide` | Home › Discover › Smart Welcome Guide |
| `/blog` | Home › Blog |
| `/blog/{slug}` | Home › Blog › {文章标题} |
| `/docs` | Home › Documentation |
| `/privacy` | Home › Privacy Policy |
| `/terms` | Home › Terms of Service |
| `/security/dpa` | Home › Data Processing Agreement |

### 3.4 页面级目标面包屑（中文版）

> 规则：position1 `name` = `首页`、`item` = `https://luciusai.com/zh`；全中文，禁英中混排；`name` 与中文 title 对齐。

| 路径 | 目标 BreadcrumbList |
|------|--------------------|
| `/zh` | 无 |
| `/zh/features` | 首页 › 功能 |
| `/zh/features/knowledge` | 首页 › 功能 › 知识引擎 |
| `/zh/features/customer-profile` | 首页 › 功能 › 客户画像 |
| `/zh/features/tasks` | 首页 › 功能 › 任务交接 |
| `/zh/features/data-analysis` | 首页 › 功能 › 数据分析 |
| `/zh/features/automation` | 首页 › 功能 › 自动化 |
| `/zh/pricing` | 首页 › 定价 |
| `/zh/roles` | 首页 › 角色 |
| `/zh/customer-support/community` | 首页 › 客户支持 › 社区支持 |
| `/zh/customer-support/email` | 首页 › 客户支持 › 邮件支持 |
| `/zh/channels/discord` | 首页 › Discord |
| `/zh/channels/telegram` | 首页 › Telegram |
| `/zh/channels/feishu` | 首页 › 飞书 |
| `/zh/channels/website` | 首页 › 网站 |
| `/zh/channels/slack` | 首页 › Slack |
| `/zh/channels/email` | 首页 › 邮件 |
| `/zh/channels/whatsapp` | 首页 › WhatsApp |
| `/zh/solutions` | 首页 › 案例与使用场景 |
| `/zh/use-cases/admin-governance` | 首页 › 案例与使用场景 › AI 团队治理 |
| `/zh/case-studies/utell` | 首页 › 案例与使用场景 › Utell |
| `/zh/discover` | 首页 › 发现 |
| `/zh/discover/social-content-community` | 首页 › 发现 › 社媒内容社区 |
| `/zh/discover/automate-refund-email` | 首页 › 发现 › 退款邮件自动化 |
| `/zh/discover/smart-welcome-guide` | 首页 › 发现 › 智能欢迎指南 |
| `/zh/blog` | 首页 › 博客 |
| `/zh/blog/{slug}` | 首页 › 博客 › {文章标题} |
| `/zh/docs` | 首页 › 文档 |
| `/zh/privacy` | 首页 › 隐私政策 |
| `/zh/terms` | 首页 › 服务条款 |
| `/zh/security/dpa` | 首页 › 数据处理协议 |

> 备注：`Discover`、`飞书`、`案例与使用场景` 等中文名以站点导航与各页 title 现状为准，若产品文案不同，面包屑与其保持一致即可（本表为推荐值）。

### 3.5 中文版规范（并入全站 meta 流程）

- **七处同步原则**（与 [luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) §4.5 一致）：title、description、og、twitter、JSON-LD name/description、**Breadcrumb name** 必须同步本地化
- Breadcrumb 额外要求：position1 恒为「首页」+ `/zh` 链接；`name` 全中文
- 新建中文页时必须复制 `/zh/blog` 的正确面包屑范式，禁止从英文模板直接复制

### 3.6 数据源与实现建议

- **单一数据源**：建立 `breadcrumb` 渲染函数/组件（输入页面 slug → 输出同源的视觉 `<nav>` + JSON-LD），避免两份配置漂移
- **根因修复**：本次全部 P0/P1 问题源自「模板复制漏改」——英文模板复制到中文页、旧标题残留、`/channels` 假设存在。落地时应统一由组件生成，禁止手写 JSON-LD
- **与主导航解耦**：面包屑层级以**内容语义**为准（如 `/case-studies/*` 归入 Solutions 分组），不与 JS 导航耦合，避免导航改动破坏面包屑

---

## 4. 落地执行清单

> 按依赖顺序执行。全部为静态模板/JSON-LD 修改，可直接上线。

### 4.1 JSON-LD 批量修复

| # | 任务 | 涉及问题 | 产出 |
|---|------|---------|------|
| 1 | P0-1：`/docs` name 英文化（`产品文档` → `Documentation`） | #1 | 单页 JSON-LD 定稿 |
| 2 | P0-2/3/4：`/zh/features` `/zh/pricing` `/zh/docs` 的 Home 本地化（`首页` + `/zh` 链接） | #2 #3 | 3 页 JSON-LD 定稿 |
| 3 | P0-5：`/zh/solutions` 全中文化 | #4 | 单页 JSON-LD 定稿 |
| 4 | P1：`/features` `/zh/features` `/solutions` 名称与 URL/子页统一 | #5 #6 #7 | 3 页 name 定稿 |
| 5 | P1：`/community-moderation` name 定稿 | #8 | 命名决策记录 |
| 6 | P1：`/channels/*` 删除 Channels 父级 → `Home > {Platform}`（7 页） | #9 | 7 页 JSON-LD 定稿 |
| 7 | P1：用例/案例父级统一 `Home > Solutions > X`（4 用例 + 3 案例 + spam-defense） | #10 #11 | 8 页 JSON-LD 定稿 |
| 8 | P1：`/security/dpa` 删除 Legal 父级 | #12 | 单页 JSON-LD 定稿 |
| 9 | P1：补齐 Discover 面包屑（英文 4 页 + 中文 4 页） | #13 #14 | 8 页新增 JSON-LD 定稿 |

### 4.2 视觉面包屑上线

| # | 任务 | 涉及问题 | 产出 |
|---|------|---------|------|
| 10 | 建立统一 `.breadcrumb` 组件（`nav[aria-label="Breadcrumb"]` + `ol/li` + `aria-current`） | #16 | 组件代码 + 样式 |
| 11 | Blog 文章页：`Back to Blog` → 面包屑（英文 38 篇模板 + 中文版模板） | — | 模板改动 |
| 12 | Discover 子页：`Back to Discover` → 面包屑（中英文） | — | 模板改动 |
| 13 | 3 级内容页加视觉面包屑（features 子页 / customer-support 子页 / channels / case-studies / use-cases） | #16 | 页面级插入 |
| 14 | 2 级页面加视觉面包屑（全站统一） | — | 页面级插入 |
| 15 | 中文 Blog 文章「返回 Blog」文案修复（随 #11 一并解决） | #15 | 文案定稿 |

### 4.3 上线前验证（当日）

- [ ] 全站抓取确认：每个非首页页面恰有 1 条 `BreadcrumbList`（无缺失、无重复）
- [ ] 所有 `item` URL 返回 200 且为规范 URL（**无 301 重定向**）
- [ ] `position` 从 1 连续递增，无跳号
- [ ] 中文页 Breadcrumb 全中文，position1 = 「首页」且 `item` = `/zh`
- [ ] 视觉面包屑文字与 JSON-LD `name` 完全一致
- [ ] Blog 38 篇 + Discover 4 页模板抽样验证（Rich Results Test 通过）
- [ ] Google Search Console 富结果报告确认面包屑富结果开始展示
- [ ] 与 [luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) 的标题/描述改动不冲突（`/features`、`/solutions`、`/zh/*` 多处交叉，同步合入）

---

## 5. 长期维护规则

- 面包屑由统一组件生成，新页面发布走「同源渲染 + 中文本地化」Checklist
- 每次 URL 结构变更（如 `/channels` 总览页上线、`/case-studies` 迁移）同步检查面包屑层级
- 每月抽查 Search Console 富结果，面包屑错误优先修复（富结果资格是免费 SERP 增强）
- 中文页面发布时核对「首页」链接与 `item` 语言一致性

---

*方案创建：2026-08-13 | 审计基线：luciusai.com 实站抓取（34 英文页 + 8 中文页）| 关联：[luciusai-site-structure.md](./luciusai-site-structure.md) 网站结构、[luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) Meta 优化*

---

## 关联文档

- [luciusai.md](./luciusai.md) — 产品概览与定位
- [luciusai-site-structure.md](./luciusai-site-structure.md) — 网站结构
- [luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) — Meta 优化方案
- [luciusai-i18n-seo-migration.md](./luciusai-i18n-seo-migration.md) — i18n SEO 迁移
- [luciusai-keywords.md](./luciusai-keywords.md) — 关键词策略
- [README.md](./README.md) — 文件索引
