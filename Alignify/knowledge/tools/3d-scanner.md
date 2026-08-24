# AI 3D Scanner · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、AOUSD/Khronos 格式公告、学术论文与预印本、ISPRS/行业白皮书、KIRI 官方对比文）；**未**引用 Alignify 站内 JSON 正文为论据。网摘整理日期 **2026-06-24**。**主轴词**：**AI 3D scanner**；中文常称 **AI 3D 扫描仪 / 三维重建**——强调 **从实物到数字（capture）**，与 text-to-3D（见 [3d-model-generator.md](./3d-model-generator.md)）及手工建模（见 [3d-modelling.md](./3d-modelling.md)）检索意图可分。

**站内对照**：[alignify.co/tools/3d-scanner](https://alignify.co/tools/3d-scanner) · [alignify.co/zh/tools/3d-scanner](https://alignify.co/zh/tools/3d-scanner) · `content/tools/en/3d-scanner.md` · `content/tools/zh/3d-scanner.md` · slug **`3d-scanner`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#3d-scanner-tools`](../../keywords/alignify-keywords-tools.md#3d-scanner-tools)

**站内相邻**：[3d.md](./3d.md) · [3d-model-generator.md](./3d-model-generator.md) · [3d-modelling.md](./3d-modelling.md) · [cad.md](./cad.md)

**内容边界**：本 slug 主责 **实物数字化**（照片/LiDAR/视频→点云/网格/splat）；文/图生 3D 见 [3d-model-generator.md](./3d-model-generator.md)。**3DGS/NeRF/摄影测量对比表 SSOT 在本页**；格式基础设施摘要见 [3d.md](./3d.md) §共享事实速查。

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **AI 3D Scanner（本知识块与 slug `3d-scanner` 的主标签）**：利用 AI/ML 算法将**实物**（照片序列、LiDAR 点云、视频帧）转化为**三维数字模型**的工具。英文检索常写 **3D scanner app**、**AI 3D reconstruction**、**photogrammetry app**、**Gaussian splatting scanner**；中文混用 **3D 扫描仪**、**三维重建**、**实景建模**。与传统 3D 扫描仪的核心差异：AI 扫描仪可工作于**非专用硬件**（普通手机摄像头即可），且输出不限于点云/网格——可直接生成**神经辐射场（NeRF）**或**3D 高斯泼溅（3DGS）**等新型表示。
- **Photogrammetry / 摄影测量（SfM）**：从**多角度照片**通过特征匹配和三角测量**重建三维几何**。是 3D 扫描最成熟的技术路线，测量级精度可达 1-3cm（配控制点/RTK）。擅长刚体表面（建筑、雕塑、工业零件），但对**透明、反光、无纹理**表面几乎无效。在 AI 语境下，「AI photogrammetry」指用深度学习增强特征匹配、深度估计和网格补全的摄影测量管线。
- **NeRF（Neural Radiance Fields）/ 神经辐射场**：将三维场景**编码进神经网络权重**，通过逐像素光线追踪合成新视角。2020 年由 Mildenhall 等人提出后引爆了 3D 视觉领域。优势在于对**复杂光照、半透明、反射**等场景的渲染质量远超传统方法；劣势是训练和渲染慢（通常需要 GPU 数分钟到数小时），且输出不是可编辑的网格——在 2025-2026 年正逐渐被 3DGS 在渲染速度上超越。
- **3D Gaussian Splatting（3DGS）/ 三维高斯泼溅**：将场景表示为**数百万个有方向的 3D 高斯椭球体**，可**实时 60+ FPS** 渲染（Kerbl et al., 2023）。擅长植被、玻璃、反射等难材质；几何精度多为**可视化级**（数厘米级偏差，非测量级）。2026 年基础设施进展：**OpenUSD v26.03** 原生 `UsdVolParticleField3DGaussianSplat`；glTF **KHR_gaussian_splatting** RC（2026-02，ratification 目标 2026 Q2）。**3DGS-to-Mesh**（如 KIRI Engine）使 splat 可进入传统 DCC，但转换后精度仍常为可视化级。
- **LiDAR Scanner / 激光雷达扫描**：使用**飞行时间（ToF）**或**相位差**测量距离，输出高精度**点云**。iPhone Pro 系列（12 代起）和 iPad Pro 内置 LiDAR 传感器，把**消费级 3D 扫描**的门槛从数千美元降至零。2026 年，AI 驱动的 LiDAR 应用（如 HoloTwin、Dot3D）加入实时 SLAM 回环修正、AI 辅助扫描引导等功能。注意：LiDAR 虽然本身不是「AI」，但几乎所有现代 LiDAR 扫描 app 都使用 AI 进行点云去噪、网格重建和语义分割。
- **SLAM（Simultaneous Localization and Mapping）/ 即时定位与建图**：在**移动中**同时估计设备位姿并构建环境地图。是手持/移动 3D 扫描的核心使能技术。AI-SLAM 融合了**惯性测量单元（IMU）**、**视觉特征**和**深度数据**，在 GPS 不可用的室内环境（工厂、矿井、建筑内部）中实现厘米级定位。Artec Jet（2026）将 AI-SLAM 推到「GPS 拒止环境全自主扫描」水平。
- **Digital Twin / 数字孪生**：物理实体或环境的**实时、可查询的三维数字副本**。AI 3D 扫描是数字孪生的**主要数据入口**——从「静态 BIM 模型」到「活着的运维孪生」的关键桥梁。2026 年趋势：Siemens Digital Twin Composer、ABB Genix + NVIDIA Omniverse 将扫描数据与**实时 IoT 数据流**（资产健康、异常检测）融合，数字孪生从「可视化的 3D 模型」升级为「可决策的空间操作系统」。
- **Guided Scan / AI 扫描引导**：在扫描过程中由**端侧 AI** 实时评估扫描质量——标记缺失表面、提示照明不足、建议最佳拍摄角度。HoloTwin HT Scan（CES 2026 获奖）的 Guided Scan Intelligence™ 是实现这一概念的代表产品，目标是在**离开现场前**确认数据完整。
- **3DGS-to-Mesh Conversion / GS 转网格**：将 3D 高斯泼溅转换为**传统多边形网格**（OBJ/glTF）的 AI 管线。KIRI Engine 首创此能力——用户以 GS 模式扫描（享受实时渲染和高视觉质量），最终输出为 Blender/Unreal 可用的 OBJ 网格。这是 3DGS 从「可视化玩具」走向「生产就绪」的关键一步。

- **Neural Surface Reconstruction（NSR）/ 神经表面重建**：与 NeRF（体积渲染）不同，NSR 直接学习**隐式表面函数**（如 SDF），输出可直接提取为网格。KIRI Engine 的「Neural Surface」模式即属于此路线——兼顾 NeRF 的光照鲁棒性与网格的可编辑性。
- **On-Device Processing / 端侧处理**：扫描数据**完全在手机/平板上处理**，无需上传云端。PocketGS（2026 年 1 月）在 iPhone 15 上实现了**5 分钟内、<3GB 内存**的完整 3DGS 训练；Scaniverse 是首个在设备端完成 GS 处理的消费级 app。端侧处理的关键意义：（1）隐私（数据不上传）；（2）即时反馈；（3）无网络环境可用（工地、矿井、偏远地区）。
- **4D Capture / 动态捕捉**：对**运动的**物体或场景进行 3D 重建——即随时间变化的三维模型（3D + 时间 = 4D）。MoBluRF（2025）可从**模糊的手机视频**中分离相机运动模糊和物体运动；StreamSplat（ICLR 2026）推动动态 GS 走向实时。应用场景：运动分析、表情捕捉、流体/布料动态重建。

---

## 专题对照 / 扩展定义

| 维度 | **3D Scanner**（本文件） | **3D Modelling** |
|------|--------------------------|-------------------|
| **数据来源** | 实物（拍照、LiDAR、视频） | 零（设计师/算法从空白创建） |
| **核心问题** | 「如何忠实地数字化现存物体」 | 「如何从概念走到可渲染模型」 |
| **输出精度标准** | 与原物的几何偏差（mm/cm 级） | 设计意图的符合程度 |
| **知识块** | 本页 | [3d-modelling.md](./3d-modelling.md) |

| 维度 | **消费级 app（手机）** | **专业手持/地面扫描仪** | **企业数字孪生平台** |
|------|----------------------|------------------------|---------------------|
| **硬件** | 手机摄像头 + 可选 LiDAR | 专用传感器（结构光、激光、多相机阵列） | 无人机/地面扫描仪 + 云处理管线 |
| **精度** | 1-5cm（视觉）/ 0.5-2cm（LiDAR） | 0.005mm-2cm（取决于技术） | 1-3cm（无人机 SfM + GCP） |
| **典型用户** | 创作者、3D 打印爱好者、小型电商 | 逆向工程、质检、文化遗产 | 工厂、基建、智慧城市 |
| **AI 的独特价值** | 把非专用硬件提升到可用精度 | AI 引导扫描 + 自动模型分类 | AI 语义分割 + IoT 融合 |

| 维度 | **Photogrammetry** | **NeRF** | **3D Gaussian Splatting** |
|------|-------------------|----------|--------------------------|
| **输出格式** | 网格/点云（可编辑） | 神经网络权重（不可直接编辑） | 高斯点云（可编辑 GS 编辑器如 SuperSplat） |
| **渲染速度** | N/A（导出到外部渲染器） | 慢（分钟级） | **实时**（60+ FPS） |
| **材质处理** | 反光/透明/无纹理表面失败 | 擅长复杂光照 | 擅长植被、玻璃、反射、头发 |
| **测量精度** | **高**（测量级） | 中等 | 可视化级（~7.82cm 均值） |
| **2026 年成熟度** | 成熟（工业标准） | 视效/复杂光照 niche | **主流**（USD v26.03 + glTF RC） |

---

## 问题域（为何会出现这类产品）

- **3D 内容需求爆炸但供给受限**：游戏、XR、电商 3D 展示、数字孪生、机器人仿真等领域对三维资产的需求激增，但传统 3D 建模的人力成本和周期是瓶颈——「每个人都需要 3D，但没几个人会做 3D」。
- **硬件门槛的坍塌**：2020 年 iPhone 12 Pro 首次内置 LiDAR，此后 Android 旗舰也逐步加入 ToF 深度传感器。到 2026 年，任何人手中都有一台**足以做 3D 扫描的计算机**——硬件不再是壁垒，算法（AI）成为差异化核心。
- **NeRF/3DGS 突破了传统摄影测量的天花板**：反光、透明、植被、毛发等材质在传统 SfM 管线中几乎无法处理——3DGS 用「百万高斯球」的概率表示绕过了几何重建的刚体假设。这是 AI 从「辅助」到「重构」3D 扫描范式的根本原因。
- **数字孪生从演示到运维的跨越**：工业界不再满足于「建一个漂亮的 3D 模型看看」——Siemens、ABB、NVIDIA Omniverse 的 2026 年产品线将扫描数据与实时 IoT 数据流融合，要求扫描不只是几何准确，还要**语义丰富**（AI 识别管道、阀门、设备型号）和**可查询**（自然语言搜索空间内对象）。
- **端侧 AI 芯片的成熟**：iPhone 15/16 的 Neural Engine、骁龙 8 Gen 3/4 的 Hexagon NPU，使得 PocketGS 这种「5 分钟手机端完整 3DGS 训练」成为可能。没有端侧 AI 算力的飞跃，消费级 3D 扫描仍会被迫依赖云端——而云端意味着延迟、隐私风险和网络依赖。
- **Physical AI（实体 AI）对训练数据的需求**：机器人、自动驾驶、机械臂操作需要**海量三维环境数据**做仿真训练——NVIDIA Isaac Sim、Deep Insight DIMENVUE 等产品直接将 3D 扫描仪定位为「Physical AI 的数据基础设施」。这为 3D 扫描打开了一个远超「创作者工具」的市场天花板。
- **电商与社交媒体的 3D 化**：Amazon、Shopify 等平台的 3D 商品展示、Apple Vision Pro 空间内容消费——催生了对「手机拍一圈就能出 3D 模型」的刚需。这些场景不要求测量级精度，但要求**快、好看、容易分享**——恰好是消费级 AI 3D 扫描的甜蜜点。

---

## 能力栈（概念拆分，非厂商功能表）

- **采集模态**：单目 RGB（普通手机拍照）、双目/多目（iPhone Pro 多摄协同）、LiDAR ToF（深度点云）、结构光（高精度工业级，如 ChaoXiLi AiScan O1 的 0.005mm 分辨率）、视频帧（MoBluRF 支持模糊视频输入）、无人机航拍（DJI Terra 30K 图像批处理）。
- **重建算法**：SfM+MVS（经典摄影测量管线）、NeRF 体积渲染（光照复杂场景）、3DGS（实时渲染 + 复杂材质）、NSR 隐式表面（可直接提取网格）、Hybrid（LiDAR 几何框架 + GS 纹理贴图——Xgrids L2 Pro 和 HoloTwin 路线）。
- **输出格式**：点云（PLY/LAS/XYZ）、网格（OBJ/STL/glTF/FBX/USD）、GS 高斯点云（PLY `.ply`）、NeRF 权重文件；以及语义层（物体分类标签、BIM 构件映射）。
- **精度层次**：测量级（±0.005mm-2cm，结构光/激光扫描仪）、工程级（±1-5cm，LiDAR + GCP 摄影测量）、可视化级（±5-10cm，纯视觉/手机 GS）、示意级（精度不重要，快和好看优先——电商展示用）。
- **AI 增强维度**：特征匹配（SuperPoint/D2-Net 替代 SIFT，在弱纹理表面更鲁棒）、深度估计（单目深度网络补全 LiDAR 盲区）、语义分割（自动识别门/窗/管道/设备）、扫描引导（端侧 AI 实时评估扫描质量——HoloTwin Guided Scan Intelligence）、3DGS-to-Mesh（AI 将概率性 GS 表示转换为确定性网格）。
- **端侧 vs 云端**：完全端侧（PocketGS、Scaniverse，Metal/Core ML 加速）、云端处理（Luma AI、DJI Terra，GPU 集群）、混合（KIRI Engine：拍照端侧缓存 → WiFi 时后台云端优化）。
- **实时性**：离线批处理（摄影测量、NeRF——分钟到小时级）、近实时（3DGS 训练——PocketGS <5 分钟）、实时（SLAM 扫描预览——扫描过程中即可看到高质量渲染）。
- **多扫描融合与场景规模**：单物体（桌面级、30-150 张照片）、房间级（LiDAR 或 GS，1-5 分钟扫描）、建筑/工厂级（无人机 + 地面扫描仪融合，DJI Terra、Xgrids 30K 图批处理）、城市级（Voyager 流式传输城市级 GS）。

---

## 形态谱系（与具体品牌解耦）

- **消费级通用扫描 App（手机拍照为主）**：KIRI Engine、Polycam——覆盖最广的硬件兼容（iOS + Android，不强制 LiDAR），支持从拍照到 GS 的多种重建模式。2026 年核心竞争点：**免费 tier 的宽松度**（KIRI 4.0 取消导出限制）、**GS-to-Mesh 转换**、**处理速度**。适合 3D 打印爱好者、内容创作者、小型电商。
- **Apple LiDAR 生态专用 App**：Scaniverse（Niantic，完全免费、端侧 GS 处理）、Dot3D（测量级精度、SLAM 回环修正、NeRF/GS 帧导出）、SiteScape（AEC/BIM 专业，E57/RCP 导出）、Canvas（扫描→CAD，按平方英尺定价）。利用 iPhone/iPad LiDAR 的深度精度（0.5-2cm）做到消费级硬件上的准专业输出。
- **NeRF/GS 品质优先型**：Luma AI——iOS only，NeRF 渲染光照质量在消费级产品中最高，适合「视觉品质 > 几何精度」的场景（艺术创作、概念可视化）。虽不再频繁更新，但其 NeRF 渲染质量仍是标杆。PostShot（Jawset，桌面端 GS 重建）和 SuperSplat（PlayCanvas，免费浏览器 GS 编辑器）构成了消费级 GS 的桌面工具链。
- **Prosumer 手持专用扫描仪**：3DMakerPro Eagle/Raven、ChaoXiLi AiScan O1——拿起就走的手持设备，**AI 的介入点是自动选择扫描模式**（AiScan O1 在结构光和 3DGS 之间自动切换）、AI 引导扫描、AI 模型分类。价格 $1,099-$4,000，定位在消费级 app 和专业设备之间的空白。
- **工业级/计量级扫描仪**：Artec Leo/Spider II/Ray II（德国，无线手持，0.01mm 精度）、Xgrids L2 Pro（唯一提供 GS→Revit BIM 插件的产品，±1-2cm，640K pts/sec）、Deep Insight DIMENVUE（韩国 WIS 2026 获奖，LiDAR + 3DGS，Physical AI 数据基础设施定位）。用户是汽车/航空航天质检、逆向工程、文化遗产保护。
- **无人机 + AI 大规模实景建模**：DJI Terra v5.2（2026 年新增 GS 支持，30K 图像批处理，$2,800-$4,400）——从无人机影像到 3DGS/3DTiles/GeoTIFF 的全自动管线。Bentley ContextCapture、Pix4D 等传统 SfM 软件也陆续加入 AI 驱动的点云分类和 GS 渲染选项。
- **企业数字孪生平台（扫描→运维一体化）**：Siemens Digital Twin Composer + NVIDIA Omniverse（工业元宇宙，PepsiCo 案例 20% 吞吐提升）、ABB Genix + Microsoft Azure（实时 IoT 数据与空间可视化融合）、HoloTwin HT Scan（CES 2026 获奖，BIM-to-Operational Twin 的桥梁）。这类「产品」的形态已超越「3D 扫描仪」——3D 扫描是他们数据入口层的**其中一个模块**。
- **开源/研究型框架**：Nerfstudio + gsplat（NVIDIA 支持，CUDA 依赖，学术事实标准）、PocketGS（手机端训练，2026 年 1 月发布）、SplatForge（$49 Blender 插件，1600 万 splat 视口内编辑）。面向开发者、研究者、需要定制管线的团队。

---

## 风险 · 合规 · 隐私与安全（轴特有 + 簇级链出）

簇级版权/深伪框架见 [3d.md](./3d.md) §风险。本 slug 特有风险：

- **扫描他人空间/物体的合法性问题**：在公共场所扫描建筑外立面通常不违法，但在**私人空间**（他人住宅、商业场所内部）或扫描**受版权/设计专利保护的物品**时涉及侵权风险。各国法律差异大——例如欧盟对「建筑全景自由（freedom of panorama）」的规定因成员国而异。
- **Biometric 数据（人脸/人体扫描）**：面部 3D 扫描属于**生物特征数据**范畴，在 GDPR 下属于**特殊类别数据**，需明确同意和目的限制。Apple 的 TrueDepth 人脸扫描 API 对第三方 app 的访问限制已逐步趋严。2026 年趋势：EM3D 等面部扫描 app 明确声明数据不上传/不用于训练。
- **云端处理 = 数据离开本地**：大量 3D 扫描 app 默认将照片/点云上传至云端处理（Luma AI、DJI Terra、Polycam 的某些模式）。对于涉及商业秘密（工厂产线布局、未公开产品原型）、安全敏感设施（机场、电站）、或隐私场景（住宅室内），**端侧处理（PocketGS、Scaniverse）是硬需求**。
- **3DGS/NeRF 中的无意信息泄露**：高斯泼溅和神经辐射场在渲染时可能**意外暴露**原始训练数据中肉眼不可见的细节——例如反射表面中映出的拍摄者、窗外景色中包含的可定位地标。这在 3D 扫描领域是新兴风险，目前尚无成熟的自动匿名化方案。
- **扫描质量 ≠ 法律效力**：手机 app 扫描结果**不是**法定测量工具——在产权边界纠纷、法医取证、建筑验收等场景中，手机 3D 扫描结果可能被法庭拒绝作为证据。需要计量认证（如 ISO 17025）的专用设备才具有法律认可的测量效力。
- **军事/敏感设施扫描**：多国（中美为甚）对关键基础设施、军事设施周边的**无人机航拍和 3D 扫描**有明确禁令和刑法条款。DJI 无人机的地理围栏（geofencing）是硬件层面的被动合规措施，但消费级扫描 app 通常不内置此类限制——合规责任在用户。

---

## 落地碎片（无先后）

- **先用手机现有摄像头测试，再决定是否买 LiDAR 设备**：KIRI Engine 和 Polycam 的纯拍照模式在好光照、有纹理的物体上已经能达到令人满意的结果。如果主要扫描对象是小型、纹理丰富的物体（雕塑、手办、产品原型），可能根本不需要 LiDAR。只有在需要扫描**大面积室内空间**（房间、工厂）、**弱纹理白墙**、或需要**厘米级测量精度**时才需要 LiDAR。
- **平整、哑光的扫描对象更友好；光泽、透明物体先喷粉/贴标记点**：即使是 AI 增强的摄影测量和 3DGS，在面对**极度反光**（镜面、抛光金属）或**全透明**（玻璃、亚克力）物体时仍然吃力。实际操作中，**显像剂喷雾（AESUB 等自挥发品牌）** 或临时贴标记点是低成本的高效解决方案。
- **3DGS 用于「分享/展示」，Photogrammetry 用于「编辑/测量」**：如果最终目的是发社交媒体、嵌入网页做 3D 展示——直接用 3DGS（Scaniverse/KIRI GS 模式），渲染漂亮且实时。如果最终目的是导入 Blender 编辑、3D 打印、或在 CAD 软件中做逆向工程——走摄影测量管线（输出 OBJ/STL 网格），GS-to-Mesh 转换可以作为备选但精度会有损失。
- **视频比照片更适合快速扫描**：大多数 app 支持**从视频帧提取关键帧**进行重建——围着物体拍一段 15-30 秒的慢速环绕视频，通常比拍 50-100 张独立照片更快且更不容易漏面。但注意：视频帧的**运动模糊**在快速移动时会导致重建失败——保持物体在画面中清晰是前提。
- **Diffuse/均匀光照 > 直射强光/阴影**：阴天户外是 3D 扫描的最佳光照条件——无硬阴影、无过曝高光。室内扫描时避免单一强光源（窗户侧光、顶灯直射），用**多角度柔光**或环形灯。硬阴影在重建后会被「烘焙」进模型的纹理贴图中，变成一个不可移除的瑕疵。
- **扫描完整度比分辨率更重要**：很多新手追求高照片数量（300-500 张），但一个只有 80 张照片但**覆盖了所有死角**的扫描，质量远超 300 张但只拍了前/侧面的扫描。关键是**底面、顶面、凹陷区域**——这些是最容易被遗漏的面。
- **善用「AI 扫描引导」功能避免返工**：如果使用的 app 有实时扫描质量评估（HoloTwin 类产品），信任它的反馈——在现场补拍 2 分钟比回办公室后发现数据缺失再跑一趟省时得多。

---

## 工具与产品类型（「3D 扫描」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|-------------|------|
| **Mobile 3D scan app**（3D scanner app、phone 3D scan） | KIRI Engine、Polycam、Scaniverse、Luma AI、Widar、Dot3D | 消费级入口；2026 年 GS/NeRF/Photogrammetry 三模共存 |
| **Handheld 3D scanner**（handheld laser scanner、structured light scanner） | 3DMakerPro Eagle/Raven、ChaoXiLi AiScan O1、Artec Leo/Spider II | prosumer 到工业级；AI 介入点在自动模式切换和质量引导 |
| **LiDAR scan app**（lidar room scanner、iPhone lidar scan） | Scaniverse、SiteScape、Canvas、Dot3D | 需要 iPhone Pro/iPad Pro LiDAR；精度优于纯视觉 |
| **Aerial / drone 3D mapping**（drone photogrammetry、drone 3D scan） | DJI Terra、Bentley ContextCapture、Pix4D | 城市/工地/矿山级；AI 用于点云分类和 GS 纹理增强 |
| **Digital twin platform**（digital twin software、reality capture platform） | Siemens Digital Twin Composer、ABB Genix + Omniverse、HoloTwin | 3D 扫描**不是**产品本身，而是平台的数据入口组件 |
| **NeRF / GS capture**（NeRF scanner、gaussian splatting app） | Luma AI、PostShot、Scaniverse（on-device GS） | 输出不一定是传统网格；视觉效果优先于几何精度 |
| **Industrial metrology scanner**（3D metrology、laser scanner industrial） | Artec Ray II、Zeiss、FARO、Creaform | 测量认证级精度（微米到亚毫米）；非 AI 驱动但 AI 辅助对齐/分类逐渐加入 |

---

## 外链索引（与 Alignify Tools 页、关键词锚点配套的参考入口；非广告、无排序优先级）

### 工具与产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| **KIRI Engine** | 消费级 3D 扫描标杆——Photogrammetry + NeRF NSR + 3DGS 三模式，首创 GS→Mesh 转换，v4.0 取消导出限制 | [kiriengine.app](https://www.kiriengine.app) |
| **Polycam** | 跨平台（iOS + Android + Web），社区 Explore 库含数百万公开模型，GS + LiDAR + 摄影测量 | [poly.cam](https://poly.cam) |
| **Scaniverse**（Niantic） | 首个端侧 3DGS 消费级 app，完全免费，社交分享导向 | [scaniverse.com](https://scaniverse.com) |
| **Luma AI** | NeRF 渲染品质标杆，iOS only，免费云端处理；捕获质量突出但产品不再频繁更新 | [lumalabs.ai](https://lumalabs.ai) |
| **Dot3D** | 专业级 LiDAR 扫描——实时 SLAM 回环修正、AprilTag 定位、NeRF/GS 帧导出给第三方软件 | [dotproduct3d.com](https://www.dotproduct3d.com) |
| **SiteScape** | AEC/BIM 行业 LiDAR 扫描 app，E57/RCP 导出，适合与 Revit/AutoCAD 对接 | [sitescape.ai](https://www.sitescape.ai) |
| **Canvas** | LiDAR→CAD（Revit/SketchUp 可用），按平方英尺计费，装修/改造场景常用 | [canvas.io](https://www.canvas.io) |
| **3DMakerPro Eagle / Raven** | Prosumer 手持扫描仪——200K pts/sec，2cm 精度，Raven 2026 年 3 月发布，原生 GS PLY/OBJ | [3dmakerpro.com](https://www.3dmakerpro.com) |
| **ChaoXiLi AiScan O1** | 2026 年新发布——结构光（0.005mm）+ AI GS 双模式自动切换，远近场双模式 | [chaoxili.com](https://www.chaoxili.com) |
| **Artec 3D**（Leo / Spider II / Ray II / Jet） | 工业计量级——0.01mm 起；Jet（2026）主打 AI-SLAM 全自主扫描 | [artec3d.com](https://www.artec3d.com) |
| **Xgrids L2 Pro** | 手持 SLAM + GS，640K pts/sec，±1-2cm，唯一 GS→Revit BIM 插件 | [xgrids.com](https://www.xgrids.com) |
| **Deep Insight DIMENVUE** | 韩国 WIS 2026 获奖——LiDAR + 3DGS 便携扫描仪，Physical AI 数据基础设施定位 | 厂商未公开官网（2026 年 4 月参展阶段） |
| **DJI Terra v5.2** | 无人机实景建模——30K 图像 SfM→GS 批处理，3DTiles/PLY/GeoTIFF 多格式输出 | [enterprise.dji.com/dji-terra](https://enterprise.dji.com/dji-terra) |
| **HoloTwin HT Scan** | CES 2026 获奖 iOS app——Hybrid Reality Capture Engine™ + Guided Scan Intelligence™，BIM 到运维孪生 | [holotwin.com](https://www.holotwin.com) |

### 开发者/开源工具

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Nerfstudio + gsplat** | NVIDIA 支持的开源 NeRF/GS 框架，学术与工程的事实标准 | [docs.nerf.studio](https://docs.nerf.studio) |
| **PostShot**（Jawset） | 桌面端 GS 重建，文化遗产研究中使用（ISPRS 2026 Caserta 案例） | [jawset.com](https://www.jawset.com) |
| **SuperSplat**（PlayCanvas） | 免费浏览器内 GS 编辑器——clean、crop、merge PLY splats | [playcanvas.com/supersplat](https://playcanvas.com/supersplat) |
| **SplatForge** | $49 Blender 插件，视口内处理 1600 万 splat | 在 Blender Market 搜索 |

### 对比与测评（第三方；观点非官方）

全光谱（手机 app→工业扫描仪）缺乏单一权威横评机构；以下为 **厂商白皮书 + 行业媒体** 归纳的常见分歧（非 Alignify 实测）：

**消费级 app（KIRI / Polycam / Scaniverse）**：KIRI 差异化在 **GS→Mesh** 与 v4.0 导出策略（见 [KIRI 官方 2026 免费 app 对比文](https://www.kiriengine.app/blog/Best_Free_3D_Scanner_Apps_2026)）；Polycam 优势在跨平台与公开 Explore 库；Scaniverse 优势在 **端侧 GS + 免费 tier**。Luma Capture 的 NeRF 渲染在复杂光照场景仍常被引用为画质标杆，但产品更新节奏慢于 KIRI/Polycam——**Luma Genie（text→场景生成）** 属 [3d-model-generator.md](./3d-model-generator.md)，非本 slug。

**精度是否够用**：3D 打印 hobbyist 常接受 **1–3 mm** 级偏差；机械装配/逆向工程需计量级手持仪。手机 GS 与 GS-to-Mesh 输出应默认按 **可视化级** 验收，工程测量走摄影测量+GCP 或计量扫描仪。

**LiDAR vs 纯视觉**：室内大空间与白墙场景 LiDAR 融合通常优于纯视觉；中小型纹理丰富物体在均匀光照下纯视觉摄影测量可表现良好。iPhone Pro 用户可融合 LiDAR+RGB；无 LiDAR 设备依赖 KIRI/Polycam 等纯视觉模式。

**企业级**：2026 年差异化更多在扫描后 **语义标注 + BIM/IoT 融合**（Siemens Digital Twin Composer、ABB Genix + Omniverse 等），而非硬件精度极限。

*以上为行业观点综合，非本站实测。*

---

## 延伸阅读与参考材料

### 技术综述与行业报告
- [Gaussian Splatting: The Complete Guide to Real-Time 3D Capture (2026)](https://www.thefuture3d.com/gaussian-splatting/) — THE FUTURE 3D 的 GS 全指南，覆盖原理、工具链和行业应用
- [Best Free 3D Scanner Apps (2026) With No Export Paywall](https://www.kiriengine.app/blog/Best_Free_3D_Scanner_Apps_2026) — KIRI Engine 官方博客的免费 3D 扫描 app 对比（含导出限制说明）
- [The Spatial Enterprise: Digital Twins and Reality Capture at AWE USA 2026](https://www.awexr.com/blog/1333-the-spatial-enterprise-how-digital-twins-and-reali) — AWE USA 2026 数字孪生与实景捕捉专题前瞻

### 学术论文（2025–2026 关键进展）
- Kerbl et al., "3D Gaussian Splatting for Real-Time Radiance Field Rendering," ACM Trans. Graph. 2023 — GS 的原始论文（非 2026 但为整个领域的基础）
- Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis," ECCV 2020 — NeRF 原始论文
- PocketGS (Jan 2026): On-device 3DGS training in <5 min, <3 GB on iPhone 15
- Auto3R (Apr 2026): First fully automated 3D scanning + reconstruction framework for 3DGS
- IGFuse (AAAI 2026, Mar): Multi-scan GS fusion with occlusion recovery
- Voyager (Jun 2025): City-scale GS streaming to mobile — 100x data reduction
- MoBluRF (2025): Dynamic 3D capture from blurry smartphone videos

### 厂商白皮书与官方资源
- [Siemens Digital Twin Composer — CES 2026 Launch](https://www.automation.com/article/siemens-industrial-metaverse-life-digital-twin-composer) — PepsiCo 案例：20% 吞吐提升、10-15% CapEx 降低
- [ABB Genix + NVIDIA Omniverse — Hannover Messe 2026](https://www.automationmagazine.co.uk/abb-genix-advances-industrial-digital-twins-through-immersive-3d-visualization-with-nvidia-omniverse-and-microsoft-azure/)
- [Deep Insight DIMENVUE — WIS 2026 Top 6](https://www.venturesquare.net/zh/1076869/) — 韩国 AI 3D 扫描仪，Physical AI 定位
- [ChaoXiLi AiScan O1 — Fabbaloo](https://www.fabbaloo.com/news/chaoxili-introduces-aiscan-o1-combining-structured-light-and-ai-based-gaussian-splatting) — 结构光 + AI GS 双模式自动切换
- [HoloTwin HT Scan — GlobeNewsWire](https://www.globenewswire.com/de/news-release/2026/05/14/3294845/0/en/pure-harvest-corporate-group-otc-phcg-operating-as-mixie-technologies-announces-holotwin-launch-of-ai-powered-ht-scan.html) — CES 2026 获奖，Hybrid Reality Capture Engine™ + Guided Scan Intelligence™

### 格式与基础设施
- [OpenUSD v26.03 — Gaussian Splatting schema](https://aousd.org/blog/openusd-v26-03/)
- [Khronos KHR_gaussian_splatting RC](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_gaussian_splatting)

---


---

## 延伸阅读 · 站内知识块

- Hub：[3d.md](./3d.md)
- 生成：[3d-model-generator.md](./3d-model-generator.md)
- 精修：[3d-modelling.md](./3d-modelling.md)
