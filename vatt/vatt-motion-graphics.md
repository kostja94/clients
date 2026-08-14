# Vatt — Motion Graphics（动效 / 包装）

> **职责**：Vatt 全部 Motion Graphics 能力的唯一维护文档（Feature · Status · 口语映射 · 缺口）。非 MG → [vatt-features.md](./vatt-features.md)。  
> Status：Current / Conditional / Opportunity 同 [vatt-features.md](./vatt-features.md#feature-status-说明)；**Gap** 为本文件专用（行业常见、产品尚未单列，不得写成已上线）。不对用户暴露 HyperFrames、Remotion、PAG 等实现框架。

**Last updated**: 2026-08-05

---

## 1. 产品定义（对外）

**英文**

> Vatt adds motion graphics on an editable timeline — layouts, captions, word art, stickers, intros, and emotion-driven visual emphasis — without locking your edit into a black-box render.

**中文**

> Vatt 在可编辑时间线上提供动效与包装：布局、字幕、花字、贴纸、片头片尾、情绪强化等；所有效果均为可调时间线对象。

MG 出现在 **粗剪与高光确定之后**；不是 beachhead 核心（理解素材 + 真实剪辑 + 可编辑时间线才是），但是创作者出片时 **高频使用**。

---

## 2. MG 能力分类

### 2.0 行业类型总表（In / Out）

Reaction / 短视频剪辑场景下的 MG 谱系。In = 本文件维护；Out = 不扩展为 Feature 表。

| # | 行业类型 | 范围 | 展开节 |
|---|----------|------|--------|
| 1 | Multi-cam / Reaction Layout（PIP、分屏、切镜） | **In** | §2.1 |
| 2 | Emphasis Motion（punch-in、shake、freeze、break-frame） | **In** | §2.2 |
| 3 | Captions / Kinetic Typography | **In** | §2.3 |
| 4 | Word Art / Meme Text | **In** | §2.3 |
| 5 | Lower Thirds / Nameplates / Context Labels | **In** | §2.4 |
| 6 | Titles / Openers / End Cards | **In** | §2.4 |
| 7 | Stickers / Emoji / Callouts | **In** | §2.5 |
| 8 | Comment / Quote / Social Cards | **In** | §2.4 |
| 9 | Transitions（hard cut 为主 + 轻量包装转场） | **In** | §2.6 |
| 10 | Overlays / Atmospheric FX | **In** | §2.7 |
| 11 | MG-paired SFX（非音频工程） | **In** | §2.8 |
| 12 | Platform Safe-Zone Packaging | **In** | §2.9 |
| 13 | Style Packs（横切：字幕 + 贴纸 + 叠加统一风格） | **In** | §2.3 · §2.10 |
| 14 | Logo / Brand Bug / Watermark | **Border** | §2.9 |
| 15 | Progress / Chapter / Countdown bars | **Border** | §4 |
| 16 | Masks / Shape reveals（作转场子集） | **Border** | §2.6 |
| 17 | Filters / Color Looks | **Out** | 调色，非 MG 主类 |
| 18 | Particles / Full VFX compositing | **Out** | — |
| 19 | Infographics / Charts / Maps / Code viz | **Out** | — |
| 20 | Explainer / UI demo / Broadcast package | **Out** | 非 beachhead |

---

### 2.1 画面布局（Layout）

Reaction 场景下「原片 + Face-Cam 怎么同时出现」——图层 transform + 时间线 clip。

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 小窗、画中画、PIP、corner cam | Picture-in-Picture Layout | Current |
| 原片大图、我在角落 | Source-First Layout | Current |
| 切到我大图、我讲的时候全屏 | Creator-First Layout | Current |
| 左右分屏、双画面 | Side-by-Side Layout | Current |
| 上下分屏 | Horizontal Split Screen | Current |
| 竖屏上下堆叠、Shorts 双画面 | Vertical Split / Stacked Layout | Current |
| 多人网格 | Grid Layout | Current |
| 全屏切原片 / 全屏切我 | Cut-Away Switching | Current |
| 自动换布局、谁说话谁大 | Smart Layout Switching | Conditional |
| 每次换布局能在时间线上改 | Layout Timeline Clips | Current |
| 小窗别挡字幕 / 人脸 | Face-Cam Auto Positioning | Opportunity |
| 抠图融入背景 | Immersive Cutout Layout | Opportunity |
| 竖屏裁切别挡脸 | Layout-Aware Resizing | Opportunity |
| 字幕区域预留 | Safe Caption Zones | Opportunity |
| 不放原片、只看我 + 时间参照 | Watch-Along Layout | Opportunity |

**摘要能力名（对外 / SEO）**：Smart Reaction Layout — PIP / Split / Stacked 等可编辑布局，可按说话与强反应自动切换。

---

### 2.2 情绪与镜头强化（Emphasis）

强反应时刻用缩放、平移、震动引导注意力；原则：正确时刻、合适强度。

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 放大脸、怼脸、反应特写 | Reaction Close-Up | Current |
| 推镜头、拉近、Ken Burns | Pan and Zoom | Current |
| 抖一下、震屏、冲击感 | Shake Emphasis | Current |
| 强反应停一下加字 | Reaction Freeze Frame | Opportunity |
| 人跳出画框 | Break-the-Frame Effect | Conditional |
| 卡通变身、 meme 效果 | Cartoon or Character Transformation | Conditional |
| AI 帮我在对的时间加 | Emotion-Aware Effect Suggestions | Conditional |
| 强度可调（轻/中/强） | Intensity Control | Current |
| 创意视觉增强 | ReAmp Creative Enhancement | Conditional |
| 效果对齐情绪峰值 | Effect Timing Suggestions | Conditional |

**摘要能力名**：Emotion Amplification / ReAmp

---

### 2.3 字幕与字体动效（Captions & Typography）

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 自动加字幕 | Automatic Captions | Conditional |
| 改字幕时间、位置、样式 | Editable Captions | Current |
| 字幕会动、TikTok captions、逐词亮 | Animated Captions | Current |
| 重点词变大变色 | Keyword Emphasis | Opportunity |
| 弹出大字、花字、meme text | Reaction Word Art | Current |
| Karaoke 高亮跟读 | Karaoke Caption Style | Opportunity |
| 弹跳 / pop 字幕 | Pop / Bounce Caption Style | Opportunity |
| 砸字、kinetic slam | Kinetic Slam Caption Style | Opportunity |
| 打字机字幕 | Typewriter Caption Style | Gap |
| 干净极简字幕 | Minimal Caption Style | Opportunity |
| Neon / 发光字幕 | Neon Caption Style | Gap |
| Emoji 跟着字弹出 | Emoji Pop Caption Style | Opportunity |
| 一键统一这期字幕风格 | Style Packs（Captions） | Conditional |

字幕风格不对用户区分 PAG / Lottie / ASS 等技术来源；统一归 Animated Captions / Style Packs。

---

### 2.4 标题、信息卡与片头片尾（Titles & Cards）

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 标题条、角标、lower third | Lower Thirds | Conditional |
| 这集讲什么、人物介绍卡 | Source Labels and Context Cards | Opportunity |
| 评论截图做成卡片 | Comment Cards | Opportunity |
| 引用金句卡、quote card | Quote Cards | Opportunity |
| 静帧、角色卡替代原片画面 | Still-Frame / Context-Card Substitution | Opportunity |
| 片头片尾、开场动画 | Intro and Outro Graphics | Opportunity |
| 开场高能 montage | Reaction Teaser Montage | Conditional |
| 介绍这期看什么 | Intro Builder | Opportunity |
| 片尾关注 / 订阅引导（视觉） | End Card / Subscribe CTA Graphics | Opportunity |
| Social follow 卡（关注三件套） | Social Follow Cards | Gap |

---

### 2.5 贴纸与标注（Stickers & Callouts）

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 贴 emoji、频道贴纸 | Custom Stickers | Current |
| 箭头指这里、圈一下重点 | Arrow / Circle Callouts | Opportunity |
| 形状强调、色块衬字 | Shape Accents | Gap |
| 边框、相框装饰 | Frame Overlays | Gap |

---

### 2.6 转场（Transition）

Reaction 成片以 **hard cut + 节奏** 为主；包装转场作可选，建议全片 2–3 处关键 moment。

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 硬切、直接切 | Hard Cut（默认） | Current |
| 淡入淡出、交叉淡化 | Crossfade | Current |
| 闪黑 / 闪白 | Dip to Black / White | Gap |
| 甩镜头、快速划过 | Whip Pan | Gap |
| 推拉转场、zoom transition | Zoom Punch Transition | Gap |
| 滑入滑出、擦除 | Slide / Wipe | Gap |
| 故障闪一下 | Glitch Transition | Gap |
| 闪一下白帧接下一镜 | Flash Frame Transition | Gap |
| 光圈、遮罩擦除 | Mask / Luma Wipe | Gap |

---

### 2.7 画面质感叠加（Overlay）

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 老电影颗粒、film grain | Grain Overlay | Gap |
| 边缘暗一点 | Vignette | Gap |
| 闪一下光、漏光 | Light Leak | Gap |
| 胶片灼烧、film burn | Film Burn | Gap |
| 闪白帧叠加 | Flash Frame Overlay | Gap |
| RGB 分离、色差 | RGB Split / Chromatic Aberration | Gap |
| 扫光、shimmer | Shimmer Sweep | Gap |
| 柔光、glow | Soft Glow | Gap |
| 瞬间模糊强调 | Blur Punch | Gap |
| 漫画速度线 | Speed Lines（Meme） | Opportunity |

---

### 2.8 配套音效（MG 配对）

与视觉 MG 成对出现；纯音频工程（Ducking、降噪、响度）→ [vatt-features.md §3.8 Audio](./vatt-features.md#38-audio-music--sound-design音频工程)。

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 高能加 impact / whoosh | Reaction Sound Effects | Conditional |
| 按反应类型推荐音效 | Emotion-Aware SFX Suggestions | Opportunity |
| 转场前后声音淡入淡出 | Audio Fade Controls | Current |

---

### 2.9 平台包装（Delivery）

画幅、导出预设等非 MG 交付能力 → [vatt-features.md §3.10 Platform](./vatt-features.md#310-platform-adaptation--delivery平台适配与导出)。

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 字幕别被平台按钮挡住 | Platform-Specific Caption Layout | Opportunity |
| 片尾引导订阅评论 | Platform-Specific Outro · Platform-Specific CTA | Opportunity |
| 角标 Logo、频道 bug | Brand Bug / Watermark | Gap |

---

### 2.10 横切：Style Packs

| 用户可能说 | Feature | Status |
|-----------|---------|--------|
| 一键统一这期风格（字幕+贴纸+叠加） | Style Packs | Conditional |

Style Packs 绑定 §2.3–§2.7 的模板组合；**不得**宣传为版权或平台合规保证。

---

## 3. MG 优先级

| Tier | 定位 | 能力 |
|------|------|------|
| **Tier 1** | Reaction 核心包装 | Smart Layout · Layout clips · Close-Up · Pan/Zoom · Shake · Editable captions · Word Art |
| **Tier 2** | 完成工作流 | Animated Captions · Lower Thirds · Style Packs · Stickers · ReAmp · Reaction SFX · Intro/Outro |
| **Tier 3** | 扩展方向 | 创意转场库 · Overlay 质感库 · 字幕风格矩阵 · Comment/Quote/Social Cards · Callouts |

与 [vatt-features.md](./vatt-features.md) Beachhead Stack：features Tier 1 为剪辑与智能；MG Tier 1 为其上的视觉包装子集。

---

## 4. 能力缺口与范围外

| 项 | 归入 | 说明 |
|----|------|------|
| 转场库（除 Hard Cut / Crossfade） | §2.6 Gap | 行业编辑器标配 |
| Overlay 质感库 | §2.7 Gap | 颗粒 / 暗角 / 漏光等 |
| 字幕风格矩阵 | §2.3 Opportunity/Gap | Karaoke / Pop / Slam / Typewriter / Neon… |
| Social Follow Cards | §2.4 Gap | Tier 3；非 beachhead |
| Progress / Chapter / Countdown bars | Border | 教育/长评赛道有用；未单列 Feature |
| Brand Bug | §2.9 Gap | Border→可进 Delivery |
| 数据图表 / 代码动画 / 地图 viz | **Out** | 不在 Vatt MG 范围 |
| Particles / Full VFX / Explainer / Broadcast | **Out** | 不在 Vatt MG 范围 |

素材理解、同步、粗剪、反应检测、时间线机制、版权工作流、评论数据层 → [vatt-features.md](./vatt-features.md)。

---

## 5. 约束与引用

**Claims（并遵守 [vatt-features.md §5](./vatt-features.md)）**

- 不得承诺「一键完美成片」「100% 情绪识别准确」
- 不得将 Style Packs / 转场宣传为版权或平台合规保证
- 对用户勿宣传：Video-as-Code、AE 级无限合成、版权规避类「特效」

| 文档 | 用途 |
|------|------|
| [vatt-keywords.md](./vatt-keywords.md) | SEO：`animated captions`、`reaction video effects` |
| [vatt-use-cases.md](./vatt-use-cases.md) | Persona「要多加字幕和特效」 |
| [vatt-reaction-video-types.md](./vatt-reaction-video-types.md) | 各赛道 Must-Have 中的 captions / layouts / SFX |
