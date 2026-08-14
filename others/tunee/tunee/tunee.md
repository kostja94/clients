# Tunee - Product Marketing Context

> 基于官网 [tunee.ai](https://www.tunee.ai/)  
> 复制到 `.cursor/product-marketing-context.md` 或 `.claude/product-marketing-context.md` 供 AI Agent 使用。

**Last updated**: 2025-03-02

**文档体系**：各子文档内容一致且独立——每份文档聚焦自身主题、可单独使用，跨主题内容通过互相引用获取，避免重复。详见文末「文档关联总览」。

---

## 0. 文档与报告语言策略（实施规则）

**原则**：主站以英文为主；本文档及子文档面向中文读者，用于内部沟通与决策。

| 场景 | 语言 | 说明 |
|------|------|------|
| **网站内容** | 英文为主 | tunee.ai 主站、落地页、FAQ |
| **文档/报告** | 中文为主 | 策略、分析、解释、待办、洞察——给中国人看 |
| **产品原文** | 英文 | 定位、slogan、key messages、官网文案——保留原文便于对照 |
| **技术/SEO** | 英文 | URL、关键词、平台名——与网站一致 |

**文档内规则**：产品名、功能名、URL、关键词、竞品名用英文；策略说明、分析、待办、洞察用中文。

---

## 1. Product Overview

**One-line description**:
```
Tunee is the smartest AI music agent—chat with me to create music. No complex prompting, no music theory required. Describe your mood, upload a melody, or share a reference—Tunee understands and brings your musical ideas to life through natural conversation.
```

**Category**: B2C / AI Music / Music Creation Agent / Generative Music  
**Business model**: Freemium（免费试用 + Basic/Plus/Pro 订阅）  
**Pricing**: 免费（有限 credits、非商用需署名）；Basic $18/月；Plus $38/月；Pro $89/月

**产品形态**：
- **Web App**：tunee.ai（在线对话式创作）
- **入口**：/sign-in（登录）、Create with Tunee（创作）
- **社区**：Discord

**核心功能**：
- **AI Music Agent**：对话式音乐创作，无需复杂 prompt、无需乐理
- **多模态输入**：文字描述、上传旋律、参考音频、视频片段
- **MV 视频生成**：音乐→AI 生成 MV，支持 Narrative、Performance、Conceptual、Lyric、Studio 等流行风格；另支持 Vinyl Visualizer、Canvas 等简单音乐视觉
- **全流程服务**：音乐生成、MV 制作、智能母带、Stem 分离
- **多模型**：Mureka O2/V7.6/V7.5、MiniMax Music 2.0、TemPolor V4.5 Beta

**技术架构**：基于 DIFY 的多 Agent 架构。**AI 模型**：音乐（Mureka O2/V7.6/V7.5、MiniMax Music 2.0、TemPolor V4.5 Beta）；MV（MidJourney V7、Kling V2.1/V2.6/O1/Avatar 2.0、Dreamina V3、Seedream 4.5、Seedance 1.5 Pro、Nano Banana Pro、InfiniteTalk）；Motion Control（MotionGen Pro、Kling Motion、Seedance 2.0、DynamicAI、FlowMaster、KineticVision）；语言（Claude 4、Qwen 3）。详见 [tunee-features.md](./tunee-features.md) 第四节

**数据规模**：免费 ~500 日刷新 credits、~40 首/月；Basic ~200 首/月；Plus ~420 首/月；Pro ~1,100 首/月

---

## 2. Positioning Statement

> **For** music producers, content creators, filmmakers, game developers, and music lovers **who** want to create custom music without learning complex tools or music theory, **our** Tunee **is the** smartest AI music agent **that** works through natural conversation—describe your mood, upload a reference, or share a video clip, and Tunee brings your musical ideas to life. **Unlike** traditional AI music tools that require complex prompting, **we** deliver creative dialogue that leads to great music **because** we're built as your creative music partner—remembering your style, learning your patterns, and suggesting directions you might not have considered.

---

## 3. Value Proposition & Key Messages

- **Primary value prop**：**对话式 AI 音乐创作**——无需 prompt 技巧、无需乐理，像和制作人聊天一样创作音乐。
- **Key messages**:
  - "The smartest AI music agent - chat with me to create music."
  - "Get your music done, with doing nothing more."
  - "We're not just generating music—we're having a creative dialogue about your vision."
  - "Music is for everyone, and so is Tunee."
- **Proof points**：多模型（Mureka、MiniMax、TemPolor）；MV 制作、Stem 分离、智能母带；付费计划全商用授权；客户故事（PETRA、柠小檬Max、Rivi Nyx、电影节合作）

---

## 4. Target Audience / ICP

**Primary ICP**:
- **Who**：音乐制作人、内容创作者、电影制作人、游戏开发者、音乐爱好者（无乐理基础）
- **Industry**：音乐、影视、广告、游戏、短视频、社交
- **Jobs to be done**：快速创作定制音乐、广告配乐、游戏 BGM、MV 制作、灵感探索
- **Pain points**：传统 AI 音乐工具需复杂 prompt；乐理门槛高；版权/商用授权不清晰
- **Buying triggers**：需要商用授权、需要长轨、需要 MV、需要多风格

**Secondary ICP**：独立艺术家、残障创作者、品牌方（慈善/环保主题）

**Use Case Personas**（产品线对应）：详见 [tunee-use-cases.md](./tunee-use-cases.md)

**Language / locale**：英文为主（tunee.ai）；客户故事含中英双语

---

## 5. Existing Website

- **URL**: https://www.tunee.ai/
- **Key pages**: /（首页）、/music-agent（Music Agent）、/virtual-artist（Virtual Artist）、/features（功能中心）、/features/music-video-generator、/features/lip-sync、/features/ai-dancing、/features/motion-control、/faq（FAQ）、/customer-stories（客户故事）
- **Resources**：About Us、Customer Stories、Terms of Use、Privacy Policy、Feedback、FAQ
- **Tech stack**: Web App、多 Agent 架构（DIFY）、多 AI 模型
- **Current state**: 增长期；强调 AI music agent、对话式创作、royalty-free、商用授权

*功能详情见 [tunee-features.md](./tunee-features.md)*

---

## 6. Keywords

> **核心词**：**AI music agent**、**AI music maker** 均为核心关键词。详见 [tunee-features.md](./tunee-features.md)、[tunee-keywords.md](./tunee-keywords.md)

| Type | Examples |
|------|----------|
| **Primary A** | AI music agent, AI music maker, music creation assistant |
| **Primary B** | AI music generator, royalty-free AI music, AI song generator |
| **Secondary** | AI music for ads, AI game music, AI BGM, mood to song |
| **Long-tail** | best AI music agent 2025, AI music agent for beginners |
| **Use case** | AI music for content creators, AI music for game developers |
| **竞品** | Suno alternative, Udio alternative, Tunee vs Suno |
| **Target intent** | Commercial（工具选型）、Transactional（注册/订阅） |

*完整映射见 [tunee-keywords.md](./tunee-keywords.md)；功能页见 [tunee-features.md](./tunee-features.md)；Use Cases 见 [tunee-use-cases.md](./tunee-use-cases.md)*

---

## 7. Competitors

- **主要竞品（AI music agent 同赛道）**：**Producer**（[producer.ai](https://www.producer.ai/)）、**MixAudio**（[agent.mix.audio](https://agent.mix.audio/)）
- **AI 音乐生成竞品**：**Suno**、**Udio**、**Mureka**（[mureka.ai](https://www.mureka.ai/)）、**Wondera**（[wondera.ai](https://www.wondera.ai/)）；**TemPolor** 已停止运营，Tunee 仍使用其 V4.5 Beta 作为模型之一
- **Alternatives**: 传统音乐制作软件、版权音乐库、雇佣制作人
- **Differentiation**: Tunee 以 **AI music agent** 定位——对话式、无需 prompt、多 Agent 全流程（音乐+MV+母带+Stem）；多模型（Mureka、MiniMax、TemPolor）可选；付费计划全商用授权
- **Gaps to exploit**: AI music agent、Producer alternative、Suno alternative、Udio alternative

*详细分析见 [tunee-competitors.md](./tunee-competitors.md)*

---

## 8. Brand & Voice

- **Voice**: 友好、创意伙伴感、易用、包容（Music is for everyone）
- **Tone**: 强调「chat」「conversation」「creative dialogue」「no music theory」
- **Avoid**: 过度技术化、冷冰冰的 B2B 语气
- **Preferred terms**: "AI music agent"、"chat"、"create"、"conversation"、"music partner"

---

## 9. Product Documentation

- **Path or link**: 官网、[FAQ](https://www.tunee.ai/faq)、[Customer Stories](https://www.tunee.ai/customer-stories)
- **Key features**：
  - **Music Agent**（/music-agent）：对话式创作、多模态输入、风格记忆
  - **Virtual Artist**（/virtual-artist）：AI 虚拟歌手、Lip Sync、AI Dancing、Motion Control
  - **Music Video Generator**（/features/music-video-generator）：2–5 分钟生成、最高 60s、4K 输出
  - **音乐生成**：Mureka、MiniMax、TemPolor 多模型
  - **智能母带**：Smart Mastering
  - **Stem 分离**：2/4/6 轨分离
  - **Use Cases**：Mood to song、Imitation、Reimagine、Ads、Game BGM 等

*详见 [tunee-features.md](./tunee-features.md)*

---

## 10. Other Context

- **Strategy**: 以 AI music agent 差异化；Freemium 获客；对话式创作降低门槛；客户故事、电影节合作背书
- **Timeline**: 持续迭代模型、MV、Stem、音效等能力
- **Constraints**: 定价以官网为准；AI 音乐版权法仍在演进

**SEO / GEO 待办**：AI music agent、AI music maker 核心词布局；Use Cases 页（Music Creation、Ads、Game）覆盖场景长尾；Suno/Udio alternative 对比页；FAQ 结构化便于 AI 引用；**Music Generator 程序化 SEO** 见 [tunee-music-generator.md](./tunee-music-generator.md)。

---

## 11. Content / Blog / Article Strategy

**Product connection**:
- 文章围绕 AI 音乐创作、对话式音乐、商用音乐、游戏 BGM、广告配乐
- 自然提及 Tunee 作为 AI music agent 解决方案
- 避免纯通用内容、无产品关联

**Keyword basis**: 使用 Section 6 及 [tunee-keywords.md](./tunee-keywords.md) 作为文章主题与目标词

**内容主题**：AI music agent 入门、mood to song、游戏 BGM 创作、广告音乐、版权音乐、Suno vs Tunee

---

## 12. Use Cases & Platform Pages

**严格区分**：Use Cases = **谁**在**什么情境**下用；Features = 产品**能做什么**。

| 类型 | 维度 | 页面 | 目标关键词 |
|------|------|------|------------|
| **Use Cases** | 场景 | Music Creation、Ads、Game | AI music for content, AI ad music, AI game music |
| **Use Cases** | 功能 | Mood to song、Imitation、Reimagine | mood to song AI, AI music imitation |
| **Features** | — | 音乐生成、MV、母带、Stem | AI music agent, AI music maker |

*Use Cases 见 [tunee-use-cases.md](./tunee-use-cases.md)*

---

## Quick Reference

| Section | Used by |
|---------|---------|
| 0 | 文档语言策略（中英分工、实施规则） |
| 1-4 | 所有 skills：SEO、页面、组件、渠道 |
| 5 | 技术 SEO、sitemap |
| 6 | On-page SEO、metadata、关键词研究 |
| 7 | 竞争定位、内容策略 |
| 8 | 文案、语气、testimonials、CTA |
| 9-10 | 功能、内容策略 |
| tunee-features.md | 功能页详情、产品线 |
| tunee-use-cases.md | Use Cases、场景页 |
| tunee-competitors.md | 竞品分析 |
| tunee-keywords.md | 关键词映射 |
| tunee-music-generator.md | Music Generator 程序化 SEO 策略 |
| tunee-brand-visual.md | 品牌视觉（色彩、字体、组件与 Brief） |

---

## 文档关联总览

```
tunee.md（主文档）
├── tunee-features.md         ← 功能、产品线、价值评估（能做什么）
├── tunee-use-cases.md        ← Use Cases、场景页（谁在什么情境下用）
├── tunee-competitors.md      ← 竞品分析
├── tunee-keywords.md         ← 关键词映射
├── tunee-brand-visual.md     ← 品牌视觉规范（色彩、字体、组件）
└── tunee-music-generator.md  ← Music Generator 程序化 SEO 策略
```
