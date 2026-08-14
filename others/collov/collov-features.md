# Collov AI Features 功能页总结

> **本文档职责**：功能页详情、能力归属、Benefit、Title/Meta；不写场景叙事，链至 Use Cases。  
> **引用**：[collov.md](./collov.md) 产品概览 | [collov-use-cases.md](./collov-use-cases.md) 场景 | [collov-solutions.md](./collov-solutions.md) 业务结果 | [collov-keywords.md](./collov-keywords.md) 关键词 | [collov-competitors.md](./collov-competitors.md) 竞品 | [collov-site-structure.md](./collov-site-structure.md) 站点结构 | [collov-growth-strategy.md](./collov-growth-strategy.md) 增长策略

**Features 与 Solutions、Use Cases 严格区分**（参考 features-page-generator v1.1）：

| 类型 | 回答的问题 | 组织维度 | 示例 |
|------|------------|----------|------|
| **Features** | 产品**能做什么**？ | Capabilities（能力） | Virtual Staging、Add Furniture、Furniture Finder |
| **Use Cases** | **在什么情境下**会用？ | Persona、Scenarios | For Real Estate Agents、For Designers、For Homeowners |
| **Solutions** | 能获得什么**业务结果**？ | Outcome、ROI | Sell Faster、Win Projects、Visualize |

**Features 页原则**：Benefit-first（先讲用户获得什么）；按能力分组，不按 use case；**不写场景叙事**，用 Use case links 链至对应页，避免内容蚕食。

---

## 一、功能概览与价值评估

### 1.1 核心产品线（已有）

| 功能 | Benefit（用户获得） | URL | 目标关键词 | 价值评估 |
|------|---------------------|-----|------------|----------|
| **Virtual Staging** | 15 秒出写实软装图，无需 3D 或实体拍摄 | /virtual-staging、/virtual-staging-ai | AI virtual staging, virtual staging AI | **高** |
| **Multi-Angle Staging** | 同一房间多图统一家具，风格一致 | /virtual-staging-ai | multi-angle staging | **高** |
| **Photo Editing** | 光线/杂物/季节/Twilight 一键优化，MLS 级照片 | /add-furniture、/change-seasons 等 | AI real estate photos, photo enhancement | **高** |
| **Virtual Tour** | 360° 沉浸式看房，提升 listing 吸引力 | /ai-virtual-tour-generator、/360-panorama-generator | 360 virtual tour, virtual tour real estate | **高** |
| **AI Vizard** | 嵌入式/白标 AI 设计工具，API 集成至第三方平台 | /ai-vizard/、app.collov.ai/ai-vizard/ | embedded AI design, white label interior design, AI design API | **高** |
| **AI Desk** | 线下门店 AI 设计 Kiosk，实时交互体验 | /ai-desk | AI desk, AI design kiosk, in-store AI interior design | **中** |

### 1.2 AI 工具（已有）

| 工具 | URL | 目标关键词 |
|------|-----|------------|
| Add Furniture | /add-furniture | add furniture to empty room, AI add furniture |
| Furniture Eraser | — | furniture eraser, remove furniture |
| Room Declutter | — | room declutter |
| Change Seasons | /change-seasons | change seasons photo, seasonal photo |
| Twilight | — | twilight real estate photos, day to dusk |
| Cabinet Visualizer | /cabinet-ai | cabinet visualizer, cabinet AI |
| Flooring Visualizer | /flooring-ai | flooring visualizer, flooring AI |
| AI Furniture Detection | /furniture-ai | AI furniture detection, furniture AI |

### 1.3 新增功能（待建）

| 功能 | Benefit（用户获得） | URL | 目标关键词 | 价值评估 |
|------|---------------------|-----|------------|----------|
| **AI Furniture Finder** | 房间图→家具清单+可购链接，Shop the Look | /furniture-finder | AI Furniture Finder, Shop the Look AI, Find Furniture from Photo, Visual Furniture Search | **高** |
| **AI Design Callout** | 房间图→专业标注图，汇报/Listing 即用 | /design-callout | AI Design Callout, Annotated Room Rendering, AI Room Breakdown, Furniture Label Overlay | **高** |
| **AI Room Score** | 房间图→6 维度 0–100 评分→低分一键 Virtual Staging | /ai-room-score | AI room score, room rating AI, AI room analysis, interior design score, room critique AI | **高** |

---

## 二、新增功能详解

### 2.1 AI Furniture Finder | /furniture-finder

**行业通用名称**：AI Furniture Finder、Visual Search、Shop the Look

**核心功能**：用户上传一张完整的室内房间照片，AI 自动识别图中每一件家具（如沙发、茶几、台灯、地毯等），提取出来并以独立的列表或卡片形式展示，每件家具附带名称、材质、风格描述，甚至可匹配到可购买的类似商品链接。

**输出结果**：Design Board / Material Board —— 结构化的家具清单，原图不做任何修改。类似 Spacely AI 的 "AI Furniture Finder" 和 REimagineHome 的 "Shoppable Bundle" 功能。

**链至 Use Cases**（场景叙事见 [collov-use-cases.md](./collov-use-cases.md)，此处不重复）：[For Homeowners](/homeowner)、[For Interior Designers](/designer)、待拓展 [Furniture Retail](/furniture-retail)

**目标关键词**：AI Furniture Finder, Shop the Look AI, Find Furniture from Photo, Visual Furniture Search, AI Design Board Generator

**Meta 建议**：
- **Title**: AI Furniture Finder — Shop the Look from Room Photos | Collov AI
- **Description**: Upload a room photo. Collov AI identifies every piece of furniture—sofa, table, lamp, rug—and creates a shoppable design board. Find similar products, build FF&E schedules, drive sales.

---

### 2.2 AI Design Callout | /design-callout

**行业通用名称**：Design Callout、Annotated Rendering、Room Breakdown

**核心功能**：用户上传一张完整的室内房间照片，AI 识别图中每一件家具的位置，然后直接在原图上叠加标注——用箭头、引线和文字标签指向对应家具，标明名称、材质或规格信息。

**输出结果**：Annotated Rendering / Callout Diagram —— 一张带有专业标注的渲染图，原图被直接修改/叠加了视觉标注层。类似室内设计师做的 Design Presentation Board 上的标注效果图。

**链至 Use Cases**（场景叙事见 [collov-use-cases.md](./collov-use-cases.md)）：[For Interior Designers](/designer)、[For Real Estate Agents](/real-estate)

**目标关键词**：AI Design Callout, Annotated Room Rendering, AI Room Breakdown, Furniture Label Overlay, Design Annotation Tool

**Meta 建议**：
- **Title**: AI Design Callout — Annotated Room Rendering | Collov AI
- **Description**: Turn any room photo into a professional annotated rendering. AI adds arrows, labels, and callouts for each piece of furniture—perfect for design presentations and listings.

---

### 2.3 Moodboard Generator | /moodboard-generator

> **说明**：Moodboard 为灵感板/情绪板，通常为多图拼贴。若与 Design Callout 为同一能力，可考虑合并或 301。此处按用户指定 URL 单独建页。

**行业通用名称**：Moodboard Generator、Design Board、Inspiration Board

**核心功能**：从房间照片或设计灵感生成可视化 moodboard，整合家具、材质、色彩等设计元素。

**链至 Use Cases**（见 [collov-use-cases.md](./collov-use-cases.md)）：[For Interior Designers](/designer)

**目标关键词**：AI moodboard generator, design moodboard, interior design moodboard

**Meta 建议**：
- **Title**: AI Moodboard Generator — Design Boards from Room Photos | Collov AI
- **Description**: Create professional moodboards from any room photo. Collov AI extracts design elements and builds visual inspiration boards for clients and presentations.

---

### 2.4 AI Room Score | /ai-room-score

> **详细文档**：[collov-ai-room-score.md](./collov-ai-room-score.md) — 功能定义、竞品空白、关键词策略、技术要点

**行业通用名称**：AI Room Score、Room Grader、Room Critique、Room Analysis、Design Score、AI Room Assessment

**核心功能**：用户上传一张完整的室内房间照片，AI 从 6 个维度（家具覆盖度、摆放整齐度、风格一致性、光线品质、空间利用率、视觉吸引力）打出 0–100 分，生成分维度雷达图 + 问题清单。**核心闭环**：低分房间一键跳转 Virtual Staging / Photo Editing 优化，形成「评分→发现问题→AI 修复→评分对比」的完整链路。

**输出结果**：总分 + 等级标签（Excellent/Good/Fair/Poor）+ 各维度子分数 + 优先级问题清单 + 优化建议 CTA。支持 Before/After 评分对比展示。

**链至 Use Cases**（场景叙事见 [collov-use-cases.md](./collov-use-cases.md)）：[For Real Estate Agents](/real-estate)、[For Interior Designers](/designer)、[For Homeowners](/homeowner)

**目标关键词**：AI room score, room rating AI, AI room analysis, interior design score, room critique AI, room assessment tool, AI room evaluation

**长尾关键词**：rate my room AI, room style checker, furniture arrangement score, room layout score AI, AI room grader real estate, interior design rating AI free, room clutter score, before after room score

**竞品空白**：RoomsGPT（5 维度评分，无转化闭环）、SpaceSenseAI（Hackathon 项目，无商业化）、Roast My Room（~13K 月访问、+129% MoM，偏娱乐化）。尚无竞品提供「评分→Virtual Staging 直达」的闭环体验。

**Meta 建议**：
- **Title**: AI Room Score — Analyze & Rate Your Room Design in Seconds | Collov AI
- **Description**: Upload any room photo. Collov AI scores your space across 6 dimensions—furniture, layout, style, lighting, space use, visual appeal. Get a 0–100 score plus fix suggestions. Low score? Jump to AI virtual staging in one click.

---

## 三、内链规划

```
首页 (/)
  ├── /virtual-staging-ai
  ├── /add-furniture、/change-seasons、/cabinet-ai、/flooring-ai、/furniture-ai
  ├── /furniture-finder       ← 新增
  ├── /design-callout         ← 新增
  ├── /moodboard-generator    ← 新增
  ├── /ai-room-score          ← 新增
  ├── /real-estate、/designer、/homeowner
  ├── /ai-virtual-tour-generator、/360-panorama-generator
  ├── /pricing
  └── /blog

各功能页「Explore More Tools」互链：furniture-finder ↔ design-callout ↔ add-furniture ↔ virtual-staging-ai ↔ ai-room-score
```

**Use case links**（链至 Use Cases，不重复场景内容）：
- [For Real Estate Agents](/real-estate) | [For Interior Designers](/designer) | [For Homeowners](/homeowner)

**待拓展 Use Cases 与 Features 映射**（见 [collov-use-cases.md §四](./collov-use-cases.md#四待拓展-use-cases)）：
- Vacation Rental：Virtual Staging、Photo Editing、Change Seasons
- Commercial：Virtual Staging、Add Furniture（需商业场景模板）
- Developers：Virtual Staging、Multi-Angle、360° Tour
- Contractors：Cabinet、Flooring、Partial Remodel、Home Redesign
- Furniture Retail：Furniture Finder、Virtual Staging（需 API、电商集成）

---

## 四、与竞品功能对齐

| 功能 | Collov | Spacely AI | REimagineHome |
|------|--------|------------|---------------|
| AI Furniture Finder | /furniture-finder（待建） | AI Furniture Finder | Shoppable Bundle |
| Design Callout | /design-callout（待建） | — | — |
| Virtual Staging | ✅ | ✅ | ✅ |

---

## 五、文档导航

→ [collov.md](./collov.md) 产品概览 | [collov-labs.md](./collov-labs.md) Collov Labs | [collov-use-cases.md](./collov-use-cases.md) 场景 | [collov-solutions.md](./collov-solutions.md) 业务结果 | [collov-keywords.md](./collov-keywords.md) 关键词 | [collov-competitors.md](./collov-competitors.md) 竞品 | [collov-site-structure.md](./collov-site-structure.md) 站点结构 | [collov-growth-strategy.md](./collov-growth-strategy.md) 增长策略 | [collov-ai-room-score.md](./collov-ai-room-score.md) AI Room Score | [collov-ai-vizard.md](./collov-ai-vizard.md) AI Vizard

**Last updated**: 2026-05-27（新增 AI Vizard 文档）
