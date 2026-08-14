# Hellyeah AI — 导航站提交方案

> **用途**：Agent 可读的主文档。同事说「基于本文档生成提交到 XXX 的内容」时，Agent 读 §0（事实锚）→ §3（站点画像）→ §8（文案池）→ §9（生成规则）→ 按需输出。  
> **原则**：核心数据只存一份；不预分配文案到具体站；每个站的提交内容在生成时决定。

**Last updated**: 2026-06-02

---

## 0. Hellyeah 官网事实锚（提交前必读）

> 所有提交内容必须以本节为准。本节与 [hellyeah-others.md](./hellyeah-others.md) §1（路由）同步。

| 维度 | 事实（2026-06-02 全站复核） |
|------|---------------------------|
| **主叙事** | **CLI**：「npm install your growth engine」；**RCLL** 循环 = Research → Create → Launch → Learn |
| **产品形态** | CLI Beta（`/#cli`）；4 分钟上手、无信用卡、BYO LLM |
| **定价** | CLI Beta **$0**；企业 Forward-Deployed Pod（% managed spend，Demo 申请）；~~勿写 $1,500/月~~ |
| **AIMA** | [/aima](https://www.hellyeahai.com/aima) — WhatsApp Live；与 CLI 叙事并存 |
| **四平台 URL** | `/aima` `/forge` `/mutation` `/deja-vu`（非 `/platforms/*`） |
| **能力页（6）** | `/capabilities/agentic-marketing` … `influencer-marketing`；GEO → `/capabilities/seo-geo` |
| **Solutions（5）** | `/solutions/automate-marketing` 等 |
| **Arena（7）** | `/for/mobile-apps` … `/for/edutech`（非 `/arenas/*`） |
| **合规** | ISO 27001、GDPR、CCPA、DPF、HIPAA-ready；~~SOC 2~~ 为 in flight，勿写 |
| **案例（9）** | [/customers](https://www.hellyeahai.com/customers) + `/customers/{slug}` — 指标见 [hellyeah-others.md](./hellyeah-others.md) §3 |
| **Déjà Vu** | Private alpha — 不夸大已 GA |
| **社媒** | [X](https://x.com/hellyeah_ai) · [LinkedIn](https://www.linkedin.com/company/hellyeahai) · [Discord](https://discord.com/invite/DG9QE7paSB) |
| **转化入口** | [/demo](https://www.hellyeahai.com/demo)（15 min） |
| **404 路径** | `/platforms/*` `/trust-center` `/about-us` `/integrations` — 勿链 |
| **提交 URL** | https://www.hellyeahai.com/ |

---

## 1. 站点筛选原则

1. 收录 B2B / 企业级 AI 产品
2. 有 Marketing / Growth / Sales 分类页
3. 有实际搜索流量（品牌词或品类词 SERP 排名）
4. 审核周期可接受（非仅限邀请制）

---

## 2. 目标导航站 — 唯一事实表

> 本节是各站提交信息（URL、费用、审核周期、外链类型）的**唯一存放处**。其他章节只引用不复制。

| # | 站点 | 月流量 (Similarweb) | 提交入口 | 费用 | 审核 | 外链 | 备注 |
|---|------|--------------------|----------|------|------|------|------|
| 1 | **There's An AI For That** | 6,100K | [get-featured](https://theresanaiforthat.com/get-featured/) | $49 基础 / **$347** 推荐（Listing + Newsletter） | 1–2d | 待确认 | 90M+ 用户；47K+ 工具；Newsletter 2.5M+；有 Task 关联字段 |
| 2 | **Toolify.ai** | 1,400K | [submit](https://www.toolify.ai/submit) | **$99** 一次性 | ~2d | dofollow ≥6 | 28K+ 工具；含 Toolify AI Certification；自报 5.1M+ 月访 |
| 3 | **Aixploria** | 954K | [submit](https://www.aixploria.com/en/submit-ai-tool-or-feature-company/) | $79 Fast / **$279** Verified（蓝标 + 1000 字 + 60d 首页） | 2–5d | nofollow | 法文起源 / 英文覆盖广；3 条额外链接；已停止免费 |
| 4 | **Futurepedia** | 678K | ⚠️ submit 404（2026-06-02）→ [Contact](https://www.futurepedia.io/contact-us) | 待确认 | 待确认 | 待确认 | 4K+ tools；Newsletter 300K+；YouTube 2M+；**暂缓提交** |
| 5 | **TopAI.tools** | 611K | [submit](https://topai.tools/submit) | $47 Fast / $229 Premium（7d 置顶） | 1–2d | 待确认 | 10K+ tools；自报 2M+ 月访；需上传截图 |
| 6 | **FutureTools** | 437K | [submit-a-tool](https://www.futuretools.io/submit-a-tool) | **$0** 免费（Featured 另购，需先过审） | ~7d | 待确认 | Matt Wolfe 运营；**>75% 被拒**；禁 waitlist/GPT wrapper |
| 7 | **Creati.ai** | 415K | [submit](https://creati.ai/submit-ai/submit-your-ai/) | $69 VIP / $99 SVIP（200 clicks 保证） | ~2d | dofollow ≥6 | 自报 2.1M+ 月用户 |

> 流量来源：Similarweb 2026-06。与各站自报数据有差异（见备注列）。

---

## 3. 各站画像 —— Agent 生成时的决策依据

> **Agent 注意**：本节描述每个站的受众、调性、什么奏效、什么该避免。生成时组合 §8 文案池，不预分配。

### 3.1 There's An AI For That (TAAFT)

| 维度 | 描述 |
|------|------|
| **受众** | 有具体任务需求的用户（"帮我写邮件""优化广告"）；偏实操者（Growth Lead / Performance Lead） |
| **调性** | 功能完整、场景明确。用户搜的是"能干什么"，不是"这公司多牛" |
| **什么奏效** | 多个 Task 关联（GEO、Ad campaign、Influencer、Lifecycle）；一句话说清覆盖哪些场景 |
| **什么该避免** | 过于抽象的平台叙事；纯品牌腔 |
| **独有字段** | **Task 关联** — 注册时勾选具体 Task（如 "Ad campaign management""SEO & GEO"），决定搜索匹配率 |
| **推荐费用档** | **$347**（Listing + Newsletter，效果最好） |

### 3.2 Toolify.ai

| 维度 | 描述 |
|------|------|
| **受众** | AI 创业者、竞品调研者；关注流量/营收数据、市场表现 |
| **调性** | 数据感、可量化。标题和描述让人一眼看出"这个工具在增长赛道有位置" |
| **什么奏效** | 对比型叙事（80h manual → 1 prompt）；具体渠道名（Meta/Google/TikTok）；价格分档 |
| **什么该避免** | 太软的品牌故事；无数据支撑的 superlative |
| **特殊要求** | 需填价格档位（选 Demo / Paid）；平台会自行估算流量 |

### 3.3 Aixploria

| 维度 | 描述 |
|------|------|
| **受众** | 设计/品牌敏感；决策层（CMO/VP）偏多 |
| **调性** | 品牌感、转型叙事。强调"取代碎片化工具"的愿景比罗列功能更有效 |
| **什么奏效** | 转型故事（from X to Y）；长文发挥空间大（Verified 1000 字）；3 条额外链接链不同页面 |
| **什么该避免** | 纯功能列表；过于技术化的 CLI 描述（除非读者画像匹配） |
| **特殊要求** | Description ≤165 chars + Long Text ≤1000 words + **3 Extra Links**；nofollow |

### 3.4 Futurepedia

| 维度 | 描述 |
|------|------|
| **受众** | AI 学习者/教育型用户；社区活跃；Newsletter 读者覆盖广（300K+） |
| **调性** | 教育 + 社区友好。强调"这工具解决什么问题"比"这工具有多强"更重要 |
| **什么奏效** | 能力线汇总（Paid + GEO + Lifecycle + Influencer）；提 Newsletter 读者可能感兴趣的角度 |
| **什么该避免** | 过度销售腔 |
| **⚠️ 状态** | 提交入口 404，暂缓。文案可先准备，提交前确认现行流程 |

### 3.5 TopAI.tools

| 维度 | 描述 |
|------|------|
| **受众** | 工具发现者；偏实用主义 |
| **调性** | 直接、功能导向。快速说清"这是什么，能干什么" |
| **什么奏效** | 功能点清晰；企业级/基础设施定位可区分于海量 C 端小工具 |
| **特殊要求** | **需上传产品截图**；48h 上线 |

### 3.6 FutureTools (Matt Wolfe)

| 维度 | 描述 |
|------|------|
| **受众** | AI 创业者、开发者、Indie maker；对 "Agent""CLI""工作流" 有天然好感 |
| **调性** | 技术向、Agentic。Matt Wolfe 审稿，不要营销腔。真诚描述你的工具如何帮助增长团队 |
| **什么奏效** | Agent/CLI 叙事；强调可定制、开发者友好；免费 + 可自托管感 |
| **什么该避免** | 营销腔、agency 替代话术、waitlist-only 产品 |
| **⚠️ 警告** | **>75% 被拒**。确保：非 GPT wrapper、非 waitlist-only、网站无需登录即可理解产品 |

### 3.7 Creati.ai

| 维度 | 描述 |
|------|------|
| **受众** | 通用 AI 工具发现者 |
| **调性** | 全面、可信。dofollow 值回票价，内容上可略详细 |
| **什么奏效** | 能力线全覆盖；信任标记（ISO/GDPR + 审计日志）增强可信度 |

---

## 4. 提交优先级与节奏

| 优先级 | 站点 | 月流量 | 理由 |
|--------|------|--------|------|
| P0 | TAAFT | 6,100K | 流量断层第一，Task 搜索匹配 |
| P0 | Toolify.ai | 1,400K | 大目录 + dofollow ≥6 |
| P1 | Aixploria | 954K | 高流量 + 品牌曝光 |
| P1 | TopAI.tools | 611K | 入口稳定，审核快 |
| P2 | FutureTools | 437K | 免费但拒稿率高；适合 Agent/CLI 叙事 |
| P2 | Creati.ai | 415K | dofollow 补充 |
| — | Futurepedia | 678K | ⚠️ 提交入口 404，恢复后插入 |

**节奏**：
- **Week 1**：TAAFT + Toolify + Aixploria + TopAI.tools
- **Week 2**：Creati.ai + FutureTools；Futurepedia 待恢复后插入

---

## 5. 通用提交字段

> 各站表单字段以此为基准；独有字段见 §3 各站画像。

| 字段 | 来源 |
|------|------|
| Name | §8.1 选 |
| Tagline | §8.2 选（≤15 words） |
| One-Liner / Short Description | §8.3 + §8.4 选 |
| Long Description | §8.4 选一篇，按站定制 |
| Category | Marketing / Growth / AI for Business（以各站表单为准） |
| Pricing | **CLI Beta · Demo**（§8.7 P0 + P3）；勿写 $1,500 |
| Logo | 512×512 PNG |
| URL | https://www.hellyeahai.com/ |
| Social | §8.9 取用 |
| Screenshots | TopAI.tools 需要（§3.5） |

---

## 6. 待办

- [x] 各站提交入口与费用核实（§2）
- [x] Hellyeah 官网事实锚定（§0）
- [ ] 确认 Futurepedia 现行提交 URL
- [ ] TopAI.tools 准备产品截图
- [ ] 首次提交后记录审核周期 → [hellyeah-project-tasks.md](./hellyeah-project-tasks.md)

---

*关联任务：[hellyeah-project-tasks.md](./hellyeah-project-tasks.md)*

---

# Part B —— Agent 生成区

> 以下章节是 Agent 生成各站提交内容时的素材池和规则。同事说「基于本文档生成提交到 **XXX** 的内容」后，Agent 按 §9 规则从 §8 取料生成。

---

## 8. Master Copy Bank（文案池）

> **Agent 注意**：这是**可选池**，不是分配表。每站生成时按 §3 画像 + §9 规则从池中组合。同一条 tagline 至多用于 2 个站。

### 8.1 Name

| ID | 文案 | 适用倾向 |
|----|------|----------|
| N1 | **Hellyeah** | 品牌最简 |
| N2 | **Hellyeah AI** | 标准 |
| N3 | **Hellyeah — npm install your growth engine** | 与官网 `<title>` 一致 |
| N4 | **Hellyeah — AI Growth CLI** | 开发者/Agent 向 |

### 8.2 Tagline（≤15 words）

| ID | 文案 | 叙事角度 |
|----|------|----------|
| T0 | *npm install your growth engine* | 官网主标语（CLI） |
| T1 | *The AI-native CLI for growth campaigns* | CLI / 产品形态 |
| T2 | *Autonomous AI Growth Infrastructure for Enterprise* | 企业级 |
| T3 | *Research, Create, Launch, Learn — One Growth Loop* | RCLL 四步循环 |
| T4 | *The Operating System for AI-Native Revenue Teams* | 愿景型 |
| T5 | *From Siloed Tools to an Autonomous Growth Machine* | 转型叙事 |
| T6 | *Custom AI Agents That Run Your Growth — 24/7* | Agentic |
| T7 | *80 Hours of Manual Work, or One Prompt* | 对比叙事 |
| T8 | *Unify Paid Ads, GEO, Lifecycle, and Influencer — One Stack* | 能力线汇总 |

### 8.3 One-Liner（~25-35 words）

**CLI 叙事（默认，与官网一致）**

| ID | 文案 |
|----|------|
| OL5 | Hellyeah is the AI-native CLI for building, testing, and scaling growth campaigns — one command layer where agents research, create, launch, and learn across Meta, Google, TikTok, Klaviyo, and your stack. |
| OL6 | Replace 80-hour weekly growth sprints with an 8-second agent loop: Hellyeah runs research, creative, launches, and learning 24/7 with spend caps, approvals, and an immutable audit log. |
| OL7 | Hellyeah compounds growth memory — every campaign inherits past wins, ranks hypotheses daily, and ships the next move with brand-policy guardrails built in. |

**平台叙事（补充；子页多 404，勿作唯一描述）**

| ID | 文案 |
|----|------|
| OL1 | Hellyeah is AI growth infrastructure for performance marketing, programmatic GEO, lifecycle automation, and agentic influencer workflows — built for teams outgrowing agencies and point tools. |
| OL2 | Hellyeah's AIMA, Forge, Mutation, and Déjà Vu modules orchestrate paid media, real-time triggers, custom agentic workflows, and always-on experiments from one system. |
| OL3 | Hellyeah replaces fragmented agencies and point tools with a unified stack for paid media, search visibility, customer journeys, and creator campaigns. |
| OL4 | Hellyeah gives growth teams autonomous agents for paid ads, GEO, lifecycle, and influencer — experiment faster and scale without adding headcount. |

### 8.4 Short Description（100-150 words）

| ID | 适用场景 | 文案 |
|----|----------|------|
| **SD4** (CLI) | **默认** | Hellyeah is the AI-native CLI for growth teams who have outgrown spreadsheets and Sunday-night campaign sprints. Install once, then run a continuous **Research → Create → Launch → Learn** loop: agents scrape competitive and audience signals, generate on-brand copy and creatives, push to Meta, Google, TikTok, Klaviyo, and your CMS with spend caps and rollbacks, then promote winners into shared growth memory. Capabilities span performance marketing, SEO/GEO, lifecycle automation, creative testing, and agentic influencer campaigns. ISO 27001-aligned controls, GDPR/CCPA-ready. Start in minutes — no credit card; book a demo for enterprise deployment. |
| **SD1** (Platform) | 通用目录 | Hellyeah is AI-native growth infrastructure for teams that have outgrown agencies and siloed point tools. Modules **AIMA, Forge, Mutation, and Déjà Vu** cover performance marketing, agentic workflows, real-time intelligence, and continuous experiments — plus SEO/GEO, lifecycle, and influencer capabilities. Trusted by brands from consumer apps to global logistics (see Customers). Enterprise controls: ISO 27001-aligned, GDPR/CCPA-ready. |
| **SD2** (AIMA-heavy) | 效果广告向 | **AIMA** drives autonomous performance across major ad networks — budget allocation, creative iteration, and ROI learning. **Forge** builds agentic workflows; **Mutation** triggers journeys from live signals; **Déjà Vu** runs always-on experiments. Deployed via CLI or managed pods for teams scaling across multiple markets — with spend caps, approvals, and audit trails. |
| **SD3** (Agentic) | 开发者/Agent 向 | Hellyeah is growth infrastructure you can shape. Its Forge platform lets teams build custom AI agents and agentic workflows for systematic growth — whether automating influencer outreach at scale, orchestrating multi-market GEO campaigns, or wiring customer event data into real-time marketing triggers via Mutation. AIMA handles autonomous performance optimization across channels, while Déjà Vu runs continuous experiments that compound into a proprietary learning system. |

### 8.5 Feature Bullets

**RCLL 循环（与官网 CLI 一致，优先使用）**

| ID | 步骤 | 文案 |
|----|------|------|
| FR1 | Research | Competitive scrape, audience clustering, channel-fit scoring, hypothesis generation |
| FC1 | Create | Copy, image, video, and landing pages under brand-policy guardrails |
| FL0 | Launch | Meta, Google, TikTok, Klaviyo, CMS with spend caps, approvals, atomic rollback |
| FN1 | Learn | Bayesian winner promotion, loser auto-prune, growth memory write-back |
| FG0 | — | Growth inbox — rank daily opportunities from 1,000+ signals with scaffolded runs |
| FT0 | — | Immutable audit log, 7y retention, open SDK for any HTTP API |

**平台 / 能力线（补充用）**

| ID | 所属 | 文案 |
|----|------|------|
| FA1 | AIMA | AI-powered cross-channel optimization across Meta, Google, TikTok, and every major ad network |
| FA2 | AIMA | Predictive budgeting — forecasts ROI and adjusts spend instantly based on live data |
| FF1 | Forge | Build custom AI growth agents and agentic workflows — no code, just configuration |
| FF2 | Forge | Orchestrate multi-step playbooks: outreach → content → testing → analysis, automated |
| FM1 | Mutation | Real-time marketing triggers based on live customer signals — not static calendars |
| FD1 | Déjà Vu | Always-on experimentation — AI runs A/B tests 24/7 and surfaces winning patterns |
| FD2 | Déjà Vu | Compound learning: every experiment feeds into a shared intelligence layer |
| FG1 | GEO | AI-powered search visibility at scale — programmatic content for LLM search |
| FG2 | GEO | Multi-language GEO: English, Chinese, Japanese, Korean, and more |
| FL1 | Lifecycle | AI-native lifecycle automation — personalized journeys triggered by real-time behavior |
| FL2 | Influencer | Agentic influencer campaigns — AI orchestrates discovery, outreach, and attribution |

### 8.6 Use Case Snippets

| ID | Persona | 文案 |
|----|---------|------|
| UC1 | CMO / VP | Replace your growth agency stack with autonomous AI that delivers predictable, auditable results |
| UC2 | Head of Growth | Run 10x more experiments without hiring — AI designs, launches, and learns autonomously |
| UC3 | Performance Lead | Manage every ad network from one AI dashboard with sub-second budget reallocation |
| UC4 | Lifecycle Lead | From static drip sequences to AI that adapts journeys based on real-time signals |
| UC5 | Influencer Lead | Scale creator campaigns from 10 to 1,000 — AI handles discovery, briefs, and attribution |
| UC6 | RevOps | Unify data across paid, organic, lifecycle, and influencer — one source of truth |
| UC7 | AI-Native Startup | When anyone can prompt software into existence, Hellyeah is the distribution layer |

### 8.7 Pricing

| ID | 文案 | 使用条件 |
|----|------|----------|
| P0 | CLI Beta — start in minutes, no credit card; bring your own LLM | **默认** |
| P3 | Demo / Paid — book a demo for enterprise deployment | 站内有价格筛选时用 |
| P4 | Outcome-linked engagements available for qualified teams | Agentic/企业向 |
| ~~P1~~ | ~~Starts at $1,500/month~~ | **禁止使用**（官网未公开） |

### 8.8 Trust / Proof

- 官网展示：ISO 27001, GDPR, CCPA, DPF, HIPAA-ready；spend caps、approval gates、immutable audit log
- 案例（可摘 1–2 条，源自 [/customers](https://www.hellyeahai.com/customers)）：Final Round AI $12M ARR in 14mo；J&T 1.4B impressions；Fish Audio +340% signup
- ~~SOC 2 Type II~~ — 勿写（in flight）

### 8.9 Links

| 类型 | URL |
|------|-----|
| Website | https://www.hellyeahai.com/ |
| Demo | https://www.hellyeahai.com/demo |
| X | https://x.com/hellyeah_ai |
| LinkedIn | https://www.linkedin.com/company/hellyeahai |
| Discord | https://discord.com/invite/DG9QE7paSB |

---

## 9. Agent 生成规则

> 同事说「基于本文档，生成提交到 **[站点名]** 的内容」时，Agent 按以下流程执行。

### 9.1 生成流程

1. **读 §2** — 确认站点提交入口、费用档位（用客户指定的档位）
2. **读 §3** — 获取该站的受众画像、调性偏好、奏效角度、避雷清单、独有字段
3. **从 §8 组合文案**：
   - **Name**：按 §3 画像选。TAAFT 用 N3（与官网 title 一致）；开发者向用 N4；其余用 N1/N2
   - **Tagline**：每个站选**唯一** tagline，同一条至多 2 站使用。优先选匹配该站画像的叙事角度
   - **One-Liner**：默认 OL5/OL6/OL7（CLI）；通用目录可考虑 OL1-OL4
   - **Short Description**：默认 SD4（CLI）。若该站有长文空间（如 Aixploria Verified 1000 字）且画像偏品牌向，可用 SD1/SD2/SD3 作为基础后扩展
   - **Feature Bullets**：选 3-4 条。优先 RCLL 四步（FR1+FC1+FL0+FN1）；按 §3「什么奏效」决定是否补充平台/能力线 bullet
   - **Use Case**：选 1-2 条，匹配 §3 受众画像
   - **Pricing**：默认 P0；站内有价格筛选时加 P3
   - **Social / Trust**：从 §8.8 + §8.9 取用
4. **对照 §0 事实锚** — 确保：无 $1,500、无 SOC 2 Type II、无 /platforms/* 链接、Déjà Vu 不写已 GA
5. **输出格式** — 按该站表单字段列出 Name / Tagline / Description / Features / Use Case / Pricing / Category / URL / Logo / Social

### 9.2 核心约束

- **CLI 叙事为默认**，平台叙事为补充
- **每个站的 tagline 必须不同**
- **Features 每站 3-4 条**，不堆砌
- **以下禁止出现在任何提交中**：
  - $1,500/月或任何官网未公开的月费数字
  - SOC 2 Type II（官网未展示）
  - `/platforms/*` 链接（404）
  - Déjà Vu 写成已 GA（实为 Private alpha）

### 9.3 生成质量自检

生成后确认：
- [ ] 是否与 §3 该站画像（受众/调性/奏效角度）一致？
- [ ] 是否通过了 §0 事实锚检查（无禁用项）？
- [ ] Tagline 是否与其他已生成站点不重复？
- [ ] 是否包含了该站的独有字段（如 TAAFT 的 Task 关联、TopAI 的截图提醒）？

---

## 10. 生成示例

> 以下展示 Agent 按 §9 规则生成的典型输出。仅作格式参考，不替代实际生成。

### 示例 A：生成「提交到 TAAFT」的内容

```
Name: Hellyeah — npm install your growth engine
Tagline: Research, Create, Launch, Learn — One Growth Loop

Description:
Hellyeah is the AI-native CLI for growth teams who have outgrown spreadsheets
and Sunday-night campaign sprints. Install once, then run a continuous
Research → Create → Launch → Learn loop: agents scrape competitive and
audience signals, generate on-brand copy and creatives, push to Meta, Google,
TikTok, Klaviyo, and your CMS with spend caps and rollbacks, then promote
winners into shared growth memory. Capabilities span performance marketing,
SEO/GEO, lifecycle automation, creative testing, and agentic influencer
campaigns. ISO 27001-aligned controls, GDPR/CCPA-ready. Start in minutes —
no credit card; book a demo for enterprise deployment.

Features:
- Research — competitive scrape, audience clustering, channel-fit scoring,
  hypothesis generation
- Create — copy, image, video, and landing pages under brand-policy guardrails
- Launch — Meta, Google, TikTok, Klaviyo, CMS with spend caps, approvals,
  atomic rollback
- Learn — Bayesian winner promotion, loser auto-prune, growth memory write-back

Use Case: Run 10x more experiments without hiring — AI designs, launches, and
learns autonomously. Built for AI-native startups and growth leads.

Pricing: CLI Beta — start in minutes, no credit card
Category: Marketing / Business
URL: https://www.hellyeahai.com/
Social: X · LinkedIn · Discord

Tasks (TAAFT only): Ad campaign management, SEO & GEO optimization,
Lifecycle automation, Influencer marketing
```

### 示例 B：生成「提交到 FutureTools」的内容

```
Name: Hellyeah — AI Growth CLI
Tagline: Custom AI Agents That Run Your Growth — 24/7

Description:
Hellyeah is the AI-native CLI for building, testing, and scaling growth
campaigns — one command layer where agents research, create, launch, and learn
across Meta, Google, TikTok, Klaviyo, and your stack. Replace 80-hour weekly
growth sprints with an 8-second agent loop: research, creative, launches, and
learning run 24/7 with spend caps, approvals, and an immutable audit log.
Every campaign inherits past wins, ranks hypotheses daily, and ships the next
move with brand-policy guardrails built in. ISO 27001-aligned. CLI Beta —
start in minutes, no credit card.

Features:
- Research — competitive scrape, audience clustering, hypothesis generation
- Create — copy, image, video under brand-policy guardrails
- Launch — Meta, Google, TikTok, Klaviyo, CMS with spend caps and rollbacks
- Learn — Bayesian winner promotion, growth memory write-back

Use Case: For AI-native startups — when anyone can prompt software into
existence, Hellyeah is the distribution layer. For growth leads — run 10x
more experiments without hiring.

Pricing: CLI Beta — free, no credit card, bring your own LLM
Category: Marketing
URL: https://www.hellyeahai.com/
Social: X · LinkedIn · Discord
```

---

*关联任务：[hellyeah-project-tasks.md](./hellyeah-project-tasks.md)*
