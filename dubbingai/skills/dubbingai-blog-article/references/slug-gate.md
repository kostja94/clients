# Slug 设计审查（Gate B）

> Agent 在 Phase 2 前加载。Slug 不通过则不得进入 Outline。

---

## 1. 七条原则

| # | 原则 | Track S | Track C |
|---|------|---------|---------|
| P1 | 常青优先 | slug **不含年份**（年份放 title/file） | 可与 CMS URL 一致（含历史 `-2025`） |
| P7 | 搜索意图优先 | slug 读起来应像目标读者会输入 Google 的搜索词；禁 framework/guide/complete 等内部架构词 | 同上 |
| P2 | 关键词对齐 | primary keyword 自然变体 | meme/角色名保留 |
| P3 | 人可读 | 大声读通顺 | 同上 |
| P5 | 集群一致 | 见 §3 | `top-*-soundboard*` 模式 |
| P6 | 语义余量 | 30% 内容变化仍合适 | 角色名 slug 可具体 |
| P4 | 长度克制 | 5–8 词，≤60 字符 | ≤70 字符 |

**原则优先级**: 常青 (P1) > 搜索意图 (P7) > 关键词对齐 (P2) > 人可读 (P3) > 集群一致 (P5) > 语义余量 (P6) > 长度克制 (P4)
当原则冲突时，按此优先级取舍。 |

---

## 2. 反模式（13 项）

| # | 反模式 | 错误 | 正确 |
|---|--------|------|------|
| A1 | Track S slug 含年份 | `best-ai-voice-changer-2026` | `best-ai-voice-changer`（文件可 `-2026`） |
| A2 | 含数量 listicle slug | `5-best-voice-changers` | `best-ai-voice-changer` |
| A3 | 连续重复词 | `voice-changer-voice-changer` | 去重 |
| A4 | 缩写/行话 | `vc-ai-discord` | 完整词 |
| A5 | 含观点 slug | `why-voicemod-is-dead` | `dubbing-ai-vs-voicemod` |
| A6 | 与 H1 断裂 | H1 best AI voice changer, slug `ai-tools-tips` | 对齐 |
| A7 | 抢 Hub 词 | 新 slug `best-real-time-voice-changer` 与 hub 重叠 | MERGE 到 hub |
| A8 | 太泛 | `voice-changer` | `how-to-change-your-voice` |
| A9 | 下划线 | `dubbing_ai_vs_voicemod` | kebab-case |
| A10 | 品牌名（非 VS） | `dubbing-ai-is-best` | `dubbing-ai-vs-voicemod` |
| A11 | 内部架构词 | `voice-changer-complete-guide-framework` · `tiktok-shop-hooks-framework` · `diagnosis-voice-changer-not-working` | `how-to-change-your-voice` · `tiktok-video-hooks` · `voice-changer-discord-not-working` |
| A12 | 301 源 slug | `top-5-voice-changers` 新稿 | STOP → hub |
| A13 | 分类前缀沉积 | 多篇文章 slug 一致以分类前缀开头（如 `voice-changer-tips-*`） | 各篇 slug 以搜索词开头；集群关系靠内链而非 URL 前缀 |

---

## 3. Dubbing 集群命名模式

| 模式 | 用途 | 示例 |
|------|------|------|
| `best-*` | Comparison hub | `best-ai-voice-changer` |
| `how-to-*` | HowTo / Platform | `how-to-change-your-voice` |
| `how-to-change-google-*` | IntentSplit | `how-to-change-google-assistant-voice` |
| `*-vs-*` | Alternative | `dubbing-ai-vs-voicemod` |
| `*-alternative` | Alternative | `voicemod-alternative` |
| `top-*-soundboard*` | SoundboardPick | `top-quandale-dingle-soundboard-sites` |
| `*-voice-actor` | VoiceActorProfile | `spongebob-voice-actor-tom-kenny` |
| `*-sound-effect` | SoundEffectPick | `oh-no-sound-effects-free` |
| `{character}-voice-changer` | CharacterBridge | 优先链 `/voice-changer/{character}` |

---

## 4. Gate B — 7 问

```
1. primary keyword 是什么？slug 对齐了吗？
2. 大声读通顺吗？
3. Track S：含年份/数量/架构词（A11）吗？Track C：与 canonical URL 一致吗？
4. content-graph / cms-overlap 冲突吗？
5. 一年后 slug 还合适吗？
6. 是否抢 Hub 或 301 源？（A12/C4）
7. 用 primary keyword 搜 Google，前 5 竞品 slug 比你的更短、更接近搜索语言吗？（A11+A13 检查）
全部 Pass → 定 slug
```

---

## 5. frontmatter slug 格式

| Track | frontmatter `slug` | 文件名 |
|-------|-------------------|--------|
| **S** | `best-ai-voice-changer`（无 `/blog/`、无年份） | `01-best-ai-voice-changer-2026.md` |
| **C** | `top-quandale-dingle-soundboard-sites` | `cms-export/top-quandale-dingle-soundboard-sites.md` |

---

## 6. 预审示例

| slug | Track | Gate B | 类型 |
|------|-------|--------|------|
| `best-ai-voice-changer` | S | ✅ | Comparison |
| `dubbing-ai-vs-voicemod` | S | ✅ | Alternative |
| `how-to-change-your-voice` | S | ✅ | HowTo |
| `top-5-voice-changers` | — | ❌ A12/C4 | STOP |
| `voice-changer-complete-guide-2026` | S | ❌ A1+A11 | — |
