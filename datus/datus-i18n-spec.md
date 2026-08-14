# Datus — 主站 i18n（`/zh`）规范

> **本文档职责**：datus.ai 主站中英双语的范围规则、URL/路由、内容分层、机翻→精调流程、术语锁定、SEO 与验收。  
> **引用**：[datus.md](./datus.md) 概览 | [datus-site-structure.md](./datus-site-structure.md) 站点结构 | [datus-positioning.md](./datus-positioning.md) 定位与中文 One Story  
> **技术栈假定**：Next.js App Router + [next-intl](https://next-intl.dev/docs/routing/configuration)（若官网非 Next，则映射等价 i18n，**公开 URL 约定不变**）

**最近更新**：2026-08-04（脱敏；对齐 Google hreflang / next-intl 最佳实践）

---

## 1. 目标与非目标

### 1.1 目标

在 [datus.ai](https://datus.ai/) 为**所有非 Blog 营销路径**提供中文镜像：

| 规则 | 说明 |
|------|------|
| **纳入** | 除 `/blog/**` 外的全部营销/产品/落地路径（现网 + 后续新增） |
| **排除** | `/blog/**`、docs.datus.ai、studio.datus.ai |
| **路径** | 中文 = `/zh` + 英文 path；**slug 不翻译** |
| **默认行为** | 新上线营销页默认同步出 `/zh` 镜像 |

本规范**不维护页面白名单**，不枚举「要做哪些页面」。覆盖检查以现网 sitemap / 路由表为准。

### 1.2 非目标

| 不做 | 原因 |
|------|------|
| Blog 中文（无 `/zh/blog`） | 范围外 |
| docs.datus.ai 任何改动或规划扩展 | 范围外（docs 自有 i18n，本规范不管） |
| 中文专用 slug | 避免双套 URL；营销站以稳定性优先 |
| 浏览器 / Cookie 自动语言跳转 | SEO：每个 locale URL 须可被爬虫直接访问，不依赖协商跳转 |
| Studio App 多语言 | 产品面独立 |

**代码落地**在 datus.ai 官网代码仓；本 clients 仓只存策略规范。本仓无官网源码。

---

## 2. URL 与 hreflang 约定

### 2.1 路由规则

```
/{path}      ↔  /zh/{path}     // path 不属于 blog
/blog/...    →  仅英文，不提供 /zh/blog
```

- 默认语言 **en**：无前缀（`localePrefix: 'as-needed'`）
- 中文 **zh**：前缀 `/zh`（URL 段用短码；见 §2.2 的 hreflang 码）
- 禁止公开 `/en/*`；若出现则 **301** 去前缀到对应英文 path（next-intl as-needed 默认行为）
- `x-default` → **该 path 的英文 URL**（全球默认语言为 EN）

符合 [Google 多语言页面指南](https://developers.google.com/search/docs/specialty/international/localized-versions)：目录前缀是合法实现方式之一；部分页面只有单一语言（Blog）也允许。

### 2.2 元数据（仅「有 ZH 镜像」的营销页）

```ts
// path 形如 "/pricing" 或 ""（首页）
const enUrl = path ? `https://datus.ai${path}` : 'https://datus.ai/';
const zhUrl = path ? `https://datus.ai/zh${path}` : 'https://datus.ai/zh/';

alternates: {
  canonical: isZh ? zhUrl : enUrl, // 各语言 canonical 指向自身，禁止跨语言 canonical
  languages: {
    en: enUrl,
    'zh-Hans': zhUrl, // 简体中文用 ISO 15924；勿只用模糊的 zh（可选 zh-CN，全站择一）
    'x-default': enUrl,
  },
}
openGraph: {
  locale: isZh ? 'zh_CN' : 'en_US',
  alternateLocale: isZh ? 'en_US' : 'zh_CN',
}
```

| 约定 | 说明 |
|------|------|
| **互指** | EN 与 ZH 必须双向声明对方 + 自身（Google：缺 return link 可能被忽略） |
| **绝对 URL** | hreflang / canonical 一律 `https://…` 完整 URL |
| **Blog** | 仅 EN：`alternates.languages` **不要**声明 `zh-Hans` |
| **html lang** | `<html lang="en">` / `<html lang="zh-CN">`（或 `zh-Hans`），与页面一致 |
| **trailing slash** | 与现网一致；hreflang、canonical、sitemap 三者写法必须一致 |

首页：EN=`https://datus.ai/`，ZH=`https://datus.ai/zh/`（或无尾斜杠，全站统一）。

### 2.3 技术分层（与框架无关的约定）

| 层 | 约定 |
|----|------|
| 路由 | `app/[locale]/...`（或等价）；EN 无前缀，ZH=`/zh` |
| 配置 | `i18n/routing.ts`、`i18n/request.ts`、`middleware` |
| UI 文案 | `messages/en.json` + `messages/zh.json` |
| 页面正文 | 按 locale 的 content / MDX / CMS |
| SEO | 页面 metadata `alternates`（首选）或 sitemap `xhtml:link`；**三选一为主即可**，避免三套互相打架 |
| 导航 | 使用 next-intl 的 `Link` / `usePathname` / `useRouter`，勿用裸 `next/link` 漏掉前缀 |
| 语言切换 | 同 path 换前缀；**保留 query string** |

---

## 3. 技术架构

### 3.1 核心路由配置

```ts
// i18n/routing.ts
import { defineRouting } from 'next-intl/routing';
import { createNavigation } from 'next-intl/navigation';

export const routing = defineRouting({
  locales: ['en', 'zh'],
  defaultLocale: 'en',
  localePrefix: 'as-needed', // 或 { mode: 'as-needed', prefixes: { zh: '/zh' } }
  localeDetection: false,    // 必关：仅靠 URL 定语言，避免 Accept-Language / Cookie 把 / → /zh
  localeCookie: false,       // 建议关：与「不自动跳转」一致，减少 as-needed 下隐式重定向
  // 部分路径仅 EN（如 blog）时，关闭中间件自动 alternateLinks，改由页面 metadata 声明
  alternateLinks: false,
});

export const { Link, redirect, usePathname, useRouter } = createNavigation(routing);
```

**为何这样配（对照 [next-intl routing](https://next-intl.dev/docs/routing/configuration)）**：

| 项 | 原因 |
|----|------|
| `as-needed` | 保持现有英文 URL 不被 `/en` 污染，利于存量 SEO |
| `localeDetection: false` | as-needed 开启检测时，Cookie 可能把无前缀路径重定向到上次语言（如 `/`→`/zh`），伤害爬虫与分享链接 |
| `alternateLinks: false` | 默认 Link 头会按「全 locale × 全路径」生成；Blog 等仅 EN 的页面不能出现虚假 `zh-Hans` 交替链接 |
| 页面级 `generateMetadata` | 只对有镜像的营销页输出完整 hreflang 簇 |

### 3.2 建议文件树（官网仓）

```
i18n/
  routing.ts
  request.ts
messages/
  en.json
  zh.json
middleware.ts                 # next-intl；/en 301；blog 仅 EN
app/
  [locale]/
    layout.tsx                # <html lang={…}>
    page.tsx
    ...
content/                      # 或现有 CMS/MDX 等价结构
  marketing/
    en/
    zh/
```

`/blog/**` 可放在 `[locale]` 外，或放在内但只渲染 `en`、不生成 `/zh/blog`。

### 3.3 Middleware 要点

1. 委托 next-intl middleware 做 locale 解析与内部 rewrite  
2. 确保 matcher **匹配无前缀路径**（as-needed 要求）  
3. `/en`、`/en/*` → 301 去前缀  
4. 不按 `Accept-Language` / Cookie 自动跳转  
5. matcher 排除 `api`、`_next`、静态资源、sitemap 等  

### 3.4 非 Next 框架

仍采用同一 URL/内容分层（UI messages + 按 locale 内容 + hreflang）。框架层换成该栈官方 i18n（如 Astro `i18n.routing`），**不得改变** §2 的公开 URL 约定。

---

## 4. 内容分层与翻译工作流

### 4.1 两层文案

| 层 | 存放 | 示例 |
|----|------|------|
| **UI** | `messages/{locale}.json` | 导航、按钮、页脚、空态、通用标签 |
| **页面正文** | `content/.../{locale}/...` 或等价 | 各营销页 hero、段落、FAQ 文案、卡片 |

组件用 `useTranslations` / `getTranslations`；禁止在组件内硬编码中英分支长文（短标签最终也应进 messages）。

### 4.2 机翻 → AI 精调

1. **抽取**：现网营销页 → UI messages + 页面级 EN content  
2. **机翻**：批量生成 ZH；覆盖检查用 sitemap / 路由表，**不在本规范写死页面列表**  
3. **术语锁定**：精调前对照 §5，禁止同词多译  
4. **AI 精调**：语气、CTA、技术准确性；代码块 / CLI / 产品名保留  
5. **门禁**：`/zh` 页内链优先留在 `/zh/*`；链 `/blog/...` 保持英文 URL；不改 docs  
6. **验收**：抽查 hreflang 互指、`html lang`、语言切换（含 query）、缺译回退  

### 4.3 翻译状态（可选机制）

可按 path 维护状态：`MT` | `AI-tuned` | `Live`。状态表可另存或脚本生成，**不是本规范正文的固定页面清单**。

### 4.4 保留不译 / 半译

| 类型 | 处理 |
|------|------|
| 产品名 Datus、Datus CLI / Studio / Enterprise | 不译 |
| CLI 命令、代码、包名（`datus-agent`、`pip install`） | 不译 |
| 专有名词 Snowflake、dbt、MCP 等 | 不译；首次可括注 |
| Agent / Subagent | 见 §5（可保留英文或固定译法，全站一致） |

---

## 5. 必锁中英术语表

对齐 [datus-positioning.md](./datus-positioning.md) 中文 One Story 与品类表述。精调与机翻后审校必须遵守；新增营销文案不得另造译法。

### 5.1 品牌与品类

| English | 中文（锁定） | 备注 |
|---------|--------------|------|
| Datus | Datus | 不译 |
| data engineering agent | 数据工程 Agent | 品类主译；可与「数据工程智能体」并存时以「数据工程 Agent」为准 |
| open-source | 开源 | — |
| evolvable context | 可演进的上下文 | One Story 用语 |
| one-man data team / one-person data team | 一人数据团队 | — |
| enterprise agent teams | 企业 Agent 团队 | — |
| modern data stack | modern data stack | 可保留英文；若译用「现代数据栈」，全站统一 |

### 5.2 产品与能力

| English | 中文（锁定） | 备注 |
|---------|--------------|------|
| Context Engine / Data Context Engine | 上下文引擎 / 数据上下文引擎 | 产品核心；勿译成「情境引擎」 |
| context | 上下文 | 数据语境下不用「情境」 |
| Subagent | Subagent / 子代理 | 选定一种后全站统一；推荐正文「子代理」，标题可保留 Subagent |
| Semantic Layer | 语义层 | — |
| semantic model | 语义模型 | — |
| metrics | 指标 | — |
| Reference SQL | Reference SQL / 参考 SQL | 产品概念可保留英文 |
| NL2SQL / text-to-SQL | NL2SQL / 自然语言转 SQL | — |
| lineage | 血缘 | — |
| data quality | 数据质量 | — |
| governance | 治理 | — |
| long-running agents | 长时运行 Agent | — |
| warehouse | 数仓 / 数据仓库 | 上下文清晰时可用「数仓」 |
| catalog | 目录 / 数据目录 | — |
| MCP (Model Context Protocol) | MCP | 不译全称到标题 |

### 5.3 产品形态与 CTA（常用）

| English | 中文（锁定） |
|---------|--------------|
| Get started | 开始使用 |
| Pricing | 定价 |
| Integrations | 集成 |
| Documentation | 文档 |
| Community | 社区 |
| Enterprise | 企业版 |
| Open Source | 开源 |
| Cloud Personal | 云端个人版 |
| Contact us | 联系我们 |

### 5.4 One Story 锚点句（首页等可直接复用）

> Datus 是一个开源的数据工程 Agent，为你的数据系统构建可演进的上下文。  
> 从一人数据团队到企业 Agent 团队——Datus 把数据工作变成可靠、可复用的 Agent 系统。

来源：[datus-positioning.md](./datus-positioning.md) §一中文版。

---

## 6. SEO、Sitemap 与内链

### 6.1 Sitemap

- 非 blog 的 sitemap：每个纳入范围的 EN path **增加**对应 `/zh/{path}`  
- **推荐**：在 sitemap 用 `xhtml:link` 声明 `en` / `zh-Hans` / `x-default` 互指（[Google 支持](https://developers.google.com/search/docs/specialty/international/localized-versions)）；若已用 HTML `alternates` 且维护成本高，可只保留一种主通道  
- **不改** blog sitemap（不增加 `/zh/blog/...`，也不给 blog URL 加虚假中文 alternate）

### 6.2 内链

| 场景 | 规则 |
|------|------|
| `/zh` 营销页 → 其他营销页 | 优先 `/zh/{path}` |
| `/zh` 营销页 → Blog | 保持 `/blog/{slug}`（英文） |
| EN 营销页 | 不链到 `/zh`（语言切换除外） |
| Docs / Studio 外链 | 保持现状；本规范不做 docs locale 特判 |

### 6.3 语言切换

- 营销页：同一 path 在 EN ↔ `/zh` 之间切换，**保留 `?query`**  
- 用户在 `/blog/*`：可隐藏切换，或切换到对应语言首页（`/` ↔ `/zh/`）  
- Docs 链接：行为保持现状（不做 locale 特判）  
- 勿用 JS 强制按浏览器语言整站跳转（可用非阻断提示条，可选）

### 6.4 结构化数据

面包屑 / FAQ JSON-LD 的 `item` URL 须带正确 locale 前缀（仅营销页）。细则见 [datus-breadcrumb-spec.md](./datus-breadcrumb-spec.md)、[datus-faq-spec.md](./datus-faq-spec.md)；双语时标签语言与页面 locale 一致。

---

## 7. 工程落地清单（官网仓）

1. 安装 `next-intl`；添加 `i18n/routing.ts`、`i18n/request.ts`；`next.config` 挂 plugin  
2. 配置：`as-needed` + `localeDetection: false` +（建议）`localeCookie: false` + `alternateLinks: false`  
3. 营销路由迁入 `app/[locale]/...`；layout 设置 `html lang`；middleware matcher 含无前缀路径  
4. 硬编码文案 → `messages/{locale}.json`；页面正文按 locale 加载  
5. Header 语言切换（保留 query）；Docs/Blog 链接保持现状  
6. 有镜像的营销页：`generateMetadata` 配 self-canonical + `en` / `zh-Hans` / `x-default`  
7. 非 blog sitemap 增加 `/zh`；可选 sitemap xhtml hreflang；不改 blog sitemap  
8. 面包屑 / FAQ JSON-LD URL 带正确 locale  

---

## 8. 验收清单

- [ ] `/{path}` 与 `/zh/{path}` 均可**直接**访问（无依赖语言协商跳转；path ∉ blog）  
- [ ] 不存在可索引的 `/zh/blog/**`  
- [ ] Blog 页未声明虚假 `zh-Hans` hreflang  
- [ ] `/en`、`/en/*` 301 去前缀  
- [ ] 营销页 hreflang **双向互指** + self + `x-default`→EN；码用 `zh-Hans`（或全站统一的 `zh-CN`）  
- [ ] 各语言 `canonical` 指向自身；绝对 URL；与 sitemap / trailing slash 一致  
- [ ] `<html lang>` 与页面语言一致  
- [ ] 语言切换同 path 换前缀且保留 query  
- [ ] UI 与正文无硬编码漏网英文（抽查）  
- [ ] 术语符合 §5  
- [ ] 非 blog sitemap 含 `/zh` 镜像；未混入 blog 中文  

---

## 9. 与公开最佳实践的对照结论

| 主题 | 结论 | 本规范落点 |
|------|------|------------|
| URL 用目录前缀 `/zh` | Google 认可的实现方式 | §2.1 |
| 默认语无前缀 `as-needed` | next-intl 正式支持；利于存量 EN URL | §3.1 |
| 关闭自动语言跳转 | 爬虫不依赖 Accept-Language；避免 Cookie 劫持无前缀路径 | §3.1 |
| hreflang 互指 + 绝对 URL + x-default | Google 硬性要求 | §2.2 |
| 简体用 `zh-Hans` | Google 文档对中文脚本的推荐写法 | §2.2（相对仅写 `zh` 的收紧） |
| 部分页面仅单语 | Google 允许；勿编造缺失语言的 alternate | §2.2 Blog、`alternateLinks: false` |
| canonical 不跨语言 | 常见 SEO 错误；各语种指向自身 | §2.2 |
| hreflang 实现通道 | HTML / Header / Sitemap 等效，选一为主 | §6.1 |
| 翻译 slug | 可选增强；营销站非必须 | 明确不做（§1.2） |

**整体判定**：原方案方向正确；本版在脱敏同时补上了 `zh-Hans`、关闭 Cookie/检测、关闭全局 `alternateLinks`、Blog 不造假 hreflang、`html lang`、query 保留、sitemap 与 canonical 一致性等关键点。

---

## 10. 文档关系

| 文档 | 关系 |
|------|------|
| [datus-site-structure.md](./datus-site-structure.md) | 主站 IA；中文站条目指向本文 |
| [datus-positioning.md](./datus-positioning.md) | 中文 One Story 与术语源头 |
| [datus-breadcrumb-spec.md](./datus-breadcrumb-spec.md) / [datus-faq-spec.md](./datus-faq-spec.md) | 结构化数据在双语下的 URL/标签规则补充点 |

---

*i18n 规范 · Datus · 范围：datus.ai 非 Blog 营销 `/zh` · 2026-08-04*
