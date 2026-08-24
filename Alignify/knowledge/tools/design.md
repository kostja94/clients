# AI Design（AI 设计工具）· 知识块（聚合 hub）

**材料范围**：本页为聚合索引——指向三个子品类知识块 `wireframing`、`ui-design`、`prototyping`。具体工具数据和外链以子品类页为准。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/design](https://alignify.co/tools/design) · `/tools/design` · [alignify.co/zh/tools/design](https://alignify.co/zh/tools/design) · `/zh/tools/design` · `content/tools/zh/design.md`、`content/tools/en/design.md` · slug **`design`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#design-tools`](../../keywords/alignify-keywords-tools.md#design-tools)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 子品类导航

AI 设计工具不是单一品类——2026 年行业共识已将其拆为五个各自由**独立搜索引擎意图、独立产品集和独立文章生态**支撑的子品类：

| slug | 核心问题 | 典型产品 | 搜索热度 |
|------|---------|---------|---------|
| [`wireframing`](./wireframing.md) | "东西该放哪？单页结构怎么排？" | Balsamiq、Whimsical、Wireframe.cc、Moqups | Google Trends 指数 94（2025.8 峰值） |
| [`ui-design`](./ui-design.md) | "界面长什么样？从 prompt 生成完整 UI" | Stitch、Uizard、Figma AI、Visily、Pencil 等 15 款 | Google Trends 指数 100（2025.8 峰值） |
| [`prototyping`](./prototyping.md) | "交互行为怎么定义？用户真的能用吗？" | ProtoPie、Axure RP、Alloy、UXPin Merge | Google Trends 指数 99（2025.8 峰值） |
| [`ux-design`](./ux-design.md) | "体验怎么组织？系统怎么治理？" | Flowstep、Stark、Zeroheight、Figr AI、Frontitude | Google Trends 指数 100（2025.8 峰值） |
| [`user-research`](./user-research.md) | "用户在想什么？为什么流失？" | Outset、ListenLabs、Aaru、Dovetail | 独立搜索曲线 |

---

## 词汇锚点

- **AI Design Tool / AI 设计工具（上位概念）**：利用 LLM 和生成式 AI 辅助产品设计流程的工具总称——覆盖从低保真结构图（wireframing）、高保真界面生成（UI design）、可点击交互原型（prototyping）、到体验组织与系统治理（UX design）的完整流程。五个子品类各有独立的产品集、买家角色和搜索意图。
- **Vibe Design**：与 Vibe Coding 平行的概念——用自然语言描述想要的设计效果，AI 生成对应的 UI。Google Stitch 2026 年 3 月大改版时将此概念推向主流。
- **Connected Canvas / 连接式画布**：2026 年设计工具的范式转变——设计画布通过 MCP 等协议与开发环境实时连接，打破"设计→开发"的单向交接。详见 [`ui-design.md`](./ui-design.md)。
- **Design Fidelity Spectrum（保真度光谱）**：Wireframe（结构）→ Mockup（视觉）→ Prototype（行为）是设计流程的三阶递进。UX Design（体验组织）横跨整个光谱——从 IA 和流程定义（早期）到设计系统治理（贯穿）到无障碍合规（后期）。跳过线框直接出高保真是行业共识中的最常见错误，但在 AI 能以秒速生成高保真 UI 的 2026 年，这条原则正在被挑战。
- **与相邻品类的边界**：AI Design 工具输出设计稿或组件代码，不覆盖后端/数据库/部署——那是 [`app-builder`](./app-builder.md) 的领域。AI Design 工具做视觉、交互和体验治理，不做用户访谈和合成用户测试——那是 [`user-research`](./user-research.md) 的领域。与 [`vibe-coding`](./vibe-coding.md) 有重叠区（自然语言→可运行应用 vs 自然语言→UI 设计稿），但买家角色不同。

---

## 问题域（为何会出现这类产品）

- **设计效率的物理上限**：传统设计流程中，从需求文档到低保真线框到高保真 mockup 到可点击原型，每一步都需要大量手动工作。AI 将「想法→可见设计」的时延从数天压缩至数分钟。
- **设计系统维护成本高**：中大型产品的 Design Tokens、组件库、品牌变量需要跨平台同步——AI 辅助设计系统治理（自动检测不一致、生成变体、无障碍合规检查）从「锦上添花」变为「必需品」。
- **设计师与开发的交接摩擦**：设计稿→代码的传统单向交接产生大量沟通成本和实现偏差——Connected Canvas 和 MCP 协议正在将这一流程变为双向实时同步。
- **非设计师的设计需求爆发**：创始人、产品经理、营销人员都需要产出设计稿——Vibe Design 和 AI UI 生成器降低了「能出图」的门槛，但「出好图」仍需设计素养。
- **无障碍合规的硬性要求**：EAA 2025（2025 年 6 月生效）将无障碍从「加分项」变为欧洲市场的「法律准入门槛」——AI 辅助无障碍检查成为设计工具的必备能力而非差异化卖点。

---

## 子品类分流依据

2026 年 Google 搜索生态中，"best wireframing tools""best prototyping tools""best AI UI design tools""best AI UX design tools""best user research tools"各自返回**独立且不重叠的排名页面集合**。Balsamiq 和 Whimsical 主战"wireframing"搜索，ProtoPie 和 Axure 主战"prototyping"搜索，Stitch 和 Uizard 主战"AI UI design"搜索，Stark 和 Zeroheight 主战"AI UX design"搜索，Outset 和 ListenLabs 主战"user research"搜索。这不是内容策略的选择，而是搜索引擎对用户意图的底层理解——它认为搜这些词的人想要不同的东西。

同样，G2 将 Wireframing 和 Prototyping 列为独立类别；ProductHunt 将 Interface Design Tools 和 User Experience 列为独立主题；ProtoPie 在 2026 年 2 月发文中将 UI 生成 / 代码生成 / 交互原型定义为三个互不重叠的品类；Veza Digital 将"设计系统感知"定义为 2026 年 UX 设计工具的评价分水岭。行业结构已形成共识。

---

## 交叉引用

- **Wireframing（线框图）** → [`wireframing.md`](./wireframing.md)：低保真结构工具——Balsamiq、Whimsical、Wireframe.cc、Moqups、Miro（线框模式）、MockFlow
- **UI Design（界面设计）** → [`ui-design.md`](./ui-design.md)：AI 界面生成工具——Stitch、Uizard、Figma AI、Visily、Motiff、Banani、UX Pilot、Pixso、Pencil、Paper、v0、Galileo AI、Claude Design、Magic Patterns、Anima
- **Prototyping（交互原型）** → [`prototyping.md`](./prototyping.md)：高保真交互原型工具——ProtoPie、Axure RP、Alloy、UXPin Merge、Framer、Maze、Quant-UX、Principle、Claude Design
- **UX Design（体验设计）** → [`ux-design.md`](./ux-design.md)：信息架构 / 用户流程 / 无障碍 / 设计系统 / UX 写作——Flowstep、Stark、Zeroheight、Figr AI、Frontitude、Magic Patterns（设计系统侧）、Figma Dev Mode、UXcelerator.ai、**getdesign.md**（Agent 向 DESIGN.md 目录）
- **User Research（用户研究）** → [`user-research.md`](./user-research.md)：AI 主持访谈 / 合成用户 / 主题分析——Outset、ListenLabs、Conveo、Aaru、Dovetail
- **相邻品类**：`app-builder`（应用搭建）、`website-builder`（AI 建站）、`vibe-coding`（氛围编程）、`logo-generator`（Logo 生成）、`presentation-maker`（演示文稿）

---

## 能力栈（跨子品类的通用能力，非厂商功能表）

- **自然语言 → 视觉输出**：从文本描述直接生成 UI 界面、线框图或交互原型——各子品类在保真度（低保真 vs 高保真）和输出格式（静态图 vs 可交互原型）上有本质差异。
- **设计系统感知**：AI 是否理解并遵循已有设计系统（Design Tokens、组件库、品牌变量），而非每次从零生成——2026 年 Veza Digital 将此定义为 UX 工具评价分水岭。
- **迭代与版本控制**：AI 辅助的"改这个按钮颜色""把整站字体换成 Inter"类自然语言迭代；部分工具支持设计版本分支与 diff。
- **代码输出**：从设计稿直接导出生产级代码（React/Vue/HTML），v0、Galileo AI、Claude Design 在此路径上竞争；与 `vibe-coding` 和 `app-builder` 有交叉。
- **无障碍检查**：自动检测对比度、焦点顺序、屏幕阅读器兼容性——EAA 2025 合规推动此类能力从"加分项"变为"准入门槛"。
- **协作与交接**：设计稿 → 开发的交接——MCP 协议和 Connected Canvas 正在将单向"导出 PNG → 开发对照"变为双向实时同步。
- **用户流程模拟**：AI 模拟用户点击路径、预测困惑点——介于 prototyping 和 UX design 的交叉地带。

---

## 形态谱系（与具体品牌解耦）

- **AI 线框图工具**：低保真、快速结构探索——Balsamiq、Whimsical 系；AI 在此多用于"从 prompt 直接出布局方案"而非像素级生成。
- **AI UI 生成器**：从文本或截图生成高保真界面——Stitch、Uizard、v0 系；2026 年竞争焦点从"能不能生成"转向"生成结果是否遵循设计系统"。
- **AI 原型工具**：生成可点击、可交互动画的高保真原型——ProtoPie、Axure 系；AI 在此辅助交互逻辑定义和条件分支设置。
- **AI UX 治理工具**：信息架构、无障碍、设计系统、UX 写作——Stark、Zeroheight 系；重"系统"而非"单页"，买家通常是设计系统团队。Agent 向 **DESIGN.md 目录**（[getdesign.md](https://getdesign.md/)）面向 vibe coder，见 [`ux-design.md`](./ux-design.md)。
- **AI 用户研究工具**：主持访谈、合成用户、主题分析——Outset、Dovetail 系；与设计工具的交界是"研究 → 设计决策"的闭环。
- **嵌入式 AI 插件**：在 Figma/Sketch 等已有工具内叠加 AI 能力——不替换平台，做增强层。
- **全栈设计 → 代码平台**：从设计直接出可部署应用——与 `app-builder` 品类有重叠，区分在于是否覆盖后端/数据库。

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Figma · AI 功能更新** | Figma 官方 AI 设计功能与社区插件动态 | [figma.com](https://www.figma.com/ai/) |
| **Stitch · Google 设计工具** | Google 2026 年 3 月大改版的 AI 设计生成工具 | [stitch.google](https://stitch.google/) |
| **Claude Design · Anthropic** | Anthropic 2026 年 4 月发布的 AI 设计能力 | [anthropic.com](https://www.anthropic.com/) |
| **G2 · Wireframing & Prototyping 独立分类** | 行业分类体系——线框图与原型为独立品类 | [g2.com](https://www.g2.com/) |
| **ProductHunt · Interface Design & UX 主题** | 产品社区分类——界面设计与用户体验为独立主题 | [producthunt.com](https://www.producthunt.com/) |
| **Veza Digital · 设计系统感知 2026** | 将设计系统感知定义为 UX 工具评价分水岭的行业分析 | 见各子品类外链 |
| **EAA 2025 · 欧洲无障碍法案** | 2025 年 6 月生效，推动无障碍检查从加分项变为准入门槛 | 见 EU 官方公报 |

---

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **EAA 2025 合规**：欧洲无障碍法案要求面向欧盟市场的数字产品满足 WCAG 2.1 AA 标准——AI 生成的设计稿不自动等于合规，需人工或工具验证对比度、焦点顺序、屏幕阅读器兼容性。
- **设计系统锁定**：部分 AI 设计工具生成的组件与特定平台（Figma/v0/Stitch）绑定——导出到其他工具的 fidelity loss 是选型前必须验证的。
- **版权与训练数据**：AI UI 生成器的训练数据可能包含受版权保护的界面设计——生成结果是否构成衍生作品，在不同司法辖区尚无统一判例。
- **品牌一致性**：AI 生成的界面可能偏离品牌指南——生产环境中需叠加设计系统校验层，而非完全信任 AI 输出。

---

## 落地碎片（无先后）

- 先定保真度需求：需要探索信息架构 → wireframing；需要确定视觉方向 → UI design；需要验证交互逻辑 → prototyping；需要治理和系统 → UX design。
- 企业选型时优先确认**设计系统感知能力**——工具是否理解你的 Design Tokens 和组件库，决定了从「生成 demo」到「生产可用」的距离。
- POC 用最复杂的 3 个页面测试（含表单、数据表格、响应式断点）——demo 首页通常过于简单。
- 欧洲市场产品选型时将**无障碍检查**作为硬性门槛而非加分项——EAA 合规不是可选的。

## 市场背景

2026 年 AI 设计工具市场规模约 $82 亿美元（CAGR 22%），生成式 AI 设计子市场 $15.2 亿美元（CAGR 37.5%）。2025 年 8 月 GPT-5 发布后，Google Trends 上所有 AI 设计相关搜索词同时触及指数 100，随后维持高位——不是短期脉冲，是品类级增长。

Figma 股价 2026 年 YTD 下跌约 35%，市场在定价"AI 原生设计工具可能蚕食传统协作设计平台"。Anthropic 2026 年 4 月发布的 Claude Design 和 Google 2026 年 3 月 Stitch 大改版是 AI 设计工具竞争白热化的两个标志性事件。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`design`（本页）** | **`ui-design`** | **`wireframing`** | **`logo-generator`** | **`app-builder`** |
|------|-----------------------|-----------------|--------------------|-----------------------|--------------------|
| **典型买家问题** | 「用 AI 做设计，有哪些工具？」 | 「用 prompt 生成 UI 界面？」 | 「页面结构怎么排？」 | 「给我做一个 logo」 | 「用 AI 搭一个完整应用？」 |
| **核心产出** | 子品类导航与选型指引 | 高保真 UI 界面设计稿 | 低保真结构布局图 | 品牌 Logo 图形 | 可部署的全栈应用 |
| **用户画像** | 设计负责人 / 产品经理 | UI 设计师 / 产品设计师 | 产品经理 / 信息架构师 | 创业者 / 品牌负责人 | 非技术创始人 / 独立开发者 |

---

## 工具与产品类型

| 类型（英文常检索词） | 代表工具 | 深入阅读 |
|---------------------|---------|----------|
| AI UI 界面设计 | Figma AI, Uizard, v0, Visily, Stitch | [ui-design.md](./ui-design.md) |
| AI 线框图/结构设计 | Balsamiq, Whimsical, Wireframe.cc | [wireframing.md](./wireframing.md) |
| AI 交互原型 | ProtoPie, Axure RP, Alloy | [prototyping.md](./prototyping.md) |
| AI UX 体验设计 | Maze, Attention Insight | [ux-design.md](./ux-design.md) |
| AI 用户研究 | UserTesting AI, Dovetail | [user-research.md](./user-research.md) |

## 对比与测评（第三方；观点非官方）

2026 年 AI 设计工具品类的核心张力在三个维度：(1) **平台原生 vs AI 原生**——Figma 以既有生态和设计系统壁垒防御，Stitch/Uizard/v0 以 AI-first 体验进攻；(2) **设计→代码一步到位 vs 设计稿留设计**——v0/Galileo AI/Claude Design 可直接出生产代码，Figma/Stitch 侧重设计稿输出；(3) **通用设计 vs 垂直场景**——Magic Patterns（落地页）、Banani（移动端）等垂直工具在特定场景的深度超过通用工具。社区共识是 2026 年尚无单一工具覆盖全流程——最佳实践是按设计阶段（wireframing → UI → prototyping → UX 治理）分工具组合。*网摘综合，非 Alignify 实测。*

---

## 延伸阅读与参考材料

- **Wireframing**：[wireframing.md](./wireframing.md)——低保真结构工具谱系
- **UI Design**：[ui-design.md](./ui-design.md)——AI 界面生成工具谱系
- **Prototyping**：[prototyping.md](./prototyping.md)——高保真交互原型工具谱系
- **UX Design**：[ux-design.md](./ux-design.md)——体验组织与系统治理工具
- **User Research**：[user-research.md](./user-research.md)——AI 用户研究工具谱系
