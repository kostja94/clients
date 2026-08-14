# Collov AI

**Collov 文档导航**（各文档独立、互相引用）：

| 文档 | 职责 | 引用 |
|------|------|------|
| [collov.md](./collov.md) | **本文档**：产品概览、Collov Labs 生态、网站结构 | — |
| [collov-labs.md](./collov-labs.md) | **Collov Labs**：collov.com 独立文档、定位、品牌 SEO 优化 | [collov.md](./collov.md) |
| [collov-features.md](./collov-features.md) | 功能页：能力、Benefit、URL、链至 Use Cases | [collov.md](./collov.md)、[collov-use-cases.md](./collov-use-cases.md)、[collov-solutions.md](./collov-solutions.md) |
| [collov-use-cases.md](./collov-use-cases.md) | 应用场景：Scenario-first、Persona、链至 Solutions（父）、Features | [collov-solutions.md](./collov-solutions.md)、[collov-features.md](./collov-features.md) |
| [collov-solutions.md](./collov-solutions.md) | 业务结果：Outcome-first、链至 Use Cases（子应用）、Features | [collov-use-cases.md](./collov-use-cases.md)、[collov-features.md](./collov-features.md) |
| [collov-keywords.md](./collov-keywords.md) | 关键词映射、目标页、待办 | [collov-features.md](./collov-features.md) §二、[collov-use-cases.md](./collov-use-cases.md) §2.3 |
| [collov-site-structure.md](./collov-site-structure.md) | 站点结构：URL 层级、IA、技术架构、sitemap 对账 | [collov.md](./collov.md)、[collov-keywords.md](./collov-keywords.md) |
| [collov-growth-strategy.md](./collov-growth-strategy.md) | 增长策略：渠道、内容战役、SEO/GEO 优化、实验 | [collov-keywords.md](./collov-keywords.md)、[collov-site-structure.md](./collov-site-structure.md) |
| [collov-competitors.md](./collov-competitors.md) | 竞品分析、差异化 | [collov-features.md](./collov-features.md)、[collov-solutions.md](./collov-solutions.md) |
| [collov-virtual-staging-ranking-fluctuation.md](./collov-virtual-staging-ranking-fluctuation.md) | virtual staging 排名波动记录、原因与来源 | [collov-keywords.md](./collov-keywords.md) |
| [collov-migration-seo-analysis.md](./collov-migration-seo-analysis.md) | 框架迁移（Next.js 原生 vs iframe）SEO 与流量影响分析 | [collov-virtual-staging-ranking-fluctuation.md](./collov-virtual-staging-ranking-fluctuation.md) |
| [collov-ai-room-score.md](./collov-ai-room-score.md) | **AI Room Score**：上传照片 → 6 维度评分 → 低分直达 Virtual Staging 优化 | [collov-features.md](./collov-features.md)、[collov-keywords.md](./collov-keywords.md) |
| [collov-ai-vizard.md](./collov-ai-vizard.md) | **AI Vizard**：嵌入式/白标 AI 设计工具，API 集成至第三方平台 | [collov.md](./collov.md)、[collov-features.md](./collov-features.md)、[collov-keywords.md](./collov-keywords.md) |

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2B/B2C SaaS / AI 虚拟软装与房产视觉平台 |
| 网站 | https://collov.ai/ |
| 母公司 | [Collov Labs](https://www.collov.com/)（Visual Intelligence Substrate） |
| 当前阶段 | 增长期 |
| 核心产品 | AI 虚拟软装、房产照片编辑、360° 虚拟看房 |
| Slogan | Virtual Staging AI : Elevate Your Real Estate Listings |
| 数据规模 | 1M+ 房产专业人士、73% 更快售出、78% 更多意向买家、20% 更高报价 |
| 公司 | Collov AI（Collov Labs 旗下产品） |
| 更新日期 | 2026-05-27 |

---

## 0. 公司背景：Collov Labs 生态系统

**Collov AI** 隶属于 **Collov Labs**（[collov.com](https://www.collov.com/)），是后者「Visual Intelligence Substrate」在房产与室内设计领域的垂直应用。

### Collov Labs 定位

- **Slogan**：Not a Product. Not a Studio. A System.
- **使命**：Unlocking the latent potential of visual intelligence through autonomous optimization. 通过自主优化释放视觉智能潜力，构建可扩展高保真创造力的自学习架构。
- **核心**：提供底层智能，支撑 AI 应用生态；系统可学习、适应、随时间复利增长。「The system is the solution.」

### Collov Labs 产品矩阵

| 产品 | 定位 | 链接 |
|------|------|------|
| **Collov AI** | Intelligent Design For Real Estate — 房产智能设计，虚拟软装与照片增强 | [collov.ai](https://collov.ai/) |
| **CozyAI** | Advanced Visual Design for Prosumers — 面向专业消费者的日常环境设计，强调 presence、comfort、continuity | App Store、Google Play |
| **Intelligent Capture** | 自主空间采集，agentic vision 赋能工作流 | Early Access |

> Each Collov product is a domain-specific interface into the same intelligence core — tuned for different contexts, users, and constraints.

### 技术底座（Collov Labs）

- **Visual Understanding**：Open-vocabulary 检测/分割，depth/line/plane 理解，将像素转为可查询场景表示
- **Self-evolving Multimodal Agentic System**：理解场景、推理用户意图与约束、规划并执行多步工作流
- **Built-in Diffusion Model Retraining**：生产交互转为训练信号，持续更新模型
- **Generative Diffusion Model**：生产级 DiT backbone，可按垂直领域与部署约束调优

### 研究支撑

| 论文/项目 | 会议 | 说明 |
|-----------|------|------|
| Meissonic | ICLR 2025 | 高分辨率 T2I 合成，SOTA 质量、更低 GPU 成本 |
| D-edit | AAAI 2025 | 室内设计元素（地板、橱柜等）高精度区域编辑 |
| Integrating View Conditions | IJCAI 2024 | 3D 空间感知、view-conditional 一致性 |
| FlexControl | ICML 2025 | 计算感知 ControlNet，优化推理成本 |
| DPaI | ICLR 2025 | 剪枝与初始化，减小模型规模 |

*详见 [collov.ai/research](https://collov.ai/research)*

### 合作伙伴与活动

- **Intel**：Hybrid AI、OpenVINO、Intel Core Ultra，边缘设备实时设计工作流
- **Qualcomm**：Snapdragon Summit 2025，行业首个消费级网站端 on-device AI 演示
- **Cloudflare**：全球边缘网络，保障速度与安全
- **a16z Tech Week**：Spatial Intelligence 主题
- **Epic**：Unreal Engine x AI「Epic Connector」，AI 生成环境导入实时引擎
- **World Economic Forum @ Davos**：3D AI 合成与可持续城市规划
- **NeurIPS 2024**、**GenAI Assembly 2024** 等

*详见 [collov.ai/partners](https://collov.ai/partners)*

---

## 1. 产品信息

### 产品定位

**Collov AI** 是 [Collov Labs](https://www.collov.com/) 旗下的 AI 虚拟软装与房产视觉平台，帮助房产经纪、室内设计师、业主将空房或低质量照片转化为专业级软装效果图。一键上传即可在约 15 秒内生成写实软装图，支持多角度、多风格、多房间类型。Collov Labs 官方描述：*By automating high-fidelity staging and image enhancement, our agent system serves as a performance multiplier—accelerating the sales cycle and increasing listing quality with minimal manual effort.*

### 目标受众

- **房产经纪**：提升房源吸引力、加速成交
- **室内设计师**：快速呈现设计效果，无需实体拍摄或 3D 建模
- **业主**：装修前可视化效果
- **待拓展**（见 [collov-use-cases.md §四](./collov-use-cases.md#四待拓展-use-cases)）：度假租赁/物业管理、商业地产、开发商、装修承包商、家具零售

### 核心产品线

| 产品 | 说明 |
|------|------|
| **Virtual Staging** | 空房一键软装，多风格（Scandinavian、Modern、Luxury 等）、多房间类型 |
| **Multi-Angle Staging** | 同一房间多张照片应用统一家具 |
| **Photo Editing** | 光线优化、杂物移除、专业级照片增强 |
| **Virtual Tour** | 360° 虚拟看房，沉浸式浏览 |
| **AI Vizard** | 嵌入式 AI 设计工具，可 API 集成至第三方平台（家具电商、房产平台等） |
| **AI Desk** | 线下门店 AI 设计 Kiosk，体验式消费场景 |

*功能页详情见 [collov-features.md](./collov-features.md)；关键词见 [collov-keywords.md](./collov-keywords.md)*

### AI 工具

- Add/Remove Furniture、Furniture Eraser、Room Declutter
- Enhance Photo Quality、Material Overlay
- Changing Seasons、Rain to Shine、Natural Twilight、Virtual Twilight
- Add Water to Empty Pool、Pool Water Enhancement、Lawn Replacement、Night to Day
- Cabinet Visualizer、Flooring Visualizer、AI Furniture Detection
- Home Renovation、Partial Remodel
- **AI Vizard**（/ai-vizard/）：嵌入式 AI 设计工具，可集成至第三方平台（API/白标）
- **AI Desk**（/ai-desk）：线下门店 AI 设计 Kiosk，实时交互体验
- **AI Furniture Finder**（/furniture-finder）：上传房间照片→AI 识别每件家具→生成 Design Board / 可购链接（Shop the Look）
- **AI Design Callout**（/design-callout）：上传房间照片→AI 在原图叠加箭头、引线、标签→专业标注图
- **AI Moodboard Generator**（/moodboard-generator）：从房间照片生成设计灵感板
- **AI Room Score**（/ai-room-score）：上传房间照片→AI 从家具、整齐度、风格一致性等 6 维度打出 0–100 分→低分一键跳转 Virtual Staging 优化

### 差异化优势

- **约 15 秒出图**：快速、写实
- **73% 更快售出**、**78% 更多意向买家**、**20% 更高报价**
- **Twilight 转换**：日转暮，提升浏览量约 35%
- **多风格**：Scandinavian、Modern、Industrial、Luxury
- **商业授权**：高分辨率下载、商用许可
- **Collov Labs 背书**：自研 Visual Intelligence Substrate、ICLR/AAAI/IJCAI 论文、Intel/Qualcomm 等合作落地

### 产品/SKU 列表（定价）

| 套餐 | 月付 | 照片 Credits | 备注 |
|------|------|--------------|------|
| Standard | $19 | 60 | 无限重生成、无水印、全房间类型与风格 |
| Advanced | $49 | 150 | 含照片编辑（家具编辑、质量增强、Twilight、天气、季节） |
| Premium | $79 | 263 | 含 AI 虚拟看房、360° 全景 |
| Enterprise | $127 | 526 | API、专属支持 |

> 约 $0.27/张（Standard）；Enterprise 额外约 $0.24/张。传统实体软装约 $1,500–4,000/月/套，Collov 成本显著更低。

---

## 2. 关键词

> 完整映射见 [collov-keywords.md](./collov-keywords.md)

| 意图 | 覆盖 | 代表词 |
|------|------|--------|
| 虚拟软装核心 / 空房软装 | ✅ | AI virtual staging, virtual staging for empty rooms |
| 房产照片增强 | ✅ | AI real estate photos |
| Solutions / Use Cases（§2.3） | ✅ | virtual staging for realtors, real estate, designer, homeowner |
| AI 工具（§2.4） | ✅ | add furniture, change seasons, cabinet, flooring, 360 panorama, virtual tour video |
| API / 地域 | 部分 | virtual staging API, virtual staging [city] |

---

## 3. 竞品

> 详细分析见 [collov-competitors.md](./collov-competitors.md)

### 直接竞品

| 竞品 | 说明 |
|------|------|
| **BoxBrownie** | 人工设计、$24/张、48h 交付 |
| **Apply Design** | AI、$7–10.5/张、10 分钟 |
| **REimagineHome** | AI 全栈、$14–99/月 |
| **StageHQ** | AI、$0.28/张、30 秒 |
| **Styldod** | AI 虚拟软装 |

### 差异化优势

- **速度**：约 15 秒出图（vs BoxBrownie 48h）
- **多工具**：虚拟软装、照片编辑、虚拟看房、季节/天气/泳池/草坪、Furniture Finder、Design Callout
- **多风格**：Scandinavian、Modern、Luxury 等
- **定价**：$19 起，低于传统实体软装（$1,500–4,000/套）

---

## 4. 网站结构

> 完整 URL 层级、IA 导航、技术架构、sitemap 对账见 [collov-site-structure.md](./collov-site-structure.md)

**导航结构**：AI Virtual Staging / AI Tools / AI Vizard / AI Desk / Solutions / Resources / Pricing。

**URL 模式**：/virtual-staging（核心）、/virtual-staging/{room}（11 种房间）、/virtual-staging/{style}（7 种风格）、/{persona}（3 种已上线 + 5 待拓展）、/{tool}（AI 工具）、/features/{slug}、/articles/{slug}。

**待建功能**：/furniture-finder、/design-callout、/moodboard-generator、/ai-room-score。

**Sitemap 对账**：/360-panorama-generator 页面存在但未收录于 sitemap.xml；/ai-virtual-tour-generator 未在 sitemap 中。

---

## 5. 增长策略

> 完整增长策略、内容营销、渠道、实验计划见 [collov-growth-strategy.md](./collov-growth-strategy.md)

**核心增长杠杆**：SEO（关键词覆盖 + 对比页 + 地域页）、内容营销（博客/教程/案例）、产品驱动增长（2 Free Renderings 试用）。

**内容主题**：虚拟软装（P0）、房产照片（P1）、虚拟看房（P1）、家具识别/购物（P1）、竞品对比（P0）。

**待办优先级**：P0 — virtual-staging-ai 差异化 meta、竞品对比页；P1 — 新建 4 个功能页、度假租赁页、API 页强化、地域页扩展。

---

## 6. 优化建议

> 详细优化计划见 [collov-growth-strategy.md](./collov-growth-strategy.md) §二、§六

### SEO

- 风格页独立 title/meta
- 对比页：Collov vs BoxBrownie、Collov vs 实体软装
- API 页覆盖开发者搜索

### GEO（Generative Engine Optimization）

- 结构化 Q&A 格式，便于 AI 引用
- 数据引用：73% 更快售出、78% 更多意向买家、20% 更高报价

---

**Last updated**: 2026-05-27
