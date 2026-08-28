# Prototyping（AI 交互原型）· 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、学术可用性评测、行业对比文与社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页时对齐（slug **`prototyping`** 待 `tools-pages-config` 收录）。

**与相邻 slug 分流**：见下表；三个知识块各自覆盖**不同的产品集和搜索意图**，互不重叠。

| slug | 核心问题 | 典型产品 | 保真度 |
|------|---------|---------|--------|
| [`wireframing`](wireframing.md) | "东西该放哪？信息架构怎么走？" | Balsamiq、Whimsical、Wireframe.cc | 刻意低保真 |
| [`ui-design`](ui-design.md) | "界面长什么样？从 prompt 生成完整 UI" | Stitch、Uizard、Figma AI、Visily 等 | 中→高保真 |
| **`prototyping`**（本页） | "交互行为怎么定义？用户真的能用吗？" | ProtoPie、Axure RP、Alloy、UXPin Merge | 高保真可交互 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Prototype / 交互原型**：可点击、可交互的**行为模拟**——用户能真实地点击按钮、填写表单、体验页面跳转和动画过渡。与静态设计稿的本质区别是：原型回答的是"这个设计用起来怎么样"，而不是"这个设计看起来怎么样"。
- **High-Fidelity Interactive / 高保真可交互**：2026 年原型的竞争焦点已从"能不能点击"升级到"交互有多真实"——传感器触发（陀螺仪、语音）、条件分支（if-else 逻辑）、变量与状态管理、公式驱动动画。ProtoPie 是这个维度的定义者。
- **Wireframe vs Prototype**：线框图测试结构（东西放对了吗），原型测试行为（用户真的能用吗）。线框阶段 2 天能发现的问题，高保真阶段修复成本是其 5-10 倍；但线框阶段**无法**发现交互摩擦——交互问题只能通过可点击原型暴露。二者是递进而非替代关系。
- **Prototyping ≠ Code Generation**：原型工具输出的是**模拟交互**（点击→跳转、条件→展示、变量→状态切换），不是生产代码。代码生成工具（Lovable、Bolt）输出可部署应用，属于 App Builder 品类。但 2026 年边界在模糊——Claude Design 输出的原型能直接作为代码交付，Alloy 在已有产品上叠加的原型能导回开发环境。
- **AI Prototyping**：2025-2026 年 AI 进入原型交互层——自然语言描述交互逻辑（"点击这个按钮后弹出一个带有模糊背景的模态框"）→ AI 自动生成触发条件、动画曲线和变量绑定。ProtoPie AI（2026-02 beta）和 Claude Design（2026-04）是两种不同范式的代表：前者 AI 生成**可编辑的行为蓝图**，后者把原型本身变成代码。

---

## 交互原型作为独立品类——2026 年的品类定义

ProtoPie 在 2026 年 2 月的一篇分析文章中将当前设计工具市场明确拆成三个互不重叠的品类：

| 品类 | 核心问题 | AI 的角色 | 代表 |
|------|---------|----------|------|
| **UI-Focused Tools** | 界面长什么样 | 加速视觉探索 | Figma AI、Framer AI、Stitch |
| **Code-Gen / App Builders** | 怎么变成可运行应用 | 全栈生成 | v0、Lovable、Bolt |
| **Interaction-First Tools**（本页） | 交互行为怎么定义 | 生成**可编辑的**交互逻辑 | ProtoPie、Axure RP、Alloy |

品类定义文章的核心论点：*"Generation is now democratised across tools. The differentiator is refinement — prompt-based iteration vs. direct manual control."* 翻译：AI 生成已普适化。真正的分水岭是**精细化控制**——你是靠反复修改 prompt 来逼近目标，还是在一个可编辑的行为模型上直接操控时间曲线、条件分支和变量。

这个三品类拆分已被 Data Science Dojo 的 Claude Design vs Google Stitch 对比文章引用，说明正在成为行业共识框架。

---

## 问题域（为何会出现这类产品）

- **静态设计无法验证交互流程**：一个"看起来很好"的页面在真实点击时可能暴露导航歧义、信息层级混乱、反馈缺失等问题——这些只有可点击原型能暴露。Jakob Nielsen 的经典结论"5 个用户测试能发现约 85% 的可用性问题"依赖的就是可交互原型。
- **工程师和设计师对"交互细节"的理解天然存在鸿沟**：设计稿上的"点击后展开"在实现时至少有 5 种不同的动画曲线、3 种不同的展开方向、2 种不同的遮罩交互——原型工具的动画时间轴和条件面板消除了这些歧义。
- **投资人/利益相关者需要"看起来真实"的演示**：线框图无法传达产品愿景，静态设计稿无法展示"为什么这个产品是活的"。高保真可点击原型是 Demo Day 和客户演示的标准交付物。
- **可用性测试需要可控的测试环境**：去掉真实后端的不确定性，让测试者聚焦在界面逻辑本身。专业原型工具（ProtoPie、Axure）支持 A/B 变体、任务路径追踪和测试录像标注，这是通用设计工具不具备的。
- **AI 加速了低保真→高保真原型的跳跃**：当 AI 能在一分钟内生成多个可点击方案时，原型的价值从"生产"转向"选择与精细化"——设计师的工作从"做原型"变成"在多个 AI 生成的方案中选择并优化交互细节"。

---

## 能力栈（概念拆分，非厂商功能表）

- **条件逻辑与变量**：if-else 分支、用户输入变量存储、状态切换——这是原型交互的骨架。Axure RP 在此维度历史最久、能力最深。
- **传感器与设备 API 触发**：调用设备陀螺仪、麦克风、摄像头、GPS 数据作为交互触发器——ProtoPie 是此维度的标杆（支持倾斜触发、语音指令、NFC 模拟）。
- **动画曲线与时间轴**：缓动函数（ease-in-out、spring、bounce）、关键帧序列、延迟与循环——决定一个交互是"能用"还是"好用"。Framer 在此维度最成熟。
- **跨设备同步**：手机原型 + 手表原型 + 电视原型的联动交互——ProtoPie 的核心差异化能力。
- **AI 生成交互逻辑**：自然语言描述交互需求 → AI 生成条件-触发-响应链 → 人在可视化编辑器里微调。2026 年 ProtoPie AI（beta）和 Claude Design 代表了两种方向：前者保留完整的可编辑行为模型，后者直接将原型映射为代码。
- **用户测试集成**：原型内置任务脚本、屏幕录制、热力图、A/B 变体分发——Maze 和 Quant-UX 在此维度聚焦。
- **已有产品叠加原型**：不从头画设计稿，而是在现有线上产品的 UI 上直接叠加新功能的原型——Alloy 是这个细分方向的唯一代表（浏览器扩展抓取现有 UI → 自然语言添加新功能层）。

---

## 形态谱系（与具体品牌解耦）

- **交互逻辑引擎型**：核心是"行为编辑"而非"视觉编辑"——提供可编辑的触发-条件-响应链、变量面板和时间轴。ProtoPie 和 Axure RP 在此象限。买家是交互设计师和信息架构师，不是视觉设计师。
- **已有产品叠加型**：不做从零画 UI 这件事——在现有产品上叠加原型层，保持与生产环境一致的视觉。Alloy 在此象限。买家是需要快速验证新功能的产品团队。
- **设计→代码桥接型**：原型不是终点——生成的原型直接输出为可合并的代码（或完整的前端工程）。UXPin Merge 和 Claude Design 在此象限。买家是追求"原型不扔掉"的设计-工程混合团队。
- **测试平台整合型**：核心价值不在"做原型"而在"测试原型"——内置了可用性测试、热力图分析、任务完成率追踪。Maze 和 Quant-UX 在此象限。买家是 UX 研究员。
- **通用设计工具的交互模式**：Figma 和 Framer 的原型功能属于此类——交互能力是完整设计工具的一个模式，而非独立产品。覆盖 80% 的常见交互场景，但条件分支、传感器、变量等高级能力弱于专用工具。

---

## 工具与产品类型（检索里常与 prototyping 同框的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 主轴（本笔记） |
|----------------------|--------------|----------------|
| **Interaction-first prototyping** | 可编辑行为模型、传感器、变量、条件分支 | 核心品类——ProtoPie、Axure RP |
| **Code-backed prototyping** | 原型输出为生产代码或 live component | 相邻品类——UXPin Merge、Claude Design |
| **Overlay prototyping** | 在现有产品 UI 上叠加原型层 | 新兴品类——Alloy |
| **Testing-integrated prototyping** | 原型 + 内置可用性测试 | UX 研究向——Maze、Quant-UX |
| **High-fidelity motion prototyping** | 动画曲线、微交互、过渡效果 | 动效向——Framer、Principle |
| **AI app builders**（仅原型阶段使用） | 用 Lovable/Bolt 做可点击原型后丢弃 | 非专用但可用——见 [`vibe-coding.md`](../coding/vibe-coding.md) |

---

## 外链索引（外链；非广告、无排序优先级）

### 工具与产品

| 名称 | 一句话 | URL | 关键特征 |
|------|--------|-----|---------|
| **ProtoPie** | 交互原型领域的定义者——传感器触发、条件分支、公式动画 | [protopie.io](https://www.protopie.io/) | ProtoPie AI（2026-02 beta）自然语言生成交互、可编辑行为蓝图、跨设备同步、从免费到企业版 |
| **Axure RP** | 企业级复杂原型——动态面板、条件逻辑、自适应视图 | [axure.com](https://www.axure.com/) | 最深的条件逻辑能力、内置文档生成与规格说明、学习曲线陡峭、$25/月起 |
| **Alloy** | 在已有线上产品上直接叠加原型 | [alloy.app](https://alloy.app/) | 浏览器扩展抓取现有 UI、自然语言添加新功能层、原型与生产环境视觉一致 |
| **UXPin Merge** | 设计 + 代码组件同步——原型即生产级 UI | [uxpin.com](https://www.uxpin.com/) | React 组件直接导入画布、条件交互与状态管理、设计→开发交接零损耗 |
| **Framer**（原型模式） | 高保真动效原型——网站级交互和动画 | [framer.com](https://www.framer.com/) | 最强的动画曲线控制、接近生产环境的交互体验、偏营销站与落地页 |
| **Maze** | 原型 + 可用性测试一体化——热力图、任务分析、A/B 测试 | [maze.co](https://maze.co/) | 与 Figma/Sketch/Adobe XD 集成、$75/月起、G2 4.7/5 |
| **Quant-UX** | 原型 + 内置用户测试——热力图与交互分析 | [quant-ux.com](https://www.quant-ux.com/) | 开源可选、内建分析而非事后接入、适合 UX 研究团队 |
| **Principle** | Mac 原生动效原型——微交互和过渡动画专精 | [principleformac.com](https://principleformac.com/) | 时间轴驱动、轻量高效、仅 Mac、一次性买断 |
| **Claude Design**（Anthropic） | AI 原生设计环境——原型即代码，设计系统是核心产物 | [anthropic.com](https://www.anthropic.com/) | 2026-04 发布、设计系统为一级 artifact、原型直接映射为 React 代码、工程师可实时 co-design |
| **ProtoPie AI** | ProtoPie 的 AI 层——自然语言生成可编辑交互逻辑 | Beta 中 | 交互蓝图而非黑箱输出、生成后可手动微调所有参数 |

### 对比与测评（第三方；观点非官方）

ProtoPie 2026 年 2 月的官方分析《AI Prototyping Tools: Why Control Matters As Much As Speed》是理解交互原型品类定位的核心文本——它将市场拆成 UI 工具 / 代码生成 / 交互优先三个品类，论证"可编辑行为模型"是交互原型的护城河。

学术维度上，格拉纳达大学（UGR）2026 年发表的论文《From Prompts to High-Fidelity Prototypes: A Usability Evaluation of Generative AI–Driven Prototyping Tools》用标准化 SUS（系统可用性量表）对 Figma（82.86）、Stitch（80.36）、Visily（78.57）、Uizard（67.14）做了可用性评分——这是目前唯一的学术级 AI 原型工具基准。

LiveSession 的《Best Prototyping Tools for 2026》和 Qualaroo 的《18 Best Prototyping Tools for UX/UI Designers in 2026》是两篇面向实践者的工具选型指南，覆盖了从 ProtoPie 到 Axure 到 Maze 的完整谱系。

Data Science Dojo 的 Claude Design vs Google Stitch 对比文章则从"原型即代码 vs 原型即设计"的角度分析了 2026 年的两条路线分歧。

*本小节为网摘与独立作者/社区观点综合，非 Alignify 实测；**不**以各平台厂商自有营销博文为论证主体。*

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **原型 ≠ 可上线产品**：原型工具生成的是模拟交互，不包含后端逻辑、数据持久化、安全层和错误处理。对利益相关者（尤其是非技术背景的人）必须明确传达"这是模拟，不是产品"。Claude Design 等新型工具正在模糊这条线，反而增加了沟通风险。
- **原型测试的生态效度**：实验室环境下 + 指定任务 + 5 个用户 = 发现 85% 可用性问题。但真实使用场景（多任务切换、网络延迟、真实数据输入）会产生额外的摩擦——原型测试的结论需要标注"在什么条件下成立"。
- **AI 生成交互的不可控性**：自然语言描述的交互逻辑可能被 AI 误解（"弹出一个模态框"在 iOS 和 Android 上的原生行为不同）。AI 生成的交互必须经过人工验证——尤其是涉及数据输入、支付流程、权限请求等高风险界面。
- **协作与 IP**：原型文件中包含产品交互逻辑、用户流程和设计决策——使用云端原型工具时确认数据驻留、访问控制和 IP 归属条款。

---

## 落地碎片（无先后）

- 不需要为每个页面做原型。只对**高风险交互流程**做原型——注册/登录、支付流程、核心功能首次使用体验、任何有 3 步以上的表单。其余页面用静态设计稿评审即可。
- 原型测试只招 5 个用户就够——Jakob Nielsen 的经典结论至今有效。多招用户不会发现更多问题，只会重复发现已有问题。把预算花在多做几轮测试，而非每轮多招人。
- ProtoPie 适合做**单个设备上**的精细化交互（传感器、手势、动画）；Axure 适合做**跨页面**的复杂条件逻辑（权限分支、多角色流程）；Alloy 适合做"在现有产品上加一个新功能"的场景——三款工具的适用场景基本不重叠。
- 如果只是验证"用户能不能完成一个简单任务"——一个 Figma 做的可点击原型足够。不需要 ProtoPie 级别的传感器交互。**工具复杂度应与验证目标成正比。**
- AI 生成原型后，至少完成一轮手动微调再进入测试——AI 生成的默认动画曲线和过渡时间几乎总是需要调整。ProtoPie 的"可编辑行为蓝图"哲学比黑箱生成更适合原型工作流。

---

## 延伸阅读与参考材料

- ProtoPie Blog：《AI Prototyping Tools: Why Control Matters As Much As Speed》（2026-02）——交互原型三品类拆分的原始出处
- UGR 学术论文：《From Prompts to High-Fidelity Prototypes: A Usability Evaluation of Generative AI–Driven Prototyping Tools》（2026, MDPI）——Figma/Stitch/Visily/Uizard 的 SUS 可用性评分
- LiveSession：《Best Prototyping Tools for 2026: The Complete Guide for UX Designers》
- Qualaroo：《18 Best Prototyping Tools for UX/UI Designers in 2026》
- Data Science Dojo：《Claude Design vs Google Stitch: AI Design Wars 2026》
- ProtoPie 官方发布：《Introducing ProtoPie AI: Effortless Start, Flawless Finish》（2026-02）
- Builder.io：《A Practical Guide to AI Prototyping》
- UXPin Blog：《Prototype vs. Wireframe vs. Mockup: Key Differences Explained (2026)》
- Balsamiq Blog：《Wireframe vs Mockup vs Prototype: How Teams Decide What to Use and When》——从线框视角看原型的角色
