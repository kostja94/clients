# AI Text-to-Speech · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商博客、OpenAI/ElevenLabs 官方发布、开源社区、行业对比文与合规报道）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-24**（架构分界与原生音频模型注记）。

**品类总览**：[voice.md](voice.md) · 本页仅覆盖 **文本→语音（TTS）**；克隆/变声/Agent 全栈见各辐条。

**站内对照**：[alignify.co/tools/text-to-speech](https://alignify.co/tools/text-to-speech) · `/tools/text-to-speech` · [alignify.co/zh/tools/text-to-speech](https://alignify.co/zh/tools/text-to-speech) · `/zh/tools/text-to-speech` · `content/tools/zh/text-to-speech.md`、`content/tools/en/text-to-speech.md` · slug **`text-to-speech`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#text-to-speech-tools`](../../product/alignify-keywords-tools.md#text-to-speech-tools)

---

## 与相邻 slug 分流

本页讨论 **AI Text-to-Speech（TTS / 文本转语音）**：将书面文本合成为可播放的语音音频。以下品类常与 TTS 检索词重叠但产品本质不同：

| 维度 | **`text-to-speech`（本页）** | **`voice-cloning`** | **`voice-changer`** | **`audio-translator`** |
|------|----------------------------|---------------------|----------------------|-------------------------|
| 典型买家问题 | 「怎么把文章/剧本/教程变成自然朗读的语音？」 | 「怎么让 AI 用我的声音说话，说我没录过的内容？」 | 「怎么在直播/录音时实时把我的声音变成别人的？」 | 「怎么把英文播客自动转成中文语音？」 |
| 输入 | 纯文本 | 参考音频样本 + 目标文本 | 你的实时/录制语音 | 源语言音频 |
| 输出 | 合成语音（通用或预置音色） | 以特定真人音色朗读的新语音 | 换了一个音色的同内容语音 | 目标语言语音（翻译+合成） |
| 验收核心 | 自然度（MOS）、多语种覆盖、流式延迟、SSML 支持 | 音色相似度、少样本克隆质量（3-60s）、跨语言克隆保真度 | 实时性（<200ms）、音色转换自然度、不丢情绪/语气 | 翻译准确度、音色保留度、唇形同步（视频场景） |
| 数据敏感度 | 中：文本可能涉商业机密，但主流 API 通常不用于模型训练 | **极高**：生物识别数据（声纹），多国需显式同意 | 中高：实时语音可能含私密对话 | 中高：会议/采访内容可能涉密 |

---

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI Text-to-Speech（TTS / 文本转语音）**：将书面文本通过 AI 模型合成为可播放的语音音频。与传统拼接式 TTS（unit selection）不同，现代 AI TTS 使用神经网络端到端生成，支持韵律预测、情感注入与零样本音色克隆。本文件讨论的 TTS 涵括云端 API、开源模型与端侧引擎三类部署形态。
- **MOS（Mean Opinion Score）**：语音自然度的主观评测指标，1-5 分，4.0 以上视为「接近真人」。当前顶级商业 TTS（ElevenLabs）和开源模型（StyleTTS 2、F5-TTS）在单说话人场景已可达 4.2-4.6，部分论文声称超越真人录音。
- **RTF（Real-Time Factor）**：推理速度指标。RTF < 1 即为实时——生成 1 秒音频耗时小于 1 秒。流式 TTS 的关键目标是将首包延迟（First-Packet Latency, FPL）压至 200ms 以下以支撑实时语音对话。
- **Voice Cloning（语音克隆）**：从少量参考音频（3-60 秒）提取说话人声纹特征，再用 TTS 为该声纹生成任意文本——属于 TTS 的一项高级能力而非独立品类。**零样本克隆（zero-shot）** 指无需针对目标说话人微调模型即可克隆。
- **SSML（Speech Synthesis Markup Language）**：XML 标准的语音合成标记语言，允许对语速、音高、停顿、重音、发音进行细粒度控制。多用于长内容（有声书）和品牌语音一致性场景，2025 年正被 AI 驱动韵律预测部分替代。
- **流式 TTS（Streaming TTS）**：与「先完整生成再播放」的批式 TTS 相对，流式 TTS 在收到部分文本后即可开始输出音频。细分为（a）输出流式——文本完整后流式播放音频块，（b）双流式——LLM 逐 token 输出文本的同时 TTS 逐块生成音频，是实时语音 Agent 的架构基础。
- **多语种 TTS vs 跨语言克隆**：前者指引擎内置多语种音色库（如 PlayHT（142 语言，⚠️ 已关闭）），后者指用单一说话人的克隆声纹朗读非母语文本。ElevenLabs 在跨语言克隆保真度上领先。
- **Conversational Speech Model（CSM / 对话语音模型）**：Sesame AI 提出的单阶段多模态 Transformer 架构，将文本与音频 token 交织处理（而非传统 TTS 的「文本→语音」两阶段流水线），生成的语音带有对话上下文感知——能根据多轮对话历史调整韵律、情绪和节奏。代表模型 CSM-1B 以 Apache 2.0 开源，2025 年 2 月首发时被 ZDNET、Ars Technica 等媒体评价为「令人不安地逼近真人」。
- **Full-Duplex TTS（全双工 TTS）**：与传统的半双工（一问一答、轮流发言）相对，全双工 TTS 支持双方同时说话、打断（barge-in）和 backchanneling（「嗯」「我明白了」等反馈声）。Kyutai 的 Moshi（2024 夏）是全球首个全双工实时对话 AI 模型，以 160ms 延迟超越人类对话反应时间。Gradium（Kyutai 的商业化分拆）将此架构产品化。
- **Speech-to-Speech（S2S / 语音到语音）**：输入为音频而非文本。**本 slug 不覆盖 S2S**——实时变声见 [voice-changer.md](voice-changer.md)，跨语言口译见 [audio-translator.md](audio-translator.md)。2026 年 **GPT-Realtime-2** 等原生音频 Agent 虽跳过文本层，但在 Agent 场景仍常与独立 TTS API 并存（IVR 播报、有声书等纯文本输入场景）。

---

## 2026 架构分界：TTS 仍何时需要？

| 场景 | 推荐路径 | 原因 |
|------|---------|------|
| 有声书、旁白、IVR 播报 | **传统/流式 TTS API** | 输入本就是文本，无需 S2S |
| 实时客服 Agent（高推理） | **GPT-Realtime-2** 或 **ElevenAgents + v3 Conversational** | 原生音频+turn-taking，韵律更自然 |
| 模块可替换、成本敏感 | **Cartesia/Deepgram STT + LLM + TTS** 管线 | 按模块优化单价；详见 [speech-to-text.md](speech-to-text.md) |
| 克隆特定品牌声线 | **TTS + voice cloning 层** | 见 [voice-cloning.md](voice-cloning.md) |

## 专题对照 / 扩展定义

TTS 产品选型中有一个关键二分——**云端 API vs 开源本地部署**——两者在采购逻辑上截然不同：

| 对比维度 | **云端 API TTS** | **开源本地 TTS** |
|----------|-----------------|------------------|
| 音质天花板 | 最高（ElevenLabs MOS 4.6+、流式低延迟） | 快速追赶（F5-TTS MOS 4.6、StyleTTS 2 超越真人） |
| 部署成本 | 按字符/小时计费，规模越大边际成本越高 | 一次性 GPU 投入或消费级 GPU 推理 |
| 隐私与合规 | 文本/音频离开本地，需审计 API 条款与训练数据政策 | 全部数据留存在本地，适合受监管行业 |
| 迭代速度 | 厂商持续优化，无需自行维护 | 需跟进社区更新，模型停更风险（如 Coqui/XTTS） |
| 商用许可 | 通常明确（付费即可商用） | 混乱——XTTS 非商用、F5-TTS 权重 CC-BY-NC、Kokoro MIT |
| 典型选型触发词 | 「开箱即用」「不想管 infra」「需要超低延迟流式」 | 「数据不能出内网」「长期大规模调用要控成本」「需要定制微调」 |

另一个关键二分——**单语种优化 vs 多语种覆盖**——直接决定产品推荐：WellSaid Labs 英语质量极高但只用英语，PlayHT（已关闭）曾以 142 语言覆盖制胜但单个语种质量不如专业选手。

2026 年的新关键二分——**半双工 TTS vs 全双工对话模型**——决定了产品能否用于实时语音 Agent：

| 对比维度 | **半双工 TTS（传统）** | **全双工对话模型** |
|----------|----------------------|---------------------|
| 交互模式 | 轮流发言，一方说完另一方才能开始 | 双方可同时说话，支持打断与 backchanneling |
| 架构 | 文本→语音两阶段流水线 | 音频+文本联合建模，单阶段生成 |
| 延迟目标 | 首包 < 200ms（流式 TTS） | 端到端 < 200ms（含理解和生成） |
| 上下文感知 | 仅当前句子级 SSML/韵律控制 | 多轮对话历史驱动情绪和节奏 |
| 代表产品 | ElevenLabs、PlayHT⚠️、WellSaid | Sesame CSM、Gradium、GPT-Realtime-2、ElevenAgents v3 Conversational |
| 典型场景 | 有声书、配音、IVR 播报 | 语音 Agent、客服、AI 陪伴、车载助手 |
| 开源可选 | F5-TTS、CosyVoice、Qwen3-TTS | CSM-1B、Moshi（Kyutai） |

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

- **基础合成**：文本解析（分词、归一化、多音字消歧）→ 声学模型（文本→梅尔谱或声码器参数）→ 声码器（谱→波形）。现代方案多为端到端，跳过显式中间表示。2026 年出现的新范式（Qwen3-TTS Dual-Track 架构）以离散多码本语言模型取代传统的「LM + Diffusion」级联，实现首字即出音频的流式生成。
- **音色多样性**：预置音色库规模（从几十到 900+）、音色分类（年龄、性别、风格、口音）。多说话人模型可在同一引擎内切换不同声线。
- **零样本克隆**：从 2-60 秒参考音频提取声纹，无需微调即可为该声纹生成任意文本。质量取决于参考音频的干净程度与时长。F5-TTS 宣称 2 秒即可实现可用克隆。
- **情感与韵律控制**：AI 驱动的情感自动检测（根据文本语境判读应使用「兴奋」「同情」「专业」等语调）vs 手动 SSML 标签控制——前者省力但可控性差，后者精细但学习成本高。
- **流式与延迟**：批式 → 输出流式 → 双流式（LLM token + TTS 并行）。2025 年实时 Agent 场景的硬指标是 FPL < 200ms。Cartesia Sonic 号称 < 100ms，ElevenLabs flash_v2 约 180-250ms，Qwen3-TTS 以 97ms 端到端延迟创下开源 TTS 新低（2026.1）。
- **多语种覆盖**：从英语单语（WellSaid）到 142 语言（PlayHT，已关闭）到「中英双语深度优化」（F5-TTS）。跨语言克隆（一个声纹说多种语言）是溢价能力最强的维度。
- **长文本鲁棒性**：有声书/教材场景需要处理数万字连续文本而不出现音质漂移、漏句、「核嗓」音调异常。部分模型在 5000+ 字长文后表现退化。
- **非语言音效**：笑声、叹息、哭泣、音乐、背景音——Bark 是目前唯一原生支持的开源模型；商业产品（ElevenLabs）可通过 prompt 引导部分非语言表达。
- **端侧与离线部署**：从云端 GB 级模型到端侧 100MB 以下的轻量化引擎（Kokoro-82M、Piper、Sherpa-onnx），适合嵌入式设备、车载、工业场景。
- **音频水印与溯源**：音频水印（频域不可感知嵌入）、C2PA 内容凭证——正在成为合规基础设施而非可选功能。
- **全双工与对话上下文**：传统 TTS 是「一次性生成」——每次调用独立，不记忆上一句说了什么。全双工对话模型（Moshi、CSM）将对话建模为两个并行的音频流，支持实时打断、语气承接和 backchanneling。这一能力正在从学术原型（Moshi 2024）走向商业产品（Gradium 2025）和开源生态（CSM-1B Apache 2.0）。
- **极致轻量化**：2026 年出现了一批 < 100MB 的高质量端侧 TTS 引擎。KittenTTS 最小仅 14M 参数 / 25MB（Nano），纯 CPU 运行，Apache 2.0 开源——目标是将可接受的 TTS 质量带到 IoT、浏览器和功能手机上。这比 2024 年的 Piper 更进一步压缩了模型体积与推理成本。

---

## 形态谱系（与具体品牌解耦）

- **Type A — 云端 API 型（Cloud API TTS）**：按字符/小时计费的 HTTP/gRPC API，开发者集成最快。覆盖从通用 TTS（Google Cloud、Amazon Polly、Azure Speech）到 AI-native 精品（ElevenLabs、Cartesia、PlayHT⚠️）。核心评估维度：音质（MOS）、流式延迟、语种数、克隆能力、定价模型。
- **Type B — 全能工作室型（Studio / All-in-One）**：面向非开发者——脚本编辑、音色选择、背景音乐、视频同步在一个 UI 内完成。Murf.ai 是代表：降低「从文案到成品配音」的跨工具摩擦。适合 L&D 团队、营销部门、e-learning 创作者。
- **Type C — 开源模型型（Open-Source Model）**：可自部署的预训练模型。F5-TTS（MIT 代码许可，中英最强）、CosyVoice（阿里通义系，中文社区活跃）、StyleTTS 2（学术质量标杆，超真人 MOS）、Bark（Suno，唯一支持非语言音效）。2026 年新锐：Qwen3-TTS（阿里，97ms 延迟，Apache 2.0）、OmniVoice（小米，646 语言，Apache 2.0）、KittenTTS（14M 参数 / 25MB，纯 CPU）。选型需额外评估许可证合规与社区活跃度。
- **Type D — 企业合规型（Enterprise Brand Voice）**：面向金融、保险、医药等受监管行业——SOC 2、SSO、严格内容审核、客制化品牌声线、从真人声音演员授权构建（非 AI 合成）。WellSaid Labs 是代表，代价是英语单语且价格远高于通用 API。
- **Type E — 端侧/嵌入式型（On-Device / Edge TTS）**：离线运行、零网络延迟、数据不出设备。从手机端（iOS/Android 内置 TTS）到工业嵌入式（Piper、Sherpa-onnx）到消费硬件（车载语音助手）。3-100MB 模型体积，牺牲部分音质换取隐私与低延迟。
- **Type F — 实时 Agent 型（Real-Time Conversational）**：专为 LLM 语音对话场景优化的低延迟引擎——双流式架构、可中断、可重规划。Cartesia Sonic（<100ms）、ElevenLabs Conversational AI、Deepgram Aura。核心评估：FPL、并发能力、打断后的上下文保持。
- **Type G — 对话语音模型型（Conversational Speech Model / CSM）**：单阶段多模态 Transformer，将文本与音频 token 联合建模，具备多轮对话上下文感知和全双工能力。与传统 TTS 的「每次调用独立」不同，CSM 能根据对话历史动态调整韵律、情绪和交互节奏。Sesame CSM-1B（Apache 2.0，2025.3）是开源代表，其 8.3B 完整版在盲测中与真人录音无明显偏好差异。Gradium（基于 Kyutai Moshi 架构，2025.12 商业化）以 160ms 全双工延迟 + 10 秒语音克隆 + 5 语言覆盖进入市场。核心评估：对话自然度、打断流畅性、上下文连贯性、情感一致性。

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

## 工具与产品类型（「AI text-to-speech」外延里常出现的品类；非穷尽、无排序优先级）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Cloud TTS API** | REST/gRPC 接口、按字符计费、多语种预置音色、流式支持 | ElevenLabs、Google Cloud TTS、Amazon Polly、Azure Speech、OpenAI TTS |
| **AI Voice Studio** | GUI 编辑器、脚本管理、多音轨、背景音乐、视频同步 | Murf.ai 为代表，降低非技术用户的「文案→配音」摩擦 |
| **Enterprise Brand Voice** | 声线客制化、真人声音演员授权、SOC 2、SSO、内容审核 | WellSaid Labs 为代表；英语单语、定价高于通用 API |
| **Open-Source TTS Model** | 预训练权重、自部署、社区维护 | F5-TTS、CosyVoice、StyleTTS 2、Bark、Kokoro、Piper |
| **Real-Time Conversational TTS** | 双流式架构、<200ms FPL、可中断、并发优化 | Cartesia Sonic、ElevenLabs Conversational AI、Deepgram Aura |
| **On-Device / Edge TTS** | 离线推理、<100MB 模型、零网络延迟 | Piper、Sherpa-onnx、iOS/Android 系统内置 TTS |
| **Voice Cloning API** | 零样本/少样本克隆、跨语言克隆、情绪保留 | 常作为 TTS API 的高级功能层而非独立产品（ElevenLabs、Resemble AI、PlayHT⚠️） |
| **Audiobook / Long-Form TTS** | 长文本鲁棒性、章节管理、多角色声线切换 | ElevenLabs Projects、Amazon Polly 长文本模式 |
| **Conversational Speech Model** | 单阶段多模态 Transformer、全双工、多轮上下文感知、打断与 backchanneling | Sesame CSM-1B（Apache 2.0）、Gradium（Moshi 架构）——与 TTS 有本质架构差异，评估维度不同 |
| **Adjacent（常一起出现但不等于 TTS 本体）** | **voice changer**（实时变声）、**voice cloning**（声纹复制）、**audio translator**（翻译配音）、**AI music vocal**（歌声合成） | 相邻能力；选型与合规各自单算 |

---

## 外链索引（外链；非广告、无排序优先级）

### 横向盘点与对比

| 名称 | 一句话 | URL |
|------|--------|-----|
| Text-to-Speech APIs in 2026 | 2026 年主流 TTS API 横向评测（音质、定价、延迟） | [voicecontrol.chat](https://voicecontrol.chat/blog/posts/text-to-speech-apis-in-2026-voices-pricing-and-what-natural-really-means) |
| Top Alternatives to ElevenLabs in 2026 | 按场景推荐的 ElevenLabs 替代方案 | [smallest.ai](https://smallest.ai/blog/top-alternatives-to-elevenlabs-in-2026) |
| Best Open Source TTS Models | 开源 TTS 模型跑分与部署指南 | [northflank.com](https://northflank.com/blog/best-open-source-text-to-speech-models-and-how-to-run-them) |
| 2025 TTS Evaluation (Chinese) | 2025 年三大开源 TTS 模型中文测评（声网） | [shengwang.cn](https://www.shengwang.cn/blog/blogdetail/2025-TTS-evaluation/) |
| Coval TTS Benchmarks | TTS 延迟与并发压测基准 | [coval.dev](https://www.coval.dev/blog/new-insights-expanding-our-voice-ai-stack-benchmarks-beyond-tts) |
| Complete Guide to TTS Technology 2025 | TTS 技术架构全览（Picovoice） | [picovoice.ai](https://picovoice.ai/blog/complete-guide-to-text-to-speech/) |

### 厂商页

| 产品 | 一句话 | URL |
|------|--------|-----|
| **ElevenLabs** | 音质天花板、零样本克隆、流式 API | [elevenlabs.io](https://elevenlabs.io/) |
| **PlayHT** ⚠️ | 142 语言 + 跨语言克隆 + 博客转音频（已于 2025.12 关闭） | ~~play.ht~~ 已迁移至 play.ai |
| **Murf** | 全能配音工作室、非技术用户友好 | [murf.ai](https://murf.ai/) |
| **WellSaid Labs** | 企业合规品牌声线、英语单语精品 | [wellsaidlabs.com](https://wellsaidlabs.com/) |
| **Cartesia** | 实时语音 Agent 低延迟引擎（Sonic） | [cartesia.ai](https://cartesia.ai/) |
| **Resemble AI** | 语音克隆精度 + 多人对话合成 | [resemble.ai](https://www.resemble.ai/) |
| **F5-TTS** | 2025 开源综合最强，中英零样本克隆 | [GitHub](https://github.com/SWivid/F5-TTS) |
| **CosyVoice** | 阿里系开源，中文社区活跃 | [GitHub](https://github.com/FunAudioLLM/CosyVoice) |
| **Sesame** | 对话语音模型 CSM，开源 Apache 2.0，逼近真人 | [sesame.com](https://www.sesame.com/) |
| **Gradium** | Kyutai 分拆，全双工 160ms，$70M 种子轮 | [gradium.ai](https://gradium.ai/) |
| **OmniVoice (Xiaomi)** | 646 语言开源，40x 实时，Apache 2.0 | [GitHub](https://github.com/k2-fsa) |
| **Qwen3-TTS (Alibaba)** | 97ms 延迟，Dual-Track 架构，Apache 2.0 | [HuggingFace](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |

### 对比与测评（第三方；观点非官方）

TTS 领域的第三方对比在 2025-2026 年围绕几个核心维度：**音质自然度**（ElevenLabs 仍领先但差距在缩小）、**开源追赶速度**（F5-TTS 和 CosyVoice 在中文场景已逼近商业产品）、**延迟与并发**（Cartesia 在实时 Agent 场景异军突起）、**定价模型复杂度**（按字符 vs 按小时 vs 按月席位，需按实际用量建模）。

教育向评测中，**Murf** 常以「上手最无痛」胜出，**ElevenLabs** 以「情感表达最丰富」用于故事叙述，**PlayHT**（⚠️ 已关闭）曾以「博客一键转音频」成为内容营销团队首选。企业采购向评测中，**WellSaid** 以合规与品牌一致性胜出但被「英语单语」限制反复提及；**Google Cloud / Amazon Polly** 多作为「不缺钱但也不冒险」的安全牌。

开源侧，2025 年的叙事主线是 **F5-TTS 的崛起**——2 秒零样本克隆、RTF 0.15、中文原生优化——被社区广泛认为是 XTTS 的继承者（XTTS 因 Coqui 停业且非商用许可已不适合新项目）。Bark 的表现力（笑声/音乐/叹息）独一无二但不可控音色、推理慢，被视为创意实验工具而非生产引擎。

2026 年的新叙事线是 **全双工对话模型的商业化**——Sesame CSM 的「恐怖谷」demo 引发了全球媒体关注（ZDNET、Ars Technica、PCWorld），Gradium 以 7000 万美元种子轮从 Kyutai 分拆将 Moshi 架构产品化，标志着对话语音从「轮流发言」向「自然打断」的范式转移。

开源生态在 2026 年迎来爆发：**Qwen3-TTS** 以 97ms 端到端延迟和 Dual-Track 架构重新定义了流式 TTS 的速度上限；**OmniVoice** 以 646 语言覆盖 + Apache 2.0 许可将极端多语言 TTS 从商业 API 独占变为开源可自部署；**KittenTTS** 以 25MB 体积证明了高质量 TTS 可以跑在纯 CPU 上。三者共同传递的信号是——开源 TTS 在 2026 年已不亚于商业产品，且覆盖了商业产品尚未触及的极端场景（646 语言、25MB 端侧、97ms 实时）。

*本小节为网摘与社区评测观点综合，非 Alignify 实测；**不**以各厂商自有营销博文为论证主体。*

---

## 延伸阅读与参考材料

- **ElevenLabs 官方博客 · 多语言 TTS**：[Multilingual TTS: Reaching a Global Audience](https://elevenlabs.io/blog/multilingual-text-to-speech-reaching-a-global-audience-with-ai-voices)
- **F5-TTS 论文与项目**：[F5-TTS: A Fairytaler that Fakes Fluent Speech](https://arxiv.org/abs/2410.06885) —— 流匹配 + DiT 的非自回归 TTS
- **StyleTTS 2 论文**：[Human-Level Text-to-Speech through Style Diffusion](https://arxiv.org/abs/2306.07691) —— 首个 MOS 超越真人的 TTS 模型
- **语音克隆全球立法综述**：[Deepfakes, Voice Cloning, and AI Impersonation: The Global Rules (Harris Sliwoski)](https://harris-sliwoski.com/zh/blog/deepfakes-voice-cloning-and-ai-impersonation-the-global-rules-are-already-here-and-they-dont-agree/)
- **Sen · Hassan 致函语音克隆厂商**：[Senator Hassan Presses Leading AI Voice Cloning Companies (2026.4)](https://www.jec.senate.gov/public/index.cfm/democrats/2026/4/senator-hassan-presses-leading-ai-voice-cloning-companies-to-prevent-exploitation-by-scammers)
- **V.O.I.C.E · 风险分类学论文**：[Risk Taxonomy of Synthetic Voice Generation (arXiv, 2026.4)](https://arxiv.org/abs/2604.24794)
- **Picovoice TTS 技术全览**：[Complete Guide to Text-to-Speech Technology (2025)](https://picovoice.ai/blog/complete-guide-to-text-to-speech/)
- **Coval TTS 延迟与并发基准**：[Expanding Our Voice AI Stack Benchmarks Beyond TTS](https://www.coval.dev/blog/new-insights-expanding-our-voice-ai-stack-benchmarks-beyond-tts)
- **Sesame · 跨越对话语音的恐怖谷**：[Crossing the Uncanny Valley of Conversational Voice (2025.2)](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice)
- **OpenAI Realtime 三模型发布 (2026-05)**：[Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)
- **ElevenLabs Expressive Mode**：[Introducing Expressive Mode for ElevenAgents](https://elevenlabs.io/blog/introducing-expressive-mode)
- **Amplify Partners · 音频 AI 的小团队胜出**：[Arming the Rebels with GPUs: Gradium, Kyutai, and Audio AI (2026.2)](https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai)
- **Gradium 发布报道**：[Voice AI Startup Gradium Comes Out of Stealth With $70M Seed Round (Slator, 2025.12)](https://slator.com/voice-ai-startup-gradium-70m-seed-round/)
- **Qwen3-TTS 开源发布**：[Alibaba Open-Sources Qwen3-TTS: 97ms Latency, 3s Voice Cloning (2026.1)](https://pandaily.com/alibaba-open-sources-qwen3-tts-model-suite-delivering-multilingual-ultra-low-latency-speech-generation/)
- **OmniVoice 开源发布**：[Xiaomi Open Sources OmniVoice: 646-Language Speech Synthesis (2026.5)](https://en.theblockbeats.news/flash/344770)
- **Sesame CSM 媒体评测**：[Talking with Sesame's AI Voice Companion is Amazing and Creepy (ZDNET, 2025.3)](https://www.zdnet.com/article/talking-with-sesames-ai-voice-companion-is-amazing-and-creepy-see-for-yourself/)
