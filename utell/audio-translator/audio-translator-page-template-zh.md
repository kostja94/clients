# Audio Translator 页面模板与线框图（v2 — 转化优化版）

> 基于 Utell Podcast Translator 已上线页面 + Vofy 12 区块模板体系 + landing page 转化最佳实践，重构为 **13 区块转化驱动骨架**。
>
> 关联：[audio-translator-scenarios.md](./audio-translator-scenarios.md) · [audio-translator.md](./audio-translator.md) · [utell-site-structure.md](../utell-site-structure.md) · [utell-keywords.md](../utell-keywords.md)
>
> **用途**：新增 Audio Translator 子页面时，按 §二确定场景品类 → 复制 §五极简草稿版 → 按 §六逐区块填充 `[ ]` 占位内容。区块顺序固定以保证全站一致性。
>
> **参考页面**：`/audio-translator/podcast` — 首个上线页面，部分区块在 v2 中优化了位置和内容。

**创建日期**：2026-05-11 · **v2 更新**：2026-05-11（转化驱动重构——social proof 前移、新增 mid-page CTA、Hero 改为 outcome 导向、Related Tools 降权、集成 objection handling）

---

## 一、场景品类速查

| 品类 | URL | H1 公式（v2 优化——前半 SEO 主词 + 后半 outcome 钩子） |
|------|-----|------|
| **Podcast** | `/audio-translator/podcast` | `AI Podcast Translator: Reach Global Audiences in 50+ Languages, in Your Own Voice` |
| **Audiobook** | `/audio-translator/audiobook` | `AI Audiobook Translator: Listen to Any Book in 50+ Languages, Narration Preserved` |
| **E-Learning** | `/audio-translator/elearning` | `AI Lecture Translator: Master Any Course in Your Native Language, Terminology Intact` |
| **Interview** | `/audio-translator/interview` | `AI Interview Translator: Transcribe & Translate Any Conversation, Every Speaker Labeled` |

> H1 设计原则：冒号前 = SEO 主词（完全匹配搜索意图）；冒号后 = 用户获得的结果（outcome），非功能描述。第二梯队场景同理。

---

## 二、13 区块转化骨架（v2 重排）

v1 区块顺序为 **信息交付型**（教育 → 功能 → 场景 → social proof垫底），v2 重排为 **转化驱动型**——信任信号前置、CTA 分布在三个决策节点、social proof 紧随产品演示。

| # | 区块 | v1 位置 | 转化角色 | 变更说明 |
|---|------|:------:|------|------|
| 1 | Breadcrumb | 1 | 导航 | 不变 |
| 2 | **Hero + Trust Signals** | 2 | **价值主张 + 信任锚** | 🆕 Hero 内嵌星级/用户数/媒体 logo；H1 改为 outcome 导向 |
| 3 | Tool Widget + Example Gallery | 3–4 | **产品演示 + 降低试用摩擦** | 合并：示例卡片直接内嵌于 tool widget 下方，点选即试 |
| 4 | **Social Proof** ⬆️ | 10→4 | **信任强化** | ⬆️ 从底部移至产品演示后——用户在了解「这是什么」之前先看到「谁在用、效果如何」 |
| 5 | Ch.01 — Education + Why Utell | 5 | **教育 + 异议处理** | 🆕 集成竞争对比（vs 传统翻译 / vs 竞品），在此处理「为什么不用 X」 |
| 6 | Ch.02 — Pipeline | 6 | **透明度（降低不确定性）** | 不变：4 步流程让用户感知「不复杂」 |
| 7 | Ch.03 — Feature Cards | 7 | **能力展示（证明价值）** | 不变：3 张卡片的维度保持 声音/文本/分发 |
| 8 | **Mid-Page CTA** 🆕 | — | **第一转化点** | 🆕 在信任建立 + 能力展示完毕后的首个转化请求——此时用户已足够了解，但尚未疲劳 |
| 9 | Ch.04 — Use Cases | 8 | **自我投射（"这是为我做的"）** | 不变：4 张 Persona 卡片 |
| 10 | Ch.05 — HowTo | 9 | **行动指南（降低操作焦虑）** | 不变：3 步 + Tip + JSON-LD |
| 11 | FAQ | 12 | **异议处理（长尾 + SEO）** | 不变：5 个 details/summary |
| 12 | Related Tools（降权） | 11 | **导航出口（仅对未转化用户）** | ⬇️ 从独立区块改为紧凑行内链接（非卡片），降低视觉权重，避免在 CTA 前将用户送走 |
| 13 | Closing CTA | 13 | **最终转化点** | 不变：双按钮 "Try It Free" + "Talk to Sales" |

> **核心变化**：Social proof 从 #10 → #4。Mid-page CTA 新增于 #8。Related Tools 降权为紧凑行。Hero H1 改为 outcome 导向。Education 集成竞争对比。

---

## 三、CTA 三节点策略

高转化 landing page 在三个决策深度各放置一个 CTA——不是重复，而是匹配用户当前的心理阶段。

| 节点 | 位置 | 用户心理 | CTA 文案策略 |
|------|------|------|------|
| **CTA-1** | Hero（区块 2） | 「这能解决我的问题吗？」— 尚未信任 | 低摩擦、零承诺："Translate your first episode — free" / "Upload a file and see it in action" |
| **CTA-2** | Mid-page（区块 8） | 「看起来不错，我能怎么用？」— 已建立信任 | 场景绑定、行动导向："Start translating your [content] now" |
| **CTA-3** | Closing（区块 13） | 「我准备好了」或「还有疑问」— 决策时刻 | 双按钮：主按钮 "Try It Free" + 次按钮 "Talk to Sales"（为犹豫用户提供低风险出口） |

> 原则：不把 "Talk to Sales" 放在前两个 CTA 节点——在用户尚未建立足够信任时看到 sales 联系会增加心理摩擦。

---

## 四、四场景差异化速查

| 维度 | Podcast | Audiobook | E-Learning | Interview |
|------|---------|-----------|------------|-----------|
| **Hero outcome 钩子** | Reach global audiences, in your own voice | Listen to any book, narration preserved | Master any course in your native language | Every speaker labeled, analysis-ready |
| **Trust 数字锚点** | 覆盖播客平台数 / 月处理分钟数 | 支持有声书时长上限（小时） / 支持格式数 | 术语领域数 / 笔记导出格式数 | 说话人识别准确率 / 导出格式数 |
| **Tool Widget 平台** | Spotify, Apple, YouTube, Podbean, RSS, MP3 | MP3/WAV/M4B 上传为主 | MP3/WAV 上传 + 课程 URL | MP3/WAV 上传为主 |
| **Ch.01 竞品对比锚点** | vs 雇佣多语种配音 / vs 纯字幕翻译工具 | vs 多语种有声书录制 / vs 文字→语音工具 | vs 人工笔记翻译 / vs 课程平台内置翻译 | vs 人工转写 / vs 通用转录工具（Maestra 3.5★ Trustpilot） |
| **Ch.02 步骤 2 动词** | Transcribe + speaker diarization | Chapter Detection + transcribe | Transcribe + term recognition | Speaker Diarization + transcribe |
| **Ch.03 能力卡片** | Voice Cloning / Subtitles / Show Notes & SEO | Voice Preservation / Chapter Navigation / Narrative Tone | Term Glossary / Note Export / Slow Playback | Speaker Labels / Bilingual Transcript / Research Export |
| **Ch.04 Persona** | Independent / Media / Educators / Brand | Casual Listeners / Language Learners / Publishers / Accessibility | International Students / Researchers / Online Learners / Institutions | Journalists / HR & Recruiters / Academic Researchers / Market Research |
| **FAQ Q1** | 多平台导入 | 长音频时长限制 | 术语准确率 | 多说话人区分 |
| **情感基调** | 创作者增长、全球发布 | 阅读自由、知识无障碍 | 学术公平、学习无障碍 | 研究严谨、信息完整 |

---

## 五、极简草稿版（v2 重排）

```
┌──────────────────────────────────────┐
│  Home > Audio Translator > [Scenario]│  1. BREADCRUMB
├──────────────────────────────────────┤
│  ⭐ 4.8/5 ([N]+ reviews) · [N]+ [users/│  2. HERO + TRUST
│     hours processed]                  │
│  [X]+ Languages badge                │
│  H1: AI [Scenario] Translator:       │
│      [Outcome Hook]                  │  ← outcome 导向，非功能描述
│  [Subtitle: 价值主张 + 信任一句话]    │
│  [CTA-1: 低摩擦行动]                 │
├──────────────────────────────────────┤
│  [URL paste 或 Upload] [语言选择器]   │  3. TOOL WIDGET
│  [Translate CTA + 隐私标注]          │  + EXAMPLE GALLERY
│  [4-6 热门示例卡片，点选即试]         │
├──────────────────────────────────────┤
│  "What [Persona] Say"                │  4. SOCIAL PROOF ⬆️
│  [2 条具名引言 + 角色/机构]           │  （紧随产品演示——在用户
│  [可选: 1 行客户 logo 条]             │   怀疑"真的有效吗？"时立即回应）
├──────────────────────────────────────┤
│  What is AI [Scenario] Translator?  │  5. CH.01 — EDUCATION
│  [定义→传统方式痛点→AI 如何替代]     │  + WHY UTELL
│  Why Utell vs Traditional Methods:   │  🆕 集成竞争对比
│  [2-3 对比行: 速度/成本/质量]        │
├──────────────────────────────────────┤
│  How Utell AI Translates Your [X].   │  6. CH.02 — PIPELINE
│  [4 steps: Import│Process│Transform   │
│            │Export]                  │
├──────────────────────────────────────┤
│  Everything [Persona] Need to        │  7. CH.03 — FEATURES
│  Go Multilingual.                    │
│  [3 cards: 声音│文本│分发]          │
├──────────────────────────────────────┤
│  ┌────────────────────────────────┐  │  8. MID-PAGE CTA 🆕
│  │ Ready to grow your [audience]?  │  │  （信任+能力展示后首个转化请求）
│  │ [CTA-2: 场景绑定 CTA]           │  │
│  └────────────────────────────────┘  │
├──────────────────────────────────────┤
│  Built for [Persona Group].          │  9. CH.04 — USE CASES
│  [4 cards: Persona 1│2│3│4]         │
├──────────────────────────────────────┤
│  How to [Verb] a [Content]           │  10. CH.05 — HOWTO
│  in Three Steps.                     │
│  01 Upload  02 Translate  03 Export  │
│  [JSON-LD HowTo schema]              │
├──────────────────────────────────────┤
│  FAQ — [5 Q&A: details/summary]      │  11. FAQ
├──────────────────────────────────────┤
│  Also try: Audio Translator ·        │  12. RELATED TOOLS（降权）
│  Accent Converter · Live Translator  │  ← 紧凑行内链接，非独立卡片区块
├──────────────────────────────────────┤
│  Ready when you are.                 │  13. CLOSING CTA
│  [CTA-3: Try It Free] [Talk to Sales]│
└──────────────────────────────────────┘
```

---

## 六、各区块内容规范（v2 优化）

### 6.1 Breadcrumb

```
Home > Audio Translator > [Scenario]
```

- `Home` → `/`（可点击）
- `Audio Translator` → `/audio-translator`（可点击）
- `[Scenario]` → 当前页（不可点击）

### 6.2 Hero + Trust Signals

| 元素 | v2 规范 | v1 对比 |
|------|------|------|
| **Trust Bar** | 🆕 H1 上方一行小字：星级 + 评价数 + 锚点数字。如 `⭐ 4.8/5 (200+ reviews) · 10,000+ hours translated` | v1 无 |
| **Badge** | `[X]+ Languages`（保持不变） | 不变 |
| **H1** | **v2 公式**：`AI [Scenario] Translator: [Outcome — 用户获得的结果，非功能描述]` | v1 为 `[Verb] Any [Content] into [X]+ Languages`（功能导向） |
| **Subtitle** | **v2 公式**：第一句 = 价值主张（1 句）。第二句 = 信任锚点（1 句，如 "Voice-cloned dubbing in under 5 minutes. No credit card."）。**删除** "Built for [persona]"（交给 Ch.04） | v1 为功能罗列 + persona |
| **CTA-1** | 低摩擦、零承诺：「`Translate your first [content] — free`」或「`Upload a [content] and see it in action`」。**不放** "Talk to Sales" | v1 无此约束 |
| **关键词** | H1 前半含 "AI [scenario] translator"（主词），后半含 outcome 长尾（如 "reach global audiences" / "listen in your language"） | 不变 |

**各场景 H1 v2 填充示例**：

| 场景 | v2 H1（outcome 导向） | v1 H1（功能导向） |
|------|------|------|
| Podcast | `AI Podcast Translator: Reach Global Audiences in 50+ Languages, in Your Own Voice` | `Translate Any Episode into 50+ Languages` |
| Audiobook | `AI Audiobook Translator: Listen to Any Book in 50+ Languages, Narration Preserved` | `Listen to Any Audiobook in 50+ Languages` |
| E-Learning | `AI Lecture Translator: Master Any Course in Your Native Language, Terminology Intact` | `Understand Any Course in 50+ Languages` |
| Interview | `AI Interview Translator: Transcribe & Translate Any Conversation, Every Speaker Labeled` | `Transcribe & Translate Any Conversation in 50+ Languages` |

**Trust 数字锚点选择**（按场景选取 1-2 个最相关的）：

| 场景 | 推荐锚点 1 | 推荐锚点 2 |
|------|-----------|-----------|
| Podcast | 覆盖播客平台数 / 月处理集数 | 支持语言数 |
| Audiobook | 支持最长音频时长（小时） | 支持文件格式数 |
| E-Learning | 支持术语领域数 | 导出笔记格式数 |
| Interview | 说话人识别准确率 | 导出分析工具数 |

> 若产品暂无可验证数字，用 `Trusted by creators worldwide` 占位，待数据就绪后替换为具体数字。具体 > 模糊，始终如此。

### 6.3 Tool Widget + Example Gallery（合并）

| 元素 | 规范 |
|------|------|
| **输入方式 1** | URL paste — 平台 icon 列表（场景决定） |
| **输入方式 2** | File upload — MP3/WAV/M4A/FLAC；拖拽或点击 |
| **语言选择器** | 8-12 个热门语言 tag 按钮（点击即选中，无需 dropdown） |
| **热门语言** | Spanish / Mandarin / Hindi / Portuguese / French / German / Japanese / Arabic / Korean / Italian |
| **Translate CTA** | 动态文案：`Translate this [content] into [Language]` |
| **隐私标注行** | `✓ Voice-cloned dubbing  ·  ✓ Multilingual SRT/VTT  ·  ✓ Zero audio retention` |

**Example Gallery**（与 Tool Widget 合并显示——示例卡片紧邻上传区下方）：

- 4-6 张预填充示例卡片（平台 icon + 分类标签 + 内容名 + 创作者名）
- 点击卡片 → 自动填入 URL 字段 + 选中推荐语言
- 反馈行：`Selected: [Content Name] → [Language]` + `Translate this [content] →` CTA
- 分类标签覆盖 2-3 个内容类型（如 Podcast：News / Science / Tech / Business / True Crime / Education）

### 6.4 Social Proof（⬆️ 从 #10 移至 #4）

**位置原则**：紧随产品演示（Tool Widget + Example Gallery）之后，用户刚理解「这个工具能做什么」，紧接着看到「别人怎么评价」——消除「这真的有效吗？」的怀疑。

| 元素 | v2 规范 |
|------|------|
| **H2** | `What [Persona] Say` |
| **引言数量** | 2 条（不多于 2 条——social proof 质量 > 数量） |
| **引言格式** | 引文（1-2 句，自然语气，包含具体结果更佳）+ `— Name, Role / Organization` |
| **好引文标准** | 提及具体场景或结果（"translated my 2-hour interview in 20 minutes" > "this tool is great"） |
| **可选增强** | 若已有知名客户/媒体 logo，在 2 条引言下方加 1 行 logo 条（灰度、小尺寸、不散焦） |

**各场景引文示例方向**：

| 场景 | 引文 1 方向 | 引文 2 方向 |
|------|-----------|-----------|
| Podcast | 播客主评论——「不用重新录制就覆盖了西班牙语听众」 | 媒体机构评论——「每天一集多语言发布，流程无缝」 |
| Audiobook | 语言学习者——「用母语听完了三本英文畅销书」 | 视障读者——「不再受限于单一语言有声书」 |
| E-Learning | 留学生——「终于能完全听懂量子力学课程」 | 教授——「国际学生成绩明显提升」 |
| Interview | 记者——「20 分钟完成了 2 小时访谈的转写+翻译」 | 研究员——「NVivo 直接导入，省了一周的人工转写」 |

> 若无可验证真实引言，宁可留白等待——fake testimonials 对转化的伤害 > 没有 social proof。占位用 `[待客户提供真实引言]`。

### 6.5 Chapter 01 — Education + Why Utell（🆕 集成竞争对比）

| 元素 | v2 规范 |
|------|------|
| **H2** | `What is AI [Scenario] Translator, Exactly?` |
| **段 1** | 定义（1 句）：工具做什么 + 用户得到什么结果。如 "An AI Podcast Translator takes your recorded episode and dubs it into another language — so you reach listeners in 50+ markets without re-recording a single word." |
| **段 2** | 传统方式的痛点（2-3 句）——建立 "before" 画面。雇佣多语种配音员（贵、慢）、纯字幕翻译（失去声音连接）、人工转写（小时→天级） |
| **段 3** | Utell 的解法（1-2 句）——口音优化 + 翻译双引擎；voice cloning 保留声音人格；分钟级产出 vs 天级 |

**🆕 "Why Utell" 子区块**（段 3 之后，2-3 行对比表）：

```
Why Utell vs Traditional Methods:

| vs Hiring multilingual voice talent | vs Transcript-only tools | vs General AI translators |
|------------------------------------|--------------------------|---------------------------|
| Minutes, not days. One voice, 50+ languages. No booking, no retakes. | Your voice, not just text. Listeners connect with a voice, not a document. | Accent-optimized output. Not just translated — clarified. |
```

**设计原则**：
- 对比锚点聚焦「用户已有的替代方案」（不是竞品名——竞品对比留给 FAQ Q5 和配套 Blog）
- 用「vs 传统方法」而非「vs Maestra」——用户心智中的替代方案是「雇人做」「自己不做」「用通用翻译工具」，不是具体竞品名
- Interview 场景例外——Maestra 3.5★ Trustpilot 是已知弱点，可在 FAQ Q5 中针对性对比

### 6.6 Chapter 02 — Pipeline（4 步流程）

**H2**：`How Utell AI Translates Your [Content Type].`

**副标题**：`Four stages, one seamless pipeline — from upload to download in under [N] minutes.`（🆕 加时间承诺）

**4 张步骤卡片**（固定数量）：

| 步骤 | 标题 | 内容要求 |
|------|------|---------|
| **01 — Import** | `Import` | 支持 URL paste + file upload；支持的平台/格式；拖拽即开始 |
| **02 — Process** | `[场景动词]` | Whisper-grade ASR + 场景特定能力（diarization / chapter detection / term recognition / speaker labeling） |
| **03 — Transform** | `Translate & Clone` | 翻译 + voice cloning 重新配音；保留原声语调/节奏/重音 |
| **04 — Output** | `Export` | 下载配音音频（MP3/WAV）、字幕（SRT/VTT）、辅助内容（show notes/transcript/notes） |

> 每张卡片右上角加步骤流向箭头（`→`）连接下一张——视觉上强化「不复杂、自动化」的感知。

### 6.7 Chapter 03 — Feature Cards（3 张能力卡片）

**H2**：`Everything You Need to Go Multilingual.`（🆕 用 "You" 替代 "[Persona]"——直接对用户说话）

**副标题**：`Voice, subtitles, and [aux content] — all translated, all production-ready.`

**3 张卡片**（固定维度：声音 / 文本 / 分发）：

| 场景 | Card 1 — 声音 | Card 2 — 文本 | Card 3 — 分发 |
|------|------|------|------|
| **Podcast** | **Voice Cloning** — Your voice, 50+ languages. Listeners hear you, not a TTS narrator. Tone, pacing, emphasis preserved. | **Subtitles** — SRT & VTT frame-accurate for Spotify Video, YouTube, Apple Podcasts. | **Show Notes & SEO** — Translated descriptions, chapter markers, transcripts. Rank in every market. |
| **Audiobook** | **Voice Preservation** — The narrator's voice in every language. Storytelling tone, character voices, narrative rhythm intact. | **Chapter Navigation** — Auto-detected chapters with translated titles. Jump to any chapter, any language. | **Narrative Tone** — Genre-appropriate tone preserved. Thriller suspense, romance warmth, non-fiction authority. |
| **E-Learning** | **Term Glossary** — Domain terminology recognized and accurately translated. STEM, medical, legal, humanities. | **Study Notes Export** — Translated transcripts as study-ready notes. Key concepts highlighted, timestamps preserved. | **Slow Playback** — Language learners slow down translated audio without pitch distortion. |
| **Interview** | **Speaker Labels** — Automatic diarization with names. Every line attributed to the right person in both languages. | **Bilingual Transcript** — Side-by-side original + translation view. Ideal for qualitative coding. | **Research Export** — NVivo, ATLAS.ti, MAXQDA formats. Timestamp-aligned for analysis. |

> 卡片设计原则：每张 = icon + 粗体标题（1 个短语）+ 2-3 句正文。正文第一句给出具体结果，不是功能名称。

### 6.8 Mid-Page CTA 🆕

**这是首个高意图转化请求**——用户已看到：工具演示（区块 3）→ 他人验证（区块 4）→ 为什么选我们（区块 5）→ 它是如何工作的（区块 6）→ 能做什么（区块 7）。现在是询问行动的最佳时刻。

| 元素 | 规范 |
|------|------|
| **形式** | 横幅（banner），非整屏区块——视觉上比其他区块窄，但比普通分隔线醒目 |
| **H2** | 场景绑定钩子。如 `Ready to grow your [podcast audience / listener base / student reach / research efficiency]?` |
| **Subtitle** | 1 句催促 + 风险消除。如 `Translate your first [content] in under 5 minutes. No credit card.` |
| **CTA 按钮** | `Start Translating Now` 或 `Translate Your First [Content]` |
| **不放** | 不放 "Talk to Sales"——此阶段用户已足够信任，给 sales 选项只会制造犹豫 |

> 若页面高度较短（移动端常见），此 CTA 可选——英雄区 CTA + 底部 CTA 足够。判断标准：若用户需滚动 3+ 屏才能到达 Closing CTA，则必须加 Mid-Page CTA。

### 6.9 Chapter 04 — Use Cases（4 张 Persona 卡片）

**H2**：`Built for [Persona Group].`

| 场景 | Persona 1 | Persona 2 | Persona 3 | Persona 4 |
|------|-----------|-----------|-----------|-----------|
| **Podcast** | 🎙️ Independent Podcasters | 📰 Media & News Networks | 🎓 Educators & Researchers | 🏢 Brand & Corporate Shows |
| **Audiobook** | 📚 Casual Listeners | 🗣️ Language Learners | 📖 Publishers & Authors | ♿ Accessibility |
| **E-Learning** | 🎓 International Students | 🔬 Academic Researchers | 🎥 Online Course Creators | 🏛️ University Administrators |
| **Interview** | 📰 Journalists & Reporters | 👔 HR & Recruiters | 🔬 Academic Researchers | 📊 Market Research Firms |

**每张卡片格式**：Icon + Persona 名称 + 2-3 句（痛点 → 解法 → 结果）。终句给具体结果，非泛化承诺。

示例（Podcast / Independent Podcasters）：
> **🎙️ Independent Podcasters**
> You built an audience in one language — now reach the next. Utell dubs your episodes in 50+ languages while keeping your voice, so Spanish and Hindi listeners hear *you*, not an AI narrator. One upload, one export, publish everywhere.

### 6.10 Chapter 05 — HowTo（3 步操作指南）

**H2**：`How to [Verb] a [Content Type] in Three Steps.`

| 步骤 | 标题 | 正文要求 | Tip |
|------|------|---------|-----|
| **01** | `[Action 1]` | 输入方式（paste URL / upload file）、支持格式 | 最佳实践（如 "For best results, use clear audio under 3 hours."） |
| **02** | `Choose your target language` | 从 50+ 语言中选择、一键启动翻译 | 推荐常用组合（EN→ES、EN→HI） |
| **03** | `Download & publish` | 下载配音音频 + 字幕 + 辅助内容；Credits 说明 | 发布平台建议（Spotify SRT、YouTube 字幕） |

> **JSON-LD HowTo schema 强制嵌入**——此区块的 SEO 价值不亚于内容价值。

### 6.11 FAQ

**H2**：`[Scenario] Translator FAQ`

**5 个问答**（使用 `<details>/<summary>` HTML——Bing 可抓取，同时减少页面视觉高度）：

| # | 通用公式 | 覆盖长尾 |
|---|------|------|
| **Q1** | "How do I translate a [content]?" — 3 步流程概述 | `how to translate [content]` / `[content] translator tool` |
| **Q2** | "Can AI translate a [content] while keeping my/the original voice?" — Voice cloning 说明 | `AI [content] dubbing with my voice` / `voice cloning translation` |
| **Q3** | "What languages can I translate my [content] into?" — 语言数 + 热门语言列举 | `translate [content] to [language]` / `[content] multilingual` |
| **Q4** | "Which platforms / file formats can I import from?" — 输入源与格式列表 | `[content] translator from [platform]` / `supported formats` |
| **Q5** | "How is this different from [alternative approach / competitor]?" — 对比锚点 | `best [content] translator` / `[tool] vs [competitor]` |

> Q5 场景差异化：
> - Podcast：vs 雇佣配音员 / vs 纯字幕工具
> - Audiobook：vs 多语种录制 / vs BookNPC（文字→语音）
> - E-Learning：vs 课程平台内置翻译 / vs 人工笔记翻译
> - **Interview**：vs 人工转写服务 / **vs Maestra（3.5★ Trustpilot——唯一可在 FAQ 中点名的竞品）**

### 6.12 Related Tools（🆕 降权为紧凑行）

**v2 重大变化**：v1 将 Related Tools 作为独立卡片区块（#11），在 Closing CTA 之前将用户导向其他页面——转化自杀。v2 降权为 FAQ 与 Closing CTA 之间的 **1 行紧凑链接**，视觉权重大幅度降低。

```
Also try: Audio Translator · Accent Converter (<100ms real-time) · Live Translator
```

- 纯文本行，`·` 分隔，无卡片、无图片、无描述段落
- 每个工具名 = 可点击链接
- Accent Converter 必须标注 `<100ms real-time`（帮助区分实时 vs 后制）
- 此行目的仅剩：SEO 交叉内链 + 为明确不需要本页的用户提供快速出口

### 6.13 Closing CTA

| 元素 | v2 规范 |
|------|------|
| **H2** | `Ready when you are.`（不变） |
| **Subtitle** | `Translate your first [content] — free.` + 1 句风险消除承诺（`No credit card. No setup. Voice-cloned dub in under 5 minutes.`） |
| **CTA 按钮 1（主）** | `Try It Free` — 指向页面顶部 Tool Widget 锚点 `#` |
| **CTA 按钮 2（次）** | `Talk to Sales` — `mailto:sales@utell.ai`。视觉上比主按钮弱一个层级（outline / 文字链接） |
| **微文案** | CTA 按钮下方 1 行 10px 小字：`✓ No credit card  ·  ✓ 5-minute setup  ·  ✓ Zero audio retention` |

---

## 七、SEO 检查清单

### 7.1 关键词矩阵

| 层级 | 关键词类型 | 示例（Podcast） | 投放位置 |
|------|-----------|----------------|---------|
| **主词** | `AI [scenario] translator` | `AI podcast translator` | H1 冒号前、breadcrumb、meta title |
| **变体 1** | `translate [content] to [language]` | `translate podcast to Spanish` | subtitle、Ch.01、FAQ Q3 |
| **变体 2** | `[scenario] dubbing AI` | `AI podcast dubbing` | Ch.02 步骤 3、Ch.03 Card 1 |
| **变体 3** | `[scenario] transcription + translation` | `podcast transcription and translation` | Ch.02 步骤 2、FAQ Q1 |
| **长尾** | `how to translate [content] with AI` | `how to translate a podcast with AI` | FAQ Q1/Q5、配套 Blog |

### 7.2 Title Tag vs H1 vs Meta Description

| 元素 | 内容 | 字符数 |
|------|------|--------|
| **Title Tag** | `AI [Scenario] Translator — [Outcome Hook in 5-7 words] \| Utell AI` | 50-60 |
| **H1** | `AI [Scenario] Translator: [Outcome Hook]` | 50-70 |
| **Meta Description** | `[Outcome first — 1 句价值]. Utell AI dubs your [content] in your own voice, with subtitles and translated [aux]. Free, no credit card, under 5 minutes.` | 140-155 |

### 7.3 FAQ 长尾关键词映射

| FAQ | 覆盖长尾 |
|-----|---------|
| Q1 | `how to translate [content]` / `[content] translator tool` |
| Q2 | `AI [content] dubbing with my voice` / `voice cloning translation` |
| Q3 | `translate [content] to [language]` / `[content] multilingual` |
| Q4 | `[content] translator from [platform]` / `translate Spotify podcast` |
| Q5 | `best [content] translator` / `AI translator vs [alternative]` |

---

## 八、移动端注意事项

| 要点 | 说明 |
|------|------|
| **Tool Widget 优先文件上传** | URL paste 在移动端体验差（需切换 App 复制链接）。移动端 UI 应优先展示 `Upload MP3` 按钮，URL paste 折叠为次要选项 |
| **Example Gallery 横向滚动** | 4-6 张卡片在移动端采用横向 `overflow-x: scroll`，不换行堆叠 |
| **Mid-Page CTA 可选** | 移动端页面高度自然较短——若 Hero + Tool Widget + Social Proof + Features 在 3 屏以内到达 Closing CTA，可省略 Mid-Page CTA |
| **FAQ 用 details/summary** | 默认折叠——5 个全展开 FAQ 在移动端可占 3-4 屏。用户只展开关心的那个 |
| **Closing CTA 双按钮垂直排列** | "Talk to Sales" 在移动端不应与主按钮抢视觉优先级——主按钮在上、次按钮在下（outline style） |

---

## 九、场景一致性检查清单

| # | 检查项 | 标准 |
|---|--------|------|
| ① | H1 句式 | `AI [Scenario] Translator: [Outcome Hook]` —— 冒号前 = SEO 主词，冒号后 = 用户结果 |
| ② | Hero 含 trust 锚点 | H1 上方必须有数字锚点行（星级/用户数/处理量——至少 1 个具体数字） |
| ③ | Tool Widget 示例 ≥ 4 张 | 至少 4 张热门内容卡片，覆盖 2+ 内容分类 |
| ④ | Social Proof 在 #4 | 紧随 Tool Widget，不可后于 Ch.01 |
| ⑤ | Ch.01 含 "Why Utell" 对比 | 必须含 2-3 行对比表（vs 传统方法） |
| ⑥ | Ch.02 4 步流程 | Import → [Process] → Translate & Clone → Export（卡片间有流向箭头） |
| ⑦ | Ch.03 恰好 3 张卡片 | 声音 / 文本 / 分发 三维度，不可增减 |
| ⑧ | Mid-Page CTA 存在 | 桌面端必须（移动端若总高度 < 3 屏可省略） |
| ⑨ | Ch.04 恰好 4 张 Persona | 每张有 emoji icon + 具体结果描述 |
| ⑩ | Ch.05 嵌入 JSON-LD | HowTo schema 必须存在 |
| ⑪ | FAQ 5 个 details/summary | 默认折叠；Q5 含竞品/替代方案对比 |
| ⑫ | Related Tools 为 1 行紧凑链接 | 非卡片、非独立区块、无描述段落 |
| ⑬ | CTA-1 不放 "Talk to Sales" | Hero 的 CTA 只放低摩擦行动文案 |
| ⑭ | CTA-3 双按钮层级分明 | 主按钮 solid / 次按钮 outline；次按钮在移动端位于主按钮下方 |
| ⑮ | slug 格式 | `/audio-translator/[kebab-case]` |
| ⑯ | Breadcrumb 可点击 | `Home` 和 `Audio Translator` 为链接，当前页不可点击 |

---

## 十、模板使用流程

1. **确定场景** → 查 [scenarios](./audio-translator-scenarios.md) 优先级
2. **确定 slug** → `audio-translator/[slug]`，kebab-case
3. **复制 §五 极简草稿版** → 粘贴为工作草稿
4. **填充 Trust 数字** → 与产品团队确认可用数字锚点（无数据则用 "Trusted by creators worldwide" 占位）
5. **按 §六 逐区块填充** → H1（outcome 导向）、subtitle、Ch.01 对比表、Ch.02 步骤动词、Ch.03 三卡片、Ch.04 四 Persona、Ch.05 三步骤、FAQ
6. **写配套 Blog** → 覆盖 "how to translate [content] with AI" 等长尾
7. **SEO 检查** → 按 §七 逐项核对
8. **交叉内链** → Related Tools 行含 Audio Translator / Accent Converter / Live Translator
9. **移动端 QA** → 检查 Tool Widget（优先文件上传）、卡片横向滚动、FAQ 折叠

---

## 站内关联

[场景规划](./audio-translator-scenarios.md) · [产品文档](./audio-translator.md) · [站面结构](../utell-site-structure.md) · [关键词映射](../utell-keywords.md) · [增长策略](../utell-growth-strategy.md)

---

*v2 — 基于 landing page 转化最佳实践的重构。Social Proof 前移 (#10→#4)、Mid-Page CTA 新增 (#8)、Hero 改为 outcome 导向、Related Tools 降权为紧凑行、Education 集成异议处理。*
