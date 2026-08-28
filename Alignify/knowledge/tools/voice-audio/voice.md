# AI Voice · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网与产品文档、OpenAI/ElevenLabs 官方发布、Artificial Analysis 等独立基准、TechCrunch/Slator 等行业媒体）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-24**（语音簇边界与架构注记修订）。

**站内对照**：[alignify.co/tools/voice](https://alignify.co/tools/voice) · `/tools/voice` · [alignify.co/zh/tools/voice](https://alignify.co/zh/tools/voice) · `/zh/tools/voice` · `content/tools/zh/voice.md`、`content/tools/en/voice.md` · slug **`voice`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#voice-tools`](../../product/alignify-keywords-tools.md#voice-tools)

> **本页角色**：Territory **「语音与声音」支柱页**——只做品类地图、架构分界与选型路由；TTS/ASR/克隆/变声/翻译/口型/音乐等**子品类细节见各辐条**，避免与 spoke 知识块重复展开。

## 与相邻 slug 分流（Territory 全图；避免混买混评）

| Slug | 典型买家问题 | 输入→输出 | 验收核心 | 知识块 |
|------|-------------|-----------|----------|--------|
| **`voice`（本页）** | 「语音 AI 有哪些品类？我该进哪个？」 | 品类总览 | 理解子类差异与路由 | — |
| **`text-to-speech`** | 「怎么把文字变成自然朗读？」 | 文本→语音 | MOS、流式延迟、多语种 | [text-to-speech.md](text-to-speech.md) |
| **`speech-to-text`** | 「怎么把录音/会议转成文字？」 | 语音→文本 | WER、流式延迟、说话人分离 | [speech-to-text.md](speech-to-text.md) |
| **`voice-cloning`** | 「怎么让 AI 用我的声音说任意话？」 | 样本+文本→克隆语音 | 声纹相似度、跨语言保真 | [voice-cloning.md](voice-cloning.md) |
| **`voice-changer`** | 「怎么实时把我的声音变成别人的？」 | 语音→语音（实时） | 延迟 <100ms、音色转换 | [voice-changer.md](voice-changer.md) |
| **`accent-conversion`** | 「怎么在同语言内让发音更清晰/本地化？」 | 语音→语音（同语言） | 口音真实性+身份保留 | [accent-conversion.md](accent-conversion.md) |
| **`audio-translator`** | 「怎么把外语语音实时翻成我的语言？」 | 跨语言语音/字幕 | 翻译准确度、延迟、声纹保留 | [audio-translator.md](audio-translator.md) |
| **`video-translator`** | 「怎么把整条视频本地化？」 | 视频→翻译视频 | 翻译+配音+字幕+口型管线 | [video-translator.md](video-translator.md) |
| **`lip-sync`** | 「怎么让画面嘴型对上配音？」 | 视频+音频→对口视频 | 唇形精度、零样本能力 | [lip-sync.md](lip-sync.md) |
| **`music-generator`** | 「怎么 AI 作曲/写歌？」 | prompt/歌词→音乐轨 | 音乐性、结构、版权 | [music-generator.md](music-generator.md) |
| **`music-video-generator`** | 「我有一首歌，怎么生成 MV？」 | 音频→音乐视频 | beat-sync、分镜、角色一致 | [music-video-generator.md](../video/music-video-generator.md) |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 共享事实速查（语音簇统一口径）

| 事实 | 统一表述（截至 2026-06） |
|------|------------------------|
| TTS 延迟标杆 | **ElevenLabs Flash v2.5 ~75ms** / **Cartesia <100ms** |
| 开源 TTS 旗舰 | **Fish Audio S2 Pro**（5B，80+ 语言）、**OpenVoice**（MIT） |
| Whisper 版本 | **Whisper v3**（OpenAI 开源 ASR 基础） |
| 实时变声延迟 | **<200ms**（Resemble AI real-time S2S） |
| EU AI Act 语音标注 | **2026-08-02 生效**，合成语音需标注 |
| C2PA 溯源标准 | 正在成为音频水印/溯源的事实标准 |

## 词汇锚点

- **AI 语音（AI Voice）**：利用 AI 技术生成、转换、增强或理解人类语音的广义品类总称。Territory「语音与声音」下分 **说话类**（TTS、克隆、变声、口音、ASR、翻译）与 **音乐类**（作曲、MV）——后者产出旋律/编曲而非对话语音。详见上表辐条索引。
- **文本转语音（TTS）**：文本→语音。细节见 [text-to-speech.md](text-to-speech.md)，本页不展开 MOS/流式/SSML 选型。
- **语音克隆（Voice Cloning）**：样本→特定人声说任意文本。与变声器严格区分——克隆文本自由、通常非实时。见 [voice-cloning.md](voice-cloning.md)。
- **语音转换（Voice Conversion / Speech-to-Speech）**：音频→音频，保留内容改音色。实时变声见 [voice-changer.md](voice-changer.md)；同语言改口音见 [accent-conversion.md](accent-conversion.md)。
- **语音增强（Speech Enhancement）**：去噪、去混响、人声分离——可独立使用或作为 TTS/ASR 前端。2025-2026 代表：ElevenLabs Voice Isolator、Adobe Podcast Enhance Speech。
- **AI 语音 Agent（AI Voice Agent）**：STT + LLM + TTS 串联的实时对话系统；2026 年亦出现 **原生音频模型**（见下「架构注记」）跳过文本中间层。编排平台：Retell AI、Vapi、ElevenLabs ElevenAgents。
- **原生音频模型（Native Audio Model，2026）**：OpenAI **GPT-Realtime-2**（语音推理 Agent）、**GPT-Realtime-Translate**（实时口译）、**GPT-Realtime-Whisper**（流式转写）于 2026-05 进入 Realtime API GA——音频作为一等输入/输出，不再强制 STT→LLM→TTS 三明治。ElevenLabs **Eleven v3 Conversational + Scribe v2 Realtime** 以 Expressive Mode 提供类似垂直整合。选型时需区分：**传统管线**（模块可换、成本低）vs **原生 S2S**（延迟与韵律更自然、单价更高）。

---

## 专题对照 / 扩展定义

| 维度 | **神经网络 TTS（Neural TTS）** | **传统拼接/参数 TTS** |
|------|-------------------------------|----------------------|
| **合成方式** | 端到端深度网络直接从文本预测波形 | 从预录音素库中拼接，或用 HMM 参数生成 |
| **自然度** | 高——可模拟呼吸、犹豫、情感 | 低至中——机械感明显 |
| **语音定制** | 支持零样本克隆、情感控制、风格描述 | 需重新录制完整音素库（数小时素材） |
| **多语言** | 单模型支持 30-140+ 语言 | 每种语言需独立音库 |
| **计算需求** | GPU 推理（云端或高端本地） | CPU 推理（轻量） |
| **代表** | ElevenLabs、Cartesia、CosyVoice 2 | 早期 Amazon Polly、旧版 Siri |

---

## 问题域（为何会出现这类产品）

- **音频内容消费爆炸与制作能力缺口**：有声书市场年增长 25%+，播客数量突破 500 万档——但专业配音员供给增长远低于需求。AI 语音使得文字到音频的转换边际成本趋零。
- **多语言内容本地化需求**：品牌需要为 30+ 市场制作本地化音频内容——传统做法需要 30 组配音员。AI 语音克隆 + 跨语言 TTS 让一条中文配音即可生成 29 种语言的等效音频。
- **从「看」到「听」的消费习惯迁移**：通勤、运动、家务场景下，音频是唯一可消费的内容形式——将文章、报告、教程转为音频的需求驱动了 TTS 的大规模采用。
- **实时语音 Agent 的爆发**：2025-2026 年，AI 语音 Agent 从「实验品」进入「生产部署」——客服、预约、回访等场景用 AI 取代人工初步对话。底层依赖：STT 精度突破（Whisper/Deepgram）+ LLM 推理速度突破 + TTS 延迟降至 40-75ms。
- **语音交互成为 AI 的下一个界面**：GUI → CLI → Chat → Voice——语音是带宽最高、摩擦最低的人机交互方式。ChatGPT 的 Voice Mode 和 Google Gemini Live 验证了「和 AI 说话比打字更自然」的用户行为迁移。
- **声纹作为生物特征的隐私觉醒**：在线语音交流中，声纹可推断性别、大致年龄和情绪状态——AI 变声器提供了实时声纹匿名化能力。但与深度伪造的边界模糊，催生了音频水印、C2PA 等溯源技术。

---

## 能力栈（概念拆分；细节见各辐条）

- **文本前端** → **声学模型** → **声码器**：TTS 三阶段；2026 趋势为 DiT/流匹配与端侧小模型（KittenTTS）并存。详 [text-to-speech.md](text-to-speech.md)。
- **ASR 编码器** → **解码/格式化**：STT 核心；流式 vs 批量取舍。详 [speech-to-text.md](speech-to-text.md)。
- **说话人编码与解耦**：克隆、变声、口音转换的共同基础——分离「说什么」与「谁在说」。详 [voice-cloning.md](voice-cloning.md)、[voice-changer.md](voice-changer.md)、[accent-conversion.md](accent-conversion.md)。
- **跨语言管线**：ASR→MT→TTS 级联 vs 端到端 S2ST（GPT-Realtime-Translate、Gemini Native Audio）。详 [audio-translator.md](audio-translator.md)。
- **视听管线**：翻译→配音→唇形→混音。详 [video-translator.md](video-translator.md)、[lip-sync.md](lip-sync.md)。
- **Agent 编排**：VAD、打断（barge-in）、turn-taking——无论管线式或原生 S2S 均需工程层。
- **安全与水印**：SynthID Audio、C2PA——克隆与变声场景的合规基础设施。

---

## 形态谱系（与具体品牌解耦）

- **Type A — 全栈语音 API 平台**：通过 REST/WebSocket API 提供 TTS + 语音克隆 + speech-to-speech + 语音增强的全能力组合。面向开发者集成。代表方向：ElevenLabs、Fish Audio S2 Pro（PlayHT 已于 2025 年 12 月被 Meta 收购并关闭平台，原用户向 Murf AI 和 ElevenLabs 迁移）。核心壁垒：音质 + 多语言 + 情感范围 + 克隆精度。
- **Type B — 极低延迟 TTS 引擎**：以「首音延迟（TTFA）」为核心竞争力——40-100ms 出第一段音频。面向实时语音 Agent、交互式语音应答（IVR）等延迟敏感场景。代表方向：Cartesia Sonic Turbo、Smallest.ai Lightning。
- **Type C — 开源 TTS 模型生态**：Apache-2.0/MIT 许可的自部署 TTS 方案——从 15M 参数的边缘模型（KittenTTS）到 11B 的云端大模型（VoxCPM2）。适合有工程能力和数据隐私要求的团队。代表方向：CosyVoice 2、GPT-SoVITS、MOSS-TTS。
- **Type D — 实时语音 Agent 编排平台**：捆绑 STT + LLM + TTS + turn-taking 的托管服务——降低从 demo 到 production 的工程门槛。代表方向：Retell AI、Vapi、Deepgram Voice Agent。核心壁垒：端到端延迟 + 打断处理 + SLA。
- **Type E — 消费者语音工具**：面向非开发者的桌面/移动端语音应用——包括配音工具、播客制作、有声书生成。代表方向：Murf AI、WellSaid Labs、Descript Overdub。
- **Type F — 情感/表现力优先 TTS**：将情感、韵律、非语言声音（笑声、叹息）作为一等公民来建模——而非事后叠加。面向需要高表现力的叙事场景（有声书、动画配音、虚拟角色）。代表方向：Hume Octave、ElevenLabs v3。
- **Type G — 语音增强与修复工具**：专注于提升已有录音的音质——去噪、去混响、人声分离。面向播客主、视频创作者、会议记录场景。代表方向：Adobe Podcast Enhance Speech、ElevenLabs Voice Isolator。

---

## 风险 · 合规 · 安全与伦理（外部框架可对照，非法律意见）

- **深度伪造音频与冒充诈骗**：语音克隆可用于冒充他人进行电话诈骗或社会工程攻击——FTC 2025 年已将 AI 冒充诈骗列为优先执法方向。技术缓解：音频水印（SynthID Audio）、C2PA 内容来源标准、服务商的事前同意验证机制（如 ElevenLabs 的声纹验证）。
- **声纹作为生物特征数据的合规**：声纹在 GDPR 下属于生物特征数据（Art. 4(14)），处理声纹需满足特殊类别数据的合规要求——包括合法基础、数据最小化、影响评估（DPIA）。语音克隆服务商的训练数据来源和用户声纹存储策略是企业采购的关键合规检查项。
- **语音 Agent 的透明性义务**：当 AI 语音 Agent 致电用户时，对方是否有权知道自己在和 AI 说话？欧盟 AI 法案第 50 条要求某些 AI 系统需披露其人工性质——但实时语音对话中的披露义务在各国法域差异大。
- **未经同意的声音克隆**：将某人的声音（如名人、同事）未经授权克隆并用于商业或恶意目的——人格权/肖像权（right of publicity）的法律保护在不同国家差异显著。Murf AI、WellSaid Labs 等平台通过「仅限授权声音」模式规避此风险。
- **开源 TTS 模型的滥用风险**：CosyVoice 2、GPT-SoVITS 等高质量开源克隆工具降低了伪造语音的技术门槛——Apache-2.0 许可证的使用限制在防止恶意用途方面是软约束。

---

## 落地碎片（无先后）

- 先明确场景是「生产语音内容」（配音、有声书）还是「实时对话」（语音 Agent、游戏变声）——两者对延迟、音质、API 的要求完全不同。
- **2026 架构分叉**：高互动 Agent 评估 **GPT-Realtime-2** 或 **ElevenAgents Expressive Mode**；模块化/成本敏感仍用 **STT+LLM+TTS** 管线（各辐条分别选型）。
- 评估 TTS 时看 **音质、首音延迟、多语言**——详 [text-to-speech.md](text-to-speech.md)；勿在支柱页重复 MOS 对比。
- 如果已在使用 ElevenLabs API 生态，其语音克隆 + TTS + Voice Isolator + Conversational AI Agent 平台形成了一定程度的「全栈绑定」——迁移成本需纳入采购评估。
- 对于数据隐私敏感的场景（如医疗、金融），优先选支持自部署的方案（CosyVoice 2 开源、Azure CNV 本地容器）或通过 HIPAA/SOC 2 认证的服务（Deepgram Aura-2、Smallest.ai）。
- 预算敏感的团队不应忽视开源方案——CosyVoice 2（Apache-2.0）在 Seed-TTS-eval 基准上接近商业产品水平，且支持零样本克隆和流式推理。但需要自行承担部署与运维成本。

---

## 工具与产品类型（路由表；详各辐条）

| 检索意图 | 路由 slug | 知识块 |
|---------|-----------|--------|
| 文字朗读 / TTS API | `text-to-speech` | [text-to-speech.md](text-to-speech.md) |
| 录音转写 / ASR | `speech-to-text` | [speech-to-text.md](speech-to-text.md) |
| 克隆我的声音 | `voice-cloning` | [voice-cloning.md](voice-cloning.md) |
| 实时变声 | `voice-changer` | [voice-changer.md](voice-changer.md) |
| 同语言改口音 | `accent-conversion` | [accent-conversion.md](accent-conversion.md) |
| 跨语言语音翻译 | `audio-translator` | [audio-translator.md](audio-translator.md) |
| 视频本地化 | `video-translator` | [video-translator.md](video-translator.md) |
| 嘴型对齐 | `lip-sync` | [lip-sync.md](lip-sync.md) |
| AI 作曲 | `music-generator` | [music-generator.md](music-generator.md) |
| 音乐 MV | `music-video-generator` | [music-video-generator.md](../video/music-video-generator.md) |

---

## 外链索引（架构层；工具清单见辐条）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **OpenAI Realtime API** | GPT-Realtime-2 / Translate / Whisper；原生音频 I/O（2026-05 GA） | [developers.openai.com](https://developers.openai.com/api/docs/guides/realtime) |
| **ElevenLabs ElevenAgents** | Expressive Mode：v3 Conversational + Scribe v2 turn-taking | [elevenlabs.io/docs](https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode) |
| **Artificial Analysis TTS** | 音质 vs 价格独立基准 | [artificialanalysis.ai](https://artificialanalysis.ai/text-to-speech/models?quality=quality-vs-price) |
| **SynthID Audio** | Google DeepMind 音频水印 | [deepmind.google](https://deepmind.google/technologies/synthid/) |
| **AI Voice Generator Market Report** | MarketsandMarkets 2026 语音市场报告 | [marketsandmarkets.com](https://www.marketsandmarkets.com/Market-Reports/ai-voice-generator-market-144271159.html) |
| **Resemble AI PerTh Watermark** | 声纹水印与深度伪造检测 | [resemble.ai](https://www.resemble.ai/perth-watermarker/) |
| **Voice Cloning Market Report** | TBRC / GII 2026 语音克隆全球市场报告 | [gii.tw](https://www.gii.tw/report/tbrc1983575-voice-cloning-global-market-report.html) |
| **Slator 2026 Language AI Report** | 语音 AI 与翻译行业年度报告 | [slator.com](https://slator.com/language-ai-market-report/) |

### 对比与测评（第三方；观点非官方）

TTS 音质/延迟详 [text-to-speech.md §对比与测评](text-to-speech.md#对比与测评第三方观点非官方)。支柱页共识：**2026 年无单一最佳平台**——配音（ElevenLabs/Murf）、Agent（GPT-Realtime-2/Cartesia/ElevenAgents）、开源（CosyVoice/Qwen3-TTS）常组合使用。

*网摘综合，非本站实测。*

---

## 行业注记 · 2026 年语音与声音格局

- **实时语音 Agent 落地**：2026 年，AI 语音 Agent 从实验阶段进入生产——客服、预约回访、电话销售等场景广泛采用「STT→LLM→TTS」管线。Cartesia（<100ms）和 ElevenLabs Flash（~75ms）的亚秒级延迟使实时语音交互流畅可用。
- **语音克隆的监管加速**：EU AI Act（2026-08 生效）要求合成语音标注并嵌入水印。美国 TAKE IT DOWN Act（2025 年生效）要求平台 48 小时内删除未经同意的深度伪造内容。46 个州已制定深度伪造专门立法。水印（如 C2PA、Resemble PerTh）从可选功能变为合规刚需。
- **TTS 质量开源追赶**：Fish Audio S2 Pro（5B 参数，80+ 语言）和 OpenVoice（MIT 许可，300M 参数）在 2026 年将开源 TTS 质量提升到接近 ElevenLabs 的商业水平，推动声纹克隆在中小开发者和隐私优先场景的普及。
- **音频翻译从管线到端到端**：OpenAI GPT-Realtime-Translate（2026-05，70+ 语言→13 输出语言）和 Gemini Native Audio 标志着从传统的 STT→MT→TTS 串行管线向端到端 S2ST 的范式迁移。
- **声纹作为生物特征的隐私挑战**：语音克隆技术的普及与深度伪造语音欺诈（2025 Q1 vishing 环比暴涨 1,600%）形成双刃剑——音频水印、C2PA 溯源和声纹验证正在成为语音 AI 生态的下游安全层。

---

## 延伸阅读与参考材料

- [Advancing voice intelligence with new models in the API (OpenAI, 2026-05)](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)
- [Introducing Expressive Mode for ElevenAgents](https://elevenlabs.io/blog/introducing-expressive-mode)
- [AI Voice Generator Market Report (MarketsandMarkets)](https://www.marketsandmarkets.com/Market-Reports/ai-voice-generator-market-144271159.html)
- [Voice Cloning Market Report (TBRC/GII)](https://www.gii.tw/report/tbrc1983575-voice-cloning-global-market-report.html)
