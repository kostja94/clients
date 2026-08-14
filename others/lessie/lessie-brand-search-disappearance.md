# Lessie AI 品牌词搜索消失问题：React + Next.js 分析与应对

> **现象**：改前端代码后，搜索「lessie ai」时 Lessie 不出现在搜索结果中；搜索「lessie」正常。其他功能词、内容词正常。已发生两次，上次回退代码后恢复。  
> **技术栈**：React + Next.js  
> **Standalone 文档**：本问题为独立情况，不依赖其他文档。

---

## 一、现象与特征

| 特征 | 说明 |
|------|------|
| **正常** | 搜索「lessie」时，lessie.ai 正常出现 |
| **正常** | 搜索功能词如「ai coach finder」时，对应页面（如 lessie.ai/coach-finder）正常出现 |
| **异常** | 搜索「lessie ai」时，lessie.ai 不出现 |
| **未受影响** | 功能关键词、内容关键词、profile.lessie.ai、lists.lessie.ai 等页面正常 |
| **触发** | 前端代码改动后出现 |
| **恢复** | 上次回退代码后恢复正常 |
| **复现** | 本次改动后再次出现相同情况 |

**关键推断**：品牌词主要对应 **lessie.ai 首页**。子域 profile.lessie.ai、lists.lessie.ai 及内页（如 /coach-finder 可被「ai coach finder」搜到）正常，说明问题集中在 **主站首页或根 layout**。  
**差异点**：「lessie」能搜到、「lessie ai」不能，功能词（如「ai coach finder」）对应内页正常，说明问题与**首页对完整品牌名「Lessie AI」的呈现方式**有关，而非整站或内页索引问题。

---

## 一（补充）、项目背景与历史

### 上次原因（已明确）

**根因**：代码报错，Next.js 兜底机制生效，将渲染方式从 **SSR（服务端渲染）降级为 CSR（客户端渲染）**。  
**后果**：爬虫拿到的首包 HTML 无内容，品牌词无法被索引。  
**恢复**：回退代码后恢复正常。

### 本次背景（2025 年 2 月 monorepo 迁移）

| 项目 | 说明 |
|------|------|
| **之前** | 三个域名（lessie.ai、profile.lessie.ai、lists.lessie.ai）对应三个独立 Next 项目，公共部件需维护三份 |
| **之后** | 整合为单一 Next.js monorepo，一套公共基建（样式、多语言、网络、公共组件） |
| **上线** | 2025-02-27 新项目发布，替代原有三个独立项目 |
| **2.27 至今** | 主要为上页面、调整组件样式 |

### 本次原因（待定位）

与上次不同，本次尚未定位到具体根因。可能方向包括：monorepo 配置、metadata 结构、多语言 hreflang、或某处静默错误再次触发 SSR→CSR 降级。

### 关键提交（建议优先排查）

**2.27 前后（monorepo 上线，根因可能在此）**：

| 提交 | 说明 | 与 SEO 相关性 |
|------|------|---------------|
| `feat: 优化SEO配置` (ee1b9ae) | 优化 SEO 配置 | **高** |
| `feat: add meta description` (ffc150b) | 添加 meta description | **高** |
| `feat: add meta keywords` (3e90b8f) | 添加 meta keywords | **高** |
| `feat: 支持多语言` (6e10f81) | 多语言支持（hreflang 等） | **中** |
| `feat: add home page` (198f117) | 首页 | **高** |
| `feat: add nextjs base config` (8e373e0) | Next.js 基础配置 | **中** |
| `feat: init nextjs monorepo` (c634394) | monorepo 初始化 | **中** |

**3 月上旬（若根因在 2.27，则可能为修复尝试或无关）**：

| 提交 | 说明 |
|------|------|
| `feat: update brand search SEO meta` (3.12) | 更新品牌搜索 SEO meta |
| `feat: update brand search pages with SEO meta` (3.11) | 更新品牌搜索页面 SEO meta |
| `feat: add 50+ landing pages along with SEO optimizations` (3.7) | 50+ 落地页 + SEO 优化 |

### 时间线说明：根因可能早于现象出现时间

Google 索引更新通常有延迟，改动后需数天至数周才会在搜索结果中体现。若「lessie ai」消失是近期才被注意到，**根因更可能来自 2.27 monorepo 上线或更早的配置**，而非 3.11–3.12 的 brand search SEO meta 更新。3.11–3.12 的提交可能是尝试修复，或问题自 2.27 起已存在、Google 延迟反映。

---

## 一（补充）、首页 HTML 首包实测分析

基于 lessie.ai 首页「查看网页源代码」实测（2025-03-12）：

### 严重问题：`<head>` 中完全缺失核心 SEO 标签

| 标签 | 状态 | 说明 |
|------|------|------|
| `<title>` | **缺失** | 整个 `<head>` 内无 `<title>` |
| `<meta name="description">` | **缺失** | 无 meta description |
| `<link rel="canonical">` | **缺失** | 无 canonical |

**结论**：首页首包 HTML 的 `<head>` 中**没有** title、meta description、canonical。这与 **metadata 流式传输** 或 **metadata 未正确注入** 高度一致——爬虫解析首包时看不到这些标签，无法将首页与「lessie ai」关联。

### 首包中已有的「Lessie AI」信号

| 位置 | 内容 |
|------|------|
| `img alt="Lessie AI"` | Logo 的 alt 文本 |
| JSON-LD（body 内） | `{"@type":"SoftwareApplication","name":"Lessie AI","description":"Lessie AI is your AI Agent for people search...","url":"https://lessie.ai"}` |

这些在 body 中，爬虫可见；但 **title 是品牌词匹配的首要信号**，缺失会严重影响「lessie ai」的排名。

### H1 与首屏文案

- H1 结构：`Agentic Search Engine to` + `Find` + [轮播词] + `Instantly`
- 轮播词（Influencer、B2B Leads、Investor 等）在首包中多为 `opacity:0`，首屏可见文案主要为「Agentic Search Engine to Find Instantly」
- 首包中**无**「Lessie AI」完整短语的可见正文，仅有 img alt 与 JSON-LD

### 与「lessie」正常、「lessie ai」异常的对应

- 「Lessie」：来自 `alt="Lessie AI"` 及 JSON-LD 的 `"Lessie AI"`，爬虫可部分匹配
- 「lessie ai」：依赖 title、meta description 等强信号，首包中**全部缺失**，故无法建立关联

---

## 二、「lessie」vs「lessie ai」差异分析

### 2.0 为何「lessie」正常而「lessie ai」不行？

| 可能原因 | 说明 |
|----------|------|
| **Title/Meta 中「Lessie AI」未进入首包** | 完整品牌名「Lessie AI」通常在 `<title>`、`<meta name="description">` 中；若这些 metadata 被流式注入、不在首包 HTML，Googlebot 可能看不到。而「Lessie」可能出现在 body 正文（如「Lessie helps you find…」），body 多为服务端渲染，在首包中可见。故 Google 能索引「lessie」但无法将首页与「lessie ai」精确关联。 |
| **查询解析差异** | 「lessie ai」可能被解析为「lessie」+「ai」；「ai」为高竞争泛词，Google 可能优先展示 AI 工具目录、对比页等，而非品牌首页。「lessie」单独搜索更易匹配品牌实体。 |
| **Title 结构** | 若 title 为「Lessie – People Search AI」等形式，未将「Lessie AI」作为连续短语出现，Google 可能不将该页与「lessie ai」精确匹配。 |
| **内容密度** | 若「Lessie AI」作为完整短语仅在 title/meta 出现、body 中多为「Lessie」，则「lessie」有更多可索引信号，「lessie ai」依赖的 title 若流式延迟则缺失。 |

**综合判断**：最符合「改代码后复现、回退后恢复」的，是 **metadata 流式传输** 导致 title/description 中「Lessie AI」未进入爬虫首包；body 中的「Lessie」仍可被索引，故「lessie」正常、「lessie ai」异常。

**已证实**：首页 HTML 首包实测（§一补充）确认 `<head>` 中**无** `<title>`、`<meta name="description">`、`<link rel="canonical">`，与上述判断一致。

### 2.1 本次排查方向（结合 monorepo 与历史）

| 方向 | 说明 |
|------|------|
| **SSR→CSR 降级（与上次同因）** | 某处静默报错再次触发 Next 兜底，首页降级为 CSR。建议：检查首页及根 layout 是否有运行时错误、hydration 警告；对比 2.27 前后首页首包 HTML 是否含完整内容。 |
| **monorepo 配置差异** | 合并后 next.config、路由、layout 继承关系可能变化。建议：对比原独立项目与现 monorepo 的 `next.config`、根 layout、metadata 导出方式。 |
| **metadata 流式 / 结构** | `feat: add meta description`、`feat: add meta keywords`、`feat: 优化SEO配置` 可能改变 metadata 的生成或注入方式。建议：检查 `ee1b9ae`、`ffc150b`、`3e90b8f` 的 diff，确认「Lessie AI」是否在首包 `<head>` 中。 |
| **多语言 hreflang** | `feat: 支持多语言` 若引入 hreflang 或 locale 路由，可能影响首页 canonical、默认语言判定。建议：检查 hreflang 配置、x-default 指向、是否有重复/错误 canonical。 |

---

## 三、根因分析（按优先级）

### 3.1 【高优先级】Next.js 15.2+ Metadata 流式传输导致 Title/Canonical 缺失（已实测确认）

**机制**：Next.js 15.2 起，`generateMetadata()` 默认对普通请求使用**流式传输**。服务端先发送初始 HTML shell，在 `<head>` 关闭前 metadata 尚未解析完成；`<title>`、`<link rel="canonical">`、`<meta name="description">` 等通过后续 chunk 注入。Googlebot 解析**初始响应**时，这些标签可能尚未到达。

**实测确认**：首页「查看网页源代码」显示 `<head>` 内**无** `<title>`、`<meta name="description">`、`<link rel="canonical">`，与流式传输一致。

**与本现象的对应**：
- Title 中「Lessie AI」若在流式 chunk 中，爬虫首包看不到 → 无法将首页与「lessie ai」关联
- Body 中 `alt="Lessie AI"`、JSON-LD 含「Lessie AI」→ 「lessie」仍可被部分索引
- 可解释「lessie」正常、「lessie ai」不行的差异

**后果**：
- Google 看到「User-declared canonical: None」或缺失完整 title
- 可能产生「Duplicate without user-selected canonical」错误
- 首页对「lessie ai」无排名，对「lessie」仍有部分信号

**验证**：用 `curl -s https://lessie.ai/ | head -80` 检查前 80 行是否含 `<title>…Lessie AI…</title>` 及 `<link rel="canonical">`。若缺失，与流式传输一致。

**来源**：
- [The Next.js SEO Bug That Made Google Ignore My Entire Site - Federico Sciuca (DEV)](https://dev.to/federico_sciuca/the-nextjs-seo-bug-that-made-google-ignore-my-entire-site-and-how-i-found-it-2mg0)
- [Next.js htmlLimitedBots 官方文档](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
- [Title tag insert into body (generateMetadata) - vercel/next.js#90024](https://github.com/vercel/next.js/discussions/90024)

---

### 3.2 【高优先级】Middleware 对爬虫与用户返回不同内容

**机制**：Next.js middleware 可重写 URL、重定向、修改 headers。若逻辑对 `User-Agent` 有分支（如区分 bot 与普通用户），爬虫可能收到与浏览器不同的响应。

**后果**：用户访问正常，但 Googlebot 被重定向到错误 URL、收到 noindex、或拿到空内容。

**验证**：用 `curl -A "Googlebot" https://lessie.ai/` 模拟 Googlebot 请求，对比普通请求的响应。

---

### 3.3 【中优先级】Canonical 或域名不一致

**机制**：页面实际 URL 与 canonical 指向不一致（如页面在 `lessie.ai`，canonical 指向 `www.lessie.ai`），或 sitemap 与 canonical 域名不统一。

**后果**：Google 认为「重复内容」或「非首选 URL」，忽略或降权首页。

**验证**：检查首页 `<link rel="canonical">` 与 sitemap 中的 URL 是否一致，且与用户实际访问的域名一致。

---

### 3.4 【中优先级】308 重定向链消耗爬虫预算

**机制**：`next.config.js` 中 `trailingSlash: true` 等配置可能产生 308 永久重定向链（如 `http` → `https` → `https/`），单次访问触发多次重定向。

**后果**：浪费 crawl budget，首页可能长期处于「Discovered - currently not indexed」。

**来源**：[Why Google Isn't Indexing Your Next.js Site - Yusufhan Saçak (DEV)](https://dev.to/yusufhansck/why-google-isnt-indexing-your-nextjs-site-and-how-to-find-out-in-3-seconds-5db5)

---

### 3.5 【中优先级】首页使用 `'use client'` 且关键内容未预渲染

**机制**：若首页或根 layout 被标记为 `'use client'`，或品牌名、H1 等关键内容在客户端才渲染，爬虫在首包 HTML 中可能看不到。

**说明**：`'use client'` 本身会做服务端预渲染，但若品牌名、标题等藏在需交互才显示的区域，仍可能影响索引。

**验证**：右键「查看网页源代码」，搜索「Lessie」等品牌词，确认是否在初始 HTML 中。

---

### 3.6 【低优先级】X-Robots-Tag 或 meta noindex

**机制**：Middleware、CDN 或页面可能对爬虫返回 `X-Robots-Tag: noindex`，或 HTML 中有 `meta name="robots" content="noindex"`。

**后果**：首页被明确告知不索引。

**验证**：检查响应头与 HTML 中的 robots 相关标签。

---

## 四、诊断清单

### 4.1 快速自检（按顺序执行）

| 步骤 | 操作 | 预期 |
|------|------|------|
| 1 | 右键首页 → 查看网页源代码 → 搜索「Lessie AI」「Lessie」 | 若 body 几乎为空、仅壳子，则可能 **SSR→CSR 降级**（与上次同因）；若有 body 内容但无 title/canonical，则可能 **metadata 流式** |
| 2 | 浏览器控制台、服务端日志 | 是否有 hydration 错误、运行时报错（上次根因） |
| 3 | GSC → URL 检查 → 输入 `https://lessie.ai/` → 请求编入索引 | 查看「已编入索引」或具体错误（如 Duplicate without user-selected canonical） |
| 4 | `curl -s https://lessie.ai/ \| head -80` | 前 80 行应含 `<title>…Lessie AI…</title>` 及 `<link rel="canonical">`；若缺失则与流式传输一致 |
| 5 | `curl -A "Googlebot" -s https://lessie.ai/ \| head -80` | 与步骤 4 对比，确认爬虫收到的内容是否一致 |
| 6 | 检查 `next.config.js` / `next.config.ts` | 是否有 `htmlLimitedBots`、`trailingSlash`、redirects 等配置 |
| 7 | 对比 `ee1b9ae`、`ffc150b`、`3e90b8f` 的 diff | 确认 meta、SEO 配置改动是否影响首页 metadata |

### 4.2 使用 vercel-seo-audit（推荐）

```bash
npx vercel-seo-audit https://lessie.ai
```

可检测：重定向链、canonical 不一致、sitemap、robots.txt、metadata、X-Robots-Tag 等。

**来源**：[vercel-seo-audit](https://github.com/JosephDoUrden/vercel-seo-audit)

---

## 五、修复建议

### 5.1 【首选】配置 htmlLimitedBots（Next.js 15.2+）

若使用 Next.js 15.2 及以上，在 `next.config.js` 或 `next.config.ts` 中添加：

```ts
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  htmlLimitedBots: /Googlebot|Google-InspectionTool|Bingbot|Yandex/i,
  trailingSlash: false,  // 避免 308 重定向链
}

export default nextConfig
```

**作用**：对匹配的爬虫关闭 metadata 流式传输，在首包 HTML 中同步输出完整 metadata（含 canonical、title、description）。

**更保守做法**：若希望所有爬虫都收到完整 HTML，可设置：

```ts
htmlLimitedBots: /.*/,
```

**来源**：[Next.js htmlLimitedBots](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)

---

### 5.2 检查并统一 Canonical

- 根 layout 的 canonical 使用 `"./"` 或当前页完整 URL，避免所有页都指向首页
- 确认 sitemap、canonical、实际访问域名一致（如统一用 `https://lessie.ai` 或 `https://www.lessie.ai`）

---

### 5.3 检查 Middleware

- 确认 middleware 未对 `Googlebot` 等 User-Agent 做特殊重定向或改写
- 若有必要区分 bot，确保 bot 收到的 HTML 与用户一致，且无 noindex

---

### 5.4 确保「Lessie AI」完整短语在首屏 HTML 中

- Title 中应含「Lessie AI」作为连续短语（如 `Lessie AI – People Search Agent`）
- 建议在 H1 或 body 首屏也出现「Lessie AI」完整短语，降低对 title 流式的依赖
- 品牌名、H1、核心文案应在服务端渲染，出现在「查看网页源代码」中
- 避免将品牌名、标题放在需 `'use client'` 交互后才显示的区域

---

### 5.5 修复后操作

1. 部署修复
2. GSC → URL 检查 → 输入 `https://lessie.ai/` → 请求编入索引
3. 等待数小时至数天观察品牌搜索恢复情况

---

## 六、预防措施

### 6.1 上线前检查

- [ ] 新功能/重构后，用「查看网页源代码」确认首页含品牌词、title、canonical
- [ ] 用 `curl -A "Googlebot"` 对比爬虫与普通用户收到的 HTML
- [ ] 定期运行 `npx vercel-seo-audit https://lessie.ai`

### 6.2 配置固化

- [ ] 若使用 Next.js 15.2+，在 `next.config` 中**默认**添加 `htmlLimitedBots`，避免后续改动引入流式 metadata 问题
- [ ] 将 `trailingSlash: false` 固定，避免 308 重定向链

### 6.3 CI 集成（可选）

在 CI 中接入 `vercel-seo-audit`，合并前自动检测 SEO 回归：

```yaml
# .github/workflows/seo-audit.yml
name: SEO Audit
on:
  push:
    branches: [main]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: JosephDoUrden/vercel-seo-audit@v1
        with:
          url: https://lessie.ai
          strict: true
```

---

## 七、网上类似/相似案例

| 案例 | 现象 | 根因 | 修复 | 来源 |
|------|------|------|------|------|
| **MonkeyTravel** | 搜索品牌词整站不可见，0 页被索引 | Next.js 15.2+ `generateMetadata()` 流式传输，canonical 不在首包 HTML，Google 报「Duplicate without user-selected canonical」 | 在 `next.config` 添加 `htmlLimitedBots`，对爬虫关闭流式 metadata | [Federico Sciuca - DEV](https://dev.to/federico_sciuca/the-nextjs-seo-bug-that-made-google-ignore-my-entire-site-and-how-i-found-it-2mg0) |
| **某 SaaS（247 路由）** | 迁移 Next.js 15 App Router 后，搜索曝光下降 73%，约 8 周损失 $34,000 | metadata 被渲染到 `<body>` 而非 `<head>`，247 个路由 SEO 受损 | 修正 metadata 渲染位置，确保在 `<head>` 中 | [Next.js 15 App Router Killed Our SEO - Medium](https://javascript.plainenglish.io/next-js-15-app-router-killed-our-seo-for-2-months-and-how-we-fixed-it-bfcc616c6dac) |
| **Cloudfresh** | 品牌词搜索网站消失，点击下降 97% | WordPress 迁移：重定向链、metadata 未迁移、修复 302→301 后突然消失；另有约 35% 有毒外链 | 修复 hreflang、sitemap、canonical、thin content，使用 Disavow 处理有毒链接，约 1 个月恢复 | [Promodo - Cloudfresh 案例](https://www.promodo.com/case-studies/how-we-helped-recover-coudfreshs-lost-google-search-rankings-in-1-month) |
| **某站（400+ 关键词）** | 品牌词及 400+ 关键词排名消失 | 负面 SEO：大量低质量、高 Spam Score 外链 | 使用 Google Disavow Tool 拒绝有毒链接，从竞品来源建设新链接 | [WebDesy - Not Ranking for Brand Keyword](https://webdesy.com/case-study-not-ranking-for-my-brand-keyword/) |
| **Google Search Central** | 品牌词突然从搜索结果消失 | 社区讨论：技术问题（robots、noindex、JS 渲染）、迁移、外链等 | 需逐案排查 | [Keyword Brand suddenly Disappear - GSC Community](https://support.google.com/webmasters/thread/373889497/keyword-brand-suddenly-disappear-from-google-search?hl=en) |

**与 Lessie 的相似度**：MonkeyTravel、Next.js 15 某 SaaS 与 Lessie 最接近——均为 **Next.js + 改代码后品牌/搜索表现异常**，且与 metadata 流式传输或渲染位置有关。Cloudfresh、WebDesy 案例根因不同（迁移、外链），但现象类似，可作排查参考。

---

## 八、引用来源

| 序号 | 来源 | URL |
|------|------|-----|
| 1 | Federico Sciuca - Next.js SEO Bug (MonkeyTravel 案例) | https://dev.to/federico_sciuca/the-nextjs-seo-bug-that-made-google-ignore-my-entire-site-and-how-i-found-it-2mg0 |
| 2 | Yusufhan Saçak - Why Google Isn't Indexing Your Next.js Site | https://dev.to/yusufhansck/why-google-isnt-indexing-your-nextjs-site-and-how-to-find-out-in-3-seconds-5db5 |
| 3 | Next.js - htmlLimitedBots | https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots |
| 4 | vercel/next.js - Title tag insert into body (generateMetadata) | https://github.com/vercel/next.js/discussions/90024 |
| 5 | vercel-seo-audit | https://github.com/JosephDoUrden/vercel-seo-audit |
| 6 | Next.js - Streaming Metadata | https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata |
| 7 | MonsterClaw - Brand keywords not appearing on Google | https://monsterclaw.com/brand-keywords-not-appearing-on-google-what-should-i-do/ |
| 8 | Search Engine Roundtable - Google fewer brand names in titles | https://seroundtable.com/google-fewer-brand-names-in-search-result-titles-35141.html |
| 9 | WebDesy - Not Ranking for Brand Keyword (负面 SEO) | https://webdesy.com/case-study-not-ranking-for-my-brand-keyword/ |
| 10 | Promodo - Cloudfresh 品牌词消失恢复案例 | https://www.promodo.com/case-studies/how-we-helped-recover-coudfreshs-lost-google-search-rankings-in-1-month |
| 11 | Next.js 15 App Router Killed Our SEO (metadata 进 body) | https://javascript.plainenglish.io/next-js-15-app-router-killed-our-seo-for-2-months-and-how-we-fixed-it-bfcc616c6dac |
| 12 | Google Search Central - Keyword brand suddenly disappear | https://support.google.com/webmasters/thread/373889497/keyword-brand-suddenly-disappear-from-google-search?hl=en |

---

*文档生成日期：2025-03-12*
