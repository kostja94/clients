# 3D 建模工具（3D Modelling） · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、Forbes/Envato 产业评论、AOUSD 发布说明、CG Channel 与 80.lv 行业报道、arXiv 预印本与市场研究）；**未**引用 Alignify 站内 JSON 为独立来源。网摘整理日期 **2026-06-24**。**主轴词**：**3D modelling / 3D modeling**；与 **3D 生成**、**3D 扫描** 在工程链路上相邻但检索意图可分。

**站内对照**：[alignify.co/tools/3d-modelling](https://alignify.co/tools/3d-modelling) · [alignify.co/zh/tools/3d-modelling](https://alignify.co/zh/tools/3d-modelling) · `content/tools/en/3d-modelling.json` · `content/tools/zh/3d-modelling.json`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#3d-modelling-tools`](../../keywords/alignify-keywords-tools.md#3d-modelling-tools)）

**站内相邻**：[3d.md](./3d.md) · [3d-model-generator.md](./3d-model-generator.md) · [3d-scanner.md](./3d-scanner.md) · [cad.md](./cad.md)

**内容边界**：本 slug 主责 **DCC 手工建模 + AI 辅助 mesh 精修**（拓扑/UV/材质/绑骨/雕刻）；text-to-3D 见 [3d-model-generator.md](./3d-model-generator.md)；**工程 CAD/BIM/text-to-CAD** 见 [cad.md](./cad.md)；实物扫描见 [3d-scanner.md](./3d-scanner.md)。完整分工见 [3d.md](./3d.md) §内容分工。

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **3D modelling / 3D 建模（本知识块主标签）**：在数字空间中通过**手动操控顶点、边、面、曲线或体素**来构建三维几何体的过程与工具集合。与完全依赖 prompt 的 **3D 生成（3D model generation / text-to-3D）** 不同——建模工具提供精确的拓扑控制，而生成工具输出的是不可预测的几何。在实际工作流中两者常互补：生成工具出草稿，建模工具精修。
- **Polygon modeling / 多边形建模**：操作顶点（vertex）、边（edge）、面（face）构建模型——是 3D 建模最基础和通用的范式。适合硬表面模型（hard-surface）、建筑、产品设计。核心技能包括**边流（edge flow）控制、拓扑（topology）规划、细分曲面（subdivision surface）**。代表工具：Blender、3ds Max、Maya。
- **NURBS modeling / 非均匀有理B样条建模**：以**数学曲线和曲面**定义精确几何——天然光滑、可无限缩放而不损失精度。核心应用：工业设计（汽车外壳、消费品）、建筑曲面（Gehry-style 自由形态）。代表工具：Rhinoceros（Rhino）、Alias。与多边形建模的关键差异：NURBS 是**数学精确**的，多边形是**离散近似**的。
- **Sculpting / 数字雕刻**：以类似雕塑的方式**推、拉、平滑、切割**虚拟黏土来塑造有机形状——每一笔可操控数百万至数千万多边形。适合角色设计、生物建模、高细节道具。核心概念：**动态细分（Dynamesh / dynamic tessellation）**——在雕刻时实时重分布多边形密度，使艺术家不被拓扑约束束缚。代表工具：ZBrush、Blender Sculpt Mode。
- **Retopology / 重拓扑**：将高面数雕刻模型（数千万面）转换为**动画友好的低面数网格**（数千至数万面）——重新布局边流以匹配肌肉运动线、关节变形区域和面部表情肌。2026 年 AI 重拓扑（auto-retopology）已从实验走向生产——Maya 的 ML Deformer、Blender 的 AI Retopo 插件、ZBrush 的 ZRemesher 通过机器学习预测最优边流分布。
- **Procedural modeling / 程序化建模**：使用**算法、规则和参数**而非手动操作生成几何体——特别适合重复元素（建筑立面、植被）、大规模环境（城市、森林）和可参数化结构。2026 年趋势：AI 在确定性程序化系统之上增加「建议层」——在保持艺术家控制的同时自动生成变体。代表工具：Houdini、Blender Geometry Nodes、Maya Bifrost。
- **UV mapping / UV 展开**：将 3D 模型表面**展平为 2D 坐标**以贴附纹理贴图——三维空间坐标记为 XYZ，二维纹理坐标记为 UV。2026 年 AI 自动 UV 展开已实用化——通过学习的接缝放置（seam placement）和岛屿打包（island packing）在数秒内完成原本数小时的手动工作。
- **PBR（Physically Based Rendering）材质**：基于物理的光照模型——材质属性（粗糙度 roughness、金属度 metallic、法线 normal、高度 height 等）独立于光照环境，在不同引擎间一致性高。现代 DCC 工具普遍内置 PBR 材质节点和纹理烘焙管线。2026 年 AI 辅助 PBR 材质生成可**从文本 prompt 或单张参考图**直接生成全套贴图（base color、roughness、metallic、normal、height）。
- **Rigging / 骨架绑定**：为 3D 模型建立**骨架层级和控制器**以便动画师操控——骨架的旋转/位移驱动网格变形。2026 年 AI 自动绑定（Auto-Rig）进步显著：Maya 的 MotionMaker（2026.1）、Blender 的 Auto-Rig Pro 插件可通过机器学习自动放置关节、设置蒙皮权重。
- **Level of Detail（LOD）**：为不同视距生成**不同精度的模型变体**——近景用高面数、远景用低面数以优化实时渲染性能。AI LOD 生成是 2026 年的成熟功能——Maya、Blender 和游戏引擎中间件都能自动生成多级 LOD。
- **CAD vs DCC**：**CAD**（制造、BIM、STEP）主归属 [cad.md](./cad.md)；**DCC**（多边形、雕刻、动画、FBX/glTF）主归属本页。Rhino 等 NURBS 工具在制造与视觉交汇——按 **最终交付格式** 选 spoke。
- **3D modelling vs 3D model generation（3D 生成）**：建模工具提供**手动的、拓扑精确的、动画就绪的**最终模型；生成工具输出**自动的、拓扑不可控的、需后处理的**初始草稿。二者不是替代关系，而是上下游——AI 生成快速出概念，建模工具精修到生产级。详见 [3d-model-generator.md](./3d-model-generator.md) 和 [3d.md](./3d.md)。

---

## 专题对照 / 扩展定义

| 维度 | **3D modelling（本文件）** | **3D 扫描（3D scanning）** |
|------|---------------------------|----------------------------|
| **起点** | 空白画布或参考图 | 物理实体 |
| **产出性质** | 主观创作——艺术家可控 | 客观捕捉——几何忠实于实物 |
| **后处理** | 直接产出最终资产 | 需建模工具精修（补洞、重拓扑、UV） |
| **知识块** | 本页 | [3d-scanner.md](./3d-scanner.md) |

| 维度 | **3D modelling（本文件）** | **3D 生成（text-to-3D）** |
|------|---------------------------|---------------------------|
| **输入** | 艺术家手动操作或参考三视图 | 文本 prompt 或单张图片 |
| **拓扑质量** | 精确可控——四边形为主、边流合理 | 不保证——常为三角形乱网 |
| **动画就绪** | 可设计绑骨友好拓扑 | 需重拓扑后才能进入动画管线 |
| **速度** | 小时至天级 | 秒至分钟级 |
| **适合场景** | 生产级资产 | 概念探索、背景资产、草稿 |

| 维度 | **多边形建模** | **数字雕刻** |
|------|---------------|-------------|
| **操作方式** | 逐点/线/面编辑 | 基于笔刷的推拉 |
| **精度控制** | 绝对精确——每个顶点可数控 | 相对自由——适合有机形态 |
| **典型产出** | 硬表面（机械、建筑、武器） | 有机体（角色、生物、布料褶皱） |
| **代表工具** | Maya、3ds Max、Blender | ZBrush、Blender Sculpt Mode、Nomad Sculpt |

| 维度 | **通用 DCC（Maya、Blender）** | **工程 CAD（见 `cad`）** |
|------|-------------------------------|------------------------------|
| **核心能力** | 建模 + 动画 + 渲染 | 参数化精确 + 工程图/BIM |
| **典型用户** | 影视/游戏美术师 | 机械/建筑工程师 |
| **输出格式** | FBX、glTF、USD | STEP、DWG、RVT |
| **知识块** | 本页 | [cad.md](./cad.md) |

| 维度 | **传统手动建模** | **AI 辅助建模（2026）** |
|------|-----------------|----------------------|
| **重拓扑** | 逐面手动铺设——数小时至数天 | AI 预测边流——分钟级 |
| **UV 展开** | 手动切缝 + 打包——数小时 | AI 接缝放置 + 自动打包——秒级 |
| **材质制作** | 手工调参数或拍照采样 | prompt→全套 PBR 贴图——分钟级 |
| **绑骨** | 手动放关节 + 画蒙皮权重 | AI 自动关节放置 + 权重预测 |
| **自然语言操控** | 不存在 | 2026 年 Claude 连接器可通过对话操控 Blender、Fusion 等 |

---

## 问题域（为何会出现这类产品）

- **物理世界的数字化需求**：建筑可视化需要将设计方案转为客户可「走进」的 3D 空间；产品设计需要在开模前验证结构和外观——数字孪生（digital twin）的精度要求推动 CAD 与 DCC 工具深度整合。
- **娱乐产业的规模化生产**：电影视效、AAA 游戏需要成千上万的高品质 3D 资产——单个主角可能耗时数月，而场景道具需要量产。DCC 工具的批处理和程序化能力直接从「职业可行性」变为「经济可行性」的前提。
- **实时渲染的爆发**：Unreal Engine 5（Nanite、Lumen）、Unity 6 等引擎将**电影级画质带入实时**——对 3D 资产的拓扑规范、LOD 层级、材质标准提出了新的量化要求。建模工具必须适配引擎的尺度单位、切线基、命名约定。
- **增材制造（3D 打印）将数字推向物理**：CAD 建模工具从视觉可视化扩展到制造就绪——拓扑优化（生成式设计）可将零件重量降低 34–52% 同时保持强度，这在航空航天和医疗植入物领域直接转化为材料成本和燃油效率。
- **AI 降低入门门槛，但拉高精修天花板**：AI 生成（见 [3d-model-generator.md](./3d-model-generator.md)）数分钟产出草稿——**精修/QC** 成为专业分水岭；本 spoke 角色从「唯一生产力」转为「质量控制站」。
- **跨行业标准化压力**：VR/AR/MR 的普及要求 3D 内容在 Web（glTF）、移动端（USDZ）、引擎内（FBX）和制造端（STEP）之间无损流转。USD（Universal Scene Description）格式正成为影视和工业仿真的通用交换层。
- **软件许可模式的变迁**：2025–2026 年间，Autodesk 等厂商继续推订阅制（Maya ~$255/月），而 Blender 作为免费开源全能套件完成了从「爱好者工具」到「电影级制作工具」的蜕变——独立电影《Flow》全程使用 Blender 制作，改变了行业对「免费=业余」的刻板印象。
- **云端协作与移动创作**：Shapr3D（iPad）、Nomad Sculpt（iPad/Android）等工具将专业建模能力带入移动端；云端工作流使分布式团队可实时协作——这对建筑、汽车等跨地域设计团队的日常运作影响深远。

---

## 能力栈（概念拆分，非厂商功能表）

- **建模范式覆盖度**：多边形、NURBS、细分曲面、雕刻、程序化——现代 DCC 以多边形+雕刻为主；CAD 以 NURBS + 实体为主。**选择依赖的不是「哪种更强」而是「哪类几何最接近你的目标形状」**。
- **拓扑质量与可动画性**：**四边形（quad）优先、避免 n-gon（5边以上）、边流沿肌肉/机械活动线**——这是绑骨和变形的工程基础。AI 重拓扑在 2026 年已可处理中等复杂度模型，但复杂角色的关键变形区仍依赖人工判断。
- **UV 与纹理管线**：展 UV → 布局岛屿 → 烘焙（bake）→ 贴图绘制——**UV 利用率**和**接缝隐蔽性**是生产级指标。AI 自动 UV 在硬表面模型上表现优秀（准确率高），在有机角色上仍需人工介入（面部 UV 需特定布局以最大化贴图分辨率）。
- **PBR 材质与着色网络**：节点编辑器（node graph）成为标配——Blender Shader Nodes、Maya Hypershade、Substance Designer。2026 年 AI 材质从「prompt→贴图」进化到「prompt→完整材质网络」，支持 procedural noise 组合和 height-based blending。
- **渲染引擎集成**：DCC 工具普遍集成或绑定渲染器——Blender Cycles/Eevee、Maya Arnold、3ds Max Arnold/V-Ray、Cinema 4D Redshift。**实时视口渲染（viewport rendering）** 通过 Vulkan/Metal GPU API 在 2026 年已成标配——艺术家可在近似最终效果的环境中建模。
- **骨骼与动画系统**：骨架层级（skeleton hierarchy）→ IK/FK 切换 → 蒙皮权重（skinning weights）→ 动画控制器（rig controls）。2026 年 AI Auto-Rig 的准确度在标准人形角色上达 85–90%，非人形生物仍需手动绑定。
- **程序化与节点工作流**：从 Houdini 的全节点范式到 Blender Geometry Nodes、Maya Bifrost——程序化建模在 2026 年不再是「小众高级用法」，而是批量生产场景和复杂环境的主流方式。节点网络使得修一个参数即可更新全部衍生几何。
- **互操作性与交换格式**：FBX（Autodesk，实际行业标准但闭源，约 600KB 规范文档）、glTF 2.0（Khronos，开源，Web/移动端首选，PBR 就绪）、USD（Pixar，影视和工业仿真通用层）——选型时需提前对齐上下游管线对轴向（Y-up vs Z-up）、缩放单位（米 vs 厘米）、切线方向的约定。
- **AI 被集成深度**：**插件级**（Blender AI 重拓扑插件）→ **内建级**（Maya ML Deformer、ZRemesher）→ **自然语言操控级**（2026 年 Anthropic Claude 通过 Blender Python API / Autodesk Fusion 连接器——MCP 协议驱动 DCC，非 text-to-3D 生成）。
- **性能与硬件绑定**：CPU 单核性能制约旧式 DCC（许多操作仍单线程）；GPU 加速覆盖渲染、雕刻细分、AI 推理（CUDA/Metal）。2025 年美国 GPU 关税推高了本地渲染农场成本，加速了云端 GPU 渲染管线的采用。

---

## 形态谱系（与具体品牌解耦）

- **全能 DCC 套件**：Blender（开源免费，2026 年 4 月 Claude 连接器上线）——覆盖建模、雕刻、动画、渲染、合成全流程；独立电影制作的首选工具。Autodesk Maya（订阅制，~$255/月）——影视和 AAA 游戏的动画与绑骨标杆；Bifrost 程序化平台覆盖特效与体积模拟。
- **数字雕刻专精**：ZBrush（订阅制）——有机角色和生物雕刻的行业标准，可操控数千万多边形；Python 脚本支持（2026 版）使其可接入程序化管线。Nomad Sculpt（移动端，一次性买断 ~$20）——iPad/Android 上专业级雕刻体验，与桌面工具的差距快速缩小。
- **工业/CAD 精确建模**：Fusion、SolidWorks、Rhino、Revit、Shapr3D 等——完整谱系与 URL 表见 [cad.md](./cad.md)。
- **移动端 DCC 雕刻**：Nomad Sculpt（iPad/Android）——有机雕刻；**移动 CAD** 见 [cad.md](./cad.md)（Shapr3D）。
- **程序化/特效建模**：Houdini（SideFX，按年订阅）——全节点程序化工作流，VFX 行业的特效/环境生成标准；集成 AI 辅助的模拟加速。Blender Geometry Nodes（免费）——将 Houdini 级程序化范式引入大众工具，2026 年社区资源丰富。
- **建筑快速草模 / BIM**：SketchUp、Revit 等——工程与 BIM 叙述见 [cad.md](./cad.md)；本页不重复施工数据流。
- **云端/浏览器轻量 3D**：Spline、Womp、Vectary——浏览器内轻量设计与 Web 导出（交互/UI 向）；**text-to-3D 生成平台**（Tripo/Meshy/Rodin）见 [3d-model-generator.md](./3d-model-generator.md)。
- **游戏引擎内建模**：Unreal Engine（Epic，免费至 $185K 收入）——Nanite 虚拟几何体使数十亿面模型无需 LOD；内建建模和地形编辑工具日趋完善。Unity（免费至 $200K 收入）——ProBuilder 和 Polybrush 提供基础建模和雕刻能力，适合快速关卡搭建（grey boxing）。

---

## 风险 · 合规 · 工程治理（轴特有 + 簇级链出）

簇级版权/深伪见 [3d.md](./3d.md) §风险。本 slug 特有：

- **文件格式锁定（vendor lock-in）**：Autodesk FBX 是事实行业标准但规范闭源——依赖逆向工程维护互操作；USD 与 glTF 2.0 在 Web/移动端进展明显但影视/游戏管线 FBX 惯性仍强。**建议**在项目启动时明确交换格式与轴向/单位约定。
- **AI 辅助工具训练数据**：AI 重拓扑/材质插件的训练数据来源与商用条款需单独审查；Adobe Firefly 的版权赔偿担保模式是否向 DCC 扩散仍待观察。
- **订阅成本累积**：Maya（~$255/月）、3ds Max（~$235/月）、ZBrush（~$40/月）、Houdini（~$269/年 indie）——专业团队的年度软件成本可在数万美元量级。Blender 的免费策略使「以 Blender 为主 + 按需短租商业工具」的混合模式在中小团队中越来越普遍。
- **GPU 硬件与能源成本**：高端渲染和 AI 推理依赖 CUDA 生态（NVIDIA）——2025 年 GPU 关税和供应链波动推高了本地部署成本。云端 GPU 渲染减少了硬件持有成本但增加了传输延迟和月度账单的可变因素。
- **拓扑债务（topology debt）**：AI 生成的模型面数失控、三角形非四边形、边流混乱——在影视/游戏的动画管线中需要投入重拓扑工时。2026 年的 AI 重拓扑虽已大幅进步，但「AI 生成 → AI 重拓扑 → 直接进入管线」的完全自动化链路在涉及角色面部、手部等关键变形区时仍不可靠。
- **学习曲线与团队培训**：DCC 工具的肌肉记忆高度绑定特定 UI 和快捷键——从 Maya 迁移到 Blender 或反之，即使概念可转移，生产速度会因肌肉记忆重置而大幅下降。培训预算不应只算许可证费用，还应包含上手期产能折损。
- **3D 打印与制造责任**：从建模工具直接输出 STL 到生产——尺寸误差、壁厚不足、支撑结构设计缺陷等问题可能在数字模型阶段不可见，在打印或 CNC 加工时才暴露。工程级建模需要内置公差分析（tolerance analysis）和干涉检查（interference checking）。

---

## 落地碎片（无先后）

- **建模范式的选择法则**：**制造/CNC/注塑** → [cad.md](./cad.md)；**游戏/影视屏幕资产** → 本页多边形/雕刻。
- **Blender 优先策略**：对预算敏感的个人/小团队——以 Blender 为核心，需要时按项目短租 Maya/ZBrush 一个月。「Blender 打基础 + 商业工具冲刺收尾」是 2026 年性价比最高的路径。
- **拓扑规范前置约定**：在项目启动文档中明确——四边面优先（quad-dominant）、最大面数上限（per-asset poly budget）、UV 岛间距（padding）、命名约定（前缀/后缀规则）、轴向（Y-up 或 Z-up）、缩放单位（1 unit = 1m 或 1cm）。这些约定如果在第一版资产交付后再补，代价是返工全部资产。
- **从 generator/scanner 导入再精修**：生成草稿（[3d-model-generator.md](./3d-model-generator.md)）或扫描 mesh（[3d-scanner.md](./3d-scanner.md)）→ Blender/ZBrush 重拓扑与 UV——混合管线在道具/背景资产上已实用，主角仍常传统建模为主。
- **版本控制不是可选项**：`.blend`、`.ma`、`.ztl` 等源文件需要版本控制——推荐 Git LFS（大文件）或 Perforce（影视/游戏管线标准）。**持续集成（CI）** 可自动检查：面数预算、命名规范、UV 重叠、n-gon 检测。
- **移动端建模的适用边界**：Nomad 等适合有机雕刻速稿；工业设计速稿与 STL 见 [cad.md](./cad.md)（Shapr3D）。
- **格式选型早于建模开始**：确定最终交付格式（FBX for 引擎、USD for 场景、glTF for Web、STEP for 制造）→ 反推中间环节的工具选择和导出设置。先建模后发现格式不兼容的返工成本最高。

---

## 工具与产品类型（按检索词常混品类区分）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| **3D modelling software / DCC** | Blender、Maya、3ds Max、Cinema 4D | 多边形+雕刻+动画+渲染的完整创作套件 |
| **CAD / BIM software** | Fusion、SolidWorks、Revit、Rhino 等 | 主归属 `cad` |
| **Digital sculpting / 数字雕刻** | ZBrush、Nomad Sculpt、3D Coat | 高面数有机体雕刻 |
| **Procedural modelling / VFX** | Houdini、Blender Geometry Nodes | 节点式程序化生成，VFX 和大型环境的标准方案 |
| **Mobile 3D / 移动雕刻** | Nomad Sculpt（移动版） | 触控有机雕刻；移动 CAD 见 `cad` |
| **AI text-to-3D 平台** | Tripo、Meshy、Rodin 等 | 属 `3d-model-generator`；本页只写精修环节 |
| **BIM / 建筑信息建模** | Revit、ArchiCAD | 主归属 `cad` |
| **Real-time / 引擎内建模** | Unreal Engine、Unity（ProBuilder） | 引擎原生的基础建模和地形编辑——以快速搭建和迭代为主 |
| **Cloud/Web 3D** | Spline、Womp、Vectary | 浏览器内轻量建模，Web 导出，适合 UI 和营销 |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Blender 官方** | 开源全能 DCC 套件的最新版本（4.5 LTS，Vulkan 完整支持）与社区资源入口 | https://www.blender.org/ |
| **Autodesk Maya 产品页** | 影视/游戏动画行业标准的绑定与动画工具集（2026.1 含 MotionMaker） | https://www.autodesk.com/products/maya/overview |
| **ZBrush（Maxon）** | 数字雕刻行业标准 | https://www.maxon.net/en/zbrush |
| **Houdini（SideFX）** | 全节点程序化建模与 VFX | https://www.sidefx.com/ |
| **Generative Design Software Market Report 2026** | 生成式设计软件全球市场规模（2025 $2.66B→2030 $5.64B，CAGR 15.6%）与行业趋势 | https://www.researchandmarkets.com/reports/5980589/generative-design-software-market-report |
| **GenAI for 3D Assets Market Report 2025-2029** | AI 生成 3D 资产市场（2025 $2.47B→2029 $7.21B，CAGR 30.7%）的量化数据 | https://www.globenewswire.com/fr/news-release/2026/01/07/3214757/28124/en/ |
| **Forbes: How AI Is Transforming 3D Content Creation（2026-03）** | AI 重拓扑、程序化生成和混合工作流的产业现状分析 | https://www.forbes.com/councils/forbestechcouncil/2026/03/19/how-ai-is-transforming-3d-content-creation/ |
| **Envato: 3D Design Trends 2026** | 8 大 3D 设计趋势：AI 渗透、实时渲染、跨学科融合 | https://elements.envato.com/learn/3d-design-trends |
| **Anthropic Claude Blender 连接器（WebProNews 2026-04）** | Claude 通过 Blender Python API 自然语言操控场景的产业意义 | https://www.webpronews.com/anthropic-wires-claude-into-creatives-core-tools-nine-connectors-reshape-3d-design-and-music-workflows/ |
| **3D Modeling Type AIGC Market Forecast 2026-2032** | GII 市场报告的 3D 建模类 AIGC 细分数据（含生成、建模、扫描） | https://www.giiresearch.com/report/ires1949958-3d-modeling-type-aigc-market-by-component.html |
| **CG Channel** | 3D 建模、VFX 和动画行业的新闻与教程聚合 | https://www.cgchannel.com/ |
| **Khronos glTF 2.0 规范** | Web 和移动端 3D 交付的开放标准——PBR 材质、动画、骨骼原生支持 | https://registry.khronos.org/glTF/ |
| **Pixar USD 官方文档** | 影视和工业仿真的通用场景描述格式——层级组合、变体集、引用机制 | https://openusd.org/ |

### 对比与测评（第三方；观点非官方）

- **Blender 4.5 LTS 的功能完整度已与 Maya/3ds Max 在多数环节相当**——建模、雕刻、UV、渲染、合成均免费可用。主要差距在工业管线集成（USD 支持深度、Studio 级引用/变体管理）和高端绑骨（Maya 的复杂角色绑定系统仍更深）。
- **ZBrush 在数字雕刻领域没有对手**——其 Dynamesh 和 ZRemesher 技术积累了二十年优化，Blender Sculpt Mode 在面数上限（通常数千万 vs ZBrush 的数亿面）和笔刷响应上有可感知差距，但对非专业雕刻用途已完全够用。
- **Rhino / FreeCAD / Fusion** 等 CAD 横评见 [cad.md](./cad.md) §对比与测评。
- **Houdini 的程序化能力碾压一切**——其全节点工作流对大型环境和 VFX 是必需项。Blender Geometry Nodes 是免费替代，但缺乏 Houdini 的动力学模拟、FLIP 流体和 Pyro 烟火深度。
- **2026 年「生成/扫描→建模精修」混合工作流已是主流**——道具与背景资产可 generator/scanner 草稿 + 本 spoke 精修；主角与硬测量仍依赖传统建模为主。生成产品选型见 [3d-model-generator.md](./3d-model-generator.md)。

---

## 延伸阅读与参考材料

- **Blender Studio 开放项目**：https://studio.blender.org/films/ — 全程使用 Blender 制作的动画短片，技术文档和源文件开放参考。
- **80 Level**：https://80.lv/ — 游戏美术和 3D 建模社区，含大量艺术家工作流拆解和工具深度评测。
- **Polycount Wiki**：http://wiki.polycount.com/ — 游戏美术技术参考，含拓扑规范、纹理尺寸、引擎最佳实践。
- **ArtStation Learning**：https://www.artstation.com/learning — 商业教程库，覆盖 ZBrush、Maya、Blender 等主流工具的进阶教程。
- **Open3D Lab（浙江大学 + 风格化 3D 研究）**：关注中国学术界的 3D 生成与建模论文产出——如 Tencent Hunyuan3D-2.0（2025-03 开源，5 个模型系列，text/image→3D）。
- **GDC Vault**：https://www.gdcvault.com/ — 游戏开发者大会存档，含大量 AAA 工作室建模管线分享。

---


---

## 延伸阅读 · 站内知识块

- Hub：[3d.md](./3d.md)
- 生成：[3d-model-generator.md](./3d-model-generator.md)
- 工程 CAD：[cad.md](./cad.md)
- 扫描：[3d-scanner.md](./3d-scanner.md)
