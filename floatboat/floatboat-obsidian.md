# Floatboat for Obsidian — 产品与内容方案

> 产品营销 / SEO / 文案方案。**不含页面搭建说明**（组件、路由实现、blueprint 见其他建站文档）。  
> **状态**：方案定稿 · 待落地页与 Integrations 上线  
> **更新**：2026-07-28  
> **关联内容**：博客 Hub–Spoke  
> - [blog/39-what-is-obsidian-vault.md](./blog/39-what-is-obsidian-vault.md)  
> - [blog/40-how-to-use-obsidian-with-ai-agent.md](./blog/40-how-to-use-obsidian-with-ai-agent.md)

---

## 1. 决策摘要

| 项 | 结论 |
|----|------|
| **主战场** | 独立落地页 **`/obsidian`**（Floatboat for Obsidian） |
| **辅入口** | [`/integrations`](https://floatboat.ai/integrations) Docs & Notes 增加 Obsidian 卡 → 链到 `/obsidian` |
| **教育层** | 博客 39（vault 定义）+ 40（how-to + agent 排名） |
| **不做主产品** | Obsidian [Community Plugin](https://community.obsidian.md/)（红海 AI 插件 + 运行时错位） |
| **产品诚实度** | 承诺「授权本机 vault 文件夹 + 跨应用/日历执行」；**不**声称「已上架 Community Plugin」 |

**一句话定位**

> Obsidian keeps the library (local Markdown vault). Floatboat runs the courtyard — calendar-triggered agents that read the vault alongside email, drives, and local files.

**隐喻（对外英文可用）**

> Most apps are one room in a courtyard. An Obsidian vault is the library. Floatboat wires the courtyard so agents can move between rooms with permission.

---

## 2. 为何是「反过来集成」而不是做插件

| 方向 | 建议 | 理由 |
|------|------|------|
| Floatboat → Community Plugin | **不主推** | 插件跑在 Obsidian 进程内，会与 Copilot / Claudian / Smart Connections 等同质竞争；Floatboat 差异化是日历运行时 + 跨应用，不是库内聊天 |
| Obsidian vault → Floatboat | **推荐** | Vault 本质是本机文件夹；Floatboat 已叙事「读本地文件」+ MCP/工具连接；零插件即可开始 |
| 可选加深 | 后续 | Local REST API / MCP bridge、Combo「Vault → Meeting Brief」、URI「Open in Floatboat」小工具 |

参考：现网 Integrations 已强调 *Reads your local files in place* 与 Docs & Notes（Notion、Word 等）——Obsidian 是同一层的自然延伸，见 [floatboat.ai/integrations](https://floatboat.ai/integrations)。

---

## 3. 方案组合（推荐 C）

| 方案 | 内容 | 角色 |
|------|------|------|
| A | 仅 Integrations 卡片 | 发现入口，SEO 弱 |
| B | 仅 `/obsidian` Landing | SEO + 转化主页 |
| **C（采用）** | **B 为主 + A 为入口** | Hub 分发 + 专页转化 |

---

## 4. SEO 与 Meta

| 项 | 值 |
|----|-----|
| **路径（首选）** | `/obsidian` |
| **备选** | `/floatboat-for-obsidian`（更贴 “for X” 搜索，略长） |
| **Primary keyword** | Floatboat for Obsidian |
| **Secondary** | Obsidian AI agent, use Obsidian with Floatboat, Obsidian vault desktop agent |
| **Avoid** | Obsidian alternative, Obsidian plugin（意图错位） |
| **`<title>`** | Floatboat for Obsidian — AI Agent for Your Local Vault |
| **Meta description** | Keep your Obsidian vault as local Markdown. Floatboat runs prep, drafts, and file work from your calendar across apps — without replacing Obsidian. |
| **H1** | Floatboat for Obsidian |
| **Hero 副文** | Your vault stays on disk. Agents use it with calendar, email, and folders. |
| **Sitemap** | 上线后收录 `/obsidian`；建议同步把 `/integrations` 纳入 sitemap |

---

## 5. 受众与 CTA

| 项 | 说明 |
|----|------|
| **目标读者** | 已有或准备建 Obsidian vault 的 solopreneur / consultant；需要跨应用执行，而非只在库内 AI 聊天 |
| **主 CTA** | Download Floatboat → `/download` |
| **次 CTA（可选）** | Read the guide → `/blog/how-to-use-obsidian-with-ai-agent` |

---

## 6. 内容叙事顺序（给文案 / 落地页作者）

落地页信息架构建议按下列顺序讲清故事（实现方式由建站文档决定）：

1. **Hero** — 不是插件；vault 仍是你的；Floatboat 跨应用用它。  
2. **Why Floatboat** — 授权文件夹、日历触发、会前/截止日、文件整理链。  
3. **How it works** — 三步可执行，降低「要不要装插件」焦虑。  
4. **Comparison** — 和 Copilot / Cowork 等分工；Floatboat 强调日历 + 跨应用。  
5. **Who it’s for** — solopreneur 优先。  
6. **FAQ** — 边界与异议（是否插件、会否覆盖 vault、与 Copilot 关系）。  
7. **CTA** — 下载。

---

## 7. 英文文案草案

### 7.1 Hero

| 字段 | 文案 |
|------|------|
| H1 | Floatboat for Obsidian |
| Sub | Keep your vault as local Markdown. Let calendar-driven agents use it across email, drives, and folders — without replacing Obsidian. |
| CTA | Download free for Mac & Windows |
| Trust line（可选） | Not an Obsidian Community Plugin. Your notes stay files on disk. |

### 7.2 Why Floatboat for Obsidian（4 点）

| # | Title | Body |
|---|-------|------|
| 01 | Authorize the vault folder — no plugin required | Point Floatboat at your Obsidian vault path. Agents read the same `.md` files you already trust. |
| 02 | Calendar runs the work | Meetings and deadlines trigger prep and drafts from project notes — not another chat sidebar to remember. |
| 03 | Cross-app, not vault-only | Pull context from vault + mail + local PDFs in one pass. Obsidian stays the library; Floatboat runs the courtyard. |
| 04 | Tidy the hallway when files pile up | Pair with the [AI File Organizer](https://floatboat.ai/ai-file-organizer): chat → preview tree → approve. On-device sorting for Downloads and project dumps. |

### 7.3 How it works（3 步）

| Step | Title | Body |
|------|-------|------|
| 01 | Point it at your vault | Create or open an Obsidian vault. Confirm the folder path. Grant Floatboat access with least privilege. |
| 02 | Attach a job to the calendar or a project | “Brief for tomorrow’s Acme call using `Projects/Acme`.” Or let the event trigger prep automatically. |
| 03 | Review, then write back selectively | Keep evergreen notes curated. Promote only what belongs in the vault; leave drafts in an AI Inbox if you prefer. |

### 7.4 对比表（建议列）

| Approach | Best for | Trigger | Lives in |
|----------|----------|---------|----------|
| **Floatboat** | Calendar-driven projects across vault + apps | Calendar / deadline | Desktop agent OS |
| In-vault AI (e.g. Copilot) | Chat, search, edits while writing | You in Obsidian | Obsidian plugin |
| Coding-agent embeds (e.g. Claudian) | Vault as Claude Code / Codex workspace | You + CLI agent | Obsidian + CLI |
| Claude Cowork | Anthropic folder batches | You start a task | Claude app |

表后可跟：You can stack in-vault tools for writing and Floatboat for delivery. One chat sidebar should not own every job shape.

细节与博客 [40 §6 排名](./blog/40-how-to-use-obsidian-with-ai-agent.md) 保持一致；落地页表可更短。

### 7.5 FAQ（最少 5）

1. **Is Floatboat an Obsidian plugin?**  
   No. It is a native Mac/Windows agent OS. You authorize the vault folder like any other local directory. We are not listing a required plugin on [community.obsidian.md](https://community.obsidian.md/).

2. **Will Floatboat replace Obsidian?**  
   No. Obsidian owns linking, graph, and daily thinking. Floatboat owns cross-app execution from your schedule.

3. **Can it overwrite my notes?**  
   Only with write permission and your approval on destructive batches. Start read-only or use an AI Inbox folder. File moves via the organizer use preview → approve.

4. **How is this different from Copilot for Obsidian?**  
   Copilot optimizes work *inside* the vault. Floatboat runs jobs that need the vault *plus* calendar, email, and other folders.

5. **Do I need Sync or Publish?**  
   No. A local vault folder is enough. Sync is Obsidian’s optional add-on.

6. **What about MCP?**（可选）  
   Advanced setups can expose the vault via MCP to other clients. Floatboat’s default path is folder authorization in the desktop app; MCP is optional plumbing, not required to start.

### 7.6 Final CTA

| 字段 | 文案 |
|------|------|
| Title | Run your Obsidian vault with the rest of your week |
| Body | Download Floatboat. Authorize the folder. Let the calendar pull notes into real deliverables. |
| CTA | Download Floatboat |

### 7.7 Integrations 卡片（`/integrations`）

| 字段 | 文案 |
|------|------|
| Category | Docs & Notes |
| Name | Obsidian |
| Blurb | Local Markdown vaults — authorize the folder; agents use your notes with calendar and apps. |
| Link | `/obsidian` |

可选：在 “Reads your local files in place” 段增加半句：*including Obsidian vaults*.

---

## 8. 内链矩阵

| From | To | 锚文本意图 |
|------|-----|-----------|
| `/obsidian` | `/blog/what-is-obsidian-vault` | what an Obsidian vault is |
| `/obsidian` | `/blog/how-to-use-obsidian-with-ai-agent` | how to use Obsidian with an AI agent |
| `/obsidian` | `/ai-file-organizer` | AI File Organizer |
| `/obsidian` | `/integrations` | integrations hub |
| `/obsidian` | `/use-cases/for-solopreneur` | solopreneur |
| `/obsidian` | `/download` | CTA |
| `/integrations` | `/obsidian` | Obsidian card |
| Blog 39 / 40 | `/obsidian` | **待补**：落地页上线后在 TL;DR 或 Conclusion 加产品 CTA |
| Blog 40 | `/ai-file-organizer` | 已有 |

---

## 9. 可承诺 vs 不可夸大

### 可承诺（与当前产品叙事一致）

- 本机 Mac/Windows 授权 vault（文件夹）路径  
- 按日历/项目使用笔记做 prep、draft、跨应用组装  
- 链到 on-device [AI File Organizer](https://floatboat.ai/ai-file-organizer)  
- 与「3500+ tools / local files」Integrations 叙事一致  

### 不可写死（除非工程已交付）

- 「Install Floatboat from the Obsidian Community Plugin directory」  
- 「Official Obsidian partner plugin」  
- 深度 wikilink/图谱 API 能力（未接 Local REST / MCP 前）  
- 「Better than Obsidian for note-taking」  

---

## 10. 内容与上线分期

| 期 | 交付 |
|----|------|
| **P0** | `/obsidian` 落地页上线（文案以本文为准；搭建另案）+ 下载 CTA |
| **P0** | 博客 39、40 补链 `/obsidian` |
| **P1** | `/integrations` Obsidian 卡 |
| **P1** | sitemap 收录 `/obsidian`（及 `/integrations`） |
| **P2** | Combo「Vault → Meeting Brief」或说明文；可选 MCP/REST 高级说明 |
| **Backlog** | 「Open in Floatboat」URI 小工具（非完整 Community Plugin） |

---

## 11. 文案验收（与实现解耦）

- [ ] H1 / Title / Meta 与 §4 一致  
- [ ] FAQ 明确 **不是** Community Plugin  
- [ ] 文案内链覆盖博客 39、40、`/ai-file-organizer`、`/download`  
- [ ] 对比不贬低 Obsidian；强调互补  
- [ ] 无「Obsidian alternative」作主词  
- [ ] Integrations 卡文案指向 `/obsidian`  

---

## 12. 相关文档

| 文档 | 用途 |
|------|------|
| [floatboat.md](./floatboat.md) | 产品总定位 |
| [floatboat-features.md](./floatboat-features.md) | 功能与关键词映射 |
| [floatboat-site-structure.md](./floatboat-site-structure.md) | 路由与 sitemap 现状 |
| [blog/39-what-is-obsidian-vault.md](./blog/39-what-is-obsidian-vault.md) | Vault 定义 Hub |
| [blog/40-how-to-use-obsidian-with-ai-agent.md](./blog/40-how-to-use-obsidian-with-ai-agent.md) | How-to + agent 排名 |

页面搭建（组件、blueprint、实现）→ 使用其他建站文档，不在本文范围。

---

*Floatboat for Obsidian · content plan v1.1 · 2026-07-28*
