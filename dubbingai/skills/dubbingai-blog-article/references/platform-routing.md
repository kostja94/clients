## §PR — 意图路由与 CTA 分层

> Phase 0 / Phase 4 加载

### 1. 意图 → 落地页（创作内链必查）

| 用户意图 | 动作词 | 主链 | 次级 |
|---------|--------|------|------|
| 下载桌面实时变声 | download, install, free | `/download-desktop` | `/` |
| Discord 设置 | Discord, virtual mic, voice chat | `/discord-voice-changer` | `/blog/how-to-change-your-voice` |
| 在线/上传 | online, browser, upload file | `/online-voice-changer` | — |
| 现成 meme 音效 | soundboard, meme, play sound | `/community-sounds` | `/soundboard` |
| AI 生成 sfx | generate, text to sound, AI sfx | `/sound-effect-generator` | **禁** 当 community-sounds |
| 克隆 | clone, custom voice | `/voice-cloning` | — |
| 硬件/主机 | PS5, Switch, Xbox, mobile box | `https://shop.dubbingai.io/` | `/supported-apps` |
| 角色 preset | Gojo, Jett, anime, game character | `/voice-changer/{slug}` | `/all-voice-changers` |
| 平台兼容列表 | supported apps, games | `/supported-apps` | — |
| FAQ / 支持 | help, questions | `/questions` | — |
| 选型 roundup | best, compare, top picks | `/blog/best-ai-voice-changer` | `/blog/dubbing-ai-vs-voicemod` |
| 竞品对比 | vs Voicemod, alternative | `/blog/dubbing-ai-vs-voicemod` | 竞品外链 nofollow |

### 2. 术语分流（P4）

| 用户说… | 正确目标 | 错误目标 |
|---------|---------|---------|
| free sound effects download | `/community-sounds` | `/sound-effect-generator` |
| AI sound effect generator | `/sound-effect-generator` | `/community-sounds` |
| meme soundboard for streaming | `/soundboard` · `/community-sounds` | 仅 homepage |
| sound gallery / sfx hub | `/community-sounds/sfx` | generator |

### 3. CTA 分层

| 读者阶段 | CTA 文案方向 | URL |
|---------|-------------|-----|
| Awareness / 选型 | Compare tools · Explore voices | `/blog/best-ai-voice-changer` · `/explore` |
| Consideration | Download free · Try Discord page | `/download-desktop` · `/discord-voice-changer` |
| Setup | Fix routing · Platform guide | `/blog/how-to-change-your-voice` |
| Hardware | Shop Dubbing Box | `shop.dubbingai.io` |

**硬规则**：全文 CTA ≤2；Track C 可在 Key Takeaways 后 1 次 + Conclusion 1 次。

### 4. 内链分布

- 首段或第二段：≥1 blog 互链（意图分流）或核心产品入口
- Body：blog 互链 1–4 条；产品页分散在不同 H2
- 避免同段堆砌 3+ 产品链接

### 5. 锚文本

| 好 | 差 |
|----|-----|
| Discord voice changer setup | click here |
| Best AI Voice Changer (2026) roundup | read more |
| Dubbing AI download page | this link |

混合 exact / partial / 品牌名 **Dubbing AI**。

### 6. 外链

- 竞品/第三方工具：`rel="nofollow noopener"`
- 平台官方帮助（Google Assistant、Discord docs）：可 follow，须可核对

### 7. Persona 路由

| Persona | 优先链 | 文章类型 |
|---------|--------|---------|
| Ranked gamer | `/download-desktop` · `/discord-voice-changer` | HowTo · PlatformGuide |
| Streamer + memes | `/soundboard` · `/community-sounds` | Comparison · SoundboardPick |
| Anime/character fan | `/voice-changer/{slug}` | CharacterBridge |
| Mobile/console | `shop.dubbingai.io` | HardwareGuide |
| Assistant confused user | `/blog/how-to-change-google-assistant-voice` | IntentSplit |
