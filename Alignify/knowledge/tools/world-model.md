# 世界模型（World Models）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**World model / 世界模型**——从观测学习环境内部表征并**预测动作下未来状态演化**；验收以**动力学预测、交互/仿真闭环、3D 资产或传感器输出**为主。本页为 **3D/仿真/具身/表征路线 SSOT**（完整 URL 表见 §外链索引）；实时交互**视频流** Live Model → [video/interactive-video.md](video/interactive-video.md)；离线 clip → [video/video-generator.md](video/video-generator.md)；离散 token 语言 → [llm/multimodal-llm.md](llm/multimodal-llm.md)。

**材料范围**：公开网络检索（维基百科综述、学界预印本与博文、Google DeepMind / Meta / NVIDIA / Runway / World Labs / 1X / Odyssey / Tencent Hunyuan / Ant Group Robbyant / **Visko / Decart / fal** 等公开产品介绍、科技媒体与产业评论）；并归纳「世界模型」在**具身智能、仿真、自动驾驶与交互式生成**语境下的常见用法。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源复述。**具体参数、开源与否与合同条款以各官网与许可证为准**。网摘整理日期 **2026-04-20**，产品刷新日期 **2026-09-02**。

**站内对照**：[alignify.co/tools/world-model](https://alignify.co/tools/world-model) · `/zh/tools/world-model` · `content/tools/en/world-model.md`、`content/tools/zh/world-model.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#world-model-tools`](../../keywords/alignify-keywords-tools.md#world-model-tools)）

**站内相邻**：[video/interactive-video.md](video/interactive-video.md)（实时交互**视频流** / Live Model 产品 SSOT）· [multimodal-llm.md](llm/multimodal-llm.md)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **World model（世界模型）**：在机器学习语境下，指从观测（图像、点云、机器人状态等）学习环境的**内部表征**，并**预测**在动作作用下未来状态如何演化的一类模型；常与**规划、强化学习、仿真**并列讨论，区别于只做分类或单次生成的系统。
- **Latent dynamics / latent space prediction**：在**潜变量空间**而非逐像素重建上预测下一步——降低计算量并鼓励抽象因果结构；与「纯视频扩散」共享工具链但优化目标不同。
- **JEPA（Joint Embedding Predictive Architecture）**：**Yann LeCun** 等推动的范式：编码观测为嵌入，预测器在嵌入空间对齐未来；代表工作含 **V-JEPA** 系列及 **LeWorldModel**（像素端到端 **JEPA** 训练的近期预印本讨论）。
- **World foundation model（WFM / 世界基础模型）**：**NVIDIA Cosmos** 等力推的叙事框架——将世界模型定位为物理 AI 的「基础模型」，上游预训练后供下游机器人、自驾等任务微调；常与 **Predict / Transfer / Reason / Policy** 多组件矩阵绑定。
- **True 3D world model（真3D 世界模型）** vs **video world model（视频世界模型）**：前者输出可编辑 **Mesh / 3DGS / 点云**，永久持久、可导入游戏引擎；后者输出**视频流**，交互时实时推演但不可编辑几何。二者检索词常混用，采购时需先辨输出形态——代表产品见 §外链索引。
- **Interactive world model API**：2026 年新兴交付形态——**REST / SDK / gRPC** 对外服务；采购评估时需关注**推理延迟、并发与按 token / 时长 / 秒计费**模式。实时交互**视频流**产品 SSOT 见 [interactive-video.md](video/interactive-video.md)。
- **Genie（DeepMind）**：从互联网视频等数据学习**可交互环境**生成的系列模型；已衍生自驾长尾仿真应用（**Waymo World Model**）。规格与访问限制见 §外链索引。
- **Embodied AI / 具身智能**：机器人或虚拟体在环境中**闭环**行动；世界模型常用于**想象 rollout**以减少真实试错成本。
- **Digital twin / 仿真闭环**：自动驾驶、物流、制造里用合成数据喂给规划器或感知训练；**仿真分布**与真实长尾场景是否对齐常是争议点。
- **vs LLM**：主流 **LLM** 以离散 token 预测为主；世界模型多在**连续感知域**建模动态。**混合系统**常见：语言层下达任务，低层策略或仿真由世界模型支撑。
- **vs「纯文生视频」**：同类架构可服务短片生成，但若强调**动作条件、状态一致性与可交互**，检索与采购话术常偏向 **world model / interactive world / physics-aware simulation**——离线 clip SSOT 见 [video-generator.md](video/video-generator.md)。
- **Query Model vs Live Model**：**Query Model** 为「输入→预测→结束」的一次性调用；**Live Model** 为**持续运行、有持久状态、生成中可干预**的进程——交互视频产品深度见 [interactive-video.md](video/interactive-video.md)，本页保留跨仿真/3D/机器人叙事。

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

| 维度 | **视频世界模型** | **真3D 世界模型** |
|------|------------------|-------------------|
| **输出形态** | 视频流（不可编辑几何） | Mesh / 3DGS / 点云（可二次编辑） |
| **持久性** | 受推理窗口限（秒~分钟级） | 一次性生成，资产永久保留 |
| **引擎兼容** | 需额外转换或不可导入 | 直接导入 Unity / UE5 / Isaac Sim |
| **推理成本** | 每次交互累积 | 一次性生成，渲染成本≈0 |
| **代表场景** | 实时探索、交互叙事、agent 训练 | 关卡原型、数字孪生、VR 预览 |

架构路线（JEPA / 工业栈 / 交互 API / 真3D / 具身 / Physical AI）→ **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **真实试错昂贵或危险**：机器人、车、能源设施等场景难以靠无限次物理试验覆盖长尾。
- **数据尺度与多样性**：互联网视频、仿真器日志、车队回传等多源数据推动**自监督**与**跨任务迁移**叙事。
- **生成式交互体验**：需要「一说即有小世界可逛」的创作流，单一短视频模型未必强调**交互闭环**。
- **算力与栈绑定**：大规模视频/点云训练与实时推理常与 **GPU、专用仿真管线**销售故事绑定（厂商生态差异明显）。
- **叙事竞争**：同一时期会出现多条路线——通用交互世界、工业仿真、机器人专用世界模型、创作向视频世界模型与表征学习底座并存；**选购需按任务切片，不宜只看「世界模型」标签**（代表见 §形态谱系）。
- **API 化与商业交付**：2026 上半年多家将世界模型从研究 demo 转为 **REST / SDK 产品**，采购开始关注**延迟 SLA、并发与按量计费**而非仅看论文指标。
- **开源冲击**：**Tencent HY-World 2.0**、**Ant Group LingBot-World** 等以开源或开放权重进入，直接对标闭源 **Marble** 与 **Genie 3**，改变「世界模型 = 巨头闭源」的早期格局。
- **自动驾驶长尾仿真**：**Waymo World Model** 将世界模型用于生成**极端罕见驾驶场景**并输出双模态传感器数据（摄像头+LiDAR），标志着世界模型从「生成好玩」到「安全验证」的跨越。

---

## 能力栈（概念拆分，非厂商功能表）

- **前向动力学（forward dynamics）**：给定当前状态与动作，预测下一状态或若干步 rollout。
- **逆动力学 / 规划接口**：从目标反推动作序列时常与 **MPC、RL、搜索** 组合；近期具身模型将逆动力学作为独立 **IDM** 模块与视频生成主干解耦——实现范例见 §外链索引 **Type F**。
- **多模态条件**：文本、布局、初始帧、**LiDAR / 相机同步**（自动驾驶仿真常用表述）；自然语言指令→双模态传感器输出见 §外链索引 **Type C** 自驾垂直代表。
- **表征迁移**：视频编码器作为下游检测、预测、控制的**预训练 backbone**——样本效率与零样本部署数据见 §外链索引 **Type A**。
- **交互一致性**：用户在环境中连续操作时的**记忆与物体持久性**（评测常见讨论点）；各产品宣称时长见 §外链索引，独立复现仍少。
- **3D 资产输出**：是否输出可编辑 **Mesh / 3DGS / 点云**，决定生成结果能否进入游戏引擎或仿真管线做二次加工——真3D 代表见 §外链索引 **Type E**。
- **实时推理 API**：商业交付时需关注的维度——**延迟、并发、按 token / 时长 / 调用次数**计费模式；各产品数值见 §外链索引。
- **引擎与工具链耦合**：是否与 **Omniverse**、自驾仿真栈、游戏引擎（**Unity / Unreal**）或机器人 SDK 预先集成，显著影响落地摩擦。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 自监督视频表征、嵌入空间预测（JEPA 路线） | JEPA / representation WM | V-JEPA 2、LeWorldModel |
| **B** | 工业级 GPU 仿真栈、Predict/Transfer/Reason/Policy 矩阵 | Industrial simulation stack / WFM | Cosmos |
| **C** | 交互式 API 可探索世界（视频流、SDK/REST） | Interactive world / Genie-like / interactive world model API | Genie 3、Odyssey-2 Pro/Max、LingBot-World |
| **D** | 创作向视频世界模型、GWM 多任务家族 | Video world model / GWM-style | GWM-1 |
| **E** | 真 3D 资产输出（Mesh / 3DGS / 点云） | True 3D world model | Marble、HY-World 2.0 |
| **F** | 具身/机器人：视频想象 + 动作条件 rollout、IDM 解耦 | Robot / embodied WM | 1XWM、X-WAM |
| **G** | 动作条件驾驶仿真、Physical AI 闭环、多机位 photorealistic | Action-conditioned driving sim / physics simulation AI | Decart Oasis 3 |
| **H** | 持续有状态 2D 视频流（Live Model、生成中 steering） | Live Model / continuous video stream | Visko Orbis、HappyOyster → [interactive-video.md](video/interactive-video.md) §外链索引 |

**Type C vs H**：均为「可交互视频」，但 C 偏**世界探索/API 仿真叙事**，H 偏 **Live Model 长流产品**——后者完整 SSOT 在 [interactive-video.md](video/interactive-video.md)。**Type G** Physical AI 叙事保留本页，与 interactive-video **Type F** 交叉引用。

---

## 风险 · 合规 · 仿真与滥用（外部框架可对照，非法律意见）

- **仿真与现实鸿沟**：长尾场景覆盖不足可导致**过度自信**的安全决策；监管敏感领域需对照行业测试标准（非本页给出具体条款）。自驾应用虽能生成极端场景，但生成数据与真实传感器分布的对齐仍需独立验证。
- **视听误导**：高写实合成环境可能被滥用于虚假信息或欺诈场景；平台政策与标识要求因地而异。
- **数据与劳工**：大规模视频训练涉及版权与标注外包伦理争议——引用第三方数据集前应核对许可证。
- **出口与军用敏感**：仿真与无人机/国防叙事相邻时，采购与开源分发可能触及**出口管制**讨论（需专项合规）。
- **环境与能耗**：长时高清 rollout 与大规模训练的云资源消耗常与 **ESG** 披露挂钩——训练/推理规模见 §外链索引各产品行。
- **API 锁闭与地域限制**：商业 API 常设访问地理围栏与 Beta 门槛——部署地域、档位与离线授权条款见 §外链索引，谈判时勿把 demo 分辨率直接写成 SLA。

---

## 落地碎片（无先后）

- 先界定任务：**预测表征**（做感知/控制的 backbone）还是**生成可交互环境**（产品/关卡原型）——二者 KPI 不同。
- 分清 **open-loop 精彩视频** vs **closed-loop 交互**：后者更在意动作接口与状态持久性。进一步区分：需**可编辑 3D 资产**（§形态谱系 **Type E**）还是**视频流**（**Type C/H**）即可。
- 若目标为机器人控制：世界模型仅生成「想象视频」还不够——需配套 **IDM（Inverse Dynamics Model）** 将视频帧转译为关节指令（§形态谱系 **Type F**）。
- 自动驾驶/机器人：**域随机化**、传感器噪声建模与真实日志对齐通常是工程大头，不单是模型参数。
- 采购谈判：厘清**推理延迟、并发、地域部署、离线授权**——各产品获取方式差异巨大，见 §外链索引。
- 关注实际交互时长限制——直接影响应用可行性，各产品宣称值见 §外链索引。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

与站内 Tools 页数据源一致：`content/tools/zh/world-model.md`、`content/tools/en/world-model.md` 中 **`bestTools`** 六款（顺序与 JSON 相同）。下表「一句话」据各 **官网门户或集团 AI 主页**公开表述归纳，**产品线细分与订阅档以厂商页面为准**。

**2026-09 增量**（未写入 JSON，成文前须核对）：**Decart Oasis 3**（Physical AI 驾驶仿真 API）、**Visko Orbis** / **HappyOyster**（交互视频流——完整 SSOT 见 [interactive-video.md](video/interactive-video.md) §外链索引）。

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Decart Oasis 3** | G | 动作条件驾驶仿真：多机位 photorealistic 闭环；22fps；<200ms 延迟；API 按秒计费（公开报道 ~$0.02/s） | [decart.ai/oasis](https://decart.ai/oasis) · [Oasis 3 Realtime 文档](https://docs.platform.decart.ai/models/realtime/oasis-3) |
| **GWM-1** | D | **Runway** 通用世界模型家族（2025-12）：**GWM-Worlds**（实时环境模拟）、**GWM-Avatars**（数字人对话）、**GWM-Robotics**（机器人策略评估，与真机 Pearson 0.95 相关）；2026-03 衍生 **Runway Characters** 实时视频 agent API | [runwayml.com · GWM-1](https://runwayml.com/research/introducing-runway-gwm-1) · [GWM-Robotics 论文](https://runwayml.com/research/accelerating-robot-policy-evaluation) · [Runway Characters](https://runwayml.com/news/introducing-runway-characters) |
| **Genie 3** | C | **Google DeepMind** 交互式世界模型（2026-01 开放公测）：文本/图片→实时可交互 3D 世界（720p/24fps），单次上限 60 秒；美国 18+ Gemini Ultra 订阅可访问（$125/3 月）；约 60 秒后一致性衰减（GDC 2026 公开承认） | [deepmind.google · Genie](https://deepmind.google/models/genie/) · [Genie 3 公告博文](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) |
| **Waymo World Model** | C | 基于 Genie 3（2026-02）：自然语言→双模态传感器（RGB+LiDAR）长尾场景生成（龙卷风、大象上路等极端事件） | Waymo 官方博文（2026-02）；背景见 Genie 3 行 |
| **Marble** | E | **World Labs**（李飞飞）真3D 空间智能：文本/图片/视频/全景→可导航 3D 环境（3DGS）；2026-04 Marble 1.1 Plus（动态立方体自动扩展）；World API（REST）；Free/Pro/Max 档位 | [marble.worldlabs.ai](https://marble.worldlabs.ai/) |
| **HY-World 2.0** | E | **Tencent Hunyuan** 真3D 世界模型（2026-04 开源）：Mesh/3DGS 输出，直接导入 Unity/UE5 | [GitHub](https://github.com/Tencent-Hunyuan/HY-World-2.0) · [arXiv:2604.14268](https://arxiv.org/abs/2604.14268) |
| **Cosmos** | B | **NVIDIA** 世界基础模型平台：**Cosmos-Predict 2.5**（2B/14B，Text2World/Image2World/Video2World）、**Cosmos-Transfer 2.5**（Sim2Real）、**Cosmos-Reason 2**（空间推理 VLM）、**Cosmos Policy**（机器人控制，LIBERO 98.5%）；开放模型许可证，HuggingFace 可获取；训练规模 10,000 H100 / 20M 小时视频 | [nvidia.com · Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) · [Predict/Transfer 2.5 博文](https://huggingface.co/blog/nvidia/cosmos-predict-and-transfer2-5) · [Cosmos Policy](https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control) |
| **1XWM** | F | **1X Technologies** 具身世界模型（2026-01）：14B 视频扩散主干 + 独立 IDM，「先想象后执行」二段式；可从 YouTube 学习新任务；推理约 11s/次；配套 Neo 人形机器人（$20K Early Access + $499/月） | [1x.tech · World Model](https://www.1x.tech/discover/world-model-self-learning) |
| **X-WAM** | F | **Xiaomi** Unified 4D World Action Modeling：统一 4D 视频-动作框架 | [arXiv 预印本](https://arxiv.org/html/2604.26694v2) |
| **V-JEPA 2** | A | **Meta AI** 自监督视频表征（2025-06）：1.2B 参数，100 万+ 小时无标注视频；2026 PhysicsIQ SOTA +7.42%（WMReward）；零样本机器人部署（~62h Droid 数据，Franka 65–80%）；推理比 Cosmos 快 30 倍 | [ai.meta.com · V-JEPA 2](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) |
| **LeWorldModel** | A | 像素端到端 **JEPA** 训练预印本（是否在产线落地以外部复现为准） | [arXiv:2603.19312](https://arxiv.org/abs/2603.19312) |
| **Odyssey-2 Pro** | C | 720p/~22fps 交互流；JS/Python SDK | [odyssey.ml · GPT-2 moment](https://odyssey.ml/the-gpt-2-moment-for-world-models) |
| **Odyssey-2 Max** | C | 宣称 120+ 秒交互一致性；VBench 2 physics 58.52（第三方基准）；目前 Private Beta | [Odyssey-2 Max 发布](https://www.i-scoop.eu/odyssey-2-max-world-model/) · [Starchild-1](https://odyssey.ml/introducing-starchild-1) · [Agora-1](https://agora.odyssey.ml/) |
| **LingBot-World** | C | **Ant Group Robbyant**（2026-01 开源）：宣称近 10 分钟交互、<1s 交互延迟 | [开源公告](https://www.donews.com/news/detail/4/6454175.html) · GitHub（`github.com/robbyant`） |
| **Visko Orbis** | H | Live Model 实时交互长视频——完整规格见 [interactive-video.md](video/interactive-video.md) §外链索引 | [visko.ai](https://www.visko.ai/) · [Introducing Live Models](https://www.visko.ai/blog/introducing-live-models) · [Orbis arXiv](https://arxiv.org/html/2607.26694v1) |
| **HappyOyster 1.0** | H | Wandering + Directing 交互视频——完整规格见 [interactive-video.md](video/interactive-video.md) §外链索引 | [Alibaba Cloud 公告](https://www.alibabacloud.com/blog/happyoyster-1-0-is-here_603380) · [happyoyster.cn](https://www.happyoyster.cn/) |

### 对比与测评（第三方；观点非官方）

- **路线分歧（§形态谱系 Type A vs B）**：**表征路线**（JEPA、嵌入空间预测）与**像素级生成路线**谁更样本高效、更易进真实机器人流水线——社区尚无共识；样本效率与 LIBERO 等 benchmark 对照见 §外链索引 Type A vs Type B，勿混作单一 winner。
- **交互一致性（Type C）**：交互世界演示在分钟级一致性、物体持久性上是否足以称为「可玩」——部分 Type C 代表在公开活动中承认约 60 秒后衰减；更长宣称均待独立 stress test（规格见 §外链索引）。
- **工业仿真 vs 创作向（Type B vs D）**：工业栈强调的物理真实度与创作向强调的指令跟随、美术风格往往不可同时极值——VBench 2 physics 子任务第三方基准对照见 §外链索引（非官方自报）。
- **视频 vs 真3D（§词汇锚点）**：2026 上半年核心分水岭——**Type C/D** 输出视频流，**Type E** 输出可编辑 3D 资产；前者适合快速探索与实时交互叙事，后者适合需二次加工的游戏/仿真管线。开源真3D 路线标志见 §外链索引 **Type E**。
- **自驾垂直（Type C/G）**：长尾场景合成价值获多家媒体报道，但生成传感器数据与真实分布对齐仍需独立验证。
- **开源 vs 闭源交付**：多路线以不同开放程度进入市场；闭源方在交付体验与生态整合上仍占优——社区常出现「开源够不够用」vs「闭源省不省心」辩论。
- **不存在单一 winner**：多家媒体将当前阶段类比为「世界模型的 GPT-2 时刻」——技术路线已验证，大规模商业化尚早。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各厂商营销首页为唯一论据。各基准数字以第三方复现与原始论文为准。*

---

## 延伸阅读 · 站内外

**站外**

- **综述入口**：[World model (artificial intelligence)](https://en.wikipedia.org/wiki/World_model_(artificial_intelligence))（概念界定与 history 线索；维基条目随社区编辑变动，引用时请核对文中参考文献）。
- **早期概念溯源**：**Jürgen Schmidhuber** 1990 年代关于 **world models** 与 **RNN** 的规划叙述（维基条目参考文献链出）。
- **AMI / JEPA 路线图**：**Yann LeCun**《A Path Towards Autonomous Machine Intelligence》（2022 立场文，PDF 广泛转载）；**AMI Labs**（€500M，€3B 估值，2026-01 成立）为其商业化载体。
- **LeWorldModel 预印本**：见 §外链索引 **LeWorldModel** 行。
- **DeepMind Genie 系列 / Waymo World Model**：见 §外链索引 **Genie 3**、**Waymo World Model** 行。
- **Meta V-JEPA 2**：见 §外链索引；2026 PhysicsIQ 延伸 WMReward 方法论文。
- **NVIDIA Cosmos**：见 §外链索引 **Cosmos** 行。
- **Runway GWM-1**：见 §外链索引 **GWM-1** 行。
- **1X World Model**：见 §外链索引 **1XWM** 行；TechCrunch / The Robot Report 第三方解读。
- **Odyssey 生态**：见 §外链索引 **Odyssey-2** 行；[Product Hunt 社区讨论](https://www.producthunt.com/search?q=odyssey+world+model)。
- **Decart Oasis 3**：见 §外链索引；[TechCrunch 2026-06 报道](https://techcrunch.com/2026/06/10/decarts-new-world-model-can-simulate-hours-of-photorealistic-driving-with-some-caveats/)。
- **Visko Orbis / HappyOyster**：见 §外链索引；Live Model 范式文 [interactive-video.md](video/interactive-video.md)。
- **Tencent HY-World 2.0 / Ant LingBot-World**：见 §外链索引对应行。
- **Tsinghua WoW**：WoW 14B/40B 物理一致性世界模型（中文社区讨论与基准对比）。
- **Xiaomi X-WAM**：见 §外链索引 **X-WAM** 行。
- **World Labs 功能分类**：[A Functional Taxonomy of World Models](https://www.worldlabs.ai/blog/taxonomy-of-world-models)（Renderer / Simulator / Planner）。
- **媒体报道示例**：**Ars Technica** 对 **Genie 3** 的解读文；**PCMag** 等对 **Waymo** 与仿真生成相关合作的报道；**The Verge** 对 Waymo World Model 的分析；**36Kr / 知乎** 对中文世界模型赛道的综述。
- **产业长文**：**Not Boring · World Models** 类赛道综述（投融资叙事与学术叙事并存，勿混作技术评测）；[World Models Race 2026](https://introl.com/blog/world-models-race-agi-2026)（IntroL 赛道分析）；**The Neuron** 等 AI 日报的「世界模型 GPT-2 时刻」论述。

**站内**

- 实时交互视频流 SSOT：[video/interactive-video.md](video/interactive-video.md)
- 离线 clip：[video/video-generator.md](video/video-generator.md)
- 多模态 LLM：[llm/multimodal-llm.md](llm/multimodal-llm.md)