# AI Image-to-Video · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Image-to-Video / I2V / 图生视频**——输入为**已有静态图**（照片、插画、产品图），输出为含运动、视差或角色表演的短视频；验收以**运动写实、品牌/细节保真、废片率与每可用秒成本**为主。本页为 **I2V 产品 SSOT**（完整 URL 表仅此一处）；从零 T2V → [text-to-video.md](text-to-video.md)；全片风格化 → [video-to-video.md](video-to-video.md)；跨模态旗舰 → [video-generator.md](video-generator.md)。

**材料范围**：公开网络检索（Runway/Seedance/Luma/Pika/Kling 厂商官网、WaveSpeed API 指南、UlazAI/APIDog 工具对比评测）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。**具体参数、定价与 API 条款以各官网为准**。网摘整理日期 **2026-09-02**。

**站内相邻**：[image.md](../image/image.md) · [image-generator.md](../image/image-generator.md) · [video.md](video.md) · [video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [video-to-video.md](video-to-video.md)

**站内对照**：[alignify.co/tools/image-to-video](https://alignify.co/tools/image-to-video) · `content/tools/en/image-to-video.md` · [alignify.co/zh/tools/image-to-video](https://alignify.co/zh/tools/image-to-video) · `content/tools/zh/image-to-video.md` · slug **`image-to-video`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 `#image-to-video-tools`

---

## 与相邻 slug 分流（避免混买混评）

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

- **AI 图像到视频（AI Image-to-Video / I2V）**：从一张或多张静态图像生成动态视频——输入为照片、插画、概念艺术或产品图——输出为包含运动、视差、相机推拉或角色动画的短视频片段。与 T2V 的核心区别：I2V 起点是「你已有的图像」——AI 的角色是「让它动起来」而非「创造全新视觉世界」。2026 年 I2V 五个关键竞争维度：运动写实度、品牌/细节保真度（图像中的文字和标志是否在动画中保持不变）、最大时长、分辨率和**每可用秒成本**（cost per usable second——考虑重试后的废片率）。
- **运动画笔（Motion Brush）**：在图像特定区域用画笔指定运动方向和强度的交互方式——「头发向右边飘、衣服随风摆、水流向左」。区别于整图自动动画的不可控性——给予导演像素级运动控制——使 I2V 从「AI 一次性猜测」变成「导演反复迭代工具」；典型实现见 §外链索引 **Type A**。
- **关键帧动画（Keyframe Animation / Start+End Frame）**：提供第一帧和最后一帧——AI 在两帧之间自动生成平滑过渡。与单图 I2V 的区别：两端锁定——AI 任务为插值而非猜测整个运动方向——降低「猜错运动」概率；消费级代表见 §外链索引 **Type C**。
- **角色动画（Character Animation / Performance Mapping）**：将静态角色图像（插画角色、数字人、历史人物肖像）转化为具表情、口型和身体动作的动态表演——路线分 **摄像头动作捕捉→角色映射** 与 **纯 AI 推理（静态人像→动态表演）** 两条；见 §外链索引 **Type E**。
- **空间一致性与 3D 感知动画（Spatial Coherence & 3D-Aware Animation）**：动画化时保持空间深度和 3D 几何一致性——不仅是「像素在移动」而是「相机在 3D 空间中移动」——近景移动快、远景移动慢，产生电影感深度而非生硬 2D 滑动。
- **风格保留与细节保真度（Style Preservation & Detail Fidelity）**：动画化过程中保持原图风格（油画、水彩、照片写实、动漫）和关键细节（品牌标志、文字、产品纹理）不变——「添加运动」与「保持原图」存在天然技术张力——模型越「创造性地」添加运动，越可能改变原图细节；电商 I2V 的核心验收维度。

---

## 专题对照 / 扩展定义

**三种 I2V 输入模式**：术语定义见 §词汇锚点；下表只列**买家体验差**，不重复术语。

| 维度 | 单图动画（Single Image） | 两帧过渡（Start+End Frame） | 多图序列（Image Sequence） |
|------|------------------------|---------------------------|--------------------------|
| **典型 Type** | 见 §外链索引 **Type A–C** | 见 §外链索引 **Type C** | 见 §外链索引 **Type A** + 专业 VFX 管线 |
| **控制精度** | 低——AI 猜测运动方向 | 中——用户指定起点和终点 | 高——AI 填充帧间间隙而非猜测整个运动 |
| **适用场景** | 快速「让概念图动起来」——社交媒体和预演 | 转场效果、产品展示「前后对比」动画 | 已有粗略动画需平滑帧率——VFX 和动画管线 |
| **失败风险** | 高——可能猜错运动方向或不自然变形 | 中——两端锁定→中间通常平滑但可能「太线性」 | 低——任务是插值而非推理 |

| 维度 | 写实派（Photorealistic I2V） | 风格派（Stylized I2V） |
|------|---------------------------|---------------------|
| **典型 Type** | 见 §外链索引 **Type B** | 见 §外链索引 **Type C** |
| **核心价值** | 「让照片动起来——像真实摄影机运动」 | 「让插画、概念艺术动起来——创造奇幻视觉效果」 |
| **用户** | 电商（产品展示）、摄影师、地产（虚拟参观） | 概念艺术家、社交媒体创作者、动画师 |
| **质量评判标准** | 运动物理真实度——是否有不自然变形和扭曲 | 运动创意度——是否有趣、惊艳、与风格一致 |

架构路线（专业创意 / 品牌安全 / 速度社交 / API 企业 / 角色动画）→ **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **「静态图像的死亡」——数字视觉内容正被期望为动态**：从 Instagram Stories 到 TikTok 到电商产品页——「静态图像」正在失去注意力竞争优势。I2V 填补的核心缺口：数十亿存量静态图像（产品图、品牌资产、历史照片、概念艺术）——拍摄时从未预期需要变为视频——现在有了批量转换技术路径。这不是替代视频拍摄——而是让存量图像资产获得第二次生命。
- **产品图和品牌资产的「视频化」需求**：电商平台（Amazon、Shopify）和社交媒体广告（Meta、TikTok）系统性偏好视频——但品牌拥有数十万静态产品图——重拍视频成本不可承受。I2V 让品牌以约 **$0.10–0.50/图** 将静态产品图转化为 5–10 秒产品展示动画——用于广告、产品页和社交媒体。**品牌细节保真**是电商 I2V 核心需求（标志和产品文字不能在动画中变形）——选型见 §外链索引 **Type B**。
- **概念艺术和预演——「在拍摄之前先看到它动起来」**：电影和广告前期——导演和 DP 需可视化场景应如何运动——传统靠故事板（静态）或昂贵 3D 预演。I2V 提供第三条路径——将概念艺术或故事板帧直接转化为动态预演——成本从数千美元降至几十美分——速度从数周降至数分钟。
- **「废片率」是 I2V 隐藏的真实成本——而非生成成本**：多数 I2V 工具按每次生成计费（约 **$0.10–0.50/Gen**）——但实际可用率（5–10 次生成中至少一次「可直接使用」）通常低于 **30–50%**。每可用秒实际成本约为标价的 **2–4 倍**。2026 年隐蔽关键选型因素不是「每代成本」而是「每可用秒成本」——取决于你对「可用」的标准有多高。
- **短内容生态的「动图即默认」期望**：从 LinkedIn 轮播到 WhatsApp Status 到公众号封面——几乎所有数字触点都在要求「至少让图片动一下」。I2V 使非视频团队（写作者、设计师、社交媒体运营）也能满足这一期望——与 [animation-generator.md](animation-generator.md)（全动画视频）和 [video-generator.md](video-generator.md)（原生视频生成）形成从轻到重的工具链。

---

## 能力栈（概念拆分，非厂商功能表）

- **单图动态化（Single Image Animation）**：核心 I2V 能力——输入单张静态图→AI 推断深度图→识别可运动区域（头发、水、衣服、树叶）→生成自然循环运动或一次性相机推拉。2026 年关键分叉：**快速风格化**（速度优先、特效向）、**电影级写实**（视差与布光自然——pre-vis 气氛镜头）、**品牌安全**（写实度与细节保真——电商和广告）；各路线代表见 §形态谱系 **Type A–C**。
- **两帧过渡动画（Start-End Frame Interpolation）**：输入第一帧和最后一帧→AI 生成中间帧——实现平滑转场。核心应用：产品图前后对比（Before→After）、风格转换动画化、概念图「初稿→终稿」展示。技术上比单图更可控——两端固定——AI 任务为「填充合理中间状态」而非「猜测所有运动」。
- **摄像头运动模拟（Camera Motion Simulation）**：在 2D 图像上模拟 3D 摄影机运动——推拉（dolly zoom）、横摇（pan）、纵摇（tilt）、轨道（track）。精细控制（Director Mode 类）使 I2V 像操作虚拟云台；验收维度包括 3D 视差准确性（远近景速度差）与景深虚化自然度。
- **角色表情与动作捕捉映射（Character Performance Mapping）**：将真人动作（摄像头捕捉——面部表情、头部转向、手势）映射到 AI 角色或静态人像；或纯 AI 推理生成合理人类运动——无需摄像头。两条技术路线：**是否需要真人表演作为驾驶信号**——见 §形态谱系 **Type E**。
- **局部运动与静态区域保护（Local Motion with Static Area Preservation）**：在特定区域添加运动——同时保持其他区域完全静态——避免「整图蠕动」的业余效果。高级应用：产品图「产品静止——背景动」——电商最需要的 I2V 能力；手动区域指定见 §词汇锚点 **Motion Brush**。
- **循环动画生成（Loop Animation Generation）**：生成首尾无缝衔接的循环动画——适合社交媒体（循环 GIF/短视频）和网页背景。质量取决于模型是否理解「循环」概念（首尾帧需视觉平滑过渡）；2026 年循环质量仍不稳定——约 **30–50%** 生成有明显「循环点」跳跃。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 精细控制、反复迭代、导演向 GUI | Professional Creative I2V | Runway Gen-4.5 |
| **B** | 写实度与品牌细节保真、3D 空间一致性 | Brand-Safe Realism I2V | Seedance 2.0、Luma Dream Machine 1.6 |
| **C** | 速度优先、风格化特效、社交产量 | Speed & Social I2V | Pika 2.5、PixVerse |
| **D** | 多模型 API、程序化集成、按秒计费 | API/Enterprise I2V | WaveSpeedAI、ModelsLab、Kling 1.6 |
| **E** | 静态人像/角色→动态表演、动作捕捉映射 | Character Avatar Animation | DreamActor、Runway Act-Two |

**Type A vs B**（均面向专业用户，诉求不同）：A 强调**控制面与迭代工作流**（Motion Brush、Director Mode）；B 强调**输出像真实拍摄且品牌元素不变**——电商主图 vs 电影 pre-vis 的分叉见 §外链索引定价与时长列。

**Type C vs D**（均可高产量）：C 为创作者 GUI 快速迭代；D 为嵌入自有产品的 API 层——不受 GUI 交互速度限制。

---

## 风险 · 合规 · 品牌安全与深度伪造（外部框架可对照，非法律意见）

- **品牌标志变形——I2V 最大的商业风险**：产品图动画化时——品牌标志、产品标签和文字可能在动画中变形、抖动或完全改变——造成虚假广告或品牌资产损害。**Type B** 产品在品牌细节保真度上通常领先——但仍需人工审核每一段输出——标志和文字区域变形可能很微妙。最佳实践：发布前逐帧检查关键品牌元素——特别是在大幅摄影机运动的 I2V 片段中。
- **真实人物的 AI 动画化——同意和隐私问题**：将含真实人物的静态照片 I2V 动画化——使人物做出原图中没有的表情和动作——可能构成肖像权和隐私侵犯。2026 年 SAG-AFTRA 协议（数字替身须知情同意）和 NO FAKES 法案（未经授权的声音和外貌复制——联邦权利）为人物 I2V 设置法律边界——I2V 将静态照片中的真人动画化本质上是在创建「数字替身」——即使动画质量不如专用 deepfake 工具。
- **I2V 的动力来源——模型的训练数据版权**：I2V 模型训练数据含受版权保护的视频和图像——将受保护的运动模式「应用」到用户图像上——是否构成衍生作品侵权？2026 年这一法律问题完全未解决——在判例法明确之前，商业用户应假设存在版权风险。

---

## 落地碎片（无先后）

- **电商 I2V 分层策略**：**Type B** 处理品牌关键产品（标志/文字不能被改变）；**Type C** 处理不需要文字保真的生活方式图（服装模特展示、室内设计巡览）——微小变形不构成品牌风险。
- **「锁定+运动」策略**：用手动区域运动控制（Motion Brush 类）标记运动区域——将品牌标志、产品文字和关键特征排除在运动之外——大幅降低品牌元素意外变形风险。若工具不支持区域控制（仅全图自动动画）——对品牌关键图像不推荐使用。
- **真实成本按 3–5 倍标价预算**：若 API 标价 **$0.20/Gen**——假设可用率 **25–33%**——每可用秒实际成本约 **$0.60–1.00**。倍数取决于「可用」定义——品牌广告标准远高于社交媒体帖子。评估时跑 **20 次生成测试**——计算有多少次输出愿意直接使用——得出对该工具的「真实成本」。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

> **分工规则**（详见 [video.md](video.md) §内容分工）：通用 T2V 旗舰表见 [video-generator.md](video-generator.md)；下表仅列 **I2V 语境** 差异点。

| 名称 | Type | 一句话（I2V 语境） | URL |
|------|------|---------------------|-----|
| **Runway Gen-4.5** | A | Motion Brush + Director Mode + Act-Two + V2V 风格迁移——$12–76/月——I2V 精细控制标杆 | [runwayml.com](https://runwayml.com) |
| **Seedance 2.0** (ByteDance) | B | 写实度最高——品牌细节保真——电商产品图 I2V 首选——B2B/API——约 $0.50–2/视频 | [wavespeed.ai](https://wavespeed.ai) (API) |
| **Luma Dream Machine 1.6** | B | 电影感 3D 视差与空间一致性——深度和布光自然——$30–100/月——片段通常 5–10 秒 | [lumalabs.ai](https://lumalabs.ai) |
| **Pika 2.5** | C | 最快 I2V（约 20–45 秒/代）+ Pikaframes 两帧过渡 + Pikaffects 特效——$8–28/月——免费层可用 | [pika.art](https://pika.art) |
| **PixVerse** | C | 快速风格化社交短片——速度>完美——趣味向 | [pixverse.ai](https://pixverse.ai) |
| **DreamActor** (ByteDance) | E | 静态人像→AI 推理动态表演——不需摄像头——专门人体/头像动画 | [wavespeed.ai](https://wavespeed.ai) (API) |
| **Runway Act-Two** | E | 摄像头动作捕捉→AI 角色映射——实时推理 | [runwayml.com](https://runwayml.com) |
| **Kling 1.6** (Kuaishou) | D | 性价比 I2V API——运动画笔——约 $0.09/秒 | [klingai.com](https://klingai.com) |
| **WaveSpeedAI** | D | 集成多种 I2V 模型——程序化调用——面向开发者 API | [wavespeed.ai](https://wavespeed.ai) |
| **ModelsLab** | D | I2V API 基准——企业集成——质量与速度 benchmark | [modelslab.com](https://modelslab.com) |

**其它旗舰模型**（Veo / Hailuo 等 generator 级条目）：见 [video-generator.md](video-generator.md) §外链索引。

### 对比与测评（第三方；观点非官方）

- **UlazAI 2026 最佳 I2V 生成器排名**：Seedance 2.0 被评为 I2V 写实度第一（与 Sora 并列）、Runway Gen-4.5 被评为创意控制第一、Luma 被评为电影感第一、Pika 被评为速度和社交内容第一。核心结论——没有全能冠军——每种 I2V 工具在不同维度上领先——选工具应按任务而非按品牌。
- **WaveSpeedAI 2026 AI 视频生成 API 完全指南**：Seedance 2.0 在图像到视频保真度上表现出色（品牌细节保持）、Runway 在专业编辑和运动控制上领先、Luma 在 3D 空间一致性上最好但片段长度受限（5–10 秒）。API 层对比：Veo 3.1（$0.35/秒——4K+原生音频——企业级）、Kling（$0.09/秒——最佳价值）、Runway（~$0.12/秒——创意控制）。
- **APIDog 2026 Luma 替代品对比**：Luma 的电影感在 I2V 领域独树一帜——但价格（$0.25/秒——2–3 倍于 Runway 和 Kling）和短片段（5–10 秒）限制了长内容和高产量场景竞争力。Runway 是 Luma 最自然的「控制替代品」——Seedance 是「写实度替代品」——Kling 是「预算替代品」。

*本小节为网摘与媒体观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **UlazAI** — "Best AI Image-to-Video Generators 2026: Runway, Kling, Luma and Pika"
- **WaveSpeedAI** — "Complete Guide to AI Video Generation APIs in 2026"（API 层 I2V 对比——Veo 3.1、Seedance 2.0、Runway、Kling、Luma）
- **APIDog** — "Best Luma AI Alternatives in 2026"（Luma vs 替代品的成本、质量和时长对比）
- **Textify Analytics** — "The Ten Best Image Motion Platforms For 2026"
- **ModelsLab** — "AI Video Generation API Benchmarks 2026"（API 质量和速度基准）

**站内**

- 品类 Hub：[image.md](../image/image.md) · [video.md](video.md)
- 生成层 SSOT：[image-generator.md](../image/image-generator.md)（静态图来源 · §共享事实速查）
- 视频簇：[video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [video-to-video.md](video-to-video.md)