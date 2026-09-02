# AI Text-to-Speech（TTS / 文本转语音）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Text-to-Speech / TTS / 文本转语音**——将**书面文本**合成为可播放语音；验收以**自然度（MOS）、流式延迟（FPL/RTF）、多语种与韵律控制**为主。本页为 **TTS 产品 SSOT**（完整 URL 表仅此一处）；零样本/品牌声线 → [voice-cloning.md](voice-cloning.md)；实时变声 → [voice-changer.md](voice-changer.md)；翻译配音 → [audio-translator.md](audio-translator.md)；语音 Agent 全栈 → [voice.md](voice.md)。

**材料范围**：公开网络检索（厂商博客、OpenAI/ElevenLabs 官方发布、开源社区、行业对比文与合规报道）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。**具体参数、定价与 API 条款以各官网为准**。网摘整理日期 **2026-06-24**（架构分界与原生音频模型注记）。

**站内对照**：[alignify.co/tools/text-to-speech](https://alignify.co/tools/text-to-speech) · `/tools/text-to-speech` · [alignify.co/zh/tools/text-to-speech](https://alignify.co/zh/tools/text-to-speech) · `/zh/tools/text-to-speech` · `content/tools/zh/text-to-speech.md`、`content/tools/en/text-to-speech.md` · slug **`text-to-speech`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#text-to-speech-tools`](../../product/alignify-keywords-tools.md#text-to-speech-tools)

**站内相邻**：[voice.md](voice.md)（Hub）· [speech-to-text.md](speech-to-text.md) · [voice-cloning.md](voice-cloning.md) · [voice-changer.md](voice-changer.md) · [audio-translator.md](audio-translator.md) · [lip-sync.md](lip-sync.md)

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`text-to-speech`（本页）** | **`voice-cloning`** | **`voice-changer`** | **`audio-translator`** |
|------|----------------------------|---------------------|----------------------|-------------------------|
| **典型买家问题** | 「怎么把文章/剧本/教程变成自然朗读的语音？」 | 「怎么让 AI 用我的声音说话，说我没录过的内容？」 | 「怎么在直播/录音时实时把我的声音变成别人的？」 | 「怎么把英文播客自动转成中文语音？」 |
| **输入** | 纯文本 | 参考音频样本 + 目标文本 | 你的实时/录制语音 | 源语言音频 |
| **输出** | 合成语音（通用或预置音色） | 以特定真人音色朗读的新语音 | 换了一个音色的同内容语音 | 目标语言语音（翻译+合成） |
| **验收核心** | 自然度（MOS）、多语种覆盖、流式延迟、SSML 支持 | 音色相似度、少样本克隆质量（3-60s）、跨语言克隆保真度 | 实时性（<200ms）、音色转换自然度、不丢情绪/语气 | 翻译准确度、音色保留度、唇形同步（视频场景） |
| **数据敏感度** | 中：文本可能涉商业机密，但主流 API 通常不用于模型训练 | **极高**：生物识别数据（声纹），多国需显式同意 | 中高：实时语音可能含私密对话 | 中高：会议/采访内容可能涉密 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI Text-to-Speech（TTS / 文本转语音）**：将书面文本通过 AI 模型合成为可播放的语音音频。与传统拼接式 TTS（unit selection）不同，现代 AI TTS 使用神经网络端到端生成，支持韵律预测、情感注入与零样本音色克隆。部署形态见 §形态谱系。
- **MOS（Mean Opinion Score）**：语音自然度的主观评测指标，1-5 分，4.0 以上视为「接近真人」。当前顶级商业与开源模型在单说话人场景已可达 4.2-4.6，部分论文声称超越真人录音；各产品数值见 §外链索引。
- **RTF（Real-Time Factor）**：推理速度指标。RTF < 1 即为实时——生成 1 秒音频耗时小于 1 秒。流式 TTS 的关键目标是将首包延迟（First-Packet Latency, FPL）压至 200ms 以下以支撑实时语音对话。
- **Voice Cloning（语音克隆）**：从少量参考音频（3-60 秒）提取说话人声纹特征，再用 TTS 为该声纹生成任意文本——属于 TTS 的高级能力；独立选型见 [voice-cloning.md](voice-cloning.md)。**零样本克隆（zero-shot）** 指无需针对目标说话人微调模型即可克隆。
- **SSML（Speech Synthesis Markup Language）**：XML 标准的语音合成标记语言，允许对语速、音高、停顿、重音、发音进行细粒度控制。多用于长内容（有声书）和品牌语音一致性场景，2025 年正被 AI 驱动韵律预测部分替代。
- **流式 TTS（Streaming TTS）**：与「先完整生成再播放」的批式 TTS 相对，流式 TTS 在收到部分文本后即可开始输出音频。细分为（a）输出流式——文本完整后流式播放音频块，（b）双流式——LLM 逐 token 输出文本的同时 TTS 逐块生成音频，是实时语音 Agent 的架构基础。
- **多语种 TTS vs 跨语言克隆**：前者指引擎内置多语种音色库，后者指用单一说话人的克隆声纹朗读非母语文本——后者是溢价能力最强的维度；代表产品见 §外链索引。
- **Conversational Speech Model（CSM / 对话语音模型）**：Sesame AI 提出的单阶段多模态 Transformer 架构，将文本与音频 token 交织处理（而非传统 TTS 的「文本→语音」两阶段流水线），生成的语音带有对话上下文感知——能根据多轮对话历史调整韵律、情绪和节奏。代表模型 CSM-1B 以 Apache 2.0 开源，2025 年 2 月首发时被 ZDNET、Ars Technica 等媒体评价为「令人不安地逼近真人」。
- **Full-Duplex TTS（全双工 TTS）**：与传统的半双工（一问一答、轮流发言）相对，全双工 TTS 支持双方同时说话、打断（barge-in）和 backchanneling（「嗯」「我明白了」等反馈声）。Kyutai 的 Moshi（2024 夏）是全球首个全双工实时对话 AI 模型，以 160ms 延迟超越人类对话反应时间。Gradium（Kyutai 的商业化分拆）将此架构产品化。
- **Speech-to-Speech（S2S / 语音到语音）**：输入为音频而非文本。**本 slug 不覆盖 S2S**——实时变声见 [voice-changer.md](voice-changer.md)，跨语言口译见 [audio-translator.md](audio-translator.md)。2026 年 **GPT-Realtime-2** 等原生音频 Agent 虽跳过文本层，但在 Agent 场景仍常与独立 TTS API 并存（IVR 播报、有声书等纯文本输入场景）。

---

## 专题对照 / 扩展定义

**云端 API vs 开源本地部署**（采购逻辑截然不同）：

| 对比维度 | **云端 API TTS** | **开源本地 TTS** |
|----------|-----------------|------------------|
| 音质天花板 | 最高（商业 API 流式低延迟） | 快速追赶（开源 MOS 已逼近/超越真人论文声称） |
| 部署成本 | 按字符/小时计费，规模越大边际成本越高 | 一次性 GPU 投入或消费级 GPU 推理 |
| 隐私与合规 | 文本/音频离开本地，需审计 API 条款与训练数据政策 | 全部数据留存在本地，适合受监管行业 |
| 迭代速度 | 厂商持续优化，无需自行维护 | 需跟进社区更新，模型停更风险（如 Coqui/XTTS） |
| 商用许可 | 通常明确（付费即可商用） | 混乱——XTTS 非商用、F5-TTS 权重 CC-BY-NC、Kokoro MIT |
| 典型选型触发词 | 「开箱即用」「不想管 infra」「需要超低延迟流式」 | 「数据不能出内网」「长期大规模调用要控成本」「需要定制微调」 |

**单语种优化 vs 多语种覆盖**：WellSaid Labs 英语质量极高但只用英语；PlayHT（⚠️ 已关闭）曾以 142 语言覆盖制胜但单个语种质量不如专业选手——具体覆盖见 §外链索引。

**半双工 TTS vs 全双工对话模型**（范式定义见 §词汇锚点；下表只列买家体验差）：

| 对比维度 | **半双工 TTS（传统）** | **全双工对话模型** |
|----------|----------------------|---------------------|
| 交互模式 | 轮流发言，一方说完另一方才能开始 | 双方可同时说话，支持打断与 backchanneling |
| 架构 | 文本→语音两阶段流水线 | 音频+文本联合建模，单阶段生成 |
| 延迟目标 | 首包 < 200ms（流式 TTS） | 端到端 < 200ms（含理解和生成） |
| 上下文感知 | 仅当前句子级 SSML/韵律控制 | 多轮对话历史驱动情绪和节奏 |
| 典型场景 | 有声书、配音、IVR 播报 | 语音 Agent、客服、AI 陪伴、车载助手 |

**2026 架构分界：TTS 仍何时需要？**

| 场景 | 推荐路径 | 原因 |
|------|---------|------|
| 有声书、旁白、IVR 播报 | **传统/流式 TTS API** | 输入本就是文本，无需 S2S |
| 实时客服 Agent（高推理） | **GPT-Realtime-2** 或 **ElevenAgents + v3 Conversational** | 原生音频+turn-taking，韵律更自然 |
| 模块可替换、成本敏感 | **Cartesia/Deepgram STT + LLM + TTS** 管线 | 按模块优化单价；STT 见 [speech-to-text.md](speech-to-text.md) |
| 克隆特定品牌声线 | **TTS + voice cloning 层** | 见 [voice-cloning.md](voice-cloning.md) |

架构路线（Cloud API / Studio / 开源 / 端侧 / Agent / CSM）→ **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **无障碍刚需与合规驱动**：全球 13 亿+ 视障人群、阅读障碍者与老龄化人口的「听取内容」需求是 TTS 最深厚的社会价值根基。WCAG 合规正成为欧美网站的硬性要求，推动「听这篇文章」按钮成为内容页标配。
- **有声内容规模化生产的成本痛点**：传统有声书录制需真人配音演员 + 录音棚 + 后期，单本成本数千至数万美元。AI TTS 将电子书库存转为有声书的成本降低约 70%，使长尾内容（小众教材、企业内部文档、地方志）首次具备有声化的经济可行性。
- **多语言本地化从「翻译」到「语音」的延伸**：全球化品牌不仅需要多语言字幕，还需要以当地语言的原生口吻讲述产品故事——单一英语视频面对非英语市场时，观众潜意识判断「这个产品不是为我做的」。
- **实时语音交互的技术前提**：LLM 语音 Agent、车载助手、实时翻译耳机等场景要求 TTS 延迟 < 200ms 且能处理中断/重规划——这反向驱动了流式 TTS 架构的快速演进。
- **内容创作者的去录音棚化**：YouTuber、播客主、在线课程讲师不再需要专业录音设备和安静环境——AI TTS 配合情感标签（友好/专业/兴奋/安抚）即可达到可发布的音质。
- **开源模型的「平权效应」**：F5-TTS、CosyVoice 等国产开源模型在中文语音克隆上已逼近商业产品，使中小团队和独立开发者首次拥有「可自部署的高质量 TTS」。
- **「恐怖谷」的跨越与不安**：Sesame CSM 的 Maya/Miles 语音 demo 在 2025 年 2 月引发全球热议——ZDNET 称「令人惊叹又令人毛骨悚然」，Ars Technica 报道有用户「挂了电话 15 分钟后仍心有余悸」。当合成语音逼近真人但未完全到达时，触发的「恐怖谷」效应本身正成为产品化的关键障碍。Sesame 联创 Brendan Iribe 公开承认「我们目前确实在谷底，但乐观地认为能爬出去」。
- **音频 AI 的「小团队胜出」现象**：Amplify Partners 2026 年 2 月的分析指出，音频是「唯一一个由小型实验室而非大厂主导的生成式 AI 领域」。Kyutai 的 Moshi 由核心 4 人团队在 6 个月内构建，在 OpenAI Advanced Voice Mode 发布之前即实现了全双工。Gradium 以 7000 万美元种子轮从 Kyutai 分拆，Sesame 以 1B 参数模型引发全球关注——音频模型的训练成本远低于文本 LLM（Moshi 7B 仅用 2.1T tokens），使小团队得以与 Google、Meta 竞争。

---

## 能力栈（概念拆分，非厂商功能表）

- **基础合成**：文本解析（分词、归一化、多音字消歧）→ 声学模型（文本→梅尔谱或声码器参数）→ 声码器（谱→波形）。现代方案多为端到端，跳过显式中间表示。2026 年出现的新范式（Dual-Track 架构）以离散多码本语言模型取代传统的「LM + Diffusion」级联，实现首字即出音频的流式生成——代表见 §外链索引 **Qwen3-TTS**。
- **音色多样性**：预置音色库规模（从几十到 900+）、音色分类（年龄、性别、风格、口音）。多说话人模型可在同一引擎内切换不同声线。
- **零样本克隆**：从 2-60 秒参考音频提取声纹，无需微调即可为该声纹生成任意文本。质量取决于参考音频的干净程度与时长；深度选型见 [voice-cloning.md](voice-cloning.md)。
- **情感与韵律控制**：AI 驱动的情感自动检测（根据文本语境判读应使用「兴奋」「同情」「专业」等语调）vs 手动 SSML 标签控制——前者省力但可控性差，后者精细但学习成本高。
- **流式与延迟**：批式 → 输出流式 → 双流式（LLM token + TTS 并行）。2025 年实时 Agent 场景的硬指标是 FPL < 200ms；各产品延迟见 §外链索引。
- **多语种覆盖**：从英语单语到 142 语言（PlayHT，⚠️ 已关闭）到「中英双语深度优化」到极端多语言开源（646 语言 OmniVoice）。跨语言克隆是溢价能力最强的维度。
- **长文本鲁棒性**：有声书/教材场景需要处理数万字连续文本而不出现音质漂移、漏句、「核嗓」音调异常。部分模型在 5000+ 字长文后表现退化。
- **非语言音效**：笑声、叹息、哭泣、音乐、背景音——Bark 是目前唯一原生支持的开源模型；商业产品（ElevenLabs）可通过 prompt 引导部分非语言表达。
- **端侧与离线部署**：从云端 GB 级模型到端侧 100MB 以下的轻量化引擎（Kokoro-82M、Piper、Sherpa-onnx、KittenTTS），适合嵌入式设备、车载、工业场景。
- **音频水印与溯源**：音频水印（频域不可感知嵌入）、C2PA 内容凭证——正在成为合规基础设施而非可选功能。
- **全双工与对话上下文**：传统 TTS 是「一次性生成」——每次调用独立，不记忆上一句说了什么。全双工对话模型（Moshi、CSM）将对话建模为两个并行的音频流，支持实时打断、语气承接和 backchanneling。这一能力正在从学术原型（Moshi 2024）走向商业产品（Gradium 2025）和开源生态（CSM-1B Apache 2.0）。
- **极致轻量化**：2026 年出现了一批 < 100MB 的高质量端侧 TTS 引擎。KittenTTS 最小仅 14M 参数 / 25MB（Nano），纯 CPU 运行，Apache 2.0 开源——目标是将可接受的 TTS 质量带到 IoT、浏览器和功能手机上。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 按字符/小时计费的 HTTP/gRPC API，开发者集成最快 | Cloud TTS API / REST TTS | ElevenLabs、Google Cloud TTS、Amazon Polly、Azure Speech、OpenAI TTS |
| **B** | GUI 脚本编辑、音色选择、背景音乐、视频同步一体化 | AI Voice Studio / All-in-One | Murf.ai |
| **C** | 可自部署预训练权重，需评估许可与社区活跃度 | Open-Source TTS Model | F5-TTS、CosyVoice、StyleTTS 2、Bark、Qwen3-TTS、OmniVoice |
| **D** | SOC 2、SSO、品牌声线客制化、真人演员授权 | Enterprise Brand Voice | WellSaid Labs |
| **E** | 离线推理、<100MB 模型、数据不出设备 | On-Device / Edge TTS | Kokoro、Piper、Sherpa-onnx、KittenTTS |
| **F** | 双流式架构、<200ms FPL、可中断、并发优化 | Real-Time Conversational TTS | Cartesia Sonic、ElevenLabs Conversational AI、Deepgram Aura |
| **G** | 单阶段多模态 Transformer、全双工、多轮上下文感知 | Conversational Speech Model / CSM | Sesame CSM-1B、Gradium（Moshi 架构） |

**Type F vs G**（均服务 Agent，架构不同）：F 为传统 TTS 的低延迟优化层；G 为音频+文本联合建模的单阶段对话语音模型——评估维度见 §专题对照「半双工 vs 全双工」，不可直接对比 MOS。

**Adjacent（常一起出现但不等于 TTS 本体）**：voice cloning（声纹复制）、voice changer（实时变声）、audio translator（翻译配音）、AI music vocal（歌声合成）——各自单算。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **语音克隆作为生物识别风险**：声纹属于生物识别数据，受 GDPR（显式同意）、IL BIPA（书面同意）、TN ELVIS Act（声音财产权）等多法域保护。美国参议员 Hassan 2026 年 4 月致函主要语音克隆厂商施压反欺诈措施。中国已有法院判例认定 AI 生成语音承载人格权。
- **深度伪造与诈骗**：FBI 报告 2025 年仅 AI 相关诈骗损失即达 8.93 亿美元。AI 语音冒充银行职员、亲属的诈骗案例全球频发，单案涉案金额从数十万到数百万美元不等。
- **全球监管碎片化**：EU AI Act Art.50 要求 AI 生成音频必须披露（2026.8 生效）；中国深度合成规定要求显著标识；印度 2026 IT 规则要求嵌入不可篡改的合成内容元数据，政府指令下架时限 2-3 小时；美国 TAKE IT DOWN Act 要求平台移除未经同意的深度伪造私密内容。
- **音频水印与溯源成为合规基础设施**：C2PA v2.2 内容凭证成为行业标准；频域不可感知水印在 3 次转码后仍有 85% 可提取率。采购决策中应优先选择已内置水印或 C2PA 签名的厂商。
- **训练数据版权**：语音演员正起诉 ElevenLabs、Lovo 等平台未经授权使用声音训练克隆模型——TTS 厂商的训练数据来源合规性是 2025-2026 年的活跃法律风险带。
- **开源许可陷阱**：XTTS 非商用、F5-TTS 权重 CC-BY-NC、Bark MIT 但权重受限制——开源 ≠ 免费用。商用部署前需逐项核验代码许可与权重许可的分离。
- **过度拟人化引发的社会心理风险**：Sesame CSM 的 Maya/Miles demo 引发了超出技术圈的广泛讨论——用户报告「4 岁孩子因不被允许再和 AI 说话而哭泣」（Ars Technica）、「挂了电话 15 分钟后仍心有余悸」（PCWorld）。当合成语音跨越恐怖谷后，可能引发情感依赖、身份混淆和「AI 拟人化欺诈」——用户误以为在与真人互动。目前尚无法规针对「过度拟人的合成语音」设定边界。
- **全双工模型的持续监听隐私风险**：全双工架构要求模型持续接收音频流以支持打断和 backchanneling——这意味着设备在对话期间实质上处于「始终监听」状态。与按键式语音助手（需手动触发）不同，全双工 Agent 的隐私边界和用户控制机制仍在早期探索阶段。

---

## 落地碎片（无先后）

- 先明确场景对延迟的要求：有声书/播客用批式即可，实时 Agent 必须 < 200ms FPL，车载/嵌入式优先考虑端侧引擎。
- 选 API 厂商时，除了 MOS 分数，重点关注其定价模型的规模曲线——按字符计费对长篇有声书可能远贵于按小时或固定席位。
- 开源模型选型先查许可证矩阵：代码许可（MIT/Apache）≠ 权重许可（CC-BY-NC/自定义），两者分离是开源 TTS 特有的坑。
- 语音克隆场景先确认目标法域是否需要声纹显式同意——从 GDPR 的「生物识别数据」到 TN ELVIS Act 的「声音财产权」，合规前置比事后补救成本低一个数量级。
- 品牌语音一致性需求 → 优先选企业合规型（WellSaid）或自训练定制模型，避免依赖通用 API 中可能随时下线或变更的预置音色。
- 中文场景优先测 F5-TTS 或 CosyVoice（开源），商业端优先测火山引擎/阿里云/腾讯云的 TTS API——国产引擎在中文多音字消歧、数字读法、标点韵律上通常优于国际厂商。
- 对话/Agent 场景不再仅评估 TTS 延迟——优先确认是否需要全双工（打断+backchanneling），若需要则重点评估 Sesame CSM 或 Gradium，而非在传统半双工 TTS 中勉强适配。
- 极端多语言场景（> 50 语言）优先评估 OmniVoice——646 语言覆盖 + 40 倍实时推理 + Apache 2.0，是当前覆盖最广的开源方案。
- 边缘设备/浏览器端 TTS 优先测 KittenTTS（25MB 纯 CPU）或 Qwen3-TTS-0.6B（3.5GB 显存）——两者均为 Apache 2.0，无需云端调用。
- 选型时注意区分「TTS」与「全双工对话模型」的评估维度差异——前者看 MOS/RTF/语种数，后者看打断流畅性、上下文连贯性和情感一致性，两者不可直接对比 MOS 分数。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **ElevenLabs** | A/F | 音质天花板、零样本克隆、流式 API；Conversational AI + Expressive Mode | [elevenlabs.io](https://elevenlabs.io/) · [Expressive Mode](https://elevenlabs.io/blog/introducing-expressive-mode) |
| **PlayHT** ⚠️ | A | 142 语言 + 跨语言克隆 + 博客转音频（已于 2025.12 关闭） | ~~play.ht~~ 已迁移至 play.ai |
| **Google Cloud TTS / Amazon Polly / Azure Speech** | A | 云平台通用 TTS API，生态绑定、统一计费 | [Google](https://cloud.google.com/text-to-speech) · [Polly](https://aws.amazon.com/polly/) · [Azure](https://azure.microsoft.com/products/ai-services/text-to-speech) |
| **OpenAI TTS** | A | API 集成 TTS，常与 Realtime 管线并存 | [openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) |
| **Murf** | B | 全能配音工作室、非技术用户友好 | [murf.ai](https://murf.ai/) |
| **WellSaid Labs** | D | 企业合规品牌声线、英语单语精品 | [wellsaidlabs.com](https://wellsaidlabs.com/) |
| **Cartesia Sonic** | F | 实时语音 Agent 低延迟引擎（<100ms FPL） | [cartesia.ai](https://cartesia.ai/) |
| **Deepgram Aura** | F | 语音 Agent 管线 TTS 层 | [deepgram.com](https://deepgram.com/) |
| **Resemble AI** | A（克隆层） | 语音克隆精度 + 多人对话合成 | [resemble.ai](https://www.resemble.ai/) |
| **F5-TTS** | C | 2025 开源综合最强，中英零样本克隆；2s 克隆、RTF 0.15 | [GitHub](https://github.com/SWivid/F5-TTS) · [arXiv](https://arxiv.org/abs/2410.06885) |
| **CosyVoice** | C | 阿里系开源，中文社区活跃 | [GitHub](https://github.com/FunAudioLLM/CosyVoice) |
| **StyleTTS 2** | C | 学术质量标杆，首个 MOS 超越真人的 TTS 论文 | [arXiv](https://arxiv.org/abs/2306.07691) |
| **Bark（Suno）** | C | 唯一原生支持非语言音效（笑声/音乐/叹息）的开源模型 | — |
| **Qwen3-TTS（Alibaba）** | C/E | 97ms 延迟，Dual-Track 架构，Apache 2.0；0.6B 版 3.5GB 显存 | [HuggingFace](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| **OmniVoice（Xiaomi）** | C | 646 语言开源，40x 实时，Apache 2.0 | [GitHub](https://github.com/k2-fsa) |
| **KittenTTS** | E | 14M 参数 / 25MB，纯 CPU，Apache 2.0 | — |
| **Kokoro / Piper / Sherpa-onnx** | E | 端侧/嵌入式轻量化引擎 | — |
| **Sesame CSM-1B** | G | 对话语音模型，Apache 2.0；8.3B 完整版盲测与真人无明显偏好差异 | [sesame.com](https://www.sesame.com/) · [研究文](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice) |
| **Gradium** | G | Kyutai Moshi 架构商业化；160ms 全双工、10s 克隆、5 语言；$70M 种子轮 | [gradium.ai](https://gradium.ai/) |

### 横向盘点与基准（第三方索引；非产品 SSOT）

| 名称 | 一句话 | URL |
|------|--------|-----|
| Text-to-Speech APIs in 2026 | 2026 年主流 TTS API 横向评测（音质、定价、延迟） | [voicecontrol.chat](https://voicecontrol.chat/blog/posts/text-to-speech-apis-in-2026-voices-pricing-and-what-natural-really-means) |
| Top Alternatives to ElevenLabs in 2026 | 按场景推荐的 ElevenLabs 替代方案 | [smallest.ai](https://smallest.ai/blog/top-alternatives-to-elevenlabs-in-2026) |
| Best Open Source TTS Models | 开源 TTS 模型跑分与部署指南 | [northflank.com](https://northflank.com/blog/best-open-source-text-to-speech-models-and-how-to-run-them) |
| 2025 TTS Evaluation (Chinese) | 2025 年三大开源 TTS 模型中文测评（声网） | [shengwang.cn](https://www.shengwang.cn/blog/blogdetail/2025-TTS-evaluation/) |
| Coval TTS Benchmarks | TTS 延迟与并发压测基准 | [coval.dev](https://www.coval.dev/blog/new-insights-expanding-our-voice-ai-stack-benchmarks-beyond-tts) |
| Complete Guide to TTS Technology 2025 | TTS 技术架构全览（Picovoice） | [picovoice.ai](https://picovoice.ai/blog/complete-guide-to-text-to-speech/) |

### 对比与测评（第三方；观点非官方）

- **音质自然度**：ElevenLabs 仍领先但差距在缩小；F5-TTS 和 CosyVoice 在中文场景已逼近商业产品。
- **延迟与并发**：Cartesia 在实时 Agent 场景异军突起；Qwen3-TTS 以 97ms 重新定义开源流式 TTS 速度上限。
- **定价模型复杂度**：按字符 vs 按小时 vs 按月席位，需按实际用量建模——长篇有声书按字符可能远贵于按小时。
- **教育向 vs 企业向**：Murf 常以「上手最无痛」胜出；ElevenLabs 以「情感表达最丰富」用于故事叙述；PlayHT（⚠️ 已关闭）曾以「博客一键转音频」成为内容营销团队首选；WellSaid 以合规与品牌一致性胜出但被「英语单语」限制反复提及；Google Cloud / Amazon Polly 多作为「不缺钱但也不冒险」的安全牌。
- **开源叙事（2025-2026）**：F5-TTS 被社区广泛认为是 XTTS 继承者（Coqui 停业且非商用）；Bark 表现力独一无二但不可控、推理慢，偏创意实验；OmniVoice + KittenTTS 覆盖商业产品尚未触及的极端场景（646 语言、25MB 端侧）。
- **全双工商业化**：Sesame CSM「恐怖谷」demo 引发全球媒体关注（ZDNET、Ars Technica、PCWorld）；Gradium 7000 万美元种子轮标志对话语音从「轮流发言」向「自然打断」范式转移。
- **不存在单一 winner**：按 §形态谱系 Type 切片选型——半双工 TTS 与全双工 CSM 评估维度不可直接对比 MOS。

*本小节为网摘与社区评测观点综合，非 Alignify 实测；**不**以各厂商自有营销博文为论证主体。*

---

## 延伸阅读 · 站内外

**站外**

- **ElevenLabs · 多语言 TTS**：[Multilingual TTS: Reaching a Global Audience](https://elevenlabs.io/blog/multilingual-text-to-speech-reaching-a-global-audience-with-ai-voices)
- **语音克隆全球立法综述**：[Deepfakes, Voice Cloning, and AI Impersonation: The Global Rules (Harris Sliwoski)](https://harris-sliwoski.com/zh/blog/deepfakes-voice-cloning-and-ai-impersonation-the-global-rules-are-already-here-and-they-dont-agree/)
- **Sen · Hassan 致函语音克隆厂商**：[Senator Hassan Presses Leading AI Voice Cloning Companies (2026.4)](https://www.jec.senate.gov/public/index.cfm/democrats/2026/4/senator-hassan-presses-leading-ai-voice-cloning-companies-to-prevent-exploitation-by-scammers)
- **V.O.I.C.E · 风险分类学论文**：[Risk Taxonomy of Synthetic Voice Generation (arXiv, 2026.4)](https://arxiv.org/abs/2604.24794)
- **Amplify Partners · 音频 AI 的小团队胜出**：[Arming the Rebels with GPUs: Gradium, Kyutai, and Audio AI (2026.2)](https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai)
- **Gradium 发布报道**：[Voice AI Startup Gradium Comes Out of Stealth With $70M Seed Round (Slator, 2025.12)](https://slator.com/voice-ai-startup-gradium-70m-seed-round/)
- **Qwen3-TTS 开源发布**：[Alibaba Open-Sources Qwen3-TTS: 97ms Latency, 3s Voice Cloning (2026.1)](https://pandaily.com/alibaba-open-sources-qwen3-tts-model-suite-delivering-multilingual-ultra-low-latency-speech-generation/)
- **OmniVoice 开源发布**：[Xiaomi Open Sources OmniVoice: 646-Language Speech Synthesis (2026.5)](https://en.theblockbeats.news/flash/344770)
- **Sesame CSM 媒体评测**：[Talking with Sesame's AI Voice Companion is Amazing and Creepy (ZDNET, 2025.3)](https://www.zdnet.com/article/talking-with-sesames-ai-voice-companion-is-amazing-and-creepy-see-for-yourself/)

**站内**

- Hub：[voice.md](voice.md)
- 反向管线 SSOT：[speech-to-text.md](speech-to-text.md)
- 克隆/变声/翻译：[voice-cloning.md](voice-cloning.md) · [voice-changer.md](voice-changer.md) · [audio-translator.md](audio-translator.md)