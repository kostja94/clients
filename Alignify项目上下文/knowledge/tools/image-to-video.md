# AI Image-to-Video · 知识块（非线性笔记）

**材料范围**：公开网络检索（Runway/Seedance/Luma/Pika/Kling 厂商官网、WaveSpeed API 指南、UlazAI/APIDog 工具对比评测）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-23**

**站内相邻**：[image.md](./image.md) · [image-generator.md](./image-generator.md) · [video.md](./video.md) · [video-generator.md](./video-generator.md) · [text-to-video.md](./text-to-video.md) · [video-to-video.md](./video-to-video.md)

**勿与…混买**：本页主轴 **输入=静态图**；从零 T2V 见 text-to-video；全片风格化见 video-to-video。

**站内对照**：[alignify.co/tools/image-to-video](https://alignify.co/tools/image-to-video) · `content/tools/en/image-to-video.json` · [alignify.co/zh/tools/image-to-video](https://alignify.co/zh/tools/image-to-video) · `content/tools/zh/image-to-video.json` · slug **`image-to-video`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 `#image-to-video-tools`

## 与相邻 slug 分流

| 维度 | **image-to-video（本页）** | **video-generator** | **text-to-video** | **filmmaking** | **video** |
|------|---------------------------|---------------------|-------------------|----------------|-----------|
| **买家问题** | 静态图如何动起来？ | 哪种模型从零生成？ | 文本如何变视频？ | 电影全管线？ | 选哪类工具？ |
| **输入** | 已有图像 | 文本/图/弱条件 | 文本/文档 | 剧本→成片 | — |
| **关键差异** | Motion Brush、废片率、品牌保真 | 跨模态模型 SSOT | prompt/讲解视频 | pre-vis 中 I2V 角色 | Hub 分流 |

| 维度 | image-to-video（本页） | filmmaking | 3d |
|------|----------------------|-----------|-----|
| **起点** | 已有静态图像→添加运动 | 创意意图→全管线制片 | 3D 建模和渲染 |
| **关键差异** | I2V 专页 | I2V 仅为 pre-vis 子步 | 3D 空间运动 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 图像到视频（AI Image-to-Video / I2V）**：从一张或多张静态图像生成动态视频的 AI 技术——输入为照片、插画、概念艺术或产品图——输出为包含运动、视差、相机推拉或角色动画的短视频片段。与文本到视频（T2V——从文字提示生成全新视频）的核心区别：I2V 的起点是一张"你已有的图像"——AI 的角色是"让它动起来"而非"创造全新的视觉世界"。2026 年 I2V 市场的五个关键竞争维度：运动写实度、品牌/细节保真度（图像中的文字和标志是否在动画中保持不变）、最大时长、分辨率和每可用秒成本（cost per usable second——考虑重试后的废片率）。
- **运动画笔（Motion Brush）**：在图像的特定区域用画笔指定运动方向和强度的交互方式——"这里的头发向右边飘、这里的衣服随风摆、这里的水流向左边"。Runway Gen-4.5 的 Motion Brush 是最著名的实现——允许像素级的运动控制。区别于"整图自动动画"的不可控性——运动画笔给予导演精细的创意控制——使 I2V 从"AI 的一次性猜测"变成"导演的反复迭代工具"。
- **关键帧动画（Keyframe Animation / Pikaframes）**：提供第一帧和最后一帧——AI 在两帧之间自动生成平滑的过渡动画。Pika 2.5 的 Pikaframes 功能是这一模式的代表——适用于制作转场效果、定格动画和产品展示。与单图 I2V 的区别：两帧动画给予 AI 更多的控制信息——减少了"AI 猜错运动方向"的概率。
- **角色动画（Character Animation / Act-Two）**：将静态角色图像（插画角色、数字人、历史人物肖像）转化为具有表情、口型和身体动作的动态表演——输入可以仅是静态角色图——也可以通过摄像头捕捉真人面部/身体动作并映射到角色上。Runway Act-Two（摄像头动作捕捉→AI 角色映射）和 DreamActor（字节跳动——静态人像→动态表演——专门的人体/头像动画）是 2026 年角色动画的两条路线——实时动作捕捉 vs 纯 AI 推理。
- **空间一致性与 3D 感知动画（Spatial Coherence & 3D-Aware Animation）**：AI 在动画化静态图像时保持空间深度和 3D 几何一致性——不仅是"像素在移动"而是"相机在 3D 空间中移动"。Luma Dream Machine 1.6 以 3D 感知动画著称——画面中的物体按正确的视差关系移动（近景移动快、远景移动慢）——产生自然的电影感深度而非"生硬的 2D 滑动效果"。Seedance 2.0 在保持原图品牌标志和文字细节的同时进行 3D 相机运动方面领先。
- **风格保留与细节保真度（Style Preservation & Detail Fidelity）**：AI 在动画化过程中保持原图的风格（油画、水彩、照片写实、动漫）和关键细节（品牌标志、文字、产品纹理）不变。这是 I2V 中最困难的挑战——因为在"添加运动"和"保持原图"之间存在天然的技术张力——模型越"创造性地"添加运动，就越可能"创造性地"改变原图的细节。Seedance 2.0 在品牌标志和细节保真度上领先——专为电商产品图动画化优化（标志不能变）。

---

## 专题对照

### 单图动画 vs 两帧过渡 vs 多图序列：三种 I2V 输入模式

| 维度 | 单图动画（Single Image） | 两帧过渡（Start+End Frame） | 多图序列（Image Sequence） |
|------|------------------------|---------------------------|--------------------------|
| **代表工具** | Runway Gen-4.5（图生视频模式）、Luma Dream Machine、Seedance 2.0 | Pika 2.5 Pikaframes | Runway Gen-4.5（多图输入模式）、专业 VFX 管线 |
| **控制精度** | 低——AI 猜测运动方向 | 中——用户指定起点和终点 | 高——AI 填充帧间间隙而非猜测整个运动 |
| **适用场景** | 快速"让这张概念图动起来"——社交媒体和预演 | 转场效果、产品展示的"前后对比"动画 | 已有粗略动画需要平滑帧率——VFX 和动画管线 |
| **失败风险** | 高——AI 可能猜错运动方向或产生不自然的变形 | 中——两端锁定→中间过渡通常平滑但可能"太线性" | 低——AI 的任务是插值而非推理 |

### I2V 写实派 vs I2V 风格派：两种动画哲学

| 维度 | 写实派（Photorealistic I2V） | 风格派（Stylized I2V） |
|------|---------------------------|---------------------|
| **代表工具** | Seedance 2.0、Luma Dream Machine | Pika 2.5（Pikaffects 特效——粉碎、融化、爆炸）、Runway 风格迁移 |
| **核心价值** | "让照片动起来——看起来像真实的摄影机运动" | "让插画、概念艺术和 AI 艺术动起来——创造奇幻的视觉效果" |
| **用户** | 电商（产品展示）、摄影师、地产（虚拟参观） | 概念艺术家、社交媒体创作者、动画师 |
| **质量评判标准** | 运动的物理真实度——是否有不自然的变形和扭曲 | 运动的创意度——是否有趣、惊艳、与风格一致 |

---

## 问题域

- **"静态图像的死亡"——所有数字视觉内容正在被期望为动态的**：从 Instagram Stories 到 TikTok 到电商产品页——"静态图像"正在快速失去注意力竞争优势。I2V 填补的核心缺口：数十亿存量静态图像（产品图、品牌资产、历史照片、概念艺术）——在拍摄时从未预期需要变为视频——现在有了变为动态内容的批量转换技术路径。这不是替代视频拍摄——而是让所有存量图像资产获得第二次生命。
- **产品图和品牌资产的"视频化"需求**：电商平台（Amazon、Shopify）和社交媒体广告（Meta、TikTok）正在系统性地偏好视频内容——但品牌拥有数十万静态产品图——重新拍摄视频的成本不可承受。I2V 让品牌以 $0.10-0.50/图的成本将静态产品图转化为 5-10 秒的产品展示动画——用于广告、产品页面和社交媒体。Seedance 2.0 在品牌细节保真度上领先——这是电商 I2V 的核心需求（品牌标志和产品文字不能在动画中变形）。
- **概念艺术和预演——"在拍摄之前先看到它动起来"**：电影和广告的前期制作阶段——导演和 DP 需要可视化和沟通一个场景应该如何运动——传统上通过故事板（静态）或昂贵的 3D 预演（耗时且昂贵）。I2V 提供了第三条路径——将概念艺术或故事板帧直接转化为动态预演视频——成本从数千美元降至几十美分——速度从数周降至数分钟。
- **"废片率"是 I2V 隐藏的真实成本——而非生成成本**：大多数 I2V 工具定价按每次生成计费（$0.10-0.50/Gen）——但实际可用率（在 5-10 次生成中至少有一次是"可以直接使用的"）通常低于 30-50%。这意味着每可用秒的实际成本是标价的 2-4 倍。2026 年 I2V 工具选择的隐蔽关键因素不是"每代成本"而是"每可用秒成本"——这取决于你对"可用"的标准有多高。
- **短内容生态的「动图即默认」期望**：从 LinkedIn 轮播到 WhatsApp Status 到公众号封面——几乎所有数字触点都在要求「至少让图片动一下」。I2V 使非视频团队（写作者、设计师、社交媒体运营）也能满足这一期望而不依赖专业视频制作——与 [`animation-generator.md`](./animation-generator.md)（全动画视频）和 [`video-generator.md`](./video-generator.md)（原生视频生成）形成从轻到重的工具链。

---

## 能力栈

- **单图动态化（Single Image Animation）**：核心 I2V 能力——输入单张静态图像→AI 推断深度图→识别可运动区域（头发、水、衣服、树叶）→生成自然的循环运动或一次性相机推拉。2026 年关键分叉：（1）快速风格化——Pika 2.5（最快——20-45 秒/代——风格化效果如粉碎、融化——适合社交媒体）、（2）电影级写实——Luma Dream Machine 1.6（电影感深度——自然的视差和布光——适合电影预演和气氛镜头）、（3）品牌安全——Seedance 2.0（写实度最高——品牌细节保真——适合电商和广告）。
- **两帧过渡动画（Start-End Frame Interpolation）**：输入第一帧和最后一帧→AI 生成中间帧——实现平滑的转场和动画效果。Pika 2.5 Pikaframes 是消费级代表。核心应用：产品图的前后对比（"Before→After"的动态过渡）、风格转换的动画化过程、概念图的"初稿→终稿"展示。技术上比单图动画更可控——因为两端固定——AI 的任务是"填充合理的中间状态"而非"猜测所有运动"。
- **摄像头运动模拟（Camera Motion Simulation）**：AI 在 2D 图像上模拟 3D 摄影机运动——推拉（dolly zoom——前进或后退）、横摇（pan——左右旋转）、纵摇（tilt——上下旋转）、轨道（track——横向移动）。Runway Gen-4.5 的 Director Mode 提供了最精细的摄影机控制——像操作虚拟摄影机云台一样操作 I2V。种子差异：Seedance 2.0 的 3D 视差更准确（远景和近景的移动速度差更真实）——Luma 的电影感更强（景深虚化更自然）。
- **角色表情与动作捕捉映射（Character Performance Mapping）**：将真人动作（通过摄像头捕捉——面部表情、头部转向、手势）映射到 AI 角色或静态人像上。Runway Act-Two（摄像头→AI 角色——实时推理）和 DreamActor（字节跳动——静态人像→AI 推理的动态表演——不需要摄像头——纯 AI 猜测合理的人类运动）代表了两条技术路线——是否需要真人表演作为"驾驶信号"。
- **局部运动与静态区域保护（Local Motion with Static Area Preservation）**：在图像的特定区域添加运动——同时保持其他区域完全静态——避免"整图蠕动"的业余 I2V 效果。Runway Motion Brush（手动指定运动区域+方向+强度）和 Pika 2.5 Modify Region（在生成后局部修正不满意的区域）提供了消费级的局部运动控制。高级应用：产品图的"产品静止——背景动"——电商最需要的 I2V 能力。
- **循环动画生成（Loop Animation Generation）**：生成首尾无缝衔接的循环动画——特别适合社交媒体（循环播放的 GIF/短视频）和网页背景。I2V 循环的质量取决于模型是否理解"循环"的概念（首帧和尾帧需要视觉上平滑过渡——而非跳跃）。Runway 和 Pika 提供了循环生成模式——但 2026 年循环质量仍然不稳定——约 30-50% 的生成有明显的"循环点"跳跃。

---

## 形态谱系

- **专业创意 I2V 平台（Professional Creative I2V Platform）**：以 Runway Gen-4.5（Motion Brush、Director Mode、Act-Two、视频到视频风格迁移——$12-76/月——综合创意控制的标杆）为代表——面向需要精细控制和迭代的创意专业人士。核心价值：不是"一键生成"而是"反复迭代的导演工具"——像操作摄影机和后期软件一样操作 AI。
- **写实与品牌安全 I2V（Realism & Brand-Safe I2V）**：以 Seedance 2.0（字节跳动——写实度最高——品牌细节保真——电商优化——B2B/API 访问——每视频 $0.50-2）和 Luma Dream Machine 1.6（电影感 3D 空间一致性——深度和布光自然——$30-100/月）为代表——面向需要"看起来像真实拍摄"的电商、广告和预演用户。核心差异化：运动有多"真实"——图像中的文字和标志在动画中是否保持不变。
- **速度与社交媒体 I2V（Speed & Social I2V）**：以 Pika 2.5（最快——20-45 秒/代——Pikaffects 特效+Pikaframes 转场——$8-28/月——免费层可用）和 PixVerse（快速风格化社交短片）为代表——面向需要快速迭代和高产量的社交媒体创作者。核心价值：速度>完美、趣味>写实、数量>质量——社交媒体的内容经济学不同于电影制作。
- **API/企业 I2V 服务（API/Enterprise I2V Service）**：以 WaveSpeedAI（集成多种 I2V 模型——程序化调用——面向开发者的 API）和 ModelsLab（I2V API 基准——企业集成）为代表——面向将 I2V 嵌入自有产品和自动化工作流的企业。核心价值：可扩展性和程序化控制——不受 GUI 交互速度限制。
- **角色/头像动画特化 I2V（Character/Avatar Animation Specialist）**：以 DreamActor（字节跳动——静态人像→动态表演）和 Runway Act-Two（摄像头动作捕捉→AI 角色映射）为代表——面向需要将静态角色或人像转化为动态表演的动画师和内容创作者。核心差异化：面部表情和身体运动的自然度——是否看起来像动画而非"鬼片蠕动的照片"。

---

## 风险 · 合规 · 品牌安全与深度伪造（外部框架可对照）

- **品牌标志变形——I2V 最大的商业风险**：当 I2V 将产品图动画化时——品牌标志、产品标签和文字可能在动画过程中变形、抖动或完全改变——造成虚假广告或品牌资产损害。Seedance 2.0 是 2026 年在品牌细节保真度上最好的选择——但仍需人工审核每一段输出——标志和文字区域的变形可能很微妙但不被接受。最佳实践：在发布前逐帧检查关键品牌元素——特别是在大幅摄影机运动的 I2V 片段中。
- **真实人物的 AI 动画化——同意和隐私问题**：将含有真实人物的静态照片 I2V 动画化——使人物做出原图中没有的表情和动作——这可能构成对肖像权和隐私的侵犯。2026 年 SAG-AFTRA 协议（数字替身必须获得知情同意）和 NO FAKES 法案（未经授权的声音和外貌复制——联邦权利）为人物 I2V 设置了法律边界——I2V 将静态照片中的真人动画化本质上是在创建"数字替身"——即使动画质量不如专用的 deepfake 工具。
- **I2V 的动力来源——模型的训练数据版权**：I2V 模型的训练数据中包含了受版权保护的视频和图像——将这些受版权保护的运动模式"应用"到用户的图像上——这是否构成衍生作品侵权？2026 年这一法律问题完全未解决——在判例法明确之前，商业用户在使用 I2V 时应假设存在版权风险。

---

## 落地碎片

- **电商 I2V——用 Seedance 2.0 处理品牌关键产品（标志/文字不能被改变）——用 Pika 2.5 处理不需要文字保真的生活方式图**：Seedance 2.0 的品牌细节保真度最高——适合产品主图和需要精确展示品牌标志的场景。Pika 2.5 的速度和低成本（$8/月）适合大量生成生活方式动画（服装模特展示、室内设计巡览）——这些场景中的微小变形不构成品牌风险。
- **在 I2V 生成中使用"锁定+运动"策略——指定哪些区域应该移动、哪些应该保持完全静止**：使用 Runway Motion Brush 手动标记运动区域——将品牌标志、产品文字和关键产品特征区域排除在运动之外。这大幅降低了品牌元素被意外变形的风险。如果工具不支持区域运动控制（只有全图自动动画）——对品牌关键图像不推荐使用——全自动 I2V 几乎不可避免地会在某些帧中改变品牌元素。
- **I2V 的真实成本不是"每次生成价格"而是"每次可用输出成本"——预算时按 3-5 倍标价计算**：如果 I2V API 标价 $0.20/代——假设可用率 25-33%——每可用秒的实际成本约为 $0.60-1.00。这个倍数直接取决于你对"可用"的定义有多严格——品牌广告的标准远高于社交媒体帖子。在评估 I2V 工具时——运行一个 20 次生成的测试——计算有多少次输出是你愿意直接使用的——这会给出你对该工具的"真实成本"。

---

## 工具与产品类型

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| **Professional Creative I2V**（Runway Gen-4.5） | Motion Brush、Director Mode、Act-Two、视频到视频——$12-76/月 | 综合创意控制的标杆——电影预演和广告 |
| **Brand-Safe Realism I2V**（Seedance 2.0, Luma Dream Machine 1.6） | 写实度最高——品牌细节保真——3D 空间一致性 | 电商和广告（Seedance）与电影预演（Luma）的分叉 |
| **Speed & Social I2V**（Pika 2.5, PixVerse） | 最快生成——风格化特效——两帧过渡——$8-28/月 | 社交媒体——速度>完美——"有趣"而不是"真实" |
| **Character Avatar Animation**（DreamActor, Runway Act-Two） | 静态人像/角色→动态表演——摄像头动作捕捉映射 | 动画师和虚拟角色创作者——"不只是一张会动的照片" |
| **API/Enterprise I2V**（WaveSpeedAI, ModelsLab） | 多模型 API——程序化集成——面向开发者 | 将 I2V 嵌入自有产品——不受 GUI 速度限制 |

---

## 外链索引

> **分工规则**（详见 [video.md](./video.md) §内容分工）：通用 T2V 旗舰表见 [video-generator.md](./video-generator.md)；下表仅列 **I2V 语境** 差异点。

| 名称 | 一句话（I2V 语境） | URL |
|------|--------|-----|
| Runway Gen-4.5 | Motion Brush + Director Mode + Act-Two——I2V 精细控制标杆 | https://runwayml.com |
| Seedance 2.0 (ByteDance) | 品牌细节保真——电商产品图 I2V 首选 | https://wavespeed.ai (API) |
| Pika 2.5 | 最快 I2V + Pikaframes 两帧过渡——社交向 | https://pika.art |
| Luma Dream Machine 1.6 | 电影感 3D 视差——pre-vis 气氛镜头 | https://lumalabs.ai |
| DreamActor (ByteDance) | 静态人像→动态表演 | https://wavespeed.ai (API) |
| Kling 1.6 (Kuaishou) | 性价比 I2V API——运动画笔 | https://klingai.com |

**其它旗舰模型**（Veo / Hailuo 等 generator 级条目）：见 [video-generator.md](./video-generator.md) §外链索引。

### 对比与测评（第三方；观点非官方）

- **UlazAI 2026 最佳 I2V 生成器排名**：Seedance 2.0 被评为 I2V 写实度第一（与 Sora 并列）、Runway Gen-4.5 被评为创意控制第一、Luma 被评为电影感第一、Pika 被评为速度和社交内容第一。核心结论——没有全能冠军——每种 I2V 工具在不同维度上领先——选工具应按任务而非按品牌。
- **WaveSpeedAI 2026 AI 视频生成 API 完全指南**：Seedance 2.0 在图像到视频保真度上表现出色（品牌细节保持）、Runway 在专业编辑和运动控制上领先、Luma 在 3D 空间一致性上最好但片段长度受限（5-10 秒）。API 层对比：Veo 3.1（$0.35/秒——4K+原生音频——企业级）、Kling（$0.09/秒——最佳价值）、Runway（~$0.12/秒——创意控制）。
- **APIDog 2026 Luma 替代品对比**：Luma 的电影感在 I2V 领域独树一帜——但价格（$0.25/秒——2-3 倍于 Runway 和 Kling）和短片段（5-10 秒）限制了其在长内容和高产量场景中的竞争力。Runway 是 Luma 最自然的"控制替代品"——Seedance 是"写实度替代品"——Kling 是"预算替代品"。

---

## 延伸阅读 · 站内知识块
- 品类 Hub：[image.md](./image.md) · [video.md](./video.md)
- 生成层 SSOT：[image-generator.md](./image-generator.md)（静态图来源 · §共享事实速查）
- 视频簇：[video-generator.md](./video-generator.md) · [text-to-video.md](./text-to-video.md) · [video-to-video.md](./video-to-video.md)

## 延伸阅读 · 站外

- UlazAI — "Best AI Image-to-Video Generators 2026: Runway, Kling, Luma and Pika"
- WaveSpeedAI — "Complete Guide to AI Video Generation APIs in 2026"（API 层 I2V 对比——Veo 3.1、Seedance 2.0、Runway、Kling、Luma）
- APIDog — "Best Luma AI Alternatives in 2026"（Luma vs 替代品的成本、质量和时长对比）
- Textify Analytics — "The Ten Best Image Motion Platforms For 2026"
- ModelsLab — "AI Video Generation API Benchmarks 2026"（API 质量和速度基准）
