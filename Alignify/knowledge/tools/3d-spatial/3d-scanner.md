# AI 3D Scanner · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI 3D scanner / 实物数字化**——照片/LiDAR/视频→点云/网格/splat；验收以与原物几何偏差、采集完整度为主。文/图生 3D → [3d-model-generator.md](3d-model-generator.md)；DCC 精修 → [3d-modelling.md](3d-modelling.md)。**3DGS/NeRF/摄影测量对比表 SSOT 在本页**；格式基础设施摘要见 [3d.md](3d.md) §共享事实速查；完整 URL 表 **仅 §外链索引**。

**材料范围**：公开网络检索（厂商产品页、AOUSD/Khronos 格式公告、学术论文与预印本、ISPRS/行业白皮书、KIRI 官方对比文）；**未**引用 Alignify 站内 JSON 正文为论据。网摘整理日期 **2026-06-24**。

**站内对照**：[alignify.co/tools/3d-scanner](https://alignify.co/tools/3d-scanner) · [alignify.co/zh/tools/3d-scanner](https://alignify.co/zh/tools/3d-scanner) · `content/tools/en/3d-scanner.md` · `content/tools/zh/3d-scanner.md` · slug **`3d-scanner`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#3d-scanner-tools`](../../keywords/alignify-keywords-tools.md#3d-scanner-tools)

**站内相邻**：[3d.md](3d.md) · [3d-model-generator.md](3d-model-generator.md) · [3d-modelling.md](3d-modelling.md) · [cad.md](cad.md)

以下条目可任意顺序阅读；**不是**文章体例。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`3d-scanner`（本页）** | **`3d-model-generator`** | **`3d-modelling`** |
|------|--------------------------|--------------------------|-------------------|
| **典型买家问题** | 怎么把实物变成 3D？ | 怎么凭空生成 3D？ | 怎么精修到生产级？ |
| **数据来源** | 实物（拍照、LiDAR、视频） | prompt / 图片 | 空白或已有 mesh |
| **验收核心** | 与原物几何偏差（mm/cm） | silhouette、贴图 | 四边面、边流、动画 |

---

## 词汇锚点

- **AI 3D Scanner（本页主轴）**：利用 AI/ML 将**实物**（照片序列、LiDAR、视频帧）转化为**三维数字模型**的工具。英文常检索 **3D scanner app**、**AI 3D reconstruction**、**photogrammetry app**、**Gaussian splatting scanner**；与传统专用扫描仪差异：可工作于**非专用硬件**（普通手机），且可输出 NeRF/3DGS 等新型表示。
- **Photogrammetry / 摄影测量（SfM）**：多角度照片特征匹配+三角测量重建几何——最成熟路线，配控制点/RTK 可达 **1–3 cm**；透明/反光/无纹理表面几乎无效。AI 语境指深度学习增强特征匹配、深度估计、网格补全。
- **NeRF（Neural Radiance Fields）**：场景编码进神经网络权重，逐像素光线追踪合成新视角（Mildenhall et al., ECCV 2020）。擅长复杂光照/半透明/反射；训练渲染慢，输出不可直接编辑网格——2025–2026 逐渐被 3DGS 在渲染速度上超越。
- **3D Gaussian Splatting（3DGS）**：数百万有方向 3D 高斯椭球，**实时 60+ FPS** 渲染（Kerbl et al., 2023）。擅长植被、玻璃、反射、头发；几何精度多为**可视化级**（数厘米偏差）。格式基础设施（OpenUSD v26.03、glTF KHR_gaussian_splatting RC）见 [3d.md](3d.md) §共享事实速查。
- **3DGS-to-Mesh Conversion**：GS→传统多边形网格（OBJ/glTF）AI 管线——KIRI Engine 首创；使 splat 可进 DCC，转换后精度仍常为可视化级。
- **Neural Surface Reconstruction（NSR）**：学习隐式表面函数（SDF）直接提取网格——KIRI「Neural Surface」模式；兼顾 NeRF 光照鲁棒性与网格可编辑性。
- **LiDAR Scanner**：ToF/相位差测距输出点云——iPhone Pro（12 代起）/ iPad Pro 内置 LiDAR 使消费级门槛归零；现代 LiDAR app 用 AI 做点云去噪、网格重建、语义分割。
- **SLAM**：移动中同时定位与建图——手持/移动扫描核心；AI-SLAM 融合 IMU+视觉+深度，GPS 拒止环境厘米级定位（Artec Jet 2026 全自主扫描）。
- **Digital Twin / 数字孪生**：物理实体/环境的实时三维副本——扫描是主要数据入口；2026 趋势是与 IoT 数据流融合（Siemens、ABB Genix + Omniverse）。
- **Guided Scan / AI 扫描引导**：端侧 AI 实时评估扫描质量——标记缺失面、提示角度/照明（HoloTwin Guided Scan Intelligence™）。
- **On-Device Processing / 端侧处理**：手机/平板本地处理不上云——PocketGS（iPhone 15，<5 min、<3 GB）、Scaniverse 端侧 GS；意义：隐私、即时反馈、无网可用。
- **4D Capture**：运动物体/场景时序重建——MoBluRF（模糊手机视频）、StreamSplat（ICLR 2026 动态 GS 实时）。

---

## 专题对照 / 扩展定义

路线定义见 §词汇锚点；下表只列 **买家选型差**。

| 维度 | **Photogrammetry** | **NeRF** | **3D Gaussian Splatting** |
|------|-------------------|----------|--------------------------|
| **输出格式** | 网格/点云（可编辑） | 神经网络权重 | 高斯点云（SuperSplat 等可编辑） |
| **渲染速度** | N/A（导出外部渲染） | 慢（分钟级） | **实时 60+ FPS** |
| **材质处理** | 反光/透明/无纹理失败 | 擅长复杂光照 | 擅长植被、玻璃、反射、头发 |
| **测量精度** | **高**（测量级） | 中等 | 可视化级（~7.82 cm 均值） |
| **2026 成熟度** | 工业标准 | 视效 niche | **主流**（USD/glTF 基础设施化） |

| 维度 | **消费级 app（手机）** | **专业手持/地面扫描仪** | **企业数字孪生平台** |
|------|----------------------|------------------------|---------------------|
| **硬件** | 手机摄像头 + 可选 LiDAR | 结构光/激光/多相机阵列 | 无人机/地面仪 + 云管线 |
| **精度** | 1–5 cm（视觉）/ 0.5–2 cm（LiDAR） | 0.005 mm–2 cm | 1–3 cm（无人机 SfM + GCP） |
| **典型用户** | 创作者、3D 打印、小型电商 | 逆向工程、质检、文化遗产 | 工厂、基建、智慧城市 |
| **AI 价值** | 非专用硬件提升到可用精度 | AI 引导 + 自动分类 | AI 语义分割 + IoT 融合 |

**精度层次 SSOT**：测量级（结构光/计量，±0.005 mm–2 cm）→ 工程级（LiDAR+GCP，±1–5 cm）→ 可视化级（手机 GS，±5–10 cm）→ 示意级（电商展示）。Hub 摘要见 [3d.md](3d.md) §共享事实速查。

---

## 问题域

- **3D 内容需求 vs 手工供给**：游戏、XR、电商、数字孪生、机器人仿真对三维资产需求激增——「每个人都需要 3D，但没几个人会做 3D」。
- **硬件门槛坍塌**：2020 年起 iPhone LiDAR、Android ToF——硬件非壁垒，**算法（AI）** 成差异化核心。
- **NeRF/3DGS 突破摄影测量天花板**：反光、透明、植被、毛发等材质——GS 用概率表示绕过刚体几何假设。
- **数字孪生从演示到运维**：工业界要求扫描不止几何准确，还要**语义丰富**与**可查询**（NL 搜索空间对象）。
- **端侧 AI 芯片成熟**：Neural Engine / Hexagon NPU 使 PocketGS 类手机端 GS 训练可行——否则被迫依赖云端（延迟、隐私、网络）。
- **Physical AI 训练数据**：机器人/自驾/机械臂需海量三维环境数据——NVIDIA Isaac Sim、Deep Insight DIMENVUE 将扫描仪定位为 Physical AI 数据基础设施。
- **电商与社交 3D 化**：Amazon/Shopify 3D 展示、Vision Pro 空间内容——需「手机拍一圈出 3D」，快、好看、易分享。

---

## 能力栈（概念拆分，非厂商功能表）

- **采集模态**：单目 RGB、多目、LiDAR ToF、结构光（ChaoXiLi AiScan O1 **0.005 mm**）、视频帧（MoBluRF 支持模糊视频）、无人机航拍（DJI Terra 30K 图批处理）。
- **重建算法**：SfM+MVS、NeRF、3DGS、NSR、Hybrid（LiDAR 几何 + GS 纹理——Xgrids L2 Pro、HoloTwin）。
- **输出格式**：点云（PLY/LAS）、网格（OBJ/STL/glTF/FBX/USD）、GS PLY、NeRF 权重；语义层（物体标签、BIM 构件映射）。
- **AI 增强**：SuperPoint/D2-Net 特征匹配、单目深度补全 LiDAR 盲区、语义分割、扫描引导、3DGS-to-Mesh。
- **端侧 vs 云端**：完全端侧（PocketGS、Scaniverse）、云端（Luma AI、DJI Terra）、混合（KIRI：端侧缓存→WiFi 云端优化）。
- **实时性**：离线批处理（分钟–小时）、近实时（PocketGS <5 min）、实时 SLAM 预览。
- **场景规模**：单物体（30–150 张）→ 房间级（1–5 min）→ 建筑/工厂级（DJI Terra、Xgrids 30K）→ 城市级（Voyager 流式 GS）。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 消费级通用 app（拍照为主，iOS+Android） | mobile 3D scan app | KIRI Engine、Polycam |
| **B** | Apple LiDAR 生态专用 | lidar room scanner | Scaniverse、Dot3D、SiteScape、Canvas |
| **C** | NeRF/GS 品质优先（视觉>几何） | NeRF scanner / gaussian splatting app | Luma AI、PostShot、SuperSplat |
| **D** | Prosumer 手持专用扫描仪 | handheld 3D scanner | 3DMakerPro、ChaoXiLi AiScan O1 |
| **E** | 工业级/计量级 | 3D metrology / laser scanner | Artec、Xgrids L2 Pro、Deep Insight DIMENVUE |
| **F** | 无人机 + AI 大规模建模 | drone photogrammetry | DJI Terra、ContextCapture、Pix4D |
| **G** | 企业数字孪生平台（扫描为数据入口） | digital twin / reality capture | Siemens、ABB Genix、HoloTwin |
| **H** | 开源/研究框架 | nerfstudio / gsplat | Nerfstudio、PocketGS、SplatForge |

---

## 风险 · 合规 · 隐私与安全（轴特有 + 簇级链出）

簇级版权/深伪见 [3d.md](3d.md) §风险。本 slug 特有：

- **扫描他人空间/物体合法性**：私人空间、受版权/设计专利保护物品涉及侵权；欧盟 freedom of panorama 因成员国而异。
- **Biometric 数据**：面部 3D 扫描属 GDPR **特殊类别数据**——须明确同意；EM3D 等声明不上传/不训练。
- **云端处理 = 数据离开本地**：工厂产线、未公开原型、敏感设施须 **端侧处理**（PocketGS、Scaniverse）。
- **3DGS/NeRF 无意信息泄露**：反射面可能暴露拍摄者/窗外可定位地标——尚无成熟自动匿名化。
- **扫描质量 ≠ 法律效力**：手机 app 结果**非**法定测量工具——产权/法医/验收须 ISO 17025 认证设备。
- **军事/敏感设施**：关键基础设施周边无人机/3D 扫描多国禁令——合规责任在用户。

---

## 落地碎片

- **先手机摄像头测试，再决定是否买 LiDAR**：纹理丰富小物体可能不需 LiDAR；大面积室内/弱纹理白墙/厘米级测量才需 LiDAR。
- **光泽/透明物体先喷粉或贴标记点**：AESUB 等自挥发显像剂是低成本方案。
- **3DGS 用于分享/展示，Photogrammetry 用于编辑/测量**：GS 发社交/嵌入网页；Blender 编辑/3D 打印/逆向工程走摄影测量 OBJ/STL。
- **视频比独立照片更快**：15–30 秒慢速环绕通常优于 50–100 张独立照——但须避免运动模糊。
- **Diffuse/均匀光照 > 硬阴影**：阴天户外最佳；硬阴影会烘焙进纹理。
- **扫描完整度 > 分辨率**：80 张覆盖所有死角优于 300 张只拍前/侧面。
- **信任 AI 扫描引导避免返工**：HoloTwin 类 app 现场补拍 2 分钟优于事后重跑。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

### 工具与产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| **KIRI Engine** | Photogrammetry + NeRF NSR + 3DGS 三模式，首创 GS→Mesh，v4.0 取消导出限制 | [kiriengine.app](https://www.kiriengine.app) |
| **Polycam** | 跨平台 iOS/Android/Web，Explore 库数百万公开模型，GS + LiDAR + 摄影测量 | [poly.cam](https://poly.cam) |
| **Scaniverse**（Niantic） | 首个端侧 3DGS 消费级 app，完全免费 | [scaniverse.com](https://scaniverse.com) |
| **Luma AI** | NeRF 渲染品质标杆，iOS only，免费云端；**Luma Genie（text→场景）** 属 generator | [lumalabs.ai](https://lumalabs.ai) |
| **Dot3D** | 专业 LiDAR——SLAM 回环、AprilTag、NeRF/GS 帧导出 | [dotproduct3d.com](https://www.dotproduct3d.com) |
| **SiteScape** | AEC/BIM LiDAR app，E57/RCP 导出 | [sitescape.ai](https://www.sitescape.ai) |
| **Canvas** | LiDAR→CAD（Revit/SketchUp），按平方英尺计费 | [canvas.io](https://www.canvas.io) |
| **3DMakerPro Eagle / Raven** | Prosumer 手持 200K pts/sec，2 cm 精度，Raven 2026-03 原生 GS PLY/OBJ | [3dmakerpro.com](https://www.3dmakerpro.com) |
| **ChaoXiLi AiScan O1** | 结构光 0.005 mm + AI GS 双模式自动切换 | [chaoxili.com](https://www.chaoxili.com) |
| **Artec 3D**（Leo / Spider II / Ray II / Jet） | 工业计量 0.01 mm 起；Jet（2026）AI-SLAM 全自主 | [artec3d.com](https://www.artec3d.com) |
| **Xgrids L2 Pro** | 手持 SLAM + GS，640K pts/sec，±1–2 cm，唯一 GS→Revit BIM 插件 | [xgrids.com](https://www.xgrids.com) |
| **Deep Insight DIMENVUE** | 韩国 WIS 2026 获奖，LiDAR + 3DGS，Physical AI 数据基础设施 | 厂商未公开官网（2026-04 参展阶段） |
| **DJI Terra v5.2** | 无人机 30K 图 SfM→GS，3DTiles/PLY/GeoTIFF | [enterprise.dji.com/dji-terra](https://enterprise.dji.com/dji-terra) |
| **HoloTwin HT Scan** | CES 2026 获奖，Hybrid Reality Capture + Guided Scan Intelligence | [holotwin.com](https://www.holotwin.com) |

### 开发者/开源

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Nerfstudio + gsplat** | NVIDIA 支持开源 NeRF/GS 框架 | [docs.nerf.studio](https://docs.nerf.studio) |
| **PostShot**（Jawset） | 桌面 GS 重建，ISPRS 2026 Caserta 文化遗产案例 | [jawset.com](https://www.jawset.com) |
| **SuperSplat**（PlayCanvas） | 免费浏览器 GS 编辑器 | [playcanvas.com/supersplat](https://playcanvas.com/supersplat) |
| **SplatForge** | $49 Blender 插件，视口内 1600 万 splat | Blender Market 搜索 |

### 对比与测评（第三方；观点非官方）

- **消费级 app**：KIRI 差异化 **GS→Mesh** 与 v4.0 导出策略；Polycam 跨平台+Explore 库；Scaniverse **端侧 GS + 免费**；Luma NeRF 复杂光照仍常被引为画质标杆但更新慢于 KIRI/Polycam。
- **精度是否够用**：3D 打印 hobbyist 常接受 **1–3 mm**；机械装配/逆向工程需计量级；手机 GS 与 GS-to-Mesh 默认 **可视化级**，工程测量走摄影测量+GCP 或计量仪。
- **LiDAR vs 纯视觉**：室内大空间/白墙 LiDAR 融合通常优于纯视觉；纹理丰富小物体均匀光照下纯视觉可表现良好。
- **企业级**：2026 差异化更多在 **语义标注 + BIM/IoT 融合**（Siemens、ABB Genix + Omniverse），非仅硬件精度极限。

*本小节为行业观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- [Gaussian Splatting: The Complete Guide (2026)](https://www.thefuture3d.com/gaussian-splatting/)
- [Best Free 3D Scanner Apps (2026)](https://www.kiriengine.app/blog/Best_Free_3D_Scanner_Apps_2026)
- [The Spatial Enterprise: Digital Twins at AWE USA 2026](https://www.awexr.com/blog/1333-the-spatial-enterprise-how-digital-twins-and-reali)
- **论文**：Kerbl et al. 2023（GS 基础）；Mildenhall et al. 2020（NeRF）；PocketGS（2026-01）；Auto3R（2026-04）；IGFuse（AAAI 2026）；Voyager（2025）；MoBluRF（2025）
- [Siemens Digital Twin Composer — CES 2026](https://www.automation.com/article/siemens-industrial-metaverse-life-digital-twin-composer)（PepsiCo：20% 吞吐提升、10–15% CapEx 降低）
- [OpenUSD v26.03](https://aousd.org/blog/openusd-v26-03/) · [Khronos KHR_gaussian_splatting RC](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_gaussian_splatting)

**站内**

- Hub：[3d.md](3d.md)
- 生成：[3d-model-generator.md](3d-model-generator.md)
- 精修：[3d-modelling.md](3d-modelling.md)