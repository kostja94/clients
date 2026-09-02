# 3D 建模工具（3D Modelling） · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**3D modelling / DCC 精修**——手工操控顶点/边/面/雕刻 + AI 辅助 mesh 精修（拓扑/UV/材质/绑骨）；验收以四边面、边流、动画变形为主。text-to-3D → [3d-model-generator.md](3d-model-generator.md)；工程 CAD/BIM → [cad.md](cad.md)；实物扫描 → [3d-scanner.md](3d-scanner.md)。完整 URL 表 **仅 §外链索引**。

**材料范围**：公开网络检索（厂商产品页、Forbes/Envato 产业评论、AOUSD 发布说明、CG Channel 与 80.lv 行业报道、arXiv 预印本与市场研究）；**未**引用 Alignify 站内 JSON 为独立来源。网摘整理日期 **2026-06-24**。

**站内对照**：[alignify.co/tools/3d-modelling](https://alignify.co/tools/3d-modelling) · [alignify.co/zh/tools/3d-modelling](https://alignify.co/zh/tools/3d-modelling) · `content/tools/en/3d-modelling.md` · `content/tools/zh/3d-modelling.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#3d-modelling-tools`](../../keywords/alignify-keywords-tools.md#3d-modelling-tools)）

**站内相邻**：[3d.md](3d.md) · [3d-model-generator.md](3d-model-generator.md) · [3d-scanner.md](3d-scanner.md) · [cad.md](cad.md)

以下条目可任意顺序阅读；**不是**文章体例。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`3d-modelling`（本页）** | **`3d-model-generator`** | **`3d-scanner`** | **`cad`** |
|------|---------------------------|---------------------------|------------------|-----------|
| **典型买家问题** | 怎么把 mesh 精修到生产级？ | 怎么凭空生成 3D？ | 怎么数字化实物？ | 怎么出可制造/施工图？ |
| **起点** | 空白画布、参考图或已有 mesh | prompt / 图片 | 物理实体 | 工程约束与参数 |
| **产出** | 精修 mesh、UV、绑定、动画就绪 | 初始 mesh + 贴图 | 点云→网格（忠实实物） | STEP、DWG、RVT |
| **验收核心** | 四边面、边流、绑骨变形 | silhouette、贴图、rig | 与原物几何偏差 | 壁厚、公差、特征可编辑 |

---

## 词汇锚点

- **3D modelling / 3D 建模（本页主轴）**：在数字空间中通过**手动操控顶点、边、面、曲线或体素**构建三维几何体的过程与工具集合——提供精确拓扑控制；与 prompt 驱动的 **3D 生成** 互补（生成出草稿，建模精修到生产级）。上下游对照见 §与相邻 slug 分流。
- **Polygon modeling / 多边形建模**：操作 vertex/edge/face 构建模型——硬表面、建筑、产品设计主流。核心技能：**边流（edge flow）、拓扑规划、细分曲面（subdivision）**。代表：Blender、3ds Max、Maya。
- **NURBS modeling / 非均匀有理 B 样条建模**：以**数学曲线和曲面**定义精确几何——天然光滑、可无限缩放。应用：工业设计、建筑曲面。代表：Rhino、Alias。与多边形差异：NURBS **数学精确**，多边形 **离散近似**。
- **Sculpting / 数字雕刻**：笔刷推拉虚拟黏土塑造有机形状——**动态细分（Dynamesh）** 实时重分布多边形密度。代表：ZBrush、Blender Sculpt Mode。
- **Retopology / 重拓扑**：高面数雕刻→动画友好低面数网格，重布局边流。2026 年 AI 重拓扑已生产可用——Maya ML Deformer、Blender AI Retopo、ZRemesher。
- **Procedural modeling / 程序化建模**：算法/规则生成几何——重复元素、大规模环境。代表：Houdini、Blender Geometry Nodes、Maya Bifrost。
- **UV mapping / UV 展开**：3D 表面展平为 2D 贴图坐标。2026 年 AI 自动 UV（接缝放置 + 岛屿打包）已实用化。
- **PBR（Physically Based Rendering）材质**：roughness、metallic、normal 等独立于光照——现代 DCC 标配；AI 可从 prompt/参考图生成全套贴图通道。
- **Rigging / 骨架绑定**：骨架层级与控制器驱动网格变形。2026 年 AI Auto-Rig（Maya MotionMaker 2026.1、Blender Auto-Rig Pro）在标准人形上准确度显著提升。
- **Level of Detail（LOD）**：不同视距不同精度变体——AI LOD 生成在 Maya、Blender、引擎中间件已成熟。
- **CAD vs DCC**：CAD（制造、BIM、STEP）→ [cad.md](cad.md)；DCC（多边形、雕刻、动画、FBX/glTF）→ 本页。Rhino 等 NURBS 按 **最终交付格式** 选 spoke。

---

## 专题对照 / 扩展定义

术语定义见 §词汇锚点；下表只列 **买家体验差**。

| 维度 | **多边形建模** | **数字雕刻** |
|------|---------------|-------------|
| **操作方式** | 逐点/线/面编辑 | 基于笔刷推拉 |
| **精度控制** | 绝对精确 | 相对自由——有机形态 |
| **典型产出** | 硬表面（机械、建筑、武器） | 有机体（角色、生物、布料） |
| **代表工具** | Maya、3ds Max、Blender | ZBrush、Blender Sculpt、Nomad Sculpt |

| 维度 | **传统手动建模** | **AI 辅助建模（2026）** |
|------|-----------------|----------------------|
| **重拓扑** | 逐面手动——数小时至数天 | AI 预测边流——分钟级 |
| **UV 展开** | 手动切缝 + 打包——数小时 | AI 接缝 + 打包——秒级 |
| **材质制作** | 手工调参或拍照采样 | prompt→全套 PBR——分钟级 |
| **绑骨** | 手动关节 + 蒙皮权重 | AI 关节放置 + 权重预测 |
| **自然语言操控** | 不存在 | Claude 连接器对话操控 Blender/Fusion 等 |

---

## 问题域

- **娱乐产业规模化生产**：AAA 游戏/视效需成千上万高品质资产——DCC 批处理与程序化是经济可行前提。
- **实时渲染爆发**：UE5 Nanite/Lumen、Unity 6 将电影级画质带入实时——对拓扑规范、LOD、材质标准提出量化要求。
- **增材制造**：CAD 拓扑优化可将零件重量降低 34–52%——航空航天/医疗植入物直接转化成本（制造向详 [cad.md](cad.md)）。
- **AI 降低入门、拉高精修天花板**：generator 数分钟出草稿——**精修/QC** 成专业分水岭；本 spoke 从「唯一生产力」转为「质量控制站」。
- **跨行业标准化**：VR/AR/MR 要求 glTF、USDZ、FBX、STEP 间流转——USD 正成为影视与工业仿真通用交换层。
- **许可模式变迁**：Autodesk 订阅（Maya ~$255/月）vs Blender 免费开源——独立电影《Flow》全程 Blender 改变「免费=业余」刻板印象。
- **云端协作与移动创作**：Shapr3D（iPad CAD，见 cad）、Nomad Sculpt（移动雕刻）将专业建模带入外勤与分布式团队。

---

## 能力栈（概念拆分，非厂商功能表）

- **建模范式覆盖度**：多边形、NURBS、细分、雕刻、程序化——选型依赖「哪类几何最接近目标形状」。
- **拓扑质量与可动画性**：**quad 优先、避免 n-gon、边流沿肌肉/机械活动线**——绑骨变形工程基础；AI 重拓扑处理中等复杂度可行，复杂角色关键变形区仍须人工。
- **UV 与纹理管线**：展 UV → 布局岛屿 → 烘焙 → 贴图——**UV 利用率**与**接缝隐蔽性**是生产级指标；有机角色面部 UV 常须人工介入。
- **PBR 材质与着色网络**：节点编辑器标配——2026 年 AI 材质进化到「prompt→完整材质网络」。
- **渲染引擎集成**：Blender Cycles/Eevee、Maya Arnold 等；**实时视口渲染**（Vulkan/Metal）2026 年已成标配。
- **骨骼与动画系统**：骨架层级→IK/FK→蒙皮权重→控制器；AI Auto-Rig 标准人形约 85–90%，非人形生物仍须手动。
- **程序化与节点工作流**：Houdini 全节点范式→Blender Geometry Nodes 大众化。
- **互操作性与交换格式**：FBX（事实标准但闭源）、glTF 2.0（Web/移动 PBR 就绪）、USD（影视/工业通用层）——须对齐轴向（Y-up vs Z-up）、单位、切线约定。
- **AI 集成深度**：插件级→内建级→**自然语言操控级**（Claude + Blender Python API / Fusion 连接器，MCP 驱动 DCC，非 text-to-3D）。
- **性能与硬件**：CPU 单核制约旧式 DCC；GPU 覆盖渲染、雕刻、AI 推理；2025 年 GPU 关税加速云端渲染管线采用。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 全能 DCC 套件（建模+动画+渲染） | 3D modelling software / DCC | Blender、Maya |
| **B** | 数字雕刻专精（数千万+ 面） | digital sculpting | ZBrush、Nomad Sculpt |
| **C** | 程序化/特效建模（全节点） | procedural modelling / VFX | Houdini、Blender Geometry Nodes |
| **D** | 游戏引擎内建模（grey boxing） | in-engine modelling | Unreal、Unity ProBuilder |
| **E** | 云端/Web 轻量 3D（交互/UI） | cloud 3D design | Spline、Womp、Vectary |
| **F** | 工程 CAD / BIM / 移动 CAD | mechanical CAD / BIM | → [cad.md](cad.md) |
| **G** | text-to-3D 生成平台 | AI 3D model generator | → [3d-model-generator.md](3d-model-generator.md) |

---

## 风险 · 合规 · 工程治理（轴特有 + 簇级链出）

簇级版权/深伪见 [3d.md](3d.md) §风险。本 slug 特有：

- **文件格式锁定**：FBX 闭源规范——USD/glTF 在 Web/移动进展明显但影视/游戏 FBX 惯性仍强；项目启动定交换格式 SSOT。
- **AI 辅助工具训练数据**：重拓扑/材质插件训练来源与商用条款须单独审查。
- **订阅成本累积**：Maya ~$255/月、3ds Max ~$235/月、ZBrush ~$40/月、Houdini ~$269/年 indie——中小团队「Blender 为主 + 按需短租商业工具」模式普遍。
- **GPU 与能源成本**：CUDA 生态依赖；云端 GPU 减少持有成本但增加传输延迟与可变账单。
- **拓扑债务**：AI 生成面数失控、三角非四边形——「AI 生成→AI 重拓扑→直接进管线」在角色面部/手部关键区仍不可靠。
- **学习曲线与团队培训**：DCC 肌肉记忆绑定 UI/快捷键——迁移产能折损应计入培训预算。
- **3D 打印与制造责任**：STL 直接生产——尺寸误差、壁厚、支撑缺陷可能在打印阶段才暴露；工程级须公差分析与干涉检查（CAD 语境见 cad）。

---

## 落地碎片

- **建模范式选择**：制造/CNC/注塑 → [cad.md](cad.md)；游戏/影视屏幕资产 → 本页多边形/雕刻。
- **Blender 优先策略**：预算敏感团队以 Blender 为核心，按需短租 Maya/ZBrush。
- **拓扑规范前置**：quad-dominant、面数上限、UV padding、命名、轴向、单位——第一版资产后再补代价是返工全部。
- **generator/scanner 导入再精修**：草稿 mesh → Blender/ZBrush 重拓扑与 UV——道具/背景已实用，主角仍常传统建模。
- **版本控制**：`.blend`/`.ma`/`.ztl` 须 Git LFS 或 Perforce；CI 可检面数、命名、UV 重叠、n-gon。
- **格式选型早于建模**：确定 FBX/USD/glTF/STEP 交付格式→反推工具与导出设置。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Blender 官方** | 开源全能 DCC（4.5 LTS，Vulkan 完整支持） | https://www.blender.org/ |
| **Autodesk Maya 产品页** | 影视/游戏绑定与动画标杆（2026.1 含 MotionMaker） | https://www.autodesk.com/products/maya/overview |
| **ZBrush（Maxon）** | 数字雕刻行业标准 | https://www.maxon.net/en/zbrush |
| **Houdini（SideFX）** | 全节点程序化建模与 VFX | https://www.sidefx.com/ |
| **Generative Design Software Market Report 2026** | 生成式设计软件市场 $2.66B→2030 $5.64B，CAGR 15.6% | https://www.researchandmarkets.com/reports/5980589/generative-design-software-market-report |
| **GenAI for 3D Assets Market Report 2025-2029** | AI 生成 3D 资产 $2.47B→2029 $7.21B，CAGR 30.7% | https://www.globenewswire.com/fr/news-release/2026/01/07/3214757/28124/en/ |
| **Forbes: How AI Is Transforming 3D Content Creation（2026-03）** | AI 重拓扑、程序化、混合工作流产业分析 | https://www.forbes.com/councils/forbestechcouncil/2026/03/19/how-ai-is-transforming-3d-content-creation/ |
| **Envato: 3D Design Trends 2026** | 8 大趋势：AI 渗透、实时渲染、跨学科融合 | https://elements.envato.com/learn/3d-design-trends |
| **Anthropic Claude Blender 连接器（WebProNews 2026-04）** | Claude 通过 Blender Python API 自然语言操控 | https://www.webpronews.com/anthropic-wires-claude-into-creatives-core-tools-nine-connectors-reshape-3d-design-and-music-workflows/ |
| **3D Modeling Type AIGC Market Forecast 2026-2032** | GII 3D 建模类 AIGC 细分数据 | https://www.giiresearch.com/report/ires1949958-3d-modeling-type-aigc-market-by-component.html |
| **CG Channel** | 3D 建模、VFX、动画行业新闻聚合 | https://www.cgchannel.com/ |
| **Khronos glTF 2.0 规范** | Web/移动 3D 开放标准——PBR、动画、骨骼 | https://registry.khronos.org/glTF/ |
| **Pixar USD 官方文档** | 影视/工业仿真通用场景描述格式 | https://openusd.org/ |

### 对比与测评（第三方；观点非官方）

- **Blender 4.5 LTS** 功能完整度与 Maya/3ds Max 多数环节相当——差距在 Studio 级 USD 深度与高端绑骨。
- **ZBrush** 雕刻领域积累二十年——Blender Sculpt 面数上限与笔刷响应有差距，非专业用途已够用。
- **Rhino / FreeCAD / Fusion** CAD 横评见 [cad.md](cad.md) §对比与测评。
- **Houdini** 程序化能力碾压——Blender Geometry Nodes 为免费替代但缺 FLIP/Pyro 深度。
- **2026 混合工作流已是主流**——道具/背景 generator/scanner 草稿 + 本 spoke 精修；主角仍依赖传统建模。生成选型见 [3d-model-generator.md](3d-model-generator.md)。

*本小节为行业观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **Blender Studio 开放项目**：https://studio.blender.org/films/
- **80 Level**：https://80.lv/
- **Polycount Wiki**：http://wiki.polycount.com/
- **ArtStation Learning**：https://www.artstation.com/learning
- **Open3D Lab / Hunyuan3D-2.0**（2025-03 开源，text/image→3D）
- **GDC Vault**：https://www.gdcvault.com/

**站内**

- Hub：[3d.md](3d.md)
- 生成：[3d-model-generator.md](3d-model-generator.md)
- 工程 CAD：[cad.md](cad.md)
- 扫描：[3d-scanner.md](3d-scanner.md)