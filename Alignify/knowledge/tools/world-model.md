# 世界模型（World Models）· 知识块（非线性笔记）

**材料范围**：公开网络检索（维基百科综述、学界预印本与博文、Google DeepMind / Meta / NVIDIA / Runway / World Labs / 1X / Odyssey / Tencent Hunyuan / Ant Group Robbyant 等公开产品介绍、科技媒体与产业评论）；并归纳「世界模型」在**具身智能、仿真、自动驾驶与交互式生成**语境下的常见用法。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源复述。**具体参数、开源与否与合同条款以各官网与许可证为准**。网摘整理日期 **2026-04-20**，产品刷新日期 **2026-05-10**。

**站内对照**：[alignify.co/tools/world-model](https://alignify.co/tools/world-model) · `/zh/tools/world-model` · `content/tools/en/world-model.md`、`content/tools/zh/world-model.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#world-model-tools`](../../keywords/alignify-keywords-tools.md#world-model-tools)）

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **World model（世界模型）**：在机器学习语境下，指从观测（图像、点云、机器人状态等）学习环境的**内部表征**，并**预测**在动作作用下未来状态如何演化的一类模型；常与**规划、强化学习、仿真**并列讨论，区别于只做分类或单次生成的系统。
- **Latent dynamics / latent space prediction**：在**潜变量空间**而非逐像素重建上预测下一步——降低计算量并鼓励抽象因果结构；与「纯视频扩散」共享工具链但优化目标不同。
- **JEPA（Joint Embedding Predictive Architecture）**：**Yann LeCun** 等推动的范式：编码观测为嵌入，预测器在嵌入空间对齐未来；代表工作含 **V-JEPA** 系列及 **LeWorldModel**（像素端到端 **JEPA** 训练的近期预印本讨论）。
- **World foundation model（WFM / 世界基础模型）**：**NVIDIA Cosmos** 等力推的叙事框架——将世界模型定位为物理 AI 的「基础模型」，上游预训练后供下游机器人、自驾等任务微调；常与 **Predict / Transfer / Reason / Policy** 多组件矩阵绑定。
- **True 3D world model（真3D 世界模型）** vs **video world model（视频世界模型）**：前者输出可编辑 **Mesh / 3DGS / 点云**（如 **Marble**、**HY-World 2.0**），永久持久、可导入游戏引擎；后者输出**视频流**（如 **Genie 3**、**GWM-1**），交互时实时推演但不可编辑几何。二者检索词常混用，采购时需先辨输出形态。
- **Interactive world model API**：2026 年新兴交付形态——世界模型不再仅是论文或闭源 demo，而以 **REST / SDK** 对外服务（如 **Odyssey-2 Max** 的 JS/Python SDK、**World Labs** 的 World API）；采购评估时需关注**推理延迟、并发与按 token / 时长计费**模式。
- **Genie（DeepMind）**：从互联网视频等数据学习**可交互环境**生成的系列模型；**Genie 3**（2026-01 开放公测）支持文本/图片→实时可交互 3D 世界（720p/24fps），但单次交互严格 **60 秒**上限；已衍生 **Waymo World Model**（自驾长尾仿真，双模态 LiDAR+摄像头输出）。
- **Embodied AI / 具身智能**：机器人或虚拟体在环境中**闭环**行动；世界模型常用于**想象 rollout**以减少真实试错成本。
- **Digital twin / 仿真闭环**：自动驾驶、物流、制造里用合成数据喂给规划器或感知训练；**仿真分布**与真实长尾场景是否对齐常是争议点。
- **vs LLM**：主流 **LLM** 以离散 token 预测为主；世界模型多在**连续感知域**建模动态。**混合系统**常见：语言层下达任务，低层策略或仿真由世界模型支撑。
- **vs「纯文生视频」**：同类架构可服务短片生成，但若强调**动作条件、状态一致性与可交互**，检索与采购话术常偏向 **world model / interactive world / physics-aware simulation**。

---

## 专题对照 / 扩展定义

| 维度 | **偏研究与机器人 / 仿真** | **偏生成与互动内容** |
|------|---------------------------|------------------------|
| **典型对象** | 传感器轨迹、操作后果、长尾物理事件 | 可玩环境、连贯场景展开、交互叙事 |
| **验收指标** | 下游控制成功率、仿真覆盖、分布外泛化 | 交互一致性时长、可控性、视觉稳定性 |
| **常与谁相邻** | 自动驾驶仿真、机器人学习、GPU 仿真栈 | 游戏原型、沉浸式预览、生成式关卡 |

| 维度 | **潜空间预测（含 JEPA 路线）** | **高保真像素生成（扩散 / AR 视频）** |
|------|----------------------------------|----------------------------------------|
| **优化重心** | 表征与动力学可迁移、样本效率 | 观感、分辨率与指令跟随 |
| **常见张力** | 可读性与任务对齐 | 物理谬误与长镜头漂移 |

| 维度 | **视频世界模型**（Genie 3 / GWM-1 / Odyssey-2 Max） | **真3D 世界模型**（Marble / HY-World 2.0） |
|------|-------------------------------------------------------|----------------------------------------------|
| **输出形态** | 视频流（不可编辑几何） | Mesh / 3DGS / 点云（可二次编辑） |
| **持久性** | 受推理窗口限（秒~分钟级） | 一次性生成，资产永久保留 |
| **引擎兼容** | 需额外转换或不可导入 | 直接导入 Unity / UE5 / Isaac Sim |
| **推理成本** | 每次交互累积 | 一次性生成，渲染成本≈0 |
| **代表场景** | 实时探索、交互叙事、agent 训练 | 关卡原型、数字孪生、VR 预览 |

---

## 问题域（为何会出现这类产品）

- **真实试错昂贵或危险**：机器人、车、能源设施等场景难以靠无限次物理试验覆盖长尾。
- **数据尺度与多样性**：互联网视频、仿真器日志、车队回传等多源数据推动**自监督**与**跨任务迁移**叙事。
- **生成式交互体验**：需要「一说即有小世界可逛」的创作流，单一短视频模型未必强调**交互闭环**。
- **算力与栈绑定**：大规模视频/点云训练与实时推理常与 **GPU、专用仿真管线**销售故事绑定（厂商生态差异明显）。
- **叙事竞争**：同一时期会出现多条路线——通用交互世界（如 **Genie** 系）、工业仿真（如 **Cosmos** 叙事）、机器人专用世界模型（如 **1XWM**）、创作向视频世界模型（如 **Runway GWM-1**）与表征学习底座（如 **V-JEPA 2**）；**选购需按任务切片，不宜只看「世界模型」标签**。
- **API 化与商业交付**：2026 上半年多家将世界模型从研究 demo 转为 **REST / SDK 产品**（World Labs 的 World API、Odyssey-2 的 JS/Python SDK、Cosmos 的 HuggingFace 开放权重），采购开始关注**延迟 SLA、并发与按量计费**而非仅看论文指标。
- **开源冲击**：**Tencent HY-World 2.0**（2026-04）、**Ant Group LingBot-World**（2026-01）以开源或开放权重进入，直接对标闭源 **Marble** 与 **Genie 3**，改变「世界模型 = 巨头闭源」的早期格局。
- **自动驾驶长尾仿真**：**Waymo World Model**（基于 Genie 3，2026-02）将世界模型用于生成**极端罕见驾驶场景**（龙卷风、大象上路等）并输出双模态传感器数据（摄像头+LiDAR），标志着世界模型从「生成好玩」到「安全验证」的跨越。

---

## 能力栈（概念拆分，非厂商功能表）

- **前向动力学（forward dynamics）**：给定当前状态与动作，预测下一状态或若干步 rollout。
- **逆动力学 / 规划接口**：从目标反推动作序列时常与 **MPC、RL、搜索** 组合；近期具身模型（如 **1XWM**、**X-WAM**）将逆动力学作为独立 **IDM** 模块与视频生成主干解耦。
- **多模态条件**：文本、布局、初始帧、**LiDAR / 相机同步**（自动驾驶仿真常用表述）；**Waymo World Model** 等已实现自然语言指令→双模态传感器输出（RGB+点云）。
- **表征迁移**：视频编码器作为下游检测、预测、控制的**预训练 backbone**；**V-JEPA 2** 验证了仅用 ~62h 无标注机器人视频即可零样本部署至 Franka 机械臂（65–80% 成功率）。
- **交互一致性**：用户在环境中连续操作时的**记忆与物体持久性**（评测常见讨论点）；Genie 3 约 60 秒后一致性衰减，Odyssey-2 Max 宣称 120+ 秒，LingBot-World 宣称近 10 分钟。
- **3D 资产输出**：是否输出可编辑 **Mesh / 3DGS / 点云**，决定了生成结果能否进入游戏引擎或仿真管线做二次加工；**Marble** 与 **HY-World 2.0** 以此为核心差异点。
- **实时推理 API**：商业交付时需关注的维度——**延迟**（1XWM ~11s/次、Genie 3 实时推演但限 60s、LingBot-World <1s 交互延迟）、**并发**、**按 token / 时长 / 调用次数**计费模式。
- **引擎与工具链耦合**：是否与 **Omniverse**、自驾仿真栈、游戏引擎（**Unity / Unreal**）或机器人 SDK 预先集成，显著影响落地摩擦。

---

## 形态谱系（与具体品牌解耦）

- **学术原型与开放权重**：侧重指标与可复现；工程封装程度参差（如 **V-JEPA 2** 开放权重、**Cosmos** 开放模型许可证）。
- **交互式 API 服务**：世界模型以 **REST / SDK** 对外交付，按调用计费——**Odyssey-2 Pro/Max**（JS/Python SDK）、**World Labs World API**（REST，Marble 后端）为此形态代表。
- **云服务 API 或套件**：面向创作者与企业的托管推理与批量渲染。
- **OEM / 垂直栈嵌入**：自动驾驶、机器人厂商将世界模型放进**闭环仿真或数据合成**流水线（**Waymo World Model** 基于 Genie 3、**1XWM** 与 Neo 硬件联动）。
- **真3D 世界模型**：输出 **Mesh / 3DGS** 而非视频——**Marble**、**HY-World 2.0**（开源，直接导入 Unity/UE5）。
- **交互世界生成（视频流）**：强调实时或准实时探索、与文本/图像条件联动（**Genie 3**、**GWM-Worlds**、**LingBot-World**）。
- **表征基础模型**：主打**预训练嵌入**而非直接「生成可玩关卡」。

---

## 风险 · 合规 · 仿真与滥用（外部框架可对照，非法律意见）

- **仿真与现实鸿沟**：长尾场景覆盖不足可导致**过度自信**的安全决策；监管敏感领域需对照行业测试标准（非本页给出具体条款）。**Waymo World Model** 等自驾应用虽能生成极端场景，但生成数据与真实传感器分布的对齐仍需独立验证。
- **视听误导**：高写实合成环境可能被滥用于虚假信息或欺诈场景；平台政策与标识要求因地而异。
- **数据与劳工**：大规模视频训练涉及版权与标注外包伦理争议——引用第三方数据集前应核对许可证。
- **出口与军用敏感**：仿真与无人机/国防叙事相邻时，采购与开源分发可能触及**出口管制**讨论（需专项合规）。
- **环境与能耗**：长时高清 rollout 与大规模训练的云资源消耗常与 **ESG** 披露挂钩。**Genie 3** 每次调用需专用计算芯片全功率运转，**Cosmos** 训练用 10,000 H100 GPU / 20M 小时视频，**1XWM** 推理约 11s/次。
- **API 锁闭与地域限制**：商业 API 常设访问地理围栏——**Genie 3** 仅面向美国 18+ Gemini Ultra 订阅用户、**Marble** 分免费/Pro/Max 档位、**Odyssey-2 Max** 目前仅 Private Beta；谈判时需确认部署地域与离线授权条款。

---

## 落地碎片（无先后）

- 先界定任务：**预测表征**（做感知/控制的 backbone）还是**生成可交互环境**（产品/关卡原型）——二者 KPI 不同。
- 分清 **open-loop 精彩视频** vs **closed-loop 交互**：后者更在意动作接口与状态持久性。进一步区分：需**可编辑 3D 资产**（选 Marble / HY-World 2.0）还是**视频流**（选 Genie 3 / GWM-Worlds / Odyssey-2 Max）即可。
- 若目标为机器人控制：世界模型仅生成「想象视频」还不够——需配套 **IDM（Inverse Dynamics Model）** 将视频帧转译为关节指令（**1XWM** 的二段式架构为此代表）。
- 自动驾驶/机器人：**域随机化**、传感器噪声建模与真实日志对齐通常是工程大头，不单是模型参数。
- 采购谈判：厘清**推理延迟、并发、地域部署、离线授权**；**Genie 3**（美国仅限）、**Odyssey-2 Max**（Private Beta）、**Cosmos**（开放权重但需自有 GPU）在获取方式上差异巨大，避免把学术 demo 分辨率直接写成 SLA。
- 关注实际交互时长限制——**Genie 3** 严格 60 秒、**Odyssey-2 Max** 宣称 120+ 秒、**LingBot-World** 宣称近 10 分钟——这些数字直接影响应用可行性。

---

## 工具与产品类型（「AI world model」「physics simulation AI」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Interactive world / Genie-like** | 文本或图像条件下的可探索世界、交互评测 | 与「一次性短片生成」话术部分重叠。代表：**Genie 3**、**LingBot-World** |
| **True 3D world model** | 直接输出可编辑 Mesh / 3DGS / 点云 | 与视频世界模型的关键分水岭。代表：**Marble**、**HY-World 2.0** |
| **Interactive world model API** | REST / SDK 交付的实时交互式世界流 | 2026 年新兴商业形态。代表：**Odyssey-2 Pro/Max**（JS/Python SDK）、**World API**（Marble 后端） |
| **Video world model / GWM-style** | 连贯镜头、物理一致性营销向表述 | GWM-1 已分化为三变体：**GWM-Worlds / GWM-Avatars / GWM-Robotics** |
| **Robot / embodied WM** | 动作条件 rollout、操纵与导航 | 安全与样本效率话语更强。代表：**1XWM**（视频想象+IDM 执行）、**X-WAM**（统一 4D 视频-动作框架） |
| **Industrial simulation stack** | GPU 加速、自驾/机器人数据合成 | **Cosmos** 已拆分为 Predict / Transfer / Reason / Policy 多组件平台；**Waymo World Model** 为垂直应用范例 |
| **JEPA / representation WM** | 自监督视频表征、下游微调 | 未必提供「游客可玩」界面。**V-JEPA 2** 已验证零样本机器人部署 |

---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

与站内 Tools 页数据源一致：`content/tools/zh/world-model.md`、`content/tools/en/world-model.md` 中 **`bestTools`** 六款（顺序与 JSON 相同）。下表「一句话」据各 **官网门户或集团 AI 主页**公开表述归纳，**产品线细分与订阅档以厂商页面为准**。

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **GWM-1** | **Runway** 通用世界模型家族（2025-12 发布）：含 **GWM-Worlds**（实时环境模拟）、**GWM-Avatars**（数字人对话）、**GWM-Robotics**（机器人策略评估，与真机 Pearson 0.95 相关）；2026-03 衍生 **Runway Characters** 实时视频 agent API | [runwayml.com · GWM-1](https://runwayml.com/research/introducing-runway-gwm-1) |
| **Genie 3** | **Google DeepMind** 交互式世界模型（2026-01 开放公测）：文本/图片→实时可交互 3D 世界（720p/24fps），单次上限 60 秒；美国 18+ Gemini Ultra 订阅可访问（$125/3 月）；已衍生 **Waymo World Model** 用于自驾长尾仿真 | [deepmind.google · Genie](https://deepmind.google/models/genie/) |
| **Marble** | **World Labs**（李飞飞）真3D 空间智能世界模型：文本/图片/视频/全景→可导航 3D 环境（3DGS 输出）；2026-04 发布 Marble 1.1 Plus（动态立方体自动扩展）；World API 已上线（REST）；分 Free/Pro/Max 档位 | [marble.worldlabs.ai](https://marble.worldlabs.ai/) |
| **Cosmos** | **NVIDIA** 世界基础模型平台：**Cosmos-Predict 2.5**（2B/14B，统一 Text2World/Image2World/Video2World）、**Cosmos-Transfer 2.5**（Sim2Real 迁移）、**Cosmos-Reason 2**（空间推理 VLM）、**Cosmos Policy**（机器人控制，LIBERO 98.5%）；开放模型许可证，HuggingFace 可获取 | [nvidia.com · Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) |
| **1XWM** | **1X Technologies** 具身世界模型（2026-01 发布）：14B 参数视频扩散主干 + 独立逆动力学模型（IDM），「先想象后执行」二段式架构；可从 YouTube 视频学习新任务；推理约 11s/次；配套 Neo 人形机器人（$20K Early Access + $499/月） | [1x.tech · World Model](https://www.1x.tech/discover/world-model-self-learning) |
| **V-JEPA 2** | **Meta AI** 自监督视频表征模型（2025-06 发布）：1.2B 参数，100 万+ 小时无标注视频训练；2026 年延伸为视频生成物理奖励（PhysicsIQ SOTA +7.42%）；零样本机器人部署（~62h Droid 数据，Franka 机械臂 65–80% 成功率）；推理速度比 Cosmos 快 30 倍 | [ai.meta.com · V-JEPA 2](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) |

### 对比与测评（第三方；观点非官方）

公开讨论中常见以下分歧线与实测数据点：

**路线分歧**：（1）**表征路线**（**JEPA**、嵌入空间预测）与**像素级生成路线**谁更样本高效、更易进真实机器人流水线——**V-JEPA 2** 仅需 ~62h 无标注数据即可零样本部署，而 **Cosmos Policy** 依赖大规模预训练但 LIBERO 达 98.5%；（2）**交互世界**演示在分钟级一致性、物体持久性上是否足以称为「可玩」——**Genie 3** 约 60 秒后一致性衰减（DeepMind 在 GDC 2026 公开承认），**Odyssey-2 Max** 宣称 120+ 秒、**LingBot-World** 宣称近 10 分钟，均待独立复现；（3）**工业仿真栈**强调的物理真实度与**创作向**强调的指令跟随、美术风格往往不可同时极值——**Cosmos** VBench 2 physics 子任务 44.92 vs **Odyssey-2 Max** 58.52（第三方基准，非官方自报）。

**视频 vs 真3D**：2026 上半年新出现的核心分歧——**Genie 3 / GWM-1 / Odyssey-2 Max** 输出视频流（不可编辑几何），**Marble / HY-World 2.0** 输出可编辑 3D 资产。前者适合快速探索与实时交互叙事，后者适合需要二次加工的游戏/仿真管线。**HY-World 2.0** 开源于 2026-04，标志着真3D 路线不再被闭源垄断。

**自动驾驶垂直应用**：**Waymo World Model**（基于 Genie 3，2026-02）实现了自然语言→双模态传感器（RGB+LiDAR）的长尾场景生成——《The Verge》、**PCMag** 等报道强调「罕见场景合成」价值，但也指出生成的传感器数据与真实分布的对齐仍需独立验证。

**开源与商业化的张力**：**Cosmos** 开放模型许可证、**HY-World 2.0** 开源、**LingBot-World** 开源——三者以不同开放程度进入市场；闭源方 **Marble**（Free/Pro/Max 档位）、**Odyssey-2 Max**（Private Beta）、**Genie 3**（美国付费订阅）在交付体验和生态整合上仍占优。**Reddit / Hacker News** 与中文社区（知乎、36Kr）讨论中常出现「开源够不够用」vs「闭源省不省心」的采购辩论。

**不存在单一 winner 叙事**：科技媒体（如 **Ars Technica** 对 **Genie 3** 的报道）、行业通讯（如 **Not Boring** 赛道长文）、**The Neuron** 等 AI 日报均将当前阶段类比为「世界模型的 GPT-2 时刻」——技术路线已验证，但大规模商业化尚早。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各厂商营销首页为唯一论据。各基准数字以第三方复现与原始论文为准。*

---

## 延伸阅读与参考材料

- **综述入口**：[World model (artificial intelligence)](https://en.wikipedia.org/wiki/World_model_(artificial_intelligence))（概念界定与_history 线索；维基条目随社区编辑变动，引用时请核对文中参考文献）。
- **早期概念溯源**：**Jürgen Schmidhuber** 1990 年代关于 **world models** 与 **RNN** 的规划叙述（维基条目参考文献链出）。
- **AMI / JEPA 路线图**：**Yann LeCun**《A Path Towards Autonomous Machine Intelligence》（2022 立场文，PDF 广泛转载）；**AMI Labs**（€500M，€3B 估值，2026-01 成立）为其商业化载体。
- **LeWorldModel 预印本**：**LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels** — [arXiv:2603.19312](https://arxiv.org/abs/2603.19312)（是否在产线落地以外部复现为准）。
- **DeepMind Genie 系列**：[Genie 3 产品页](https://deepmind.google/models/genie/) 与 [Genie 3 公告博文](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)；**Waymo World Model** 官方博文（2026-02 发布）。
- **Meta V-JEPA 2**：[官方博文与物理推理基准](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/)；2026 年 PhysicsIQ 延伸：WMReward 方法论文。
- **NVIDIA Cosmos**：[Cosmos Predict 2.5 & Transfer 2.5 技术博文](https://huggingface.co/blog/nvidia/cosmos-predict-and-transfer2-5)；[Cosmos Policy 机器人控制](https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control)。
- **Runway GWM-1**：[GWM-1 研究公告](https://runwayml.com/research/introducing-runway-gwm-1)；[GWM-Robotics 策略评估论文](https://runwayml.com/research/accelerating-robot-policy-evaluation)；[Runway Characters 发布](https://runwayml.com/news/introducing-runway-characters)。
- **1X World Model**：[1XWM 自学习系统公告](https://www.1x.tech/discover/world-model-self-learning)；TechCrunch / The Robot Report 第三方解读。
- **Odyssey**：[Odyssey-2 Max 发布](https://www.i-scoop.eu/odyssey-2-max-world-model/)；[Product Hunt 社区](https://www.producthunt.com/search?q=odyssey+world+model) 讨论。
- **Tencent HY-World 2.0**：[GitHub 开源仓库](https://github.com/Tencent-Hunyuan/HY-World-2.0)；[技术报告 arXiv:2604.14268](https://arxiv.org/abs/2604.14268)。
- **Ant Group LingBot-World**：[LingBot-World 开源公告](https://www.donews.com/news/detail/4/6454175.html)；GitHub（`github.com/robbyant`）。
- **Tsinghua WoW**：WoW 14B/40B 物理一致性世界模型（中文社区讨论与基准对比）。
- **Xiaomi X-WAM**：[Unified 4D World Action Modeling 预印本](https://arxiv.org/html/2604.26694v2)。
- **媒体报道示例**：**Ars Technica** 对 **Genie 3** 的解读文；**PCMag** 等对 **Waymo** 与仿真生成相关合作的报道；**The Verge** 对 Waymo World Model 的分析；**36Kr / 知乎** 对中文世界模型赛道的综述。
- **产业长文**：**Not Boring · World Models** 类赛道综述（投融资叙事与学术叙事并存，勿混作技术评测）；[World Models Race 2026](https://introl.com/blog/world-models-race-agi-2026)（IntroL 赛道分析）；**The Neuron** 等 AI 日报的「世界模型 GPT-2 时刻」论述。
