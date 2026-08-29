# Project Context

> 项目上下文文档，供 AI Agent 与营销技能使用。基于 [marketing-skills/project-context](https://github.com/kostja94/marketing-skills/blob/main/templates/project-context.md) 模板，结合 Nova Scientia 实际结构填写。

**Last updated**: 2026-08-29 — 保持更新；过时上下文会降低输出质量。

---

## Document System

| Document | Role |
|----------|------|
| **project-context.md** (this file) | 产品概览、定位、ICP、品牌、关键词、竞品 |
| [page-types.md](page-types.md) | **页面类型与职责**（`/topic`、`/{slug}`、`/products`、`/{segment}` 分类 hub 等严格区分） |
| [reference.md](reference.md) | 内容、SEO、视觉、本地化规范 |
| [brand.md](brand.md) | 品牌视觉全规范（颜色/字体/布局/按钮/链接/Logo/动效/暗色模式/禁止事项） |
| [task-tracker.md](../operations/task-tracker.md) | 营销与 SEO 任务追踪 |
| [README.md](../README.md) | 全量资产地图（入口） |

---

## Language Strategy

| Context | Language | Notes |
|---------|----------|-------|
| **Website content** | pt-BR | 全站葡语，巴西受众 |
| **Documents / reports** | zh-CN | 内部规范、任务、分析 — 中文 |
| **Product copy** | pt-BR | 定位、slogan、关键信息 |
| **Technical / SEO** | pt-BR | URLs、keywords、平台名 — 与网站一致 |

**Rule**: 产品名、功能名、URL、关键词使用网站语言；策略、任务、洞察使用文档语言。

---

## Project Overview

| Field | Content |
|-------|---------|
| **Industry** | AI tools portal, content media, product discovery |
| **Website** | https://novascientia.com.br |
| **Stage** | Growth |
| **Core product** | Portal de Inteligência Artificial para o Brasil — 发现、评测、对比 AI 工具与产品 |
| **Slogan** | Portal de IA para o Brasil |
| **Metrics** | 435 ferramentas, 35 temas, 35 empresas avaliadas |
| **Company** | Nova Scientia |

**Product form**:
- **Platforms**: Web only
- **Entry points**: Explorar Produtos, Temas（首页 CTA）
- **Data scale**: `content/products/*.json`（435）、`content/topics/*.md`（35 主题指南）、`content/companies/*.json`（35）

---

## 1. Product Overview

**One-line description**:
```
Portal de IA para o Brasil que ajuda usuários a descobrir, comparar e escolher as melhores ferramentas e produtos de inteligência artificial através de análises detalhadas e guias práticos.
```

**Category**: AI tools directory, product reviews, comparison guides  
**Business model**: Content media, affiliate / referral（潜在）  
**Pricing**: Free content

**Core product lines**:

| Product / Feature | Description |
|-------------------|-------------|
| **Produtos** | 产品评测页，单产品深度分析（features、pricing、pros/cons、alternatives、FAQ） |
| **Temas / guias** | 主题详情 `/{slug}`（如 LLM、生图），总聚合 `/topic`；分类 hub 短路径 `/{segment}`（如 `/image`） |

**Differentiation**:
- 专注巴西市场，全站 pt-BR
- 双轨内容：Produtos（单产品评测）+ Temas（主题指南与目录聚合）
- 结构化数据驱动：JSON（products、topics、companies）

---

## 2. Positioning Statement

> **For** profissionais e empresas brasileiras **who** precisam escolher ferramentas de IA para trabalho e projetos, **our** Nova Scientia **is a** portal de curadoria **that** oferece análises detalhadas, comparações e guias práticos em português. **Unlike** sites genéricos em inglês, **we** focamos exclusivamente no mercado brasileiro **because** conteúdo localizado, termos pt-BR e recomendações adaptadas ao contexto local.

---

## 3. Value Proposition & Key Messages

- **Primary value prop**: Encontre as melhores ferramentas de IA com análises em português e recomendações curadas para o Brasil.
- **Key messages**:
  - Descubra ferramentas de IA por categoria
  - Análises completas com preços, prós e contras
  - Guias práticos para escolher a solução ideal
  - Conteúdo atualizado e curado
- **Proof points**: 435+ ferramentas avaliadas, conteúdo curado em pt-BR

---

## 4. Target Audience / ICP

**Primary ICP**:
- **Who**: Profissionais, desenvolvedores, designers, criadores de conteúdo no Brasil
- **Industry**: Tech, creative, startups, SMBs
- **Jobs to be done**: 发现、比较、选择适合的 AI 工具
- **Pain points**: 英文内容难懂、信息分散、缺乏本地化推荐
- **Buying triggers**: 新项目启动、工具升级、预算评估

**Secondary ICP**: 企业决策者、教育机构

**Language / locale**: pt-BR

---

## 5. Existing Website

- **URL**: https://novascientia.com.br
- **Tech stack**: Next.js 15, React 18, Tailwind CSS, Radix UI
- **Current state**: Iterating（内容优化、pt-BR 翻译进行中）
- **Product entry points**: Web only

**Navigation structure**:
- **Main nav**: Produtos, Temas（主题下拉 + `/topic`）, Empresas
- **Footer**: Produtos, Início, Empresas, Mapa do site

**URL hierarchy**:

| Path pattern | Example | Purpose |
|--------------|---------|---------|
| / | Homepage | Hero, CTA, featured product |
| /products | Produtos index | 产品列表 |
| /products/categoria/[cat] | …/image 等 | **301 重定向**至短 hub（`/image` 等），非活跃路由 |
| /products/[slug] | /products/cursor | 产品详情 |
| /topic | Temas index | 主题/指南总聚合 |
| /[slug] | /llm | 主题指南详情（content/topics） |
| /sitemap.xml | Sitemap | 动态生成 |

**Subdomains**: 无

---

## 6. Keywords

| Type | Examples |
|------|----------|
| **Primary** | ferramentas de IA, produtos de IA, gerador de imagem, IA para |
| **Secondary** | melhores ferramentas IA 2026, comparação, análise |
| **Long-tail** | como escolher gerador de imagem, Cursor vs Copilot |
| **Competitor / brand** | [produto] alternativa, [produto] vs [produto] |
| **Target intent** | Informational, Commercial |

**Programmatic SEO**: 主题页 `/{slug}`（Temas）与产品目录 `/products`、分类 hub `/{segment}` 覆盖主要意图与长尾。

---

## 7. Competitors

- **Direct**: 其他 AI 工具目录、评测站（多为英文）
- **Alternatives**: Google 搜索、Reddit、YouTube 评测
- **Differentiation**: 专注 pt-BR、Produtos + Temas（主题指南）、结构化内容
- **Gaps to exploit**: 巴西市场本地化内容稀缺
- **Comparison pages**: 产品页内 alternatives；主题页内对比表（若有）

---

## 8. Brand & Voice

- **Voice**: Profissional, útil, direto
- **Tone**: Confiante mas não arrogante, conciso, acolhedor
- **Avoid**: Buzzwords 过度、英文术语（优先 IA 而非 AI）
- **Preferred terms**: ferramentas（非 tools 在正文）, produto（产品）, análise（评测）

---

## 9. Product Documentation

- **知识库入口**：[knowledge/topics/README.md](../knowledge/topics/README.md)
- **规范参考**：见 [reference.md](reference.md)

---

## 10. Other Context

- **Strategy**: 内容优化（Meta、字数、pt-BR 翻译）、SEO、GEO
- **Timeline**: 持续迭代，见 [task-tracker.md](../operations/task-tracker.md)
- **Constraints**: 仅葡语；禁止硬编码颜色/字号；提交需用户明确指令

---

## 11. Content / Blog / Article Strategy

**Optimization foundation**: Product + Keywords + Article intent + Competitor articles

**Article orientations**:
- **SEO-driven**: 主题指南、产品评测 — 目标关键词，优化搜索
- **Evergreen vs timely**: 以 evergreen 为主（70–75%）；年份（2026）用于时效性

**Product connection**:
- **How articles support product**: 教育用户选择工具；自然引入产品推荐；CTA 到产品页
- **Natural product mentions**: CTA 在结论、工具卡片、alternatives
- **Avoid**: 纯通用内容无产品关联

**Keyword basis**: Section 6；见 [reference.md](reference.md)

---

## 12. Features vs Use Cases vs Solutions

| Type | Focus | Example page |
|------|-------|--------------|
| **Produtos** | 单产品能力、定价、评测 | /products/cursor |
| **Ferramentas** | 类别内工具对比、选择建议 | /image-generator |
| **Solutions** | 暂未独立；可扩展 /solutions/for-[industry] | — |

---

## 13. Optimization Priorities

| Priority | SEO | GEO (AI search) | Content |
|----------|-----|-----------------|---------|
| **P0** | Meta 50–60/150–160 字符，sitemap | FAQ 结构化 | Products hero/description；Topics Meta/pt-BR |
| **P1** | Title/meta 每页类型 | Q&A 格式 | 对比页、alternatives |
| **P2** | Internal links, schema | — | Long-tail articles |

---

## 14. Visual Identity

**详细规范**：[brand.md](brand.md) | [reference.md](reference.md) 第三节

**Colors**: primary、foreground、muted-foreground、background、surface、border  
**Typography**: Inter, JetBrains Mono；12–60px 字号层级  
**Spacing**: container-professional (max-w 1200px), section-spacing  
**Layout**: Header fixed（`--header-height` 64px）、BreadcrumbNav（`--breadcrumb-height` 32px）、main#main-content、Footer — 见 [brand.md](brand.md) §5

---

## 15. Technical Architecture (from src/)

**Data sources**:
- `content/products/*.json` → `getAllProducts`, `getProductBySlug`（JSON，直接编辑）
- `content/companies/*.json` → `getAllCompanies`, `getCompanyBySlug`（JSON，直接编辑）
- `content/topics/*.md` → `getAllTopics`, `getTopicBySlug`（MD，经 `topic-md.ts` 解析）
- `content/locales/{locale}/` → 多语言覆盖层（见 `content-dir.ts`）
- 路由：`app/[locale]/` + `middleware.ts`（5 locale，pt-BR 无前缀）

**Key components**:
- `Header` / `HeaderWithNav` — Produtos、Temas、Empresas 下拉
- `Footer` — FOOTER_PRODUCTS_LINKS, FOOTER_SITE_LINKS（navigation-config.ts）
- `BreadcrumbNav` — 面包屑
- `ProductLayout` — 产品详情布局
- `TopicPage` — 主题指南详情
- `HeroSection` — 首页 Hero、CTA、featured product

**Types**:
- `Product` / `ApiProduct` — slug, name, content.hero, sections…
- `ApiTopic` — slug, content, featured products…（见 `src/types/topics.ts`）

---

## Quick Reference

| Section | Used by |
|---------|---------|
| Overview, 1–4 | All skills: SEO, pages, components |
| 5 | Technical SEO, sitemap, crawlability |
| 6 | On-page SEO, metadata, keyword research |
| 7 | Competitive positioning |
| 8 | Copy, tone, CTAs |
| 9–10 | Features, content strategy |
| 11 | Article creation |
| 12 | Page taxonomy |
| 13 | Prioritization |
| 14 | Logo, brand visual |
| 15 | Implementation reference |

**相关**：操作规范见 [reference.md](reference.md)；任务进度见 [task-tracker.md](../operations/task-tracker.md)。
