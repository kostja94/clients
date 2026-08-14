# Prediction Markets 技术栈与平台说明

> **文档边界**：本文档记录 predictionmarkets.org 的构建方式、平台能力与 SEO 适用性。  
> 关联：[predictionmarkets.md](./predictionmarkets.md) | [predictionmarkets-events.md](./predictionmarkets-events.md) | [predictionmarkets-features.md](./predictionmarkets-features.md)

**Last updated**: 2026-03-12

---

## 1. 构建方式

| 项目 | 内容 |
|------|------|
| **CMS** | Ghost |
| **网站** | https://www.predictionmarkets.org/ |
| **内容形态** | 博客文章（Posts）、静态页面（Pages）、标签（Tags）、Newsletter |

**技术栈决策**：当前使用 Ghost；若后续需求变化（如程序化 SEO 大规模扩展、复杂应用），可再评估迁移。

---

## 2. Ghost 是否 SEO 友好？

**结论：是。Ghost 对 SEO 友好，多数技术 SEO 需求已内置。**

### 2.1 内置 SEO 能力

| 能力 | 说明 |
|------|------|
| **性能** | 现代技术栈、语义化标记；页面加载快 |
| **结构化数据** | 自动为所有 Posts 和 Pages 添加结构化数据，便于搜索引擎理解内容 |
| **Canonical 标签** | 全站自动添加，避免重复内容问题 |
| **XML Sitemap** | 自动生成与更新，帮助搜索引擎发现内容 |
| **社交元数据** | 内置 Twitter Cards、Open Graph（Facebook） |
| **自定义元数据** | 每篇 Post/Page 可单独设置 meta title、description；留空则自动回退 |
| **Google Search Console** | 官方集成，可监控索引、展示、点击等 |

*来源：[Ghost SEO 官方文档](https://ghost.org/help/seo/)*

### 2.2 建议与注意

- 使用设计良好的主题，控制外部脚本和大文件数量，以保持页面速度
- 标签（Tags）对 SEO 有帮助：2–5 个相关标签、含长尾关键词
- 会员/付费内容：需区分公开内容（用于 SEO 引流）与付费内容

---

## 3. Ghost 能否搭建落地页与产品页？

**结论：可以。Ghost 不仅支持博客，也支持落地页、产品页等非博客页面。**

### 3.1 页面类型

| 类型 | 说明 |
|------|------|
| **Posts** | 博客文章，按时间线展示，支持标签、作者 |
| **Pages** | 静态独立页面，不进入博客时间线，可做落地页、产品页、About 等 |

### 3.2 落地页能力

| 能力 | 说明 |
|------|------|
| **自定义落地页** | 使用 Pages 功能，配合 Beta Editor 可隐藏标题和特色图，实现差异化布局 |
| **动态卡片** | 支持 Header、CTA、Signup、图片、Toggle 等卡片，无需写代码即可搭建落地页 |
| **无代码设计** | 通过页面设置中的开关即可隐藏标题/特色图，组合卡片完成落地页设计 |

*来源：[Ghost Create Landing Pages](https://ghost.org/changelog/create-landing-pages/)*

### 3.3 产品页能力

| 方式 | 说明 |
|------|------|
| **主题模板** | 部分 Ghost 主题（如 TanaFlows）提供产品页模板，可展示功能、定价、评价、CTA |
| **自定义模板** | 开发者可通过自定义 Page 模板实现产品页布局 |
| **原生元素组合** | 利用 Header、Signup、图片等原生卡片，配合 HTML/CSS 注入，可搭建产品展示页 |

### 3.4 注意事项

- **主题兼容**：落地页相关能力需官方主题最新版本或支持该功能的自定义主题
- **自定义主题**：若使用自定义主题，需开发者更新以支持新功能

---

## 4. Ghost Features 页面配置（可视化编辑）

> 适用于文字内容多、功能点多的 Features 页面。**全程在 Ghost Admin 后台可视化操作，无需写代码。**

### 4.1 是否可视化编辑？

**是。** Ghost 提供可视化编辑器（WYSIWYG），在后台直接编辑，所见即所得。

- **入口**：Ghost Admin → **Pages** → **New page**
- **编辑方式**：富文本 + 卡片（Cards），无需写代码

### 4.2 配置步骤

| 步骤 | 操作 |
|------|------|
| 1 | 登录 Ghost Admin（如 `yoursite.com/ghost`） |
| 2 | 左侧菜单选择 **Pages** → 右上角 **New page** |
| 3 | 输入标题（如 "Features"）和 URL（如 `/features`） |
| 4 | 在编辑器中输入正文，或按 `/` 插入卡片 |
| 5 | 右侧设置：Feature image、SEO meta、是否显示标题/特色图 |
| 6 | 发布后，在 **Settings → Navigation** 中把该页面加入导航 |

### 4.3 文字多时推荐使用的卡片

| 卡片 | 用途 |
|------|------|
| **Header** | 分段标题、副标题、可选 CTA |
| **Callout** | 重点说明、提示框 |
| **Toggle** | 可折叠内容（类似 FAQ） |
| **Button** | CTA 按钮 |
| **Divider** | 分隔线（输入 `---` 即可） |
| **Markdown** | 大段文字、列表、表格 |

**插入方式**：新起一行输入 `/`，在菜单中选对应卡片。

### 4.4 页面设置（右侧边栏）

- **Show title and feature image**：关闭后可做更自由的落地页布局
- **Feature image**：页面顶部大图（可选）
- **Meta data**：每页可单独设置 SEO title、description

### 4.5 主题与布局

- 页面外观由主题决定
- 若需自定义布局（如多列、特殊卡片布局），需选用支持该布局的官方主题或定制开发

---

## 5. 对 predictionmarkets.org 的启示

| 场景 | 建议 |
|------|------|
| **SEO** | Ghost 已覆盖技术 SEO 基础；重点做好内容、标签、元数据 |
| **Features 页面** | 用 Pages + 可视化编辑器；文字多时用 Header、Callout、Toggle、Markdown 等卡片；见 §4 |
| **落地页** | 可用 Pages + Beta Editor 搭建产品/功能介绍页、Newsletter 注册页等 |
| **程序化 SEO** | 事件页（如 [predictionmarkets-events.md](./predictionmarkets-events.md)）若需批量生成，需评估 Ghost 的 API 与主题对动态页面的支持 |
| **产品页** | 若有复杂产品展示（如多产品对比、定价表），可选用带产品模板的主题或定制开发 |

---

## 6. 参考链接

| 资源 | URL |
|------|-----|
| Ghost SEO 官方文档 | https://ghost.org/help/seo/ |
| Ghost 落地页更新 | https://ghost.org/changelog/create-landing-pages/ |
| Ghost Pages 说明 | https://ghost.org/help/pages/ |
| Ghost 编辑器介绍 | https://ghost.org/help/using-the-editor/ |
| Ghost 卡片说明 | https://ghost.org/help/cards/ |
| Ghost + Google Search Console | https://ghost.org/integrations/google-search-console |
| Ghost 主题市场 | https://ghost.org/themes |
