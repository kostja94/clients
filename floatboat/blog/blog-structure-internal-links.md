# Floatboat Blog 文章结构与内链

> **用途**：全站 Blog 唯一的结构与内链参考（人类 + 站点维护）。回答两件事——**① 59 篇文章如何组织；② 文章之间应如何互链**（含实测快照与补链待办）。
>
> **Skill 对齐**：创作 Gate / Canonical / Hub-Spoke 以 [`skills/floatboat-blog-article/references/content-graph.md`](skills/floatboat-blog-article/references/content-graph.md) 为 SSOT，写作规则见 [`references/internal-links.md`](skills/floatboat-blog-article/references/internal-links.md)（R1–R7）。本文档是同一信息的**项目级视图**，随实际成稿维护。
>
> **⚠ content-graph 声明**:skill 内 content-graph 仍写「下一序号 62」，但**实际已到 #87**（file-organizer 78–86、doubao 87、model 76/77 均未登记）。本文档以**实际文件系统为基准**（59 篇，快照 2026-09-09）。维护时请优先回填 content-graph。
>
> **快照**：2026-09-09 · 59 篇全量实测。统计口径：frontmatter 之后正文中站内 `/blog/{slug}` 链接（HTML `<a href>` / Markdown `](/…)` / 绝对 URL 三种写法），一篇文章对同一 slug 计 1；带 NN 前缀的错误目标已归一化（见 §6.1）；产品页链接不计入。

---

## 一、Blog 文章结构

```
Blog (/blog) — 59 篇 · 下一序号 88
│
├── (root) Scheduling Agent 簇                     ← 02–07（Cluster: scheduling-agent）
│   ├── #03  what-is-agentic-calendar              ★ Hub（品类定义）
│   ├── #02  ai-scheduling-agent                    （四代演进定义）
│   ├── #04  calendar-driven-ai-vs-chat-ai          （范式对比）
│   ├── #05  best-ai-scheduling-assistants          （选型 Ranking）
│   ├── #06  ai-meeting-preparation                 （场景：会前）
│   └── #07  ai-follow-up-automation                （场景：会后）
│
├── Updates/                                       ← Cluster: updates / floatim
│   ├── #01  introducing-floatim                    ★ FloatIM 产品公告（standalone 链出）
│   ├── #33  kimi-k3-floatboat                      （Kimi K3 接入 Floatboat）
│   ├── #34  vibe-coding-one-prompt-html-game       （vibe coding SEO spoke）
│   └── #56  introducing-flow-mode                  ★ Flow Mode 公告（voice 桥）
│
├── worldcup/                                      ← Cluster: worldcup（#09/#10 Pillar）
│   ├── #09  world-cup-2026-guide                   ★ Hub P01
│   ├── #10  world-cup-2026-schedule                ★ Hub P02（数据）
│   ├── #17  world-cup-2026-google-calendar-ics     （P09 教程）
│   ├── #18  floatcup-world-cup-2026-calendar-subscribe （P10 产品）
│   └── #19  world-cup-2026-schedule-usa            （P11 受众）
│
├── openai/                                        ← Cluster: openai
│   ├── #57  codex-harness-open-source              ★ Hub（Codex Harness open）
│   ├── #30  gpt-5-6-sol-terra-luna                 ★ Hub（GPT-5.6 模型族）
│   ├── #31  gpt-5-6-floatboat                      （GPT-5.6 接入 Floatboat）
│   └── #77  gpt-6-astra                            （GPT-6 Astra 模型族）
│
├── claude/                                        ← Cluster: claude
│   ├── #35  what-is-claude-cowork                  ★ Hub（Cowork）
│   ├── #36  best-claude-cowork-alternatives        （Ranking spoke）
│   ├── #37  what-is-claude-tag                     ★ Hub（Tag）
│   ├── #38  best-claude-tag-alternatives           （Ranking spoke）
│   ├── #47  claude-code-vs-cowork-vs-tag           ★ 三方枢纽桥
│   ├── #48  what-is-claude-code                    ★ Hub（Code）
│   └── #49  best-claude-code-alternatives          （Ranking spoke）
│
├── deepseek/                                      ← Cluster: deepseek
│   ├── #41  what-is-deepseek-agent                 ★ Hub（Agent）
│   ├── #42  how-to-build-deepseek-agent            （Product spoke）
│   ├── #43  deepseek-agent-function-calling        （Product spoke）
│   ├── #44  deepseek-agent-vs-claude-code          （Comparison 桥 → claude）
│   ├── #46  what-is-deepseek-harness               ★ Hub（Harness）
│   ├── #50  deepseek-v4-pro-0813                   （模型 GA）
│   └── #52  cordis-plugin-framework                （插件内核）
│
├── voice/                                         ← Cluster: voice-agent
│   ├── #58  what-is-voice-dictation-for-ai-agents  ★ Hub
│   ├── #59  voice-mode-vs-dictation-for-ai-agents  （范式）
│   ├── #60  best-voice-dictation-for-ai-agents     （Ranking）
│   ├── #70  chatgpt-voice-mode-vs-dictation        （Comparison）
│   ├── #73  what-is-a-voice-agent                  （Glossary）
│   └── #75  voice-agent-vs-voice-dictation-for-work（范式）
│
├── file-organizer/                                ← Cluster: file-organizer（78–86）
│   ├── #78  what-is-an-ai-file-organizer           ★ Hub（品类定义）
│   ├── #79  file-organizer-vs-file-renamer-vs-file-sorter （决策）
│   ├── #80  best-ai-file-organizer                 （Ranking organizer）
│   ├── #81  best-ai-file-renamer                   （Ranking renamer）
│   ├── #82  do-ai-file-organizers-upload-your-files（隐私 canonical）
│   ├── #83  ai-file-organizer-mac                  （平台 Mac）
│   ├── #84  ai-file-organizer-windows              （平台 Windows）
│   ├── #85  clean-up-downloads-folder-with-ai      （场景教程）
│   └── #86  organize-receipts-and-invoices-with-ai （场景教程）
│
├── (root) Obsidian 簇                             ← Cluster: obsidian
│   ├── #39  what-is-obsidian-vault                 ★ Hub（定义）
│   └── #40  how-to-use-obsidian-with-ai-agent      （Product spoke）
│
└── (root) Model 单篇 / 其它                       ← Cluster: model-singles / standalone
    ├── #32  kimi-k3-open-frontier-model            ★ Kimi K3 Hub（root，配对 Updates/33）
    ├── #45  what-is-minimax-h3                     ★ MiniMax H3 Hub
    ├── #61  minimax-h3-max-infinite-ai-livestream  （H3 Max Live spoke）
    ├── #51  grok-4-6                               （Grok 4.6 对照枢纽）
    ├── #53  grok-bot                               （Grok Bot agent 产品）
    ├── #54  glm-5-3                                （GLM-5.3 单篇）
    ├── #55  gemini-3-7-flash                       （Gemini 3.7 单篇）
    ├── #76  gemini-3-8-flash                       （Gemini 3.8 单篇）
    └── #87  what-is-doubao-work                    （Standalone Research · 中文产品）
```

| NN | 文件 | slug | 簇 | 角色 |
|----|------|------|----|------|
| 01 | `Updates/01-introducing-floatim-2026.md` | introducing-floatim | updates | 产品公告 |
| 02 | `02-ai-scheduling-agent.md` | ai-scheduling-agent | scheduling | Spoke（定义） |
| 03 | `03-what-is-agentic-calendar.md` | what-is-agentic-calendar | scheduling | **Hub** |
| 04 | `04-calendar-driven-ai-vs-chat-ai.md` | calendar-driven-ai-vs-chat-ai | scheduling | Spoke（对比） |
| 05 | `05-best-ai-scheduling-assistants.md` | best-ai-scheduling-assistants | scheduling | Spoke（Ranking） |
| 06 | `06-ai-meeting-preparation.md` | ai-meeting-preparation | scheduling | Spoke（场景） |
| 07 | `07-ai-follow-up-automation.md` | ai-follow-up-automation | scheduling | Spoke（场景） |
| 09 | `worldcup/09-world-cup-2026-guide.md` | world-cup-2026-guide | worldcup | **Hub P01** |
| 10 | `worldcup/10-world-cup-2026-schedule.md` | world-cup-2026-schedule | worldcup | **Hub P02** |
| 17 | `worldcup/17-world-cup-2026-google-calendar-ics.md` | world-cup-2026-google-calendar-ics | worldcup | Spoke（教程） |
| 18 | `worldcup/18-floatcup-world-cup-2026-calendar-subscribe.md` | floatcup-world-cup-2026-calendar-subscribe | worldcup | Spoke（产品） |
| 19 | `worldcup/19-world-cup-2026-schedule-usa.md` | world-cup-2026-schedule-usa | worldcup | Spoke（受众） |
| 30 | `openai/30-gpt-5-6-sol-terra-luna.md` | gpt-5-6-sol-terra-luna | openai | **Hub（模型）** |
| 31 | `openai/31-gpt-5-6-floatboat.md` | gpt-5-6-floatboat | openai | Spoke（Product） |
| 32 | `32-kimi-k3-open-frontier-model.md` | kimi-k3-open-frontier-model | model-singles | **Hub（Kimi K3）** |
| 33 | `Updates/33-kimi-k3-floatboat.md` | kimi-k3-floatboat | updates | Spoke（Product） |
| 34 | `Updates/34-vibe-coding-one-prompt-html-game.md` | vibe-coding-one-prompt-html-game | updates | Spoke（SEO） |
| 35 | `claude/35-what-is-claude-cowork.md` | what-is-claude-cowork | claude | **Hub（Cowork）** |
| 36 | `claude/36-best-claude-cowork-alternatives.md` | best-claude-cowork-alternatives | claude | Spoke（Ranking） |
| 37 | `claude/37-what-is-claude-tag.md` | what-is-claude-tag | claude | **Hub（Tag）** |
| 38 | `claude/38-best-claude-tag-alternatives.md` | best-claude-tag-alternatives | claude | Spoke（Ranking） |
| 39 | `39-what-is-obsidian-vault.md` | what-is-obsidian-vault | obsidian | **Hub** |
| 40 | `40-how-to-use-obsidian-with-ai-agent.md` | how-to-use-obsidian-with-ai-agent | obsidian | Spoke（Product） |
| 41 | `deepseek/41-what-is-deepseek-agent.md` | what-is-deepseek-agent | deepseek | **Hub（Agent）** |
| 42 | `deepseek/42-how-to-build-deepseek-agent.md` | how-to-build-deepseek-agent | deepseek | Spoke（Product） |
| 43 | `deepseek/43-deepseek-agent-function-calling.md` | deepseek-agent-function-calling | deepseek | Spoke（Product） |
| 44 | `deepseek/44-deepseek-agent-vs-claude-code.md` | deepseek-agent-vs-claude-code | deepseek | Spoke（Comparison 桥） |
| 45 | `45-what-is-minimax-h3.md` | what-is-minimax-h3 | model-singles | **Hub（MiniMax H3）** |
| 46 | `deepseek/46-what-is-deepseek-harness.md` | what-is-deepseek-harness | deepseek | **Hub（Harness）** |
| 47 | `claude/47-claude-code-vs-cowork-vs-tag.md` | claude-code-vs-cowork-vs-tag | claude | **三方枢纽桥** |
| 48 | `claude/48-what-is-claude-code.md` | what-is-claude-code | claude | **Hub（Code）** |
| 49 | `claude/49-best-claude-code-alternatives.md` | best-claude-code-alternatives | claude | Spoke（Ranking） |
| 50 | `deepseek/50-deepseek-v4-pro-0813.md` | deepseek-v4-pro-0813 | deepseek | Spoke（模型 GA） |
| 51 | `51-grok-4-6.md` | grok-4-6 | model-singles | Spoke（对照枢纽） |
| 52 | `deepseek/52-cordis-plugin-framework.md` | cordis-plugin-framework | deepseek | Spoke（插件内核） |
| 53 | `53-grok-bot.md` | grok-bot | model-singles | Spoke（agent 产品） |
| 54 | `54-glm-5-3.md` | glm-5-3 | model-singles | Spoke（Model 单篇） |
| 55 | `55-gemini-3-7-flash.md` | gemini-3-7-flash | model-singles | Spoke（Model 单篇） |
| 56 | `Updates/56-introducing-flow-mode.md` | introducing-flow-mode | updates | 产品公告（voice 桥） |
| 57 | `openai/57-codex-harness-open-source.md` | codex-harness-open-source | openai | **Hub（Codex Harness）** |
| 58 | `voice/58-what-is-voice-dictation-for-ai-agents.md` | what-is-voice-dictation-for-ai-agents | voice-agent | **Hub** |
| 59 | `voice/59-voice-mode-vs-dictation-for-ai-agents.md` | voice-mode-vs-dictation-for-ai-agents | voice-agent | Spoke（范式） |
| 60 | `voice/60-best-voice-dictation-for-ai-agents.md` | best-voice-dictation-for-ai-agents | voice-agent | Spoke（Ranking） |
| 61 | `61-minimax-h3-max-infinite-ai-livestream.md` | minimax-h3-max-infinite-ai-livestream | model-singles | Spoke（H3 Max Live） |
| 70 | `voice/70-chatgpt-voice-mode-vs-dictation.md` | chatgpt-voice-mode-vs-dictation | voice-agent | Spoke（Comparison） |
| 73 | `voice/73-what-is-a-voice-agent.md` | what-is-a-voice-agent | voice-agent | Spoke（Glossary） |
| 75 | `voice/75-voice-agent-vs-voice-dictation-for-work.md` | voice-agent-vs-voice-dictation-for-work | voice-agent | Spoke（范式） |
| 76 | `76-gemini-3-8-flash.md` | gemini-3-8-flash | model-singles | Spoke（Model 单篇） |
| 77 | `openai/77-gpt-6-astra.md` | gpt-6-astra | openai | **Hub（GPT-6 模型）** |
| 78 | `file-organizer/78-what-is-an-ai-file-organizer.md` | what-is-an-ai-file-organizer | file-organizer | **Hub（品类）** |
| 79 | `file-organizer/79-file-organizer-vs-file-renamer-vs-file-sorter.md` | file-organizer-vs-file-renamer-vs-file-sorter | file-organizer | Spoke（决策） |
| 80 | `file-organizer/80-best-ai-file-organizer.md` | best-ai-file-organizer | file-organizer | Spoke（Ranking） |
| 81 | `file-organizer/81-best-ai-file-renamer.md` | best-ai-file-renamer | file-organizer | Spoke（Ranking） |
| 82 | `file-organizer/82-do-ai-file-organizers-upload-your-files.md` | do-ai-file-organizers-upload-your-files | file-organizer | Spoke（隐私 canonical） |
| 83 | `file-organizer/83-ai-file-organizer-mac.md` | ai-file-organizer-mac | file-organizer | Spoke（平台） |
| 84 | `file-organizer/84-ai-file-organizer-windows.md` | ai-file-organizer-windows | file-organizer | Spoke（平台） |
| 85 | `file-organizer/85-clean-up-downloads-folder-with-ai.md` | clean-up-downloads-folder-with-ai | file-organizer | Spoke（场景） |
| 86 | `file-organizer/86-organize-receipts-and-invoices-with-ai.md` | organize-receipts-and-invoices-with-ai | file-organizer | Spoke（场景） |
| 87 | `87-what-is-doubao-work.md` | what-is-doubao-work | standalone | Standalone Research |

**结构规则**：NN 全 blog 递增、不随子目录重置；公开 URL 扁平 `/blog/{slug}`；`category` 与簇注册一致；不设文末 Related articles，内链只在正文自然语境出现。

---

## 二、内链硬性规则（R1–R7 · 引用 internal-links.md）

| 规则 | 要求 |
|------|------|
| **R1** | 每篇正文 ≥2 条不同 `/blog/` slug 内链 |
| **R2** | 每篇被其他 blog 文章链入（backlink）≥1 |
| **R3** | 锚文本描述性（目标关键词或变体），禁 click here / learn more / this article |
| **R4** | 同一目标 slug 单篇仅 1 次 `<a>`（首次保留，后续纯文本） |
| **R5** | TL;DR 内链 ≤1；正文内链分散在不同 H2 |
| **R6** | 簇 hub-spoke 双向互链 |
| **R7** | 上下文相关优先；跨簇仅自然工作流延伸（Context Bridge） |

**R4 提醒**：FAQ 不加内链；每篇同 slug 只用 1 种锚文本。
**产品页**：`/floatim`、`/floatcup-2026` 等仅信息性提及，不包转化链接（见 internal-links §5.5）。

---

## 三、簇内链矩阵（应链向 / 应被链自）

> 标记：**✓** = 2026-09-09 优化后实测正文已有该出链；✗ = 可选增强（无自然落点、暂未加）；△ = 入链 ≤1（≥1 已合规）。
> R1/R2/R3/R4（含 2x）/R5、NN 前缀、死链已**全部清零**；剩余 ✗ 仅 1 处：41→50（41 正文为 V4 Preview 语境、无 V4 Pro GA 落点，见 §6.4）。

### 3.1 Scheduling Agent 簇（03 Hub）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `what-is-agentic-calendar` (03) | **Hub** | 02 ✓、04 ✓、05 ✓、06 ✓、07 ✓ | 02 ✓、04 ✓、05 ✓、06 ✓、07 ✓ 及全站高频 ✓ |
| `ai-scheduling-agent` (02) | 定义 | 03 ✓、04 ✓、05 ✓ | 03 ✓、04 ✓、05 ✓、30 ✓、31 ✓、33 ✓、35 ✓、37 ✓ |
| `calendar-driven-ai-vs-chat-ai` (04) | 对比 | 03 ✓、02 ✓ | 03 ✓、06 ✓、35 ✓、36 ✓、37 ✓、38 ✓、40 ✓、47 ✓、56 ✓、58 ✓、87 ✓ |
| `best-ai-scheduling-assistants` (05) | Ranking | 02 ✓、03 ✓ | 02 ✓、03 ✓（原 ×0/单入链已解） |
| `ai-meeting-preparation` (06) | 场景 | 04 ✓、07 ✓、03 ✓ | 03 ✓、07 ✓、36 ✓、40 ✓、56 ✓、87 ✓ |
| `ai-follow-up-automation` (07) | 场景 | 06 ✓、03 ✓ | 03 ✓、06 ✓、36 ✓、56 ✓ |

### 3.2 World Cup 簇（09/10 双 Hub）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `world-cup-2026-guide` (09) | **Hub** | 10 ✓、17 ✓、18 ✓、19 ✓ | 10 ✓、17 ✓ |
| `world-cup-2026-schedule` (10) | **Hub P02** | 17 ✓、18 ✓、09 ✓ | 09 ✓、17 ✓、18 ✓、19 ✓ |
| `world-cup-2026-google-calendar-ics` (17) | 教程 | 10 ✓、09 ✓、18 ✓ | 10 ✓、18 ✓ |
| `floatcup-world-cup-2026-calendar-subscribe` (18) | 产品 | 17 ✓、10 ✓、09 ✓ | 09 ✓、10 ✓、19 ✓ |
| `world-cup-2026-schedule-usa` (19) | 受众 | 10 ✓、18 ✓、09 ✓ | 09 ✓（单入链 △） |

### 3.3 OpenAI 簇（30/57/77 Hub）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `gpt-5-6-sol-terra-luna` (30) | **Hub 模型** | 02 ✓、03 ✓、31 ✓、77 ✓ | 31 ✓、57 ✓、77 ✓ |
| `gpt-5-6-floatboat` (31) | Product | 02 ✓、03 ✓、30 ✓ | 30 ✓、57 ✓ |
| `codex-harness-open-source` (57) | **Hub Harness** | 30 ✓、46 ✓、31 ✓ | 77 ✓（单入链 △；原 ×0 已解） |
| `gpt-6-astra` (77) | **Hub 模型** | 30 ✓、55 ✓、03 ✓、57 ✓、76 ✓ | 30 ✓（单入链 △；原 ×0 已解） |

### 3.4 Claude 簇（35/37/48 Hub + 47 三方桥）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `what-is-claude-cowork` (35) | **Hub** | 36 ✓、47 ✓、48 ✓、37 ✓、04 ✓、03 ✓、02 ✓ | 36 ✓、37 ✓、38 ✓、40 ✓、47 ✓、48 ✓ |
| `best-claude-cowork-alternatives` (36) | Ranking | 35 ✓、47 ✓、03 ✓、06 ✓、07 ✓、04 ✓、87 ✓ | 35 ✓、47 ✓ |
| `what-is-claude-tag` (37) | **Hub** | 38 ✓、35 ✓、48 ✓、01 ✓、04 ✓、03 ✓、47 ✓、02 ✓ | 35 ✓、38 ✓、47 ✓、48 ✓ |
| `best-claude-tag-alternatives` (38) | Ranking | 37 ✓、01 ✓、03 ✓、04 ✓、35 ✓、47 ✓ | 37 ✓、47 ✓ |
| `claude-code-vs-cowork-vs-tag` (47) | 三方桥 | 48 ✓、35 ✓、37 ✓、04 ✓、38 ✓、36 ✓、01 ✓、49 ✓、44 ✓ | 35 ✓、36 ✓、37 ✓、38 ✓、48 ✓、49 ✓ |
| `what-is-claude-code` (48) | **Hub** | 47 ✓、35 ✓、37 ✓、44 ✓、49 ✓ | 35 ✓、37 ✓、47 ✓、49 ✓ |
| `best-claude-code-alternatives` (49) | Ranking | 48 ✓、47 ✓、03 ✓、01 ✓ | 47 ✓、48 ✓ |

### 3.5 DeepSeek 簇（41/46 Hub）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `what-is-deepseek-agent` (41) | **Hub** | 42 ✓、43 ✓、44 ✓、46 ✓、50 ✗ | 42 ✓、43 ✓、44 ✓、46 ✓、50 ✓、51 ✓、53 ✓ |
| `how-to-build-deepseek-agent` (42) | Product | 41 ✓、43 ✓、44 ✓ | 41 ✓、43 ✓、44 ✓ |
| `deepseek-agent-function-calling` (43) | Product | 42 ✓、41 ✓ | 41 ✓、42 ✓、44 ✓、46 ✓ |
| `deepseek-agent-vs-claude-code` (44) | Comparison | 41 ✓、42 ✓、43 ✓ | 41 ✓、42 ✓、46 ✓、47 ✓、48 ✓ |
| `what-is-deepseek-harness` (46) | **Hub** | 43 ✓、50 ✓、44 ✓、41 ✓、52 ✓ | 50 ✓、52 ✓、57 ✓ |
| `deepseek-v4-pro-0813` (50) | 模型 GA | 41 ✓、51 ✓、46 ✓ | 46 ✓、51 ✓、52 ✓、54 ✓ |
| `cordis-plugin-framework` (52) | 插件内核 | 46 ✓、50 ✓、53 ✓ | 46 ✓、53 ✓ |

### 3.6 Voice × Agent 簇（58 Hub · 56 为 Updates 桥）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `what-is-voice-dictation-for-ai-agents` (58) | **Hub** | 59 ✓、60 ✓、73 ✓、70 ✓、75 ✓、04 ✓、56 ✓ | 56 ✓、59 ✓、60 ✓、70 ✓、73 ✓、75 ✓ |
| `voice-mode-vs-dictation-for-ai-agents` (59) | 范式 | 58 ✓、73 ✓、70 ✓、75 ✓、56 ✓ | 58 ✓、60 ✓、61 ✓、70 ✓、73 ✓、75 ✓ |
| `best-voice-dictation-for-ai-agents` (60) | Ranking | 58 ✓、56 ✓、59 ✓ | 58 ✓、75 ✓ |
| `chatgpt-voice-mode-vs-dictation` (70) | Comparison | 58 ✓、56 ✓、59 ✓、73 ✓ | 58 ✓、59 ✓、73 ✓ |
| `what-is-a-voice-agent` (73) | Glossary | 58 ✓、70 ✓、59 ✓、75 ✓、56 ✓ | 58 ✓、59 ✓、70 ✓、75 ✓ |
| `voice-agent-vs-voice-dictation-for-work` (75) | 范式 | 58 ✓、73 ✓、59 ✓、60 ✓、56 ✓ | 58 ✓、59 ✓、73 ✓ |

### 3.7 File Organizer 簇（78 Hub · 2026-08/09 新簇 · backdate 已上线）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `what-is-an-ai-file-organizer` (78) | **Hub** | 79 ✓、80 ✓、81 ✓、82 ✓、83 ✓、84 ✓、85 ✓、86 ✓、39 ✓、40 ✓、03 ✓ | 79 ✓、80 ✓、81 ✓、82 ✓、83 ✓、84 ✓、85 ✓、86 ✓ |
| `file-organizer-vs-file-renamer-vs-file-sorter` (79) | 决策 | 78 ✓、39 ✓、40 ✓、81 ✓、80 ✓ | 78 ✓、80 ✓、81 ✓、82 ✓、83 ✓、85 ✓、86 ✓ |
| `best-ai-file-organizer` (80) | Ranking organizer | 79 ✓、78 ✓、81 ✓ | 78 ✓、79 ✓、81 ✓、84 ✓ |
| `best-ai-file-renamer` (81) | Ranking renamer | 78 ✓、79 ✓、80 ✓ | 78 ✓、79 ✓、80 ✓（原 ×0 已解） |
| `do-ai-file-organizers-upload-your-files` (82) | 隐私 canonical | 78 ✓、79 ✓、40 ✓ | 78 ✓、83 ✓、84 ✓、85 ✓、86 ✓ |
| `ai-file-organizer-mac` (83) | 平台 Mac | 79 ✓、78 ✓、82 ✓、84 ✓ | 78 ✓、79 ✓、84 ✓、85 ✓ |
| `ai-file-organizer-windows` (84) | 平台 Windows | 78 ✓、80 ✓、82 ✓、83 ✓ | 78 ✓、83 ✓、85 ✓（原单入链 △ 已解） |
| `clean-up-downloads-folder-with-ai` (85) | 场景 | 78 ✓、79 ✓、83 ✓、84 ✓、82 ✓、86 ✓ | 78 ✓、86 ✓（原单入链 △ 已解） |
| `organize-receipts-and-invoices-with-ai` (86) | 场景 | 85 ✓、78 ✓、79 ✓、82 ✓ | 78 ✓、85 ✓（原 ×0 已解） |

### 3.8 Obsidian 簇（39 Hub）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `what-is-obsidian-vault` (39) | **Hub** | 40 ✓、04 ✓ | 40 ✓、78 ✓、79 ✓ |
| `how-to-use-obsidian-with-ai-agent` (40) | Product | 39 ✓、04 ✓、06 ✓、35 ✓ | 39 ✓、56 ✓、78 ✓、79 ✓、82 ✓ |

### 3.9 Model 单篇 & Updates（无强 Hub 的松散簇）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `introducing-floatim` (01) | 产品公告 | 历史 slug（见 §6.1） | 37 ✓、38 ✓、47 ✓、49 ✓ |
| `kimi-k3-open-frontier-model` (32) | Kimi K3 Hub | 03 ✓、33 ✓、34 ✓ | 33 ✓、34 ✓、45 ✓ |
| `kimi-k3-floatboat` (33) | Product | 03 ✓、34 ✓、02 ✓、32 ✓ | 32 ✓、34 ✓ |
| `vibe-coding-one-prompt-html-game` (34) | SEO spoke | 33 ✓、03 ✓、32 ✓ | 33 ✓、45 ✓、61 ✓ |
| `what-is-minimax-h3` (45) | MiniMax Hub | 61 ✓、32 ✓、34 ✓、03 ✓ | 51 ✓、61 ✓ |
| `minimax-h3-max-infinite-ai-livestream` (61) | spoke | 45 ✓、59 ✓、34 ✓、03 ✓ | 45 ✓ |
| `grok-4-6` (51) | 对照枢纽 | 45 ✓、50 ✓、41 ✓ | 50 ✓、53 ✓、76 ✓ |
| `grok-bot` (53) | agent 产品 | 51 ✓、52 ✓、41 ✓ | 52 ✓ |
| `glm-5-3` (54) | Model 单篇 | 50 ✓、55 ✓ | 55 ✓（单入链 △） |
| `gemini-3-7-flash` (55) | Model 单篇 | 03 ✓、54 ✓ | 54 ✓、76 ✓、77 ✓ |
| `gemini-3-8-flash` (76) | Model 单篇 | 55 ✓、51 ✓、03 ✓ | 77 ✓（原 ×0 已解；姊妹升级语境由 77 承担） |
| `introducing-flow-mode` (56) | 产品公告 | 04 ✓、06 ✓、07 ✓、40 ✓、58 ✓ | 58 ✓、59 ✓、60 ✓、70 ✓、73 ✓、75 ✓ |
| `what-is-doubao-work` (87) | Standalone | 03 ✓、04 ✓、06 ✓ | 36 ✓（原 ×0 已解） |

---

## 四、跨簇桥（Context Bridge）

| 从 | 到 | 语境 |
|----|-----|------|
| 45 MiniMax H3 | 32/34 | 多模态生成 → vibe coding 视觉推理 |
| 51 Grok 4.6 ↔ 50 DeepSeek V4 | 双向 | 同日发布对照（模型代理能力） |
| 55 Gemini 3.7 ↔ 54 GLM | 双向 | 24h 双发布对照 |
| 57 Codex Harness | 46 DeepSeek Harness | harness 平台横评 |
| 44 DeepSeek vs Claude Code | 47/48 | agent 编程对比 → Claude 簇 |
| 56 Flow Mode | 58–75 voice 簇 | 语音转写产品线与品类词覆盖 |
| 40 Obsidian + AI | 78/79 file-organizer | AI 组织知识 / 文件两种形态 |
| 39 Obsidian vault | 78 file organizer Hub | vault ≠ 文件整理工具边界 |
| 87 Doubao Work | 04/06/03 | 中文办公 Agent 与 Calendar-Driven 对照 |

---

## 五、实测快照（2026-09-09）

> 详细出入链逐篇见 `temp/fb_links_audit.json`（维护脚本 `temp/fb_links_audit.py`）。

**健康度（2026-09-09 全量优化 + 遗留收尾后）**：R1 出链 ≥2 全 59 篇 PASS；R2 库内入链 ≥1 全 59 篇 PASS（零入链 0）；R3 / R4（含 2x 全量重复）/ R5 FAQ 段内链 / NN 前缀 / 死链 **全部为 0 残留**；TL;DR 段各篇 ≤1。§6.4 可选增强亦已执行完毕（2 项跳过，见该节）。

### 5.1 出链 <2（R1 预警 · 口径为库内 slug 出链）

| slug | 库内出链 | 站内出链(含线上) | 现状 |
|------|:---:|:---:|------|
| `what-is-obsidian-vault` (39) | 2 | 2 | ✅ 已补 `04`（§6「What's Next」段），R1 达标 |
| `introducing-floatim` (01) | 0 | 2 | 2 条均指向站内线上-only 历史 slug（sitemap 确认在线，非断链）；R1 达标 |
| `ai-scheduling-agent` (02) | 1 | 2 | 含 1 条线上-only（`ai-agent-solo-operators`）；R1 达标 |

> ✅ 2026-09-09 优化后：R1 无硬缺口（库内口径 39 已修复）。

### 5.2 零入链（R2 缺口 · 优先级自上而下）— ✅ 全部已补（2026-09-09）

| slug | 簇 | 实际补入链来源 |
|------|----|---------------|
| `best-ai-file-renamer` (81) | file-organizer | 78 Hub + 79 + 80（§1/§4/§5 语境） |
| `organize-receipts-and-invoices-with-ai` (86) | file-organizer | 78 Hub + 85（姊妹场景互链） |
| `best-ai-scheduling-assistants` (05) | scheduling | 03 Hub §4.1（四代框架选型句） |
| `codex-harness-open-source` (57) | openai | 77 §3.2（ARC-AGI harness 差量化语境） |
| `gemini-3-8-flash` (76) | model | 77 §3.3（DeepSWE 独立对照语境；替代原 55 建议） |
| `gpt-6-astra` (77) | openai | 30 TL;DR Update（GPT-5.6 → GPT-6 换代桥） |
| `what-is-doubao-work` (87) | standalone | 36 §5 platform bundling（中国 IM 生态对照） |

---

## 六、发现与补链待办

### 6.1 P0 — 站内断链 / 可疑目标 — ✅ 已修复（2026-09-09）

| slug | 链接 | 处理 |
|------|------|------|
| 45 `what-is-minimax-h3` | `/blog/32-kimi-k3-open-frontier-model`、`/blog/34-vibe-coding-one-prompt-html-game` | ✅ 已去 NN 前缀 |
| 61 `minimax-h3-max-infinite-ai-livestream` | `/blog/34-vibe-coding-one-prompt-html-game` | ✅ 已去 NN 前缀 |

> ✅ 复核结论：站内目标全集 = 本地 59 篇 + 线上 sitemap 75 篇（`blog-live-articles.md`），凡命中者均为**有效链接**；此前疑似的 `ai-agent-solo-operators`、`how-one-person-businesses-work-like-a-team-with-ai` 等均在线上 sitemap 中（在线），**非断链**。全库未发现指向不存在文章的站内死链。

### 6.1b P1 — R4 同 slug 高频重复链接（>2 次）— ✅ 已收敛（2026-09-09）

原识别（>2 次组）全部处理为「首次超链 + 后续纯文本」：

| slug | 目标 | 原次数 | 处理 |
|------|------|:---:|------|
| `introducing-flow-mode` (56) | `ai-meeting-preparation` | 4 | ✅ 仅 L69 保留 |
| `introducing-flow-mode` (56) | `ai-follow-up-automation` | 4 | ✅ 仅 L69 保留 |
| `deepseek-agent-function-calling` (43) | `how-to-build-deepseek-agent` | 4 | ✅ 仅 L26 保留 |
| `what-is-doubao-work` (87) | `what-is-agentic-calendar` | 3 | ✅ 仅 §5.1 表注保留 |
| `what-is-doubao-work` (87) | `calendar-driven-ai-vs-chat-ai` | 3 | ✅ 仅 §5.1 表注保留 |

> ✅ FAQ 段 9 处站内内链已全部改纯文本（30/32/37/40/42/44/56/87 等），R5 FAQ=0 达成。
> ✅ 遗留 2x 组已于 2026-09-09 二次收尾全部降为 1 次：`gpt-5-6-floatboat`、`kimi-k3-floatboat`、`what-is-claude-tag`、`best-claude-tag-alternatives`、`how-to-use-obsidian-with-ai-agent`（2 组）、`how-to-build-deepseek-agent`、`introducing-flow-mode` 共 **8 组全部唯一化**（保留正文叙述主线处，TL;DR/收尾指引处改纯文本）。当前全库无任何同 slug 重复链。

### 6.2 P1 — 补链建议 — ✅ 全部执行完毕（2026-09-09）

| 动作 | 入口 → 目标（语境） | 状态 |
|------|---------------------|------|
| 补入链 | 80 `best-ai-file-organizer` → `best-ai-file-renamer`（「名字好但文件夹乱 / 只要改名买 renamer」分叉段） | ✅ |
| 补入链 | 85 `clean-up-downloads-folder-with-ai` → `organize-receipts-and-invoices-with-ai`（票据类文件清理延伸） | ✅ |
| 补入链 | 03 `what-is-agentic-calendar` → `best-ai-scheduling-assistants`（「选型榜单」指向） | ✅ |
| 补入链 | 77 `gpt-6-astra` → `codex-harness-open-source`（ARC-AGI harness 差量化语境；以 77 实现） | ✅ |
| 补入链 | 77 `gpt-6-astra` → `gemini-3-8-flash`（DeepSWE 独立对照语境；替代原 55 建议，76 已获入链） | ✅ |
| 补入链 | 30 `gpt-5-6-sol-terra-luna` → `gpt-6-astra`（TL;DR Update：GPT-5.6 → GPT-6 换代桥） | ✅ |
| 结构性 | 78 Hub 链向 79–86 各 spoke（各 1 条，分散在不同 H2）；79→80/81、83→84、85→86 补齐对称互链 | ✅ |

### 6.3 content-graph 同步 — ✅ 已完成（2026-09-09）

- skill 内 `content-graph.md` 已登记 **#76 gemini-3-8-flash、#77 gpt-6-astra、#78–#86 file-organizer、#87 what-is-doubao-work**（文件表 12 行）；「下一序号」已改 **88**；Cluster 注册表补充 `file-organizer` 簇并回填 openai(77)/model-singles(76)；新增 §3G File Organizer Hub-Spoke 结构图。
- 若在本文档维护矩阵，请同步回填 content-graph 的文件表与 Cluster 注册表（本次已同步）。

### 6.4 可选增强（✗ 低优先级）— ✅ 全部执行完毕（2026-09-09）

下表为原「应链但缺失」的锦上添花项，已全部按语境补链；2 项经核实无自然落点跳过：

| 建议 | 状态 | 实际位置 |
|------|------|------|
| 02 `ai-scheduling-agent` → 04/05 | ✅ 两条 | 04 @L140（Gen4 vs 三代对照）；05 @L105（评估选型五问段） |
| 06 `ai-meeting-preparation` → 03 | ✅ | @L81（calendar-triggered prep 归属段） |
| 09 `world-cup-2026-guide` → 17 | ✅ | @L164（§8 时区处理段） |
| 17 `world-cup-2026-google-calendar-ics` → 18 | ✅ | @L33（ICS 静态导入局限段） |
| 18 `floatcup...subscribe` → 09 | ✅ | @L40（§1 Step 2 订阅内容段） |
| 19 `world-cup-2026-schedule-usa` → 09 | ✅ | @L44（USMNT 出线路径语境） |
| 32 `kimi-k3-open-frontier-model` → 34 | ✅ | @L136（视觉反馈回路段） |
| 41 `what-is-deepseek-agent` → 46/50 | ✅ 46；⏭️ 50 跳过 | 46 @L149（官方 harness 段）；50 因正文为 V4 Preview(Apr) 语境、无 V4 Pro GA 落点 |
| 46 `what-is-deepseek-harness` → 52 | ✅ | @L87（built on Cordis 架构段） |

---

## 七、维护节奏

| 时机 | 动作 |
|------|------|
| 每篇新稿发布前 | 对照 §3 对应簇「应链向」落实内链；跑 `tools/link_checker.py {file}` |
| 每篇新稿发布后 | 回填本文档 §1 表、§3 矩阵（✓）与 §5 快照；同步 `content-graph.md`、`README.md` |
| 每批 ≥3 篇后 | 扫 §6.2 待办，对零入链补 1 条/篇（有自然语境时） |
| 快照刷新 | 重跑 `python temp/fb_links_audit.py`，更新本文档 §5 与「快照」日期 |

---

*Floatboat blog · blog-structure-internal-links · v1.0 · 2026-09-09（59 篇实测快照）*
