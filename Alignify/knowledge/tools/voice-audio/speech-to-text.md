# AI Speech-to-Text（ASR / STT / 语音转文字）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Speech-to-Text / ASR / 自动语音识别**——将**语音信号**转为可编辑文字；验收以**WER、流式首字延迟、说话人分离与领域适配**为主。本页为 **STT/ASR 产品 SSOT**（完整 URL 表仅此一处）；文字合成 → [text-to-speech.md](text-to-speech.md)；实时变声 → [voice-changer.md](voice-changer.md)；翻译配音 → [audio-translator.md](audio-translator.md)；会议记录+摘要 → [note-taker.md](../productivity/note-taker.md)（ASR 为底层）。

**材料范围**：公开网络检索——厂商文档（OpenAI Realtime API、Deepgram Nova 3、Google Chirp 3、ElevenLabs Scribe v2、AssemblyAI、Cartesia Ink、Mistral Voxtral）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。**具体参数、定价与 API 条款以各官网为准**。网摘整理日期 **2026-06-24**。

**站内对照**：[alignify.co/tools/speech-to-text](https://alignify.co/tools/speech-to-text) · `/tools/speech-to-text` · [alignify.co/zh/tools/speech-to-text](https://alignify.co/zh/tools/speech-to-text) · `/zh/tools/speech-to-text` · `content/tools/zh/speech-to-text.md`、`content/tools/en/speech-to-text.md` · slug **`speech-to-text`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#speech-to-text-tools`](../../product/alignify-keywords-tools.md#speech-to-text-tools)

**站内相邻**：[voice.md](voice.md)（Hub）· [text-to-speech.md](text-to-speech.md) · [voice-changer.md](voice-changer.md) · [audio-translator.md](audio-translator.md) · [note-taker.md](../productivity/note-taker.md)

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`speech-to-text`（本页）** | **`text-to-speech`** | **`voice-changer`** | **`audio-translator`** | **`note-taker`** |
|------|----------------------------|----------------------|----------------------|-------------------------|------------------|
| **典型买家问题** | 「怎么把录音/会议/播客转成文字？」 | 「怎么把文章变成朗读语音？」 | 「怎么实时变声？」 | 「怎么把英文播客翻成中文语音？」 | 「怎么自动记会议并出摘要？」 |
| **输入** | 语音/音频 | 纯文本 | 实时/录制语音 | 源语言音频 | 会议/通话音频 |
| **输出** | 可编辑文本（含时间戳/说话人标签） | 合成语音 | 换音色后的语音 | 目标语言语音 | 转录 + 摘要 + 行动项 |
| **验收核心** | WER、流式延迟、说话人分离、领域词汇 | MOS、FPL、多语种 TTS | 实时性、音色转换 | 翻译准确度、音色保留 | 摘要质量、集成工作流 |
| **管线位置** | voice-in 第一步 | voice-out | 娱乐/直播 | 跨语言全栈 | ASR 上层应用 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **ASR（Automatic Speech Recognition / 自动语音识别）**：将语音信号转换为文字序列的技术总称。**STT（Speech-to-Text / 语音转文字）** 是其应用层表述，两者在行业讨论中常互换使用。Slug 用 **`speech-to-text`**；正文与 meta 覆盖 **ASR、voice recognition、transcription API、real-time transcription** 等同意图短语。
- **WER（Word Error Rate / 词错率）**：语音识别准确度的核心指标——插入、删除、替换错误之和除以参考文本总词数。越低越好；理想环境下头部产品可达 2-5%，嘈杂环境可能升至 15-20%。**跨厂商对比需在相同测试集上进行**——公开数字不可直接对标。
- **流式/实时转录（Streaming / Real-time STT）**：音频边输入边输出文字，延迟通常在 200-500ms。关键场景：直播字幕、在线会议、语音助手。与批量转录的取舍在于 **延迟 vs 准确度**。
- **批量/离线转录（Batch / Offline STT）**：等待完整音频文件上传后一次性处理，准确度通常高于流式（可利用完整上下文）。关键场景：播客后期、采访整理、视频字幕生成。
- **说话人分离（Speaker Diarization / 分割聚类）**：识别「谁在何时说话」，输出带说话人标签的转录。多用于会议、访谈、客服对话。各厂商实现差异大：部分仅做说话人切换标记，部分支持说话人识别（需注册声纹）。
- **端到端模型（End-to-End ASR）**：从音频波形直接映射到文字 token，区别于传统的「声学模型 + 语言模型 + 词典」级联架构。Whisper（Encoder-Decoder Transformer）、Conformer（CNN + Self-Attention 混合编码器）是当前两种主流端到端路线。
- **Conformer 编码器**：将卷积（捕获局部声学特征）与 self-attention（建模全局上下文）结合。Deepgram Nova 3、Google Chirp 3 均基于此类架构，在噪音鲁棒性与长句理解上优于纯 Transformer。
- **Whisper 风格多语言训练**：在 90+ 语言的 68 万小时弱监督数据上联合训练，单一模型覆盖多语种。优势是零样本泛化强；劣势是特定领域需微调才能达到专用模型精度。
- **自定义词汇/领域适配（Custom Vocabulary / Domain Adaptation）**：向 ASR 引擎注入行业术语、人名、缩写等。Deepgram、AssemblyAI 支持 API 级传参；Whisper 需通过微调实现。
- **on-device / 本地推理**：模型在用户设备上运行（如 Whisper.cpp、Core ML 部署），不从云端传输音频。优势是延迟极低、数据不出设备；劣势是模型体积受限、准确度通常低于云端大模型。
- **原生流式转写（Native Streaming STT，2026）**：专为「边听边出字」设计，与批量 Whisper API 分工不同。选型时区分：**独立 ASR API**（可接入任意 LLM）vs **Agent 内置 STT**（与 TTS/turn 模型耦合）——代表见 §外链索引。

---

## 专题对照 / 扩展定义

**实时转录 vs 批量转录**（范式定义见 §词汇锚点；下表只列买家体验差）：

| 维度 | **实时转录** | **批量转录** |
|------|-------------|-------------|
| 延迟 | 200-500ms | 分钟级（取决于音频长度） |
| 准确度 | 略低于批量（缺少后文上下文） | 最高（可利用双侧上下文） |
| 典型场景 | 直播字幕、语音助手、在线客服 | 播客后期、采访稿、视频字幕 |
| 代表产品 | 见 §外链索引 Type C/D | 见 §外链索引 Type A/B |

| 维度 | **通用 ASR 引擎** | **专精垂直 ASR** |
|------|-------------------|------------------|
| 覆盖语言 | 50-100+ 语言 | 特定语种/口音优化 |
| 领域泛化 | 需要自定义词汇补强 | 预训练已针对领域（如医疗、法律） |
| 代表产品 | Whisper、Chirp 3、Voxtral | Deepgram Nova 3、AssemblyAI |

**独立 ASR API vs Agent 内置 STT**（2025-2026 新分叉）：

| 维度 | **独立 ASR API** | **Agent 内置 STT** |
|------|-----------------|-------------------|
| 集成 | 可接入任意 LLM/TTS | 与 TTS/turn-taking 同平台耦合 |
| 典型产品 | Deepgram、Whisper API、AssemblyAI | GPT-Realtime-Whisper、Scribe v2 Realtime |
| 选型触发 | 模块可替换、成本敏感管线 | 端到端 Agent、最低集成摩擦 |

架构路线 → **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **手动转录效率瓶颈**：1 小时音频人工转写需 3-5 小时；内容创作者、记者、研究人员需要分钟级甚至秒级出稿。
- **会议与客服的存档与可检索需求**：企业每天产生大量音频数据（通话录音、会议录像），非结构化音频无法被搜索、分析、审计。ASR 是音频→文本管道的**第一步**。
- **多语言内容全球化**：企业出海需要同时处理中、英、日、西等多语种音频。开源方案（Whisper）把多语种能力从企业级 API 下放到开发者可自部署。
- **无障碍（Accessibility）合规**：视频平台、教育机构、政府网站需为音频/视频提供字幕。实时字幕还服务于听障群体与多语言观众。
- **AI Agent 需要「听」的能力**：语音助手、AI 客服、车载交互——Agent 管线的 voice-in 端依赖低延迟 ASR。2025-2026 年 Agent 叙事推动了对**流式 + 低延迟** ASR 的新一轮需求。
- **开源 + 本地推理的隐私诉求**：医疗、法律、金融行业受合规约束，音频不得出域。Whisper 开源 + on-device 部署（Whisper.cpp）满足了**数据不出设备** 的刚需。

---

## 能力栈（概念拆分，非厂商功能表）

- **准确度（WER 基线）**：核心差异化维度。影响因子包括：音频质量（采样率、背景噪音）、说话人口音、语种、领域术语密度。**跨厂商对比需在相同测试集上进行**——各厂商公开的 WER 数字不可直接对比。
- **实时性（首字延迟 vs 尾字延迟）**：流式 ASR 关注首 token 到达时间（~200ms）与稳态延迟。部分产品用**投机解码**或**分块流式**压低延迟；各产品数值见 §外链索引。
- **多语言覆盖与口音鲁棒性**：Whisper Large-v3 覆盖 99 种语言；Chirp 3 宣称 100+；Deepgram 支持 30+ 但深度优化英语。小语种与方言的覆盖是**长尾竞争**维度。中文 + 英语混读场景优先选在多语种混合测试集上验证过的产品。
- **说话人分离（Diarization）**：从简单的「说话人切换」标记到「声纹识别 + 说话人命名」。后者需要注册声纹库，复杂度与隐私影响显著升高——会议/访谈场景往往比绝对 WER 更重要。
- **自定义词汇与领域模型**：API 注入 vs 微调 vs 从头训练。Deepgram 提供 API 级 Key Term 注入；AssemblyAI 支持自定义模型训练；Whisper 依赖微调。
- **格式化输出**：自动标点、大小写、数字规范化（"three hundred" → "300"）、时间戳（词级/句级）。各厂商格式质量差异大。
- **部署模式**：云端 API（最低运维成本） vs 本地部署（Whisper.cpp、Docker、VPC） vs 边缘推理（on-device Core ML / TensorFlow Lite）。选型取决于**延迟、隐私、成本**三角。
- **文件格式与集成**：支持 MP3/WAV/M4A/FLAC/OGG 等格式；提供 REST API、WebSocket 流式、SDK（Python/JS/Go 等）。集成复杂度直接影响开发者的**上线速度**。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 全语种覆盖、可本地部署、可微调 | Open-Source ASR / Whisper-style | Whisper（+ WhisperX、faster-whisper 社区衍生） |
| **B** | 针对英语或特定语种深度优化，WER 低于通用开源 | High-Precision ASR API | Deepgram Nova 3、AssemblyAI |
| **C** | 流式 Conformer 或分块 Transformer，牺牲少量准确度换延迟 | Real-Time / Low-Latency STT | Scribe v2 Realtime、Cartesia Ink |
| **D** | 云服务生态内置，统一计费与生态绑定 | Cloud Platform STT | Google Chirp 3、Azure Speech |
| **E** | 本地处理、数据不离开设备，模型较小 | On-Device / Privacy-First STT | Wisprflow、Whisper.cpp |
| **F** | 效率与准确度平衡的新兴轻量模型 | Lightweight Open STT | Voxtral（Mistral） |
| **G** | 与 TTS/turn-taking 同平台，Agent 内置流式转写 | Native Streaming STT / Agent STT | GPT-Realtime-Whisper、Scribe v2 Realtime |

**Type C vs G**（均低延迟，集成逻辑不同）：C 为独立 ASR API；G 与 Agent 管线耦合——选型见 §专题对照「独立 ASR vs Agent 内置」。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **音频数据隐私**：音频包含的生物特征（声纹）与对话内容（可能含 PII）受 GDPR/CCPA/PIPL 等多法域约束。**云端 ASR 意味着音频传输至第三方服务器**；需审查 DPA 与数据留存策略。
- **跨境传输**：音频经云端 ASR 处理时，数据可能跨越国界。中国 PIPL 要求个人信息出境需安全评估；EU 需 SCC 或 adequacy decision。
- **声纹与生物特征**：部分说话人分离功能涉及声纹注册，触发更严格的生物特征数据法规。**需明确告知并获得同意**。
- **转录准确度的法律后果**：医疗、法律、金融领域——一个转录错误可能导致诊断失误或合同纠纷。**关键应用需人工审核 + 置信度阈值**。
- **模型偏见与口音公平性**：ASR 模型在非标准口音（如非洲裔美国人英语、印度英语）上 WER 显著升高。部署前需在**目标用户群体的音频样本**上评估。
- **开源模型的供应链安全**：Whisper 等开源模型依赖社区维护，安全漏洞修复不保证时效。定制微调可能引入新的攻击面（如投毒数据）。

---

## 落地碎片（无先后）

- POC 时用**最能代表生产环境的 10 段音频**（含噪音、口音、多说话人）横向对比至少 3 家 ASR，不只看官网 Demo。
- 对于会议/访谈场景，**说话人分离**往往比绝对 WER 更重要——错误的说话人归属比漏词更影响可读性。
- 实时场景先厘清 **「首字延迟」**（用户感知快慢）与 **「尾字延迟」**（全部文字完成时间）的区别；直播字幕只需首字快，客服分析需要完整上下文。
- 如果有中文 + 英语混读场景，优先选在多语种混合测试集上验证过的产品（Whisper、Chirp 3 在此类场景表现优于单语种专精模型）。
- Agent 场景先确认是否需要 **独立 ASR**（模块可替换）还是 **平台内置 STT**（最低集成摩擦）——见 §专题对照。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **OpenAI Whisper** | A | 开源通用 ASR：99 语言、端到端 Transformer、可本地部署；社区衍生 WhisperX（对齐+分割）、faster-whisper（CTranslate2 加速） | [openai.com/index/whisper](https://openai.com/index/whisper) · [GitHub](https://github.com/openai/whisper) |
| **Deepgram Nova 3** | B | 高精度云端 ASR API：实时+批量、自定义词汇、说话人分离；面向金融/医疗/法律等专业领域优化 | [deepgram.com](https://deepgram.com/) · [Nova 3 技术文](https://deepgram.com/learn/nova-3-speech-to-text-api) · [YouTube](https://www.youtube.com/watch?v=a9rfeYBHdac) |
| **AssemblyAI** | B | 企业级语音 AI 平台：STT + 说话人分离 + 情感分析 + 实体检测；REST API + SDK | [assemblyai.com](https://www.assemblyai.com/products/speech-to-text) · [Blog](https://www.assemblyai.com/blog/) · [YouTube](https://www.youtube.com/watch?v=w09b30BI0lk) |
| **Google Chirp 3** | D | Google Cloud Speech-to-Text 最新模型：100+ 语言、Conformer 架构、与 Google Cloud 生态深度集成 | [Chirp 3 文档](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3) · [YouTube](https://www.youtube.com/watch?v=0scL9ma-52g) |
| **ElevenLabs Scribe v2** | C/G | 实时低延迟转录：~150ms partial transcript；与 ElevenAgents turn-taking 绑定 | [elevenlabs.io/speech-to-text](https://elevenlabs.io/speech-to-text) · [Blog](https://elevenlabs.io/blog/) · [YouTube](https://www.youtube.com/watch?v=_AZ7ptRuzs8) |
| **Cartesia Ink** | C | 实时语音转录：Sonic 模型架构，首字延迟 < 200ms；与 Cartesia TTS 形成语音全栈 | [cartesia.ai/ink](https://cartesia.ai/ink) · [Blog](https://cartesia.ai/blog) · [YouTube](https://www.youtube.com/watch?v=QSnH1GfqaGI) |
| **Wisprflow** | E | AI 语音处理平台：STT + 智能分析（说话人识别、关键词提取、摘要）；支持多种音频格式与云存储 | [wisprflow.ai](https://wisprflow.ai/) · [YouTube](https://www.youtube.com/watch?v=x6XJIbRksgI) |
| **Voxtral（Mistral）** | F | 轻量开放式 STT 模型：Mistral AI 出品，英文与欧洲主要语言优化 | [mistral.ai/news/voxtral](https://mistral.ai/news/voxtral) |
| **GPT-Realtime-Whisper** | G | OpenAI Realtime API 流式转写：边听边出字（2026-05 GA，~$0.017/分钟） | [Realtime API 文档](https://developers.openai.com/api/docs/guides/realtime) |

### 对比与测评（第三方；观点非官方）

- **本地 vs 云端**：Whisper 因开源 + 免费 + 99 语言覆盖在开发者社区占有率最高，但**实时能力不是其设计目标**；Deepgram 与 AssemblyAI 在企业特性（自定义词汇、说话人分离、SLA）上领先，按用量计费。
- **延迟 vs 准确度**：Scribe v2 与 Cartesia Ink 主打「首字延迟 < 200ms」，适合语音助手等对延迟敏感的交互场景——但准确度通常略低于批量模式的同量级模型。
- **Agent 内置 STT 新赛道（2026）**：GPT-Realtime-Whisper 与 Scribe v2 Realtime 形成与独立 ASR API 不同的选型逻辑——前者与 TTS/turn-taking 耦合，后者可接入任意 LLM。
- **不存在单一 winner**：按 §形态谱系 Type 切片选型；跨厂商 WER 对比需在相同测试集上进行——公开数字不可直接对标。

*本小节为网摘与行业观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读 · 站内外

**站外**

- **Whisper 论文与架构说明**（OpenAI 官方 index 页；仓库与模型卡见 §外链索引 **OpenAI Whisper**）
- **Deepgram Nova 3 技术深度**（Conformer 架构、领域泛化——URL 见 §外链索引 **Deepgram Nova 3**）
- **Google Chirp 3 文档**（语言覆盖、流式/批量——URL 见 §外链索引 **Google Chirp 3**）
- **AssemblyAI 研究博客**（Conformer-2、说话人分离演进——URL 见 §外链索引 **AssemblyAI**）
- **Cartesia Sonic / Ink 技术文**（低延迟 ASR 架构——URL 见 §外链索引 **Cartesia Ink**）

**站内**

- Hub：[voice.md](voice.md)
- 反向管线 SSOT：[text-to-speech.md](text-to-speech.md)
- 相邻品类：[voice-changer.md](voice-changer.md) · [audio-translator.md](audio-translator.md) · [note-taker.md](../productivity/note-taker.md)