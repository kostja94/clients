## §5 关键词与主题桶

> Phase 0 加载 · 禁运行时读 dubbingai-keywords.md

### 5.1 三核心词（P0 布局）

| 核心 | 示例关键词 | 主目标 |
|------|-----------|--------|
| **A** | AI voice changer, real-time voice changer, free AI voice changer | `/` · `/download-desktop` · hub #01 |
| **B** | voice changer for gaming, Discord voice changer | `/discord-voice-changer` · PlatformGuide |
| **C** | voice changer for streaming, meme soundboard | `/soundboard` · Comparison |

### 5.2 主题桶 → 文章类型

| 桶 | 关键词示例 | 类型 | Track |
|----|-----------|------|-------|
| **Hub 选型** | best AI voice changer 2026 | Comparison | S |
| **竞品** | Dubbing AI vs Voicemod, Voicemod alternative | Alternative | S/C |
| **实操** | how to change your voice, virtual mic routing | HowTo | S |
| **意图分流** | change Google Assistant voice | IntentSplit | S |
| **平台** | Discord voice changer setup, OBS voice changer | PlatformGuide | S/C |
| **角色** | Gojo voice changer, Jett voice changer | CharacterBridge | C |
| **Meme SB** | Quandale Dingle soundboard, fart soundboard | SoundboardPick | C |
| **SFX 下载** | free sound effects, notification sounds | SoundEffectPick | C |
| **声优** | SpongeBob voice actor, character cast | VoiceActorProfile | C |
| **硬件** | Dubbing Box PS5, mobile voice changer | HardwareGuide | S |
| **诊断** | voice changer not working Discord | Diagnosis | S/C |

### 5.3 平台长尾

Discord · Zoom · VRChat · Fortnite · Valorant · Roblox · OBS · Twitch — 平台页 + PlatformGuide 分工；blog 不复制整页 programmatic 内容。

### 5.4 Soundboard vs Sound effects vs Generator

| 词族 | 落地 | 文章类型 |
|------|------|---------|
| meme soundboard, soundboard for streaming | `/community-sounds` `/soundboard` | SoundboardPick |
| free sound effects download, sfx pack | `/community-sounds` | SoundEffectPick |
| AI sound effect generator, text to sfx | `/sound-effect-generator` | SoundEffectPick（含分流段） |

### 5.5 禁抢词 / MERGE

| 禁新稿（Track C 亦慎） | 原因 |
|----------------------|------|
| `best-ai-voice-changer` 同 intent 变体 | Hub #01 |
| `top-5-voice-changers` | 301 → hub |
| 完整 Gojo preset 教程 | `/voice-changer/gojo` programmatic |

### 5.6 JTBD 速查

| 读者任务 | 关键词信号 | 路由 |
|---------|-----------|------|
| 选工具 | best, compare, vs | Comparison / Alternative |
| 装 Discord 麦 | how to get voice changer on Discord | PlatformGuide |
| 搞清 Assistant | Google Assistant voice | IntentSplit |
| 找梗音 | {meme} soundboard | SoundboardPick |
| 下音效文件 | {sound} effect free download | SoundEffectPick |
| 主机/mobile | PS5 voice changer, Dubbing Box | HardwareGuide |

### 5.7 keywords 规划（2026-08-11 起不入 frontmatter）

keywords 仅用于 **SEO 规划**（title/description/H2 用词与 SERP 对照），**不写进 frontmatter**。

Track S：≥5 项 — primary + 2 长尾 + 2 平台/场景变体

Track C：可 3–5 项；meme/角色名 + soundboard/sound effect + year 可选
