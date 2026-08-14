## 平台与能力内链路由

> **Phase 0 第五问 + Phase 4 内链规划必查**

### 1. 四平台 OS 分层

| 平台 | URL | 角色 | 一句话 |
|------|-----|------|--------|
| **AIMA** | `/aima` | Agent / orchestration | AI Marketing Assistant · WhatsApp-first · **$0 Free** |
| **Forge** | `/forge` | Execution | 六系统执行层（Data→Asset、Event Trigger、Copy A/B、Compliance、Creative、Influencer Dashboard） |
| **Mutation** | `/mutation` | Intelligence | 外部信号 → 营销情报 · ~60s 响应叙事 |
| **Déjà Vu** | `/deja-vu` | Experimentation | Continuous experimentation · **private alpha** |

**Capabilities 索引 FAQ 三层**：AIMA = orchestration · Forge = execution · Mutation = intelligence · Déjà Vu = experimentation。

**Manifesto 叙事**：AIMA sees · Mutation reacts · Forge builds · Déjà Vu remembers。

### 2. RCLL 与 AIMA 页内四步

| 全站 RCLL | AIMA 页内用词 | 要点 |
|-----------|--------------|------|
| Research | Plan（AIMA 页） | 竞品/受众/渠道/假设 |
| Create | Create | 文案/图/视频/落地页 + brand policy |
| Launch | Launch | Meta, Google, TikTok, Klaviyo, CMS；spend cap / rollback |
| Learn | Optimize（AIMA 页） | Bayesian 优胜 / memory write-back |

博客可同时使用 RCLL（全站）或 Plan→Create→Launch→Optimize（AIMA 语境），但须一致不混用同段。

### 3. 六能力线 → 何时链

| 能力 | URL | 链入场景 |
|------|-----|---------|
| Agentic Marketing | `/capabilities/agentic-marketing` | 工作流编排、launch 速度、ops 自动化 |
| Performance Marketing | `/capabilities/performance-marketing` | ROAS、paid ads、预算浪费 |
| SEO / GEO | `/capabilities/seo-geo` | **所有 GEO 话题 canonical**；programmatic content |
| Lifecycle Automation | `/capabilities/lifecycle-automation` | email/SMS/WhatsApp 旅程 |
| Creative Generation | `/capabilities/creative-generation` | 创意 A/B、素材批量 |
| Influencer Marketing | `/capabilities/influencer-marketing` | KOL 规模、达人 ROI |

### 4. CTA 分层（按文章类型）

| 文章类型 | 主 CTA | 次 CTA | 全文 CTA 上限 |
|---------|--------|--------|:------------:|
| Pillar / Framework | `/capabilities/{relevant}` | `/demo` | ≤2 |
| CommercialEducational | `/aima` | `/capabilities/performance-marketing` | ≤2 |
| PlatformExplainer | 对应平台页 | `/demo` | ≤2 |
| Alternative | `/demo` | `/aima` 或 capability | ≤2 |
| UseCase | `/for/{arena}` | `/demo` + 相关 capability | ≤2 |
| Diagnosis | 相关 capability | `/demo` | ≤2 |
| Compliance | `/security` | `/demo` | ≤2 |

**硬规则**：
- 企业采购意图 → 优先 `/demo`
- 创始人 / 少人头 / AI ads manager 教育 → 优先 `/aima`
- GEO 任何类型 → 必链 `/capabilities/seo-geo`（P5）

### 5. AIMA 内置六 Agent（页内命名，PlatformExplainer 可用）

| Agent | 角色 |
|-------|------|
| strategos | Strategist — 周计划、预算、渠道 |
| scribe | Copywriter |
| forge | Designer — 图/视频 |
| trader | Media Buyer |
| lighthouse | Lifecycle Op — email/SMS/WhatsApp |
| oracle | Analyst — 阈值与 recap |

### 6. AIMA 渠道（OAuth，页内列表）

Meta Ads, Google Ads, TikTok Ads, Reddit, Pinterest, X, LinkedIn, WhatsApp, Klaviyo, Shopify, WooCommerce, Instagram, YouTube, Mailchimp, Threads, +and more

**教育文注意**：若写「全渠道统一视图」，须与 AIMA 页内实际 OAuth 列表一致；勿抽象为未接入平台。

### 7. Persona → 默认落地页

| Persona | 默认链 |
|---------|--------|
| CMO / VP Marketing | `/solutions/improve-marketing-roi` · `/demo` |
| Head of Growth | Agentic capability + `/deja-vu` |
| Performance Lead | `/capabilities/performance-marketing` · `/aima` |
| Lifecycle Lead | `/capabilities/lifecycle-automation` |
| Influencer Lead | `/capabilities/influencer-marketing` |
| RevOps | `/mutation` · `/forge` |
| Founder / Indie | `/aima` · `/#cli` |
| Growth engineer | `/` · `/about` |

### 8. Arena → 案例关联

| Arena | URL | 案例 |
|-------|-----|------|
| Mobile Applications | `/for/mobile-apps` | BeFreed, The Dyrt |
| B2B & Enterprise | `/for/b2b-enterprise` | Eragon |
| Consumer Tech | `/for/consumer-tech` | Final Round AI, Viggle, Fish Audio |
| E-Commerce | `/for/ecommerce` | — |
| Gaming & Entertainment | `/for/gaming` | Playco |
| Fintech | `/for/fintech` | Truist |
| EduTech | `/for/edutech` | — |

UseCase 文须链 ≥1 Arena + ≥1 capability + 可选 `/customers/{slug}`。

### 9. Cannibalization 边界

| 页面类型 | 博客角色 | 边界 |
|---------|---------|------|
| `/capabilities/seo-geo` | GEO **canonical 详述** | 博客 = 教育/对比/框架；不复制 capability 页全文 |
| `/aima` | AIMA **转化** | 博客 CommercialEducational = 品类教育；不抢 AIMA 页主转化意图 |
| `/demo` | 企业转化 | 博客 CTA 克制，≤2 次 |
| Capability 页 | 能力 SEO | 博客 Spoke 引述 1–2 句 + link，不逐步展开 How it works |
