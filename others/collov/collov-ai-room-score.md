# Collov AI — AI Room Score 房间智能评分

> **本文档职责**：AI Room Score 功能定义 — 上传房间照片 → AI 多维度评分 → 低分直达 Virtual Staging 优化。  
> **引用**：[collov.md](./collov.md) 产品概览 | [collov-features.md](./collov-features.md) 功能 | [collov-keywords.md](./collov-keywords.md) 关键词 | [collov-use-cases.md](./collov-use-cases.md) 场景 | [collov-competitors.md](./collov-competitors.md) 竞品

**文档导航**：→ [collov.md](./collov.md) | [collov-features.md](./collov-features.md) | [collov-use-cases.md](./collov-use-cases.md) | [collov-keywords.md](./collov-keywords.md) | [collov-site-structure.md](./collov-site-structure.md) | [collov-growth-strategy.md](./collov-growth-strategy.md)

---

## 一、功能概览

| 项目 | 内容 |
|------|------|
| **功能名称** | AI Room Score（AI 房间智能评分） |
| **一句话** | 上传任意房间照片，AI 从家具、整齐度、风格一致性等多维度打出 0–100 分，低分房间一键跳转 Virtual Staging 优化 |
| **URL** | `/ai-room-score` |
| **行业通用名称** | AI Room Score、Room Grader、Room Critique、Room Analysis、Design Score、AI Room Assessment |
| **状态** | 待建 |
| **价值评估** | **高** — 需求验证：RoomsGPT AI Design Advisor（房间评分核心功能）月访问 74.2K（2026-03），有机搜索占 24% 约 ~18K/月；Roast My Room 月访问 ~13.3K、+129% MoM、峰值 91.3K（2025-03）；上述数据来自 aitools.xyz 和 explodone.toolsurf.com 的第三方工具监测 |

---

## 二、核心功能

### 2.1 输入

用户上传一张**完整的室内房间照片**（客厅、卧室、厨房、浴室等均可）。

### 2.2 AI 分析维度（6 维度评分）

| 维度 | 评估内容 | 权重 |
|------|----------|------|
| **家具覆盖度** (Furniture Presence) | 房间是否有家具？空房 vs 已布置；家具密度是否合理（过空/过满） | **高** |
| **摆放整齐度** (Arrangement & Tidiness) | 家具摆放是否规整、动线是否合理、表面是否杂乱、是否有遮挡 | **高** |
| **风格一致性** (Style Consistency) | 家具之间风格是否统一（现代/北欧/传统 混搭是否刻意）、色彩是否协调 | **高** |
| **光线品质** (Lighting Quality) | 自然光与人工光平衡、阴影分布、亮度是否适合展示 | 中 |
| **空间利用率** (Space Utilization) | 家具尺寸与房间比例、空间是否被充分利用、动线畅通度 | 中 |
| **视觉吸引力** (Visual Appeal) | 整体美感、构图、是否产生「想住」的感觉 | 中 |

### 2.3 输出

- **总分**：0–100 分，带等级标签（Excellent 90+ / Good 70–89 / Fair 50–69 / Poor <50）
- **分维度得分**：雷达图 + 各维度独立分数
- **问题清单**：按优先级列出具体问题（如「沙发与茶几风格冲突」「窗帘遮挡自然光」「地面杂物过多」）
- **优化建议**：可执行建议 + CTA

### 2.4 低分 → Virtual Staging 转化路径

**核心闭环**：分数越低，Virtual Staging 价值越明显。

| 评分区间 | 用户痛点 | 推荐操作 | CTA |
|----------|----------|----------|-----|
| **<50 (Poor)** | 空房或严重杂乱、无法展示 | 全屋 Virtual Staging | [Stage This Room →](/design-center/virtual-staging) |
| **50–69 (Fair)** | 有家具但风格不统一、光线差 | Virtual Staging 替换风格 + Photo Editing | [Enhance This Room →](/add-furniture) |
| **70–89 (Good)** | 小问题（杂乱、个别家具突兀） | Furniture Eraser + Declutter + 微调 | [Fine-tune This Room →](/virtual-staging-ai) |
| **90+ (Excellent)** | 基本完美 | 无需操作 | 分享成绩 / 对比其他房间 |

### 2.5 与现有功能的关系

| 现有功能 | 与 AI Room Score 的关系 |
|----------|-------------------------|
| **Virtual Staging** | Room Score 是 Virtual Staging 的**入口触发器** — 低分 → 一键软装 |
| **Furniture Finder** | Room Score 识别家具有无 → Furniture Finder 识别具体家具+可购链接 |
| **Design Callout** | Room Score 发现问题 → Design Callout 生成标注图向客户解释 |
| **Photo Editing** | Room Score 发现光线/杂乱问题 → Photo Editing（Declutter、Twilight、Enhance） |

---

## 三、竞品与市场空白

### 3.1 直接对标

| 工具 | 评分维度 | 评分输出 | 转化闭环 | 规模 |
|------|----------|----------|----------|------|
| **RoomsGPT AI Design Advisor** | 5 维度（色彩、布局、光线、风格、家具比例） | 0–100 分 | 无（仅给建议+涂料推荐） | 免费，3 次/天 |
| **SpaceSenseAI** | 6 维度（光线、杂乱、色彩和谐、空间布局、风水、亲生物） | 0–100 + 字母等级 | 「Fix」按钮生成改进版 | Hackathon 项目 |
| **Harmony** | 布局（开放度、动线、遮挡） | Harmony Rating | 自动优化布局+热力图 | Hackathon 项目 |
| **Roast My Room** | 通用 AI 室内评估 | 定性反馈 | 无 | ~13K 月访问，+129% MoM |
| **Collov AI Room Score（本文档）** | **6 维度 + Virtual Staging 直达** | **0–100 分 + 问题清单 + 分数→CTA 路径** | **✅ 直接跳转 Virtual Staging / Photo Editing** | 待建 |

### 3.2 市场空白与 Collov 差异化

- **RoomsGPT / SpaceSenseAI**：有评分但无后续转化（不能一键美化）
- **Roast My Room**：有流量验证（13K 月访问、129% 增长）但偏娱乐化，缺乏专业变现路径
- **现有 Virtual Staging 工具**：直接软装但缺乏「先分析再优化」的决策引导

**Collov 独有优势**：Room Score → Virtual Staging / Photo Editing 的**评分→优化闭环**，让用户在「发现问题」和「解决问题」之间零跳转。这一定位在市场上尚无直接竞品。

---

## 四、关键词与搜索需求

> 完整关键词映射见 [collov-keywords.md](./collov-keywords.md)。  
> **数据说明**：精确搜索量数据仅限 SEMrush/Ahrefs 付费工具内查看；以下基于第三方工具公开的竞品流量反推 + 2025–2026 新增竞品数量推断搜索需求规模。

### 4.1 需求验证：竞品流量（房间评分/分析类产品）

| 竞品 | 月访问量 | 有机搜索占比 | 估算有机搜索量/月 | 数据来源 |
|------|----------|-------------|-------------------|----------|
| **RoomsGPT**（AI Design Advisor 为核心功能之一） | **74.2K**（2026-03） | 24.2% | **~18K** | explodone.toolsurf.com |
| **Roast My Room** | **~13.3K**（2025-12），峰值 **91.3K**（2025-03） | 40.2% | **~5.3K**（峰值 ~37K） | aitools.xyz |
| **SpaceSenseAI** | Hackathon 项目，未商业化 | — | — | devpost.com |
| **Harmony** | Hackathon 项目 | — | — | devpost.com |
| **Decorous** | 2025-03 上线，未公开 | — | — | aitoolhub.co |
| **Findecor** | 2025 夏上线（YC 申请） | — | — | Hacker News |

**结论**：仅 RoomsGPT + Roast My Room 两个产品，月均有机搜索合计约 **~23K**（峰值期可达 ~55K）。2025–2026 年至少有 6 个新项目进入房间评分/分析赛道，说明搜索需求在快速增长。

### 4.2 目标关键词（功能专属）

| 关键词 | 类型 | 搜索量判断依据 | 竞争度 |
|--------|------|----------------|--------|
| **AI room design** | 入口词（含评分意图） | RoomsGPT 主要流量来源词群，量级千级/月 | 中–高 |
| **AI room analysis** | Primary | 与 RoomsGPT "AI Design Advisor" 功能对应 | 低–中 |
| **room design AI free** | 入口词（含评分意图） | RoomsGPT 免费策略覆盖词 | 中 |
| **interior design score** | Primary | 直接功能词，RoomsGPT 5 维度评分覆盖 | 低 |
| **AI room scanner** | Primary | 3D Snap 2M+ 用户，房间扫描+分析需求 | 中 |
| **rate my room AI** | Secondary | Roast My Room 品牌词变体，已验证搜索行为 | 低 |
| **AI room score** | Secondary | 新兴词，尚无竞品精确匹配，首发优势 | 低 |
| **room assessment tool** | Secondary | 含商业/房产评估交叉意图 | 低–中 |

### 4.3 长尾关键词（功能专属）

| 关键词 | 搜索意图 | 适配内容 |
|--------|----------|----------|
| AI room design score checker | 找房间评分工具 | Room Score 首页 |
| room style checker AI | 检查风格是否统一 | 风格一致性维度详解 |
| furniture arrangement score | 检查家具摆放 | 摆放整齐度维度详解 |
| room layout score AI | 检查布局合理性 | 空间利用率维度详解 |
| AI room grader real estate | 房产经纪评估房源 | /real-estate + Room Score |
| room clutter score | 检查杂乱程度 | 摆放整齐度维度详解 |
| before after room score | 改造前后对比 | Room Score + Virtual Staging 对比 |
| AI room evaluation tool | 通用房间评估 | Room Score 首页 |
| room feng shui score AI | 风水评分 | 可拓展维度 |

### 4.4 竞品品牌词截获

| 竞品品牌词 | 策略 |
|------------|------|
| RoomsGPT alternative | Room Score 功能对比页（RoomsGPT 74K 月访问可截获） |
| Roast My Room alternative | 更专业（非娱乐化）+ 可执行 CTA（Roast My Room 13K 月访问可截获） |
| SpaceSenseAI alternative | Room Score + Virtual Staging 闭环优势 |

---

## 五、Title / Meta 建议

- **Title**: AI Room Score — Analyze & Rate Your Room Design in Seconds | Collov AI
- **Description**: Upload any room photo. Collov AI scores your space across 6 dimensions—furniture, layout, style, lighting, space use, visual appeal. Get a 0–100 score plus fix suggestions. Low score? Jump to AI virtual staging in one click.
- **H1**: AI Room Score — Rate Your Room, Then Fix It
- **OG Image**: Room Score 雷达图 + Before/After 展示

---

## 六、URL 与内链规划

```
首页 (/)
  ├── /ai-room-score          ← 新增
  │     ├── → /virtual-staging-ai（低分 → 软装）
  │     ├── → /add-furniture（家具不足 → 添加家具）
  │     ├── → /change-seasons（光线差 → Twilight）
  │     ├── → /furniture-finder（识别家具 → 可购链接）
  │     └── → /design-callout（问题 → 标注呈现）
  ├── /furniture-finder
  ├── /design-callout
  ├── /real-estate、/designer、/homeowner
  └── /blog
```

**内链交叉**（各功能页互相引流）：
- ai-room-score ↔ virtual-staging-ai ↔ furniture-finder ↔ design-callout

**Use case links**：
- [For Real Estate Agents](/real-estate)：评估 listing 照片质量，快速决定是否软装
- [For Interior Designers](/designer)：向客户展示方案前后的评分对比
- [For Homeowners](/homeowner)：装修前先打分，明确改造优先级

---

## 七、用户体验流

```
上传房间照片
    ↓
AI 分析（~5–10 秒）
    ↓
┌─────────────────────────────────────┐
│  总分：62 / 100 — Fair              │
│                                     │
│  ●●●●○  家具覆盖度  75             │
│  ●●●○○  摆放整齐度  58  ⚠         │
│  ●●●○○  风格一致性  52  ⚠         │
│  ●●●●○  光线品质    71             │
│  ●●●●○  空间利用率  68             │
│  ●●●○○  视觉吸引力  55             │
│                                     │
│  ⚠ 关键问题：                        │
│  • 茶几与沙发风格冲突                │
│  • 地面杂物过多，遮挡动线            │
│  • 窗帘遮挡自然光，建议改用百叶帘    │
│                                     │
│  [Fix with AI Virtual Staging →]    │
│  [Declutter →]  [Change Style →]    │
└─────────────────────────────────────┘
    ↓ (点击 Fix)
Virtual Staging 重新生成
    ↓
Before (62) → After (91) 对比展示
```

---

## 八、与现有 Persona 的适配

> 场景叙事见 [collov-use-cases.md](./collov-use-cases.md)，此处仅概述功能适配。

| 受众 | 使用场景 | 核心价值 |
|------|----------|----------|
| **房产经纪** | 挂牌前评估房源照片，决定是否软装 | 量化 listing 质量，避免凭感觉决策 |
| **室内设计师** | 向客户展示改造前后评分对比，用数据支撑方案 | 增强提案说服力，提升签单率 |
| **业主** | 卖房前自检或装修前评估 | 明确改造优先级，避免盲目投入 |

**待拓展**：
- Vacation Rental：评估短租房源照片质量，高分 → 更高预订率
- Commercial：评估办公室/零售空间展示效果
- Furniture Retail：房间评分 + 推荐适配家具（结合 Furniture Finder）

---

## 九、技术实现要点

### 9.1 AI 能力需求

| 能力 | 说明 |
|------|------|
| **物体检测与分割** | 识别房间内每件家具、杂物、装饰物（Collov Labs Visual Understanding 已有基础） |
| **风格分类** | 识别每件家具的设计风格（Modern、Scandinavian、Traditional 等），判断一致性 |
| **空间分析** | 评估家具比例、动线宽度、遮挡关系 |
| **光线评估** | 检测曝光、阴影、色温分布 |
| **美学评分模型** | 可参考 IJICT 2026 复合损失函数 + 扩散架构的美学评分研究（见 §十 来源[1]） |

### 9.2 性能目标

| 指标 | 目标 |
|------|------|
| 分析耗时 | 5–10 秒（与 Virtual Staging 15 秒形成「分析+生成=20 秒」总体验） |
| 准确率 | 与人类设计师评分相关度 ≥ 0.75（参考 Buildings 2026 研究 r=0.760[2]） |

---

## 十、来源与引用

| 编号 | 来源 | URL | 引用内容 |
|------|------|-----|----------|
| [1] | Tan & Wang, IJICT 2026 | [inderscience.com](https://www.inderscience.com/info/inarticle.php?artid=151654) | AI 视觉美学评分系统：+52.54% portal engagement、+40.08% agency engagement；扩散架构 + 复合损失函数 |
| [2] | Wang, Zhao & Guan, Buildings 2026 | [mdpi.com](https://www.mdpi.com/2075-5309/16/8/1508) | FHASID-10K 数据集；功能/健康/美学三维评分；GBDT 代理模型 R²=0.9992；与人评相关 r=0.760 |
| [3] | DataHacker.rs 2026 | [datahacker.rs](https://datahacker.rs/llm_log-019-layout-scoring-does-furniture-placement-follow-the-rule-of-thirds/) | 布局评分：渐变显著度 + CLIP ViT-B/32 + Gemini Vision；Bradley-Terry ρ=1.000 |
| [4] | RoomsGPT | [roomsgpt.io](https://www.roomsgpt.io/zh/ai-design-advisor) | 5 维度 0–100 设计评分：色彩、布局、光线、风格、家具比例 |
| [5] | SpaceSenseAI (Devpost) | [devpost.com](https://devpost.com/software/space-sense-ai) | 6 维度评分 + Fix 按钮；光线、杂乱、色彩和谐、空间布局、风水、亲生物 |
| [6] | Roast My Room | [aitools.xyz](https://aitools.xyz/index.php/tools/roast-my-room/statistics) | AI 室内评估工具；~13.3K 月访问（2025-12）；2025-03 峰值 91.3K；+129% MoM；有机搜索 40.2% |
| [7] | Harmony (Devpost) | [devpost.com](https://devpost.com/software/harmony-y9qiug) | Harmony Rating 布局评分；3D 重建 + 热力图；Gemini + Claude + Three.js |
| [8] | RoomsGPT 流量数据 | [explodone.toolsurf.com](https://explodone.toolsurf.com/website/roomsgpt.io/overview/) | 74.2K 月访问（2026-03）；有机搜索 24.2% ≈ ~18K/月；直接流量 42.6%；1.86K 引用域 |
| [9] | Virtual Staging AI Docs | [virtualstagingai.app](https://docs.virtualstagingai.app/v2-api/core-concepts) | Furniture Analysis API：家具检测 + 覆盖率百分比（房间评分关键能力参考） |
| [10] | Roast Or Praise (Groq) | [community.groq.com](https://community.groq.com/t/roast-or-praise-ai-powered-image-critiques-with-groq-vision/870) | AI 房间评分工具：0–10 分 + 批评/表扬；Groq Vision 驱动；验证房间评分赛道的独立需求 |

---

**Last updated**: 2026-05-20
