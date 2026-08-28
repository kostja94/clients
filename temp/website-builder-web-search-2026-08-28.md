# 深度搜索报告 — Website Builder / AI Website Builder

> **检索基准日**：2026-08-28  
> **时间范围**：2026 年以来优先；历史基线追溯至品类形成期（2010s–2025）  
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档；唯一本地输入为本元文档与 KB 结构模板  
> **Loop 轮次**：7 轮（R1 英文广度 + R1b 中文补充 + R2–R6 长尾 + R7 交叉验证）  
> **来源统计**：Tier 0 12 · Tier 1 14 · Tier 2 4  
> **置信度摘要**：概念基线三问（定义/类型/产品地图）已多源互证；AI agentic 趋势与平台锁定风险有 Tier 0/1 支撑；精确搜索量/买家意图量化数据在 Tier 1 公开渠道未覆盖。

---

## 1. 执行摘要

**Website builder（网站构建器）** 是一类面向非技术用户的 SaaS 工具：通过拖拽/WYSIWYG 或 AI 对话，在厂商托管基础设施上创建、发布并维护网站，典型包含模板、托管、域名与基础营销能力（TechTarget，2025-01-14；Webflow 官方 glossary）。与 open-source CMS（WordPress.org）或 headless CMS 相比，其边界在于**更低上手成本、更少底层控制、更高 vendor lock-in 风险**（TechTarget，2025-01-14）。

**2026 品类增量**：竞争焦点从「模板 + 拖拽」转向 **AI 即时生成** 与 **agentic 全链路**（建站 → 后端/电商/营销自动化）。Wix（2023-07-17）、WordPress.com（2025-04-09）、Squarespace Blueprint AI（官方 2026-01-06）、Hostinger AI Builder（2026-08-18）均已在 Tier 0 披露 prompt/conversation 建站；Hostinger 进一步宣称 agentic 平台可自动开通商店、用户系统与邮件营销（Tier 0，2026-08-18）。

**市场份额（W3Techs，2026-08-28）**：在已知 CMS 的网站中，Wix 6.1%、Squarespace 3.5%、Webflow 1.2%、Duda 1.1%、GoDaddy Website Builder 0.9%；WordPress 仍占 59.0% 但属 adjacent open CMS，非本品类核心。

**社区反响（Tier 2）**：HN 对 Wix AI 偏 pragmatic——认可非技术用户价值，但批评编辑器性能与模板约束；WordPress.com AI builder 讨论集中在 **WordPress.com vs WordPress.org 混淆** 与 blocks 路线争议（HN，2023-07、2025-04）。

**权威缺口**：Gartner/Forrester 针对「website builder」品类的 Magic Quadrant 未在公开检索中找到；Semrush/Ahrefs 级搜索量数据无 Tier 1 直接来源，见 §8。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `what is website builder site:techtarget.com` | TechTarget 三分法：custom / website builder / open-source WCMS |
| R1 | `site:w3techs.com Wix Squarespace market share` | W3Techs 2026-08-28 份额：Wix 6.1%、Squarespace 3.5%、Webflow 1.2% |
| R1 | `AI website builder 2026 TechCrunch Wix Hostinger` | Wix AI Site Generator、WordPress.com AI、Hostinger agentic 叙事 |
| R2 | `Framer 2B valuation site:techcrunch.com` | Framer $2B 估值、50 万 MAU、$50M ARR（2025-08-28） |
| R2 | `Webflow Vidoso acquisition site:techcrunch.com` | Webflow 定位「agentic marketing platform」（2026-03-12） |
| R3 | `website builder SEO limitations Wix Squarespace` | SEO 能力已大幅改善但大规模/程序化 SEO 仍受限（需 Tier 1 互证） |
| R3 | `site:news.ycombinator.com Wix AI website builder` | HN：Wix AI = 模板选择 + 默认内容 + 拖拽续编 |
| R4 | `Squarespace Blueprint AI site:squarespace.com` | Blueprint AI：<4 分钟建站；发布率 +10%、首日图库搜索 -18%（官方） |
| R4 | `website builder vs CMS site:techtarget.com` | 与 CMS/headless/landing page 边界澄清 |
| R5 | `Durable AI website builder site:durable.co` | Durable Tier 0：30 秒生成 + CRM/开票（无 Tier 1 独立评测） |
| R1b | `AI网站生成器 2026 Hostinger Wix 迁移` | 中文媒体强调平台锁定与 Hostinger/Wix 定价差异（非 Tier 1，仅作信息差） |
| R6 | `website builder market size 2026 Mordor Intelligence` | 市场规模区间 $2.4B–$3.57B（2026），研究方法差异大 |
| R7 | 交叉验证 Wix SEO + lock-in + Framer enterprise | 汇总 §7.0 diff 表，确认单源项隔离 |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线三问：Q1 Website builder 是什么 | `website builder definition TechTarget` | **已覆盖** |
| 概念基线三问：Q2 有哪些类型 | `types drag-and-drop AI instant design-first` | **已覆盖**（分类依据：交付形态 + 创建范式，见 §4.2） |
| 概念基线三问：Q3 知名产品/方案 | `site:w3techs.com content management` | **已覆盖**（份额来自 W3Techs；AI 代表产品来自 Tier 0/1） |
| AI website builder 趋势 | `Wix AI Site Generator`, `Hostinger AI Builder launch` | **已覆盖** |
| 平台 lock-in / 迁移 | `vendor lock-in website builder TechTarget` | **已覆盖** |
| SEO 能力与天花板 | `Wix Squarespace SEO 2026` | **部分**（核心事实有 TechTarget + 官方；深度 SEO 工程细节多为非 Tier 1） |
| 买家意图 vs 相邻品类 | `website builder vs CMS vs ecommerce` | **已覆盖** |
| 搜索量/意图信号 | `website builder search volume Gartner` | **权威源未覆盖**（无 Tier 1 搜索量报告） |
| 中文语境 | `AI网站生成器 2026` | **已覆盖**（补充锁定风险与定价，核心事实仍靠英文 Tier 0/1） |

---

## 4. 核心发现（多源验证）

### 4.1 Website Builder 是什么

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 面向非技术用户的建站工具，拖拽/WYSIWYG，集成托管 | [TechTarget](https://www.techtarget.com/enterprise-software/tip/Drupal-vs-WordPress-vs-Joomla-Whats-the-difference) T1，2025-01-14 | [TechTarget CMS 定义](https://www.techtarget.com/searchcontentmanagement/definition/content-management-system-CMS) T1 | **已确认** |
| 相较 open-source WCMS：更少定制、更易 vendor lock-in | TechTarget T1 | [GoDaddy GoCentral 报道](https://techcrunch.com/2017/01/25/godaddys-new-site-builder-offers-templates-for-1500-industries/) T1，2017-01-25 | **已确认** |
| 与 headless CMS 边界：一体化 front+back，非 API-first 多渠道 | [TechTarget headless vs traditional](https://www.techtarget.com/enterprise-software/feature/Traditional-CMS-vs-headless-CMS-Whats-the-difference) T1 | [Webflow CMS feature](https://webflow.com/feature/cms) T0 | **已确认** |
| **非** pure ecommerce platform：可含商店模块但品类核心是「站点存在 + 内容」 | TechTarget Wix 条目 T1 | WordPress.com AI 明确不支持复杂电商（TechCrunch，2025-04-09）T1 | **已确认** |

**叙述**：Website builder 属于 **no-code/low-code 建站 SaaS** 子集（TechTarget low-code 定义可互证）。典型交付 = 可视化编辑 + 厂商托管 + 模板/组件库 + 域名/SSL/基础 SEO 面板。买家诉求是「快速上线可访问的 .com」，而非内容模型治理或全栈开发。与 **headless CMS**（Contentful 等）的分界：后者分离 content API 与 presentation；website builder 保持 monolithic 体验以换取速度（TechTarget，2025）。

### 4.2 Website Builder 有哪些类型

**分类依据**：采用 TechTarget「建站路径三分法」+ 2023–2026 Tier 0/1 披露的 **AI 创建范式** 叠加（非自创 taxonomy）。

| 类型（分类依据：创建范式 × 托管形态） | 特征 | 典型场景 | 来源 |
|-----------------------------------|------|----------|------|
| **A. 模板优先 · 一体化托管（Template-first all-in-one）** | 拖拽编辑器、应用市场/扩展、厂商托管 | SMB 官网、本地服务、简单博客 | TechTarget；Wix/Squarespace/GoDaddy T0 |
| **B. 设计优先 · 视觉开发（Design-first visual）** | 高保真布局、设计系统、团队更新无需工程 | 品牌官网、SaaS marketing site、设计师主导 | Framer TC 2025-08-28；Webflow T0 |
| **C. AI 即时生成 · 对话/问卷建站（AI instant / prompt-first）** | Prompt/问卷 → 整站骨架+文案+图；后续可进拖拽 | 个体户、极速 MVP、非技术创始人 | Wix AI TC 2023-07-17；Squarespace Blueprint T0；Durable T0 |
| **D. Agentic 平台 · 建站+运营自动化（2026 新兴）** | AI 不只生成首页，还配置后端、电商、营销 | 从「网站」扩展到 SaaS/portal/store 一体化 | Hostinger AI Builder T0 2026-08-18；Webflow+Vidoso TC 2026-03-12 |
| **E. CMS 桥接型（Hosted CMS + builder UX）** | 底层 WordPress 等，上层 AI/可视化 builder | 需要 CMS 生态但要降低门槛 | WordPress.com AI TC 2025-04-09 |

**易混淆点**：
- **Type C vs D**：C 侧重「首次生成速度」；D 侧重「生成后 AI 持续操作业务系统」（Hostinger 官方区分 handoff 消除点，2026-08-18）。
- **Webflow/Framer vs Wix**：前者偏 B（设计/视觉开发），后者偏 A+C；Webflow 自宣 hybrid CMS，但仍属 hosted builder 品类（Webflow T0）。
- **Shopify**：W3Techs 计为 CMS 份额 7.7%，但买家意图是 ecommerce-first，应分流至 `ecommerce-website-builder`（W3Techs 2026-08-28）。

### 4.3 知名产品 / 代表方案

#### 按 W3Techs 使用量/份额（2026-08-28，已知 CMS 网站）

| 场景或类型 | 代表产品 | 备注（份额/定位） | 来源 |
|-----------|----------|------------------|------|
| 一体化模板 builder | **Wix** | CMS 份额 **6.1%**；全站 4.2% | [W3Techs](https://w3techs.com/technologies/comparison/cm-drupal,cm-squarespace,cm-wix) |
| 设计导向 SMB | **Squarespace** | CMS 份额 **3.5%** | W3Techs |
| 视觉开发 + CMS | **Webflow** | CMS 份额 **1.2%**；年趋势稳定上升 | [W3Techs 历史](https://w3techs.com/technologies/history_overview/content_management/ms/y) |
| 代理机构/multi-site | **Duda** | CMS 份额 **1.1%** | W3Techs |
| 域名+建站捆绑 | **GoDaddy Website Builder** | CMS 份额 **0.9%** | W3Techs |
| WordPress 插件层 builder | **Elementor** | CMS 份额 **18.6%**（属 WP 生态，非纯 hosted builder） | W3Techs comparison |

#### 按 AI / 2026 产品动态（Tier 0/1，非份额排名）

| 代表产品 | AI 能力要点 | 定位 | 来源 |
|----------|------------|------|------|
| **Wix AI Site Generator** | Prompt → 首页+内页+文案+图；可嵌入电商/预约/票务组件 | 成熟 A+C 平台 | TechCrunch 2023-07-17 T1 |
| **Squarespace Blueprint AI** | <4 分钟；AI 图/文案/布局；Design Intelligence | 设计品质 + AI onboarding | Squarespace 官方 2026-01-06 T0 |
| **WordPress.com AI Builder** | 聊天式；30 免费 prompt；不支持复杂电商 | CMS 桥接 E | TechCrunch 2025-04-09 T1 |
| **Hostinger AI Builder** | Agentic；后端/电商/Reach 邮件原生；2026-08-18 GA | 预算型 agentic D | Hostinger 官方 2026-08-18 T0 |
| **Durable** | ~30 秒三问生成；CRM/开票/预约 bundled | 个体户 AI instant C | Durable 官方 T0 |
| **Framer** | 设计优先 + AI；50 万 MAU；$50M ARR | 设计团队 B | TechCrunch 2025-08-28 T1 |

**Top 5（综合：份额 + AI 代表性，供 KB 索引）**：**Wix · Squarespace · Webflow · Framer · Hostinger AI Builder**（Durable 作 AI-native 候补，份额统计未入 W3Techs Top tier）。

### 4.4 增量维度：AI 趋势、锁定、SEO、买家意图

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 2026 竞争从 drag-and-drop 转向 prompt/agentic | Wix CEO 引语 TC 2023 | Hostinger VP 引语 T0 2026-08-18 | **已确认** |
| Website builder 可导致 vendor lock-in | TechTarget 2025-01-14 | WordPress.com AI：仅新站、需 hosting plan（TC 2025-04-09） | **已确认** |
| 迁移通常需重建而非一键导出 | TechTarget lock-in | HN WordPress.com：与 .org 生态隔离（Tier 2 观点+TC 事实） | **很可能** |
| Google **不**因 Wix/Squarespace 惩罚；但大规模 SEO 受平台天花板约束 | TechTarget 未直接写；需 Tier 1 SEO 互证 | Wix 官方 SEO 工具集 + TechCrunch Wix AI 提及 spam 风险（2023） | **很可能**（SEO 细节单源偏多） |
| 买家选 builder vs CMS：简单 presence → builder；omnichannel/复杂内容 → CMS | TechTarget CMS 选型 2020 | TechTarget headless 2025 | **已确认** |

---

## 5. 时间线

| 日期 | 事件 | 来源（Tier） |
|------|------|-------------|
| 2012-10 | Wix HTML5 builder + App Market | TechCrunch T1 |
| 2017-01 | GoDaddy GoCentral：1500 行业模板 | TechCrunch T1 |
| 2023-07 | Wix 发布 AI Site Generator | TechCrunch T1 |
| 2025-04 | WordPress.com 免费 AI website builder | TechCrunch T1 |
| 2025-08 | Framer $2B 估值；$50M ARR | TechCrunch T1 |
| 2026-01 | Squarespace Blueprint AI 指南更新；发布率 +10% | Squarespace T0 |
| 2026-03 | Webflow 收购 Vidoso；定位 agentic marketing | TechCrunch T1 |
| 2026-08-18 | Hostinger AI Builder 全球发布 | Hostinger T0 |

---

## 6. 实体关系（如适用）

```
[买家: SMB / 个体户 / 设计团队]
        │
        ▼
┌───────────────────────────────────────┐
│     Website Builder 品类 (hosted SaaS)   │
├─────────┬─────────┬─────────┬─────────┤
│ Type A  │ Type B  │ Type C  │ Type D  │
│ Wix     │ Framer  │ Durable │Hostinger│
│Squarespace│Webflow │ Wix AI  │ AI Bldr │
│ GoDaddy │         │ SQ BP   │ Webflow │
└─────────┴─────────┴─────────┴─────────┘
        │ lock-in / 托管绑定
        ▼
   [Adjacent: WordPress CMS · Shopify ecommerce · Headless CMS · Landing page SaaS]
```

---

## 7. 增量信息

### 7.0 增量对照表（多源 diff）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源（Tier） | 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|-----------------|---------|---------|--------|
| Hostinger 客户项目 12 个月内非传统网站占比 ~20% | 官方未在旧 Website Builder 文档中披露 | Hostinger blog 2026-08-18 T0 | — | 单源 Tier 0 | **很可能（单源）** |
| Squarespace Blueprint 试用发布率 +10% | 运营指标 | Squarespace 2026-01-06 T0 | — | 单源 Tier 0 | **很可能（单源）** |
| Framer 企业客户已成新客多数 | 战略转向 B2B | TechCrunch 2025-08-28 T1 | Framer CEO 引语 | 单源 T1 | **很可能（单源）** |
| Webflow 自定位为 agentic marketing platform | 超越 website builder 标签 | TechCrunch 2026-03-12 T1 | Webflow CEO 引语 | 单源 T1 | **很可能（单源）** |
| Wix AI 可能加剧低质 SEO 内容/spam | 官方未在发布公告强调 | TechCrunch 2023-07-17 T1（记者分析） | HN 用户顾虑 T2 | 观点类 | **待核实**（解读/风险，非事实） |
| Hostinger AI 生成后不可换模板 | 官方产品页未强调 | 中文/个人对比文 | Hostinger 官方未否认 | 待 Tier 0/1 | **待核实** |
| 2026 全球 website builder 市场 $3.57B | — | Mordor Intelligence T1? | Fact.MR $2.4B | 方法分歧 | **很可能（研究口径差异）** |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| Hostinger AI Builder 将 backend/ecommerce/marketing 原生集成，消除「生成后 handoff」 | [Hostinger blog](https://www.hostinger.com/blog/ai-builder-launch/) T0，2026-08-18 | 已确认 | Tier 0 全文 |
| Squarespace Blueprint AI 官方称帮助试用用户发布率提升 10% | [Squarespace AI 指南](https://www.squarespace.com/blog/guide-to-squarespace-ai-tools) T0，2026-01-06 | 很可能 | 单源 Tier 0 |
| Framer 2025 年 ARR $50M、break-even | [TechCrunch](https://techcrunch.com/2025/08/28/no-code-website-builder-framer-reaches-2b-valuation/) T1，2025-08-28 | 很可能 | 单源 T1，公司发言人 |
| WordPress.com AI builder 30 免费 prompts；复杂电商不支持 | [TechCrunch](https://techcrunch.com/2025/04/09/wordpress-com-launches-a-free-ai-powered-website-builder/) T1，2025-04-09 | 已确认 | |
| Wix AI Site Generator 可自动嵌入 ecommerce/scheduling/food ordering | [TechCrunch](https://techcrunch.com/2023/07/17/wixs-new-tool-can-create-entire-websites-from-prompts/) T1，2023-07-17 | 已确认 | |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源（Tier） | 拒绝原因 |
|----------|-------------|---------|
| Hostinger 是 2025–2026 搜索量最高的 AI builder | designingit.com / ecommerce-platforms.com | 非 Tier 1；联盟/测评站 |
| Agentic builder 完全取代模板时代 | 10web.io blog | 厂商营销文，非独立 Tier 1 |
| Google 惩罚 Wix/Squarespace | 部分 SEO 博客 | 与「无平台惩罚、有架构天花板」的 Tier 1 叙述冲突且无 Google 官方惩罚声明 |

### 7.3 权威媒体解读

- **Wix（TechCrunch，2023）**：生成式 AI 迫使品类重新定义「builder 抽象层」——客户不愿再逐像素定制；但 AI 生成内容 spam/幻觉风险需厂商 moderation（OpenAI moderation + 内部 abuse 工具）。
- **Framer（TechCrunch，2025）**：Website builder 赛道与 Figma、Squarespace、Wix 及 Cursor/Lovable 等 vibe coding 平台同台竞争；Framer 押注 enterprise + 「run entire .com」。
- **Webflow（TechCrunch，2026）**：收购 Vidoso 标志从 site builder → **agentic marketing platform**；强调 brand-governed AI content vs 泛化 frontier model 输出。
- **WordPress.com（TechCrunch，2025）**：AI builder 是对 Squarespace/Wix 的直接竞争回应；与开源 WordPress 生态刻意隔离。

### 7.4 社区与舆论反响

**Wix AI Site Generator（HN，2023-07）**  
- **支持**：非技术用户可快速获得「够用」站点；托管一体化适合 nonprofit/SMB 志愿者维护。  
- **批评**：WYSIWYG 编辑器加载慢、操作迟钝；AI 本质是「选模板 + 填内容」而非真正 custom code；设计师推荐 Framer。  
- **技术人观点**：与 FrontPage 时代 WYSIWYG 同类优缺点；可 work with it 但非最优。

**WordPress.com AI Builder（HN，2025-04）**  
- **混淆点**：标题应区分 WordPress.com（托管商）vs WordPress.org（开源）。  
- **战略解读**：应对 Elementor 等 builder 插件蚕食；blocks/FSE 路线延续。  
- **情绪**：对 Automattic/WP Engine 纠纷背景下「投资人焦虑」的讨论。

**Hostinger AI Builder（2026-08-18 后）**  
- 检索范围内 **HN/Reddit 尚无显著热帖**；中文 Neodrop 等对官方 agentic 叙事转述（非 Tier 1）。

### 7.5 争议与风险

| 风险 | 要点 | 来源 |
|------|------|------|
| **Vendor lock-in** | 导出/迁移常需重建；TechTarget 明确列为 website builder 缺陷 | TechTarget 2025 |
| **AI 内容质量** | 低质/重复 SEO 内容；hallucination；版权 | TechCrunch Wix 2023 |
| **SEO 天花板** | 100–500+ 页站点：URL 架构、schema 规模、server header、log 分析受限 | TechTarget + 工程向分析（非全部 Tier 1） |
| **平台混淆** | WordPress.com vs .org；Hostinger Website Builder vs WordPress 主机 | TechCrunch 2025；中文 idcspy 2026 |
| **定价陷阱** | 长期预付低价、续费跳涨 | 中文 idcspy（信息差）；Hostinger 官方价需用户自行核对 |

### 7.6 竞品与行业对照

| 相邻品类 | 与 website builder 分界 | 来源 |
|----------|------------------------|------|
| **Open-source CMS**（WordPress.org） | 更高灵活/自托管；更高维护成本 | TechTarget 2025 |
| **Headless CMS** | API-first、omnichannel；需 front-end 工程 | TechTarget 2025 |
| **Ecommerce platform**（Shopify） | 核心验收=交易/库存；Wix 等仅部分场景 | TechTarget；W3Techs |
| **Landing page builder** | 单页/活动页、转化；非完整站点 IA | TechTarget event marketing 间接 |
| **App builder**（Bubble 等） | 应用逻辑/数据库；Hostinger 2026 模糊网站/应用边界 | Hostinger T0 |

### 7.7 中文语境

- **36氪/量子位/少数派**：本轮检索未命中 2026 年 Tier 1 深度稿；中文 idcspy、站长百科、zzbaike 等汇总 Hostinger/Wix/Durable 定价与 **迁移需重做** 警告（2026-08），与 TechTarget lock-in 一致，但 **不得作为份额/排名事实源**。
- **Neodrop（2026-08）**：转述 Hostinger AI Builder 全球可用与 agentic 链路，与 Tier 0 一致。
- **国内开发者讨论**：平台锁定、WordPress 导出、AI 生成代码能否「换平台部署」——与英文 HN 对 WordPress.com 隔离的讨论同构。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| 2026 市场规模 | Mordor：$3.57B | Fact.MR：$2.4B | 引用时标注研究口径；不写单一「官方数字」 |
| AI builder 搜索热度 | 联盟测评称 Hostinger #1 | 无 Semrush/Gartner 公开数据 | 标注「Tier 1 未覆盖」；用 W3Techs 采用率作 proxy |
| Wix/Squarespace SEO | 「无惩罚、可排名」 | 「大规模站点架构受限」 | 并存：不惩罚 ≠ 无天花板 |
| Hostinger 生成后能否换模板 | 第三方称不可换模板 | Hostinger 官方未明确 | 待官方文档或 Tier 1 评测 |

---

## 9. 对用户问题的直接回答

### 9.1 Website Builder 是什么

面向非技术用户、在厂商托管环境内通过可视化或 AI 交互创建和维护网站的 SaaS 工具，通常打包模板、拖拽编辑、托管、域名与基础营销/SEO 能力；相对 open-source CMS 更易上手但定制性更低、vendor lock-in 更高（TechTarget，2025-01-14）。

### 9.2 有哪些类型

按 **创建范式 × 托管一体化程度**：  
A 模板一体化（Wix、Squarespace、GoDaddy）· B 设计/视觉开发（Framer、Webflow）· C AI 即时生成（Durable、Blueprint AI、Wix AI）· D Agentic 全链路（Hostinger AI Builder、Webflow 营销化）· E CMS 桥接（WordPress.com AI）。

### 9.3 有哪些知名产品 / 代表方案

**使用量（W3Techs，2026-08-28）**：Wix 6.1%、Squarespace 3.5%、Webflow 1.2%、Duda 1.1%、GoDaddy WB 0.9%。  
**AI/2026 代表**：Wix AI Site Generator、Squarespace Blueprint AI、WordPress.com AI Builder、Hostinger AI Builder、Durable、Framer。

---

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方
- https://www.hostinger.com/blog/ai-builder-launch/（2026-08-18）
- https://www.squarespace.com/blog/guide-to-squarespace-ai-tools（2026-01-06）
- https://www.squarespace.com/websites/ai-website-builder
- https://durable.co/ai-website-builder
- https://webflow.com/feature/cms
- https://webflow.com/glossary/cms

### Tier 1 权威媒体
- https://www.techtarget.com/enterprise-software/tip/Drupal-vs-WordPress-vs-Joomla-Whats-the-difference（2025-01-14）
- https://www.techtarget.com/searchcontentmanagement/definition/content-management-system-CMS
- https://www.techtarget.com/enterprise-software/feature/Traditional-CMS-vs-headless-CMS-Whats-the-difference
- https://techcrunch.com/2023/07/17/wixs-new-tool-can-create-entire-websites-from-prompts/
- https://techcrunch.com/2025/04/09/wordpress-com-launches-a-free-ai-powered-website-builder/
- https://techcrunch.com/2025/08/28/no-code-website-builder-framer-reaches-2b-valuation/
- https://techcrunch.com/2026/03/12/webflow-buys-ai-content-generation-platform-vidoso-to-bolster-its-marketing-suite/
- https://techcrunch.com/2017/01/25/godaddys-new-site-builder-offers-templates-for-1500-industries/

### Tier 2 补充（反响/社区/统计）
- https://news.ycombinator.com/item?id=36757778（Wix AI，2023）
- https://news.ycombinator.com/item?id=43654279（WordPress.com AI，2025）
- https://w3techs.com/technologies/comparison/cm-drupal,cm-squarespace,cm-wix（2026-08-28）
- https://w3techs.com/technologies/history_overview/content_management/ms/y
- https://www.mordorintelligence.com/industry-reports/website-builders-market（市场规模，方法论独立）

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-08-28，共 7 轮 loop。*
