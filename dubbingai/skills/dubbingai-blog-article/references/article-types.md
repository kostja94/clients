## §2 文章类型路由（12 类）

收到任务后**先匹配类型**，再跳转对应 H2 模板。

### 2.1 路由表

| 类型 | CMS category | Track | 词数 | 产品提及上限 | 参考 slug |
|------|--------------|-------|------|-------------|-----------|
| **Comparison** | voice-changer-review | S | 2500–3500 | ≤35% | `best-ai-voice-changer` |
| **HowTo** | voice-changer-tips | S/C | S:2200–3200 / C:1500–2200 | ≤40% | `how-to-change-your-voice` |
| **IntentSplit** | voice-changer-tips | S | 1800–2600 | ≤25% | `how-to-change-google-assistant-voice` |
| **Alternative** | voice-changer-review | S/C | 2200–3000 | ≤45% | `dubbing-ai-vs-voicemod` |
| **PlatformGuide** | voice-changer-tips | S/C | 2000–2800 | ≤40% | `how-to-get-voice-changer-on-discord` |
| **SoundboardPick** | soundboard-tips | C | 1200–2000 | ≤50% | `top-*-soundboard-sites` |
| **SoundEffectPick** | sound-effect-tips | C | 1200–2000 | ≤45% | `*-sound-effect` lists |
| **VoiceActorProfile** | voice-actors | C | 1500–2500 | ≤20% | `*-voice-actor` |
| **PopCultureExplain** | voice-changer-tips | C | 1000–1800 | ≤30% | trend/news explainers |
| **CharacterBridge** | voice-changer-tips | C | 1200–1800 | ≤35% | bridge to `/voice-changer/{slug}` |
| **HardwareGuide** | voice-changer-tips | S | 1800–2600 | ≤40% | Dubbing Box setup |
| **Diagnosis** | voice-changer-tips | S/C | 1800–2600 | ≤30% | virtual mic / latency |

**路由规则**：
- `best` / `top picks` / `compare` → **Comparison**
- `how to` + live mic / routing → **HowTo**；+ Google Assistant / Siri → **IntentSplit**
- `vs` / `alternative` → **Alternative**
- Discord / Valorant / OBS setup → **PlatformGuide**
- `soundboard` + meme → **SoundboardPick**
- `sound effect` + download → **SoundEffectPick**（P4 分流）
- `voice actor` / cast → **VoiceActorProfile**
- 角色名 + voice changer → **CharacterBridge**（C3 禁 duplicate 程序化页）

### 2.2 Track S 通用模块

| 模块 | 要求 |
|------|------|
| **Lead** | frontmatter 后第一段（第一个 `##` 前）；≤250 words |
| **Summary block** | `At a glance` 或 `The 30-second answer`（二选一或组合） |
| **H2** | 英文描述性标题；**不编号**（禁 `## 1.`） |
| **Conclusion** | `## Conclusion`（FAQ 之上） |
| **FAQ** | `## FAQ` 或 `## Frequently asked questions`；≥3 题 |
| **内链** | ≥2 blog 或产品；Hub 4-Spoke 互链见 project-config §1.8 |
| **CTA** | ≤2 次 |
| **无 TL;DR** | 用 Lead + summary block |
| **无 Key Takeaways** | Track S 禁用 CMS 式 bullet 摘要块 |

### 2.3 Track C 通用模块

| 模块 | 要求 |
|------|------|
| **Key Takeaways** | `## Key Takeaways` · 3–5 bullets（可选 Pro Tip blockquote） |
| **H2/H3** | 可更短节；允许列表偏多 |
| **产品钩** | Key Takeaways 后或第一节 1 次 CTA |
| **category** | frontmatter 必填，匹配 manifest 五类 |

---

### 2.4 Comparison — H2 模板（Track S）

```
{Lead — scope intent: live gaming vs record-first}
## At a glance                    ← 对比表 + Quick picks
## Why "{keyword}" is three different searches
## How we ranked these tools
## 1. {Product A} — {angle}       ← 可用 ## 产品名 非编号
## 2. {Product B} — ...
## Setup tips / routing
## Conclusion
## FAQ
```

---

### 2.5 HowTo — H2 模板（Track S）

```
{Lead — pain + promise}
## The 30-second answer
## Job A vs Job B: live vs file-based
## Web, desktop, and where each breaks
## {Scenario sections}
## Conclusion
## FAQ
```

---

### 2.6 IntentSplit — H2 模板（Track S）

```
{Lead — disambiguate intents in first 2 sentences}
## What you are actually trying to change
## Path A: {Assistant/system TTS}
## Path B: {Your live microphone}
## When to use a real-time voice changer instead
## Conclusion
## FAQ
```

---

### 2.7 Alternative — H2 模板（Track S）

```
{Lead — fair comparison frame; link Comparison hub if needed}
## At a glance                    ← axis table, not winner-take-all
## Who each tool is for
## {Axis 1: Real-time + latency}
## {Axis 2: Voice library vs community}
## {Axis 3: Soundboard depth}
## {Axis 4: Pricing honesty}
## When to pick Voicemod / Voice.ai instead
## Conclusion
## FAQ
```

**Alternative 专属**：≥1 段 Voicemod 真实优势；Disclosure 可放在 Lead 后。

---

### 2.8 PlatformGuide — H2 模板

```
{Lead}
## Key Takeaways（Track C）或 The 30-second answer（Track S）
## What you need before you start
## Step-by-step setup
## Troubleshooting
## Conclusion / Next steps
## FAQ（Track S）
```

---

### 2.9 SoundboardPick — H2 模板（Track C）

```
{Lead — meme/context hook}
## Key Takeaways
## {Product 1 — often Dubbing AI} — why it fits
## {Product 2 — third party}
## {Product 3}
## How to use sounds in {Discord/stream/game}
## Conclusion
```

链 `/community-sounds`；禁把 generator 当下载库。

---

### 2.10 SoundEffectPick — H2 模板（Track C）

```
{Lead}
## Key Takeaways
## Free libraries vs AI generation（P4 分流段）
## Top picks for {sound name}
## Conclusion
```

---

### 2.11 VoiceActorProfile — H2 模板（Track C）

```
{Lead — character/show context}
## Key Takeaways
## Who voices {character}
## Other roles / career notes
## How fans use voice changers for {character}（CharacterBridge 轻量）
## Conclusion
```

产品提及 ≤20%；链 `/voice-changer/{character}` 若存在。

---

### 2.12 CharacterBridge — H2 模板（Track C）

```
{Lead}
## Key Takeaways
## Why {character} voices trend in {year}
## Get the preset on Dubbing AI     ← 短；链 /voice-changer/{slug}
## Tips for streaming / memes
## Conclusion
```

**硬规则**：正文 ≤800 词讲 preset 细节 → 余下链程序化页（C3）。

---

### 2.13 HardwareGuide — H2 模板（Track S）

```
{Lead}
## Desktop vs Dubbing Box — when each wins
## What Dubbing Box supports
## Setup on {PS5/mobile/PC}
## Limitations and honest tradeoffs
## Conclusion
## FAQ
```

---

### 2.14 Diagnosis — H2 模板

```
{Lead — symptom}
## The 30-second answer / Key Takeaways
## Checklist: routing first
## {Symptom-specific fixes}
## When to switch tools
## Conclusion
```

---

## §8 Voice 与禁止措辞

> **全文 Voice 标准、禁止措辞清单、空泛句检测、句段量化指标 → `references/writing-style.md` §2–§5**
> 
> 本文档仅保留类型差异快照——所有通用写作规则以 writing-style.md 为唯一入口，禁止两处独立维护。

### 8.1 Track S Voice（5 正向要点）

见 `writing-style.md` §2.1 正向标准 + §2.2 类型语气表（Comparison/HowTo/Alternative/IntentSplit/HardwareGuide/Diagnosis 行）。

### 8.2 Track C Voice

见 `writing-style.md` §2.2 类型语气表（SoundboardPick/SoundEffectPick/VoiceActorProfile/CharacterBridge/PopCultureExplain 行）。

### 8.3 禁止措辞与空泛句

**通用禁词** → `writing-style.md` §3  
**Dubbing 专属禁词** → `writing-style.md` §3.2  
**空泛句 10 项检测** → `writing-style.md` §4  
**句段量化指标** → `writing-style.md` §5
