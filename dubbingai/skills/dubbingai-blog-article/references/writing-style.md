## §WS — 写作风格与语调

> Phase 4 / Phase 5 加载 · B2C 游戏/直播 · 对标 #01–#03 质量标准
>
> **定位**: 写作质量直接影响读者信任和回访率。本文档覆盖 Editorial Voice、禁止措辞、句段量化指标、空泛句检测、AI 原创性检查——构成 Track S 和 Track C 共同的写作底线。

---

### 1. 评分标准（Phase 5 SelfCheck 引用）

| 分数 | 标准 |
|:---:|------|
| **10** | 品牌 Voice 5 项全满足；空泛句 Track S ≤1 / Track C ≤2；≥1 个具名竞品/工具 + ≥1 个具体 workflow；句段指标全达标 |
| **7** | 可读但偏平；有 1–2 处 Voice 偏差或 1–2 处空泛句；基本合格 |
| **4** | 逻辑跳跃或空泛句 ≥4 处；AI 腔明显（连续抽象开头、telegraphic pattern） |
| **1** | 全文 AI 生成痕迹明显；空泛句 >5 处；零具体细节；禁止措辞多处命中 |

---

### 2. Editorial Voice — 品牌调性

#### 2.1 正向标准（5 项）

| 维度 | 要求 | 判断标准 |
|------|------|------|
| **Clear** | 技术概念解释清楚，不炫技 | 非游戏/音频专业读者能复述核心观点 |
| **Evidence-led** | 先给事实、场景、例子，再下结论 | 每个强判断都有依据或限定（"in our testing"、"as of dubbingai.io"、"marketed as"） |
| **Practitioner-grade** | 像真正玩过游戏、做过直播的人写的 | 有本领域具体对象：latency、virtual mic routing、OBS settings、Discord audio subsystem、Dubbing Box passthrough |
| **Calm but opinionated** | 有判断，但不过度营销 | 至少 1 处承认非 Dubbing AI 方案更适合的场景（如 "Murf wins for polished narration"、"Voicemod has better Elgato Stream Deck integration"） |
| **Category-building** | 帮读者理解品类，不推单一产品 | Dubbing AI 首次出现前，文章已提供独立价值（品类框架 / routing 原则 / 对比轴） |

#### 2.2 文章类型语气标准

| 类型 | 语气 | 不该做 |
|------|------|------|
| **Comparison** | 公正、克制、Wirecutter 式 | 不要把竞品写成 strawman；不要每个对比维度的结论都是 "Dubbing AI wins" |
| **Alternative** | 公平对比，Disclosure 前置 | 不要全篇无竞品优势段；不要 "Dubbing AI is just better" |
| **HowTo / PlatformGuide** | 直接、可执行、少形容词 | 不要长篇战略铺垫；不要写成产品广告 |
| **IntentSplit** | 分流优先，disambiguate 在前两句 | 不要把 Assistant 教程和 live mic 教程混为一谈 |
| **SoundboardPick / SoundEffectPick** | 可略活泼、meme 友好 | 仍禁无来源「#1 best ever」；禁把 community-sounds 当 generator |
| **VoiceActorProfile** | 信息性、轻量趣味 | 产品提及 ≤20%；禁硬塞 CTA |
| **CharacterBridge** | 轻量引导、强链目标页 | 正文 ≤800 词 preset 细节；其余链 programmatic 页 |
| **HardwareGuide** | 诚实 tradeoff、限制作显式说明 | 禁 "Dubbing Box 所有平台零配置" |
| **Diagnosis** | 检查清单式友好、routing-first | 禁在未排除 routing 问题前推 Dubbing AI |

---

### 3. 禁止风格与措辞

#### 3.1 禁止风格 5 类

| 禁止风格 | 触发词/模式 | 替代方式 |
|------|------|------|
| **AI hype** | "revolutionary"、"game-changing"、"AI is transforming voice changers" | 写具体变化："Dubbing AI's latest model reduces latency to sub-30ms on mid-range GPUs" |
| **Vendor puffery** | "{Dubbing AI} is the only solution"、"best-in-class"、"unmatched" | 写具体适用场景与边界，而非绝对化 |
| **Generic SaaS copy** | "unlock your potential"、"seamless"、"magic"、"next level" | 写可验证的具体收益或工作流变化："switching virtual mic takes two clicks in the Dubbing AI tray menu" |
| **Fake neutrality** | 表面比较，每段都推 Dubbing AI | 明确写出竞品在什么场景更合适（≥1 段） |
| **Academic fog** | 连续抽象定义，无具体对象 | 每 300–500 词至少 1 次出现本领域具体对象（mic routing, latency ms, Discord audio subsystem） |

#### 3.2 Dubbing AI 专属禁止措辞

| 禁写 | 正确写法 |
|------|---------|
| over 1000 tones for free | 500+ character-style voices (as of dubbingai.io, {month} {year}) |
| Dubbing AI is the #1 voice changer | Dubbing AI is one of the most popular real-time voice changers on Discord |
| Voicemod falls short / limited voices（无据） | Voicemod offers hundreds of presets; compare on axes you can verify |
| guaranteed <30ms latency | marketed sub-30ms class; verify on your rig |
| seamless magic | N/A（禁止出现） |
| revolutionary AI voice technology | real-time voice changer with low-latency audio processing |
| Murf for Discord gaming | Murf for recorded narration; not built for live gaming mic |
| Dubbing AI updates every week（无据） | check official changelog for latest; avoid unverified cadence claims |
| Impersonate celebrities for fraud | entertainment use; follow platform ToS |

---

### 4. 空泛句检测（10 项）

出现以下模式 → 标记 ⚠️，Track S 超过 2 处 / Track C 超过 3 处 → ❌ Fail：

| # | 空泛句模式 | 为什么空泛 |
|---|------|------|
| 1 | "In today's digital world…" | 零信息——没有说哪个世界、什么变了 |
| 2 | "This is why…"（无前文因果） | 假装总结了什么，但前面没有给出因果链 |
| 3 | "Consider the following…" | 填充句——直接列出内容即可 |
| 4 | "It is important to note that…" | 如果真重要，不需要宣告它重要 |
| 5 | "As we all know…" | 假定读者共识——如果真都知道，不需要写 |
| 6 | "The reality is that…" | 修辞 filler——直接陈述现实即可 |
| 7 | "Here's the thing…" | 口语化 filler，在书面博客中突兀 |
| 8 | "But that's not all…" | 电视购物语言 |
| 9 | "Let's dive in…" | 不需要邀请——读者已经在读了 |
| 10 | "Without further ado…" | 自我指涉 filler |

---

### 5. 句段量化指标

#### 5.1 段落标准

| 检查项 | 标准 | 红线 |
|------|------|------|
| 平均段落长度 | 60–90 words | — |
| 单段上限 | 130 words → ⚠️ | 连续两个 ≥130 词段落 → ❌ |
| H2 下首段 | 必须说明本节要回答什么问题 | 首段即列表/表格 → ❌ |
| 连续抽象开头 | 连续 3 段以抽象判断开头 → ❌ | — |

#### 5.2 句子标准

| 检查项 | 标准 | 红线 |
|------|------|------|
| 平均句长 | 15–24 words | — |
| 长句处理 | 连续多个 35+ words 长句 → ⚠️ | — |
| 从句层数 | 避免 3 层以上从句 | 4 层 → ❌ |
| 语态 | 主动语态优先 | 连续 5 句被动 → ⚠️ |

#### 5.3 具体性检查（3 项）

- [ ] 是否有至少 1 个具名竞品/工具/平台出现（不只是概念）？
- [ ] 是否有至少 1 个具体数字、命令、配置或 workflow step？
- [ ] 是否避免每段都用同一种句式开头（如连续 3 段 "You can…" 开头）？

---

### 6. AI 原创性检查（4 项）

- [ ] **原创观点**: 是否有原创判断，而不只是 SERP top 5 的摘要综合？
- [ ] **品牌独有经验**: 是否有产品生态特有问题/场景/边界（Live vs File 分流、Dubbing Box 硬件、community-sounds vs generator 差异）？
- [ ] **无编造**: 是否没有编造引用、产品能力、时间线或 creator 名？
- [ ] **有判断**: 是否没有过度平衡——每段都 "on one hand / on the other hand" 导致无判断？

---

### 7. Master Checklist — 写作项（8 项）

| # | 检查项 | 标准 | 常见 Fail |
|---|------|------|------|
| **W1** | 论点递进清晰 | 一段一意，逻辑不跳跃 | 段落之间话题突变 |
| **W2** | 无 AI 腔 | 空泛句 ≤2 (S) / ≤3 (C)；§5 句段指标全达标 | telegraphic pattern |
| **W3** | 术语准确 | Live vs File · Assistant vs Mic · Soundboard vs Generator 不混用 | 混用术语类 |
| **W4** | 有具体 example | ≥1 个具名场景/workflow/设置步骤 | 全文抽象论述 |
| **W5** | 对比文承认竞品长处 | ≥1 场景推荐非 Dubbing AI 产品 | 全推自有品牌 |
| **W6** | 边界说明 | 硬件/延迟文必须写限制与 tradeoff | 只有优点 |
| **W7** | 表格服务论点 | 表前有导语、表后有 takeaway | 裸表 |
| **W8** | CTA 自然、匹配阶段 | ≤2 次；选型文链 comparison hub，设置文链 download | 多处或突兀 |

---

### 8. 与相邻文档的关系

- 空泛词（"revolutionary"等）同时触发本文档和 Meta description 质量检查
- 段落节奏多样性 → `presentation-rhythm.md` §1
- 列表质量 → `presentation-rhythm.md` §3
- 竞品描述公平性 → `proof-gate.md` P6 · `product-competitors.md`
- 产品数字 as-of → `proof-gate.md` P1 · `citations.md`
