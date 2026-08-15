# AI CAD Tools · 知识块（非线性笔记）

**材料范围**：公开网络检索（Autodesk / Dassault / Trimble 产品页、Zoo.dev / Adam 文档、KCL 说明、CAD 行业媒体与 Forbes 2026 摘要）；**未**引用 Alignify 站内 JSON 正文为论据。网摘整理日期 **2026-06-24**。

**站内对照**：[alignify.co/blog/cad](https://alignify.co/blog/cad) · [alignify.co/zh/blog/cad](https://alignify.co/zh/blog/cad) · 正文 JSON 已同步至部署仓 `alignify-by-kostja/content/blog/{en|zh}/cad.json` · slug **`cad`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#cad-tools`

**站内相邻**：[3d.md](./3d.md) · [3d-modelling.md](./3d-modelling.md) · [3d-model-generator.md](./3d-model-generator.md)

**内容边界**：本 slug 主责 **制造与工程向 CAD**——参数化实体、NURBS、B-Rep、BIM 数据模型、STEP/IGES 交换，以及 **AI 加持层**（text-to-CAD、CAD Copilot、geometry API）。**影视/游戏 DCC 精修**（拓扑/UV/绑骨）见 [3d-modelling.md](./3d-modelling.md)；**展示用 mesh 生成**（Tripo/Meshy）见 [3d-model-generator.md](./3d-model-generator.md)。完整分工见 [3d.md](./3d.md) §内容分工。

**勿与…混买**：本页是 **可加工 / 可出图 / 可算量的工程几何**——不是游戏道具 mesh、不是 listing 虚拟软装、不是 UI 原型（`ui-design`）。

以下条目可任意顺序阅读；**不是**文章体例。

---

## Buyer 子决策树

| 你的问题 | 去哪个 slug | 知识块 |
|----------|-------------|--------|
| 机械零件 / CNC / 注塑，要 STEP/B-Rep？ | `cad` | 本页 |
| 用 **自然语言** 直接生成可编辑 CAD？ | `cad` | 本页 §AI text-to-CAD |
| 影视/游戏 mesh 要拓扑/UV/绑骨精修？ | `3d-modelling` | [3d-modelling.md](./3d-modelling.md) |
| 文/图凭空生成 **展示 mesh**（非制造）？ | `3d-model-generator` | [3d-model-generator.md](./3d-model-generator.md) |
| 建筑 **施工级 BIM** 算量与协同？ | `cad` | 本页 §BIM |
| 业主 **效果图级** 家装 redesign（非施工图）？ | `interior-design` | [interior-design.md](./interior-design.md) |

---

## 内容分工（编辑前必读 · CAD 轴）

| 内容类型 | 主归属 slug | 其它块 |
|----------|-------------|--------|
| Fusion / SolidWorks / AutoCAD / Rhino / FreeCAD **URL 表** | **`cad`（本页）** | modelling ≤2 代表 |
| Text-to-CAD / Zoo / Adam / KCL API | **`cad`** | generator 1 句 |
| CAD Copilot（Fusion AI 等） | **`cad`** | modelling 不写长文 |
| BIM（Revit、ArchiCAD）工程数据流 | **`cad`** | interior-design 不写算量 |
| Shapr3D / 移动 CAD | **`cad`** | modelling 移动 **雕刻** 写 Nomad |
| STEP/IGES/B-Rep 格式 SSOT | **`cad`** | hub 不重复 |
| Blender/Maya/ZBrush 雕刻动画 | **`3d-modelling`** | cad 不写绑骨长段 |
| Claude → **Fusion** 连接器 | **`cad`** 1 句 | Blender 连接器在 modelling |

---

## 词汇锚点

- **CAD / Computer-Aided Design（本知识块主标签）**：检索常写作 **CAD software**、**3D CAD**、**parametric CAD**、**mechanical CAD**；偶与 **AutoCAD**、**Fusion 360** 等品牌词混搜。核心产出为 **尺寸驱动、可制造或可出施工图** 的几何与数据——非单纯渲染图。
- **CAD vs DCC**：CAD 面向 **制造 / 工程 / BIM 数据**（STEP、IGES、DWG、RVT）；DCC 面向 **屏幕呈现**（FBX、glTF、雕刻、动画）——详见 §专题对照与 [3d-modelling.md](./3d-modelling.md)。
- **B-Rep / 边界表示**：精确实体边界——机械加工与模具常用；与三角 **mesh** 不同。
- **STEP / IGES**：制造业 **交换格式** SSOT；AI CAD 黄金交付常为 STEP。
- **Parametric / 参数化建模**：尺寸与约束驱动特征树——改一处参数全局更新；SolidWorks、Fusion、FreeCAD 范式。
- **NURBS CAD**：Rhino、Alias 等 **数学曲面**——工业设计与自由曲面建筑。
- **BIM / 建筑信息模型**：Revit、ArchiCAD——模型携带 **构件数据** 流向施工与运维；≠ 家装效果图（见 `interior-design`）。
- **Text-to-CAD / AI CAD generator**：NL、草图 → B-Rep/STEP——Zoo.dev、Adam；品类词 **text to cad** 月搜低于 **autocad** 但意图更纯。
- **Geometry-as-code（KCL）**：Zoo 生态——模型即代码，适合 API 与 CI。
- **Generative design（生成式设计）**：仿真驱动拓扑优化——Fusion、nTopology；非 NL 主路径，属 CAD 子类。

---

## 专题对照 / 扩展定义

| 维度 | **cad（本文件）** | **3d-modelling** |
|------|-------------------|------------------|
| **核心任务** | 工程几何、制造、出图、BIM 数据 | DCC 创作、雕刻、动画、影视精修 |
| **典型工具** | Fusion、SolidWorks、AutoCAD、Rhino、Revit | Blender、Maya、ZBrush、Houdini |
| **输出格式** | STEP、IGES、DWG、RVT | FBX、glTF、USD（场景） |
| **AI 角色** | text-to-CAD、Copilot 改特征 | 重拓扑、UV、Auto-Rig、操控 Blender |
| **检索词** | CAD software, Fusion 360, text to cad | 3D modelling, Blender, ZBrush |

| 维度 | **cad（本文件）** | **3d-model-generator** |
|------|-------------------|------------------------|
| **产出** | 可制造实体 / 工程模型 | 展示 mesh / splat |
| **验收** | 壁厚、公差、特征可编辑 | silhouette、贴图、rig |
| **检索词** | AI CAD, prompt to STEP | text to 3D, image to 3D |

| 维度 | **cad（本文件）** | **interior-design** |
|------|-------------------|----------------------|
| **产出** | 施工图/BIM/加工件 | 效果图、风格方案、mood board |
| **买家** | 机械/建筑工程师 | 业主、室内设计师 |
| **SketchUp** | 建筑草模 CAD 向 | 家装可视化向（与 Planner 5D 等） |

| 维度 | **cad（本文件）** | **vibe-coding** |
|------|-------------------|-----------------|
| **产出** | 几何零件 | 应用源代码 |

---

## 问题域（为何会出现这类产品）

- **制造数字化**：从概念到 CNC/注塑/钣金的全链路依赖 CAD——AI 压缩 **首轮建模** 而非取代 QC。
- **订阅成本与开源替代**：AutoCAD/Fusion 订阅 vs FreeCAD 免费——中小团队选型压力大。
- **硬件初创缺 CAD 人力**：text-to-CAD 与 geometry API 服务 **定制件下单**。
- **BIM  mandated**：大型建筑项目要求 **数据模型** 交付——Revit 等仍为基建。
- **AI Copilot 嵌入传统 CAD**：Fusion AI 等降低 **特征编辑** 门槛——与 standalone text-to-CAD 并存。
- **移动与外勤**：Shapr3D 等将 CAD 带到客户现场——速稿到 STL 闭环。

---

## 能力栈（概念拆分，非厂商功能表）

- **建模范式**：参数化实体、NURBS、直接建模、BIM 构件、程序化（Grasshopper）。
- **AI 输入**：NL 对话、草图、三视图、Copilot 自然语言改特征。
- **可编辑性**：特征树、参数滑块（Adam）、KCL 源码 vs 死 mesh STL。
- **导出与互操作**：STEP、IGES、STL、DWG、IFC（BIM）。
- **装配与工程**：多体装配、干涉检查、公差标注——传统 CAD 强项；AI 生成多体仍弱。
- **仿真与生成式设计**：FEA、流体、拓扑优化——Fusion、SolidWorks Simulation 生态。
- **协作与 PDM**：云 CAD（Fusion）、PLM 集成——企业采购维度。
- **API / 嵌入**：Zoo geometry API、部分厂商脚本 API。

---

## 形态谱系（与具体品牌解耦）

- **机械参数化 CAD**：SolidWorks、Fusion 360、Onshape、FreeCAD——机械与产品设计主流。
- **2D+3D 通用 CAD**：AutoCAD、BricsCAD——工程制图传统强项 + 部分 3D。
- **NURBS / 工业设计**：Rhinoceros + Grasshopper——曲面与参数化建筑。
- **BIM 平台**：Revit、ArchiCAD、Vectorworks——建筑信息模型与施工协同。
- **建筑快速草模**：SketchUp——推拉式直觉建模；家装 **效果图** 与 interior-design 工具重叠。
- **移动 CAD**：Shapr3D（iPad）——外勤速稿与 STL。
- **AI text-to-CAD**：Zoo.dev、Adam——NL/KCL → STEP。
- **CAD 内嵌 Copilot**：Fusion AI、SolidWorks 助手——操控既有特征树。
- **开源参数化**：FreeCAD——模块化工作台，成本敏感团队。

---

## 风险 · 合规 · 工程治理（轴特有；簇级见 Hub）

簇级版权见 [3d.md](./3d.md) §风险。本 slug 特有：

- **制造责任**：AI 或自动生成的 STEP **可能存在非流形、不可加工倒角、螺纹错误**——上机前 DFM 与计量复核；模具前 **禁止** 跳过人工审查。
- **BIM 与施工安全**：AI 辅助 ≠ 结构计算——拆改承重须注册工程师签字。
- **vendor lock-in**：DWG/专有格式 vs STEP/IFC 开放交换——项目启动定格式 SSOT。
- **许可与训练数据**：上传零件草图是否进训练集——B2B API 合同须明确。
- **「导出 STL」≠ CAD 就绪**：mesh 表面光滑但无特征树时，修改成本仍高。

---

## 落地碎片（无先后）

- **制造件** → 本页或传统 CAD；**游戏/电商 mesh** → [3d-model-generator.md](./3d-model-generator.md)。
- **精修拓扑/UV** → [3d-modelling.md](./3d-modelling.md)（即使起点是 CAD 导出的 mesh）。
- 混合管线：**Adam/Zoo 初稿 STEP → Fusion 精修 → 工程图 → CAM**。
- 选型 text-to-CAD：用支架/法兰/外壳 3 prompt 测 **特征树可编辑性**。
- 广义词 **autocad** 流量大但品牌指向 Autodesk——品类文用 **CAD software** + 品牌横评。

---

## 工具与产品类型

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Mechanical CAD** | SolidWorks、Fusion 360、Onshape | 参数化实体 |
| **2D/3D CAD** | AutoCAD、BricsCAD | 工程图传统 |
| **NURBS CAD** | Rhino、Alias | 曲面工业/建筑 |
| **BIM** | Revit、ArchiCAD | 施工数据流 |
| **Open-source CAD** | FreeCAD | 免费参数化 |
| **Mobile CAD** | Shapr3D | iPad 外勤 |
| **Text-to-CAD / AI CAD** | Zoo.dev、Adam | NL→STEP |
| **Sketch-to-CAD** | 部分 Zoo/Adam | 成熟度需实测 |
| **Text-to-3D mesh** | Tripo、Meshy | → `3d-model-generator` |
| **DCC** | Blender、Maya | → `3d-modelling` |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Autodesk Fusion** | 云 CAD + 制造 + Fusion AI Copilot | https://www.autodesk.com/products/fusion/overview |
| **SolidWorks** | 机械参数化 CAD 标杆 | https://www.solidworks.com |
| **AutoCAD** | 2D/3D 通用 CAD（Autodesk） | https://www.autodesk.com/products/autocad/overview |
| **Rhinoceros 3D** | NURBS + Grasshopper 生态 | https://www.rhino3d.com/ |
| **FreeCAD** | 开源参数化 CAD | https://www.freecad.org |
| **Revit** | BIM 建筑信息建模 | https://www.autodesk.com/products/revit/overview |
| **Shapr3D** | iPad 专业 CAD | https://www.shapr3d.com/ |
| **SketchUp** | 建筑快速草模 | https://www.sketchup.com |
| **Zoo.dev** | KCL + text-to-CAD API | https://zoo.dev |
| **Adam（AdamCAD）** | 对话式 CAD + 参数滑块 | https://adam.new |
| **KittyCAD / KCL** | 几何语言与引擎 | https://github.com/KittyCAD |

### 对比与测评（第三方；观点非官方）

- **Fusion vs SolidWorks**：Fusion 云协作与制造一体化强；SolidWorks 传统机械企业惯性大——AI 功能迭代速度需跟官网。
- **Rhino vs FreeCAD**：Rhino 曲面与 Grasshopper 生态领先；FreeCAD 覆盖基础机械免费需求。
- **Zoo/Adam vs 传统 CAD**：简单支架类件可 NL 起步；**装配、A 级曲面、全工程图** 仍回流 Fusion/SolidWorks。
- **text-to-CAD vs text-to-3D**：制造件勿用 mesh 生成器；展示件勿强行走 STEP 管线。

*本小节为行业观点综合，非 Alignify 实测。*

---

## 延伸阅读与参考材料

- DCC 精修：[3d-modelling.md](./3d-modelling.md)
- Mesh 生成：[3d-model-generator.md](./3d-model-generator.md)
- 家装效果图（非施工图）：[interior-design.md](./interior-design.md)
- Forbes 2026：制造 CAD vs 内容 mesh 管线区分

---


---

## 延伸阅读 · 站内知识块

- Hub：[3d.md](./3d.md)
- DCC 精修：[3d-modelling.md](./3d-modelling.md)
- 展示 mesh：[3d-model-generator.md](./3d-model-generator.md)
