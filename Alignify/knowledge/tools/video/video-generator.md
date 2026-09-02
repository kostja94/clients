# AI Video Generator / AI 视频生成 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI video generator / AI 视频生成器**——以文本、图像或视频为弱条件**一次性生成固定 clip**；验收以**单段画质、音频、角色一致与续写长度**为主。本页为 **离线 clip 生成层 SSOT**（Runway / Veo / Kling 等完整 URL 表仅此一处）；**生成中改 prompt / 无限流** → [interactive-video.md](interactive-video.md)；输入模态专论 → T2V / I2V / V2V 姊妹块；时间线编辑 → 见 §与相邻 slug 分流；与 **AI 视频编辑**、**AI 动画生成**、**AI 电影制作** 相邻但**不同采购与验收维度**。

**材料范围**：公开网络检索（厂商产品页、行业评测与横向对比、开发者社区讨论）；**未**将 Alignify 站内 Tools 正文 JSON 当作独立事实来源复述。**具体参数、定价与 API 条款以各官网为准**。网摘整理日期 **2026-06-24**。

**站内对照**：[alignify.co/tools/video-generator](https://alignify.co/tools/video-generator) · [alignify.co/zh/tools/video-generator](https://alignify.co/zh/tools/video-generator) · `/tools/video-generator` · `/zh/tools/video-generator` · `content/tools/zh/video-generator.md`、`content/tools/en/video-generator.md` · slug **`video-generator`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#video-generator-tools`](../../product/alignify-keywords-tools.md#video-generator-tools)

**站内相邻**：[video.md](video.md)（品类总览）· [interactive-video.md](interactive-video.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md) · [video-to-video.md](video-to-video.md) · [filmmaking.md](filmmaking.md) · [animation-generator.md](animation-generator.md)

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`video-generator`（本页）** | **`interactive-video`** | **`video-editor`** | **`animation-generator`** | **`filmmaking`** |
|------|------------------------------|-------------------------|--------------------|--------------------------|------------------|
| **典型买家问题** | 怎么用 AI 从文本/描述直接生成一段视频？ | 生成过程中能否改方向、连续播多久？ | 怎么用 AI 编辑已有视频片段？ | 怎么生成 AI 动漫/动画？ | 怎么用 AI 辅助电影制作全流程？ |
| **主交互** | 文本 prompt → 固定 clip | 持续流 + 中途 prompt/投票 | 已有视频素材 → 修剪/合成/特效 | 文本→动画风格视频 | 剧本→分镜→生成→后期 |
| **时长特征** | 3 秒–3 分钟 | 分钟–小时级（理论无限） | 不限 | 数秒–数分钟 | 任意 |
| **代表性产品** | 见 §外链索引 | Visko Orbis、fal.live、Odyssey-2 Pro | VEED、CapCut、Descript | AniJam、DomoAI | LTX Studio |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Text-to-video（T2V）**：输入为文本/文档的生成模态——**定义、讲解视频子类、数字人播报专表**见 [text-to-video.md](text-to-video.md)。
- **Image-to-video（I2V）**：输入为静态图的生成模态——**Motion Brush、废片率、电商品牌保真**见 [image-to-video.md](image-to-video.md)。
- **Video-to-video（V2V）**：以既有视频为输入的风格/内容变换——**时间一致性专论**见 [video-to-video.md](video-to-video.md)。
- **Native audio / 原生音频**：视频生成同时产出同步音频（对话、环境音、音效）——2026 年旗舰模型逐步内置；多数早期/轻量模型（Runway、Pika 等）仍静音，需后期配音。各产品音频能力见 §外链索引。
- **Character consistency / 角色一致性**：同一人物/角色跨多个生成片段保持外观一致——专业向与轻量 Face-lock 方案分化；横向对比见 §外链索引。
- **Extend / 续写**：在已有视频片段基础上生成后续内容——单链最长续航因产品而异，见 §外链索引 **Kling 3.0**。
- **Draft Mode / 快速探索**：低精度快速生成模式（如 Midjourney V7：10× 速度、半价 GPU），用于快速测试多个创意方向后再高精度渲染。
- **AGEI（Artificial General Editing Intelligence）**：Vidrush 提出的愿景——AI 自主编辑长视频达到人类专业剪辑师水平。代表了「视频生成→视频自动编辑」的能力延伸方向。
- **Gemini + Veo 双模型协作**：Google Sparkify 的核心架构——LLM 负责内容理解与叙事编排、视频模型负责帧生成；这种 LLM+视频模型协作范式在 2026 年正在成为标配。

---

## 专题对照 / 扩展定义

| 维度 | **长视频生成（Long-form）** | **短视频生成（Short-form）** |
|------|---------------------------|---------------------------|
| **典型时长** | 1 分钟–数分钟 | 3–60 秒 |
| **内容类型** | YouTube 解说、纪录片、品牌故事 | TikTok/Reels/Shorts、教育动画、广告 |
| **叙事复杂度** | 高——需脚本、章节、多场景 | 低——单概念、视觉冲击优先 |
| **代表性产品** | 见 §外链索引（Vidrush、Kling、Runway、Veo） | Sparkify、Pika、Luma、Hailuo |
| **AI 角色** | AI 写脚本+生成画面+配音+剪辑一体化 | AI 快速将点子→可分享的视觉短片 |

| 维度 | **通用视频生成模型** | **Agentic 全流程平台** |
|------|---------------------|----------------------|
| **核心能力** | 文本/图→视频片段 | 想法→研究→脚本→画面→配音→成品视频 |
| **控制粒度** | prompt + 技术参数 | 对话式编辑 + 智能替换 + 分析仪表盘 |
| **目标用户** | 专业创作者、VFX 艺术家 | 内容创作者、YouTuber、营销团队 |
| **代表性产品** | 见 §外链索引 | Vidrush |

---

## 问题域（为何会出现这类产品）

- **视频制作成本的 AI 替代**：传统视频制作需要编剧、摄像、演员、剪辑、配音等多角色——AI 视频生成将单条视频制作成本从 $500–$5,000+ 压缩到 $0.50–$5（API 调用费）。Vidrush 用户报告将 4 天团队工作流压缩到 30 分钟。
- **内容平台的供给饥渴**：YouTube 每分钟上传 500+ 小时视频，TikTok 日活 10 亿+——平台对视频内容的需求理论上无限。AI 视频生成将内容供给从「人类创作者的时间」中解放出来。
- **长视频 YouTuber 的 AI 化**：「Faceless YouTube」（不出镜解说频道）已经是成熟品类——Vidrush 将这一品类的生产进一步自动化：从选题研究到最终 4K 成品。
- **教育内容的视频化浪潮**：Google Sparkify（Gemini + Veo）代表了「知识→视频」的新范式——将复杂概念自动转化为儿童友好或学术风格的动画短片，降低教育内容的视频化门槛。
- **模型能力的快速跃升**：从 2024 年「能生成连贯 3 秒就不错」到 2026 年「60 秒 4K + 原生音频 + 文字渲染」——视频生成模型进步速度甚至快于同期图像生成；主力梯队与 Sora 关停转折见 §外链索引 · §行业注记。

---

## 能力栈（概念拆分，非厂商功能表）

- **视频生成引擎**：从 prompt/图像/视频生成新视频帧。技术路线包括扩散模型、DiT 架构（Sora 首创，已关停；后继者见 §外链索引）、混合架构。主要质量维度：时间连贯性、物理合理性、角色一致性、分辨率（720p–4K）。
- **原生音频生成**：同步产出配音+环境音+音效——无需后期配音；2026 年旗舰内置，轻量/静音模型仍占多数。各产品音频能力见 §外链索引。
- **角色与场景一致性**：跨多个生成片段的角色/场景锚定——专业向与轻量方案分化；横向对比见 §外链索引。
- **精确定向控制**：Motion Brush（指定画面区域运动）、Camera Control（pan/tilt/zoom/dolly）、Pose Control（指定模特姿态）——专业创作者依赖此类功能；代表产品见 §外链索引 **Runway Gen-4.5**。
- **视频续写与拼接**：在已有片段基础上向后延伸——单链最长续航因产品而异，见 §外链索引；续写质量随长度递减是所有模型的共同挑战。
- **全流程 Agent 编排**：从想法→研究→脚本→生成→配音→剪辑→成品的端到端自动化——Vidrush（YouTube 长视频）和 Sparkify（教育短视频）在各自领域实现了不同程度的 Agent 化。
- **速度与成本**：生成速度与 API 定价因产品差异大——从免费每日刷新到 Ultra 订阅不等；具体数值见 §外链索引。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **Premium T2V** | 最高画质 + 原生音频 + 角色一致 | Premium T2V model / flagship video generator | Veo 3.1、Runway Gen-4.5、Kling 3.0 |
| **Value T2V** | 性价比优先，中高画质 | Value T2V model | Kling 2.6、Luma Dream Machine |
| **Creative / effects** | 创意特效 + 风格化输出 | Creative T2V / effects video | Pika 2.5、Hailuo AI |
| **Long-form agent** | 全流程 Agent 自动化（研究→成品） | Long-form agent platform | Vidrush |
| **Educational** | LLM 叙事 + 视频模型双引擎 | Educational short video | Google Sparkify |
| **OSS / self-hosted** | 本地部署、可微调 | Open-source video generation | CogVideoX、AnimateDiff、Wav2Lip 社区变体 |

---

## 风险 · 合规 · 版权与深度伪造（外部框架可对照，非法律意见）

- **深度伪造与政治操纵**：AI 视频生成是深度伪造的最高风险品类——可生成虚假的政治人物发言、伪造新闻事件。Google Veo 3.1 内置 SynthID 水印，但水印可被裁剪或二次处理。
- **版权与训练数据争议**：视频生成模型的训练数据来源（是否包含受版权保护的影视作品、YouTube 视频）是持续的法律争议焦点。Runway 和已关停的 Sora 的训练数据来源被多次公开质疑。
- **儿童安全**：Google Sparkify 明确面向儿童教育市场——AI 生成的视频内容审核、不当内容过滤、隐私保护（COPPA 合规）需要更严格的机制。
- **内容生产者生态冲击**：AI 视频生成对自由职业摄像师、剪辑师、配音演员的生计构成直接威胁——Flawless AI 的 SAG-AFTRA 认可模式（演员授权+二次录音）提供了一种共存模板，但多数视频生成产品尚未建立类似的利益分配机制。
- **AI 生成内容的平台标识**：YouTube、TikTok、Meta 各自对 AI 生成视频的标注要求不同——创作者需要了解各平台的 AI 内容政策以避免限流或下架。

---

## 落地碎片（无先后）

- 先分清你在哪个赛道：**长视频 YouTube 内容**（Vidrush）vs **短视频/社媒**（Pika、Luma）vs **电影级制作**（Runway、Veo）——不同赛道的最佳工具完全不同；各产品定位见 §外链索引。
- 如果做 YouTube 长内容（尤其 faceless 频道）——Vidrush 是目前唯一将「研究→脚本→配音→画面→剪辑→成品」全流程 Agent 化的平台。用户数据：3 个频道约 5 个月可产生收入，4 天工作流压缩到 30 分钟。
- 如果做教育短视频——Google Sparkify（免费排队）将知识点→多种视觉风格（卡通/折纸/动漫/粘土/3D 卡通/写实）的 2 分钟内短片，适合儿童教育、科学普及、好奇心驱动的内容。
- 追求最高画质或精确控制——旗舰模型与 Motion Brush 能力见 §外链索引 **Veo 3.1**、**Runway Gen-4.5**。
- 预算有限或速度优先——性价比与快速生成选项见 §外链索引 **Kling 3.0**、**Hailuo AI**、**Luma Dream Machine**。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

> **分工规则**（详见 [video.md](video.md) §内容分工）：Runway / Veo / Kling / Pika / Luma / Hailuo **完整横评表仅在本节**；T2V 讲解视频 / 白板 / 数字人专表见 [text-to-video.md](text-to-video.md) §外链索引。

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Sora 2**（OpenAI） | — | ⚠️ 已关停——2026-03-24 宣布；Web/App 2026-04-26 下线；API 2026-09-24 下线。曾是电影级物理模拟+原生音频标杆，DiT 架构开创者 | [openai.com/sora](https://openai.com/sora) |
| **Google Veo 3.1** | Premium T2V | 原生音频 + 4K 输出 + SynthID 水印；prompt 遵循度与音视频综合评分领先（9.0/10）；$19.99–$249/月 | [deepmind.google/veo](https://deepmind.google/technologies/veo/) |
| **Runway Gen-4.5** | Premium T2V | 角色一致性行业最强，Motion Brush + Camera Control 专业级控制，$12/月起 | [runwayml.com](https://runwayml.com/) |
| **Kling 3.0** | Premium T2V | 多镜头叙事 + 原生音频 5 语言 + Elements 3.0 视频参考；Extend 可达 3 分钟，性价比领先 | [klingai.com](https://klingai.com/) |
| **Pika 2.5** | Creative | Pikaswaps/Pikaffects 创意特效，社交向快速迭代，$8/月 | [pika.art](https://pika.art/) |
| **Luma Dream Machine** | Value | Ray 3 HDR 输出，电影感运镜；120 帧/120 秒快速生成，$29.99/月无限计划 | [lumalabs.ai](https://lumalabs.ai/) |
| **Hailuo AI 2.3**（MiniMax） | Creative | 每日免费刷新积分，动画/角色风格优，$0.01–0.03/秒量级 | [hailuoai.com](https://hailuoai.com/) |
| **Vidrush** | Long-form agent | AI 长视频全流程 Agent 平台——研究→脚本→配音→Remotion 图形→成品，YouTube 优化，Free→$19/月 | [vidrush.ai](https://www.vidrush.ai/) |
| **Google Sparkify** | Educational | Gemini + Veo 双模型教育短视频生成，卡通/折纸/动漫/粘土多风格，<2 分钟，需排队 | [sparkify.withgoogle.com](https://sparkify.withgoogle.com/) |
| **AI Video Generator Market Report** | — | GII / Grand View Research 2026 市场规模与预测 | [giiresearch.com](https://www.giiresearch.com/report/grvi1942046-ai-video-generator-market-size-share-trends.html) |

### 对比与测评（第三方；观点非官方）

- **没有全能冠军**：2025–2026 年共识——各工具在画质、控制、速度、价格四维度上各有取舍；具体规格见 §外链索引。
- **Premium T2V 路线取舍**：原生音频与 prompt 遵循、精确运动控制、多镜头叙事与 Extend 续航往往不可同时极值——各维度领先者见 §外链索引，勿按单一 benchmark 选「冠军」。
- **宏观格局**：Sora 关停、旗舰三足鼎立、实时交互分支等**趋势 SSOT** 见 §行业注记；关停日期与产品规格见 §外链索引 **Sora 2** 行。

*本小节为网摘与媒体观点综合，非 Alignify 实测。*

---

## 行业注记 · 2026 年视频生成格局

- **Sora 关停成为品类转折**：OpenAI 于 2026-03-24 宣布关停 Sora 2（Web/App 2026-04-26 下线，API 2026-09-24 下线），标志着大厂直接从消费级视频生成退场——市场格局向 Veo、Runway、Kling 三足鼎立收敛。
- **原生音频成为新基线**：2026 年旗舰模型（Veo 3.1、Runway Gen-4.5、Kling 3.0 Omni）全部内置原生音频生成，替代了「先生成视频→再用 ElevenLabs 配音」的两段式管线。视频+音频的一体化生成使单人创作者工具栈进一步简化。
- **分辨率与时长跃进**：2026 年标准从「3-5 秒 720p」跃迁到「60 秒 4K + 文字渲染」——Runway Gen-4.5 和 Veo 3.1 均支持 4K 原生输出，文字渲染质量大幅追赶图像生成器。
- **推理成本 10× 下降**：API 价格从 2025 年的 ~$2.50/5s 降至 2026 年的 ~$0.18-0.30/5s 片段量级——单位内容成本下降使得「AI 视频作为 YouTube 内容农场的燃料」经济账初步跑通。
- **短剧与竖屏经济驱动需求**：TikTok/Reels/Shorts 的竖屏内容发布量指数增长——短剧平台（ReelShort、DramaBox）和 AI 短剧生成工具（SkyReels、Kling 短剧模式）将视频生成从「创意工具」推向「内容工厂」。
- **实时交互分支（2026-09）**：**Visko Orbis**（Live Model）、**fal H3 Max Live / fal.live**（RTF>1 无限 TV）等将品类从「等一条 clip」推向「持续流 + 中途 steering」——与离线 generator **不同 slug、不同验收**；完整 SSOT 见 [interactive-video.md](interactive-video.md)。

---

## 延伸阅读 · 站内外

**站外**

- **行业事件**：2025 年 5 月 Google I/O 发布 Veo + Sparkify、2026 年 3 月 Runway Characters 实时 Agent 发布。
- **Alignify Tools 正文**：产品清单与选型步骤以线上 `/zh/tools/video-generator` 为准；本知识块**不**替代站内长文教程，仅作概念索引与外链锚点。

**站内**

- 上游/并列：[video.md](video.md) · [interactive-video.md](interactive-video.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md) · [video-to-video.md](video-to-video.md)
- 下游：[video-editor.md](video-editor.md) · [canvas-video.md](canvas-video.md)（多模型编排）
- 垂直：[filmmaking.md](filmmaking.md) · [animation-generator.md](animation-generator.md) · [short-drama.md](short-drama.md)
- 上游视觉：[image-generator.md](../image/image-generator.md)