# Hellyeah 功能与平台页结构

> **职责**：战术/四平台/能力线叙事、单页模板、Title/Meta；路由见 [hellyeah-others.md](./hellyeah-others.md)。  
> **关联**：[hellyeah.md](./hellyeah.md) | [hellyeah-platform-aima.md](./hellyeah-platform-aima.md)

**Last updated**: 2026-06-02

---

## 1. 能力分层（官网 2026-06-02）

### 1.1 全站增长循环（首页 / About）

| 步骤 | 官网用词 | 要点 |
|------|----------|------|
| Research | Research | 竞品/受众/渠道/假设 |
| Create | Create | 文案/图/视频/落地页 + brand policy |
| Launch | Launch | Meta, Google, TikTok, Klaviyo, CMS；spend cap / rollback |
| Learn | Learn | Bayesian 优胜 / memory write-back |

### 1.2 四平台（线上路径根级）

| 平台 | URL | 官网定位（nav 副标题） |
|------|-----|------------------------|
| **AIMA** | `/aima` | AI Marketing Assistant — WhatsApp-first，**$0** |
| **Forge** | `/forge` | Agentic systems — 六系统执行层 |
| **Mutation** | `/mutation` | Marketing intelligence — 外部信号 |
| **Déjà Vu** | `/deja-vu` | Continuous experimentation — **private alpha** |

三层关系（Capabilities 索引 FAQ）：**AIMA** = agent/orchestration；**Forge** = execution；**Mutation** = intelligence；**Déjà Vu** = experimentation（Solutions 页亦述四层 OS）。

### 1.3 能力线（6，均已上线）

| 能力 | URL | 页内核心统计（站内宣称） |
|------|-----|--------------------------|
| Agentic Marketing | `/capabilities/agentic-marketing` | 8× launch；4× experiments；73% ops 痛点 |
| Performance Marketing | `/capabilities/performance-marketing` | 3.2× ROAS avg；67% wasted spend ↓ |
| SEO / GEO | `/capabilities/seo-geo` | 20–80 文/月；GEO 多模型 |
| Lifecycle Automation | `/capabilities/lifecycle-automation` | 3.4× open rate；80% manual ↓ |
| Creative Generation | `/capabilities/creative-generation` | 47% sales lift（Nielsen 引用） |
| Influencer Marketing | `/capabilities/influencer-marketing` | $24B market；73% ROI 难衡量 |

**GEO canonical**：`/capabilities/seo-geo`（见 [hellyeah-keywords.md](./hellyeah-keywords.md) §4）。

### 1.4 Solutions（5，outcome 向）

| Solution | URL |
|----------|-----|
| Automate Marketing | `/solutions/automate-marketing` |
| Improve Conversion Rate | `/solutions/improve-conversion-rate` |
| Improve Marketing ROI | `/solutions/improve-marketing-roi` |
| Reduce CAC | `/solutions/reduce-cac` |
| Scale Paid Ads | `/solutions/scale-paid-ads` |

---

## 2. 单页模板

> **同质化问题分析（2026-06-15）** → [hellyeah-content-homogenization-audit.md](./hellyeah-content-homogenization-audit.md)（仅诊断，不含改造方案）

**平台页**：Hero outcome → 子系统/Agent → 渠道或信号 → 对比表 → 定价（若 AIMA）→ CTA `/demo` → FAQ。  
**能力页**：Definition → Traditional vs AI → 4-step How it works → Use cases → AIMA/Forge/Mutation 三层 → FAQ → Related capabilities。  
**Arena 页**：Vertical challenge → 4 capabilities cards → 3-step deploy → Outcomes → FAQ。

---

## 3. Title / Meta 草稿（须品牌终审；首页以线上为准）

| 页 | Title（线上或建议） | 备注 |
|----|---------------------|------|
| 首页 | Hellyeah · npm install your growth engine | 线上 `<title>` |
| AIMA | （页内 H1 AIMA） | 子标题 AI Marketing Assistant |
| Capabilities 索引 | Capabilities — AI Growth Platform Features \| Hellyeah | 线上 |
| Performance | AI Performance Marketing Optimization — … \| Hellyeah | 线上 |
| SEO/GEO | SEO / GEO Content Engine — … \| Hellyeah | 线上 |
| Trust | Trust Center（/security） | 线上 H1 |

---

## 4. 内链规则

- 首页 → `/demo` + `/aima` + `/capabilities/agentic-marketing`  
- 各 Capability → **AIMA → Forge → Mutation** 三层块（页内已有）  
- GEO 相关博客/目录提交 → 只链 `/capabilities/seo-geo`  
- 勿链 `/platforms/*`、`/trust-center`、`/arenas/*`

---

## 5. 对外表述禁区（与官网不一致的旧文案）

- ~~SOC 2 Type II~~（除非 security 页更新）  
- ~~$1,500/month 起价~~（AIMA 页为 **$0**；Pod 为 % managed spend）  
- ~~/platforms/aima~~、~~capital engine only~~ 作为唯一 AIMA 叙事（与当前 WhatsApp 产品页并存时需分层）
