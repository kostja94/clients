## §12 证据链与引用标准

### 12.1 引用分级

| 级别 | 触发条件 | 要求 |
|------|---------|------|
| **P0 必须引用** | Dubbing 产品数字、竞品定价、平台政策路径 | 官网 URL + `as of {month} {year}` |
| **P1 应当引用** | Voicemod/Voice.ai 能力、游戏/platform 设置步骤 | 官方 docs/help |
| **P2 可不引用** | 通用 routing 逻辑、主观 UX 偏好 | 注明 "in our testing" 或限定 persona |

### 12.2 Dubbing AI 产品引用（P0）

> Dubbing AI lists **500+ character voices** and **100,000+ soundboard sounds** on its homepage as of June 2026 — confirm current limits on [dubbingai.io](https://dubbingai.io/) before purchasing.

**硬规则**：禁 CMS 遗留「1000 tones」；latency/CPU 用「marketed」「verify on your rig」。

### 12.3 竞品引用（P1）

> [Voicemod Pro](https://www.voicemod.net/) pricing and VoiceLab features are documented on Voicemod's official site — figures change; verify before buying.

Markdown 外链竞品：`rel="nofollow noopener"`。

### 12.4 Live vs File 引用（P2）

> Murf is built for **recording → AI voice** workflows, not replacing a **live** Discord game microphone — same category boundary as in our [Best AI Voice Changer](https://dubbingai.io/blog/best-ai-voice-changer) roundup.

### 12.5 平台官方引用（P1）

Google Assistant menu paths、Discord settings — link Google Help / Discord support; include as-of note when UI changes.

### 12.6 反模式

| 反模式 | 修复 |
|--------|------|
| 裸引 500+ voices 无 as-of | 加 as-of + 链官网 |
| Easeus 等第三方当 Voicemod 官方源 | 换 voicemod.net / support.voicemod.net |
| 「studies show gamers prefer」 | 删或给来源 |
| 锚文本 click here | 语义化 |

### 12.7 Source Map 模板

```markdown
## Source Map
| Claim | § | Source | Checked | Confidence |
|------|---|--------|---------|:---:|
| 500+ voices | §2 | dubbingai.io | 2026-06-16 | High |
| Voicemod Pro ~$50/yr | §4 | support.voicemod.net | 2026-06-16 | Medium |
| Murf not live mic | §3 | murf.ai + category test | 2026-06-16 | High |
```

Confidence: High = 官网一手 / Medium = 第三方 pricing 聚合 / Low = 不可用于核心论证。

### 12.8 跨篇数字一致性

同一数字跨篇须 as-of 一致；Canonical 最完整上下文在 Hub #01 或 Alternative #04。

### 12.9 引用优先级（6 级）

引用来源按可信度排序。Low 级别的来源不得用于核心论证。

| 级别 | 来源类型 | 可信度 | 示例 |
|:---:|------|:---:|------|
| **L1** | 官方文档 / changelog / GitHub repo | **最高** | dubbingai.io, voicemod.net, voice.ai, support.discord.com |
| **L2** | 标准组织 / 平台帮助中心 | 高 | Google Help, Discord Support, OBS Wiki |
| **L3** | 一手研究 / 年度行业报告 | 高（如有链接） | Streamlabs State of Streaming, Gartner（如有可查证链接） |
| **L4** | 权威媒体 / 行业分析 | 中 | TechCrunch, The Verge, PC Gamer |
| **L5** | 二手 SEO/blog 资料 / 价格聚合 | 中偏低 | 第三方 pricing 聚合站；Easeus 等 Voicemod 第三方评测 |
| **L6** | Reddit / forum / social | **最低** | 仅可作为用户观点引用，不作为事实依据 |

**硬规则**：
- L1–L2: 可用于核心论证
- L3: 有链接可用，无链接降为 L4
- L4–L5: 仅用于补充/背景，不能作为唯一来源
- L6: 禁止用于产品能力/竞品描述/pricing 声明
- Easeus 等第三方不得作为 Voicemod 官方源 → 必须换 voicemod.net / support.voicemod.net
