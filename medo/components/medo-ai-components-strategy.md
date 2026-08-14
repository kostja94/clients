# MeDo AI Components — 功能 Landing Page 与组件市场策略

> **类型**：功能营销方案 | **版本**：v0.2 | **日期**：2026-07-08
>
> 本文档定义 MeDo "AI Components" 功能的 Go-to-Market 策略：Landing Page 设计、关键词关键词承接、公开组件库截留策略。
>
> **引用**：[medo.md](./medo.md) | [medo-features.md](./medo-features.md) | [medo-competitors.md](./medo-competitors.md) | [medo-keywords.md](./medo-keywords.md)

---

## 一、核心叙事：组件是乐高积木

### 1.1 一个网站 = 一堆积木

```
一个 Landing Page = Navbar + Hero + Features + Pricing + FAQ + Footer
一个 SaaS App     = Sidebar + Dashboard + DataTable + Forms + Settings

→ 这些"积木块"就是组件。
→ 有了现成的组件，用户不用每次从零描述，像乐高一样拼接即可。
```

**乐高积木的价值**：不是每一块积木有多精美，而是**任何一块都能和另一块无缝拼接**。Navbar 和 Hero 的间距一致、Card 和 Button 的圆角统一、所有积木共享同一套设计语言。

### 1.2 21st.dev 的验证：2M MAU 不是巧合

21st.dev 是目前最成功的 AI 组件 Registry，**月活 2M MAU**。它的模式极其简单：

- 社区上传 React 组件（Tailwind + Radix UI）
- 其他开发者浏览、复制 Prompt、粘贴到 Lovable / Bolt / Cursor
- Lovable 官方文档直接推荐 21st.dev 作为组件来源

**2M MAU 证明了一件事**：vibe coding 用户真的需要组件积木——不是"要不要做"的问题，而是"方向已经验证，看谁能做得更好"。

### 1.3 当前市场空白

| 现状 | 问题 | MeDo 的机会 |
|------|------|------------|
| vibe coding 用户生成 App 后，需要去 **第三方** 找组件（21st.dev、Jiro） | 用户离开平台，流量外泄 | **在 MeDo 内部提供组件积木**——不需要离开 |
| "navbar components"、"footer components" 等关键词被 CMS 模板占据 | 没有 vibe coding 工具承接这些词 | **Landing Page 承接**——"AI-generated navbar components" |
| 21st.dev 的组件是 React 社区的，用户需要筛选、适配 | 有门槛，非开发者不会用 | **AI 对话直接生成**——描述需求即可，不需要技术背景 |
| 没有一个 vibe coding 平台的组件库是 **公开的、跨平台可用的** | 用户锁定在单个平台 | **组件库公开/开源**——Lovable、Bolt、v0 用户也能用 → 截留用户到 MeDo |

### 1.4 "被动生成"与"拖拽即用"：MeDo 的两大核心引擎

MeDo 的组件体系由两个相互独立但协同的机制驱动：

- **被动生成（内容引擎）**：AI 每次对话自然产出组件，自动填充 Gallery
- **拖拽即用（消费引擎）**：用户在 Gallery 中发现好的组件/模板，**拖到当前项目中直接使用**

两个引擎解决的问题不同，缺一不可。

---

#### 引擎一：被动生成——Gallery 的自动供血机制

用户每次在 MeDo 中说"给我一个 SaaS Dashboard"，AI 不只是在生成一个页面——它在内部已经拆解出了 Sidebar、DataTable、StatCard、Chart、SettingsForm……这些积木**不是额外制造的，是生成过程中自然存在的**。

```
用户说："给我一个落地页"
  └─ AI 内部分解：
       ├─ Navbar     ← 这就是一块积木
       ├─ Hero        ← 这也是一块积木
       ├─ Features    ← 这还是一块积木
       ├─ Pricing     ← ...
       ├─ Testimonials
       └─ Footer
```

**MeDo 不是在"造"组件，而是在"丢弃"组件。** 每一个通过对话生成的 App，本质上已经包含了 5-20 个高质量、风格统一的组件积木——但它们在生成后被锁在一个完整的 App 里。

如果把这些"顺便生成"的积木释放到 Gallery 中：

| 维度 | 21st.dev 模式 | MeDo 被动生成模式 |
|------|-------------|-----------------|
| 组件来源 | 人写代码 → 手动上传 | AI 每次对话自然产生 |
| 质量保障 | 人工审核 | 同一 session 上下文自动保证一致性 |
| 增长速度 | 线性（靠上传量） | 指数（每次生成 App = 产出 N 个组件） |
| 用户参与 | 用户需要刻意"贡献" | 用户无需额外操作——用了 MeDo 就是在产组件 |

**对这个引擎而言，Gallery 的角色是**：组件从 AI 生成中"自动捕获"后的汇聚地。每个用户生成 App 的过程，都在无声地为 Gallery 贡献积木。Gallery 不靠运营填充——它靠的是平台所有用户的日常使用。

---

#### 引擎二：拖拽即用——Gallery 之上的零门槛消费体验

被动生成解决了"组件从哪来"。但组件到了 Gallery 之后，用户怎么用？

当前方案中"浏览 Gallery → 复制 Prompt → 粘贴到 Lovable"的流程，本质上仍然是**开发者思维**：用户需要理解 Prompt、知道在哪粘贴、等待 AI 重新生成。对于非技术用户，"复制 Prompt"本身就是门槛。

**真正的降维打击是：用户在 Gallery 中看到一块好积木，直接拖到自己的项目画布上，它就出现在那里了。**

```
┌──────────────────────────────────────────────────────────┐
│  MeDo 项目编辑界面                                          │
│                                                          │
│  ┌─ Gallery 侧栏 ───────────┐  ┌─ 当前项目画布 ────────┐  │
│  │                          │  │                        │  │
│  │  [搜索] "pricing table"  │  │  ┌── Navbar ─────────┐ │  │
│  │                          │  │  │                    │ │  │
│  │  ┌──────────────────┐    │  │  └───────────────────┘ │  │
│  │  │ Pricing Table A  │    │  │                        │  │
│  │  │ [预览缩略图]      │    │  │  ┌── Hero ───────────┐ │  │
│  │  │ ⭐ 2.3k 使用      │    │  │  │                    │ │  │
│  │  │  拖→        ← 拖   │  │  │  └───────────────────┘ │  │
│  │  └──────────────────┘    │  │                        │  │
│  │                          │  │  ┌── Pricing ◄─ 拖进来的│  │
│  │  ┌──────────────────┐    │  │  │  从 Gallery 拖到     │  │
│  │  │ Pricing Table B  │    │  │  │  画布上直接用        │  │
│  │  │ [预览缩略图]      │    │  │  └───────────────────┘ │  │
│  │  └──────────────────┘    │  │                        │  │
│  │                          │  │                        │  │
│  │  AI 帮我生成更多...       │  │  继续拼...              │  │
│  └──────────────────────────┘  └────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

**拖拽 vs 复制 Prompt 的本质区别**：

| 复制 Prompt 方式 | 拖拽方式 |
|-----------------|---------|
| 理解 Prompt → 选平台 → 复制 → 打开工具 → 粘贴 → 等生成 | 看到 → 拖 → 放下 → 拼好了 |
| 需要知道 Prompt 是什么 | 不需要任何技术概念 |
| 结果不确定（每次生成可能不同） | 所见即所得——预览什么样，拖进去就是什么样 |
| 离开 MeDo 平台 | 全程在 MeDo 内完成 |

乐高叙事说"像积木一样拼"。拖拽是把积木盒（Gallery）放在手边，手伸过去拿一块放上去——这才是真正的乐高体验。如果每次拼积木还得先把说明书（Prompt）抄到另一张纸上，那就不叫积木了。

#### 两个引擎的协同关系

```
被动生成（引擎一）                    拖拽即用（引擎二）
     │                                    │
     │  AI 每次生成 App                   │  用户在 Gallery 中浏览
     │  自动分解为组件积木                  │  发现喜欢的 Navbar/Footer/...
     │  发布到 Gallery                    │  拖到当前项目画布
     │                                    │  立即可用
     │                                    │
     └────────────  Gallery  ──────────────┘
                组件汇聚地 + 发现平台
```

- **引擎一让 Gallery 永不枯竭**：用户越多，组件越多。不像 21st.dev 需要社区主动上传。
- **引擎二让 Gallery 直接可用**：不需要"复制 Prompt 粘贴到别处"，拖进来就是成品。
- **两者叠加**：Gallery 既是自动生长的内容池，也是拖拽即用的积木盒——构成了一个自循环的组件生态。

#### 这对非技术用户意味着什么

一个完全没有代码经验的用户，使用 MeDo 拼一个落地页：

1. 打开 MeDo，新建项目
2. 打开 Gallery 侧栏 → 搜索 "navbar" → 看到 50 个现成的导航栏积木 → **拖一个喜欢的到画布**
3. 搜索 "hero" → **拖一个首屏积木**
4. 搜索 "pricing" → **拖一个定价表积木**
5. 搜索 "footer" → **拖一个页脚积木**
6. 调整顺序 → 发布

全程不需要写一行代码、不需要理解组件是什么、不需要知道 Prompt。**像拼乐高一样拼网站。** 这个体验是 Lovable、Bolt、v0 目前都不具备的。

---

## 二、Landing Page 设计

### 2.1 URL 与页面结构

```
medo.dev/components
```

页面结构（从上到下）：

```
① Hero
   标题：Build Websites Like LEGO — AI Components That Snap Together
   副标题：Navbar, Hero, Pricing, Footer... pick your blocks, snap them together, ship in minutes. Works with MeDo, Lovable, Bolt, v0.
   CTA：[Browse Gallery]  [Start Building →]

② 核心逻辑（为什么是乐高）
   ┌─────────────────┬─────────────────┬─────────────────┐
   │ Pick a Block    │ Snap Together   │ Ship             │
   │ 从数千个组件中    │ 组件无缝拼接      │ 导出为完整页面    │
   │ 选你需要的积木    │ 间距、圆角、配色   │ 部署到 MeDo 或    │
   │                 │ 自动统一         │ 导出到任何工具    │
   └─────────────────┴─────────────────┴─────────────────┘

③ 核心功能三列
   ┌─────────────────┬─────────────────┬─────────────────┐
   │ AI Generate     │ Browse Gallery  │ Use Anywhere    │
   │ "给我一个定价表"  │ 数千个社区组件    │ 导出到 Lovable/  │
   │ → AI 生成积木    │ 一键拼进项目      │ Bolt/v0/Cursor  │
   └─────────────────┴─────────────────┴─────────────────┘

③ 组件分类展示（按搜索量排序）
   Navbar · Footer · Hero · Pricing Table · Forms · Card · Button · FAQ · Testimonials · Dashboard

④ 热门组件 Gallery（实时）
   展示 12-20 个精选组件，每个卡片：
     - 组件截图/预览
     - 组件名称 + 分类
     - "Import to MeDo" / "Copy Prompt for Lovable" 按钮

⑤ 使用流程
   Step 1: Browse or describe → Step 2: Preview → Step 3: Import or export

⑥ 数据社会证明
   "Join 17,000+ builders using MeDo Components" / "X,XXX components generated this week"

⑦ FAQ
   面向 SEO：AI component generator, navbar components, footer components, react components 等

⑧ Final CTA
```

### 2.2 组件分类页（每个分类独立 Landing Page）

```
medo.dev/components/navbar
medo.dev/components/footer
medo.dev/components/hero
medo.dev/components/pricing-table
medo.dev/components/forms
medo.dev/components/card
medo.dev/components/button
medo.dev/components/faq
medo.dev/components/testimonials
medo.dev/components/dashboard
```

每个分类页：该分类的组件 Gallery + 该分类的 AI 生成入口 + 对应的 SEO 内容。

### 2.3 核心宣传语（LEGO 叙事）

| 场景 | 宣传语 |
|------|--------|
| **首页 Banner** | "Components are LEGO blocks for your app. Pick, snap, ship." |
| **主 Hero** | "Build Websites Like LEGO — AI Components That Snap Together" |
| **Gallery 入口** | "Browse thousands of blocks. Snap together a website in minutes." |
| **对比 Lovable** | "Lovable makes you describe every block from scratch. MeDo gives you the pieces — just snap them together." |
| **对比 Bolt** | "Bolt gives you a blank canvas. MeDo gives you the LEGO set." |
| **对比 21st.dev** | "21st.dev has bricks. MeDo has bricks AND the person who hands you exactly the one you need." |
| **开源/GitHub** | "Open-source LEGO blocks for the AI era. Build anything, anywhere." |

---

## 三、关键词策略

### 3.1 关键词分层

#### 第一层：组件 Marketplace / Gallery 类（高意向）

| 关键词 | 说明 | 目前被什么占据 |
|--------|------|--------------|
| components marketplace | 用户想找组件市场 | 第三方组件市场、CMS 模板站 |
| AI component generator | 用户想用 AI 生成组件 | aiappbuilder、长尾博主 |
| AI component library | 用户想找 AI 组件库 | 各类 AI 组件项目 |
| component gallery | 用户想浏览组件 | CMS 组件展示页 |
| react components marketplace | React 组件市场 | 21st.dev、传统组件库 |

**MeDo 承接**：`/components` — "AI Components Marketplace & Gallery"

#### 第二层：具体组件名（长尾搜索量巨大）

| 关键词 | 搜索意图 | 目前被什么占据 |
|--------|---------|--------------|
| navbar components | 找导航栏组件 | Bootstrap、Tailwind CSS 文档、CMS 模板 |
| footer components | 找页脚组件 | WordPress 主题、Tailwind 模板 |
| hero section components | 找首屏组件 | 设计模板站 |
| pricing table components | 找定价表组件 | SaaS 模板站 |
| contact form components | 找联系表单组件 | CMS 插件 |
| card components | 找卡片组件 | CSS 框架文档 |
| button components | 找按钮组件 | UI 库文档 |
| faq components | 找 FAQ 组件 | WordPress 插件 |
| testimonial components | 找用户证言组件 | 设计模板站 |
| dashboard components | 找仪表板组件 | 管理面板模板 |
| landing page components | 找落地页组件 | Landing page 模板 |
| tailwind components | 找 Tailwind 组件 | Tailwind UI、社区 |

**MeDo 承接**：`/components/{navbar|footer|hero|...}` — 分类 Landing Page

#### 第三层：竞品组合词

| 关键词 | 意图 | 承接页面 |
|--------|------|---------|
| lovable components | Lovable 用户找组件 | `/components` + "Export to Lovable" |
| bolt new components | Bolt 用户找组件 | `/components` + "Export to Bolt" |
| v0 components | v0 用户找组件 | `/components` + "Export to v0" |
| cursor components | Cursor 用户找组件 | `/components` + "Export to Cursor" |
| 21st dev alternative | 21st.dev 替代品 | `/vs/21st-dev` 或 Blog |

#### 第四层：行为词

| 关键词 | 意图 | 承接 |
|--------|------|------|
| free AI components | 免费 AI 组件 | `/components` — "Free & Open Source" |
| open source react components | 开源组件 | `/components` — "Open Source" |
| copy paste components | 复制粘贴组件 | `/components` — "Copy, paste, use" |
| generate UI components AI | AI 生成 UI | `/components` — "AI Generate" |

### 3.2 关键词优先级矩阵（按搜索量 × 转化意图）

| 优先级 | 关键词 | Landing Page |
|--------|--------|-------------|
| P0 | AI component generator | `/components` |
| P0 | navbar components | `/components/navbar` |
| P0 | footer components | `/components/footer` |
| P0 | components marketplace | `/components` |
| P0 | hero section components | `/components/hero` |
| P1 | pricing table components | `/components/pricing-table` |
| P1 | card components | `/components/card` |
| P1 | button components | `/components/button` |
| P1 | faq components | `/components/faq` |
| P1 | landing page components | `/components` |
| P1 | lovable components | `/components` |
| P1 | tailwind components | `/components` |
| P2 | dashboard components | `/components/dashboard` |
| P2 | contact form components | `/components/forms` |
| P2 | testimonial components | `/components/testimonials` |
| P2 | bolt new components | `/components` |
| P2 | 21st dev alternative | Blog / `/vs/*` |

---

## 四、公开组件库 + 跨平台截留策略

### 4.1 设计原则

> MeDo Components 库是**公开的、开源的积木盒**。不锁定在 MeDo 平台内——Lovable 用户、Bolt 用户、v0 用户、Cursor 用户都可以拿一块积木去用。目的是让他们**先习惯用 MeDo 的积木拼东西，再发现 MeDo 才是最好的拼搭工作台**。

### 4.2 三种截留方式

#### 方式一：组件页面上的多平台入口

每个组件详情页同时提供：

```
┌──────────────────────────────────────────────────┐
│  Pricing Table Component                          │
│  [预览图]                                         │
│                                                   │
│  → Import to MeDo      (一键导入，推荐)            │
│  → Copy for Lovable    (复制 Prompt)              │
│  → Copy for Bolt.new   (复制 Prompt)              │
│  → Copy for v0         (复制 Prompt)              │
│  → Copy for Cursor     (复制 .tsx)                │
│  → Download Source     (下载源码)                  │
│                                                   │
│  💡 Built with MeDo. Try generating your own →    │
└──────────────────────────────────────────────────┘
```

- **"Import to MeDo" 是主 CTA**（引导到 MeDo）
- 其他按钮是**次要 CTA**（服务竞品用户，获取接触点）
- 底部引导语："Built with MeDo. Try generating your own →" 是引流

#### 方式二：导出 Prompt 中嵌入 MeDo 水印

Lovable/Bolt/v0 用户复制 Prompt 后，Prompt 末尾自动包含：

```
---
This component was generated by MeDo (medo.dev/components).
Browse 10,000+ more components → medo.dev/components
```

不破坏功能，但建立了品牌关联。

#### 方式三：GitHub 开源组件库

将精选组件开源到 GitHub：

```
github.com/medo-dev/components
```

- 每个组件一个文件夹（.tsx + 预览图 + Prompt）
- README 中引导到 medo.dev/components 获取更多
- 吸引 GitHub Star → 社区认知 → 转化为 MeDo 用户
- 对标 21st.dev (GitHub 开源 registry)

### 4.3 截留漏斗

```
竞品用户（Lovable / Bolt / v0 / Cursor）
  │
  ├── 搜索 "navbar components" → 搜到 medo.dev/components/navbar
  │     → 看到积木盒 → 拿走一块 Navbar → Prompt 底部有 MeDo 水印
  │
  ├── GitHub → github.com/medo-dev/components
  │     → Star / Fork → README: "拼完整页面？来 MeDo——最好的积木工作台"
  │
  ├── 朋友分享 → "用 MeDo 这块积木拼的"
  │     → 访问 medo.dev/components → 看到 "Snap into MeDo" 是主按钮
  │
  └── → 产生认知："拿积木去 MeDo，拼积木也在 MeDo"
        → 某天要建新项目 → "用 Lovable 还要自己去 21st.dev 找积木，MeDo 里直接有"
```

---

## 五、Go-to-Market 路径

### Phase 1：Landing Page + 被动捕获机制上线（4-6 周）

**交付物**：
- **核心机制**：AI 对话中每次生成 App，自动识别并捕获其中的可复用组件块——用户无需手动上传，"生成即产生组件"
- `medo.dev/components` Landing Page 上线
- 10 个分类子页面上线（/components/navbar 等）
- 初始 500+ 组件（由早期用户对话自然产生 + 从 MeDo 广场优质 App 中拆卸）
- 每个组件支持 "Copy for Lovable/Bolt/v0/Cursor"
- Gallery 侧栏上线：项目编辑界面内置 Gallery 面板，用户可浏览、搜索、拖拽 Gallery 中的组件到当前项目画布（基础版）
- GitHub 开源仓库 github.com/medo-dev/components 上线

**营销动作**：

| 渠道 | 内容 | 目标 |
|------|------|------|
| 21st.dev 社区 | 发布文章/评论："Tried 21st.dev, found MeDo Components — here's how they compare" | 从 21st.dev 2M MAU 中截流 |
| Lovable 社区/Discord | 分享组件："Found these MeDo components that work perfectly in Lovable" | 渗透 Lovable 用户 |
| Bolt Discord | 同上 | 渗透 Bolt 用户 |
| X (Twitter) | 每日分享 1 个组件："Today's free component: Responsive Navbar with dark mode — copy prompt, paste in Lovable/Bolt/v0" | 社媒传播 + SEO 信号 |
| Reddit (r/lovable, r/boltnew, r/vibecoding) | "I built a free component gallery that works with Lovable, Bolt, and v0 — medo.dev/components" | 社区渗透 |
| GitHub | 开源仓库上线 → 发布到 Hacker News "Show HN" | 开发者社区曝光 |

**成功指标**：
- `/components` 日均 UV ≥ 500
- 组件导出次数（Copy for Lovable/Bolt 等）≥ 200/天
- GitHub Star ≥ 200

### Phase 2：被动捕获规模化 + SEO 上量（8-12 周）

**交付物**：
- 被动捕获系统规模化：每位用户每次生成 App 均自动产出可复用组件（无需手动发布）
- 用户可将个人组件**一键发布到 Gallery** 供社区使用（或有权限设置仅自己可见）
- Gallery 组件数 ≥ 3,000（被动捕获 + 少量主动发布，非人工填充）
- 10 个分类 Landing Page 全量 SEO 优化（meta、schema、内链）
- 每个分类页 ≥ 20 个精选组件

**营销动作**：

| 渠道 | 内容 | 目标 |
|------|------|------|
| SEO | 持续创建分类页 + 组件页的内链网络 | 承接 "navbar components" 等关键词 |
| Blog | 《10 Best Navbar Components for Your Next AI-Generated App》《Free Footer Components That Work in Lovable, Bolt & MeDo》 | 长尾 SEO |
| Hackathon 组件赛道 | MeDo Hackathon 新增 "Best Component" 奖项 | 激发 UGC |
| 联盟素材 | 为 Affiliate 提供 "Top 50 Components" 素材包（含 Gallery 链接） | 联盟推广 |
| Product Hunt 更新 | "MeDo Components: Free, Open-Source UI Components for Any AI Builder" | 二次曝光 |
| Lovable 官方 | 尝试联系 Lovable 团队——建议 Lovable 文档也推荐 MeDo Components 作为组件源（同 21st.dev 一样） | 渠道合作 |

**成功指标**：
- `/components` 日均 UV ≥ 3,000
- 分类页 SERP 排名 Top 10（navbar components、footer components 等）
- Gallery 组件数 ≥ 3,000
- 导出次数 ≥ 1,000/天

### Phase 3：拖拽生态完善 + 跨平台（6 月+）

**交付物**：
- **拖拽即用体验升级**：Gallery 侧栏全面升级——分类筛选、预览放大、拖拽到画布自动匹配当前项目的设计风格（间距/配色自适应）。用户像逛积木店一样浏览 Gallery，看到喜欢的直接拖进项目
- MCP Server for Cursor / Claude Code（建议 Phase 2 即可 MVP）
- 一键导入插件：Lovable、Bolt 插件市场
- 组件作者激励机制（组件使用量 → MeDo credits 奖励）

**目标**：
- `/components` 月均 UV ≥ 100,000
- 成为除 21st.dev 外第二大的 AI 组件源
- GitHub Star ≥ 5,000
- 跨平台截留转化率 ≥ 5%（从竞品用户 → MeDo 注册）

---

## 六、内容营销计划

### 6.1 Blog 文章矩阵

| # | 标题 | 目标关键词 | 目标受众 |
|---|------|-----------|---------|
| 1 | MeDo Components: AI-Generated Building Blocks for Lovable, Bolt, v0 & More | MeDo components, free AI components | 所有 vibe coding 用户 |
| 2 | 10 Navbar Components You Can Copy-Paste Into Your AI-Generated App | navbar components, free navbar | Lovable/Bolt 用户 |
| 3 | Footer Components: 7 Free Blocks to Finish Your AI-Built Website | footer components | Lovable/Bolt 用户 |
| 4 | 21st.dev Alternative: Why MeDo Components Is the Better Choice for Non-Developers | 21st.dev alternative | 21st.dev 不满用户 |
| 5 | Build a Landing Page in 10 Minutes: Just Snap 6 Components Together | landing page components, build landing page fast | 所有用户 |
| 6 | Pricing Table Components: 7 Free Templates to Snap Into Your AI-Generated App | pricing table components | Indie 创始人 |
| 7 | Dashboard Components for AI-Built Apps: Free & Customizable | dashboard components | 工具类构建者 |
| 8 | Open Source React Components: MeDo vs 21st.dev vs shadcn/ui | open source react components | 开发者 |

### 6.2 社交媒体例行内容

| 频率 | 内容 |
|------|------|
| **每日** | "Today's free block: [组件名] — copy prompt, snap it into Lovable/Bolt/v0 → [链接]" |
| **每周 2 次** | 计时对比：手写 prompt 搭一个页面 vs 用 MeDo 组件拼接——哪个更快 |
| **每月 1 次** | "本月最受欢迎的 10 块积木" 合集 |

---

## 七、与现有 MeDo 功能的协同

| 现有功能 | AI Components 如何增强 |
|---------|---------------------|
| **AI 对话生成**（核心） | 每次生成 App → 自动捕获组件积木并发布到 Gallery。用户无需手动"制作组件"——用了 MeDo 就是在产组件。这是 MeDo 区别于 21st.dev 的根本优势 |
| **Gallery 拖拽** | Gallery 侧栏嵌入项目编辑器——用户浏览积木盒，看到好的直接拖到画布上用。非技术用户拼网站像拼乐高，不需要复制 Prompt 或理解技术概念 |
| **应用广场**（17k+ apps） | 从现有优质 App 中拆卸出组件积木 → 填充 Gallery——种子内容零成本 |
| **Hackathon** | 新增组件赛道 → 降低参与门槛（搭一块积木比搭一整栋楼容易） |
| **Affiliate (30%)** | Affiliate 推广"免费积木盒" → 组件是极易传播的内容（比推广整个平台更容易） |
| **对比页（/vs/*）** | 新增对比维度："Built-in Component Library"——Lovable/Bolt 没有内置积木盒；"Auto-Capture"——其他平台的组件每次都要重新生成，MeDo 自动存 |
| **模板页（/templates/*）** | 模板页下方嵌入对应的积木分类推荐——"这个模板用了这些组件，直接拿" |
| **Blog** | Blog 文章中嵌入组件积木卡片——读者看到就能直接复制拼进自己的项目 |

---

## 八、成功指标

| 指标 | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| `/components` 日均 UV | ≥ 500 | ≥ 3,000 | ≥ 10,000 |
| 分类页 SERP Top 10 数量 | — | ≥ 5 个关键词 | ≥ 15 个关键词 |
| Gallery 组件总数 | ≥ 500 (被动捕获) | ≥ 3,000 (规模化捕获) | ≥ 20,000 |
| 跨平台导出次数/天 | ≥ 200 | ≥ 1,000 | ≥ 5,000 |
| GitHub Star | ≥ 200 | ≥ 1,000 | ≥ 5,000 |
| 截留转化率 | — | ≥ 3% | ≥ 5% |
| Gallery 拖拽使用率 | ≥ 15% | ≥ 35% | ≥ 50% |

---

## 附录 A：21st.dev 参考数据

- **MAU**：2M（公开数据）
- **模式**：社区上传 React 组件 → 其他用户浏览 → 复制 Prompt → 粘贴到 Lovable/Bolt/Cursor
- **Lovable 集成**：Lovable 官方文档推荐，用户选组件 → 选 "Lovable" prompt 类型 → 复制 → 粘贴
- **定价**：$20/月
- **GitHub**：[21st-dev/registry](https://github.com/21st-dev/registry) — 开源 CLI

**可参考的策略**：21st.dev 成功在 Lovable 社区建立 "组件来源" 的认知。MeDo 可以复制这条路径——先在 Lovable/Bolt 社区中被认知为 "另一个组件源"，再引导用户到 MeDo 平台。

## 附录 B：关键词搜索量参考（方向性估算）

| 关键词 | 预估月搜索量 | 竞争度 |
|--------|------------|--------|
| navbar components | 高（5k-10k） | 中（CMS 模板占据） |
| footer components | 高（3k-8k） | 中 |
| components marketplace | 中（1k-3k） | 低 |
| AI component generator | 中（1k-3k） | 低 |
| hero section components | 中（1k-3k） | 中 |
| pricing table components | 中（500-2k） | 低 |
| card components | 高（5k+） | 高（CSS 框架占据） |
| button components | 高（5k+） | 高 |
| tailwind components | 高（5k+） | 高（Tailwind UI 占据） |
| open source react components | 中（1k-3k） | 中 |

---

## 附录 C：PR 消息模板（LEGO 叙事）

### 首次发布（Phase 1）

> **Introducing MeDo Components — LEGO Blocks for AI-Built Websites**
>
> Every website is made of the same pieces: Navbar, Hero, Pricing, Footer. MeDo Components gives you those pieces — AI-generated, production-ready, ready to snap together like LEGO.
>
> Pick a block. Snap it in. Ship.
>
> Works with MeDo, Lovable, Bolt, v0, and Cursor.
>
> Start building: medo.dev/components

### 竞品对比发布（Phase 2）

> **Same IDEA. Lovable vs Bolt vs MeDo. Guess which one is LEGO.**
>
> We asked Lovable, Bolt, and MeDo to build the same SaaS landing page.
>
> Lovable needed 47 prompts. Bolt needed 38. MeDo? 12 blocks. Snap. Done.
>
> [三列计时对比图]
>
> Your website isn't a blank page. It's 12 blocks waiting to be assembled.
> medo.dev/components

---

*本方案基于市场调研制定。MeDo 产品信息见 [medo.md](./medo.md)，竞品分析见 [medo-competitors.md](./medo-competitors.md)，关键词映射见 [medo-keywords.md](./medo-keywords.md)，增长策略见 [medo-growth-strategy.md](../archive/medo-growth-strategy.md)。*
*最后更新：2026-07-08*
