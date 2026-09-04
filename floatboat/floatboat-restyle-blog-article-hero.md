# Floatboat 任务单 — Blog 文章页 Hero / TL;DR / TOC 版式改造

> **任务类型**：页面版式改造（模板布局重构 + 社交分享 UI；不涉及文章内容）
> **目标域名**：floatboat.ai
> **状态**：待处理
> **优先级**：P1（全站 Blog 文章页共用模板；单点改动即全覆盖）
> **提交**：2026-09-03

---

## 1. 任务目标

对 floatboat.ai 全部 Blog 文章页（`https://floatboat.ai/blog/{slug}`）的文章页模板做版式重构，使其 hero（首屏头部区）与正文区结构按本单 §2.3「期望版式」改造，同时**不修改任何文章内容**（`.md` 源文件、frontmatter、正文文案、图片资源一律不动，只改渲染模板与样式）。

完成判定标准：

- 桌面端 hero 变为**左右两栏**：左栏为标签 pill、标题、描述（含日期/阅读时长行），右栏为封面图——封面图从当前「hero 文字下方」上移为与文字同排；
- hero 与 TL;DR 区块为**全宽横贯**区段（不再被右侧 TOC 栏挤压为窄列）；
- 目录（Table of Contents）**从正文开始处出现**（视觉上不与 hero/TL;DR 同起点并排），保持吸顶跟随；
- 目录卡片内新增**分享到社交媒体的按钮**（X / LinkedIn / Facebook / 复制链接等）；
- 全站任一文章页生效，文章正文与既有功能（面包屑/返回链接、订阅块、FAQ 锚点）无回归。

---

## 2. 问题证据（2026-09-03 实测）

### 2.1 当前页面 DOM 结构（实测抓取渲染后 HTML）

对 `https://floatboat.ai/blog/gemini-3-8-flash` 的渲染后 HTML 抓取，正文区顶层结构（已省略 script/link 与长文本）：

```html
<section class="py-16 md:py-20">
  <div class="mx-auto w-full max-w-[1440px] px-10 max-lg:px-5">
    <a href="/blog" class="inline-flex items-center gap-2 ...">← Back to Blog</a>   <!-- 头部返回链接/面包屑区 -->

    <!-- 关键：整个页面为“左内容 + 右 360px TOC”的两栏网格，从 hero 处即开始 -->
    <div class="mt-10 grid grid-cols-1 gap-10 lg:grid-cols-[minmax(0,1fr)_360px]">
      <article>
        <!-- hero 文字块：仅文字，无图 -->
        <header class="max-w-[920px] space-y-4">
          <div class="flex flex-wrap gap-2"><span class="... rounded-xl ...">Label</span></div>  <!-- tag pill -->
          <div class="... text-[#7a7671]"><span>Sep 3, 2026</span>·<span>21 min read</span></div>
          <h1 class="font-serif ...">Gemini 3.8 Flash — Google's New Coding &amp; Agent Workhorse</h1>
          <p class="...">Gemini 3.8 Flash is Google's new coding-and-agent workhorse: ...</p>      <!-- 描述 -->
        </header>

        <!-- 封面图：目前在 hero 文字下方、正文之前，且仅占左列宽度 -->
        <div class="mt-10 overflow-hidden rounded-2xl border border-black/10 bg-white/20 shadow-sm">
          <img src="https://d1z7vojvoo4ca1.cloudfront.net/1788429571027-26680f28-3ebd-4c33-8fb3-1e4fab795481.png"
               alt="Gemini 3.8 Flash — Google's New Coding &amp; Agent Workhorse"
               class="aspect-[16/9] w-full object-cover"/>
        </div>

        <!-- TL;DR 与正文：连续渲染在 .docs 中，TL;DR 是 markdown 第一个 H2（id="tldr"） -->
        <div class="mt-10">
          <div class="docs ..."><div class="markdown-body">
            <h2 id="tldr" data-level="2">TL;DR</h2>
            <ul>…（5 条要点）…</ul>
            <h2 id="1-why-gemini-38-flash-matters-right-now" data-level="2">1. Why …</h2>
            …
          </div></div>
        </div>

        <!-- 订阅块（Get automation tips）在 article 内部末尾 -->
        <div class="mt-16 rounded-2xl border …">…Subscribe…</div>
      </article>

      <!-- 右侧 TOC：hidden lg:block，吸顶从页面顶部即与 hero 并排开始 -->
      <aside class="hidden lg:block">
        <div class="sticky top-24 rounded-2xl border border-black/10 bg-white/25 p-6">
          <h2 class="font-serif …">Table of Contents</h2>
          <div class="mt-4"><nav aria-label="Table of contents"><ul class="space-y-2">
            <li><a href="#tldr">TL;DR</a></li>
            <li><a href="#1-why-gemini-38-flash-matters-right-now">1. Why Gemini 3.8 Flash Matters Right Now</a></li>
            …（含 FAQ 子项，缩进 pl-3）…
          </ul></nav></div>
        </div>
      </aside>
    </div>
  </div>
</section>
```

要点：页面容器限宽 `max-w-[1440px]`；整页从 hero 起即为 `1fr + 360px` 两栏；**hero 文字与封面图上下堆叠在左列**；TL;DR 混排在正文流顶部（同处左列）；TOC 吸顶卡片与 hero 从同一起点并排存在；TOC 卡片内**无任何分享按钮**。

### 2.2 同区域在其他文章页的表现（抽验，2026-09-03）

对 `/blog/grok-4-6` 抽验：同样命中 `lg:grid-cols-[minmax(0,1fr)_360px]`、`sticky` TOC（"Table of Contents"）、`aspect-[16/9]` 封面图、"Back to Blog"。即：**所有文章页共用同一 post 模板**，一处模板改动即全站生效。grok 页 tag pill 文本为 "Deepseek"（本页为 "Label"），说明 pill 文本由文章元数据驱动、非硬编码——改版时沿用现有渲染逻辑即可。

### 2.3 期望版式（本任务改造目标，2026-09-03 定稿）

目标版式是一套常见于主流内容站点的「长文阅读布局」，按视觉层次拆为三个纵向区段：

- **全宽 hero band**：横贯页面容器宽度、带浅背景与底部细分隔线的头部区（不参与下方 TOC 侧栏网格）。band 内部为两栏 `grid lg:grid-cols-2`：左栏 = tag pill + H1 + 描述（日期/阅读时长行）；右栏 = 封面图，圆角卡片、`aspect-[1200/630]`（或与图片资源适配的等宽比）、`object-cover`、`loading="eager"`。
- **TL;DR 全宽引导区段**：紧随 hero band 之下、同样横贯容器宽度，承载 `h2#tldr` 标题与要点列表。
- **正文区网格（TOC 侧栏 + 正文）**：`lg:grid-cols-12` 或 `[minmax(0,1fr)_360px]` 两栏——左侧窄栏为 **sticky 的 TOC（含分享按钮组）**，右侧为正文阅读列（`max-w` 阅读宽度）。该网格的视觉起点即正文起点（TL;DR 区段之后），页首与 hero/TL;DR 区域不再出现并排 TOC。

版式层级示意即 §5.3；分享按钮交互规格见 §5.2-6 与 §5.4 参考实现。

---

## 3. 根因分析

- **现状版式**把「hero 文字 → 封面图 → TL;DR+正文」整体塞进两栏网格的左列，同时右侧 TOC 从页面顶部就吸顶并排：这导致 (a) hero 无法做「文左图右」的宽幅展示（图片只能窄列平铺或下移堆叠）；(b) hero 与 TL;DR 事实上只有 `1fr - 360px` 的可用宽度，视觉上「不横贯全页」；(c) TOC 的视觉起点落在页首与 hero 并列，而非随正文出现。
- 目标版式（§2.3）将页面在模板层拆为三个纵向区段：**全宽 hero band → TL;DR 全宽引导区 → 正文区网格（TOC 侧栏 + 正文）**，TL;DR 需要跨区呈现为全宽引导块；TOC 从正文区起点开始吸顶；分享入口放在 TOC 卡片内。该改造只需调整**模板结构与样式**，各字段来源（title/description/category→pill、日期/阅读时长、封面图、正文 md、TOC 锚点）均可复用现有渲染链路，因此可以做到零内容改动。
- 该模板同时承载「返回链接/面包屑」任务（见关联任务 `floatboat-fix-blog-breadcrumb-nav.md`）：本次 hero 重构后，返回链接/面包屑行应保持在 hero band 顶部原位置（详见 §5.5 协同规则），两任务互不破坏。

---

## 4. 影响范围

| 页面 | 受影响位置 | 处理 |
|------|-----------|------|
| `/blog/{slug}`（全部已发布文章页） | 文章页模板：hero 区、封面图容器、TL;DR 容器、TOC 侧栏容器 | 模板级重构（本任务主范围） |
| `/blog`（Blog 列表页）、首页、产品页 | 无文章 hero/TOC 组件 | 不涉及 |

**组件性质**：文章页共用模板的单点组件（基于 2.2 抽验一致性与 Next.js 页面产物推断）——请对方 agent 定位到文章页模板组件后一次改全；**无需也不得改动任何文章 `.md` 源文件**。

---

## 5. 修复要求

### 5.1 修复位置

定位文章页渲染模板（blog post / article page template，Next.js App Router 下形如 `app/[locale]/(landing)/blog/[slug]/page.*` 及其引用的页面组件）。源码内搜索关键词：**"Table of Contents"**、**`grid-cols-[minmax(0,1fr)_360px]`**、**`aspect-[16/9]`**、**"Back to Blog"**。页面上这些容器/类名均出自同一模板。

### 5.2 规则（必须满足）

1. **零内容改动**：不修改任何文章 `.md`/frontmatter/正文/图片资源；title、description、pill 文本、日期/阅读时长、封面图 URL、正文 HTML、FAQ 锚点、TOC 条目的**取值逻辑全部沿用现有渲染**，仅调整结构与样式。
2. **Hero 全宽双栏（桌面 ≥lg）**：hero 区脱离当前 `1fr_360px` 网格，成为横贯页面容器的全宽 band；band 内 `grid lg:grid-cols-2`（或等价两栏）：
   - 左栏：tag pill（原样）→ 日期/阅读时长行 → H1 → 描述；
   - 右栏：封面图（原 `cloudfront` 图 URL 不变；圆角卡片；建议纵横比沿用现有资源原比例或采用 `aspect-[1200/630]` 目标比，`object-cover`）。
3. **移动端（<lg）堆叠**：hero 为单栏，顺序为 pill → 日期/时长 → H1 → 描述 → 封面图（图在文字下方，保持当前 DOM 顺序即可）。
4. **TL;DR 全宽**：将正文中 `h2#tldr` 及其要点列表渲染为 hero 下方的**全宽引导区段**（横贯页面容器宽度，不进入右侧 TOC 栏窄列）；TL;DR 之后才进入「TOC 栏 + 正文」网格。实现上可在渲染层将 `#tldr` 标题与内容提取/投影到该区段，正文网格从第一个正文 H2（如 `1. …`）开始——**不要在 md 源里移动 TL;DR**。
5. **TOC 从正文开始 + 吸顶**：正文区网格（建议 `lg:grid-cols-[minmax(0,1fr)_360px]` 或 12 栏网格）起点对齐正文（TL;DR 全宽区段之后）；TOC 卡放在网格侧栏并 `sticky`（沿用现有 `top-24` 级吸顶）；吸顶后 TOC 不与 hero/TL;DR 视觉重叠（用网格自身起点保证，不依赖额外 hack）。
6. **TOC 内加分享按钮**：在 TOC 卡片内（标题下方或卡片底部）新增「分享到社媒」按钮组，目标平台建议：X / LinkedIn / Facebook / 复制链接；分享 URL = 当前页 canonical（`https://floatboat.ai/blog/{slug}`），文案 = 页面标题；点击新开窗口或写剪贴板。建议做成紧凑的小图标按钮行（含平台品牌色 hover），置于卡片内分隔线下方或标题行右侧。移动端 TOC 隐藏逻辑保持现状（如现状移动端无 TOC，则分享按钮可同步不显示，或另按 §5.5 可选项处理）。
7. **无重复渲染**：封面图只出现在 hero 右栏；正文与 TL;DR 不在页面重复出现；TOC 锚点 `#tldr`、`#faq` 等仍能正确跳转到对应区块。
8. **功能无回归**：面包屑/返回链接行、正文阅读体验、订阅块（Get automation tips）、`article` 语义标签、FAQ 折叠/锚点等保持可用。
9. **全站生效**：一处模板改动覆盖所有文章页。

### 5.3 修复后的期望输出（页面纵向结构与桌面 hero 示意）

`/blog/gemini-3-8-flash` 修复后版式（桌面，示意）：

```
┌──────────────────────────────────────────────────────────────┐
│ Back to Blog / 面包屑行（保持原位置，勿删勿移）                  │
├───────────────────────────────┬──────────────────────────────┤
│  [Research]                   │                              │
│  Sep 3, 2026 · 21 min read    │        封面图（原图 URL）      │
│  # Gemini 3.8 Flash — …       │   （圆角卡片，object-cover）    │
│  描述 paragraph                │                              │
├───────────────────────────────┴──────────────────────────────┤
│  TL;DR 全宽引导区段（h2#tldr + 要点列表，横贯容器宽度）          │
├───────────────────────────────┬──────────────────────────────┤
│  Table of Contents（sticky）   │  1. Why Gemini 3.8 Flash …    │
│   ────────────────            │  2. …                        │
│  分享： [X][in][f][🔗]         │  3. …                        │
│   (TOC 卡片内新增分享按钮组)     │  … 正文 …                    │
│   #tldr / #1-… / #faq …       │  FAQ …                       │
├───────────────────────────────┴──────────────────────────────┤
│  订阅块（Get automation tips）…                                │
└──────────────────────────────────────────────────────────────┘
```

（TL;DR 全宽区段与「TOC+正文」网格的相对顺序、是否给 hero/TL;DR 加深浅分隔背景，由对方 agent 按站点现有视觉风格定；核心约束 = 层级与 §5.2 各条。）

### 5.4 代码级参考（示意，按项目实际实现调整）

以组件结构示意（组件命名/拆分按项目实际实现调整）：

```tsx
// —— hero：全宽 band，内部两栏（左文右图）——
<header className="bg-surface border-b border-border/50">       {/* 全宽 band */}
  <div className="container mx-auto px-4">
    <div className="grid grid-cols-1 lg:grid-cols-2 items-center gap-10 lg:gap-14">
      <div>
        {label && <span className="tag-pill">{label}</span>}   {/* pill 沿用现有字段 */}
        <div className="meta-row">{date} · {readTime}</div>
        <h1>{title}</h1>
        <p>{description}</p>
      </div>
      <div className="rounded-xl overflow-hidden border">
        <img src={coverImageUrl} alt={title} className="aspect-[1200/630] w-full object-cover" />
      </div>
    </div>
  </div>
</header>

{/* —— TL;DR 全宽引导区（渲染层将 markdown 首个 #tldr 区块投影至此）—— */}
<section className="container mx-auto px-4 py-…">
  <TldrBlock html={tldrHtml} />     {/* 含 h2#tldr 标题与要点，保持 id 供锚点跳转 */}
</section>

{/* —— 正文区：TOC 侧栏 + 正文 —— */}
<main className="container mx-auto px-4">
  <div className="grid lg:grid-cols-[minmax(0,1fr)_360px] gap-10">
    <div className="docs">{bodyHtml}</div>   {/* 从 TL;DR 之后的第一个 H2 开始 */}
    <aside>
      <div className="sticky top-24 …">
        <TocCard items={tocItems} />          {/* TOC 列表逻辑沿用现状 */}
        <ShareOnSocial url={canonicalUrl} title={title} />   {/* 新增：X/LinkedIn/Facebook/复制 */}
      </div>
    </aside>
  </div>
</main>
```

分享交互实现要点（各平台打开方式）：X / LinkedIn / Facebook 用各平台 Web Intent URL（`https://twitter.com/intent/tweet`、`https://www.linkedin.com/sharing/share-offsite/?url=`、`https://www.facebook.com/sharer/sharer.php?u=`）新开窗口，复制链接用 `navigator.clipboard.writeText` + 成功反馈；拼 URL 时对查询参数做 `encodeURIComponent`。落成 Floatboat 自己的样式与实现即可。

### 5.5 协同与可选项

- **与面包屑任务协同**：`floatboat-fix-blog-breadcrumb-nav.md`（另单提交）负责把 "Back to Blog" 替换为面包屑。两任务改动同一模板不同区块：本任务要求 hero band 顶部**保留返回链接/面包屑行于原相对位置**（最上），不删除、不叠加。两单可顺序执行，无冲突。
- **可选项**（不做不影响主验收）：若希望移动端也有分享入口，可在文章正文末尾或订阅块上方补一组分享按钮；列表页无需处理。

---

## 6. 验收标准

- [ ] 源码/构建产物中：文章页模板已无「hero 文字与封面图在左列上下堆叠、右列 TOC 从页首并排」的旧结构（以浏览器 DOM 复核为准）
- [ ] 桌面（≥1024px）任一文章页 hero 为两栏：左 = tag pill + 日期/阅读时长 + H1 + 描述；右 = 封面图（图 URL 与改版前一致，圆角、object-cover）
- [ ] hero 与 TL;DR 均横贯页面容器宽度（不位于右侧 360px TOC 窄栏内）
- [ ] 封面图不再出现在正文顶部/hero 文字下方等原位置（页面仅一处封面图）
- [ ] TOC 卡片视觉起点与正文（TL;DR 之后）起点对齐；滚动时吸顶正常且不与 hero 重叠；移动端显示行为与改版前一致
- [ ] TOC 卡片内可见分享按钮组（X / LinkedIn / Facebook / 复制链接 ≥3 项），点击分享 URL 为 `https://floatboat.ai/blog/{slug}`、文案为页面标题
- [ ] 抽查 ≥4 篇不同类型文章（如 `/blog/gemini-3-8-flash`、`/blog/grok-4-6`、`/blog/gemini-3-7-flash`、`/blog/glm-5-3`）版式一致且生效
- [ ] 正文所有 H2/H3、FAQ 锚点可跳转；文章内容与改版前逐字一致（无内容改动）；订阅块、面包屑/返回链接、页脚等无回归
- [ ] 移动端（<1024px）hero 单栏顺序正确、无横向溢出、图片正常显示

---

*本任务单由外部 SEO/协作方提交，供 Floatboat 方 agent 直接执行。*
