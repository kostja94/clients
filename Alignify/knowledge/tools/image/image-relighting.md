# AI Image Relighting · 知识块（非线性笔记）

**材料范围**：公开网络检索（Vividon/Higgsfield/Luminar Neo/Photoroom 厂商官网、arXiv/CVPR/ICLR 学术预印本（TokenLight、PIXLRelight、GeoRelight、PI-Light、WildRelight）、Petapixel/WaveSpeedAI 行业报道）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-23**

**站内对照**：[alignify.co/tools/image-relighting](https://alignify.co/tools/image-relighting) · `content/tools/en/image-relighting.md` · [alignify.co/zh/tools/image-relighting](https://alignify.co/zh/tools/image-relighting) · `content/tools/zh/image-relighting.md` · slug **`image-relighting`**

**站内相邻**：[image.md](image.md) · [image-generator.md](image-generator.md) · [image-editor.md](image-editor.md) · [image-enhancer.md](image-enhancer.md)

**勿与…混买**：只改光照；天空替换叙事见 editor §Sky AI

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 `#image-relighting-tools`

## 与相邻 slug 分流

| 维度 | image-relighting（本页） | image-editor | image-enhancer | 3d |
|------|------------------------|-------------|---------------|-----|
| **买家问题** | "AI 能改变照片中的光照吗？" | "AI 能编辑图片内容吗？" | "AI 能提升图片质量吗？" | "AI 能生成 3D 模型吗？" |
| **核心操作** | 改变光源方向、强度、色温、阴影——不改变场景内容 | 添加/移除/替换图像中的对象 | 提升分辨率、去噪、去模糊——不改变光照 | 3D 建模和渲染（relighting 是其渲染管线的一个环节） |
| **关键差异** | 只改变"光的舞蹈"——场景几何和材质不变 | 改变"舞台上有什么" | 改善"画面的清晰度" | 创建"3D 舞台和演员"——relighting 是其子功能 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 图像重打光（AI Image Relighting）**：利用 AI 改变已有 2D 照片中的光照条件——调整光源方向、强度、色温、软硬度和阴影分布——而不改变场景中的几何结构、人物身份或物体材质。与简单的亮度/对比度滤镜的本质区别：AI 重打光理解图像的三维深度和表面材质——它能识别"这是一个球体，光从左边来——如果光从右边来，高光应该移动到这里、阴影应该投射到那边"。2026 年核心技术进步：从"2D 亮度滤镜"升级为"3D 深度感知+物理光照模型+扩散模型纹理合成"的三层技术栈。
- **3D 深度感知重打光（3D Depth-Aware Relighting）**：不是对 2D 像素统一应用亮度变化——而是先通过深度估计模型（monocular depth estimation）创建图像的深度图——然后模拟 3D 光源在场景中的光照交互——最后用扩散模型修复因光照变化而产生的纹理缺失。Luminar Neo Relight AI（前景/背景独立光照——带深度感）、Higgsfield Relight（3D 方向控制器——拖拽光源在 3D 空间中移动）和 Vividon（100+ 电影光照预设——基于深度感知）是 2026 年三类代表实现。
- **本征图像分解（Intrinsic Image Decomposition）**：将一张照片分解为底层物理组件——反照率（albedo——物体的"真实颜色"，不受光照影响）、法线图（normal——表面朝向）、深度图（depth——距离）、粗糙度（roughness——表面光滑程度）和环境光遮蔽（ambient occlusion——角落和缝隙的暗度）。这是 2026 年重打光研究的核心管线：分解→在新光照下重新合成——PIXLRelight（Oxford, 2026）、PI-Light（NTU/Tencent, ICLR 2026）和 GeoRelight（Meta, CVPR 2026）均采用此范式。核心挑战：从单张 2D 图像推断精确的物理属性是一个病态问题（ill-posed problem——无限多种 3D 场景可以产生同一张 2D 图像）。
- **物理启发式扩散重打光（Physics-Inspired Diffusion Relighting）**：将物理渲染方程（Lambertian 漫反射定律、Cook-Torrance 镜面反射模型、PBR 材质）嵌入扩散模型的训练和推断过程——确保生成的高光、阴影和反射遵循真实的物理规律。PI-Light（ICLR 2026——两阶段"逆向-正向"——漫反射着色损失+PBR 着色损失——灰球光照指定界面）和 TokenLight（CVPR 2026——属性 Token——连续控制强度、颜色、环境光、漫反射和 3D 光源位置——支持透明材质和内发光物体）是 2026 年物理启发的代表。与纯扩散模型（Magnific 风格——可能物理上不正确但"看起来好"）形成对照。
- **前馈式重打光（Feed-Forward Relighting）**：抛弃扩散模型的慢速迭代去噪——使用前馈式 Transformer 在单次推理中完成重打光——推理速度 <0.1 秒/图。PIXLRelight（Oxford, 2026——ViT+ConvNeXt→Transformer→身份初始化的逐像素仿射调制——"网络只学习光照残差"）和 SyncLight（2026 年 1 月——首个无需相机姿态的一致多视角重打光——一次推理）代表了前馈式的两条路线。核心优势：速度使实时应用成为可能（视频重打光、交互式光照设计）。
- **环境光遮蔽与高光控制（Ambient Occlusion & Specular Control）**：准确模拟自然光的两大特征——（1）环境光遮蔽（角落和凹陷处的柔暗——传统亮度滤镜无法模拟）、（2）镜面高光（光源在光滑表面上的反射——需要理解表面法线方向）。Vividon（100+ 电影光照预设——软硬光切换——菲涅尔效果）和 Higgsfield（软硬光开关——影响阴影锐度和高光范围）在 2026 年的消费级工具中提供了这些高级控制。
- **参考光照匹配（Reference Light Matching）**：从一张参考照片中提取光照特征（光源方向、色温、强度、软硬度、环境光颜色）——应用到目标照片上。Vividon（Match 功能——提取参考图的光照并应用——非破坏性 Photoshop 图层）和 IC-Light V2（文本描述光照——"温暖的黄金时刻阳光从右边来"——通过 WaveSpeedAI API 调用——每张约 $0.20）是文本驱动和参考驱动的两极代表。

---

## 专题对照

### 「滤镜式打光」vs「物理式重打光」：两种重打光方法

| 维度 | 滤镜式（2D Filter-Based） | 物理式（3D/Physics-Based） |
|------|-------------------------|--------------------------|
| **核心理念** | 在 2D 像素上应用颜色和亮度变换——模拟新光照的外观 | 理解 3D 场景几何和材质→在新的光照条件下重新计算光传输 |
| **阴影准确度** | 低——可能产生物理上不可能的光影 | 高——阴影位置、方向和软硬度遵循物理规律 |
| **高光准确度** | 低——表面高光位置不变（只是变亮） | 高——高光移动到新的光源方向上的正确位置 |
| **速度** | 快——秒级 | 慢——分钟级（学术 SOTA——GeoRelight ~35 秒/帧 A100） |
| **2026 消费级工具** | Dreamina by CapCut（免费——文本驱动）、部分 Clipdrop 模式 | Vividon（深度感知 3D 光照重新映射——Photoshop 图层）、Higgsfield（3D 方向板）、Luminar Neo（前景/背景独立深度） |
| **2026 研究前沿** | — | PI-Light、PIXLRelight、TokenLight、GeoRelight——物理规则嵌入扩散模型的学术竞赛 |

### 产品重打光 vs 人像重打光：两类应用的专业化分叉

| 维度 | 产品/电商重打光 | 人像重打光 |
|------|--------------|---------|
| **核心关注** | 材质（金属、玻璃、织物）和色彩准确度 | 皮肤质感、眼睛光影、面部轮廓的柔和度和方向感 |
| **关键工具** | Photoroom AI Relight（电商批量——$11/月）、Bria Fibo Relight（商业安全——$0.04/图——11+ 光照风格）、Clipdrop Relight（$7/月——最便宜的全功能方案） | Luminar Neo Relight AI（3D 深度前景/背景+暖度调整+去光晕）、Vividon（电影风格预设——Film Noir、Blade Runner——参考匹配） |
| **典型失败模式** | 金属表面高光的形状不匹配产品几何——产品看起来"假" | 眼睛光影死板——"死鱼眼"（catchlight 缺失）——皮肤过度平滑 |

---

## 问题域

- **"拍完才发现光不对"是摄影最普遍的遗憾——且传统上无法真正修复**：一张在正午硬光下拍摄的肖像无法在后期变为黄金时刻的柔光肖像——传统方法只能调整亮度和色温（改变"光是什么颜色"但无法改变"光从哪里来"）。AI 重打光的根本价值：将"光的决策"从拍摄时刻延迟到后期——这在胶片和早期数码摄影中是不可能的。
- **电商产品摄影的"一图多变"经济需求**：同一款产品需要展示在不同的光照场景（白底棚拍、暖色客厅、自然光、黄昏氛围）中——传统做法是多次重新拍摄（每次 $20-150）或昂贵的 3D 渲染（每张 $50-200）。AI 重打光使"拍一次→扩展到多种光照"成为可能——Photoroom AI Relight 和 Bria Fibo Relight（$0.04/图——11+ 风格）将多次拍摄的成本从 $200-600 降至约 $1（一次拍摄+AI 重打 ×10 风格）。
- **学术研究的"物理正确性"与消费级工具的"视觉愉悦性"之间的技术落差**：学术 SOTA（PI-Light, TokenLight, GeoRelight——CVPR/ICLR 2026——精确物理模型——分钟级处理和 A100 GPU）与消费级工具（Vividon, Luminar Neo——秒级处理——消费级设备）之间存在巨大的实用性鸿沟。2026 年消费级工具的质量提升主要来自"更好的深度估计+扩散模型纹理修复"——而非"精确的物理光传输模拟"——消费级重打光在大多数场景中"看起来对"但可能"物理上不完全正确"。
- **视频重打光的"最后前沿"**：2026 年静态图像重打光的质量已非常接近可用——但视频重打光（逐帧保持光照一致性——不出现闪烁和跳动）仍处于研究阶段。Relit-LiVE（SIGGRAPH 2026——联合环境-视频预测——支持动态光照和相机运动——支持对象插入和材质编辑）和 SyncLight（首个无需相机姿态的一致多视角重打光——一次推理）代表了 2026 年前沿——但距离消费级产品仍有 1-2 年的距离。
- **房地产与室内场景的「同空间多时段」展示需求**：购房者和租客期望看到同一空间在晨光、正午、黄昏、夜景下的效果——传统做法是物理布光多次拍摄，AI 重打光将这一成本降至单次拍摄即可生成多时段光照变体，与 [`virtual-staging.md`](../3d-spatial/virtual-staging.md) 和 [`interior-design.md`](../3d-spatial/interior-design.md) 形成工具链互补。

---

## 能力栈

- **3D 深度感知重打光**：先估计深度图→模拟 3D 光源→应用光照变化——Luminar Neo（前景/背景独立——近亮/远亮滑块）、Vividon（100+ 预设——每种预设包含不同的光源距离、方向和软硬度设置）、Higgsfield（实时 3D 方向板——拖拽光源在 3D 空间中实时移动）代表了三个不同方向——分层控制（Luminar）、预设艺术化（Vividon）、实时交互（Higgsfield）。2026 年的大多数"看起来可信"的消费级重打光都使用了不同程度的深度感知——纯粹的 2D 滤镜式重打光正在过时。
- **本征分解→重新合成管线**：学术研究的核心方法——分解反照率、法线、粗糙度、深度→在新光照下重新合成→扩散模型修复合成伪影。关键挑战：单张 2D 图像→精确 3D 属性的推断是不适定问题——不同方法的分解质量差异极大。PIXLRelight（前馈 Transformer——<0.1 秒/图——身份初始化的逐像素仿射调制——只学习光照残差）代表了从慢速扩散向实时前馈转型的技术方向。
- **文本驱动与参考驱动的光照指定**：用户如何告诉 AI "我要什么样的光照"？2026 年的三种界面范式：（1）文本描述（IC-Light V2——"温暖的黄金时刻阳光从右边来"——通过 API）、（2）参考图像（Vividon Match——提取参考图的光照并应用）、（3）3D 交互（Higgsfield——拖拽光源方向——软硬光切换——色温和亮度滑块）。第 3 种（3D 交互）对于产品/电商场景的专业用户是最精确的——因为他们需要特定的产品展示标准（如亚马逊要求的光照角度）。
- **多光照风格化**：预制的光照条件集合——用于快速在不同光照场景中切换——Bria Fibo Relight（11+ 光照风格——正午太阳、蓝调时刻、金色日出、月光、雾——商业安全训练数据——$0.04/图）和 Vividon（100+ 电影风格预设——Film Noir、Blade Runner、German Expressionist）是预设丰富度的两极——实用电商 vs 创意电影。
- **商业安全性与训练数据合规**：AI 重打光工具使用的训练数据是否获得授权——这对电商和广告的商业用途至关重要（你不能用可能侵权的模型处理商业产品图）。Bria Fibo Relight（完全授权的训练数据——商业安全——$0.04/图）是 2026 年商业合规重打光的标杆——专为规避 AI 训练数据版权诉讼而设计。
- **批处理与 API 集成**：对大量图像自动应用一致的重打光——电商平台的核心需求（数千 SKU 需要统一的光照风格）。Dreamina by CapCut（AI Agent 模式——单批最多 40 张——完全免费）和 WaveSpeedAI（IC-Light V2 和 Bria Fibo Relight 的 API——程序化重打光——面向开发者的集成）是批量重打光的免费和付费代表。
- **去光晕与光照伪影修复**：重打光（特别是大幅度改变光源方向时）会在高对比度边缘（头发边缘、物体轮廓）产生光晕伪影——看起来不自然的亮环或暗环。Luminar Neo 的去光晕工具（Dehalo Tool——专门处理重打光产生的边缘伪影）是 2026 年唯一专门应对这一问题的消费级功能。学术方法通过物理光照模型（PI-Light 的 PBR 着色损失）来根本性地减少光晕——但代价是速度和复杂度。

---

## 形态谱系

- **桌面专业插件（Desktop Professional Plugin）**：以 Vividon（2026 年 4 月新发布——Photoshop 插件——100+ 光照预设——参考匹配——非破坏性图层——$10-55/月）和 Luminar Neo Relight AI（3D 深度感知——前景/背景独立——$9.95/月或 $99 一次性）为代表——面向需要高控制度和专业工作流集成的摄影师。核心价值：不离开 Photoshop/Lightroom——照片编辑选光照是自然的工作流延伸而非工具跳转。
- **云端 API 重打光服务（Cloud API Relighting Service）**：以 IC-Light V2（文本驱动——WaveSpeedAI API——~$0.20/图——5 方向+文本控制）和 Bria Fibo Relight（商业安全——11+ 风格——$0.04/图——Scene-Aware 场景分析）为代表——面向开发者和企业——将重打光集成到自有应用和自动化工作流中。核心价值：可扩展性和程序化控制——不受 GUI 速度限制。
- **Web 交互式重打光（Web Interactive Relighting）**：以 Higgsfield Relight（3D 方向板+软硬光+色温——实时交互——也支持视频）和 Clipdrop Relight（Stability AI——移动虚拟光源——$7/月——配背景去除和超分）为代表——无需安装——浏览器即用。核心价值：最低的尝试成本——"我想看看重打光能否解决我的问题"的最快入口。
- **电商专用重打光（E-Commerce Specialized Relighting）**：以 Photoroom AI Relight（批量 250 张——分析并自动改善产品光照——光方向/强度/色温调整——$11/月——与虚拟模特集成）为代表——专为产品图和目录设计。核心价值：不是"一张图的光照艺术"而是"一千张图的光照一致性"——这是电商特有的需求维度。
- **免费/开源重打光（Free/Open-Source Relighting）**：以 Dreamina by CapCut（完全免费——文本驱动——Seedream 5.0——AI Agent 批处理 40 张——区域画笔精细控制）和 Qwen-Edit-Relight LoRA（阿里通义千问——双 LoRA 架构——12 种光照场景——92% 光照保真度——ComfyUI/SD WebUI——8GB VRAM——免费开源）为代表。核心价值：零成本——但需要技术能力（开源）或接受平台锁定（免费但非开源）。

---

## 风险 · 合规 · 产品真实性（外部框架可对照）

- **产品重打光可能构成虚假广告——如果光照改变使产品看起来与实物不同**：如果 AI 重打光使服装的颜色在"黄金时刻"光下显得更饱和和吸引人——而实际产品在室内光下完全不同——这可能构成虚假广告。2026 年 FTC（美国联邦贸易委员会）和欧盟消费者保护法的立场：如果 AI 修改导致产品在功能和外观的实质性方面与实物有重大差异——需要标注"经过 AI 光照修改"或"光环境经过数字修改"。
- **电商平台的内容政策——Amazon/Zalando/Shopify 对 AI 重打光的态度**：2026 年主要电商平台允许 AI 背景替换和 AI 增强——但对 AI 修改产品本身（包括可能改变颜色感知的重打光）保持谨慎。建议：验证 AI 重打光后的产品颜色是否在 sRGB 色彩空间中与实物在标准 D65 光照下的颜色一致——不一致的应标注或避免用于主产品图。
- **人像重打光的"不自然"风险**：当 AI 大幅度改变人物面部的光影方向时——可能导致"Uncanny Valley"效果——观众潜意识中察觉到光影与 3D 面部结构之间的不匹配。特别是眼睛的反光点（catchlight——眼角膜上的微小高光——是人类视觉系统判断光照方向的最敏感线索）——如果 AI 重打光改变了整体光照但没有相应地移动眼睛高光——面部会看起来很"假"。2026 年最可靠的人像重打光工具（Luminar Neo、Vividon）在微妙光照调整上表现最好——大幅度改变光照方向仍然存在不可忽视的风险。

---

## 落地碎片

- **对人像重打光——"少即是多"——微调优于彻底改变**：AI 重打光最适合的场景不是"中午变成午夜"——而是"正午硬光→稍微柔和的午后光"或"给暗部稍微补一点光"。微调（+0.5 到 +1 档前景光、暖度 ±10%）产生自然的结果——大改变（光源方向翻转 180°）产生"Uncanny"的不自然感。在 2026 年的技术水平下——适度是重打光质量的最佳保障。
- **产品重打光——Bria Fibo Relight 是性价比和商业安全的最优选择**：$0.04/图——11+ 光照风格——完全授权的训练数据——对电商和广告的商业用途完全安全。IC-Light V2 的质量更高（文本驱动更灵活——$0.20/图）但对于大批量（10,000+ SKU——$2,000 vs $400）的成本差值得考虑。Photoroom Relight（$11/月——批量 250 张）适合电商卖家——提供了一站式的背景去除+重打光+虚拟模特工作流。
- **Photoshop 用户——Vividon 的非破坏性图层是工作流整合的突破**：与一键生成 JPEG 的工具不同——Vividon 的重打光结果存储在单独的 Photoshop 图层中——你可以随时调整不透明度、混合模式、添加蒙版。这保留了 Photoshop 用户期望的完全后期控制——同时获得了 AI 的重打光能力。$10-55/月（含 30 免费试用点数）——对 Photoshop 用户来说添加成本不高。
- **视频重打光尚未就绪——2026 年不要基于这一假设规划工作流**：虽然 Higgsfield 声称支持视频重打光——且学术研究（Relit-LiVE, SyncLight）在快速进步——但 2026 年视频重打光的质量、一致性和可用性尚未达到"可交付"水平。对视频项目——仍然通过物理灯光（实际的光源和柔光箱）或 3D 渲染来控制光照——AI 视频重打光在 2026 年仍处于 R&D 而非生产阶段。

---

## 工具与产品类型

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| **Desktop Plugin**（Vividon, Luminar Neo Relight AI） | Photoshop/Lightroom 集成，3D 深度感知，非破坏性图层 | 专业摄影师——"不离开我的编辑器" |
| **Cloud API Service**（IC-Light V2, Bria Fibo Relight） | 文本/参考光照驱动，程序化集成，商业安全训练数据 | $0.04-0.20/图——开发者和企业——规模化 |
| **Web Interactive Tool**（Higgsfield Relight, Clipdrop Relight） | 浏览器 3D 光照交互，零安装，也支持视频 | $7/月起——"试试重打光能不能解决我的问题"的最快入口 |
| **E-Commerce Specialist**（Photoroom AI Relight） | 批量产品图重打光+虚拟模特+背景去除一站式 | $11/月——电商专用——光照一致性而非光照艺术 |
| **Free/OSS Relighting**（Dreamina by CapCut, Qwen-Edit-Relight LoRA） | 免费/开源，文本驱动或 ComfyUI 节点，AI Agent 批处理 | 零成本——但平台锁定或需要技术能力 |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| Vividon | Photoshop 重打光插件——100+ 电影预设+参考匹配+非破坏性图层，$10-55/月 | https://vividon.ai |
| Luminar Neo Relight AI | 3D 深度感知——前景/背景独立光照+暖度+去光晕，$9.95/月或 $99 一次性 | https://skylum.com/luminar |
| IC-Light V2 | 文本驱动重打光 API——ControlNet 作者 Lvmin Zhang 出品，~$0.20/图 | https://wavespeed.ai |
| Bria Fibo Relight | 商业安全重打光——授权训练数据+11+ 风格，~$0.04/图 | https://wavespeed.ai |
| Higgsfield Relight | 3D 方向板实时交互重打光——也支持视频，点数制 | https://higgsfield.ai |
| Photoroom AI Relight | 电商批量重打光——250 张/批+虚拟模特集成，~$11/月 | https://photoroom.com |
| Clipdrop Relight | Stability AI——移动虚拟光源——$7/月——配背景去除和超分 | https://clipdrop.co |
| Dreamina by CapCut | 免费 AI 重打光——文本驱动+AI Agent 批处理 40 张+区域画笔 | https://dreamina.capcut.com |

### 对比与测评（第三方；观点非官方）

- **Petapixel 2026 年 4 月 Vividon 评测**：Vividon 的参考匹配和非破坏性 Photoshop 图层是其最大差异化——允许摄影师在保持完全后期控制的同时获得 AI 重打光能力。100+ 电影预设（Film Noir、Blade Runner、German Expressionist）覆盖了最常需要的创意光照风格。
- **Petapixel 2026 年 1 月 AI 重打光 App 综述**：AI 重打光在 2026 年从"有趣的 AI 把戏"升级为"摄影师日常工具"——关键转折点是 3D 深度感知技术的成熟——使光照变化看起来可信而非"生硬的滤镜"。
- **WaveSpeedAI 2026 IC-Light V2 和 Bria Fibo Relight 公告**：IC-Light V2（ControlNet 作者开发——16 通道 VAE——文本+5 方向控制）和 Bria Fibo Relight（完全授权训练数据——11+ 光照风格——$0.04/图）代表了云端 API 重打光的两条路径——创意灵活 vs 商业安全。
- **Filmora 2026 Luminar Neo Relight AI 评测**：Luminar Neo 的 3D 深度感知前景/背景独立控制是其区别于"一键 AI 重打光 App"的核心——允许摄影师精确控制光照的纵深感和层次感——而不仅仅是"更亮或更暗"。

---

## 延伸阅读与参考材料

- arXiv — TokenLight（CVPR 2026）: Precise Lighting Control in Images using Attribute Tokens — `arxiv.org/abs/2604.15310`
- arXiv — PIXLRelight（Oxford, 2026）: Controllable Relighting via Intrinsic Conditioning — `arxiv.org/abs/2605.18735`
- arXiv — PI-Light（NTU/Tencent, ICLR 2026）: Physics-Inspired Diffusion for Full-Image Relighting — `arxiv.org/abs/2601.22135`
- arXiv — Relit-LiVE（SIGGRAPH 2026）: Relight Video by Jointly Learning Environment Video — `arxiv.org/abs/2605.06658`
- arXiv — WildRelight（DTU, 2026）: A Real-World Benchmark for Single-Image Relighting — `arxiv.org/abs/2605.11696`
- Petapixel — "Vividon's New Photoshop Plugin Uses AI to Change Photo Lighting"（2026 年 4 月）
- Petapixel — "This AI App Lets You Relight Your Photos"（2026 年 1 月）
- WaveSpeedAI — IC-Light V2 和 Bria Fibo Relight 产品公告（2026）
- Filmora — "Luminar Neo Relight AI Review 2026: Pro Lighting Alternative"

---


---
## 延伸阅读 · 站内知识块
- 品类 Hub：[image.md](image.md)
- 生成层 SSOT：[image-generator.md](image-generator.md)（§行业注记 / §外链索引 / §共享事实速查）
