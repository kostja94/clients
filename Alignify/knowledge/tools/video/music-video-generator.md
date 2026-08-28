# AI 音乐视频生成器（Music Video Generator）· 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网、第三方评测、版权与法律分析）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-06-24**（簇边界修订）。

**品类总览**：[voice.md](../voice-audio/voice.md) · Territory「语音与声音」辐条，但产品哲学为 **music-first**（先有歌后有画）；通用 T2V 见 [video-generator.md](video-generator.md)。

**站内相邻**：[music-generator.md](../voice-audio/music-generator.md)（上游音频） · [video-generator.md](video-generator.md)（**排除**：通用 T2V 横评）

**勿与…混买**：**music-first、beat-sync** 专用 MV 工具；通用 T2V 挪用见 video-generator / text-to-video。

**站内对照**：[alignify.co/tools/music-video-generator](https://alignify.co/tools/music-video-generator) · `/tools/music-video-generator` · [alignify.co/zh/tools/music-video-generator](https://alignify.co/zh/tools/music-video-generator) · `/zh/tools/music-video-generator` · `content/tools/zh/music-video-generator.md`、`content/tools/en/music-video-generator.md` · slug **`music-video-generator`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#music-video-generator-tools`](../../product/alignify-keywords-tools.md#music-video-generator-tools)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI music video generator（本文件所指）**：以音乐/音频为**首要输入**，将音频转化为动态视频的专用工具——核心特征是「先有歌、后有画面」，而非通用 T2V 工具的挪用。与 Runway、Pika、Kling 等通用 AI 视频工具的本质区别在于：内置 beat-sync（节拍同步）、stem separation（分轨分析）、歌词对齐等音乐专属能力栈。
- **Audio-reactive / beat-sync**：视觉内容随音频节拍、BPM、频谱实时变化——是品类内最核心的技术指标。精度从「整曲一个 BPM 粗略对齐」到「分 stem 逐帧映射」差距巨大。Neural Frames 的 8-stem 分析是当前公开可用的最高精度实现。
- **Stem separation（分轨分离）**：将混合音频拆分为独立音轨（kick、snare、vocal、bass、melody 等），各 stem 驱动不同视觉参数。Neural Frames 支持 8 stem——底鼓触发镜头震动、人声触发色彩变化、旋律驱动过渡效果。
- **Scene scripting / storyboard（分镜脚本）**：按歌曲时间轴为不同段落（verse、chorus、bridge）写入独立提示词，实现场景随音乐结构切换。Plazmapunk 的 Scene Editor（GPT-4o 辅助）和 Tunee 的 MV Agent（五种创作模式、全流程自动化分镜）是这一范式的代表。
- **Character consistency（角色一致性）**：跨多场景、多镜头保持 AI 生成角色外观不变——Koyal 将此作为核心卖点（自称"best-in-class"），1 More Shot 通过 custom LoRA 训练实现。在叙事型 MV 中，角色在 verse 和 chorus 中长相不同会立刻破坏沉浸感。
- **Lip-sync / AI singer（口型同步）**：AI 生成角色口型与歌声同步——1 More Shot 宣称"帧级精确口型匹配"。与 `avatar`（视觉数字人）和 `voice-cloning`（声音克隆）品类技术耦合但产品形态不同。
- **Faceless music channel（不露脸频道）**：用 Suno/Udio 生成歌曲 + AI MV 工具生成画面 + 自动化发布流水线的 YouTube 运营模式。2026 年爆发式增长，覆盖 lofi、synthwave、ambient 等品类。经济模型是 Suno Pro（$10/月）+ MV 工具（$14–29/月）= 月成本 $40 内出片。
- **Hybrid pipeline（混合管线）**：组合多个 AI 工具完成「作词 → 作曲 → MV 画面 → 剪辑 → 发布」全链路。2025 年戛纳 AI Film Awards 获奖作品 *Croquette Crew* 使用了 ElevenLabs + Suno + Runway + Kaiber + Pika + Adobe Firefly + GPT-4 七工具串联。2026 年的趋势是单工具内完成「出歌 + 出画」闭环（Neural Tunes、Plazmapunk 内置 AI composer）。
- **Music-first vs video-first（音乐优先 vs 视频优先）**：品类内最根本的产品哲学分裂——music-first 工具要求先上传音频（Neural Frames、Tunee），video-first 工具从文本/图像生成视频再手动配乐（通用 T2V 工具的 MV 用法）。本文件以 music-first 专用工具为主体。

---

## 专题对照 / 扩展定义

### 专用 MV 工具 vs 通用 AI 视频工具的边界

本文件**仅收录以音乐视频为第一场景的专用工具**。通用 AI 视频工具（Runway Gen-3/4、Pika、Luma Dream Machine、Kling 3.0 Omni、Veo 3.1、Seedance 2.0）虽然也能做 MV，但缺少音乐专属能力栈，不在本文档范围内。

| 维度 | 专用 AI MV 工具 | 通用 AI 视频工具（排除） | 易混品类 |
|------|----------------|------------------------|---------|
| 核心范式 | Audio → Video（音频驱动） | Text/Image → Video（文字/图像驱动） | Mirelo：Audio generator（给视频配声音，方向相反） |
| 必备能力 | beat-sync、stem 分析、歌词对齐、BPM 检测 | 镜头控制、分辨率、角色一致性 | AI music generator（Suno/Udio）：只出音频 |
| 典型买家问题 | 「我有一首歌，帮我生成 MV」 | 「我需要一段视频素材」 | 「我需要给静音视频配上音效」（Mirelo 适用） |
| 代表产品 | Neural Frames、Plazmapunk、Koyal、VidMuse、1 More Shot、Kaiber | Runway、Pika、Kling（尽管理论上可做 MV，但不收录） | Suno、Udio（MV 工具的**上游输入源**） |

### 专用 MV 工具内部的子类型分裂

| 子类型 | 核心特征 | 代表产品 | 典型工作流 |
|--------|---------|---------|-----------|
| **Pro 级帧控型** | DAW 式时间轴、stem 级音频分析、4K 输出 | Neural Frames、Koyal | 上传音频 → 逐帧 prompt → 精调时间轴 → 导出 |
| **一键快出型** | 上传音频后自动生成、低保真但速度快 | Freebeat、Plazmapunk（基础模式） | 上传/导入 Suno 链接 → 点生成 → 直接发布 |
| **分镜导演型** | 逐场景 prompt + 角色一致性引擎 | Plazmapunk（Scene Editor）、Tunee（MV Agent）、VidMuse | 编写分镜脚本 → 逐段生成 → 拼接 |
| **歌词/文字型** | 音节级歌词同步、动态排版 | LyricEdits.ai | 上传音频 + 粘贴歌词 → AI 对齐音节 → 导出 |
| **素材剪辑型** | 非生成式 AI——用授权素材库按节拍自动剪辑 | Rotor Videos | 上传音频 → 选风格 → AI 剪辑素材 → 导出 |
| **风格化动画型** | 艺术风格迁移、Flipbook 帧动画、强风格表现力 | Kaiber | 上传音频 → 选艺术风格 → beat-synced 动画 |
| **移动先行型** | 手机端操作、token 制、支持 Suno 链接导入、口型同步 | 1 More Shot | 手机上传/粘贴链接 → 选模式 → 导出 |

---

## 问题域（为何会出现这类产品）

- **MV 预算断崖**：传统 MV 制作成本 $5K–$50K+，独立音乐人几乎无法负担。专用 AI MV 工具将单条 MV 的边际成本压至 $10–$30，且可在数十分钟至数小时内完成。
- **音频可视化需求从 DJ/VJ 圈外溢**：EDM、lofi、ambient 等纯器乐/电子流派本身没有「歌手出镜」传统，AI 视觉化工具天然适配。Neural Frames 的种子用户就是电子音乐人和 VJ——以音频为第一输入的 workflow 恰好命中这批创作者的需求。
- **短内容平台的画面需求**：TikTok、Reels、Shorts、Spotify Canvas 全部要求竖屏/方形动态画面。纯静态封面图已无法满足分发需求。54% 的头部艺人已在用 AI 辅助视觉内容。
- **「不露脸频道」经济模型跑通**：Suno + AI MV 工具 + 自动化发布 = 月成本 $40 内运营音乐 YouTube 频道。2026 年 faceless music channel 爆发式增长。
- **Suno/Udio 用户的下游需求外溢**：AI 音乐生成工具（Suno、Udio）解决了「出歌」，但用户面临「歌有了、画面怎么办」的下一站问题。这是专用 MV 工具最直接的增长引擎——Freebeat、1 More Shot、Atlabs 均以「直接导入 Suno 链接」为核心功能。
- **版权焦虑催生「自有内容」需求**：RIAA vs Suno/Udio 的版权诉讼、SORA 因迪士尼 IP 争议关停——创作者意识到「用 AI 生成原创视觉」比「挪用版权素材做 remix」更安全。专用 MV 工具的商业使用权条款比通用视频工具更清晰。

---

## 能力栈（概念拆分，非厂商功能表）

- **Audio-to-visual mapping（音频到视觉映射）**：BPM 检测、频谱分析、onset detection、stem separation——将音频信号解析为可驱动视觉的参数。精度从「整曲粗略匹配」到「8-stem 逐帧映射」差距巨大。Neural Frames 的 8-stem 分析是当前最高精度实现；Tunee MV Agent 集成 Seedance 2.0 满血版模型，在中文/多语种口型同步方面有独特积累。
- **Beat/lyric synchronization（节拍/歌词同步）**：将视觉切换时间点对齐节拍或歌词边界。LyricEdits.ai 的音节级同步属于此类；Freebeat 的 Singing MV 模式自动按人声段落分镜。与手动剪辑软件的「打关键帧」有本质区别——AI 自动检测并匹配。
- **Prompt-to-scene generation（提示词到场景）**：底层依赖 T2V 模型。在 MV 语境下的特殊需求是「同一 prompt 框架下保持角色/风格跨场景一致」——这是通用 T2V 的弱点，也是 Plazmapunk 的 Scene Editor、Koyal 的 character consistency engine 和 Tunee 的 MV Agent 全流程自动分镜的护城河。
- **Character consistency engine（角色一致性）**：跨场景保持 AI 角色外观不变。Koyal 自称 best-in-class；1 More Shot 通过 custom LoRA 训练（上传参考图 → 锁定角色外观）实现。实现路径通常是在底层 T2V 模型之上叠加 reference image conditioning 或 LoRA 微调。
- **AI music co-generation（音频+视频联生）**：同一平台内同时生成音乐和匹配视频。Neural Frames 于 2026 年 4 月推出 Neural Tunes（文本 → AI 歌曲 + MV），Plazmapunk 内置 AI composer，Tunee 支持「输入文字描述 → 同步生成原创歌曲与 MV」。代表了从「MV 工具」向「音乐+视觉一站式平台」的演进。
- **Multi-model orchestration（多模型调度）**：在一个 UI 内调用多个底层视频模型（Kling、Seedance、Runway 等），按场景特征选择最佳模型。VidMuse 是多模型调度的代表——但其执行质量受 Trustpilot 1.7/5 的严重质疑。
- **Lip-sync（口型同步）**：AI 虚拟角色口型与歌声同步。1 More Shot 宣称帧级精确匹配；Seedance 2.0 宣称支持 8+ 语言口型同步（但 Seedance 是通用视频模型，非专用 MV 工具）。
- **Pipeline automation（流水线自动化）**：用 n8n、Make 等工具串联「LLM 写词 → Suno 作曲 → AI MV 工具出画 → FFmpeg 合成 → YouTube 发布」——faceless channel 运营者的核心工作流。

---

## 形态谱系（与具体品牌解耦）

- **Pro 级时间轴编辑器型**：以 DAW 式时间轴为核心——逐帧 prompt、stem 分析驱动的视觉效果、关键帧控制。核心用户是需要精细控制每个镜头的专业音乐人。Neural Frames 是范式代表，Koyal 以 audio-first 叙事加入此阵营。交付为 Web App，强调逐帧可控而非一键生成。学习曲线最陡。
- **音频驱动 / AI Agent 分镜型**：用户上传音频或输入创意描述 → AI Agent 自动分析歌曲结构（verse/chorus/bridge）、生成分镜脚本和视觉方案 → 用户可在分镜面板上干预单个镜头。核心用户是想要叙事控制力但又不想逐帧操作的独立音乐人。Plazmapunk、Tunee、VidMuse 属于此类。学习曲线中等。
- **一键自动生成型**：上传音频/粘贴 Suno 链接 → 选模式/风格 → AI 全自动生成 → 导出发布。最低操作门槛，最快产出速度。核心用户是需要高频产出社交内容的创作者和 faceless channel 运营者。Freebeat 和 1 More Shot 的 Auto Mode 是代表。
- **歌词/文字专做型**：以歌词同步为核心——音节级对齐、动态排版、karaoke 风格。非生成式 AI 画面，而是文字动画工具。LyricEdits.ai 是目前该子类的唯一代表。
- **素材剪辑型**：非生成式 AI——用百万级授权素材库按节拍自动剪辑。优势是无 AI hallucination、版权安全、适合 YouTube 货币化。Rotor Videos 是代表。
- **风格化动画型**：艺术风格迁移 + 节拍同步动画。核心用户是需要强烈视觉风格辨识度的电子/实验音乐人。Kaiber（Flipbook + Motion 双引擎）是代表——曾被 Linkin Park 用于 "Lost" MV。
- **移动端消费型**：手机 App 操作、token 制按量付费、Suno/Udio/YouTube 链接直接导入。核心用户是手机端创作者和 Suno 用户。1 More Shot（iOS/Android，10 万–50 万安装量）是代表。

---

## 风险 · 合规 · 版权与伦理（外部框架可对照，非法律意见）

- **商用权的逐层许可链**：这是专用 MV 工具最实际的合规问题。Plazmapunk 的商业使用权仅在 €12/月 Punk 以上计划开放；低价计划（Pioneer €4.99）不含商用权。跨模型平台的商用权最为复杂——VidMuse 调度多个底层视频模型，各模型的商用权条款可能不一致且用户难以逐层验证。
- **AI 输出的可版权性**：美国版权局明确——纯 prompt 生成的 AI 输出不受版权保护，必须有充分的人类创作投入。对于 MV 工具，这意味着「一键生成」的输出可能无法注册版权；「分镜脚本 + 逐场景 prompt 调优 + 人工剪辑」更可能满足 human authorship 标准。
- **音乐版权的双重风险**：MV 工具内置的 AI 音乐生成功能（Neural Tunes、Plazmapunk AI composer）使用的训练数据是否获得授权——这复刻了 RIAA vs Suno/Udio 的诉讼逻辑。用户上传的自有歌曲若含 uncleared sample/翻唱，AI 画面生成不改变底层音乐侵权事实。
- **声音/形象克隆（deepfake risk）**：AI 口型同步技术（1 More Shot、Seedance 2.0）可被未经授权克隆真人歌手形象。印度歌手 Arijit Singh 已被 Codible Ventures 未经授权克隆，孟买高等法院签发禁令。美国 47 州已通过 deepfake 相关立法。YouTube 2026 年上线 Likeness Detection Tool。
- **平台政策碎片化**：YouTube 要求披露 AI 生成内容；Spotify 对 AI 音乐态度收紧——2026 年 2 月「Say No to Suno」艺术家联盟指控 AI 曲目稀释版权池。Koyal 的 CHARCHA 安全协议（需 webcam 验证真人身份以防止未经授权的 deepfake）代表了从产品端主动合规的趋势。
- **VidMuse 的特有消费者风险**：Trustpilot 1.7/5 的低评反映了一个品类内值得警惕的问题——credit 制工具可能在生成失败时仍消耗信用点、免费宣称可能后续出现 paywall、客服响应可能严重缺失。在 credit 制 MV 工具选型中，建议优先选择有明确退款政策和活跃社区的厂商（Neural Frames、Kaiber）。

---

## 落地碎片（无先后）

- 先定义输出用途再选工具层级：**Pro 级帧控 + 4K** → Neural Frames/Koyal；**低成本商用** → Plazmapunk Punk（€12/月，品类最低商用门槛）；**日更社交内容** → Freebeat/1 More Shot 一键模式；**歌词视频** → LyricEdits.ai 音节级同步；**YouTube 货币化安全（零 AI hallucination）** → Rotor Videos 授权素材剪辑。
- Suno + MV 工具的跨工具互操作是 2026 年最大效率杠杆——优先选用直接支持 Suno 链接导入的工具（Freebeat、1 More Shot、Atlabs），省去手动下载/上传/对齐。
- Faceless channel 的经济账：Suno Pro（$10/月）+ Plazmapunk Punk（€12/月）+ Canva 做缩略图（$13/月）≈ $35/月全包。但需注意——此赛道已高度拥挤，纯 AI 生成的低差异化内容正面临 YouTube 算法降权。突围策略是选择极窄流派（dungeon synth、sovietwave 等）和人工策展（频道品牌、封面设计、播放列表编排）。
- Credit 制工具的隐性成本陷阱：1 More Shot 和 VidMuse 使用 token/credit 制——生成失败可能仍消耗 credit、高清模式 credit 消耗远超预期。高频用户应优先选择 subscription 制工具（Plazmapunk、Koyal）以锁定月度成本上限。
- Neural Tunes（2026 年 4 月上线）代表了品类演进方向——在一个平台内完成「出歌 + 出画」闭环。关注其他 MV 工具是否跟进内置音乐生成，这会进一步模糊专用 MV 工具与 AI music generator 的边界。
- Tunee 的 OpenClaw API 集成代表了另一种趋势——MV 工具作为可被外部 Agent 调用的 skill，而非封闭的 Web App。如果 Agentic workflow 继续渗透创作者工具链，API-first 的 MV 工具可能比纯 UI 工具更具生态优势。
- Koyal 的 CHARCHA 安全协议（webcam 真人验证）是行业内最早从产品端主动解决 deepfake 合规问题的机制——如果 AI 形象权法规继续收紧，此类安全协议可能成为行业标配，选型时可作为前瞻性加分项。
- 注意 Mirelo（$41M 种子轮，Index + a16z 投）虽然名字像 MV 工具，但实际上是 **audio generation for video**——给静音视频配上音效/配乐，工作流方向完全相反（Video → Audio，而非 Audio → Video）。切勿将其与专用 MV 工具混淆。

---

## 工具与产品类型（仅收录以 MV 为第一场景的专用工具；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Pro 级帧控 MV 工具** | Neural Frames、Koyal | DAW 式时间轴、stem 级音频分析、4K；学习曲线最陡 |
| **AI Agent 分镜 MV 工具** | Plazmapunk、Tunee、VidMuse | AI 自动生成分镜脚本 + 用户干预单镜头 |
| **一键自动 MV 工具** | Freebeat、1 More Shot（Auto Mode） | 上传音频 → 全自动生成；最低门槛 |
| **歌词/文字 MV 专做** | LyricEdits.ai | 音节级歌词同步动画；非画面生成 |
| **素材剪辑 MV 工具** | Rotor Videos | 授权素材库按节拍自动剪辑；非生成式 AI |
| **风格化动画 MV 工具** | Kaiber | 艺术风格迁移 + 节拍同步；Flipbook + Motion 双引擎 |
| **移动端 MV App** | 1 More Shot（iOS/Android） | 手机操作、token 制、口型同步、Suno 链接导入 |
| **AI 音乐生成器（MV 工具的上游）** | Suno、Udio | 只出音频；但几乎所有 MV 工具都在主动集成其链接导入 |
| **音效/配乐生成器（易混淆）** | Mirelo | Video → Audio（方向相反）；非 MV 工具，勿混入 |

---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Neural Frames** | 专用 MV 工具 #1；8-stem 音频分析 + DAW 式时间轴 + 4K；40K+ 艺术家，近 200 万视频；$26–$199/月；2026-04 上线 Neural Tunes（AI 音乐生成） | [neuralframes.com](https://www.neuralframes.com/) |
| **Plazmapunk** | 最低商用门槛 €12/月；GPT-4o Scene Editor 分镜；100K+ 创作者；SDXL/Kandinsky 多风格；内置 AI composer | [plazmapunk.com](https://www.plazmapunk.com/) |
| **Koyal** | YC S24；audio-first 电影级 MV；character consistency 自称 best-in-class；CHARCHA 安全协议（webcam 真人验证防 deepfake）；合作过 Universal Music、T-Series、A.R. Rahman；$29/月 | [koyal.ai](https://www.koyal.ai/) |
| **VidMuse** | Sand.ai 旗下；「Music in, Video out」Video Agent；上线 2 个月 ARR 破千万美金；多模型调度 + 分镜自动生成；⚠️ Trustpilot 1.7/5（credit 消耗、客服缺失） | [vidmuse.ai](https://vidmuse.ai/) |
| **1 More Shot** | iOS/Android/Web；custom LoRA 角色训练 + 口型同步；Suno/Udio/YouTube/SoundCloud 链接导入；token 制 $8.25/月起；10 万–50 万安装量 | [onemoreshot.ai](https://www.onemoreshot.ai/) |
| **Tunee** | 趣丸科技；MV Agent 五大模式（一键MV/对口型/肢体控制）；Seedance 2.0 + 虚拟角色定制 + 音色克隆；OpenClaw API；Tunee 2.0 全球创作挑战赛；免费–$88/月 | [tunee.ai](https://www.tunee.ai/) |
| **Kaiber** | 风格化动画；Flipbook + Motion 双引擎；Linkin Park「Lost」MV 使用；$5–$29/月 | [kaiber.ai](https://www.kaiber.ai/) |
| **Freebeat.ai** | 一键 beat-synced 视频；Suno 链接直接导入；Singing MV / Storytelling MV 双模式；$7–$14/月 | [freebeat.ai](https://freebeat.ai/) |
| **Rotor Videos** | 非生成式 AI——100 万+ 授权素材按节拍自动剪辑；YouTube 货币化友好；$9–$17/月 | [rotorvideos.com](https://rotorvideos.com/) |
| **LyricEdits.ai** | 音节级歌词同步 + 动态排版；karaoke 风格 lyric video 专做；$39/月 | [lyric-ai.com](https://www.lyric-ai.com/) |

### 对比与测评（第三方；观点非官方）

第三方评测和社区讨论里的共识大致分几个叙事线：

**「谁才是真正的专用工具」之争**：社区内对「专用 MV 工具」vs「通用视频工具做 MV」有明确区分标准——工具是否要求先上传音频、是否内置 beat-sync 和 stem 分析、是否以音乐为第一输入源。按此标准，Neural Frames 是社区公认最专注的 MV 工具（Techloy 2026 年 9 工具横评第一，92/100 分），Plazmapunk 和 Kaiber 紧随其后。通用视频工具（Runway、Pika、Kling）尽管画质有时更高，但缺少音乐专属能力栈，不被视为同一品类。

**VidMuse 的争议**：VidMuse 是 2026 年最两极化的产品——ARR 千万美金、$5000 万融资的商业成绩亮眼，但 Trustpilot 1.7/5 的低评暴露了严重的执行问题。社区报告的问题包括：宣称免费但中途 paywall、生成失败仍消耗 credit、视频被截短（如 3:42 的歌被切成 3:15）、项目无故被删、客服 6–7 天无响应。2026 年多个第三方横评（ToolWorthy 11 工具、Techloy 9 工具、Serenade Magazine 平台指南）均未收录 VidMuse——这一缺席比低分更值得注意。

**音乐生成 + MV 的闭环趋势**：2026 年最值得关注的结构性变化是专用 MV 工具向上游扩展——Neural Frames 推出 Neural Tunes（2026-04）、Plazmapunk 内置 AI composer、Tunee 支持 text → 原创音乐 + MV 同步生成。这意味着 MV 工具正在吃掉 AI music generator 的部分蛋糕。社区讨论的焦点是：这种闭环是否会进一步挤压纯 AI music generator（Suno/Udio）的生存空间。

**Koyal 的安全协议**：Koyal 的 CHARCHA（webcam 真人验证防 deepfake）在 AI 伦理社区引发了积极讨论——它是行业最早从产品端主动合规的案例。在 deepfake 法规快速推进的背景下，这种「合规即功能」的策略可能成为差异化的选型维度。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各厂商自有营销博文为论证主体。*

---

## 延伸阅读 · 站内知识块

- 音频上游：[music-generator.md](../voice-audio/music-generator.md)
- 排除参照：[video-generator.md](video-generator.md)（通用 T2V，非 music-first）

**站外**

- **Neural Frames 深度评测（2026）**：[Neural Frames Audio Visualizer Review](https://www.toolworthy.ai/tool/neural-frames-audio-visualizer) — 定价、4K 视觉、竞品对比
- **Neural Frames 创始人访谈**：[How Neural Frames is giving independent musicians a visual voice](https://sociable.co/brains-byte-back/you-created-the-song-now-what-how-neural-frames-is-giving-independent-musicians-a-visual-voice-brains-byte-back-podcast/) — Brains Byte Back 播客
- **Koyal 评测（2026）**：[Agentic AI Filmmaking Platform for Music & Video](https://outlierkit.com/resources/koyal-review/) — 含 pricing、CHARCHA 安全协议、行业合作案例
- **VidMuse Trustpilot**：[VidMuse Trustpilot 评价](https://www.trustpilot.com/review/vidmuse.ai) — 1.7/5，credit 消耗与客服问题
- **专用 MV 工具横评（2026）**：[11 Best AI Music Video Generators 2026](https://www.toolworthy.ai/blog/best-ai-music-video-generator) — ToolWorthy 11 工具对比
- **SORA 关停与版权教训**：[Sora 离场后的冷思考](http://field.10jqka.com.cn/20260325/c675546975.shtml)（中文分析，2026-03）
- **Mirelo（易混淆，非 MV 工具）**：[Mirelo raises $41M to solve AI video's silent problem](https://techcrunch.com/2025/12/15/mirelo-raises-41m-from-index-and-a16z-to-solve-ai-videos-silent-problem/) — Audio generation for video，方向相反
- **Tunee MV Agent 发布**：[趣丸科技Tunee上线MV Agent，支持接入OpenClaw](https://www.163.com/dy/article/KP17VP4A05568W0A.html)（中文，2026-03）— 五种创作模式、虚拟角色定制、API 开放
- **1 More Shot 官网**：[Song to Video AI](https://www.onemoreshot.ai/song-to-video-ai/) — 上传音频→AI MV 流程说明
- **AI 输出可版权性**：美国版权局关于 AI 生成内容的指南——纯 prompt 输出不受版权保护（U.S. Copyright Office, 2025–2026）
- **AI 生成角色与形象权**：[YouTube's AI Likeness Detection Tool](https://ubaltlawreview.com/2026/03/16/youtubes-ai-likeness-detection-tool-and-the-emerging-law-of-digital-identity/)（Baltimore Law Review, 2026-03）
