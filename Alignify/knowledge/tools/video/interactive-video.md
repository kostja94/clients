# 实时交互视频（Interactive Video / Live Video Generation）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Interactive video / 实时交互视频**——生成或播放中**持续向前**，用户可中途**改 prompt、投票或发动作**，画面**不重启**而沿当前状态演化；验收以**交互延迟、长程状态保持与 steering** 为主。本页为 **Live Model / 实时交互长视频产品 SSOT**（完整 URL 表仅此一处）；离线 clip → [video-generator.md](video-generator.md)；真 3D / 仿真 → [world-model.md](../world-model.md)；节点编排 → [canvas-video.md](canvas-video.md)。

**材料范围**：公开网络检索（Visko / fal / Odyssey / Google DeepMind / Alibaba / Decart / Krea 等官方博客与通稿、arXiv 技术报告、SiliconANGLE / TechCrunch / The Robot Report 等 Tier 1 媒体、World Labs 世界模型分类文）；**未**将 Alignify 站内 Tools 正文 JSON 当作独立事实来源复述。**具体参数、定价与 API 条款以各官网为准**。网摘整理日期 **2026-09-02**。

**站内对照**：待上线正式页时对齐（新文优先 `/blog/interactive-video`）· slug **`interactive-video`** · KB only

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 `#interactive-video-tools`）

**站内相邻**：[video.md](video.md)（Hub）· [video-generator.md](video-generator.md) · [world-model.md](../world-model.md) · [canvas-video.md](canvas-video.md) · [filmmaking.md](filmmaking.md) · [animation-generator.md](animation-generator.md)

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`interactive-video`（本页）** | **`video-generator`** | **`world-model`** | **`canvas-video`** |
|------|--------------------------------|----------------------|-------------------|-------------------|
| **典型买家问题** | 生成过程中能否改方向？能连续播多久？ | 给我 prompt 出一条可用短片 | 世界怎么模拟/探索？能进机器人/自驾管线吗？ | 怎么在画布上串多个模型？ |
| **主交互** | 持续流 + 中途 prompt/投票/动作 | 一次性 prompt → 固定 mp4 | 探索/API/3D 资产/闭环仿真 | 节点图编排 |
| **时长特征** | 分钟级–小时级（理论无限） | 通常 3 秒–3 分钟 | 依产品（Genie ~数分钟；Marble 一次性 3D） | 依管线 |
| **验收核心** | 交互延迟、长程一致性、状态保持 | 单段画质、音频、角色一致 | 物理/持久性/动作接口/引擎导出 | 编排灵活性与复现 |
| **代表性产品** | 见 §外链索引 | Veo 3.1、Runway Gen-4.5、Kling 3.0 | Genie 3、Marble、Decart Oasis 3 | ComfyUI、Krea Nodes |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Query Model（查询式模型）**：输入一次 → 预测完整输出 → **结束**；主流 AI 视频（Sora、Runway、Veo、Kling）均属此类——适合 bounded clip，**不适合**生成中改 prompt。
- **Live Model（实时运行模型）**：Visko 官方术语——模型作为**持续运行的进程**（run rather than render），维护**持久世界状态**，按真实时间时钟推进；用户可在生成中切换 prompt（steering latency 据 Orbis 技术报告平均 **<1s**）。
- **Interactive video / 实时交互视频（本页主轴）**：不强调厂商命名，指**任何**「画面持续生成 + 用户可中途干预」的视频系统——实现路线见 §形态谱系。
- **Real-time factor（RTF / 实时因子）**：生成 1 秒视频所需的 wall-clock 时间。RTF **< 1** 表示比播放更快（可缓冲无限流）；RTF **≈ 1** 表示边播边生成；RTF **> 1** 仍为离线 clip。
- **In-generation prompt switching**：生成**进行中**修改文本条件，输出沿当前视觉状态继续变化而非从头重渲——本品类核心能力；与 video-generator 的「改 prompt 需重新生成整条」严格区分。
- **Segment chaining（片段拼接）**：多个短 generation 自回归串联、靠上一段 latent 保 continuity——**Type C** 路线；具体窗口见 §外链索引 **fal H3 Max**。
- **Stateful chunk-autoregressive generation**：分块自回归 + **有界多尺度记忆**——**Type A** 路线；长程声称见 §外链索引 **Visko Orbis**。
- **Action-conditioned stream（动作条件流）**：输入为 throttle/steering 等控制信号而非纯文本——**Type F**；主叙事在 [world-model.md](../world-model.md)。
- **vs 直播推流（live streaming）**：本页指 **AI 生成**的持续视频流，非 OBS/摄像头推流；采购时需确认交付为 **generative stream**。

---

## 专题对照 / 扩展定义

**离线 clip vs 本页（实时交互）**：范式定义见 §词汇锚点；下表只列**买家体验差**，不重复术语。

| 维度 | **离线 clip** | **实时交互长视频（本页）** |
|------|------------------------------|---------------------------|
| **用户心智** | 「做一条片」 | 「开一个不断演化的世界/频道」 |
| **典型等待** | 数十秒–数分钟拿成品 | 首帧秒级可见，之后持续流 |
| **改需求** | 重新跑整条 generation | 中途改 prompt/投票/动作 |

| 维度 | **视频流世界模型** | **真 3D 世界模型** |
|------|-------------------|-------------------|
| **输出** | 2D 像素流 | Mesh / 3DGS / 点云 |
| **交互** | 漫游、prompt 事件 | 可导入 Unity/UE |
| **深度** | 本页 + [world-model.md](../world-model.md) §视频 | world-model §Marble/HY-World |

架构路线（Type A 持续流 / RTF 拼接 / 开源 AR / 动作条件）→ **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **Clip 范式不够用**：游戏、互动叙事、直播式 AI 电视、机器人训练 footage 需要「**一直播、能改**」，而非 10 秒定稿片。
- **长程一致性墙**：越长越 drift（人物变脸、色偏、物理穿帮）——2026 年赛道焦点从「单段 4K」转向「**能跑多久还不崩**」。
- **推理速度突破**：fal 等对 MiniMax **H3** post-train + 推理 co-design，使单段生成快于播放，从而 **RTF<1** 支撑无限缓冲流（**注意**：视频无限流用的是 **H3 Max**，不是编程 LLM **MiniMax M3**）。
- **世界模型 API 化**：多家从 demo 走向 **public access / API**——采购开始问延迟 SLA 与按秒计费（代表产品见 §外链索引）。
- **平台 moderation 新摩擦**：always-on 生成内容无法事前审核——fal 工程师 Twitch 实验流被下架后产品化为 **fal.live**，预示 UGC 平台政策与生成式直播的冲突。

---

## 能力栈（概念拆分，非厂商功能表）

- **交互延迟（steering latency）**：从用户改 prompt/动作到画面可见变化的时间——本品类**首要验收维度**，通常比单段画质 benchmark 更关键；各产品数值见 §外链索引。
- **上下文 / memory 窗口**：原生保持人物、场景、风格的时长；超出窗口则靠拼接、压缩记忆或接受 drift。
- **输出维度**：分辨率 × FPS × 是否音视频同步——选型时与目标终端（TV / 移动端 / API 下游）对齐。
- **入口模态**：T2V / I2V / V2V 续写 / 多语言 prompt / **动作条件**（后者多归 world-model + Type F）。
- **交付形态**：Playground、无限 TV 网站、REST/gRPC API、SDK、自托管权重。
- **技术路线（底层）**：Neural SDE + world clock；chunk-wise AR + streaming super-resolution；Self-Forcing / Causal-Forcing 蒸馏（开源线见 §延伸阅读）。
- **成本模型**：多数 consumer 定价未公开；API 产品常见**按秒 / 按 session**——持续生成需按 **world-hour** 估算，勿只看首段 demo 成本。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 单一持续 session，持久 latent，生成中干预 | Live Model / continuous video | Visko Orbis |
| **B** | 因果 rollout + 文本 steering，分钟级+ | Interactive world stream API | Odyssey-2 Pro、Genie 3 |
| **C** | RTF<1，短片段拼接 + 可选观众投票 | Infinite AI TV / faster-than-realtime | fal H3 Max Director、fal.live |
| **D** | Wandering 探索 + Directing 实时改镜 | Open-world wander + direct | HappyOyster |
| **E** | Self-Forcing 系蒸馏，自托管需 GPU | Real-time AR video (open weights) | Krea Realtime 14B；研究向 Helios、LongLive |
| **F** | policy action → 多机位帧（Physical AI） | Action-conditioned driving sim | Decart Oasis 3 → [world-model.md](../world-model.md) |

**Type A vs C**（体验均「无限播」，底层不同）：A 为架构层 Live Model；C 为快于实时 + 工程拼接层——媒体对照见 §外链索引「对比与测评」。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **Always-on moderation**：无限生成流难以事前审核——Twitch/Kick 下架 fal 实验流说明 **平台政策** 可能先于技术成熟度成为上线瓶颈。
- **Deepfake 与误导**：实时改 prompt 降低「做假新闻片」门槛；欧盟 AI 法案合成标识、各平台 AI 内容披露要求仍适用。
- **算力与成本不可见**：hour-scale 4K 实时流的边际成本结构多数未公开——PoC 好看 ≠ 规模商用便宜（SiliconANGLE 引 Constellation 分析师 caution）。
- **基准自报**：Arena 对比多为厂商组织——独立第三方 stress test 尚少；采购勿仅信 launch-day 表格。
- **供应商锁定**：流式 session 状态往往绑定单一推理栈——评估 API portability 与导出/录制策略。

---

## 落地碎片（无先后）

- 先问：**要 closed-loop 仿真（动作 in）还是创作向 steering（文本 in）**——前者优先 world-model + Type F；后者进本页 Type A–E。
- 验收测 **改 prompt 后几秒可见**，而非只评首段 5s 画质。
- 区分 **MiniMax H3**（视频）与 **MiniMax M3**（编程 LLM）——「Twitch 无限流」报道均指 **H3 Max**，非 M3。
- 需要 **可编辑 3D** 时勿买视频流产品——转 [world-model.md](../world-model.md) §真3D。
- 企业 API：确认 **地域、并发、按秒/按 session 计费、录制与 moderation hook**。
- 开源路线：Krea Realtime 14B 等非商用许可——商用需另签或选 API 产品。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Visko Orbis 1.0** | A | 2026-09 Live Model：4K/24fps 实时流，生成中 prompt 切换，hour-scale 记忆 | [visko.ai](https://www.visko.ai/) · [arXiv](https://arxiv.org/html/2607.26694v1) · [通稿](https://www.prnewswire.com/news-releases/ai-startup-visko-closes-10-million-pre-seed-round-and-launches-orbis-its-first-live-model-302865890.html) |
| **Visko · Introducing Live Models** | — | Query Model vs Live Model 范式；六支柱定义 | [visko.ai/blog/introducing-live-models](https://www.visko.ai/blog/introducing-live-models) |
| **fal H3 Max + fal.live** | C | 5s 768p <3s 生成；Director ~2min 上下文；无限 AI TV | [blog.fal.ai/introducing-h3-max-by-fal](https://blog.fal.ai/introducing-h3-max-by-fal/) · [fal.live](https://fal.live/) |
| **Odyssey-2 Pro** | B | 720p/~22fps 交互流；JS/Python SDK | [odyssey.ml/the-gpt-2-moment-for-world-models](https://odyssey.ml/the-gpt-2-moment-for-world-models) |
| **Odyssey Starchild-1** | B | 实时**音视频同步**因果世界模型预览 | [odyssey.ml/introducing-starchild-1](https://odyssey.ml/introducing-starchild-1) |
| **Google Genie 3 / Project Genie** | B | 720p/20–24fps 可探索世界；promptable events；Ultra 美国 18+ | [deepmind.google/models/genie](https://deepmind.google/models/genie/) |
| **HappyOyster 1.0** | D | Wandering + Directing；720p 最长 ~3min；SDK/API gray | [公告](https://www.alibabacloud.com/blog/happyoyster-1-0-is-here_603380) · [happyoyster.cn](https://www.happyoyster.cn/) |
| **Krea Realtime 14B** | E | 开源 14B 因果视频；~11fps B200；生成中改 prompt | [krea.ai/blog/krea-realtime-14b](https://www.krea.ai/blog/krea-realtime-14b) · [GitHub](https://github.com/krea-ai/realtime-video) |
| **Decart Oasis 3** | F | 动作条件驾驶仿真；22fps；<200ms；API ~$0.02/s（媒体报道） | [decart.ai/oasis](https://decart.ai/oasis) · [TechCrunch](https://techcrunch.com/2026/06/10/decarts-new-world-model-can-simulate-hours-of-photorealistic-driving-with-some-caveats/) |

### 对比与测评（第三方；观点非官方）

- **范式之争（2026-09）**：Visko 将 Live Model 与 Query Model 对立（定义见 §词汇锚点）；SiliconANGLE、The Robot Report 报道 Orbis 融资与公众访问；hour-scale 一致性仍待社区 stress test。
- **fal vs Orbis**：架构对照见 §形态谱系 **Type C vs A**；媒体共识为体验相近、可维护性与 steering 精度存疑。
- **Odyssey Arena 与 Visko 论文**：Orbis 1.0 技术报告 long-form Arena 含 Odyssey、LongLive-2、Krea Realtime、Helios——**厂商自组织基准**，引用须标注 tier。
- **平台 moderation**：SaaSCity、Latent Space 综述 fal Twitch→Kick→Rumble 迁移——生成式无限 TV 合规成本被低估。
- **不存在单一 winner**：Genie 偏探索；HappyOyster 偏导演/国内 SDK；Oasis 偏 Physical AI——按 §形态谱系 Type 切片选型。

*本小节为网摘与媒体观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **World Labs 功能分类**：[A Functional Taxonomy of World Models](https://www.worldlabs.ai/blog/taxonomy-of-world-models)（Renderer / Simulator / Planner——本页产品多落在 Renderer + 轻 Simulator）。
- **因果蒸馏开源线**：[Self-Forcing](https://github.com/guandeh17/Self-Forcing) · [Causal-Forcing（清华等）](https://github.com/thu-ml/Causal-Forcing) · [Helios（北大）](https://github.com/PKU-YuanGroup/Helios) · [LongLive 2.0（NVIDIA）](https://github.com/NVlabs/LongLive)。
- **Odyssey Agora-1**：多人共享同一实时生成世界（最多 4 人）——[agora.odyssey.ml](https://agora.odyssey.ml/)。
- **Moonlake Reverie**：游戏 native 实时 diffusion 渲染层——见 [world-model.md](../world-model.md)；偏 programmable gameplay skin。

**站内**

- Hub：[video.md](video.md)
- 离线 clip SSOT：[video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md)
- 3D / 仿真 SSOT：[world-model.md](../world-model.md)
- 编排/垂直：[canvas-video.md](canvas-video.md) · [filmmaking.md](filmmaking.md) · [short-drama.md](short-drama.md)