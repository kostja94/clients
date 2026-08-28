# Canvas Video · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页与官方文档、Product Hunt 条目、行业对比文与社区讨论、Chase Jarvis / House of gAi 等分析师评测）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-24**（簇去重修订）。**主轴词**：**AI video canvas** / **node-based AI video workflow**。


**站内相邻**：[video.md](video.md) · [video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md) · [workflow.md](../agent/workflow.md)

**勿与…混买**：节点画布编排本页；单次 prompt 生视频见 video-generator；通用 n8n 业务自动化见 workflow。

**站内对照**：[alignify.co/tools/canvas-video](https://alignify.co/tools/canvas-video) · [alignify.co/zh/tools/canvas-video](https://alignify.co/zh/tools/canvas-video) · slug **`canvas-video`**（待上线 Tools 页后生效）。

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#canvas-video-tools`](../../product/alignify-keywords-tools.md#canvas-video-tools)）

**关联关键词（跨品类检索术语，本知识块需覆盖但非专属）**：

| 角色 | 英文关键词 / 短语 | 中文关键词 / 短语 |
|------|-------------------|-------------------|
| 核心品类 | AI video canvas, node-based AI video, canvas video generator, visual AI video workflow, AI workflow canvas, node-based video creation | 节点式 AI 视频画布、AI 视频工作流画布、节点式视频生成、AI 可视化视频管线 |
| 架构范式 | node-based workflow, DAG video pipeline, composable AI video, multi-model video chain | 节点工作流、DAG 视频管线、可编排 AI 视频、多模型视频串联 |
| 交互形态 | drag-and-drop video creator, infinite canvas AI video, visual programming video generation | 拖拽式视频生成、无限画布 AI 视频、可视化编程视频生成 |
| 竞品检索 | ComfyUI alternative, n8n video generation, Figma Weave alternative, Krea Nodes alternative, TapNow alternative | ComfyUI 替代品、节点式视频工具、AI 导演 Agent（与 agentic 分流） |
| 相邻品类（分流用） | AI video generator, text-to-video, image-to-video, AI video editor, AI filmmaking, workflow automation | AI 视频生成器、文生视频、图生视频、AI 视频剪辑、AI 电影制作、工作流自动化 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流（品类易混时必读）

本知识块描述的是**以可视化节点画布为交互界面**，用户手动拖拽模型节点、连线构建多步视频生成管线的工具。它不是"输入一句话出一个视频"的黑箱，也不是"在时间线上剪片子"的传统编辑器。下表厘清与本目录内其他视频相关 slug 的边界：

| slug | 典型买家问题 | 交互范式 | 与本 slug 的边界 |
|------|-------------|---------|------------------|
| **`canvas-video`（本页）** | 「我想把 Gemini 写脚本 → Flux 出图 → Kling 转视频 → ElevenLabs 配音，整个管线在一个画布上串起来，每个环节都能手动调参」 | 可视化节点画布（drag-and-drop nodes + edges）；多模型串联管线；工作流可复用/分享 | — |
| **`video-generator`** | 「给我一句话/一段脚本，出一个能看的视频」 | 单次 prompt → 单段视频输出；无节点编排 | video-generator 是**模型能力层**，本页是**编排层**——把多个 video-generator 模型串成管线 |
| **`text-to-video`** | 「用文字描述，生成一段视频」 | prompt → video；纯文本条件 | 本页的工具**内部调用** text-to-video 模型（Sora、Veo、Kling 等），但价值不在模型本身而在**多步编排** |
| **`image-to-video`** | 「给一张图，让它动起来」 | image + optional prompt → video | 同上——image-to-video 是本页工具管线的**一个步骤节点**，而非完整产品形态 |
| **`video-editor`** | 「我要剪辑已有素材，加转场、字幕、调色」 | 时间线编辑器（timeline-based）；操作的是**已有像素** | video-editor 编辑**成品素材**；本页工具**生成新像素**并编排生成流程。Mosaic 跨在两列之间——节点画布 + AI agent 执行剪辑 |
| **`filmmaking`** | 「用 AI 辅助电影级制作的完整流程」 | 覆盖 pre-production 到 post 的全链路工具 | filmmaking 是**领域应用层**（剧本、分镜、选角、后期）；本页是**工具形态层**（画布式编排）。Flora 的 Story Analysis 跨在两列之间 |
| **`workflow`** | 「让 A 应用的数据自动同步到 B，并在 C 发通知」 | 可视化/低代码工作流编辑器；SaaS 集成自动化 | workflow（n8n、Zapier、Make）是**通用业务自动化**；本页是**创意媒体生成专用**。二者在 n8n+ComfyUI 集成场景有交集 |
| **`image-generator`** | 「生成一张高质量的图片」 | prompt → image；单次生成 | 本页的管线通常以 image-generator 模型为**中间步骤**（先出图→再转视频），但核心价值在**多步串联**而非单图质量 |

---

## 词汇锚点

- **AI video canvas / 节点式 AI 视频画布（本知识块的主标签）**：以**可视化节点画布**为交互界面的 AI 视频生成工具品类。用户在画布上拖放功能节点（文本→图像→视频→音频→导出），以连线定义数据流，构建**可复用、可分支、可共享**的多步视频生成管线。英文检索常混用 **node-based AI video workflow**、**generative AI canvas**、**infinite canvas for AI video**；中文尚无统一品类词，**节点式 AI 视频画布** 为本文提议用语。
- **Node / 节点**：画布上的最小功能单元。每个节点执行一个原子操作——调用特定 AI 模型（如 Veo 3.1 做 i2v）、执行传统编辑（裁切/调色/放大）、或控制流程（分支/循环/条件）。节点有明确的**输入端口**和**输出端口**，同类端口之间才能连线（如 IMAGE 输出只能连 IMAGE 输入）。节点式架构的核心价值在于**透明性**（每一步可见可调）和**可复现性**（工作流导出为 JSON 即可异地复现）。
- **DAG（Directed Acyclic Graph / 有向无环图）**：节点式画布的底层数据结构。数据从上游节点向下游**单向流动**，不允许循环回路。ComfyUI 是 DAG 范式在 AI 图像/视频领域最成熟的实现——其 JSON 格式的工作流文件成为事实上的跨平台交换标准。
- **Canvas / 画布**：区别于线性表单或聊天界面的**空间化交互**范式。用户在二维平面上自由排布节点位置，用连线表达逻辑关系，通过缩放/平移导航复杂管线。画布范式起源于 3D/VFX 软件（Houdini、Nuke、Blender Nodes），2025–2026 年被 AI 创意工具大规模采纳。与 "infinite canvas"（无限画布）的区别：后者更强调空间无边界的 UX 特征，前者强调节点连线的编排能力——二者高度重叠但不完全等同。
- **Agentic video generator / 智能体式视频生成器**：本知识块覆盖谱系中「自动化程度最高」的一端。与节点式画布的**手工编排**不同，agentic 工具由 AI agent 自主决定生成步骤——用户输入一段创意梗概，agent 自动完成剧本、分镜、模型选择、多镜头生成、剪辑合成全流程。代表：Zopia、UniVA、Grok Imagine Agent。与节点式不是对立关系，而是**人工控制 ↔ 自动化**光谱的两端，且部分产品（Mosaic）同时提供两种模式。
- **Model-agnostic / 模型无关**：节点画布工具的共同设计原则——不绑定单一 AI 模型，而是通过统一接口接入多个提供商的模型（OpenAI、Google、Kuaishou、ByteDance 等），让用户在同一画布内 A/B 对比不同模型输出。Figma Weave 和 AICRON 都宣称"all major models in one canvas"。与此相对的是模型原生产品（如 Runway 主要用自己的 Gen-3/Gen-4 模型）。
- **Reference anchoring / 角色锚定**：视频管线中的关键难题——跨多镜头保持同一角色的外貌、服装、光影一致。节点式工具通过 **Ref Node**（参考节点）实现：将角色/产品的参考图上传为持久化节点，下游生成节点自动从上游 Ref 读取视觉特征并注入 prompt。Flowboard 的 Ref 节点、Flora 的 Character Reference、TwitCanva 的种子锁定都是此模式的变体。
- **Multi-source batching / 多源批处理**：节点式工具的典型效率优势——一个 image 节点生成 4 个姿势变体，下游 video 节点一次调用将 4 张静态图转为 4 段不同视频（而非人工逐张处理）。这是画布编排相对于"逐次 prompt 抽卡"的核心生产力差异。

---

## 专题对照 / 扩展定义

本笔记用法：厘清「节点式画布 vs agentic 自动化 vs 简单 prompt 生视频」三者的分界。

| 维度 | **Node-based canvas（本页主轴）** | **Agentic video generator** | **Single-prompt video** |
|------|----------------------------------|----------------------------|------------------------|
| **交互范式** | 手工拖拽节点 + 连线 | 自然语言对话，Agent 自主规划 | 输入 prompt/图片，点生成 |
| **控制粒度** | 每个步骤的参数都可调 | 粗粒度——「要改第三幕的光线」 | 无步骤概念——重新生成 |
| **可复现性** | 极高——导出 JSON 工作流 | 低——Agent 决策路径不透明 | 无——每次独立抽卡 |
| **学习曲线** | 陡峭（需理解模型链路） | 低（对话即可） | 最低 |
| **代表** | ComfyUI, Figma Weave, Krea Nodes, TapNow, OpenCreator, Flora | Zopia, UniVA, Grok Imagine Agent | Runway 原生界面, Pika, Luma Dream Machine |
| **适合谁** | 专业创作者、工作室、需要管线化的团队 | 短剧批量生产、MCN、非技术创作者 | 快速概念验证、个人用户 |

**光谱定位**（从左到右 = 人工控制增强 → 自动化增强）：

```
ComfyUI ── Figma Weave ── Krea Nodes ── TapNow/OpenCreator ── Flora ── Mosaic ── Zopia ── Grok Imagine Agent
   ↑                                           ↑                        ↑            ↑
 极致控制                               社区+管线复用              叙事导向      全自动Agent
```

---

## 问题域（为何会出现这类产品）

- **"黑箱抽卡"疲劳**：单 prompt 生视频的体验类似老虎机——无法复现好结果、无法局部修改不满意的部分、无法复用成功的工作流。节点式画布将视频生成从**赌博式**变为**工程式**。
- **多模型碎片化**：2025–2026 年视频生成模型爆发——Sora 2、Veo 3.1、Kling 2.6/3.0、Seedance、Hailuo、Wan 2.6、Runway Gen-4——每个模型有其独特的优势和短板。节点式画布以 model-agnostic 原则统一调度，让创作者在同一界面内组合最优模型链。
- **专业创作需要管线**：真正的视频制作从来不是"一步到位"——剧本→分镜→关键帧→逐镜头生成→配音→剪辑→调色。节点式工具把这条专业管线**可视化**和**可复用化**，而非把它压缩成一个黑箱按钮。
- **团队协作与工作流资产化**：画布上的工作流可以保存为模板、分享给团队、被他人复现。TapNow 的 TapTV 社区（12 万+公开工作流）、Figma Weave 的 App Mode（将复杂画布发布为简单工具）都在把"编排能力"从个人技能转化为**组织资产**。
- **ComfyUI 的验证与门槛矛盾**：ComfyUI 证明了节点式 AI 生成的强大——开源、可扩展、透明。但它的学习曲线让非技术创作者望而却步。2025–2026 年涌现的云端画布工具（Figma Weave、Freepik Spaces、Krea Nodes）本质上是在做同一件事：**把 ComfyUI 的能力装进可访问的 UI**。
- **Figma × Adobe 品类定义竞赛**：Figma 收购 Weavy（~$200M）和 Adobe 推出 Project Graph 在 2025 年 Q4 仅隔数周发生。这标志着节点式 AI 画布从极客工具升级为**主流创意基础设施**——两家最大的设计工具公司用真金白银确认了这个品类。

---

## 能力栈（概念拆分，非厂商功能表）

- **节点粒度**：从粗粒度（一个节点 = 整个"文生视频"，如 AICRON）到细粒度（一个节点 = VAE 解码器，如 ComfyUI）。产品定位差异体现在粒度选择上——面向非技术用户的产品倾向粗粒度封装，面向 power user 的产品暴露更多底层控制。
- **模型接入广度**：从仅接入自有模型（Runway Workflows 主用 Gen-4）到 model-agnostic 接入 200+ 模型（Figma Weave、AICRON、Flora）。广度不等于质量——关键在节点封装是否暴露了模型的核心参数（种子、步数、CFG、运动强度等）。
- **条件模态串联**：文本→图像、图像+文本→视频、视频→视频（风格迁移）、音频→口型同步。节点式画布的价值在**跨模态串联**——上游图像节点的风格参数自动传导到下游视频节点的 prompt。
- **角色/主体一致性**：单镜头内一致（同帧不换脸）vs 跨镜头一致（多镜头同角色）。实现路径包括 Ref Node 锚定（Flowboard）、种子+风格后缀锁定（TwitCanva）、LLM 辅助 prompt 一致性（OpenCreator 的上下文感知提示词合成）。
- **分支与 A/B 测试**：同一上游节点分叉到不同模型/参数的下游节点，并行生成多版本对比。Flora 的 Branching Workflows 和 OpenCreator 的多轮结果对比是典型实现。
- **部分重跑与增量迭代**：修改管线中间某一节点后仅重跑受影响的下游，而非整条管线重新执行。OpenCreator 的局部重跑和 ComfyUI 的缓存机制均属此能力。
- **工作流资产化**：导出为 JSON/模板文件、分享到社区、克隆他人工作流。TapNow 的 TapTV（12 万+工作流）和 Freepik Spaces 的模板市场代表了两种不同的资产化路径——社区 UGC vs 平台精选。
- **协作层级**：单人画布 → 实时多人协作（Freepik Spaces、Flora）→ 团队工作空间 + 角色权限（Figma Weave Enterprise）。协作层级决定了工具面向个人创作者还是机构客户。
- **App Mode / 工具发布**：将复杂画布封装为简化 UI，供非技术团队成员使用。Figma Weave 的 App Mode 是本维度的开创者。这本质上是将"画布编排者"和"画布使用者"两个角色解耦。
- **Agent 辅助编排**：AI 辅助搭建工作流——自然语言描述意图，agent 自动生成节点图。Krea 2026 年推出的 Node Agent（自动构建工作流）、Caraca 计划中的 AI assistant 均属此方向。这预示着节点式工具的下一步：从**手动编排**向**半自动编排**演进。

---

## 形态谱系（与具体品牌解耦）

- **Type I：开源引擎型**——ComfyUI。纯节点图，JSON 可序列化，2000+ 社区自定义节点。绝对灵活但绝对陡峭。定位是"AI 生成的 Linux"——power user 的首选，但大众进不来。

- **Type II：云端专业画布型**——Figma Weave、Adobe Firefly Graph。把节点画布搬上云端，整合主流模型 + 专业编辑工具（遮罩/图层/修复/重新打光），面向专业创作者和团队。核心竞争力是生态集成（Figma CC / Adobe CC）和 App Mode 降低使用门槛。

- **Type III：云端大众画布型**——Freepik Spaces、Krea Nodes、AICRON。定位"ComfyUI for the masses"——云托管、无 GPU 需求、上手快。通常牺牲部分底层控制以换取简易性。Freepik 以素材库为差异化，Krea 以实时生成为差异化，AICRON 以内置视频编辑为差异化。

- **Type IV：社区工作流型**——TapNow、OpenCreator（及国内的 Vidoo、Seko 等）。核心价值在**工作流资产化**——用户可以一键克隆他人的完整项目。中文社区生态活跃，集成国产模型（Kling、Seedance、即梦等）深度优于西方竞品。面向电商、广告、短剧等商业场景。

- **Type V：叙事/分镜优先型**——Flora。画布服务于**故事板构建**而非纯技术管线。从剧本分析到角色一致到场景分镜，AI 辅助叙事是核心竞争力。$42M 融资（Redpoint，2026 年 1 月）验证了"创意过程 SaaS"的投资逻辑。

- **Type VI：Agentic 混合型**——Mosaic、Zopia。同时提供节点画布和 AI agent 自动执行两种模式。Mosaic 的 Tiles（节点）+ Agents（自动执行剪辑）是混合范式的代表——用户可以手工搭建流程，也可以让 agent 全部代劳。Zopia 更偏纯 agentic 端。

- **Type VII：开源 BYOK 型**——Caraca、Vibe Workflow、TwitCanva、Flowboard。开源 + 自带 API Key。面向想在节点画布上工作但不想被厂商锁定和订阅费捆绑的开发者/技术创作者。2025–2026 年的增长反映了对 Figma/Adobe 云垄断的反制需求。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **模型授权与商用合规**：节点画布聚合多家模型 API，每个模型的商用条款、训练数据授权、输出所有权声明各不相同。用户在一个工作流中可能同时调用商用友好模型（Adobe Firefly 含版权赔偿）和高版权风险模型（部分开源模型训练数据未获授权）。平台是否对最终输出的版权状态负责——目前全行业无统一答案。
- **深度伪造与内容审核**：多模型编排降低深度伪造的技术门槛——一条节点管线可以串联"人脸替换 + 视频生成 + 口型同步"，产出高仿真虚假视频。云端画布平台的内容审核策略差异巨大：有的仅做 prompt 过滤（可绕），有的加后验分类器（影响速度），有的完全依赖 API 提供商自身的审核。
- **工作流投毒与供应链安全**：公开工作流社区（如 TapNow 的 TapTV）存在**工作流投毒**风险——恶意节点可能注入隐蔽的 prompt 指令（越狱、品牌诋毁、版权侵犯）或调用未声明的外部 API。工作流作为可执行资产，其安全审计机制尚属空白。
- **数据驻留与 API 密钥管理**：BYOK 型工具（Caraca、TwitCanva 等）需要用户自行管理多家模型提供商的 API 密钥。密钥泄露影响面远超单一服务。云端画布平台虽替用户管理 API 调用，但视频素材的上传和处理意味着用户的原始内容经过平台服务器——数据驻留和删除权成为企业采购的关键阻力。
- **AI 生成标识与溯源**：多模型编排使单一视频的生成链路跨越 3–5 个 AI 模型，C2PA 等内容溯源标准的逐模型签名机制在节点式管线中面临"我应该签哪个节点"的溯源链断裂问题。目前 Adobe Firefly Graph 是唯一在节点级嵌入溯源信息的平台。
- **创作者劳动替代与行业冲击**：节点式工具将传统需要 5–10 人团队（导演、摄影师、剪辑、调色、配音）的视频制作压缩为单人+画布，对广告制作、电商摄影、MCN 内容生产等行业产生直接的劳动力替代效应。

---

## 落地碎片（实践建议）

- 选型第一步是判断**控制需求**：如果你需要调整 VAE、采样器、CFG 等底层参数 → ComfyUI；如果你只是需要"比 prompt 更可控，但不想碰底层" → Krea Nodes 或 Freepik Spaces。
- 如果团队里有非技术成员，优先考虑有 **App Mode** 的产品（目前仅 Figma Weave 提供）——让一个人搭画布，其他人用简化界面操作。
- 电商/广告场景优先看 TapNow 和 OpenCreator——它们对 Kling、Seedance 等国产模型的集成深度优于西方竞品，且社区里有大量可直接复用的商业工作流。
- 开源拥护者从 Caraca 或 Vibe Workflow 开始——前者还在早期但理念对路，后者社区更成熟。
- 不要把 Zopia 当成节点式工具评估——它在光谱的 agentic 端，适合"快速批量出片"而非"精细控制管线"。二者的选型取决于"你要导演的权力还是导演的速度"。
- 测试一个平台时，不要看它宣称接入"多少模型"——看它**暴露了每个模型的哪些参数**。200 个模型但每个只能调 prompt，不如 10 个模型但能调种子+步数+运动强度。

---

## 工具与产品类型（检索词常混在一起的品类）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|-------------|------|
| **Node-based AI video canvas** | ComfyUI, Figma Weave, Krea Nodes, TapNow, OpenCreator, Flora, Freepik Spaces, AICRON, Caraca, Vibe Workflow, TwitCanva, Flowboard | 本知识块的核心品类——可视化节点画布 + 多模型视频编排 |
| **Agentic video generator** | Zopia, UniVA, Grok Imagine Agent, Seko | AI agent 自动完成全流程——从剧本到成片。交互方式是对话而非画布 |
| **Agentic + Canvas hybrid** | Mosaic | 同时提供节点画布（Tiles）和 AI agent 自动执行——跨在两个品类之间 |
| **Single-prompt AI video** | Runway Gen-3/4 原生界面, Pika, Luma Dream Machine, Sora 原生界面 | 单 prompt 或单张图直接出视频；无节点编排概念 |
| **AI video editor** | Descript, Runway 编辑模式, CapCut AI | 时间线编辑 + AI 辅助功能（智能剪裁/字幕/调色）；操作的是已有素材，非生成新像素 |
| **AI filmmaking tool** | LTX Studio, Higgsfield, SkyReels | 电影/短剧全流程（剧本→分镜→选角→后期）；更接近垂直行业方案 |
| **AI music video generator** | Kaiber, Neural Frames, Music Video Generator 类 | 音乐驱动的视频生成；与节点式工具有交叉（部分产品在画布上编排 audio-reactive 管线） |

---

## 外链索引

### 本文重点覆盖产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| Figma Weave | Figma 收购的节点式 AI 创意画布（前身 Weavy），模型无关，App Mode 发布工作流为简易工具，面向专业设计与创意团队 | https://weave.figma.com/ |
| Flora | 无限画布 AI 创意平台（$42M Redpoint 融资），200+ 模型，叙事/分镜优先，实时多人协作，Story Analysis 剧本到分镜 | https://flora.ai/ |
| Krea Nodes | 50+ 模型的实时节点画布，LCM 驱动的低延迟生成（webcam/屏幕实时输入），3,000 万用户，$83M 融资 | https://www.krea.ai/nodes |
| OpenCreator | 国产 AI 视频工作流平台，"原子化解构"方法论，20+ 模型（Sora 2、Veo 3.1、Kling 2.1 Pro 等），时间线编辑器，多轮结果对比，按量付费 | https://opencreator.io/ |
| TapNow | 国产节点式 AI 视频工具（Tapflow 画布），TapTV 社区 12 万+公开工作流可克隆复用，集成本土模型（Gemini 3、Sora 2、Veo 3.1、Kling 等），曾被用于百万级 TVC 广告 | https://www.tapnow.ai/ |
| Zopia | 端到端 AI 视频导演 Agent（非节点式），多 Agent 协作（编剧/分镜/场景/角色/剪辑），对话式交互，"一句话出成片"，24/7 无人值守批量生产 | https://zopia.ai/ |
| Mosaic | YC W25，节点式 AI 视频编辑画布（前 Tesla 工程师），Tiles 功能节点 + AI agent 自动执行，支持并行多版本 A/B 测试，导出 XML 到 Premiere Pro/DaVinci | https://mosaic.so/ |

### 品类内其他值得关注的产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| ComfyUI | 开源节点式 AI 图像/视频引擎，DAG 范式的事实标准，2000+ 社区节点，JSON 工作流可跨平台移植 | https://github.com/comfyanonymous/ComfyUI |
| Freepik Spaces | 云端节点式画布（"大众版 ComfyUI"），36+ 图像模型 + 9+ 视频模型，深度整合 Freepik 素材库，实时多人协作 | https://www.freepik.com/spaces |
| AICRON | 韩国节点式 AI 画布（2026 年 2 月发布），200+ 模型，首个内置视频编辑的画布平台，由韩国电影 VFX 专业人士参与设计 | https://aicron.io/ |
| Caraca | 开源节点编辑器（Product Hunt 上线），定位在 ComfyUI 和 Freepik 之间，fal.ai + OpenRouter 驱动，计划加入 AI 辅助搭建工作流 | https://www.producthunt.com/products/caraca |
| Vibe Workflow | MIT 开源，自部署的节点式 AI 工作流构建器（图像+视频管线），基于 MuAPI/Vadoo AI 后端，对标 Weavy/Krea/Freepik/Flora | https://github.com/SamurAIGPT/Vibe-Workflow |
| TwitCanva | 开源节点式 AI 视频/图像平台，多模型（GPT Image、Gemini、Veo、Kling、Hailuo），LangGraph Agent，运动控制，TikTok/X 直发 | https://www.producthunt.com/products/twitcanva |
| Flowboard | 开源无限画布（AI 产品视频专用），Ref 节点锚定角色/产品一致性，Google Flow（Veo 3.1）+ Claude CLI 自动提示词合成 | https://github.com/crisng95/flowboard |
| Adobe Firefly Graph | Adobe 的节点式创意工作流画布（Project Graph），250+ 节点，Firefly 模型 + CC 编辑工具（PS/AI/PR），企业级治理 | https://helpx.adobe.com/firefly/web/firefly-graph/firefly-graph-overview.html |
| Raelume | 70+ 模型跨六种媒体类型（Image/Video/3D/Audio/Text/WORLDS），独特 WORLDS 功能（2D→3D 高斯泼溅），Veo 3.1 4K 视频 | (官网无公开链接，参阅 Dev.to 对比文) |
| Amaro | 节点式无限画布（2024 年 8 月发布），整合 Runway/Luma/Stability/Black Forest Labs/ElevenLabs/OpenAI，Freemium $5/月起 | https://www.producthunt.com/products/amaro |
| Blooming | 白板式 AI 模型串联工具，文本→图像→视频管线，多模型并行对比，定位类似 "n8n 但专注于 AI 媒体生成" | https://blooming1000.com/ |
| Flowith.io | 无限画布 AI 工作空间（100 万+用户，NVIDIA 支持），通用 AI 工作台 | https://flowith.io/ |
| Segmind PixelFlow | 节点式时尚视频管线：Flux Kontext Max → SegFit 虚拟试穿 → Claude 自动提示词 → SeeDance 视频生成 | https://www.segmind.com/pixelflows |

### 对比与测评（第三方；观点非官方）

- Chase Jarvis 系列对比文章（2025–2026）覆盖 Weavy vs Freepik Spaces、Weavy vs Krea、Weavy vs ComfyUI、Weavy vs Leonardo、Flora vs Raelume 等横向对比——是当前最系统的英语圈品类分析源。
- Dev.to 上 alexmercer_creatives 系列："Krea vs Raelume""Freepik Spaces vs Raelume""Flora vs Raelume""Why AI Workflow Canvas Tools Are the Future"——2026 年 1–3 月发布，偏产品功能拆解。
- House of gAi 博客 "Node-Based AI Tools Explained: Weavy, Flora, and the Future of Creative Workflows"——品类定义级文章，将 Node-Based AI 确立为独立品类。
- AlternativeTo.net 的 "Runway launches node-based Workflows" 新闻条目（2025 年 10 月）和 "Figma acquires Weavy" 条目（2025 年 11 月）——记录了关键行业事件的时间线。
- Product Hunt 上 Caraca、TwitCanva、Amaro、Blooming、Visual Cloner 等产品的条目和社区讨论——反映早期用户的真实反馈。
- The Faces of the Unknown 博客 "The Nodes Are Coming"——从创意专业人士视角分析节点范式对行业的影响。

---

## 延伸阅读 · 站内知识块

- 上游生成：[video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md)
- 并列：[video-editor.md](video-editor.md) · [workflow.md](../agent/workflow.md)

## 延伸阅读 · 站外

- **品类分析**：Chase Jarvis "Best Generative AI Canvas Apps for Creative Professionals"（2026）——横向对比 Weavy/Flora/Freepik/ComfyUI/Leonardo 等 10+ 产品的功能与定位。
- **行业事件**：Figma acquires Weavy 官方博客（2025 年 10 月）；Adobe introduces Project Graph 官方博客（2025 年 11 月）——两周内的两次品类定义事件。
- **开源演进**：ComfyUI 2025 年度报告（blog.comfy.org）——70K+ GitHub Stars，2–3M MAU，55% 专业用户市占率。Subgraph 功能上线（2025 年末）标志着从"单张画布"向"模块化工作流组件"的演进。
- **中国市场**：TapNow 百度百科、OpenCreator 百度百科、Zopia 多篇中文媒体报道（太平洋电脑网、站长之家、i 黑马）——提供中国节点式 AI 视频工具的市场叙事。
- **学术相关**：UniVA 框架论文（多所大学联合发布，2025）——Plan-Act 双智能体架构的通用 AI 视频生成框架，MCP 协议集成。GenFlow 论文（arXiv 2506.21369）——交互式模块化图像生成系统。
- **市场数据**：Forbes "Three New AI Platforms For Cinematic AI Productions"（2025 年 6 月）；a16z 2025 年 3 月 Web Top 50 报告中视频生成品类排名（Hailuo、KlingAI 超过 Sora）。
