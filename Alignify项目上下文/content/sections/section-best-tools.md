# 产品展示（Best Tools）章节最佳实践

本文档定义产品展示章节的**通用规范**（格式、字数、布局、组件用法、内容质量）。

**主要适用范围**：Tools 页面的产品推荐、产品对比、排名列举。SEO/Marketing 若有类似产品展示需求可参考。

**参考**：BestTools 组件（`src/components/BestTools.tsx`）、[section-consistency](../content-rules/section-consistency.md)

---

## 〇、规则层级（必读）

| 层级 | 适用 | 说明 |
|------|------|------|
| **A 硬底线** | 组件使用、产品数量、比例、字数绝对上下限 | 不可逾越，违规必须修复 |
| **B 强建议** | shortDescription 最佳区间、描述最佳区间、风格统一 | 尽量达标，偏离需有理由 |
| **C 软建议** | 差异化表达、条件推荐语气、信息密度 | 内容质量导向，持续优化 |

---

## 一、定位与作用

**产品展示**是列举具体工具/产品的章节，核心作用是：

- **产品介绍**：每个产品包含名称、图片/视频、描述、CTA 按钮
- **垂直大图布局**：图片在上、文字在下，统一卡片样式
- **差异化定位**：每款产品的描述需回答「**最适合谁**」和「**与同页其他产品的关键差异**」
- **SEO 与转化**：产品描述含关键词，CTA 引导试用

---

## 二、通用规范

### 2.1 使用 BestTools 组件

**A 层硬底线**：Tools 页面的产品展示 **必须** 使用 `BestTools` 组件，禁止手写 HTML 卡片或 `<h2>` + `<p>` 占位。

**组件 Props**：
- `id`：章节锚点 ID
- `title`：H2 标题
- `introduction`：介绍段落
- `locale`：`"zh"` 或 `"en"`（影响按钮文案「试试」/「Try」）
- `tools`：`{ id, name, shortDescription, imageSrc?, imageAlt?, linkUrl, youtubeUrl?, description }[]`

**图片格式（三选一，推荐 imageSrc）**：
- **imageSrc + imageAlt**（推荐）：`imageSrc: "/tools/xxx/foo.jpg"` 或 YouTube 缩略图 URL，`imageAlt` 用于 SEO
- **image**（兼容）：`image: { src, alt }`，组件内部会转换为 imageSrc/imageAlt
- **video**（兼容）：`video: { videoId, videoUrl, title }`，组件自动生成 YouTube 缩略图；video 时需提供 videoUrl 以支持点击跳转

### 2.2 产品数量

**A 层硬底线**：每个 BestTools 块至少包含 **2 个产品**。单产品无法构成「排名/推荐」。

### 2.3 篇幅

#### 硬底线（A 层）

| 项目 | 中文 | 英文 | 说明 |
|------|------|------|------|
| **shortDescription 上限** | ≤ 25 字 | ≤ 50 字符 | 防止撑破卡片布局 |
| **shortDescription 下限** | ≥ 4 字 | ≥ 10 字符 | 防止无信息量（如单字"好"） |
| **产品 description 上限** | ≤ 400 字 | ≤ 800 字符 | 防止堆砌 |
| **产品 description 下限** | ≥ 100 字 | ≥ 280 字符 | 防止信息空洞，至少说清定位+功能+适用场景 |
| **同页 max/min 比例** | < 3x | < 3x | 避免极端篇幅悬殊 |

**shortDescription 额外硬底线**：不得与产品 name 重复或高度重叠。例如 name 为 "Style3D AI"，shortDescription 写 "Style3D AI Tool" 视为违规（重复产品名）。

#### 强建议（B 层）

| 项目 | 中文（建议） | 英文（建议） |
|------|-------------|-------------|
| **shortDescription** | 6–18 字 | 15–35 字符 |
| **产品 description** | 180–260 字 | 350–650 字符 |
| **风格统一** | 同页各 shortDescription 句式统一 | 同上 |

#### 软建议（C 层）

纯内容质量导向，不限字数，旨在提升读者决策效率：

| 原则 | 说明 |
|------|------|
| **差异化原则** | 每款描述必须包含：① 核心定位 ② 最适合谁（Ideal for / Perfect for）③ 与同页其他产品的关键差异点 |
| **条件推荐语气** | 使用 "Ideal for / Perfect for / Best suited for / 最适合" 等条件推荐语，而非泛泛的 "Great tool / 优秀工具" |
| **避免冗余** | 跨产品描述不重复相同的功能点表述；同页产品避免同一句式套壳（如全部以 "XXX is a powerful platform that..." 开头） |
| **通用句禁止** | 禁止 "dramatically improving efficiency" "revolutionizing the industry" "显著提升效率" "彻底改变行业" 等无信息量的空洞结尾 |
| **信息密度** | 每个词承载信息，避免 "Comprehensive Solution" "Professional Platform" "全面解决方案" 等无辨识度标签 |

详见 [§四 内容质量要求](#四内容质量要求)。

### 2.4 标题格式

- **H2 格式**：`[年份] 年最好的 [工具分类]`（中文）/ `Best [Tool Category] [Year]` 或 `[Year] Best [Tool Category]`（英文）
  - 示例：`2026 年最好的 AI 时尚工具` / `2026 Best AI Fashion Tools: Design & Styling Innovation`
  - 允许加冒号副标题提供额外语境
- **H3 格式**：`[序号]. [产品名称]：[shortDescription]`
  - shortDescription 渲染为冒号后的文本，与产品名自然衔接
  - 示例：`1. Style3D AI：3D Garment Design & Virtual Try-On`

### 2.5 布局要求

- **卡片样式**：`border-2 border-border rounded-lg p-6 bg-muted/40 shadow-md my-8`
- **图片**：居中，`w-full rounded-lg shadow-lg`，支持 `loading="lazy"`；Alt 与文件名规范参见图片 SEO 规范
- **按钮**：居中，`btn-external-link`，文案 `试试 [产品名称]`（中文）或 `Try [产品名称]`（英文）；外链自动使用 `addUtmToExternalLink` 和 `getExternalLinkRel`
- **描述容器**：`product-description` 类

---

## 三、shortDescription 格式指南

shortDescription 渲染为 `[序号]. [产品名]：[shortDescription]` 中冒号后的部分，本质是**品类标签 / 角色识别词**。

### 3.1 三种推荐格式

| 类型 | 格式 | EN 示例 | ZH 示例 |
|------|------|---------|---------|
| **功能定位型** | `[核心功能] [品类名词]` | "Real-Time Voice Changer"、"3D Garment Simulator" | "实时变声工具"、"3D 服装模拟器" |
| **差异化定位型** | `[核心优势] [品类]` | "Enterprise-Grade Code Review"、"Open-Source 3D Engine" | "企业级代码审查"、"开源 3D 引擎" |
| **场景定位型** | `[场景/人群] [功能]` | "E-Commerce Model Generation"、"Social Media Video Clipping" | "电商模特生成"、"社媒视频剪辑" |

### 3.2 禁止格式

| 反模式 | 问题 | 示例 |
|--------|------|------|
| 纯形容词堆砌 | 无信息量 | ❌ "Powerful Professional Platform" |
| 重复产品名 | 废话 | ❌ name="Style3D AI" + shortDescription="Style3D AI Tool" |
| 过度通用标签 | 无法区隔产品 | ❌ "Comprehensive Solution"、"AI Tool" |
| 功能罗列 | 短描述不应是功能清单 | ❌ "Design, Try-On, Model Generation, Analytics" |

### 3.3 同页一致性

同一页面内各产品的 shortDescription 应保持**句式结构统一**。如果第一个产品用「功能定位型」，其他产品也应用同一类型，避免混用。

---

## 四、内容质量要求

### 4.1 产品描述的必备要素

每款产品描述应在一段内包含以下三个要素（C 层软建议）：

| 要素 | 位置建议 | EN 示例 |
|------|----------|---------|
| **核心定位** | 首 1-2 句 | "Style3D AI is the most comprehensive 3D fashion design platform..." |
| **关键功能/差异化** | 中段 | "Unlike basic try-on tools, it provides full 3D garment simulation, pattern generation, and intelligent stitching..." |
| **最佳适用场景/人群** | 尾 1-2 句 | "Ideal for fashion brands and design teams requiring end-to-end 3D workflows." |

### 4.2 差异化写作原则

同页产品描述应让读者能快速区分**每款产品最适合什么场景**：

- ✅ **好**：每款以不同定位词开头，尾句给出不同的 "Ideal for"
- ❌ **差**：三款产品都以 "XXX is a powerful platform that..." 开头，尾句都是 "suitable for various needs"

### 4.3 禁止的冗余表达

| 类别 | 禁止表达 | 替代方案 |
|------|----------|----------|
| 空洞副词 | "dramatically"、"revolutionarily"、"incredibly" | 删除或用具体数据替代 |
| 万能结尾 | "This tool will significantly improve your workflow and efficiency." | 写具体的 "Ideal for..." 收尾 |
| 废话定语 | "comprehensive solution"、"powerful platform"、"innovative technology" | 写具体的功能或优势 |
| 功能堆砌 | "Supports A, B, C, D, E, F, G, and H." | 选 2-3 个最核心的差异化功能 |

### 4.4 条件推荐语气

使用 "Best for / Ideal for / Perfect for / Particularly suitable for" 等条件推荐语收尾，而非泛泛的结论。这既帮助读者决策，也符合 Google 对「有帮助的内容」的评价标准。

---

## 五、产品图片优先级

### 5.1 优先级顺序

1. **产品代表页面截图**（最高，Firecrawl 抓取）：默认使用 JSON 中的 `linkUrl`；当首页无法展示核心 UI（营销页、登录墙、功能在子路径）时，在 `scripts/data/tools-screenshot-registry.json` 中指定 `screenshotUrl`。使用本地路径 `/tools/{page-slug}/{product-slug}.jpg`（或历史 `/seo/` 路径），通过 `scripts/ops/screenshot-tools-products.py` 批量抓取。截图配置 `fullPage: false`（仅首屏，非全页）。
2. **官方演示视频**：仅当产品无独立官网可截图，或产品本身是视频型工具（如 Nano Banana）时使用。此时 `imageSrc` 使用 YouTube 缩略图 URL，同时保留 `youtubeUrl` 字段供点击跳转。
3. **已有本地截图**：从现有截图库复用。
4. **通用图片**：以上均不可用时的最后手段。

### 5.2 YouTube 缩略图规则

- **YouTube 缩略图 URL**：`https://img.youtube.com/vi/[VIDEO_ID]/maxresdefault.jpg`
- **不应滥用 YouTube 缩略图**：如果产品有真实官网，优先使用 Firecrawl 首页截图，而非 YouTube 视频缩略图。YouTube 缩略图仅在以下情况使用：
  - 产品官网就是 YouTube 视频（无独立网站）
  - 产品是纯视频/演示类工具
  - 产品官网无法正常抓取（如需要登录、反爬严格）
- **现有 YouTube 缩略图存量**：109 个产品当前使用 YouTube 缩略图作为主图（详见 `knowledge/tools/screenshot-audit-youtube-2026-05.md`），分阶段迁移为 Firecrawl 首页截图。

### 5.3 Firecrawl 截图规范

| 参数 | 值 | 说明 |
|------|-----|------|
| `fullPage` | `false` | 仅截首屏（viewport），非全页截图 |
| `quality` | `90` | JPEG 质量（推荐 90；最低 85） |
| 输出格式 | `.jpg` | 统一使用 JPEG |
| 命名规则 | `{product-slug}.jpg` | 小写、连字符分隔、无 vendor 前缀 |
| 存放路径 | `public/tools/{page-slug}/{product-slug}.jpg` | 按页面分组 |

**独立使用视频预览**（非 BestTools）：参见 [section-youtube-thumbnail](./section-youtube-thumbnail.md)

---

## 六、实现示例

```tsx
<BestTools
  id="ai-image-tool-details"
  title="各类型AI图片工具详细介绍"
  introduction="我们为不同类型的AI图片工具创建了详细的指南页面..."
  tools={[
    {
      id: "ai-image-generation",
      name: "AI图片生成（文生图+图生图）",
      shortDescription: "文字或图像生成图片",
      imageSrc: "/tools/image-generator/flux.jpg",
      imageAlt: "AI图片生成工具界面展示...",
      linkUrl: "/zh/tools/image-generator",
      youtubeUrl: "https://www.youtube.com/watch?v=xxx", // 可选
      description: "AI图片生成工具根据文本描述自动生成新图像，支持文生图和图生图两种模式..."
    },
    // ...
  ]}
/>
```

---

## 七、迁移检查清单

- [ ] BestTools 组件已正确导入
- [ ] 所有产品数据完整（id, name, shortDescription, imageSrc, linkUrl, description）
- [ ] shortDescription 符合 A 层硬底线（10-50 字符 EN / 4-25 字 ZH；不重复产品名）
- [ ] 产品描述符合 A 层硬底线（280-800 字符 EN / 100-400 字 ZH）
- [ ] 同页 max/min 描述比例 < 3x
- [ ] 每款描述包含：核心定位 + 关键差异 + 最佳适用场景
- [ ] 图片路径正确且文件存在于 `/public/tools/[page-name]/`
- [ ] YouTube 视频 ID 正确（如适用）
- [ ] 产品描述中无 `<Link>` 组件
- [ ] 同页 shortDescription 风格统一

---

## 八、常见错误

- ❌ 图片文件不存在
- ❌ 产品描述仍含内链
- ❌ 按钮文案使用「访问官网」而非「试试 XXX」
- ❌ H3 标题在卡片外
- ❌ **图片不显示**：若使用 `image` 或 `video` 格式，需确保 BestTools 为最新版本（已支持自动转换）；**应迁移为 `imageSrc`/`imageAlt`/`youtubeUrl` 规范格式**
- ❌ 使用原始 HTML 替代 BestTools 组件
- ❌ shortDescription 与产品名重复
- ❌ shortDescription 为纯形容词堆砌（"Powerful Professional Platform"）
- ❌ 多款产品描述套用同一模板仅替换关键词
- ❌ 产品描述以 "dramatically improving efficiency" 等空洞句结尾
- ✅ 使用 BestTools 组件，垂直大图布局，shortDescription 信息密集，描述区隔清晰

---

## 九、格式迁移（image/video → imageSrc/imageAlt/youtubeUrl）

**背景**：组件已兼容 `image`、`video` 旧格式，但新内容应统一使用规范格式。

**迁移规则**：

| 原格式 | 迁移为 |
|--------|--------|
| `image: { src: "...", alt: "..." }` | `imageSrc: "..."`，`imageAlt: "..."` |
| `video: { videoId: "xxx", videoUrl: "https://...", title: "..." }` | `imageSrc: "https://img.youtube.com/vi/xxx/maxresdefault.jpg"`，`imageAlt: "..."`（title），`youtubeUrl: "https://..."` |

**批量迁移已全部完成**（2026-02-11）：全站 JSON 文件中的 `image`/`video` 旧格式已统一迁移为 `imageSrc`/`imageAlt`/`youtubeUrl` 规范格式。

---

## 十、文档修订

| 日期 | 说明 |
|------|------|
| 2026-02-11 | 初版 |
| 2026-05-10 | 全面重写：引入 A/B/C 三级规则分层；shortDescription 上限从 15 字符放宽至 50 字符（硬）/ 35 字符（软），增加下限和格式指南；描述增加 280 下限和 800 上限（硬），保留 350-650 为软建议；新增 §三 shortDescription 格式指南、§四 内容质量要求（差异化原则、条件推荐、反模式） |
