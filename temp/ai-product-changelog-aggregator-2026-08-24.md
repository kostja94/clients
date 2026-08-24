# AI 产品 Changelog 聚合页

> **检索基准日**：2026-08-24  
> **时间范围**：默认近 90 天（2026-05-26 起）；下文「统一时间线」聚焦 2026-07 至 2026-08  
> **检索约束**：按 [web-deep-search-spec.md](../web-deep-search-spec.md) v1.3，未读取客户业务文档；事实均来自 Tier 0 官方 changelog / release notes  
> **定位**：① 行业 changelog 聚合草稿；② **Vatt** `vatt.ai/changelog` 落地与接入方案（§9–§14）  
> **范式参考**：[Midjourney Updates](https://updates.midjourney.com/)、[Runway Changelog](https://runway.com/changelog)、[Quizlet News](https://quizlet.com/blog/news)、[Wayground Product Updates](https://wayground.com/home/product-updates?lng=en)  
> **维护**：行业线每周扫 §2 → 追加 §4；Vatt 线按 §14 发布 SOP

---

## 1. 执行摘要

2026 年 7–8 月，主流 AI 产品的更新高度集中在 **Agent 化**（Cursor Origin、Runway Agent 2.0、Perplexity Computer、Grok Bot）、**模型迭代**（Claude Opus 5 / Sonnet 5、Grok 4.6、Gemini 3.7 Flash、GPT-5.6 Sol Ultrafast）和 **平台互操作**（MCP 接入、Microsoft 365 / Google Workspace 插件、代码托管与 CI 集成）三条主线。  
各产品官方 changelog 形态不一：Runway / Cursor / Lovable 有独立 changelog 页；Midjourney 用 Ghost 博客；OpenAI / Anthropic 分产品 release notes；Perplexity 混用 `/changelog` 与 Hub blog。  
本页先建立 **来源注册表 + 统一时间线 + 单篇候选标记**，便于后续决定是否拆成 floatboat 式 Updates 文章或独立 `/product-updates` 落地页。

---

## 2. 官方 Changelog 来源注册表

按产品类别列出 **Tier 0** 一手来源。聚合时只以这些 URL 为事实依据。

### 2.1 大模型 / API 平台

| 产品 | 官方 Changelog / News | 形态 | 更新频率 |
|------|----------------------|------|----------|
| **OpenAI** | [Release Notes](https://openai.com/products/release-notes/) · [News](https://openai.com/news/) | 产品分组 release notes + 新闻稿 | 高（ChatGPT / Codex / API 分轨） |
| **Anthropic** | [Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview) · [Claude Apps RN](https://support.claude.com/en/articles/12138966-release-notes) · [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) | API 文档 RN + Help Center + GitHub | 高 |
| **Google** | [AI Blog](https://blog.google/innovation-and-ai/) · [Gemini API Changelog](https://ai.google.dev/gemini-api/docs/changelog) | 月度汇总 + API changelog | 中–高 |
| **xAI / Grok** | [News](https://x.ai/news) · [API Release Notes](https://docs.x.ai/developers/release-notes) | 新闻列表 + 开发者 RN | 极高 |
| **DeepSeek** | [GitHub](https://github.com/deepseek-ai) · 官方公告（无统一 changelog 页） | 零散 | 中 |

### 2.2 编码 / Agent 开发工具

| 产品 | 官方 Changelog / News | 形态 | 更新频率 |
|------|----------------------|------|----------|
| **Cursor** | [Changelog](https://cursor.com/changelog) | 独立 changelog（含 Origin 等子页） | 高 |
| **GitHub Copilot** | [Changelog](https://github.blog/changelog/label/copilot/) | GitHub Blog 标签页 | 中 |
| **Claude Code** | [GitHub Releases](https://github.com/anthropics/claude-code/releases) | Semver releases | 高 |
| **Replit** | [Updates](https://docs.replit.com/updates) | 文档站按日 changelog | 中–高 |
| **Lovable** | [Changelog](https://docs.lovable.dev/changelog) | Mintlify 文档 changelog | 高 |
| **Bolt.new** | [Blog / Discord](https://bolt.new/) | 无独立 RN（需跟 blog / 社区） | 低–中 |
| **v0 (Vercel)** | [Changelog](https://v0.dev/changelog) | 产品内 changelog | 中 |

### 2.3 创意 / 多媒体

| 产品 | 官方 Changelog / News | 形态 | 更新频率 |
|------|----------------------|------|----------|
| **Runway** | [Changelog](https://runway.com/changelog) | 独立 changelog（日期 + 计划标签） | 高 |
| **Midjourney** | [Updates](https://updates.midjourney.com/) | Ghost 博客聚合 | 中 |
| **ElevenLabs** | [Changelog](https://elevenlabs.io/docs/changelog) | 文档 changelog | 中 |
| **Suno** | [Blog](https://suno.com/blog) | 博客 | 低–中 |

### 2.4 搜索 / 通用 Agent

| 产品 | 官方 Changelog / News | 形态 | 更新频率 |
|------|----------------------|------|----------|
| **Perplexity** | [Changelog](https://www.perplexity.ai/changelog) · [Hub Blog](https://www.perplexity.ai/hub/blog) | changelog 条目 + 新闻稿 | 高 |
| **OpenClaw** | [GitHub Releases](https://github.com/openclaw/openclaw/releases) | OSS releases | 高 |

### 2.5 第三方聚合（辅助，非 Tier 0）

| 来源 | URL | 用途 | **不能做什么** |
|------|-----|------|----------------|
| **Releasebot** | [releasebot.io](https://releasebot.io/) · [Browse feeds](https://releasebot.io/updates) | **订阅**各产品官方 RN/changelog；RSS / Email / CLI / **MCP** / API / Slack / n8n；用于发现遗漏，须回链官方验证 | ❌ **不能**作为 Vatt 等产品的 changelog **发布/hosting** 方案 |
| **Product Hunt Launch** | producthunt.com | 新产品上线信号，非迭代追踪 | — |

**Releasebot 能力摘要**（2026-08）：

- 监控数百产品的官方 release note 渠道，更新进个人 feed  
- 热门 feed：Anthropic（774）、OpenAI（945）、Google（1922）、Perplexity（29）、Cursor 等  
- 接入：RSS、Email、CLI、MCP、API、Slack、n8n  
- **定位**：发现层 / 监控竞品；写 timeline 或 blog 时仍须 Tier 0 官方页互证（见 §7.3）

---

## 3. 聚合页信息架构（落地页参考）

参考 [Runway Changelog](https://runway.com/changelog) 与 [Midjourney Updates](https://updates.midjourney.com/) 的常见模式：

```
/product-updates          ← Hub 页（本文件 §4 统一时间线）
├── ?product=cursor       ← 可选：按产品筛选
├── ?category=coding      ← 可选：按类别筛选
└── /updates/{slug}       ← 未来：高价值单篇（类似 floatboat Updates/）
```

**Hub 页每条记录建议字段**：

| 字段 | 说明 |
|------|------|
| `date` | 官方发布日期（ISO） |
| `product` | 产品名 |
| `category` | model / feature / integration / pricing / beta-ga |
| `title` | 一句话标题 |
| `summary` | 1–2 句摘要 |
| `tier` | announce / beta / ga |
| `source_url` | Tier 0 链接 |
| `blog_candidate` | ⭐ 是否值得拆单篇 |

**列表排序**：默认按日期降序；同日内按 product 字母序。

---

## 4. 统一时间线（2026-07-01 — 2026-08-24）

> 仅收录有 Tier 0 来源的条目。`⭐` = 建议后续拆 blog 的候选。

### 2026-08

| 日期 | 产品 | 类别 | 事件 | 来源 |
|------|------|------|------|------|
| 08-22 | Floatboat | feature | Flow Mode 上线：语音听写 + 边讲边改 + 会议实时 action items | 本地 Updates/56（非本次 web 检索） |
| 08-21 | xAI | pricing | Grok Bot 纳入 SuperGrok Plus、Cursor Pro+、Cursor Teams | [x.ai/news](https://x.ai/news) |
| 08-21 | Claude Code | feature | v2.1.239：data-residency 成本估算、Python SDK 1.x 迁移命令 | [GitHub Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) |
| 08-20 | Midjourney | ux | Alpha 站 changelog：Upscale/Zoom/Vary 回归、V8.2 HD 修复、sidebar 优化 | [Changelog 8/20/26](https://updates.midjourney.com/changelog-8-20-26/) |
| 08-20 | Anthropic | platform | Python SDK v1.0 GA（httpx2）；Computer use / Browser use / Files API / Agent Skills 出 beta | [Platform RN](https://platform.claude.com/docs/en/release-notes/overview) |
| 08-20 | OpenAI | product | Codex：Apple Messages 插件、Site URL 可编辑、共享 thread 快照、GitLab 云支持 | [Release Notes](https://openai.com/products/release-notes/) |
| 08-19 | Cursor | agent | ⭐ Subscriptions（PR/Slack/定时任务）、Custom Modes、Subagents 独立 VM、`/goal` | [Changelog](https://cursor.com/changelog) |
| 08-18 | Replit | enterprise | ⭐ Admin API beta、Audit Logs、Workspace Settings、Compliance API 预告 | [Blog](https://replit.com/blog/new-enterprise-governance-tools) |
| 08-18 | Perplexity | research | Brain 技术博客：自改进 memory，correctness +25% | [Hub Blog](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents) |
| 08-17 | Cursor | platform | ⭐ **Origin** 代码托管 early beta：repos、PR、GitHub 双向同步、Vercel/Depot/Buildkite | [Origin Changelog](https://cursor.com/changelog/origin-code-hosting) |
| 08-14 | Replit | integration | MCP 原生接入 ChatGPT/Claude/Slack；workspace region；Admin API beta | [Aug 14 RN](https://docs.replit.com/updates/2026/08/14/changelog) |
| 08-13 | OpenAI | model | ⭐ GPT-5.6 Sol **Ultrafast** preview（Cerebras，最高 14× 速度） | [Blog](https://openai.com/index/previewing-ultrafast/) |
| 08-13 | Cursor | infra | ⭐ Cloud Agents **Builds**：环境预热，启动 10× 更快 | [Changelog](https://cursor.com/changelog/08-13-26) |
| 08-13 | Perplexity | api | Agent API 统一端点：web search、MCP、finance/people search | [Hub Blog](https://www.perplexity.ai/hub/blog) |
| 08-12 | xAI | model | ⭐ **Grok 4.6** GA：500K context，Cursor / Grok Build / API | [News](https://x.ai/news/grok-4-6) |
| 08-11 | xAI | product | ⭐ **Grok Bot** GA：持久云电脑 Agent | [News](https://x.ai/news) · [API RN](https://docs.x.ai/developers/release-notes) |
| 08-10 | Anthropic | pricing | Claude Sonnet 5  introductory 价 $2/$10 定为标准价（取消 9/1 涨价） | [Platform RN](https://platform.claude.com/docs/en/release-notes/overview) |
| 08-07 | xAI | product | Imagine Image 2.0 | [News](https://x.ai/news) |
| 08-07 | Replit | security | Agent 构建时 security scan；项目跨 workspace 迁移 | [Aug 7 RN](https://docs.replit.com/updates/2026/08/07/changelog) |
| 08-06 | Perplexity | product | Computer for builders（solo founder 自动化） | [Hub Blog](https://www.perplexity.ai/hub/blog) |
| 08-05 | Anthropic | enterprise | Inference hooks beta；Claude Opus 4.1 退役 | [Platform RN](https://platform.claude.com/docs/en/release-notes/overview) |
| 08-03 | Cursor | integration | Google Workspace 插件（Gmail / Drive / Calendar） | [Changelog](https://cursor.com/changelog) |

### 2026-07

| 日期 | 产品 | 类别 | 事件 | 来源 |
|------|------|------|------|------|
| 07-31 | xAI | model | Imagine Video 1.5 + References（1080p） | [News](https://x.ai/news) |
| 07-29 | Cursor | mobile | iPad 版 GA；Inbox + 完整 PR review | [Changelog](https://cursor.com/changelog) |
| 07-29 | xAI | model | Grok Voice Think Fast 2.0 | [News](https://x.ai/news) |
| 07-28 | xAI | product | Build Mode early beta；Grok 4.5 in GitHub Copilot | [News](https://x.ai/news) |
| 07-28 | Perplexity | product | Personal Computer on Windows；Model Council in Computer | [Hub Blog](https://www.perplexity.ai/hub/blog) |
| 07-24 | Midjourney | model | ⭐ **V8.2** 图像模型：美学/个性化大幅提升 | [Version 8.2](https://updates.midjourney.com/version-8-2/) |
| 07-24 | xAI | integration | Grok in Google Workspace | [News](https://x.ai/news) |
| 07-24 | Anthropic | model | ⭐ **Claude Opus 5** GA：1M context，$5/$25 MTok | [Platform RN](https://platform.claude.com/docs/en/release-notes/overview) |
| 07-23 | xAI | product | Workflows in Grok Build（并行 agent 编排） | [News](https://x.ai/news) |
| 07-22 | xAI | model | Grok 4.5 全平台 rollout | [News](https://x.ai/news) |
| 07-16 | xAI | model | Grok 4.5 发布 | [News](https://x.ai/news/grok-4-5) |
| 07-13 | Perplexity | feature | Brain memory preview；Opus 4.8 fast mode；网站发布到 pplx.app | [Changelog](https://www.perplexity.ai/changelog/brain-faster-computer-models-website-publishing) |
| 07-02 | Runway | agent | Agent Skills：广告 campaign / 本地化等一键命令 | [Changelog](https://runway.com/changelog) |
| 07-01 | Runway | model | Nano Banana 2 Lite 图像生成 | [Changelog](https://runway.com/changelog) |
| 07-01 | Google | model | Gemini 3.6 Flash / 3.5 Flash-Lite / 3.5 Flash Cyber；Robotics ER 2 | [July AI Updates](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-july-2026/) |
| 06-30 | Runway | model | Gemini Omni Flash 视频生成/编辑 | [Changelog](https://runway.com/changelog) |
| 06-30 | Anthropic | model | ⭐ **Claude Sonnet 5** GA | [Platform RN](https://platform.claude.com/docs/en/release-notes/overview) |
| 06-29 | Runway | audio | Seed Audio 1.0：最长 120s 语音/音效/音乐 | [Changelog](https://runway.com/changelog) |
| 06-25 | Runway | agent | ⭐ Agent 2.0：全链路营销 campaign | [Changelog](https://runway.com/changelog) |
| 06-25 | xAI | integration | Interactive Brokers + Grok | [News](https://x.ai/news) |
| 06-18 | Runway | product | Studio：trim / stitch / export 一体化 | [Changelog](https://runway.com/changelog) |
| 06-18 | Perplexity | feature | Brain 自改进 memory 宣布 | [Hub Blog](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents) |
| 06-16 | Midjourney | feature | Draft mode for V8.1 | [Updates](https://updates.midjourney.com/) |
| 06-11 | Midjourney | model | V8.1 成为默认模型 | [Updates](https://updates.midjourney.com/) |

### Lovable 近期（文档 changelog 无逐条日期，按条目重要性摘录）

| 条目 | 类别 | 摘要 | 来源 |
|------|------|------|------|
| Gemini 3.7 Flash 默认 | model | App AI features 默认模型切换至 gemini-3.7-flash | [Changelog](https://docs.lovable.dev/changelog) |
| Gemini Embedding 2 默认 | model | 搜索/RAG 默认 embedding，支持 multimodal | 同上 |
| Design systems 全付费计划 | feature | 设计系统全 paid plans 可用 | 同上 |
| Credit check-ins beta | billing | 长跑消息成本中途确认 | 同上 |
| MCP → Strawberry Browser | integration | Lovable MCP 接入 Strawberry | 同上 |
| Figma .fig 附件 | integration | Chat 内拖入 Figma 文件 | 同上 |
| Data collection opt-out | policy | 2026-09-09 起 Free/Pro 训练数据政策 + 提前 opt-out | 同上 |

---

## 5. 按产品快速索引（2026-07 — 2026-08 要点）

### Cursor
- **Origin**（08-17）：AI-native git hosting + PR + GitHub sync + Vercel CI ⭐
- **Cloud Agents Builds**（08-13）：环境预热 ⭐
- **Subscriptions / `/goal` / Subagents VM**（08-19）：always-on agent 体系 ⭐
- **Google Workspace 插件**（08-03）

### OpenAI
- **GPT-5.6 Sol Ultrafast**（08-13）：Cerebras 14× 推理 ⭐
- **Codex**：Apple Messages、Site URL 编辑、GitLab、thread 共享（08-20）

### Anthropic
- **Claude Opus 5**（07-24）、**Sonnet 5**（06-30）⭐
- **Platform GA**：Computer/Browser use、Files API、Agent Skills、Python SDK v1.0（08-19–20）
- **Claude Code** v2.1.239（08-21）

### xAI / Grok
- **Grok 4.6**（08-12）、**Grok Bot**（08-11）⭐
- **Build Mode / Workflows / Microsoft & Google 插件**（07 月密集）
- Grok Bot 扩计划（08-21）

### Runway
- **Agent 2.0 + Agent Skills**（06-25 — 07-02）⭐
- 第三方模型聚合（Kling、Sora 2 Pro 等）、Seed Audio、Gemini Omni Flash

### Midjourney
- **V8.2**（07-24）⭐
- Alpha 站 UX 大改 + 8/20 changelog 修复潮

### Perplexity
- **Brain** memory（07-13 preview）⭐
- **Agent API**（08-13）、Computer → M365 / email（07-08）
- 网站发布 pplx.app / custom domain

### Replit
- **MCP 全平台**（08-14）⭐
- **Enterprise governance**：Admin API、Audit Logs（08-14–18）
- Security scan while building（08-07）

### Lovable
- Gemini 3.7 Flash / Embedding 2 默认
- Design systems、MCP 生态扩展、训练数据 opt-out 政策

### Google
- Gemini 3.6 Flash / 3.5 Flash-Lite / Flash Cyber（07）
- Gemini Robotics ER 2

---

## 6. Blog 候选清单（⭐ 标记项）

| 优先级 | 主题 | 理由 | 已有本地稿 |
|--------|------|------|------------|
| P0 | Cursor Origin | 行业级事件：代码托管 + GitHub outage 背景 | temp/cursor-origin-web-search |
| P0 | Grok 4.6 + Grok Bot | 模型 + Agent 产品双发 | floatboat 51, 53 |
| P0 | Claude Opus 5 / Sonnet 5 | 旗舰模型换代 | floatboat claude 簇可延伸 |
| P1 | Runway Agent 2.0 生态 | 创意工具 Agent 化范式 | 无 |
| P1 | Perplexity Brain + Agent API | 搜索 Agent 记忆与 API 统一 | 无 |
| P1 | OpenAI GPT-5.6 Ultrafast | 推理基础设施叙事 | floatboat openai 30 |
| P2 | Replit MCP + Enterprise | Vibe coding 平台治理 | 无 |
| P2 | Midjourney V8.2 | 创意模型迭代 | 无 |
| P2 | Lovable 模型默认切换 | 与 Gemini 3.7 Flash 文联动 | floatboat 55 |

---

## 7. 维护 SOP

### 7.1 每周扫描（约 30 min）

1. 按 §2 表逐个打开官方 changelog 首页  
2. 对比 §4 最新日期，追加新行  
3. 新 ⭐ 候选写入 §6  
4. 重大发布（新模型 / 新产品 / beta→GA）考虑触发 web-deep-search 深搜

### 7.2 深搜触发条件

- 新模型 announce（如 Grok 5、GPT-6）  
- 收购 / 合并（如 Midjourney 首笔收购 2026-07-23）  
- 政策变更（Lovable 训练数据、定价结构调整）  
- 社区争议需验证（Origin 企业 opt-out 等）

### 7.3 格式约定

- 日期：ISO `YYYY-MM-DD`  
- 阶段：`announce` / `beta` / `ga` / `deprecation`  
- 每条必须有 Tier 0 URL；Releasebot 仅作发现线索

---

## 8. 参考链接（Tier 0 精选）

### Changelog 页（聚合范式参考）
- [Runway Changelog](https://runway.com/changelog)
- [Midjourney Updates](https://updates.midjourney.com/)
- [Cursor Changelog](https://cursor.com/changelog)
- [Lovable Changelog](https://docs.lovable.dev/changelog)
- [Replit Updates](https://docs.replit.com/updates)
- [OpenAI Release Notes](https://openai.com/products/release-notes/)
- [Anthropic Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)
- [Perplexity Changelog](https://www.perplexity.ai/changelog)
- [xAI News](https://x.ai/news)

### 竞品聚合页参考（非 AI，结构可借鉴）
- [Quizlet News](https://quizlet.com/blog/news)
- [Wayground Product Updates](https://wayground.com/home/product-updates?lng=en)

### Changelog SaaS（发布层，Vatt 可选）
- [Headway](https://headwayapp.co) — 轻量 public page + widget  
- [AnnounceKit](https://announcekit.app) — 美观 embed + 通知  
- [Beamer](https://www.getbeamer.com) — in-app update feed 强  
- [LaunchNotes](https://www.launchnotes.com) — 企业级 roadmap + subscriber  
- [Changelog SaaS 对比参考](https://userorbit.com/blog/best-product-changelog-and-release-notes-software)

---

## 9. Vatt 现状与 Changelog 需求

> 来源：`clients/vatt/` 站点与客户文档（2026-08-24 整理，非 web-deep-search 隔离范围）

### 9.1 产品 / 站点现状

| 维度 | 状态 |
|------|------|
| 产品 | [vatt.ai](https://vatt.ai/) — AI reaction video editor，邀请制早期 |
| 公司 | Vattention（杭州时空注力） |
| 现网页面 | `/`、`/pricing`、`/login`；**无** `/blog`、`/changelog`（均 404） |
| 技术栈 | 推测 Next.js / React SPA；SEO 基建弱（无 robots/sitemap） |
| 本地内容 | `vatt/blog/` Markdown + `vatt-blog-article` skill；blog 仅 1 篇已交付 |
| 功能真源 | [vatt-features.md](../vatt/vatt-features.md) Status 字段 |

### 9.2 目标

- 公开 **产品更新时间线**，参考 [Runway Changelog](https://runway.com/changelog) / [Midjourney Updates](https://updates.midjourney.com/)  
- URL 建议：**`vatt.ai/changelog`**（同域 SEO + 品牌统一）  
- 小迭代走 changelog feed；大功能可链到 `/blog/{slug}`（单篇是否写另议）  
- 后期（有登录用户）：产品内 What's New badge / widget

---

## 10. 方案选型：SaaS vs Docs vs 自建

### 10.1 三类路线总览

| 路线 | 代表 | 适合 Vatt 阶段 | 优点 | 缺点 |
|------|------|----------------|------|------|
| **A. Changelog 专用 SaaS** | Headway、AnnounceKit、Beamer、LaunchNotes | 零前端人力、先要 What's New | 上线快；widget + 邮件通知；hosted 页 | 多在子域/embed；SEO/品牌弱；月费 |
| **B. Docs 平台** | GitBook、Mintlify、ReadMe | 同时要 API 文档 + changelog | 一套系统；[Lovable 即 Mintlify changelog](https://docs.lovable.dev/changelog) | Vatt 暂无 docs 需求 → **过重** |
| **C. 自建同站页面** | Next.js MDX、Ghost 子域 | 有 dev、要 SEO + 品牌 | 控 URL/样式；与 blog 共用 Markdown 流程 | 需一次开发 + 发布 SOP |

### 10.2 Changelog 专用 SaaS 对比

| 产品 | 公开 changelog 页 | 产品内 widget | 定价量级 | Vatt 适用场景 |
|------|------------------|---------------|----------|---------------|
| **Headway** | ✅ 简洁 | ✅ | 免费 ~ $29/月 | 小团队、只要更新页 + 轻 widget |
| **AnnounceKit** | ✅ 美观 | ✅ | 中档 | 要好看 public page + embed |
| **Beamer** | ✅ | ✅ 强（popup/NPS） | 中档 | 邀请用户多、要强 in-app 触达 |
| **LaunchNotes** | ✅ 企业级 | ✅ roadmap/feedback | ~$299+/月 | 现阶段偏重 |
| **Canny** | changelog 附带 | feedback/roadmap 为主 | 中高档 | 除非同时要 roadmap 系统 |

参考：[Userorbit changelog 软件对比](https://userorbit.com/blog/best-product-changelog-and-release-notes-software) · [ProductBridge SaaS changelog 清单](https://productbridge.io/blog/best-changelog-software-for-saas)

### 10.3 GitBook / Mintlify 要不要上？

| 问题 | 结论 |
|------|------|
| 仅做 changelog？ | **不需要** GitBook/Mintlify；URL 会变成 `docs.vatt.ai`，与营销站分离 |
| 何时考虑 Docs 平台？ | 3–6 个月内要上线 **API 文档、集成指南、Webhook 参考** 时再评估 Mintlify（与 Lovable 同范式）或 GitBook |
|  interim 方案 | `vatt.ai/changelog` 自建 + 未来 docs 站 footer 互链 |

### 10.4 Vatt 推荐决策（2026-08-24）

| 阶段 | 推荐 | 理由 |
|------|------|------|
| **Phase 1（现在）** | **C — 自建 `vatt.ai/changelog`（Markdown/MDX）** | 已有 `vatt/blog/` 工作流；同域 SEO；与 Runway 范式一致 |
| **Phase 1 备选**（dev 极度紧张） | **A — Headway / AnnounceKit** | 先 embed + hosted 子页，后期迁移同域 |
| **Phase 2**（有登录用户） | A 的 widget **或** 自建 badge，读同一 JSON feed | 避免 SaaS + 自建双写 |
| **Releasebot** | 仅 **监控竞品** changelog（§2.5），不用于发 Vatt 更新 | — |

---

## 11. Vatt 接入架构（分阶段）

```
Phase 1 — 公开页（优先）
├── 路由：vatt.ai/changelog
├── 内容源：clients/vatt/changelog/*.md（或 vatt/blog/ 内 category: Changelog）
├── 构建：Next.js 读 frontmatter → 时间线列表 + 详情页 /changelog/{slug}（可选）
├── 发布：PR 合并 → 与主站同 deploy pipeline
├── SEO：加入 sitemap；页 title「Product Updates & Changelog | Vatt」
└── 可选：/changelog/rss.xml

Phase 2 — 产品内触达
├── 产品内 header/footer「What's New」badge（未读计数）
├── 数据源：与 Phase 1 同一 JSON（build 时 generate changelog.json）
└── 或：Headway/Beamer embed（若 Phase 1 用了 SaaS 备选）

Phase 3 — 自动化（发版频繁后）
├── 触发：GitHub Release / Linear done → webhook
├── 动作：生成 changelog 草稿 PR（不自动上生产）
└── 人工：润色 + 核对 vatt-features.md Status → merge
```

### 11.1 内容 Frontmatter 规范

```yaml
---
title: "Auto-sync facecam with source video"
description: "One-line summary for SERP and RSS."
slug: "auto-sync-facecam-source"
date: 2026-08-24
type: feature          # feature | improvement | fix | model | policy
tier: ga               # announce | beta | ga | deprecation
plans: all             # free | pro | all | invite-only
related_blog: ""       # 可选：/blog/how-to-edit-reaction-videos-faster
---
```

### 11.2 页面 UI 参考（Runway 模式）

| 元素 | 说明 |
|------|------|
| 列表项 | 日期 · 计划标签（All / Pro / Beta）· 标题 · 1 句摘要 |
| 详情 | 点击展开或进 `/changelog/{slug}` |
| 筛选 | `type` / `tier`（二期） |
| 页脚 | 链到 `/blog`、`/features`（上线后） |

### 11.3 建议目录结构（clients 仓库）

```
vatt/
├── changelog/                    ← 新建
│   ├── README.md                 ← 发布登记表
│   ├── 01-emotion-detection-beta.md
│   └── ...
├── blog/                         ← 已有；深度文 / 教程
└── vatt-site-structure.md        ← 后续补 /changelog 路由
```

---

## 12. Changelog vs Blog 分工（Vatt）

| 内容类型 | 放哪里 | 例子 |
|----------|--------|------|
| 小迭代、bugfix、UI 调整 | `/changelog` 一条 | 「修复 timeline  scrub 卡顿」 |
| 大功能、品类叙事、SEO 长尾 | `/blog/{slug}` + changelog 摘要链过去 | 「Emotion detection 2.0 怎么用」 |
| 仅内测 / 邀请制 | changelog 标 `tier: beta` + `plans: invite-only`，或暂不公开 | 新模型 A/B |
| 行业竞品动态 | **不写进 Vatt changelog**；维护本文件 §4 行业时间线 | Cursor Origin |

**原则**：changelog = **产品事实 feed**；blog = **解释与获客**；行业聚合 = **本 temp 文档**。

---

## 13. Releasebot 在 Vatt 工作流中的位置

```
┌─────────────────────────────────────────────────────────┐
│  监控层：Releasebot RSS/MCP → 发现 Cursor/Runway 等更新   │
│           ↓ 人工筛选                                       │
│  行业聚合：本文件 §4 时间线（不写进 vatt.ai）               │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  发布层：vatt/changelog/*.md → vatt.ai/changelog          │
│           （或 Headway 备选）                              │
│           ↓ 可选 deep link                                │
│  深度层：vatt/blog/{slug}                                │
└─────────────────────────────────────────────────────────┘
```

**Releasebot 接入建议**（监控竞品，非发 Vatt）：

1. Follow：Runway、Descript、Rev.id 等 reaction/视频编辑竞品（按 [vatt-competitors.md](../vatt/vatt-competitors.md) 扩展）  
2. MCP/API 接入 Cursor 工作流：每周 digest → 更新 §4  
3. 发现重大竞品功能 → 评估是否写 Vatt blog 对比文，**不**冒充 Vatt 自身 changelog

---

## 14. Vatt 实施清单 & 待决项

### 14.1 实施 checklist

| # | 任务 | 负责 | 状态 |
|---|------|------|------|
| 1 | 在 Vatt 代码仓加 `/changelog` 路由（MDX/Markdown） | Eng | 待做 |
| 2 | 新建 `clients/vatt/changelog/` + README 登记表 | Content | 待做 |
| 3 | 写首条 changelog（如 invite 扩量 / 某功能 beta） | Product + Content | 待做 |
| 4 | `vatt-site-structure.md` 增加 `/changelog` + sitemap | SEO | 待做 |
| 5 | 首页/页脚加「Updates」链到 `/changelog` | Eng | 待做 |
| 6 | （可选）RSS `/changelog/rss.xml` | Eng | 待定 |
| 7 | Phase 2：产品内 What's New badge | Eng | 待定 |
| 8 | （备选）Headway trial + embed 评估 | PM | 仅 dev 紧张时 |

### 14.2 待用户确认

| 项 | 选项 |
|----|------|
| 主方案 | A) 自建同站 **（推荐）** B) Headway 先顶 C) LaunchNotes 企业档 |
| 是否需要 in-app widget（Phase 2 优先级） | 是 / 否 |
| changelog 是否要多语言（`?lang=` 8 语种） | 先 en only / 同步 i18n 路径方案 |
| 首条 changelog 主题 | 待定（对齐 vatt-features 最近 GA 功能） |

### 14.3 首条 changelog 模板

```markdown
---
title: "Emotion highlight detection now in beta"
description: "Vatt automatically finds laugh, surprise, and shock moments in long reaction footage."
slug: "emotion-highlight-detection-beta"
date: 2026-08-24
type: feature
tier: beta
plans: invite-only
---

## TL;DR

- **Emotion highlight detection** finds reaction peaks in your source and facecam tracks.
- Available to **invite-only** users on the web editor.
- Results land on a **fully editable timeline** — accept, trim, or reject any suggestion.

## What's included

- Automatic peak detection for common reaction emotions
- Side-by-side source + facecam alignment before you cut
- Manual override on every suggested clip

## Known limitations

- English UI only in this beta
- Best results on videos ≥ 10 minutes with clear facecam

*Questions? Reply in Discord / support channel.*
```

---

*本文件：行业聚合（web-deep-search-spec v1.3 · 2026-08-24）+ Vatt changelog 接入方案（2026-08-24 增补）· 存放于 `clients/temp/` · 长期保留时可拆为 `vatt/vatt-changelog-spec.md` + 行业线独立文档*
