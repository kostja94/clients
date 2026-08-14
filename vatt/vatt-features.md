# Vatt — 功能分析

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[vatt.md](./vatt.md) | [vatt-motion-graphics.md](./vatt-motion-graphics.md) | [vatt-use-cases.md](./vatt-use-cases.md) | [vatt-site-structure.md](./vatt-site-structure.md) | [vatt-keywords.md](./vatt-keywords.md) | [vatt-reaction-video-types.md](./vatt-reaction-video-types.md)  
> **能力真源**：非 MG 能力见下文 §3；MG 能力 → [vatt-motion-graphics.md](./vatt-motion-graphics.md)

**Last updated**: 2026-08-05

---

## 0. 与 Motion Graphics 的边界

Vatt 能力分两类，**分文档维护、内容不重复**：

| 文档 | 维护范围 |
|------|---------|
| **本文件** | 非 MG：采集、理解、同步、粗剪、反应检测、Hook 结构（非视觉包装部分）、音频工程、长素材、平台导出、时间线机制、版权、评论数据层 |
| **[vatt-motion-graphics.md](./vatt-motion-graphics.md)** | 全部 MG（类型总表 §2.0 + Feature/Status）；含布局、强调动效、字幕、标题卡、贴纸、转场、叠加、MG 音效、平台包装 |

| 能力域 | 文档 |
|--------|------|
| §3.1–§3.6、§3.8–§3.13（及其中非 MG 项） | 本文件 |
| MG 全谱 → [motion-graphics §2.0](./vatt-motion-graphics.md) | [vatt-motion-graphics.md](./vatt-motion-graphics.md) |

工作流中 Step ⑥–⑧ 为 MG 阶段 → 能力详情见 motion-graphics 专文；Step ①–⑤、⑨–⑪ 见本文件 §2–§3。

---

## 1. 核心功能模块

**产品定义（对外推荐英文）**

> Vatt is an AI video editor that understands footage, performs real edits, and keeps every result adjustable on an editable timeline.

中文释义：Vatt 是能理解素材、执行真实剪辑、且所有结果仍可在 **editable timeline** 上调整的 AI 视频编辑器——不是固定双画面拼接工具，也不是生成锁定成片的 AI 黑盒。

**Reaction 场景定义（英文）**

> Vatt helps reaction creators understand long footage, find the moments that matter, organise source and face-cam recordings, shape layouts around the conversation, and keep every AI edit under control.

中文释义：帮助 Reaction 创作者理解长素材、找到关键时刻、组织 Source / Face-Cam、按对话塑造 Layout，并保持对每次 AI 编辑的控制权。

| 功能 | 描述 | 差异化? | Status | 对应页面 URL | 目标关键词 |
|------|------|---------|--------|-------------|-----------|
| **Long-Footage Understanding** | 把数小时原片与 Reaction 录制整理成可检索的时间线地图 | ★★★ | Conditional | 待建 `/features` | understand long reaction footage, ai long video editor |
| **Reaction Highlight Detection** | 自动找出大笑、惊讶、震惊、兴奋等强 Reaction 时刻 | ★★★ | Conditional | 待建 `/features` | ai reaction highlight finder, find best reaction moments |
| **Source and Facecam Sync** | 按音频/时间线索对齐原片与 Face-Cam，减少手动拖波形 | ★★★ | Conditional | 待建 `/features` | sync facecam with source video |
| **Dead Air and Rough-Cut Cleanup** | 清理无意义静音/空录，缩短停顿但不过度拍扁节奏；生成可编辑粗剪 | ★★★ | Conditional | 待建 `/features` | remove dead air reaction video, ai rough cut |
| **Editable AI Timeline** | AI 生成的剪切、布局、字幕、音频、效果均为可编辑时间线对象 | ★★★ | Current | 待建 `/features` | ai video editor editable timeline |
| **Manual Refinement and Undo** | AI 之后可继续手调；可 Undo 某次 AI 编辑 | ★★★ | Current | 待建 `/features` | undo ai video edits, refine ai edits |
| **Motion Graphics** | 布局、字幕、花字、动效等包装能力 | ★★★ | 见专文 | 待建 `/features` | [vatt-motion-graphics.md](./vatt-motion-graphics.md) |
| **Voice-Source Audio Balance** | 协调人声与原片音量；说话时 Automatic Ducking | ★★ | Current | 待建 `/features` | balance reaction voice and source audio |
| **Multi-Source Recording** | 同流程录制屏幕、摄像头、麦克风、系统音频 | ★★ | Conditional | 待建 `/features` | multi-source reaction video recording |
| **Long-to-Short Repurposing** | 从长视频选出强反应做成 Shorts / Reels / TikTok | ★★ | Current | 待建 `/features` | turn long reaction into shorts |
| **AI Commentary-First Edit** | 以创作者评论为主线重组 Movie Reaction（非连续播原片） | ★★ | Opportunity | 待建 `/features` | commentary-first movie reaction |
| **Cold-Open Hook** | 把后段高能时刻提前作开场 Hook | ★ | Conditional | 待建 `/features` | reaction video hook generator |

### Feature Status 说明

| Status | 含义 |
|--------|------|
| **Current Capability** | 有当前产品证据；对外商用文案前仍需 **release-scope** 确认 |
| **Conditional Capability** | 能力存在，但依赖登录、云服务、credits、权限、硬件、素材质量或分析完成 |
| **Product Opportunity** | 已验证需求或方向；**不得写成已上线** |
| **Claim-Restricted** | 话题可用作教育，但不得承诺法律 / 平台 / 质量 / 性能保证 |

判断以 active tool registry、实际 handler、Domain/UI 闭环为准；仅有底层原子能力、disabled tool、设计文档或测试夹具 → 不视为 Feature 可用。

---

## 2. 用户流程

### 2.1 Reaction 完整任务流

```
① Record or Import          录制或导入素材（屏幕 / Face-Cam / 本地文件）
  → ② Understand the Footage  理解素材（镜头、语音、情绪信号、长素材地图）
  → ③ Sync and Organise       同步并对齐 Source / Face-Cam / 音频轨道
  → ④ Build a Rough Cut       粗剪与清理（Dead Air、响度、Ducking）
  → ⑤ Find Reactions & Hooks  找强反应与开场 Hook
  → ⑥–⑧ Layout / Emotion / GFX     → [vatt-motion-graphics.md](./vatt-motion-graphics.md)
  → ⑨ Adapt for Platform      按平台画幅与导出预设适配
  → ⑩ Review on Timeline      在可编辑时间线上审阅与精修
  → ⑪ Export                  导出
```

**粗剪原则（英文）**：*Remove dead air without flattening the reaction.*  
中文：删掉无意义空录，但不要拍扁 Reaction 里作为期待、紧张、憋笑的停顿。

### 2.2 Beachhead Feature Stack（优先级）

| Tier | 定位 | 能力 |
|------|------|------|
| **Tier 1** | Core Reaction Differentiation（产品叙事核心） | Long-Footage Understanding · Reaction Highlight Detection · Source and Facecam Sync · Dead Air and Rough-Cut Cleanup · Editable AI Timeline · Manual Refinement and Undo · *MG Tier 1 → [motion-graphics](./vatt-motion-graphics.md)* |
| **Tier 2** | Complete the Creator Workflow | Hook Suggestions · Voice-Source Audio Balance · Multi-Source Recording · Long-to-Short · AI Commentary-First Edit · Source Burst Planning · Alternative Cut Generation · *MG Tier 2 → [motion-graphics](./vatt-motion-graphics.md)* |
| **Tier 3** | Expansion Opportunities | YouTube Comment Import · Commentary Coverage Map · Source-Usage Overview · Single-Camera Person Separation · Remote Guest Capture · Source-Free Watch-Along · Creator Style Memory · Reusable Highlight Library · Platform Risk Profiles · Pre-Publish Rights Review · *MG Tier 3 → [motion-graphics](./vatt-motion-graphics.md)* |

**Movie Reaction — Copyright-Conscious Stack**：Long-Footage Understanding → Commentary-Linked Source Selection → AI Commentary-First Edit → Source Burst Planner → Creator Cutaway Automation → Still-Frame / Context-Card Substitution → Source Audio Reduction → Long Continuous Source Warning → Commentary Coverage Map → Alternative Cut Generator → Editable Timeline + Human Review  

---

## 3. 能力详表（按模块）

表头统一：**Feature（英文名）** | **描述（中文）** | **Status**

### 3.1 Capture & Source Ingestion（采集与导入）

解决素材从哪来、如何尽量保留后期自由度。

| Feature | 描述 | Status |
|---------|------|--------|
| **Screen Recording** | 录制全屏、窗口或指定区域 | Current |
| **Camera Recording** | 同步录制创作者 Face-Cam | Current |
| **Microphone Recording** | 录下解说与现场声音 | Current |
| **System Audio Recording** | 录制电脑正在播放的原片声音 | Conditional |
| **Multi-Source Recording** | 一次流程同时录屏幕、摄像头、麦克风、系统音频 | Conditional |
| **Editable Source Separation** | 录完后原片、Face-Cam、音频仍可作为独立可调元素 | Conditional |
| **Local Media Import** | 导入本地视频、音频、图片或文件夹 | Current |
| **Batch Media Import** | 一次导入多段 Reaction 或多份素材 | Current |
| **Source URL Import** | 通过链接导入允许使用的素材 | Opportunity |
| **YouTube Comment Import** | 通过 YouTube 链接导入选中公开评论 | Opportunity |
| **Remote Guest Capture** | 将远程嘉宾反应分别录成独立素材 | Opportunity |

### 3.2 Footage Understanding & Search（素材理解与搜索）

先理解素材，再决定如何剪——相对模板工具的重要基础。

| Feature | 描述 | Status |
|---------|------|--------|
| **Shot Detection** | 自动识别镜头切换与画面变化 | Conditional |
| **Shot Descriptions** | 为每个镜头生成可检索描述 | Conditional |
| **Speech Recognition** | 将创作者与原片语音转成文字 | Conditional |
| **Semantic Footage Search** | 按内容含义搜索片段，不依赖时间码/文件名 | Conditional |
| **Silence Detection** | 识别无声或低活动时段 | Conditional |
| **Loudness Analysis** | 分析整条时间线声音强弱 | Conditional |
| **Emotion Signal Detection** | 识别笑、惊讶、兴奋、紧张等强反应信号 | Conditional |
| **Face and Expression Signals** | 检测人脸与表情，支撑 Reaction 分析 | Conditional |
| **Long-Footage Overview** | 把长素材整理成易读的时间线地图 | Conditional |
| **Source-vs-Creator Role Detection** | 判断哪条轨道是原片、哪条是创作者 | Conditional |
| **Speaker and Participant Detection** | 识别多人素材中谁在说话/反应 | Opportunity |
| **Commentary Density Map** | 标出有实质解说 vs 只是观看的时段 | Opportunity |

### 3.3 Sync, Alignment & Source Organisation（同步与组织）

Reaction 常同时存在原片、Face-Cam、麦克风、系统声、第二机位；同步最易耗时。

| Feature | 描述 | Status |
|---------|------|--------|
| **Audio-Video Alignment** | 按共同声音或时间线索自动对齐不同录制 | Conditional |
| **Waveform Sync** | 用波形峰值匹配原片与 Face-Cam | Conditional |
| **Multi-Source Timeline Setup** | 自动把原片、创作者画面、音频放入清晰时间线结构 | Current |
| **Track Role Labelling** | 为轨道标注 Source / Creator / Camera / Microphone 等角色 | Opportunity |
| **Automatic Gap Handling** | 删除片段时相关轨道保持对齐 | Current |
| **Multi-Camera Sync** | 同步同一场 Reaction 的多机位 | Conditional |
| **Single-Camera Person Separation** | 从单画面识别多人并分别构图 | Opportunity |
| **Drift Detection** | 发现长录制中逐渐累积的音画不同步 | Opportunity |

### 3.4 Rough Cut & Cleanup（粗剪与清理）

先把原始素材变成干净、可继续创作的第一版。

| Feature | 描述 | Status |
|---------|------|--------|
| **Dead Air Removal** | 自动识别并删除无意义沉默或空录 | Conditional |
| **Pause Shortening** | 缩短停顿，而非删光所有沉默 | Conditional |
| **Retake Detection** | 找出说错重来、重复台词、重新开始的段落 | Opportunity |
| **Failed Intro Removal** | 删除录制准备与失败开场 | Opportunity |
| **Failed Outro Removal** | 删除结束后的空白与未完成结尾 | Opportunity |
| **Ripple Delete** | 删除一段后自动闭合时间线空隙 | Current |
| **Batch Cut Operations** | 对多选区间批量执行相同剪切/清理 | Current |
| **Filler Word Removal** | 按需删除 “um”“uh” 等填充词 | Conditional |
| **Background Noise Reduction** | 降低解说中的持续背景噪声 | Current |
| **Loudness Normalisation** | 将人声与原片调到更一致响度 | Current |
| **Audio Ducking** | 创作者说话时自动压低原片或音乐 | Current |
| **Rough Cut from a Prompt** | 用自然语言描述需求，生成仍可编辑的第一版粗剪 | Conditional |

### 3.5 Reaction Moment Detection & Editorial Intelligence（反应检测与剪辑智能）

Beachhead 差异化核心：理解「什么时候真正发生了 Reaction」。

| Feature | 描述 | Status |
|---------|------|--------|
| **Reaction Highlight Detection** | 自动找出大笑、惊讶、震惊、兴奋等强反应 | Conditional |
| **Emotional Peak Ranking** | 按情绪强度与剪辑价值排序候选时刻 | Conditional |
| **Commentary Highlight Detection** | 找出有观点的评论、解释、笑话、金句 | Opportunity |
| **Source Highlight Detection** | 找出原片中真正触发反应的关键时刻 | Opportunity |
| **Reaction-Source Pairing** | 将创作者反应与触发它的原片事件配对 | Opportunity |
| **Pause-and-Talk Detection** | 识别暂停原片进行评论/分析的时刻 | Conditional |
| **Replay and Breakdown Detection** | 识别为讲解而重复播放的原片段落 | Opportunity |
| **Reaction Timeline Markers** | 在时间线上标记强反应、评论、笑声、停顿、素材变化 | Conditional |
| **Best-Moment Collection** | 将选中精彩反应收入可复用集合 | Opportunity |
| **Long-Form Highlight Extraction** | 从电影/直播/游戏/整集中提取候选高光 | Opportunity |

### 3.6 Hook, Structure & Story Editing（Hook 与结构）

| Feature | 描述 | Status |
|---------|------|--------|
| **Cold-Open Hook** | 把后面高能时刻提前到开头 | Conditional |
| **AI Hook Suggestions** | 从完整录制给出多个可选高能开场 | Conditional |
| **Context-Preserving Hook** | Hook 中保留必要背景，避免反应脱离上下文 | Opportunity |
| **Recap Builder** | 汇总主要反应、观点与结论 | Opportunity |
| **Question-Led Outro** | 把结论改成邀请讨论的问题式结尾 | Opportunity |
| **Chapter and Segment Suggestions** | 为长 Reaction 建议有意义的章节分段 | Opportunity |

*开场 montage、Intro Builder、End Card / CTA 等视觉包装 → [vatt-motion-graphics.md §2.4](./vatt-motion-graphics.md)*

### 3.7 Motion Graphics（动效 / 包装）

→ **[vatt-motion-graphics.md](./vatt-motion-graphics.md)**（唯一维护处；类型索引见 [§2.0](./vatt-motion-graphics.md)）

### 3.8 Audio, Music & Sound Design（音频工程）

难点是让 Source Audio、Creator Voice、Music、SFX 按说话关系自动协调。

| Feature | 描述 | Status |
|---------|------|--------|
| **Voice-Source Balance** | 协调人声与原片，两者都听得清 | Current |
| **Automatic Ducking** | 创作者开口时自动压低原片或音乐 | Current |
| **Loudness Normalisation** | 不同轨道调到相对一致响度 | Current |
| **Background Noise Reduction** | 减少解说中的持续背景噪声 | Current |
| **Music Bed and Commentary Ducking** | 保留背景音乐，说话时压到人声下 | Current |
| **Source Audio Mute / Restore** | 在选中段落静音或恢复原片声音 | Current |
| **Replay Audio Handling** | 协调重播素材与讲解的声音关系 | Opportunity |

*Reaction SFX、转场音效等 MG 配对 → [vatt-motion-graphics.md §2.8](./vatt-motion-graphics.md)*

### 3.9 Long-Form Editing（长素材）

| Feature | 描述 | Status |
|---------|------|--------|
| **Long-Footage Indexing** | 为数小时原片与 Reaction 建立可搜索索引 | Conditional |
| **Chapter Suggestions** | 自动建议长视频章节与分段 | Opportunity |
| **Highlight Reel Generation** | 从长时间录制汇集强反应与精彩评论 | Opportunity |
| **Long-Form Rough Cut** | 把数小时素材压成可审阅的长视频粗剪 | Opportunity |
| **Batch Dead-Air Cleanup** | 批量删除/缩短反复出现的低活动段落 | Conditional |
| **Repeated Segment Detection** | 找出重播片段或重复解说 | Opportunity |
| **Long-to-Short Repurposing** | 将选中长视频片段改成 Shorts / Reels / TikTok | Current |
| **Reusable Highlight Library** | 保存高质量反应片段供片头、合辑、社媒复用 | Opportunity |

### 3.10 Platform Adaptation & Delivery（平台适配与导出）

| Feature | 描述 | Status |
|---------|------|--------|
| **16:9 Landscape Canvas** | 横屏画布，适合 YouTube 长视频 | Current |
| **9:16 Vertical Canvas** | 竖屏画布，适合 Shorts / TikTok / Reels | Current |
| **1:1 Square Canvas** | 方形画幅 | Current |
| **Vertical Highlight Cut** | 将强反应时刻制成竖屏短视频 | Current |
| **Export Presets** | 按目标平台预设格式、分辨率、帧率、编码 | Current |
| **Poster / Thumbnail Frame Selection** | 从视频中选适合封面/缩略图的强画面 | Opportunity |
| **Multi-Version Export** | 同一项目导出长视频及多个短视频版本 | Opportunity |

*Layout-Aware Resizing、Platform Caption Layout、Platform Outro 等 MG 包装 → [vatt-motion-graphics.md §2.1·§2.9](./vatt-motion-graphics.md)*

### 3.11 Editable Timeline & AI Control（可编辑时间线与 AI 控制）

最重要的信任机制：AI 做完后，用户仍能理解发生了什么并继续修改。

| Feature | 描述 | Status |
|---------|------|--------|
| **Natural-Language Editing** | 用自然语言描述想要的剪辑结果 | Conditional |
| **Project-Aware AI** | AI 动手前先读取当前素材与时间线状态 | Conditional |
| **Editable AI Timeline** | AI 生成的剪切、布局、字幕、音频、效果均为可编辑对象 | Current |
| **Preview Before Commitment** | 应用前先预览 AI 建议及影响范围 | Opportunity |
| **Keep or Skip** | 创作者决定接受或跳过某条 AI 建议 | Opportunity |
| **Undo an AI Edit** | 一键恢复到某次 AI 编辑之前 | Current |
| **Manual Refinement** | AI 之后继续手动调时间、布局、文字、音频、效果 | Current |
| **Partial-Range Editing** | 只让 AI 处理时间线中选中的局部范围 | Current |
| **Editing History and Explanation** | 显示 AI 改了什么、改在何处 | Current |
| **Creator Style Memory** | 跨项目记住偏好的节奏、布局、字幕、效果 | Opportunity |

### 3.12 Copyright-Conscious Movie Reaction Editing（版权意识剪辑）

**产品目标**：自动化「评论优先」剪辑——只在观点需要上下文时使用原片，随后切回创作者 / 静帧 / 字幕 / Context Card；减少无评论支撑的连续原片；每个自动决定可审阅。  
**不是**：规避 Content ID，也不是保证 Fair Use。

**原则（英文）**：*Reduce unnecessary source exposure. Increase original commentary. Keep every automated choice reviewable.*  
中文：减少不必要的原片暴露；增加原创评论；保持每项自动决定可审阅。

**Required Disclaimer（必须保留英文）**

> Vatt can automate commentary-first editing and help creators review source usage, but it cannot determine fair use or guarantee monetisation, claim-free publishing, or freedom from takedowns.

| Feature | 描述 | Status |
|---------|------|--------|
| **AI Commentary-First Edit** | 以创作者评论为主线重组 Movie Reaction，而非沿剧情连续播放 | Opportunity |
| **Commentary-Linked Source Selection** | 将每段评论与理解它所必需的电影上下文配对 | Opportunity |
| **Source Burst Planner** | 将连续电影拆成短暂、可调的 Source Bursts，其间切回原创内容 | Opportunity |
| **Creator Cutaway Automation** | 电影上下文结束后自动切回创作者全屏 / Face-Cam / 解说布局 | Opportunity |
| **Source Audio Reduction** | 不需要原对白/配乐时自动压低或静音原片声音 | Opportunity |
| **Third-Party Music and Dialogue Markers** | 标出配乐、歌曲、长时间连续对白等需重点检查的音频 | Opportunity |
| **Long Continuous Source Warning** | 标记过长、未被评论打断的连续原片/声音 | Opportunity |
| **Source-Usage Overview** | 展示每段原片在成片中的位置、时长与连续使用情况 | Opportunity |
| **Commentary Coverage Map** | 显示原创评论/分析在整条视频中的覆盖位置 | Opportunity |
| **Plot-Continuity Review** | 识别多个片段是否在连续复述剧情，提醒补充分析或重构 | Opportunity |
| **Source-Free Watch-Along Mode** | 不含原视频、只保留创作者与时间参照的 Watch-Along | Opportunity |
| **Platform Risk Profiles** | 按 YouTube Long-Form / Shorts / TikTok 显示不同检查重点 | Opportunity |
| **Alternative Cut Generator** | 自动生成 Commentary-First / Minimal-Source / Source-Free 三种可编辑版本 | Opportunity |
| **Pre-Publish Rights Review** | 导出前集中展示原片、原声、连续片段、评论覆盖与待确认项 | Opportunity |
| **Rights Notes and Source Attribution** | 在项目中记录素材来源、授权、许可与署名 | Opportunity |
| **Copyright Education** | 用权威资料解释 Copyright / Fair Use / Content ID / Reused Content | Opportunity |
| **Copyright-Safe Guarantee** | 声称某版本一定构成 Fair Use / 不会被 Claim | **Claim-Restricted** |
| **Content ID Bypass** | 通过镜像、变速等专门逃避自动版权识别 | **Claim-Restricted** |

*Still-Frame / Context-Card Substitution 等视觉替代 → [vatt-motion-graphics.md §2.4](./vatt-motion-graphics.md)*

创作者常见手法 → 产品判断：

| 做法 | 产品判断 |
|------|---------|
| **Short Source Bursts** | 可自动化；时长是可调参数，**不是「安全秒数」** |
| **Frequent Creator Cutaways** | 可自动化；联动 Commentary / Reaction Detection |
| **Commentary-Led Structure** | 应成为核心自动剪辑逻辑 |
| **Source Audio Reduction** | 可自动化 |
| **Still Frames / Context Cards** | 可生成可编辑替代方案 |
| **Source-Free Watch-Along** | 低原片方案；**不得宣传为绝对安全** |
| **Multiple Pre-Publish Cuts** | 适合 AI 多版本 + 完整时间线控制 |
| Crop / Mirror / Blur / Speed / Pitch | **不能**单独构成 Fair Use；**不得**设计成 Content ID 规避 |

### 3.13 Comments, Community & Audience Feedback（评论与社群）

独立且有潜力的产品方向；当前多为 Opportunity。**评论卡片等视觉包装** → [vatt-motion-graphics.md §2.4](./vatt-motion-graphics.md)

| Feature | 描述 | Status |
|---------|------|--------|
| **YouTube Comment Selection** | 从视频链接导入评论并挑选值得回应的内容 | Opportunity |
| **Comment Theme Clustering** | 按问题、观点、请求或争议自动归类评论 | Opportunity |
| **Comment Sentiment and Intensity** | 找出正面、负面、搞笑、惊讶或争议性强的评论 | Opportunity |
| **Comment Reply Sequence** | 自动形成「展示评论 → 创作者回应」时间线结构 | Opportunity |
| **Comment Evidence Links** | 每条评论保留与原始来源的关联 | Opportunity |
| **Audience Request Finder** | 从评论识别观众想看的新视频与后续解释 | Opportunity |
| **Comment-to-Shorts** | 围绕单条评论快速制作短视频回应 | Opportunity |
| **Privacy and Moderation Controls** | 按需隐藏用户名、头像或敏感评论 | Opportunity |

---

## 4. 技术指标与约束

| 指标 | 数值/描述 | 来源 |
|------|----------|------|
| 能力审计基线 | `video-editor-next` `origin/main` @ `9aca7d7b` | 官方 2026-07-23 |
| 核心信任机制 | Editable AI Timeline + Manual Refinement + Undo | 官方 Feature Universe |
| 粗剪原则 | Remove dead air without flattening the reaction | 官方 |
| 访问模式 | 邀请制（Enter invite code） | vatt.ai 2026-07-06 |
| 站点效率话术 | “10x faster” / “first AI editor…” | 营销原文；**无方法论时不作产品事实承诺** |
| 公司技术叙事 | MACE / ACE / PACE | 融资报道；非本文件 Feature Status 证据 |

*定价与套餐 → [vatt.md §商业模式](./vatt.md)*

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| **Reaction Highlight Detection** | 长录制里找强反应瞬间 | Casey / Sam |
| **Long-Footage Understanding** | 电影、直播、游戏数小时素材可剪 | Jordan / Dana |
| **Source and Facecam Sync** | 原片 + Face-Cam 对齐 | 多数 Reaction 创作者 |
| **Editable AI Timeline** | AI 粗剪后仍要精修控制权 | Riley / Professional Editor |
| **Long-to-Short Repurposing** | 一条长内容拆多条 Shorts | Alex / Streamer |
| **AI Commentary-First Edit** | Movie Reaction 评论优先、减少连续原片 | Movie Reaction 创作者 |
| **Motion Graphics** | 布局、字幕、花字、动效包装 | 多平台创作者 → [motion-graphics](./vatt-motion-graphics.md) |

*完整 Persona / JTBD → [vatt-use-cases.md](./vatt-use-cases.md)；赛道 × Feature Stack → [vatt-reaction-video-types.md](./vatt-reaction-video-types.md)*

---

## 6. Claims Must Not Publish（对外禁令）

以下英文句式**不得作为对外产品承诺**发布（可作内部合规清单）：

- “Vatt guarantees fair use.”
- “Vatt prevents copyright claims or strikes.”
- “Vatt bypasses Content ID.”
- “Clips under a specific number of seconds are automatically safe.”
- “Mirroring, cropping, blurring, speeding up, or changing pitch makes copyrighted footage legal.”
- “Vatt can determine whether an edit qualifies as fair use.”
- “Any reaction video becomes monetisable.”
- “Vatt automatically creates a perfect finished video.”
- “Vatt understands every emotion with 100% accuracy.”
- “All processing stays local.”
- “Every feature works on every operating system.”
- “Vatt is 10x faster,”（无已发布方法论或证据时）
- “Vatt is the first AI reaction editor,”（无站得住的品类证据时）

站点 FAQ / Slogan 中的 “10x” / “first” 仅作营销原文归档，不写入客户文档的产品事实栏。

---

*来源：官方 Product Feature Universe（2026-07-23 审计）· 与站点 FAQ/Slogan 冲突时，以本文件 Status + Claims 禁令为准*
