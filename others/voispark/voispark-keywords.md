# VoiSpark 关键词与目标页面映射

> 关联：[voispark.md](./voispark.md) | [voispark-voice-generator.md](./voispark-voice-generator.md) | [voispark-features.md](./voispark-features.md) | [voispark-use-cases.md](./voispark-use-cases.md) | [voispark-competitors.md](./voispark-competitors.md) | 基于官网、竞品分析、核心词 TTS / Voice Generator / Voice Cloning

---

## 1. 主关键词表

| 意图 | 关键词 | 目标页 | 覆盖 | P |
|------|--------|--------|------|---|
| **核心 A** | **TTS**, **text to speech**, **AI text to speech** | 首页、/text-to-speech | ✅ | 0 |
| **核心 B** | **voice generator**, **AI voice generator** | 首页、功能页 | ✅ | 0 |
| **核心 C** | **voice cloning**, **AI voice cloning** | 首页、/voice-cloning | ✅ | 0 |
| **功能** | voice changer, AI voice changer | /voice-changer | 部分 | 1 |
| **功能** | AI voice cover, AI song cover, vocal replacement | /ai-voice-cover（规划） | 待建 | 2 |
| **功能** | voice library, celebrity voice | /voice-generator | 部分 | 1 |
| **程序化** | [celebrity] AI voice, Taylor Swift voice | /voice-generator/{celebrity} | 部分 | 1 |
| **程序化** | AI voice for ads, ASMR voice | /voice-generator/{style} | 部分 | 2 |
| **Use case** | AI voice for YouTube Shorts, voice cloning for audiobook | Use Cases | 部分 | 1 |
| **竞品** | ElevenLabs alternative, PlayHT alternative, best AI voice generator 2025 | /alternatives（待建）、博客 | 部分 | 1 |
| **扩展** | TTS API, voice cloning API | /docs | 部分 | 2 |
| **模型截流** | Cartesia TTS, ElevenLabs voice, MiniMax voice | /leaderboard、/models | 部分 | 2 |
| **Target intent** | Commercial、Transactional | — | — | — |

---

## 2. 功能关键词表

### 2.1 TTS

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| 核心 | TTS, text to speech, AI text to speech | 首页、/text-to-speech |
| 扩展 | text to speech AI, AI TTS, realistic TTS |
| **长尾** | best AI text to speech 2025, TTS with emotion |

### 2.2 Voice Generator

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| 核心 | voice generator, AI voice generator | 首页、功能页 |
| 扩展 | AI voice generator free, online voice generator |
| **长尾** | best AI voice generator for creators |

### 2.3 Voice Cloning

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| 核心 | voice cloning, AI voice cloning | 首页、/voice-cloning |
| 扩展 | voice clone AI, clone voice 15 seconds |
| **长尾** | AI voice cloning 15 seconds, voice cloning for audiobook |

### 2.4 Voice Changer / Voice Library

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| 核心 | voice changer, voice library, celebrity voice | /voice-changer、/voice-generator |
| 扩展 | celebrity voice generator, celebrity AI voice | /voice-generator |

### 2.5 AI Voice Cover（规划中）

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| 核心 | **AI voice cover**, **AI song cover**, **vocal replacement** | /ai-voice-cover（规划） |
| 扩展 | voice swap, replace song vocals with my voice, AI cover with my voice | /ai-voice-cover |
| 长尾 | make AI cover with your voice, sing any song in my voice, voice clone for song cover | /ai-voice-cover（规划） |

---

## 3. Use Cases 关键词（Persona 维度）

| 类型 | 受众/场景 | 关键词 | 目标页 |
|------|-----------|--------|--------|
| **Persona** | Short-Form Creator | AI voice for YouTube Shorts, TTS for TikTok | /use-case/creator |
| **Persona** | Storyteller / Narrator | AI voice for podcast, voice cloning for audiobook | /use-case/narrator |
| **Persona** | Marketer | AI voice for ads, brand voice generator | /use-case/marketer |
| **Persona** | Event Planner | AI voice for events | /use-case/event-planner |
| **Persona** | Educator | TTS for e-learning | /use-case/educator |
| **Persona** | Performer | voice cloning for voice actor | /use-case/performer |

---

## 4. 竞品关键词

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| **Alternatives 页** | ElevenLabs alternative, PlayHT alternative, Murf alternative | 待建 /alternatives |
| **工具选型** | best AI voice generator 2025, best TTS, best voice cloning | 首页、博客、/alternatives |
| **对比** | VoiSpark vs ElevenLabs, VoiSpark vs PlayHT | /alternatives 子页 |

### 4.1 竞品核心关键词重叠与机会

| 关键词/意图 | 竞品覆盖 | VoiSpark 目标页 | 机会 |
|-------------|----------|----------------|------|
| TTS | 全部 | 首页、/text-to-speech | 多模型、情感、700+ 声音 |
| voice generator | 全部 | 首页、功能页 | 多模型聚合、名人库 |
| voice cloning | ElevenLabs、PlayHT、Murf | /voice-cloning | 15 秒克隆 |
| ElevenLabs alternative | — | /alternatives | 多模型含 ElevenLabs |
| best AI voice generator | 通用 | 首页、博客 | 创作者专注 |

---

## 5. URL 模式

| 类型 | 模式 | 示例 |
|------|------|------|
| 首页 | / | voispark.com |
| 定价 | /pricing | 定价页 |
| 功能 | /text-to-speech, /voice-cloning, /narration（核心）, /voice-library（核心）, /voice-changer（非核心）, /voice-generator | 功能页 |
| **API** | **/docs** | **API 文档** |
| **Leaderboard** | **/leaderboard** | **模型对比** |
| **Models** | **/models/{model}** | cartesia, elevenlabs, minimax 等 |
| Use Cases | /use-case/{persona} | creator, narrator, marketer 等 |
| **Narration** | **/narration** | **核心：长内容旁白、有声书、播客** |
| **AI Voice Cover** | **/ai-voice-cover**（规划） | **歌曲人声替换：用我的声音/名人声音翻唱** |
| **Voice Library** | **/voice-library** | **核心：1,200+ 声音、Use Cases/Languages/Celebrities/Styles** |
| **Voice Library Hub** | **/voice-generator** | **聚合页，9 大分类 + 风格入口** |
| **名人单页** | **/voice-generator/{celebrity}** | taylor-swift, morgan-freeman, donald-trump 等 300+ |
| **风格页** | **/voice-generator/{style}** | asmr, broadcast, narration, advertisement 等 14 个 |
| **Leaderboard** | **/leaderboard** | **TTS 模型对比：11Labs vs Cartesia vs MiniMax** |
| **Models** | **/models/{model}** | cartesia, elevenlabs, minimax 等 7 个 |
| **Affiliate** | **/affiliate** | **22% 佣金、首年无上限** |
| Alternatives | /alternatives（待建） | 竞品对比 |

---

## 6. 模型关键词（SEO 截流）

| 模型 | 核心关键词 | 长尾关键词 | 目标页 |
|------|------------|------------|--------|
| **Cartesia** | Cartesia TTS, Cartesia AI voice | Cartesia 40ms latency, Cartesia real-time TTS | /models/cartesia、/leaderboard |
| **ElevenLabs** | ElevenLabs voice, ElevenLabs TTS | ElevenLabs alternative | /models/elevenlabs、/leaderboard |
| **MiniMax** | MiniMax voice, MiniMax TTS | MiniMax voice cloning | /models/minimax、/leaderboard |
| **OpenAI** | OpenAI TTS, OpenAI voice | OpenAI text to speech | /models/openai、/leaderboard |
| **Fish Audio** | Fish Audio TTS | Fish Audio voice cloning | /models/fish-audio、/leaderboard |
| **Hume** | Hume AI voice | Hume AI TTS | /models/hume、/leaderboard |
| **Orpheus** | Orpheus voice | Orpheus AI companion | /models/orpheus、/leaderboard |

### 6.1 Leaderboard 页

**URL**: [https://voispark.com/leaderboard](https://voispark.com/leaderboard)  
**Title**: TTS Leaderboard 2025: See Why VoiSpark Leads the Competition

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| 聚合 | TTS leaderboard 2025, TTS comparison, ElevenLabs vs Cartesia vs MiniMax | /leaderboard |
| 工具 | use ElevenLabs in VoiSpark, use Cartesia in VoiSpark | /leaderboard、博客 |
| 对比 | best TTS model 2025, compare TTS models | /leaderboard |

### 6.2 Cartesia 单页

**URL**: [https://voispark.com/models/cartesia](https://voispark.com/models/cartesia)  
**Title**: Cartesia AI Real-Time Text-to-Speech with 40ms Latency

| 类型 | 关键词 |
|------|--------|
| 核心 | Cartesia TTS, Cartesia AI voice, Cartesia real-time |
| 长尾 | Cartesia 40ms latency, Cartesia voice agent, Cartesia free |
| Use case | Cartesia for podcast, Cartesia for audiobook |

### 6.3 Affiliate 页

**URL**: [https://voispark.com/affiliate](https://voispark.com/affiliate)  
**Title**: VoiSpark Affiliate Program: Earn 10-30% Commission

| 类型 | 关键词 |
|------|--------|
| 核心 | VoiSpark affiliate, VoiSpark affiliate program |
| 长尾 | earn promoting AI voice tools, AI voice affiliate |

---

## 7. Voice Generator 板块关键词

**Voice Generator 为 SEO 主驱动板块**；完整关键词、名人单页、风格页、分类页见 **[voispark-voice-generator.md](./voispark-voice-generator.md)** §二、§三。

| 类型 | 目标页 |
|------|--------|
| voice generator, AI voice generator | 首页、/voice-library、/voice-generator |
| [celebrity] AI voice | /voice-generator/{celebrity} |
| AI voice for ads, ASMR voice 等 | /voice-generator/{style} |

---

## 8. 文档导航

| 文档 | 用途 |
|------|------|
| [voispark.md](./voispark.md) | 主文档、产品概览、定位、ICP |
| [voispark-voice-generator.md](./voispark-voice-generator.md) | **Voice Generator 专用（SEO 主驱动）** |
| [voispark-features.md](./voispark-features.md) | 功能页、Narration、Voice Changer、Models |
| [voispark-use-cases.md](./voispark-use-cases.md) | Use Cases 页面、Persona |
| [voispark-competitors.md](./voispark-competitors.md) | 竞品分析、对比页机会 |

---

## 9. 待办（优先级）

| P | 待办 | 说明 |
|---|------|------|
| **0** | 首页强化 TTS、Voice Generator、Voice Cloning | 三核心词 |
| **1** | 功能页覆盖 text to speech、voice cloning、voice generator | 见 [voispark-features.md](./voispark-features.md) |
| **1** | Use Cases 页：creator、narrator、marketer 等 | 见 [voispark-use-cases.md](./voispark-use-cases.md) |
| **1** | 博客 best AI voice generator 2025、voice cloning 15 seconds | 工具选型 |
| **2** | 新建 /alternatives：ElevenLabs alternative、PlayHT alternative | 见 [voispark-competitors.md](./voispark-competitors.md) |
| **2** | /leaderboard、/models 强化模型关键词 | Cartesia、ElevenLabs、MiniMax |
| **2** | Voice Generator 板块：名人单页、Evidence block、Person 分类页 | 见 [voispark-voice-generator.md](./voispark-voice-generator.md) |
| **2** | AI Voice Cover 功能页（规划）：AI voice cover、AI song cover、vocal replacement | 见 [voispark-features.md](./voispark-features.md) §六 |
