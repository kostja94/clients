# MeDo /components 组件页面分析报告

> 分析日期：2026-07-31
> 数据来源：https://miaoda.io/components（全部 17 个详情页逐页分析）、shadcn/ui 完整组件列表、Landingfolio（4650+ 组件示例）、21st.dev 社区组件库（全部分类）、UXPin 设计系统分析、trinkui/Vireya/Layered-UI 等主流组件库
>
> **关联文档**：[medo-ai-components-strategy.md](./medo-ai-components-strategy.md)

---

## 一、当前 MeDo /components 已有内容（17 个）

| # | 名称 | URL | 分类 |
|---|------|-----|------|
| 1 | Navbar | /components/navbar | 组件 |
| 2 | Header | /components/header | 组件 |
| 3 | Sidebar | /components/sidebar | 组件 |
| 4 | Breadcrumb | /components/breadcrumb | 组件 |
| 5 | Footer | /components/footer | 组件 |
| 6 | Hero Section | /components/hero-section | 页面区块 |
| 7 | Testimonials | /components/testimonials | 页面区块 |
| 8 | Gallery | /components/gallery | 页面区块 |
| 9 | Feature Grid | /components/feature-grid | 页面区块 |
| 10 | Blog Section | /components/blog-section | 页面区块 |
| 11 | CTA Section | /components/cta-section | 页面区块 |
| 12 | Pricing Table | /components/pricing-table | 页面区块 |
| 13 | Contact Form | /components/contact-form | 组件 |
| 14 | Newsletter Signup | /components/newsletter-signup | 页面区块 |
| 15 | Cookie Banner | /components/cookie-banner | 组件 |
| 16 | Loading Spinner | /components/loading-spinner | 组件 |
| 17 | 404 Page | /components/404-page | **独立页面** |

---

## 二、多余项 —— 不属于组件的页面

### 2.1 明确是独立页面（Page），不是组件

| # | 名称 | 问题 | 建议 |
|---|------|------|------|
| 1 | **404 Page** | 这是一个**完整的独立页面**（居中布局、大号 404 数字、文案、回首页按钮），不是可嵌入的 UI 零件。其页面内容自身也明确说了 *"a fully designed not-found page"*。 | 应移至独立分类（如 `/pages/404`）或标注为 Page 而非 Component |

### 2.2 功能高度重复

| 重复组 | 问题 | 建议 |
|--------|------|------|
| **Navbar** vs **Header** | 两者功能几乎相同：顶部品牌区 + 导航链接 + CTA 按钮 + 响应式汉堡菜单 + 滚动粘性。Navbar 多了下拉菜单，Header 多了毛玻璃效果，但本质上是同一个组件的两个变体。 | 合并为一个 **Navigation** 组件，通过 variant 切换（Navbar / Header / Sticky / Transparent） |

### 2.3 被埋没的独立组件

以下组件在 MeDo 中作为 Section 的子元素存在，但**实际是独立可复用的通用组件**，MeDo 未将它们独立列出：

| 嵌入式组件 | 当前所在位置 | 说明 |
|-----------|-------------|------|
| Lightbox | Gallery 内部 | 全屏图片预览，含键盘导航、焦点捕捉、左右箭头——21st.dev 有大量独立 Lightbox 实现 |
| Star Rating | Testimonials 内部 | 评分星星展示/交互，可独立使用 |
| Testimonial Card | Testimonials 内部 | 单张客户评价卡片（头像+引言+姓名+职位） |
| Gallery Image Card | Gallery 内部 | Masonry 网格单项（图片+hover覆盖层+标题） |
| Pricing Tier Card | Pricing Table 内部 | 单个定价套餐卡 |
| Billing Toggle | Pricing Table 内部 | 月/年计费切换开关 |
| Feature Card | Feature Grid 内部 | 单张特性卡片（图标+标题+描述） |
| Blog Post Card | Blog Section 内部 | 文章卡片（封面图+标签+标题+日期+作者） |
| Category Filter Bar | Blog Section / Gallery 内部 | 分类筛选标签条 |
| Email Capture Form | Newsletter Signup | 单输入框邮件收集表单 |
| Social Proof Logo Strip | Hero Section 内部 | 客户/合作伙伴 Logo 行 |

---

## 三、缺失项 —— 按重要性排列

### 3.1 ⭐⭐⭐ 几乎所有网站必备（MeDo 完全缺失）

| # | 组件名称 | 类型 | 说明 |
|---|---------|------|------|
| 1 | **Button** | 原子 | 按钮系统（Primary/Secondary/Ghost/Destructive + 多种尺寸 + loading/disabled 态），占设计系统组件的 23.6%，是最重要的基础组件。21st.dev 有 2043 个按钮实现 |
| 2 | **Input / Textarea** | 原子 | 文本输入框 + 多行文本，所有表单的基础。21st.dev 有 949 个 Input、187 个 TextArea |
| 3 | **Checkbox / Radio Group** | 原子 | 多选/单选，表单标配。21st.dev 有 238 个 Checkbox、152 个 Radio Group |
| 4 | **Select / Dropdown** | 原子 | 下拉选择器，选项 >5 个时必用。21st.dev 有 316 个 Select、506 个 Dropdown |
| 5 | **Toggle / Switch** | 原子 | 开关切换，设置页标配。21st.dev 有 532 个 Toggle |
| 6 | **Card** | 复合 | 最通用的内容容器，10 个主流框架实现。21st.dev 有 1780 个 Card |
| 7 | **Modal / Dialog** | 复合 | 模态弹窗，11 个框架实现，弹窗是 Web 标配。21st.dev 有 328 个 Dialog/Modal |
| 8 | **Alert Dialog** | 复合 | 确认弹窗（删除确认、操作确认），几乎每站必备 |
| 9 | **Tooltip** | 复合 | hover 提示气泡。21st.dev 有 267 个 Tooltip |
| 10 | **Toast / Notification** | 复合 | 操作反馈通知（成功/失败/警告）。21st.dev 有 79 个 Toast、247 个 Notification |
| 11 | **Tabs** | 复合 | 标签页切换，11 个框架实现。21st.dev 有 239 个 Tabs |
| 12 | **Accordion** | 复合 | 折叠面板，10 个框架实现。21st.dev 有 234 个 Accordion |
| 13 | **Badge** | 复合 | 徽标/角标（通知数、状态标签）。21st.dev 有 605 个 Badge |
| 14 | **Avatar** | 复合 | 用户头像。21st.dev 有 597 个 Avatar |
| 15 | **Search Bar** | 复合 | 搜索输入栏，10 大基本 GUI 元素之一。21st.dev 有 222 个 Search Bar |
| 16 | **Dropdown Menu** | 复合 | 用户菜单/操作菜单。21st.dev 有 287 个 Menu |
| 17 | **FAQ Section** | 区块 | 折叠问答区，几乎所有 SaaS 站必备。21st.dev 有 191 个 FAQ |
| 18 | **Logo Cloud / Partners** | 区块 | 客户/合作伙伴 Logo 展示条。21st.dev 有 17 个 Clients |
| 19 | **Stats / Metrics Counter** | 区块 | 数字统计区。21st.dev 有 153 个 Stats & KPIs |
| 20 | **Team Section** | 区块 | 团队成员展示。21st.dev 有 119 个 Team Sections |
| 21 | **Contact Section** | 区块 | 联系方式区块（区别于 Contact Form 组件） |
| 22 | **Sign Up / Sign In** | 区块 | 注册/登录表单区。21st.dev 有 103 个 Sign In、58 个 Sign Up |
| 23 | **Alert / Banner** | 复合 | 通知横幅（info/success/warning/error）。21st.dev 有 240 个 Alert |
| 24 | **Table / Data Table** | 复合 | 数据表格。21st.dev 有 313 个 Table |
| 25 | **Pagination** | 复合 | 分页器。21st.dev 有 130 个 Pagination |

### 3.2 ⭐⭐ 大部分网站需要

| # | 组件名称 | 类型 | 21st.dev 数量 | 说明 |
|---|---------|------|--------------|------|
| 26 | Date Picker / Calendar | 原子/复合 | 250 + 239 | 日期选择器 + 完整日历视图 |
| 27 | Slider | 原子 | 217 | 滑动条（价格范围、评分等） |
| 28 | Combobox | 原子 | -- | 搜索式下拉选择 |
| 29 | Skeleton Loader | 复合 | 480 (Spinner Loaders) | 骨架屏加载占位 |
| 30 | Progress Bar | 复合 | 375 | 进度条 |
| 31 | Drawer / Sheet | 复合 | -- | 侧滑面板（移动端菜单/详情） |
| 32 | Empty State | 复合 | 77 | 无数据空状态占位 |
| 33 | Steppers | 复合 | 124 | 步骤条（多步表单、引导流程） |
| 34 | How It Works | 区块 | -- | 步骤流程/工作原理 |
| 35 | Integrations | 区块 | -- | 集成/连接器展示 |
| 36 | Demo / Product Showcase | 区块 | -- | 产品演示区 |
| 37 | Case Studies | 区块 | -- | 案例研究 |
| 38 | About Section | 区块 | -- | 关于我们区块 |
| 39 | Promotion Bar | 区块 | -- | 页顶促销条 |
| 40 | Profile | 复合 | 270 | 个人资料展示 |
| 41 | Tags | 复合 | 74 | 可交互标签 |
| 42 | Lists | 复合 | 349 | 高级列表（拖拽排序、虚拟滚动） |
| 43 | Forms (Container) | 复合 | 1522 | 表单容器+验证系统 |
| 44 | Links | 复合 | 354 | 链接样式与交互动效 |
| 45 | Onboarding | 复合 | 53 | 新手引导/Product Tour |
| 46 | File Upload | 复合 | 154 | 文件上传 |
| 47 | Input OTP | 原子 | -- | 验证码输入 |

### 3.3 ⭐ 特定场景需要

| # | 组件名称 | 类型 | 21st.dev 数量 | 说明 |
|---|---------|------|--------------|------|
| 48 | Carousel | 复合 | 239 | 图片/卡片轮播 |
| 49 | Popover | 复合 | 179 | 浮动内容面板 |
| 50 | Hover Card | 复合 | -- | hover 展开预览卡片 |
| 51 | Context Menu | 复合 | -- | 右键菜单 |
| 52 | Command Palette | 复合 | -- | cmd+k 命令面板 |
| 53 | Kbd | 复合 | -- | 键盘快捷键展示 |
| 54 | Separator | 复合 | -- | 视觉分隔线 |
| 55 | Scroll Area | 复合 | 293 | 自定义滚动区样式 |
| 56 | Chart / Data Viz | 复合 | 246 | 图表组件 |
| 57 | Before / After | 复合 | -- | 前后对比滑块 |
| 58 | Timeline | 复合 | 74 | 时间轴 |
| 59 | Maps | 复合 | 51 | 嵌入式地图 |
| 60 | Icons | 复合 | 851 | 图标系统组件 |
| 61 | Grids & Bento | 复合 | 620 | Bento 网格布局 |
| 62 | Numbers | 复合 | 54 | 数字滚动动画 |
| 63 | Calendars | 复合 | 239 | 完整月/周/日视图日历 |

### 3.4 2025-2026 年新兴类别（来自 21st.dev）

| # | 组件名称 | 21st.dev 数量 | 说明 |
|---|---------|--------------|------|
| 64 | **AI Chats** | 248 | AI 聊天界面（ChatGPT 风格对话组件）—— AI 时代新兴需求 |
| 65 | **Dashboards** | 400 | 完整仪表盘页面（KPI 卡片+图表组合） |
| 66 | **File Trees** | 61 | IDE 风格文件树/目录浏览器 |
| 67 | **Shaders / Backgrounds** | 新类 + 365 | WebGL 着色器 + 背景特效（液态金属、粒子效果） |
| 68 | **Marquees** | 113 | 跑马灯/无限滚动文本条 |
| 69 | **Docks** | 49 | macOS 风格底部 Dock 导航 |
| 70 | **Cursors** | 152 | 自定义光标/鼠标跟随特效 |
| 71 | **Globes** | 41 | 3D 交互式地球仪 |
| 72 | **Texts** | 663 | 文本特效（渐变文字、打字机、闪烁文字） |
| 73 | **Videos** | 162 | 视频背景/嵌入/轮播 |
| 74 | **Borders** | 111 | 边框装饰组件 |
| 75 | **Announcements** | 71 | 公告/通知横幅 |
| 76 | **Gradients** | 新类 | CSS 渐变效果组件 |

### 3.5 缺失的独立页面

| # | 页面 | 说明 |
|---|------|------|
| 77 | Sign In Page | 独立登录页 |
| 78 | Sign Up Page | 独立注册页 |
| 79 | Reset Password Page | 忘记密码/重置密码页 |
| 80 | About Page | 关于我们页面 |
| 81 | Contact Page | 联系我们页面 |
| 82 | Blog Index Page | 博客列表页 |
| 83 | Blog Post Page | 文章详情页 |
| 84 | Search Results Page | 搜索结果页 |
| 85 | Terms / Privacy Page | 条款隐私政策页 |

---

## 四、数据统计总览

```
═══════════════════════════════════════════════════
  MeDo /components 现状
═══════════════════════════════════════════════════
  现有总数：              17 个
  ─────────────────────────────────────────────
  真正的组件 (Component)：  8 个
  页面区块 (Section)：      8 个  ← 挂在 "components" 下不够精确
  独立页面 (Page)：         1 个  ← 不是组件，应移除
  ─────────────────────────────────────────────
  多余/重复项：             2 个
    - 404 Page（不是组件）
    - Navbar ↔ Header（功能高度重复，应合并）
  ─────────────────────────────────────────────
  缺失组件总数：            约 76 个
    原子组件缺失：          13 个
    复合组件缺失：          37 个
    页面区块缺失：          18 个
    独立页面缺失：           8 个
═══════════════════════════════════════════════════
```

---

## 五、建议优先级

### P0 立即补充（网站存在感极弱的基础组件）

Button、Input、Card、Modal、Tooltip、Toast、Tabs、Accordion、Badge、Avatar、Alert、Search Bar、Dropdown Menu

### P1 尽快补充（营销站/产品站高频需求）

FAQ Section、Logo Cloud、Stats Counter、Team Section、Pricing Tier Card、Sign Up/Sign In Block、Contact Section、Table、Pagination、Skeleton、Progress Bar、Date Picker、Steppers、Empty State

### P2 规划补充（差异化竞争力）

Carousel、Drawer、Popover、Hover Card、Chart/Data Viz、Onboarding、File Upload、Tags、How It Works Section、Integrations Section、Case Studies Section

### P3 创新补充（2025-2026 新兴趋势）

AI Chat Interface、Dashboard、File Tree、Shaders/Backgrounds、Marquees、Docks、Cursors、Bento Grid、Timeline、Globe、Gradients

### 架构建议

考虑将 /components 拆分为三条路径：

```
/components/         → 原子级组件（Button, Input, Card, Modal...）
/sections/           → 页面区块（Hero, FAQ, Pricing, Testimonials...）
/pages/              → 独立页面（404, Sign In, About, Contact...）
```

这样可以消除当前"404 Page 和 Button 放在同一个列表"的混乱问题。

---

*报告依据数据来源：*
- *https://miaoda.io/components （全部 17 个详情页逐页分析）*
- *https://ui.shadcn.com/llms.txt （shadcn/ui 完整 57 个组件）*
- *https://21st.dev/community/components （全部分类统计，含量化数据）*
- *Landingfolio 4650+ 组件示例分类*
- *UXPin、Supernova.io 设计系统分析*
- *trinkui、Vireya、Layered-UI、Ona 等主流组件库分类体系*
