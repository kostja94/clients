# Vofy Style 类 Apps — 缺口分析与页面模板

> **适用品类**：Style（风格化）——将照片转化为特定艺术风格的完整视觉语言。覆盖 Ghibli、Impressionist、Cyberpunk、3D Clay、Ink Wash、Oil Painting、Colored Pencil 等。
>
> 关联：[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Filter 类指南](./vofy-filter-apps-guide-zh.md) · [Effect 类指南](./vofy-effect-apps-guide-zh.md) · [Edit 类指南](./vofy-edit-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md)

**创建日期**：2026-05-11 · **更新**：2026-05-12（合并缺口分析与页面模板）

---

# 第一部分：缺口分析

## 一、Style 品类定义

Style 类 App 的核心动作是「变成某种风格」——将照片转化为特定艺术流派的完整视觉语言，而非叠加单层效果或套用色调预设。用户心智为审美方向型搜索。

| 维度 | Style | Filter | Effect | Edit |
|------|-------|--------|--------|------|
| **核心动作** | 「变成某种风格」 | 「套一个整体色调」 | 「加一个视觉效果」 | 「改这张图的某个部分」 |
| **用户心智** | 审美方向 | 一键快餐 | 单次操作 | 实用修改 |
| **典型搜索** | `Ghibli style AI`, `turn photo into oil painting` | `vintage filter online`, `film grain preset` | `add bokeh to photo`, `glitch effect online` | `remove background`, `expand image` |

## 二、Vofy 现有 Style Apps

Vofy 85 个 Apps 中，Style 类约 5 个（5.9%）：

- `ghibli-style`, `ai-style-transfer`, `digital-art-styles`, `family-guy-art-style`, `rick-and-morty-art-style`

另有部分 Generator 类 App 本质上是风格化输出，可向 Style 靠拢：`random-cartoon`, `ai-pokemon`, `fantasy-art`, `superhero`, `mandala`, `stained-glass`, `ai-pin-up` 等约 15 个。

## 三、竞品对标

### 3.1 Picsart AI Art Effects（10 个，2024–2026）

| # | Effect | 风格描述 | 热度 |
|---|--------|---------|------|
| 1 | **Through the Water** | 水下电影感，波纹光线 | Top 1 |
| 2 | **Autumn Heart** | 秋日柔焦人像，金叶飘落 | Top 2 |
| 3 | **Colored Pencil Portrait** | 彩铅手绘质感人像 | Top 3 |
| 4 | **Art Nouveau Dream** | 新艺术运动插画，金线花卉 | Top 4 |
| 5 | **Dollar Engraving** | 钞票雕刻风格人像 | Top 5 |
| 6 | **Impressionist Breeze** | 印象派松散笔触，阳光色调 | Top 6 |
| 7 | **Notebook Doodle** | 笔记本随手涂鸦风 | Top 7 |
| 8 | **Vintage Watercolor Collage** | 水彩 + 拼贴 + 花卉 | Top 8 |
| 9 | **Neoclassical Portrait** | 博物馆级欧式古典人像 | Top 9 |
| 10 | **Anime Style** | 动画风格，粗轮廓线 | Top 10 |

### 3.2 Canva 相关功能

| 功能 | 说明 |
|------|------|
| **Magic Morph** | 对文字/形状施加图案与纹理变换（风格化） |
| **Magic Media** | 文本 → AI 图像生成 |

### 3.3 2026 社交媒体趋势（Style 相关）

| 趋势 | 热度 | 描述 |
|------|------|------|
| **Glitch Art** | 🔥🔥 | 故障艺术持续热门，约 38.8K 用户 |
| **Anime Portrait（深度版）** | 🔥🔥 | 2026 版 AI 动漫人像保留真实面部特征 |
| **3D Clay / Claymation** | 🔥 | 粘土动画质感 |
| **Ink / Su Mi-e** | 🔥 | 水墨风格——极简黑白毛笔笔触（Midjourney Top 10） |
| **Pencil Sketch 多子类** | 🔥 | 铅笔素描、彩铅、炭笔、粉彩——各有独立搜索需求 |
| **Vintage Retro（1970s/80s/90s）** | 🔥 | 分年代复古风格 |
| **PS2 / Retro Gaming** | 🔥🔥 | 怀旧 PlayStation 2 低多边形美学，约 42.6K 用户 |

## 四、Style 缺口矩阵

以下为 Style 类需填补的缺口（从 Picsart 66 API + AI Art 10 + 2026 趋势中提取）：

### 4.1 完全缺失的 Style

| 序号 | 缺口功能 | Picsart 对标 | 搜索量估算 | 社交热度 |
|------|---------|-------------|-----------|---------|
| 1 | **Glitch / 故障艺术** | cyber1/2, glitch | 30K–60K/月 | 🔥🔥 |
| 2 | **Impressionist / 印象派** | Impressionist Breeze（AI Top 6） | 15K–35K/月 | 🔥 |
| 3 | **Colored Pencil / 彩铅** | Colored Pencil Portrait（AI Top 3） | 10K–25K/月 | 🔥 |
| 4 | **Cyberpunk / 赛博朋克** | cyber1/2 | 10K–25K/月 | 🔥 |
| 5 | **Neon / 霓虹** | Neopop, Neon Noir | 8K–20K/月 | 🔥 |
| 6 | **Art Nouveau / 新艺术** | Art Nouveau Dream（AI Top 4） | 5K–12K/月 | — |
| 7 | **3D Clay / 粘土化** | —（Face Many AI 有） | 8K–20K/月 | 🔥 |
| 8 | **Ink / 水墨** | —（Midjourney Top 10） | 8K–18K/月 | 🔥 |
| 9 | **Notebook Doodle / 涂鸦** | Notebook Doodle（AI Top 7） | 5K–12K/月 | — |
| 10 | **Dollar Engraving / 钞票雕刻** | Dollar Engraving（AI Top 5） | 3K–8K/月 | — |
| 11 | **Pixel Art / 8-Bit 像素艺术** | —（独立工具有） | 10K–25K/月 | — |
| 12 | **Charcoal / 炭笔画** | — | 5K–10K/月 | — |
| 13 | **Comic Book / 美漫风** | popart 近似 | 8K–18K/月 | — |
| 14 | **Digital Collage / 数字拼贴** | Vintage Watercolor Collage 近似 | 5K–12K/月 | — |

### 4.2 已有但需深化的 Style

| 缺口 | Vofy 现状 | 深化方向 | 搜索量估算 |
|------|----------|---------|-----------|
| **Oil Painting / 油画** | ⚠ 仅有 renaissance-portrait 近似 | 扩展为油画系（古典/厚涂/刮刀） | 10K–25K/月 |
| **Watercolor / 水彩** | ⚠ 仅有 photo-to-watercolor 基础款 | 扩展（淡彩/浓彩/水墨融合） | 10K–25K/月 |
| **Anime Deepen / 动漫深化** | ⚠ 仅有 90s-anime-filter, chibi-maker | 扩展子风格（赛璐璐/新海诚/复古 OVA） | 15K–40K/月 |
| **Doodle / 手绘线稿** | ⚠ photo-to-line-drawing 基础款 | 扩展（圆珠笔/马克笔/便签风） | 8K–18K/月 |

## 五、优先级与路线图

### 🔴 P0 — AI 强项 × 大流量 × 竞品已验证

| 新增 App（建议 slug） | AI 优势 | 搜索量估算 | 竞品信号 | 社交热度 |
|----------------------|---------|-----------|---------|---------|
| `glitch-effect` | ⭐⭐⭐⭐⭐ | 30K–60K/月 | Picsart cyber1/2 + glitch | 🔥🔥 |
| `impressionist-style` | ⭐⭐⭐⭐⭐ | 15K–35K/月 | Picsart AI Top 6 | 🔥 |
| `colored-pencil-portrait` | ⭐⭐⭐⭐⭐ | 10K–25K/月 | Picsart AI Top 3 | 🔥 |
| `cyberpunk-style` | ⭐⭐⭐⭐⭐ | 10K–25K/月 | Picsart cyber1/2 | 🔥 |

### 🟡 P1 — AI 优势 × 中高流量 × 差异化

| 新增 App | AI 优势 | 搜索量估算 | 竞品信号 |
|---------|---------|-----------|---------|
| `neon-style` | ⭐⭐⭐⭐⭐ | 8K–20K/月 | Picsart Neopop + Neon Noir |
| `oil-painting-style` | ⭐⭐⭐⭐⭐ | 10K–25K/月 | Picsart AI Top 9 |
| `watercolor-art-style` | ⭐⭐⭐⭐⭐ | 10K–25K/月 | Picsart AI Top 8 + water1/2 |
| `anime-art-style` | ⭐⭐⭐⭐⭐ | 15K–40K/月 | Picsart AI Top 10 |
| `art-nouveau-style` | ⭐⭐⭐⭐⭐ | 5K–12K/月 | Picsart AI Top 4 |
| `3d-clay-style` | ⭐⭐⭐⭐⭐ | 8K–20K/月 | Face Many AI |
| `ink-wash-style` | ⭐⭐⭐⭐⭐ | 8K–18K/月 | Midjourney Top 10 |
| `pixel-art-style` | ⭐⭐⭐⭐⭐ | 10K–25K/月 | 独立工具有 |

### 🟢 P2 — 利基市场

| 新增 App | AI 优势 | 搜索量估算 | 备注 |
|---------|---------|-----------|------|
| `notebook-doodle-style` | ⭐⭐⭐⭐⭐ | 5K–12K/月 | Picsart AI Top 7 |
| `charcoal-sketch` | ⭐⭐⭐⭐ | 5K–10K/月 | 素描变体，可打包 |
| `dollar-engraving-style` | ⭐⭐⭐⭐ | 3K–8K/月 | Picsart AI Top 5，独特利基 |
| `through-the-water-style` | ⭐⭐⭐⭐ | 3K–8K/月 | Picsart AI Top 1 |
| `autumn-heart-style` | ⭐⭐⭐⭐ | 3K–8K/月 | Picsart AI Top 2，季节性强 |

### 推荐实施路线

| Phase | 时间 | App 数量 | 内容 |
|-------|------|---------|------|
| **Phase 1** | 本月 | 4 个 P0 | Glitch、Impressionist、Colored Pencil、Cyberpunk |
| **Phase 2** | 下月 | 8 个 P1 | Neon、Oil Painting、Watercolor、Anime、Art Nouveau、3D Clay、Ink Wash、Pixel Art |
| **Phase 3** | 后续 | 5 个 P2 | Notebook Doodle、Charcoal、Dollar Engraving 等 |

## 六、AI 原生优势：为何不需要照搬 Picsart

Picsart 的 66 个 API effects 大部分是传统图像处理算法。Vofy 作为 AI 模型聚合器，实现路径完全不同：

| 维度 | Picsart 路径 | Vofy 路径 | Vofy 优势 |
|------|-------------|----------|----------|
| **Sketch 素描** | 边缘检测 + 阈值 | AI style transfer | 可指定笔触、纸张纹理、阴影风格 |
| **Cyberpunk** | 固定 LUT 调色 | AI 重绘 | 可生成霓虹灯牌、全息投影等新画面元素 |
| **Watercolor** | 固定风格迁移模型 | 多模型 prompt | 可组合风格（水彩 + 水墨 + 拼贴） |
| **Oil Painting** | 固定滤镜 | 多模型 prompt | 可指定笔触厚度、刮刀纹理、古典/现代流派 |

**核心策略**：Vofy 应用 Style Preset / Prompt 模板覆盖 AI 原生优势区，而非为每个算法 effect 建独立工具页。

## 七、Blog 内容联动

新增的每个 Style App 应配套一篇 HowTo blog：

- `how-to-create-glitch-art-effect` → 故障风格教程
- `impressionist-style-ai-guide` → 印象派 AI 风格教程
- `colored-pencil-portrait-ai-tutorial` → 彩铅人像教程
- `cyberpunk-ai-art-style-guide` → 赛博朋克风格教程
- `how-to-make-3d-clay-art-ai` → 粘土化教程
- `ink-wash-style-ai-guide` → 水墨风格教程

---

# 第二部分：页面模板

## 一、页面线框图（Style 类专用）

```
┌─────────────────────────────────────────────────────────────┐
│  BREADCRUMB                                                  │
│  Apps > Style > [Style Name] Style                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  HERO                                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Style]  badge                                        │   │
│  │                                                       │   │
│  │  H1: AI [Style Name] Style Generator —                │   │
│  │      Turn Your Photo into [Style Name] Art             │   │
│  │                                                       │   │
│  │  Subtitle: 1-2 句，第一句描述风格感受（诗意），        │   │
│  │           第二句说明技术能力 + 含 1-2 个变体关键词      │   │
│  │                                                       │   │
│  │  [Upload an image]  CTA                                │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  TOOL WIDGET                                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Upload an image  [JPG, PNG, WebP, GIF]               │   │
│  │                                                       │   │
│  │  Style preset  [dropdown: Select a style preset]      │   │
│  │  ┌──────────────┬──────────────┬──────────────┬─────┐│   │
│  │  │ Preset 1     │ Preset 2     │ Preset 3     │Prst4││   │
│  │  │ (具名+缩略图) │ (具名+缩略图) │ (具名+缩略图) │ ... ││   │
│  │  └──────────────┴──────────────┴──────────────┴─────┘│   │
│  │                                                       │   │
│  │  Settings: [Model ▼] · [Aspect ▼] · [Resolution ▼]   │   │
│  │                                                       │   │
│  │  [Generate [Style Name] Art]  CTA                      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  EXAMPLE GALLERY                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Example]  [Latest]  [History]   tabs                │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │ Before  │ │ Before  │ │ Before  │ │ Before  │   │   │
│  │  │  After  │ │  After  │ │  After  │ │  After  │   │   │
│  │  │(original│ │         │ │         │ │         │   │   │
│  │  │ → styled│ │         │ │         │ │         │   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 01 — 教育模块                                       │
│  H2: What is [Style Name] Style, Exactly?                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  2-3 段正文：                                          │   │
│  │  段 1 — 风格定义（1 句） + 艺术史/文化起源（1 句）      │   │
│  │  段 2 — 典型视觉特征概述（2-3 句）                      │   │
│  │  段 3 — Vofy AI 如何重现这种风格（技术层次, 1-2 句）    │   │
│  │  [Available on all Vofy plans]  badge                  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 02 — 风格特征拆解（4 张视觉卡片）                    │
│  H2: What Makes a Photo Look [Style Name].                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│   │
│  │  │ 🎨       │ │ ☀️       │ │ 🖼️       │ │ ✏️       ││   │
│  │  │ Palette  │ │ Light    │ │ Tone     │ │ Texture  ││   │
│  │  │ 配色特征  │ │ 光影特征  │ │ 色调特征  │ │ 笔触/质感 ││   │
│  │  │          │ │          │ │          │ │          ││   │
│  │  │ [具体描述 │ │ [具体描述 │ │ [具体描述 │ │ [具体描述 ││   │
│  │  │ 该风格的 │ │ 该风格的 │ │ 该风格的 │ │ 该风格的 ││   │
│  │  │ 标志性   │ │ 标志性   │ │ 标志性   │ │ 标志性   ││   │
│  │  │ 配色方案]│ │ 光线处理]│ │ 色调范围]│ │ 笔触质感]││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 03 — 使用场景                                       │
│  H2: When to Use [Style Name] Style.                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│   │
│  │  │ Portraits│ │Landscapes│ │  Social  │ │  Prints  ││   │
│  │  │ 人像/头像 │ │ 旅行/风景 │ │ 社交媒体 │ │ 印刷/周边 ││   │
│  │  │          │ │          │ │          │ │          ││   │
│  │  │ [2-3句   │ │ [2-3句   │ │ [2-3句   │ │ [2-3句   ││   │
│  │  │ 场景说明]│ │ 场景说明]│ │ 场景说明]│ │ 场景说明]││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 04 — HowTo 步骤                                    │
│  H2: How to Turn Your Photo into [Style Name] Art            │
│      in Three Steps.                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  01 — Upload Your Photo                               │   │
│  │  [描述：支持格式、建议主体清晰]                         │   │
│  │  Tip: [建议使用何种类型的照片效果最佳]                  │   │
│  │                                                       │   │
│  │  02 — Pick a [Style Name] Preset                      │   │
│  │  [描述：浏览预设、子风格变体、预览效果]                  │   │
│  │  Tip: [推荐哪个预设适合哪种照片类型]                    │   │
│  │                                                       │   │
│  │  03 — Generate & Download                             │   │
│  │  [描述：点击生成、查看结果、Credits 消耗一句说明]        │   │
│  │  Tip: [可继续在 Studio 中微调或叠加其他效果]            │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  SOCIAL PROOF                                                │
│  H2: What Creators Say                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────────────────┐ ┌──────────────────────┐    │   │
│  │  │ "[风格感受引文]"      │ │ "[风格感受引文]"      │    │   │
│  │  │  — Name, Role        │ │  — Name, Role        │    │   │
│  │  └──────────────────────┘ └──────────────────────┘    │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  RELATED APPS                                                │
│  H2: Also in the Studio                                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐             │   │
│  │  │ 同品类   │ │ 相邻品类  │ │ 热门通用  │             │   │
│  │  │ Style App│ │ Filter/  │ │ Popular  │             │   │
│  │  │          │ │ Effect   │ │ App      │             │   │
│  │  └──────────┘ └──────────┘ └──────────┘             │   │
│  │  [See all apps →]                                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  FAQ（使用 `<details>/<summary>` HTML，确保 Bing 可抓取）     │
│  H2: Questions, Answered.                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Q1: [版权/风格归属——如 "Is this official [Style]?"]  │   │
│  │  A1: [说明 AI 生成 vs 原作关系 + 使用许可]             │   │
│  │  ─────────────────────────────────────────            │   │
│  │  Q2: 适用照片类型（什么照片效果好）                    │   │
│  │  Q3: 输出格式与分辨率                                  │   │
│  │  Q4: 商用许可范围                                      │   │
│  │  Q5: 与竞品/传统滤镜的区别                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CLOSING CTA                                                 │
│  H2: Reimagine Your Photos with [Style Name] Art.            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Subtitle: [简短行动描述，呼应 Hero 的情感钩子]         │   │
│  │  [Turn Your Photo into [Style Name] Art]  CTA          │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、H1 标题公式

**公式**：`AI [Style Name] Style Generator — Turn Your Photo into [Style Name] Art`

**设计原则**：
- 破折号前 = 搜索引擎主词（匹配 "ai [style] style" / "[style] style generator"）
- 破折号后 = 情绪钩子 + 长尾关键词（匹配 "turn photo into [style]" / "[style] art"）
- Title Tag 取破折号前 + ` | Vofy`（50-60 字符），H1 取完整双段式（50-70 字符）

**填充示例**：

| App | H1 |
|-----|-----|
| Ghibli Style | `AI Ghibli Style Generator — Turn Your Photo into Studio Ghibli Art` |
| Impressionist | `AI Impressionist Style Generator — Turn Your Photo into a Monet Painting` |
| Cyberpunk | `AI Cyberpunk Style Generator — Turn Your Photo into a Neon-Lit Future` |
| 3D Clay | `AI 3D Clay Style Generator — Turn Your Photo into Stop-Motion Clay Art` |
| Ink Wash | `AI Ink Wash Style Generator — Turn Your Photo into Sumi-e Brush Painting` |
| Colored Pencil | `AI Colored Pencil Style Generator — Turn Your Photo into Hand-Drawn Portrait Art` |

---

## 三、各区块内容规范

### 3.1 Breadcrumb

```
Apps > Style > [Style Name] Style
```

### 3.2 Hero

| 元素 | 规范 |
|------|------|
| **Badge** | `Style` |
| **H1** | 按 §二公式，必须含主关键词 `AI [Style Name] Style Generator` |
| **Subtitle** | 段 1：风格感受（诗意，1 句）。段 2：Vofy AI 能做什么 + 含 1-2 个变体关键词 |
| **CTA** | `Upload an image` 或 `Turn your photo into [Style] art` |
| **关键词密度** | H1 含 "AI" + "[style]" + "style generator"；subtitle 含 "[style] art" / "[style] effect" 等变体 |

### 3.3 Tool Widget

| 元素 | 规范 |
|------|------|
| **上传区域** | JPG, PNG, WebP, GIF — 建议主体清晰 |
| **Selector** | `Style preset` dropdown — 3-5 个具名预设，每项有风格缩略图 |
| **预设命名** | 使用风格子变体名（如 Impressionist 的 "Monet Garden"、"Van Gogh Starry"、"Renoir Portrait"） |
| **Settings 行** | Model · Aspect Ratio · Resolution（默认推荐模型 + Auto） |
| **Generate CTA** | `Generate [Style Name] Art` |

### 3.4 Example Gallery

- 3 个 Tab：Example / Latest / History
- 4 列 Before/After 对比网格
- 前 2 列：精选高质量示例（人工挑选）
- 后 2 列：最近生成 / 历史记录
- 每列 Before 标注 `Original` / After 标注 `[Style Name] Style`

### 3.5 Chapter 01 — 教育

| 元素 | 规范 |
|------|------|
| **H2** | `What is [Style Name] Style, Exactly?` |
| **段 1** | 风格定义（1 句）+ 艺术史/文化起源（1 句） |
| **段 2** | 典型视觉特征概述——自然融入 Ch.02 四个维度的关键词（2-3 句） |
| **段 3** | Vofy AI 如何重现——风格迁移模型 + prompt 引导的实现层次（1-2 句） |
| **Badge** | `Available on all Vofy plans`（若适用） |
| **关键词** | 主词出现 2-3 次，变体（如 "[style] art" / "[style] painting"）1-2 次 |

### 3.6 Chapter 02 — 风格特征拆解

**H2**：`What Makes a Photo Look [Style Name].`

**4 张卡片**（固定维度，不可增减）：

| 卡片 | 标题 | 内容要求 |
|------|------|---------|
| **Color Palette**（配色） | 标志性配色方案的名称 | 2-3 句描述该风格的标志性色彩组合（如 "soft pastel blues and warm amber highlights"），可提一个代表色号 |
| **Lighting**（光影） | 标志性光线处理的名称 | 2-3 句描述该风格如何运用光线（柔和/戏剧化/平面/逆光），以及光的色温倾向 |
| **Tonal Range**（色调） | 标志性色调范围的名称 | 2-3 句描述整体色调倾向（明亮高调/暗沉低调/中间调丰富），以及对比度特征 |
| **Texture & Brushwork**（笔触/质感） | 标志性质感或笔触的名称 | 2-3 句描述画面质感特征（光滑/粗粝/可见笔触/水彩渗透/油画厚度），以及线条风格 |

### 3.7 Chapter 03 — 使用场景

**H2**：`When to Use [Style Name] Style.`

**4 张场景卡片**（Style 类侧重）：

| 场景 | 适用条件 | 内容示例 |
|------|---------|---------|
| **Portraits & Avatars** | 单人/双人肖像，面部清晰 | "Turn your selfies into [style] portraits that look like they belong in a gallery." |
| **Landscapes & Travel** | 风景、建筑、城市 | "Reimagine your travel photos through the lens of [style] — every skyline becomes a painting." |
| **Social Media Content** | Instagram/TikTok/Pinterest | "Stand out in feeds flooded with generic filters. [Style] art stops the scroll." |
| **Prints & Merchandise** | 海报、明信片、T 恤 | "High enough resolution for prints, posters, and gifts — your photo, reimagined as [style] wall art." |

### 3.8 Chapter 04 — HowTo

**H2**：`How to Turn Your Photo into [Style Name] Art in Three Steps.`

| 步骤 | 标题 | 正文要求 | Tip |
|------|------|---------|-----|
| **01** | `Upload Your Photo` | 支持 JPG/PNG/WebP；建议主体清晰、光线充足；最大文件尺寸（按产品实填） | "For best results, use photos with a clear subject against an uncluttered background." |
| **02** | `Pick a [Style Name] Preset` | 从预设中选择风格子变体；每个预设产生微妙不同的配色与笔触效果 | "Try [Preset A] for [portraits/landscapes]，[Preset B] for [different subject] — each preset interprets the style slightly differently." |
| **03** | `Generate & Download` | 点击生成；AI 处理时间一句说明；下载选项（PNG/JPG）；Credits 一句说明 | "After generating, you can continue editing in the Studio — add filters, adjust lighting, or layer effects on top of your [style] art." |

> JSON-LD HowTo schema 参考 [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) 范例 A。

### 3.9 Social Proof

- **H2**：`What Creators Say`
- 1-2 条引言，每张 = 引文（风格感受，自然语气）+ 署名 + 角色/平台
- 语气温暖、真实，避免 "best tool ever" 类过度营销

### 3.10 Related Apps

- **H2**：`Also in the Studio`
- **选择策略**：1 个同品类 Style App + 1 个相邻品类（Filter 或 Effect）+ 1 个热门通用 App
- 每张卡片 = App 名 + 一句话描述
- `See all apps →` 链接指向 `/apps`

### 3.11 FAQ

**H2**：`Questions, Answered.`

**5 个问答**（使用 `<details>/<summary>` HTML，确保 Bing 可抓取）：

| # | 主题 | 问题示例 |
|---|------|---------|
| **Q1** | 版权/风格归属 | "Is this an official [Style Name] product / Does Vofy own the [Style] style?" → 说明 AI 生成 vs 原作的关系 |
| **Q2** | 适用照片 | "What kind of photos work best with [Style Name] style?" |
| **Q3** | 输出格式 | "What resolution and format does the [Style Name] output come in?" |
| **Q4** | 商用许可 | "Can I use [Style Name] style photos for commercial projects?" |
| **Q5** | 竞品对标 | "How is this different from [competitor]'s [style] filter?" |

### 3.12 Closing CTA

| 元素 | 规范 |
|------|------|
| **H2** | `Reimagine Your Photos with [Style Name] Art.`（呼应 Hero 的 "Turn Your Photo into" 情感钩子） |
| **Subtitle** | 简短行动描述（1 句） |
| **CTA 按钮** | `Turn Your Photo into [Style Name] Art` |

---

## 四、SEO 检查清单（Style 类）

### 4.1 关键词矩阵

| 层级 | 关键词类型 | 示例（以 Impressionist 为例） | 投放位置 |
|------|-----------|---------------------------|---------|
| **主词** | `AI [style] style` / `[style] style generator` | `AI Impressionist style` / `Impressionist style generator` | H1 破折号前、breadcrumb、meta title |
| **变体 1** | `turn photo into [style]` | `turn photo into Impressionist painting` | H1 破折号后、Ch.01 正文、subtitle |
| **变体 2** | `[style] art generator` | `Impressionist art generator` | Ch.01 正文、Ch.04 H2 |
| **变体 3** | `[style] portrait` / `[style] painting` | `Impressionist portrait` / `AI Impressionist painting` | Ch.03 场景卡片、FAQ |
| **长尾** | `how to [style] photo` / `create [style] art with AI` | `how to make impressionist art with AI` | FAQ Q2/Q5、配套 Blog |

### 4.2 Title Tag vs H1 对照

| 元素 | 内容 | 字符数 |
|------|------|--------|
| **Title Tag** | `AI [Style Name] Style Generator — Turn Photo into [Style] Art \| Vofy` | 50-60 |
| **H1** | `AI [Style Name] Style Generator — Turn Your Photo into [Style Name] Art` | 50-70 |
| **Meta Description** | `Turn your photo into [style] art with Vofy's free AI [Style Name] Style Generator. [1 句风格感受]. No design skills needed. Try it now.` | 140-155 |

### 4.3 FAQ 长尾关键词映射

| FAQ | 覆盖长尾 |
|-----|---------|
| Q1 | `is [style] AI generator free` / `[style] AI official` |
| Q2 | `best photos for [style] style` / `[style] style before after` |
| Q3 | `[style] AI resolution` / `[style] generator output format` |
| Q4 | `[style] AI commercial use` / `AI [style] art license` |
| Q5 | `[style] AI vs [competitor]` / `best [style] generator` |

---

## 五、极简草稿版（用于快速填充）

```
┌──────────────────────────────────────┐
│  Apps > Style > [Style Name] Style   │  BREADCRUMB
├──────────────────────────────────────┤
│  [Style] badge                       │  HERO
│  H1: AI [Style] Style Generator —    │
│      Turn Your Photo into [Style] Art│
│  [Subtitle: 风格感受 + 技术能力]      │
│  [Upload an image]                   │
├──────────────────────────────────────┤
│  [Upload] [Style preset ▼]           │  TOOL WIDGET
│  [4 preset cards with thumbnails]    │  + GALLERY
│  Settings: [Model ▼]·[Aspect ▼]·[Res]│
│  [Examples: Original→Styled ×4]      │
├──────────────────────────────────────┤
│  What is [Style] Style, Exactly?     │  CH.01
│  [定义→视觉特征→AI 实现, 2-3段]      │
├──────────────────────────────────────┤
│  What Makes a Photo Look [Style].    │  CH.02
│  [4 cards: Palette│Light│Tone│Texture]│
├──────────────────────────────────────┤
│  When to Use [Style] Style.          │  CH.03
│  [4 cards: Portraits│Landscapes│     │
│            Social Media│Prints]       │
├──────────────────────────────────────┤
│  How to Turn Photo into [Style] Art  │  CH.04
│  in Three Steps.                     │
│  01 Upload  02 Pick Preset  03 Gen   │
├──────────────────────────────────────┤
│  "What creators say" [2 quotes]      │  SOCIAL
├──────────────────────────────────────┤
│  Also in the Studio [3 app cards]    │  RELATED
├──────────────────────────────────────┤
│  FAQ [5 Q&A: 版权→照片→格式→许可→竞品]│  FAQ
├──────────────────────────────────────┤
│  Reimagine Your Photos with [Style]  │  CLOSING
│  [Turn Your Photo into [Style] Art]  │
└──────────────────────────────────────┘
```

---

## 六、品类内一致性检查清单

每次新增 Style 类 App 页面时，逐项核对：

| # | 检查项 | 标准 |
|---|--------|------|
| ① | H1 句式 | 必须匹配 `AI [X] Style Generator — Turn Your Photo into [X] Art` |
| ② | Ch.02 卡片数 | 必须恰好 4 张（不可多不可少） |
| ③ | Ch.02 卡片维度 | 必须使用 Palette / Lighting / Tone / Texture 四个维度 |
| ④ | HowTo 步骤 2 | 必须以 `Pick a [X] Preset` 为核心动词 |
| ⑤ | FAQ Q1 | 必须覆盖版权/风格归属类问题 |
| ⑥ | slug 后缀 | 必须以 `-style` 结尾 |
| ⑦ | Breadcrumb 品类 | 必须为 `Apps > Style > [App Name]` |
| ⑧ | Related Apps #1 | 必须为同品类 Style App |
| ⑨ | CTA 文案 | 必须含 "Turn Your Photo into [Style] Art" 变体 |
| ⑩ | 情感基调 | 诗意、温暖、灵感——全文不可出现机械/冷感的描述 |

---

## 站内关联

[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [缺口分析](./vofy-style-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) · [站面结构](../vofy-site-structure.md) · [关键词映射](../vofy-keywords.md)

---

*基于 Vofy Ghibli Style 页面的完整逆向结构分析。所有区块和顺序已验证为全站一致模式。*
