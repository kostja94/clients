# AI Text-to-Video · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网、产品评测、社区讨论、技术媒体对比文）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-24**（簇去重修订）。


**站内相邻**：[video.md](video.md)（品类总览）· [video-generator.md](video-generator.md)（通用模型 SSOT）· [image-to-video.md](image-to-video.md) · [video-editor.md](video-editor.md)

**勿与…混买**：本页主轴为 **输入=文本/文档**；通用扩散模型完整 URL 表见 video-generator；静态图起点见 image-to-video。

**站内对照**：[alignify.co/tools/text-to-video](https://alignify.co/tools/text-to-video) · `/tools/text-to-video` · [alignify.co/zh/tools/text-to-video](https://alignify.co/zh/tools/text-to-video) · `/zh/tools/text-to-video` · `content/tools/zh/text-to-video.md`、`content/tools/en/text-to-video.md` · slug **`text-to-video`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#text-to-video-tools`](../../product/alignify-keywords-tools.md#text-to-video-tools)

**与相邻 slug 分流**：text-to-video（文本/文档 → 视频生成）↔ image-to-video（静态图 → 动态视频）↔ video-generator（通用视频生成，含 T2V/I2V/多模态模型）↔ video-editor（已有视频的编辑修剪，非从头生成）。text-to-video 与 video-generator 的边界在于：前者聚焦「输入模态为文本」的产品与工作流，后者涵盖所有模态的底层模型与综合平台。Veo 3、Sora 2 等跨模态模型同时在两个文件中出现，但以 video-generator 为主归属。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Text-to-Video (T2V) / 文生视频**：以自然语言提示词（prompt）或文档为输入，AI 模型生成动态视频内容的技术品类。区别于 image-to-video（I2V，静态图像为起点）和 video-to-video（V2V，已有视频为输入做风格迁移或编辑）。
- **Prompt adherence / 提示词遵循度**：模型对文本描述中场景、主体、动作、风格、镜头语言的执行精度——是 T2V 评测的核心指标之一，直接影响可复现性。
- **Native audio generation / 原生音频生成**：视频生成模型在单次推理中同步输出配乐、环境音或对话音轨的能力。2026 年 Veo 3.1 和 Kling 3.0 率先实现商用级联合音视频生成，被视为 T2V 从「无声 GIF」进化为「完整视频」的分水岭。
- **Multi-shot composition / 多镜头组合**：在单一生成中编排多个连续镜头（如远景→特写→跟随），算法需保持主体一致性（character consistency）、光照连续性和空间逻辑。Kling 3.0 和 Seedance 2.0 在此维度领先。
- **Physics engine / 物理引擎**：模型对现实世界物理规则（重力、碰撞、布料飘动、液体流动、人体运动学）的内在理解——决定视频的「可信度」而非画质。评测中常以「人物走路是否滑步」「液体倒出是否自然」为典型案例。
- **AI explainer video / AI 讲解视频**：T2V 的垂直子品类，从文本/文档生成带 AI 配音的教学或营销讲解视频，风格包括白板手绘（whiteboard animation）、动画讲解、数字人播报。代表产品：Golpo AI、VideoTutor、Synthesia。
- **Credit-based pricing / 积分定价**：T2V 工具的主流计费方式——按生成视频的秒数消耗积分，而非按月订阅无限制使用。Runway（~5–12 credits/sec）、CapCut（免费额度 + 付费加速）等均采用此模型，原因是推理算力成本高。
- **Manim / 数学动画引擎**：Python 开源的精确数学动画库，VideoTutor 将其与自研几何解析模型结合，实现对复杂几何图形、公式推导的可编程动画生成——区别于扩散模型的逐像素生成，成本和精度更可控。

---

## 专题对照：通用视频生成 vs 垂直讲解视频

| 维度 | 通用 T2V（Runway/Veo/Kling） | AI 讲解视频（Golpo/VideoTutor/Synthesia） |
|------|------------------------------|------------------------------------------|
| 核心输入 | 短 prompt（1–3 句） | 长文本/文档/题目图片 |
| 输出形态 | 短片段（3–60 秒），通常无声或合成音轨不完整 | 完整视频（1–15 分钟），配音+动画+字幕齐全 |
| 底层技术 | 扩散模型/Transformer 逐像素生成 | 脚本规划 + 素材组合 + 动画引擎渲染 |
| 控制精度 | prompt 即唯一控制面，细粒度编辑困难 | 可逐帧编辑脚本、替换素材、调整动画节奏 |
| 典型买家 | 创意工作室、广告代理、电影预演 | 教育机构、企业培训、YouTube 自动化频道 |
| 2026 年关键趋势 | native audio、物理引擎、多镜头组合 | 自研动画引擎、交互式教学（打断追问） |

---

## 问题域（为何会出现这类产品）

- **视频制作成本结构的根本矛盾**：传统摄制单分钟成本远高于 T2V API 调用——让「为一句话生成视频」成为可行选项（宏观成本曲线见 [video-generator.md](video-generator.md)）。
- **Sora 退场与多供应商管线**：Sora 2 已关停（共享事实见 [video.md](video.md) §全簇共享事实）——T2V 选型应组合至少两家 API，详见 video-generator。
- **无声视频的体验天花板**：早期 T2V 模型输出均为无声片段，用户需额外配音配乐。2026 年 native audio 的普及（Veo/Kling）将 T2V 从「动态素材」升级为「可消费的完整视频」。
- **教育与企业培训的规模化需求**：每门课程、每个产品、每个 SOP 都需要讲解视频——传统制作无法规模化。AI 讲解视频（Golpo、VideoTutor、Synthesia）填补了「需要 1000 个视频但只有 1 个视频团队」的缺口。
- **社交媒体内容工厂化**：TikTok/Reels/Shorts 的算法奖励高频发布。T2V 让创作者从「每周 3 条」变成「每天 10 条」，Pika、CapCut 等工具核心服务于这一场景。

---

## 能力栈（概念拆分，非厂商功能表）

- **提示词理解与场景构图**：从文本中抽取主体、动作、环境、风格、镜头指令；模型对空间关系（「左边」「后面」「从上方」）的理解决定构图的可用性。
- **时序一致性与物理合理性**：跨帧保持主体外观、光照方向和运动轨迹的一致性；物理引擎（重力、碰撞、流体）决定真实感，是 2026 年模型间的核心差距维度。
- **原生音频联合生成**：单次推理同步输出配乐/环境音/对话；Veo 3.1 和 Kling 3.0 在此领先；多数工具仍需外部配音工具补充。
- **多镜头编排与主体保持**：连续镜头切换时维持角色、场景、风格一致；需要显式的「角色参考图/描述」支持（Runway Reference、Seedance）。
- **分辨率与时长控制**：从 Pika 的 720p/5s 到 Kling 的 4K/120s，分辨率和时长直接决定可用的交付场景（社交媒体 vs 广告片 vs 课程视频）。
- **编辑与迭代工作流**：生成后的微调能力——Runway 的 Motion Brush、CapCut 的多轨时间线、Golpo 的逐帧 prompt 编辑——决定了工具是「一次性生成器」还是「创作平台」。
- **模板与脚本自动化**：讲解视频子类的核心能力——AI 从文档自动写脚本、分镜、选风格、配语音——决定规模化生产效率（Golpo 的 prompt→完整视频、VideoTutor 的题目→教学视频）。

---

## 形态谱系（与具体品牌解耦）

- **通用扩散模型型**：纯 prompt→短视频，强写实度，弱编辑控制。代表方向是「AI 摄影棚」——替换实拍素材的 B-roll、预演、概念片。Runway、Veo、Kling 属此类型。
- **全栈创作平台型**：T2V 生成 + 多轨时间线编辑 + 素材库 + 字幕/音效，面向「在一个工具里完成从 0 到交付」的用户。CapCut、PowerDirector 是典型。
- **AI 讲解视频型**：从长文本/文档/题目自动生成带配音、动画、字幕的完整讲解视频。脚本→分镜→动画→配音→输出全自动。Golpo（白板手绘风格）、VideoTutor（数学动画引擎）、Synthesia（数字人播报）分别占据不同风格生态位。
- **社交特效型**：轻量、风格化、病毒传播导向——Pika 的 Pikaffects（cakeify/melt/inflate）、Viggle 的 3D 角色替换舞蹈等。不追求写实，追求可分享性。
- **数字人播报型**：AI 虚拟形象朗读脚本，面向企业培训、产品介绍、新闻播报。Synthesia、HeyGen、DeepBrain AI 占据此方向——输入是脚本，输出是数字人出镜视频。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **深度伪造与身份冒用**：T2V 模型可生成以假乱真的人物视频，被滥用于政治虚假信息、金融诈骗、非自愿色情内容。各国监管正在分化——欧盟 AI Act 要求标注 AI 生成内容，中国要求显式水印，美国联邦层面尚无统一立法。
- **版权与训练数据争议**：T2V 模型训练集通常抓取自公开网络视频，原始创作者未获授权也未获补偿——这是 2026 年最活跃的 AI 版权诉讼领域之一。使用 T2V 工具生成的视频，其版权归属在多数司法辖区未明确。
- **Sora 的前车之鉴与产品停运风险**：Sora 2 于 2026-03-24 宣布关停（Web/App 2026-04-26、API 2026-09-24）——依赖单一 T2V 平台的生产管线面临供应商风险。Veo 3.1、Runway、Kling 3.0 提供替代路径，但每家都可能调整定价或关闭服务。
- **教育内容的准确性与责任**：AI 讲解视频（Golpo、VideoTutor）自动生成教学内容——若 AI 生成的数学推导有误、历史事实偏差、或科学解释错误，责任归属模糊（平台方、用户、还是模型提供方？）。
- **算力成本与商业可持续性**：T2V 推理的 GPU 消耗远超文本/图像生成。Sora 的失败是算力经济学的典型案例——积分定价、按秒计费、免费额度限制是行业的生存策略，不是贪婪。

---

## 落地碎片（无先后）

- 先分清楚需求：需要「10 秒素材片段」（用 Runway/Veo/Kling）还是「5 分钟完整讲解视频」（用 Golpo/VideoTutor/Synthesia）——选错品类等于拿菜刀砍树。
- 对通用 T2V，不同模型有不同风格倾向——Veo 偏写实电影感，Pika 偏社交特效，Kling 偏长镜头叙事——先试各家的免费额度找到匹配风格的。
- 教育/培训场景不要用通用 T2V 模型逐段生成再拼接——讲解视频专用工具（Golpo、VideoTutor）已把脚本→分镜→动画→配音全自动化，效率和一致性远超手动组合。
- 2026 年建 T2V 生产管线时避讳单一供应商——Sora 关闭是教训。建议至少接入两家 API（如 Runway + Kling 或 Veo + 自部署开源模型）。
- 关注 native audio——无声视频在社交媒体的完播率显著低于带音频的视频。优先选 Veo 3.1 或 Kling 3.0 等支持联合音视频生成的方案。
- 商业用途前检查版权条款——部分工具（如 Runway）对 Pro 以上套餐提供商业使用权，部分工具（如免费 CapCut）生成内容的商用条款需逐条核对。

---

## 工具与产品类型（「text-to-video」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **General T2V model / platform** | prompt→短视频片段，扩散模型驱动 | 与 image-to-video、video-generator 交叉 |
| **AI explainer / whiteboard video** | 文档/文本→完整讲解视频，脚本+动画+配音全自动 | 输入是长文本而非短 prompt |
| **AI avatar / presenter video** | 数字人出镜朗读脚本的视频生成 | 与 avatar、lip-sync slug 相邻但输入模态不同 |
| **Social / effects T2V** | 轻量特效视频生成，病毒传播导向 | 不追求写实，追求可分享性和速度 |
| **All-in-one video creation suite** | T2V + 剪辑 + 字幕 + 素材库一体化 | 与 video-editor slug 功能重叠需交叉引用 |

---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

### 通用 T2V 模型与平台（摘要）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Google Veo 3.1** | T2V 评测轴代表：native audio + prompt 遵循 + 4K | [deepmind.google](https://deepmind.google/) |
| **CapCut** | **本块独占**：T2V + 多轨编辑 + 数字人 + 字幕一体化，TikTok 生态 | [capcut.com](https://www.capcut.com/) |

**完整旗舰横评**（Runway / Kling / Pika / Luma / Hailuo / Sora 关停说明等）：见 [video-generator.md](video-generator.md) §外链索引。

### AI 讲解视频（Explainer / 白板手绘）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Golpo AI** | YC S25 · Stanford 团队，prompt/文档→白板手绘讲解视频，50+ 语言，$39.99/月起 | [video.golpoai.com](https://video.golpoai.com/) |
| **VideoTutor** | $11M 种子轮 · 自研几何解析模型 + Manim 数学动画引擎，题目→AI 教学视频，TikTok 5000 万+ 播放 | [videotutor.io](https://videotutor.io/) |
| **Synthesia** | 企业级 AI 数字人播报，120+ 语言，超写实虚拟形象，$18/月起 | [synthesia.io](https://www.synthesia.io/) |
| **HeyGen** | UGC 风格 AI 数字人视频 + 配音本地化，API 接入，$29/月起 | [heygen.com](https://www.heygen.com/) |
| **InVideo AI** | prompt→完整视频（脚本+素材+配音），6000+ 模板，YouTube 自动化频道常用 | [invideo.io](https://invideo.io/) |
| **Pictory** | 长文/博客→短视频摘要 + 字幕，内容再利用，$19/月起 | [pictory.ai](https://pictory.ai/) |
| **Lumen5** | 博客/文章→社交视频，RSS 自动导入，拖拽编辑，含免费计划 | [lumen5.com](https://www.lumen5.com/) |

### 数字人播报 / AI Avatar 视频

| 名称 | 一句话 | URL |
|------|--------|-----|
| **DeepBrain AI** | 新闻演播室风格 AI 主播，多语言，企业级 | [deepbrain.io](https://www.deepbrain.io/) |
| **Veed.io** | 浏览器端视频编辑 + AI 自动字幕 + T2V，$24/月起 | [veed.io](https://www.veed.io/) |

### 动画与特效

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Viggle AI V4** | JST 3D 运动引擎，多角色替换与 foot-lock 物理，$9.99/月起 | [viggle.ai](https://viggle.ai/) |
| **Pixverse AI V3.5** | MultiShot AI Agent 多镜头叙事，20 秒 1080p，唇形同步 | [pixverse.ai](https://pixverse.ai/) |

### 对比与测评（第三方；观点非官方）

综合 Artificial Analysis 视频基准、社区评测（Reddit r/aivideo、r/TextToVideo、X/Twitter）、以及多篇 2026 横评博文，T2V 赛道的核心叙事在 2026 年发生了结构性变化。

**Sora 关闭重塑了市场格局。** 2024 年 Sora 以惊人的写实度定义了公众对 T2V 的想象，但 2026-03-24 OpenAI 宣布关停（Web/App 2026-04-26、API 2026-09-24）——社区讨论的核心结论是「模型能力 ≠ 产品可持续性」。Veo 3.1 被普遍视为最接近的替代方案，尤其在 prompt 遵循度和 native audio 方面领先。但社区也指出 Veo 的编辑工作流不如 Runway 成熟——Runway 的 Motion Brush 和摄像机控制仍然是专业创作者不可替代的工具。

**没有「最好的 T2V 模型」，只有最适合场景的组合。** 评测社区的主流观点是专业创作者已形成「多工具组合」惯习：Runway 做受控镜头，Veo 或 Kling 做写实叙事片段，Pika 做社交特效。教育/培训场景的讨论则独立于通用 T2V——教育科技社区更关注 Golpo AI 和 VideoTutor 等讲解视频专用工具，因为它们解决了「通用模型生成 60 秒片段后还要手动拼脚本配音」的碎片化问题。

**Native audio 是 2026 年评测的决定性差异维度。** 多篇横评将「是否原生生成音频」列为第一筛选条件——因为无声视频在社交媒体完播率显著低于带音频内容，而后期配音的工作量抵消了 T2V 的效率优势。Veo 3.1 和 Kling 3.0 在此维度领先，Runway 的音频能力被普遍评为「仍需外部工具补充」。

**定价模式争议持续。** 积分制（按秒计费）是主流，但社区对「积分消耗不透明」「高分辨率片段消耗暴增」有普遍不满。Pika $8/月的低价位和 CapCut 的大方免费额度在 Reddit 被频繁推荐为入门首选。Runway Unlimited $76/月被评价为「对重度用户合理，对偶尔使用的创作者偏贵」。

**教育 T2V 的独特叙事。** VideoTutor 以 $11M 种子轮和 5000 万 TikTok 播放的有机增长，证明了「AI 不只给答案，更可生成教学视频」的市场需求——其自研几何解析模型 + Manim 动画引擎的技术路线，被教育科技评论者视为优于「通用 LLM + 通用 T2V 组合」的解法。Golpo AI 的 $4.1M 种子轮和 YC 背景则锚定了「白板手绘讲解」这一垂直风格的商业化可行性。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各工具厂商自有营销博文为论证主体。*

---

## 延伸阅读 · 站内知识块

- 并列/上游：[video.md](video.md) · [video-generator.md](video-generator.md) · [image-to-video.md](image-to-video.md)
- 下游：[video-editor.md](video-editor.md) · [video-clipping.md](video-clipping.md)

**站外**

- **Artificial Analysis · Video Generation Benchmark** — 2026 年 T2V 模型客观评测基准（prompt 遵循度、运动质量、物理合理性）。[Artificial Analysis](https://artificialanalysis.ai/)
- **Pixflow · "Best AI Video Generator in 2026"** — Runway/Veo/Kling/Seedance 横评。[Pixflow](https://pixflow.net/blog/best-ai-video-generator/)
- **WaveSpeed · "Complete Guide to AI Video Generation APIs in 2026"** — API 接入与定价对比。[WaveSpeed](https://wavespeed.ai/blog/posts/complete-guide-ai-video-apis-2026/)
- **VideoTutor 融资与产品叙事** — YZi Labs 领投 $11M，由「给答案」到「生成教学」的 AI 教育范式转变。[GlobeNewswire](https://www.globenewswire.com/de/news-release/2026/05/01/3285655/0/en/videotutor-surpasses-50-million-tiktok-views-signals-shift-in-ai-education-from-giving-answers-to-generating-instruction.html)
- **Golpo AI 2.0 发布与 $4.1M 种子轮** — YC S25，Stanford 团队，AI 原生白板讲解视频。[EIN Presswire](https://www.einpresswire.com/article_print/892180959/golpo-ai-launches-golpo-2-0-and-announces-4-1m-seed-round-to-advance-ai-native-explainer-video-creation)
- **Sora 关闭分析** — 日烧 $1M 算力，3.3M 峰值下载 vs $2.1M 总收入——T2V 商业化的反面教材。行业媒体多方报道。
