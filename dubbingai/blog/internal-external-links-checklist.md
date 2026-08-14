# Internal & External Links Checklist（Dubbing AI Blog）

> **依据**：与 [ThetaWave blog internal-external-links-checklist](../../thetawave/blog/internal-external-links-checklist.md) 同一思路；站点以 **dubbingai.io** 为准；正文为 **英文**，本规范为 **中文**。  
> **产品语境**：[dubbingai.md](../dubbingai.md) · **全站内链总纲**：[dubbingai-internal-links.md](../dubbingai-internal-links.md) · **关键词映射**：[dubbingai-keywords.md](../dubbingai-keywords.md)

**适用范围**：`blog/` 根目录 **2026 新稿**（`01-`…`04-`）适用下文互链矩阵硬性要求。**`cms-export/`** 第一阶段为 CMS 忠实镜像，`related` / 首段互链 / 竞品 nofollow **暂不强制**（见 [cms-export/README.md](./cms-export/README.md)）。

---

## 链接分层（Dubbing AI Blog）

| 类型 | 路径 / URL | 用途 |
|------|------------|------|
| **Blog 互链** | `https://dubbingai.io/blog/{slug}` | 相关主题文章；与 **frontmatter `related`** 数组一致 |
| **核心转化** | `https://dubbingai.io/`、`/download-desktop` | 首页、桌面端下载 |
| **Voice Changer 线** | `/voice-changer`、`/all-voice-changers`、`/voice-changer/{slug}` | 产品与程序化角色/游戏页；稿内强相关时再链 |
| **平台页** | `/discord-voice-changer`、`/zoom-voice-changer`、`/vrchat-voice-changer` 等 | 与稿内平台一致时链 |
| **功能线** | `/voice-cloning`、`/online-voice-changer`、`/community-sounds`、`/soundboard` | 克隆、在线变声、社区音效、音效板 |
| **工具 / 资源** | `/sound-effect-generator`、`/supported-apps`、`/questions`、`/explore` | 与稿内任务一致；**Sound Effect Generator** 与 **Community Sounds** 意图分流见 [dubbingai-sound-effect-generator.md](../dubbingai-sound-effect-generator.md) |
| **硬件** | `https://shop.dubbingai.io/` | Dubbing Box 等 |
| **FAQ** | `/questions`（非 `/faq`） | 官方问答 |

---

## Internal Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **首段或第二段** | ≥1 条 | **Blog 互链**（相关 slug）或核心产品入口，满足意图分流 |
| **Body Blog 互链** | 每篇 **1–4 条**（随博文数量增长） | 链至 **`/blog/{slug}`**；锚文本描述主题（ranking vs how-to vs Assistant） |
| **产品 / 转化内链** | 按节分布 | **download-desktop、discord-voice-changer、online-voice-changer** 等宜分散在不同 **H2**，避免同段堆砌 |
| **文末 Related** | 由 **frontmatter `related`** + 正文 **Next steps** 承担 | 与互链表一致 |
| **锚文本** | 描述性 | 避免 "click here"；可混合 exact / partial / **Dubbing AI** 品牌 |

---

## External Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **权威** | 按需 | 平台帮助文档（如 Google Assistant）、游戏/平台官方说明；**可核对** |
| **竞品 / 第三方工具** | 对比稿必备 | 与 [dubbingai-competitors.md](../dubbingai-competitors.md) 一致；`rel="nofollow noopener"` 按法务与站点惯例 |
| **E-E-A-T** | 可引用来源 | 数据、政策、菜单路径注明出处 |

---

## 博文互链矩阵（Blog ↔ Blog）

用于写稿与修订时快速对齐 **who links whom**；上线后同步更新 **frontmatter `related`**。

| slug | 指向其他博文（建议正文至少出现 1 次锚文本） |
|------|-----------------------------------------------|
| `best-ai-voice-changer` | → `how-to-change-google-assistant-voice`（意图分流）· → `how-to-change-your-voice`（榜单 vs 实操） |
| `how-to-change-google-assistant-voice` | → `best-ai-voice-changer`（实时变声选型）· → `how-to-change-your-voice`（路由与 Web/PC） |
| `how-to-change-your-voice` | → `best-ai-voice-changer`（工具对比）· → `how-to-change-google-assistant-voice`（Assistant vs 自己麦克风） |
| `dubbing-ai-vs-voicemod` | → `best-ai-voice-changer`（更广对比）· → `how-to-change-your-voice`（路由/setup）· → `how-to-change-google-assistant-voice`（Assistant 误搜分流） |

**4-Spoke 角色**：`best-ai-voice-changer` 偏 **选型**；`how-to-change-your-voice` 偏 **怎么做**；`how-to-change-google-assistant-voice` 偏 **系统助手 TTS**；`dubbing-ai-vs-voicemod` 偏 **双产品对比**。

---

## 文章链接状态

新稿入库后在 [README.md](./README.md) 登记表补充一行，并在下表记录内链 / 外链抽检状态。

| # | 文章 slug | 内链 Body（Blog+产品） | `related` | 外链 | 已优化 |
|---|-----------|-------------------------|-----------|------|--------|
| 01 | `best-ai-voice-changer` | ✅ | `how-to-change-google-assistant-voice`, `how-to-change-your-voice` | 竞品站按需 | ✅ |
| 02 | `how-to-change-google-assistant-voice` | ✅ | `best-ai-voice-changer`, `how-to-change-your-voice` | Google Help | ✅ |
| 03 | `how-to-change-your-voice` | ✅ | `best-ai-voice-changer`, `how-to-change-google-assistant-voice` | — | ✅ |
| 04 | `dubbing-ai-vs-voicemod` | ✅ | `best-ai-voice-changer`, `how-to-change-your-voice`, `how-to-change-google-assistant-voice` | Voicemod 官网 | ✅ |

---

## CMS 镜像抽检（cms-export/）

第一阶段验收：frontmatter 完整、H1 与 title 一致、无导航/footer 泄漏。互链优化属第二阶段。

| 批次 | 抽检 slug | frontmatter | 正文结构 | 内链可点击 | 备注 |
|------|-----------|-------------|----------|------------|------|
| P0 | `dubbing-ai-vs-voicemod` | ✅ | ✅ (H2=5) | ✅ | 试点 |
| P0 | `how-to-get-voice-changer-on-discord` | ✅ | ✅ (H2=7) | ✅ | 试点 |
| P0 | `jett-voice-changer` | ✅ | ✅ (H2=5) | ✅ | 试点 |
| P0 | `minecraft-soundboard` | ✅ | ✅ (H2=6) | ✅ | 试点 |
| P0 | `dubbing-ai-trump-voice` | ✅ | ✅ (H2=4) | ✅ | 试点 |

全量：**256 done** · **1 skip**（`hello-world`）· **0 error** — 见 [cms-export/manifest.csv](./cms-export/manifest.csv)。

---

## 规范总结

- **内链**：首段意图分流 + Body **blog 互链** + 分布式产品页；与 [dubbingai-internal-links.md](../dubbingai-internal-links.md) **§8.2 上下文内链**、**§8.3 自检** 一致。
- **外链**：权威帮助文档为主；竞品 **nofollow**。
- **维护**：新博文上架 → 更新本矩阵、**README 列表**、必要时回写旧文 `related` 与「相关一句」内链。
