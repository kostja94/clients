## §4 内容图谱

### 4.1 Track S 文件表与下一序号

| NN | 文件 | slug | 类型 | 角色 | 主关键词 |
|----|------|------|------|------|---------|
| 01 | 01-best-ai-voice-changer-2026.md | `best-ai-voice-changer` | Comparison | **Hub** | best AI voice changer |
| 02 | 02-how-to-change-google-assistant-voice-2026.md | `how-to-change-google-assistant-voice` | IntentSplit | Spoke | Google Assistant voice |
| 03 | 03-how-to-change-your-voice-2026.md | `how-to-change-your-voice` | HowTo | Spoke | how to change your voice |
| 04 | 04-dubbing-ai-vs-voicemod-2026.md | `dubbing-ai-vs-voicemod` | Alternative | Spoke | Dubbing AI vs Voicemod |

**下一序号：05**

### 4.2 Hub-Spoke 结构

```
                    ┌──────────────────────────────┐
                    │  01 best-ai-voice-changer     │
                    │  Comparison Hub               │
                    └──────────────┬───────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┬─────────────────┐
         │                         │                         │                 │
    02 IntentSplit            03 HowTo                 04 Alternative        05+
    Google Assistant          live vs file             vs Voicemod      PlatformGuide
    routing-only              + Setup                                          / Hardware
         │                         │                         │
         └────────────────── 四向互链 ───────────────────────┘
```

**阅读旅程**：选型 hub → 意图分流 or 实操 how-to or 竞品对比 → PlatformGuide / Hardware

### 4.3 P0 战略队列（Track S）

| 状态 | 优先级 | 类型 | slug | 主关键词 | 备注 |
|------|--------|------|------|---------|------|
| **Done** | P0 | Alternative | `dubbing-ai-vs-voicemod` | Dubbing AI vs Voicemod | #04 · PromoteFrom cms-export · 2026-06-16 |
| **Active** | P0 | PlatformGuide | `how-to-get-voice-changer-on-discord` | Discord voice changer setup | #05 候选 · RefreshInPlace 或 PromoteToStrategic |
| **Backlog** | P1 | HardwareGuide | `dubbing-box-setup-guide` | Dubbing Box PS5/mobile | 硬件差异化 |
| **Backlog** | P1 | Alternative | `voicemod-alternative` | Voicemod alternative | 竞品拦截 |

### 4.4 Canonical Concept Registry

| 概念 | Canonical | 引用方式 |
|------|-----------|---------|
| Live vs File 工作流 | `/blog/how-to-change-your-voice` | 1–2 句 + link |
| Assistant vs Mic | `/blog/how-to-change-google-assistant-voice` | IntentSplit 强制 |
| Best 选型 | `/blog/best-ai-voice-changer` | Comparison hub |
| Dubbing vs Voicemod | `/blog/dubbing-ai-vs-voicemod` | Alternative canonical |
| 角色 preset | `/voice-changer/{slug}` | CharacterBridge 短引 + link |
| Meme 音效库 | `/community-sounds` | SoundboardPick |
| AI 生成 sfx | `/sound-effect-generator` | 与库区分 |

### 4.5 冲突表（MERGE 对照）

| 新选题关键词 | 已有 canonical | 判定 |
|-------------|---------------|------|
| best AI voice changer / top voice changers | 01 hub | Spoke 链 hub；`top-5-voice-changers` STOP（301） |
| how to change voice / routing | 03 | MERGE 除非 Platform-specific（Discord only → PlatformGuide） |
| Google Assistant voice | 02 | KEEP IntentSplit；live mic 文链 02 |
| Dubbing AI vs Voicemod | 04 + cms `dubbing-ai-vs-voicemod` | PromoteToStrategic #04；cms 填 superseded_by |
| Gojo voice changer long guide | `/voice-changer/gojo` | CharacterBridge ≤800w preset 细节 |

### 4.6 Blog 互链矩阵（Track S — 以本表为准）

| slug | 正文应链 | 最低 |
|------|---------|:---:|
| `best-ai-voice-changer` | → `how-to-change-google-assistant-voice` · → `how-to-change-your-voice` · → `dubbing-ai-vs-voicemod` | ≥3 |
| `how-to-change-google-assistant-voice` | → `best-ai-voice-changer` · → `how-to-change-your-voice` | ≥2 |
| `how-to-change-your-voice` | → `best-ai-voice-changer` · → `how-to-change-google-assistant-voice` · → `dubbing-ai-vs-voicemod` | ≥3 |
| `dubbing-ai-vs-voicemod` | → `best-ai-voice-changer` · → `how-to-change-your-voice` · → `how-to-change-google-assistant-voice` | ≥3 |

### 4.7 CMS 重叠索引（高频 slug）

Phase 0：slug 精确匹配此表；未知 slug 声明「manifest 未预置，人类需查 manifest.csv」— **禁止加载整个 cms-export/**。

| slug | 处置 | Track | category |
|------|------|-------|----------|
| `dubbing-ai-vs-voicemod` | PromoteToStrategic → #04 | S | voice-changer-review |
| `how-to-get-voice-changer-on-discord` | RefreshInPlace | C→S 可选 | voice-changer-tips |
| `top-5-voice-changers` | **STOP**（301→hub） | — | — |
| `top-10-free-voice-changer-online-2025` | **STOP**（301→hub） | — | — |
| `top-*-soundboard*` | 默认 SoundboardPick | C | soundboard-tips |
| `*-voice-actor*` | VoiceActorProfile | C | voice-actors |
| `alternative-voicemod` | MERGE → `dubbing-ai-vs-voicemod` 或 Refresh | C | voice-changer-review |

**CMS 规模**：256 done · 1 skip · 5 categories（manifest 2026-06-15）

### 4.8 301 计划（人类执行）

| 旧 URL slug | 新目标 |
|-------------|--------|
| `top-5-voice-changers` | `best-ai-voice-changer` |
| `top-10-free-voice-changer-online-2025` | `best-ai-voice-changer` |

---

## §7 文件命名与 README 同步

| 约定 | Track S | Track C |
|------|---------|---------|
| 文件名 | `NN-{slug}-2026.md` | `{slug}.md` in cms-export/ |
| NN | 两位递增；当前下一 **05** | — |

> **2026-08-11 起**：`image` 字段不再写入 frontmatter，图片由 CMS 单独管理。

**发布后人类 checklist**：
1. bump §4.1 下一序号
2. 更新 blog/README 文章表
3. Track C：更新 manifest.csv
4. bump SKILL.md frontmatter `version` patch
