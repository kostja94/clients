# Topview - Product Marketing Context

> 基于官网 [topview.ai](https://www.topview.ai/) 与网络搜索  
> 复制到 `.cursor/product-marketing-context.md` 或 `.claude/product-marketing-context.md` 供 AI Agent 使用。

**Last updated**: 2025-03-02

---

## 0. 文档与报告语言策略（实施规则）

**原则**：网站以英文为主；本文档及子文档面向中文读者，用于内部沟通与决策。

| 场景 | 语言 | 说明 |
|------|------|------|
| **网站内容** | 英文 | topview.ai 主站、落地页、博客、产品文案 |
| **文档/报告** | 中文为主 | 策略、分析、解释、待办、洞察——给中国人看 |
| **产品原文** | 英文 | 定位、slogan、key messages、官网文案——保留原文便于对照 |
| **技术/SEO** | 英文 | URL、关键词、hreflang、API 名称——与网站一致 |

**文档内规则**：产品名、功能名、URL、关键词、竞品名、模型名用英文；策略说明、分析、待办、洞察用中文。AI 生成时提示「文档面向中文读者，产品术语保留英文」。

---

## 1. Product Overview

**One-line description**:
```
Topview is an AI Video Agent that generates, edits, and collaborates on viral UGC and marketing videos—upload your product, provide a reference video, and get a complete ad in minutes at a fraction of traditional cost.
```

**Category**: B2B SaaS / AI Video Generation / Marketing Video / UGC Creator  
**Business model**: Freemium + 订阅（Free / Pro / Business / Enterprise）  
**Pricing**: Free $0（10 credits/月）；Pro $18/月；Business $45/月；Enterprise 定制

**产品形态**：
- **Web App**：topview.ai（在线使用）
- **入口**：Dashboard、Pricing、API、Affiliate program
- **多语言**：20 种语言/地区，见 Section 5.3

---

## 2. Positioning Statement

> **For** affiliate marketers, DTC brands, e-commerce sellers, and agencies **who** need scroll-stopping product videos and viral UGC ads without studios, models, or the product on hand, **our** Topview **is an** AI Video Agent **that** understands your creative intent and autonomously generates professional marketing videos—from scripting to final cut. **Unlike** traditional video tools that require manual editing of every frame, **we** let you describe what you want in natural language and deliver in minutes **because** we learn from 5M+ viral videos and recreate any style with your product.

---

## 3. Value Proposition & Key Messages

- **Primary value prop**: 用自然语言描述需求，AI 自动完成从脚本到成片——10 倍速度、80–90% 成本节省、零学习曲线。
- **Key messages**:
  - "Generate, Edit, Collaborate — All in One Place."
  - "Your AI Video Agent."
  - "Create videos 10× faster at a fraction of the cost."
  - "Clone any video style with AI—upload product, provide reference, get a complete video."
  - "Not just editing—AI understands and recreates the entire video concept."
- **Proof points**: 10x 速度、80–90% 成本节省、0 学习曲线；iLive by SHOPNOW 案例：AI 视频服务收入 +80%、人力成本 -50%

---

## 4. Target Audience / ICP

**Primary ICP**:
- **Who**: Affiliate marketers、DTC brands、E-commerce sellers、Agencies
- **Industry**: 营销、电商、联盟营销、广告
- **Jobs to be done**: 快速产出高转化产品视频、UGC 风格广告、病毒式营销内容
- **Pain points**: 传统制作周期长（天/周）、成本高（$1K–10K+）、需要工作室/模特/实物
- **Buying triggers**: 新品上市、广告投放、联盟推广、需要规模化视频产出

**Secondary ICP**: Solopreneurs、内容创作者、直播电商（AI live stream）

**不覆盖**：教育、企业培训（规划中扩展）

**Language / locale**: 英文为主；支持 20 种语言/地区（en、es、fr、pt、it、ja、th、pl、ko、de、ru、da、ar、nb、nl、id、zh、tw、tr）；AI 配音；多语种 URL 见 Section 5.3

---

## 5. Existing Website

- **URL**: https://www.topview.ai/
- **Key pages**: /（首页）、/pricing（定价）、/openapi（API）、/affiliate-program（联盟计划）、/make/advertising、/make/e-commerce、/solutions/*（行业解决方案）、/alternatives（竞品对比）、/models（AI 视频大模型 Board）；API 与 Affiliate 详情见 Section 5.1、5.2；Solutions 详情见 [topview-solutions.md](./topview-solutions.md)；竞品分析见 [topview-competitors.md](./topview-competitors.md)；大模型与 Board 见 [topview-models.md](./topview-models.md)
- **Use cases**：Advertising、Recreate viral video、Affiliate marketing、Ecommerce、DTC brands、AI live stream（规划中）；完整列表见 [topview-use-cases.md](./topview-use-cases.md)
- **AI tools**：AI Video Agent、AI Ads Video、AI Product Video、AI UGC Video、URL to Video、AI Avatar、Product Avatar、Design My Avatar、AI Lip-sync、AI Video Generator、AI Short Video；**Topview Board**：多 AI 视频大模型（Veo、Sora、Kling、Seedance、Hailuo、Wan、Vidu、Runway、Nano Banana 等）统一工作台；功能详情见 [topview-features.md](./topview-features.md)；大模型见 [topview-models.md](./topview-models.md)
- **Resources**：Blog、Case studies、Affiliate program、Learning center
- **Tech stack**: 未公开；Web 应用
- **Current state**: 增长期；强调 AI Video Agent、病毒式 UGC、营销广告

### 5.1 API（/openapi）

**URL**: [https://www.topview.ai/openapi](https://www.topview.ai/openapi)  
**Title**: Topview API: AI Avatars & AI Video Generation

**API 端点**：
| API | 用途 |
|-----|------|
| **Materials to Video** | 图片、脚本、音频 → 营销视频 |
| **URL to Video** | 产品/落地页 URL → 视频 |
| **Video Avatar** | 文本/音频 → 头像视频；支持上传视频克隆头像 |
| **Product Avatar** | 产品图 + AI 头像展示 |
| **Product Anyshoot** | 产品虚拟试穿、场景植入 |

**适用对象**：开发者、营销人、电商平台、SaaS、代理商  
**价值**：10x 视频产出速度、0 人工剪辑、90% 成本降低；支持 MP4、多分辨率、多比例  
**联系**：official@topview.ai

### 5.2 Affiliate Program（/affiliate-program）

**URL**: [https://www.topview.ai/affiliate-program](https://www.topview.ai/affiliate-program)  
**Title**: Topview Affiliate Program

| 项目 | 内容 |
|------|------|
| **佣金** | 25%  recurring，首年有效 |
| **最低 payout** | $30 |
| **Cookie 时长** | 30 天 |
| **追踪** | Rewardful |
| **联系** | affiliate@topview.ai |

### 5.3 多语种与 URL（hreflang）

| 语言 | 代码 | URL | 状态 |
|------|------|-----|------|
| **English** | en | https://www.topview.ai | 200 |
| **Español** | es | https://www.topview.ai/es | 200 |
| **Français** | fr | https://www.topview.ai/fr | 200 |
| **Português** | pt | https://www.topview.ai/pt | 200 |
| **Italiano** | it | https://www.topview.ai/it | 200 |
| **日本語** | ja | https://www.topview.ai/ja | 200 |
| **ภาษาไทย** | th | https://www.topview.ai/th | 200 |
| **Polski** | pl | https://www.topview.ai/pl | 200 |
| **한국어** | ko | https://www.topview.ai/ko | 200 |
| **Deutsch** | de | https://www.topview.ai/de | 200 |
| **Русский** | ru | https://www.topview.ai/ru | 200 |
| **Dansk** | da | https://www.topview.ai/da | 200 |
| **العربية** | ar | https://www.topview.ai/ar | 200 |
| **Norsk** | nb | https://www.topview.ai/nb | 200 |
| **Nederlands** | nl | https://www.topview.ai/nl | 200 |
| **Indonesian** | id | https://www.topview.ai/id | 200 |
| **繁體中文** | zh-Hant-TW | https://www.topview.ai/tw | 200 |
| **简体中文** | zh-CN | https://www.topview.ai/zh | 200 |
| **Türkçe** | tr | https://www.topview.ai/tr | 200 |
| **x-default** | 默认 | https://www.topview.ai | 200 |

**共 20 种语言/地区**（含 x-default）

---

## 6. Keywords

| Type | Examples |
|------|----------|
| **Primary** | AI video agent, AI video generator, AI marketing video, AI UGC video |
| **Secondary** | AI product video, product video AI, URL to video, AI avatar video |
| **Long-tail** | AI video agent for marketing, AI UGC video generator, clone video style AI |
| **Use case** | AI video for affiliate marketing, AI product video for ecommerce |
| **竞品** | Heygen alternative, Tavus alternative, Synthesia alternative, Pictory alternative, Topview vs HeyGen |
| **扩展** | AI avatar generator, AI lip sync, viral video AI |
| **大模型截流** | Veo AI video, Sora AI video, Kling AI video, Runway Gen-3, AI video models all in one | /models |
| **API** | AI video API, URL to video API, video avatar API | /openapi |
| **Affiliate** | Topview affiliate, AI video affiliate program | /affiliate-program |
| **Target intent** | Commercial（工具选型）、Transactional（注册/试用） |

*完整映射见 [topview-keywords.md](./topview-keywords.md)；功能页详情见 [topview-features.md](./topview-features.md)；Use Cases 见 [topview-use-cases.md](./topview-use-cases.md)；Solutions 见 [topview-solutions.md](./topview-solutions.md)*

---

## 7. Competitors

- **Direct**: Pictory AI、Tagshop AI、Synthesia、HeyGen、Runway
- **Alternatives**: 传统视频制作、手动剪辑、外包 agency
- **Differentiation**: Topview 以 AI Video Agent 为核心——理解创意意图、自动完成全流程；支持参考视频克隆风格；产品 URL 直接生成视频；80–100+ AI Avatar
- **Gaps to exploit**: 病毒式 UGC 风格、产品视频、联盟营销场景、成本优势

*详细分析见 [topview-competitors.md](./topview-competitors.md)。竞品核心关键词、功能、使用场景见 Section 6；关键词重叠与机会见 [topview-keywords.md](./topview-keywords.md) Section 5.1。*

---

## 8. Brand & Voice

- **Voice**: 高效、专业、自信、面向营销人
- **Tone**: 强调「10x」「fraction of cost」「zero learning curve」
- **Avoid**: 过度技术化、冷冰冰的 AI 术语
- **Preferred terms**: "AI Video Agent"、"viral"、"UGC"、"marketing ads"

---

## 9. Product Documentation

- **Path or link**: 官网、Learning center、[API 文档](https://www.topview.ai/openapi)（Materials to Video、URL to Video、Video Avatar、Product Avatar、Product Anyshoot）
- **Key features**:
  - **AI Video Agent**：Guided Mode（对话式）、Instant Mode（提示词即出片）
  - **Clone video style**：上传产品 + 参考视频 → AI 复刻风格
  - **AI Ads**：AI Ads Video、AI Product Video、AI UGC Video、URL to Video
  - **AI Avatar**：80–100+ 头像、Product Avatar、Design My Avatar、AI Lip-sync
  - **AI Video**：AI Video Generator、AI Short Video
  - **Topview Board**：多 AI 视频大模型（Veo、Sora、Kling、Seedance、Hailuo、Wan、Vidu、Runway、Nano Banana）统一画布；实时协作
  - **Ad library**：学习 5M+ 病毒视频
  - **多语言**：20+ 语言、OpenAI/ElevenLabs 配音

---

## 10. Other Context

- **Strategy**: 专注营销视频场景；Freemium 获客；API 开放
- **Timeline**: 持续扩展教育、内容创作、企业用例
- **Constraints**: 定价以官网为准；Credit 消耗需透明说明

---

## 11. Content / Blog / Article Strategy

**Product connection**:
- 文章围绕 AI 视频、营销视频、UGC、产品视频
- 自然提及 Topview 作为 AI Video Agent 解决方案
- 避免纯通用内容、无产品关联

**Keyword basis**: 使用 Section 6 及 [topview-keywords.md](./topview-keywords.md) 作为文章主题与目标词；大模型截流词（Veo、Sora、Kling 等）见 [topview-models.md](./topview-models.md)

---

## 12. Use Cases

**严格区分**：Use Cases = **谁**在**什么情境**下用；Features = 产品**能做什么**。

| 类型 | 维度 | 页面 | URL | 目标关键词 |
|------|------|------|-----|------------|
| **Use Cases** | Persona | For affiliate marketers | /use-cases/for-affiliate-marketers | AI video for affiliate marketing |
| **Use Cases** | Persona | For DTC brands | /use-cases/for-dtc-brands | AI marketing video for DTC |
| **Use Cases** | Persona | For e-commerce | /use-cases/for-ecommerce | AI product video for ecommerce |
| **Use Cases** | Persona | For agencies | /use-cases/for-agencies | AI video agent for agencies |
| **Use Cases** | Persona | For solopreneurs | /use-cases/for-solopreneurs | AI video for solopreneurs |
| **Use Cases** | Campaign goal | Advertising | /use-cases/advertising | AI video for advertising |
| **Use Cases** | Campaign goal | Product launch | /use-cases/product-launch | AI video for product launch |
| **Use Cases** | Campaign goal | Seasonal promotion | /use-cases/seasonal-promotion | AI video for Black Friday |
| **Use Cases** | Campaign goal | Replicating viral ads | /use-cases/replicating-viral-ads | replicate viral ad style |
| **Use Cases** | Campaign goal | A/B testing | /use-cases/ab-testing-creatives | AI video for A/B testing |
| **Use Cases** | 业务阶段 | Scaling creatives | /use-cases/scaling-creatives | scale video production AI |
| **Features** | — | AI Video Agent、clone、URL to video 等 | /、功能页 | AI video agent, AI product video |

*完整内容见 [topview-use-cases.md](./topview-use-cases.md)*

---

## Quick Reference

| Section | Used by |
|---------|---------|
| 0 | 文档语言策略（中英分工、实施规则） |
| 1-4 | 所有 skills：SEO、页面、组件、渠道 |
| 5 | 技术 SEO、sitemap、目录提交、API、Affiliate、多语种 |
| 6 | On-page SEO、metadata、关键词研究 |
| 7 | 竞争定位、内容策略 |
| 8 | 文案、语气、testimonials、CTA |
| 9-10 | 功能、内容策略 |
| topview-features.md | 功能页详情、价值评估 |
| topview-use-cases.md | Use Cases 页面、persona 规划 |
| topview-solutions.md | Solutions 行业解决方案、Outcome 页 |
| topview-competitors.md | 竞品分析 |
| topview-keywords.md | 关键词映射 |
| topview-models.md | AI 视频大模型、Board、大模型 SEO 截流 |

**文档间关联**：Features → Use Cases、Solutions、Models；Use Cases → Features、Solutions；Solutions → Features、Use Cases；Competitors → Features、Use Cases、Keywords；Keywords → 各文档；Models → Features、Keywords。
