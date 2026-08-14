# Dubbing AI Agent-Ready 审计与优化报告

> **归档说明**：本文档已于 2026-06-22 移入 `_archive/`，不再维护。活跃文档见 [_archive/README.md](./README.md)。

> 基于 Cloudflare isitagentready.com 的 19 项 AI 代理就绪度检查框架，以及扩展的六种网站类型策略模型，对 dubbingai.io 进行 Agent-Ready 基线审计、类型定位与分级优化建议。框架依据：[GEO Agent-Ready 与 AI 代理发现](../../../GEO/08-GEO-Agent-Ready与AI代理发现.md)。

**审计日期**：2026-05-12  
**审计对象**：dubbingai.io（含 blog.dubbingai.io、dubbing.tech、shop.dubbingai.io）  
**审计工具链**：isitagentready.com 框架 + 手工审查 + 站内文档对照

---

## 一、执行摘要

Dubbing AI 是一个**混合型 B2C 站点**——兼具 SaaS（桌面 App + 在线变声器 Web 端）、内容（Blog + 程序化 SEO 页面矩阵）和电商（Dubbing Box 硬件 shop）三重属性。这是 Agent-Ready 框架中最复杂的站点类型之一：不像纯内容站可以安心停留在 Level 3，也不像纯 SaaS 平台可以直奔 Level 5。

**核心发现**：Dubbing AI 已有一个被低估的 Agent-Ready 资产——`/llm-info` 页面——专门面向「Hey AI, know us better」场景设计，这在同体量竞品中极为罕见。但站点在**基础可发现性层面存在严重短板**（sitemap 返回 HTML 而非 XML、robots.txt 无 AI 爬虫规则、无 Content Signals），这会导致即使内容优质，AI 代理也无法高效发现和消费。

**快速胜出机会**：修复 sitemap + 加 Content Signals + 补 Link 响应头——三项合计约 1 小时的工程投入——即可将该站从当前约 Level 1 提升至 Level 2-3，领先 96% 的互联网站点。

---

## 二、站点类型分类

按照 Agent-Ready 框架中的六种网站类型，Dubbing AI **以 SaaS/内容站为主，含电商子站**：

| 维度 | 分类 | 说明 |
|------|------|------|
| **核心类型** | SaaS（B2C 工具型） | 桌面 App 下载 + Web 在线变声器 + SDK |
| **内容层** | 内容/Blog + 程序化页面 | Blog + /all-voice-changers Hub + 数百个角色/游戏/音效程序化页面 |
| **电商层** | 电商（硬件） | shop.dubbingai.io — Dubbing Box 硬件销售 |
| **多语言** | 11 种语言子路径 | de/fr/ja/ru/es/pt/it/kr/zh/tr + 根路径英文 |
| **中文站** | 独立域名 | dubbing.tech |

**影响**：这种混合性质意味着 Agent-Ready 策略不能一刀切。Voice Changer 和 Soundboard 的内容层适用内容站策略（Level 3 为合理目标），但 SDK 页面和 API 如有则应适用 SaaS 策略（Level 4-5）。需要在不同子域/路径层采用差异化的判断标准。

---

## 三、当前状态审计（19 项逐项检查）

### 3.1 Discoverability（可发现性）

| # | 检查项 | 当前状态 | 发现 | 判定 |
|---|--------|---------|------|------|
| 1 | robots.txt | ⚠️ 存在但不完善 | 存在但仅 4 条 Disallow（`/sounds/`、`/login/`、`/terms-of-policy`、`/privacy-policy`）。**无任何 AI 爬虫规则**（GPTBot、ClaudeBot、PerplexityBot 等均未声明）。主站 robots.txt 已有 `/privacy-policy` 被 Disallow——这可能意外阻止某些 AI 爬虫的合法访问。 | 🔴 应修复 |
| 2 | sitemap.xml | ❌ 严重问题 | `/sitemap.xml` 返回 HTML（SPA 壳），**非**标准 XML。AI 代理和传统搜索引擎爬虫均无法通过它发现全站 URL。这是本次审计中**严重性最高**的单一缺陷。 | 🔴 紧急 |
| 3 | Link 响应头 | ❌ 未部署 | 无任何 Link 响应头。代理无法在 HTML 解析前发现 sitemap、RSS feed 或 Markdown 替代版本。 | 🔴 应做 |

### 3.2 Content Accessibility（内容可访问性）

| # | 检查项 | 当前状态 | 发现 | 判定 |
|---|--------|---------|------|------|
| 4 | Markdown 内容协商 | ❌ 未部署 | 不支持 `Accept: text/markdown`。对 Blog 文章和程序化 SEO 页面而言，这是让 AI 代理高效消费内容的最重要优化。 | 🔴 应做（高价值） |

### 3.3 Bot Access Control（机器人访问控制）

| # | 检查项 | 当前状态 | 发现 | 判定 |
|---|--------|---------|------|------|
| 5 | AI Bot Rules | ❌ 缺失 | robots.txt 中无任何 AI 爬虫 User-Agent 规则。OAI-SearchBot、Claude-SearchBot、PerplexityBot 等均未声明允许或禁止。 | 🔴 应做 |
| 6 | Content Signals | ❌ 缺失 | robots.txt 中无 Content-Signal 声明。这是零成本、1 分钟可完成的优化。 | 🔴 应做 |
| 7 | Web Bot Auth | ⚪ 不适用 | 加密签名 bot 验证，Dubbing AI 当前不需要。 | ⚪ |

### 3.4 Protocol Discovery（协议发现）

| # | 检查项 | 当前状态 | 发现 | 判定 |
|---|--------|---------|------|------|
| 8 | MCP Server Card | ⚪ 不适用（当前） | 无 MCP 服务。但 Dubbing AI 有一个 `/sdk` 页面——如果未来将 SDK 扩展为可供编程代理调用的 API，MCP Server Card 会变得相关。 | 🟡 远期可考虑 |
| 9 | A2A Agent Card | ⚪ 不适用 | 无 AI 代理间通信需求。 | ⚪ |
| 10 | Agent Skills | ⚪ 不适用 | 无供代理调用的能力声明。但 Voice Changer 参数查询（如"支持哪些游戏"、"Gojo 声音怎么设"）如通过 API 暴露，可声明为 Agent Skill。 | 🟡 远期可考虑 |
| 11 | WebMCP | ⚪ 不适用 | 浏览器端 MCP。 | ⚪ |
| 12 | API Catalog（RFC 9727） | ⚪ 不适用 | 无公开 API。但 `/sdk` 存在——如 SDK 是面向开发者的集成接口，API Catalog 将来可能适用。 | 🟡 远期可考虑 |
| 13 | OAuth Discovery | ⚪ 不适用 | 无 OAuth 认证的 API。 | ⚪ |
| 14 | OAuth Protected Resource | ⚪ 不适用 | 同上。 | ⚪ |

### 3.5 Commerce（商业协议）

| # | 检查项 | 当前状态 | 发现 | 判定 |
|---|--------|---------|------|------|
| 15-19 | x402 / MPP / UCP / ACP / AP2 | ⚪ 不适用 | shop.dubbingai.io 是独立子域电商。当前非 Shopify 架构，UCP/ACP 不适用。但如未来切换 Shopify 或对接 AI 购物代理，Commerce 协议会变得相关。 | 🟡 远期可考虑 |

### 3.6 特殊资产：`/llm-info` 页面

Dubbing AI 拥有一个在同类竞品中罕见的 **`/llm-info`** 页面——专门为「Hey AI, know us better」场景设计。它的存在说明团队对 AI 代理发现已有意识，这是 SEO 成熟度的积极信号。

**当前局限**：
- `/llm-info` 的存在没有被 Link 响应头或 robots.txt 信号化——代理需要主动猜测或从 Footer 链接中发现
- `llms.txt` 尚未部署——`/llm-info` 可以作为 `/llms.txt` 的内容基础

---

## 四、Gap 分析：与同类站点的差距

### 4.1 竞争对比

| 维度 | Dubbing AI 当前 | Voicemod（推测） | Voice.ai（推测） | 行业基准（SaaS 类） |
|------|----------------|-----------------|-----------------|-------------------|
| robots.txt | 基础存在 | 未知 | 未知 | 78% 有 |
| AI Bot Rules | ❌ | 未知 | 未知 | ~15% 有 |
| sitemap（XML） | ❌ SPA 壳 | 未知 | 未知 | 基准 |
| Content Signals | ❌ | 未知 | 未知 | ~4% |
| Link Headers | ❌ | 未知 | 未知 | ~3.8% |
| Markdown 协商 | ❌ | 未知 | 未知 | ~3.9% |
| /llm-info 或等效 | ✅ 有 | 未知 | 未知 | <1% |
| 评分估算 | **~Level 1** | — | — | — |

**关键机会**：Dubbing AI 作为一个已经有 `/llm-info` 的站点，修复基础层（sitemap + AI Bot Rules + Content Signals + Link 头）后即可**大幅度领先行业基线**。鉴于竞品大概率也处于 Level 0-1（基于 4% 的 Content Signals 行业通过率），1 小时的工程投入可建立显著的 Agent-Ready 先发优势。

### 4.2 潜在 AI 消费场景（与产品特性高度相关）

Dubbing AI 的以下内容类型会被 AI 代理频繁消费：

| 内容类型 | AI 消费场景 | Agent-Ready 优先级 |
|----------|-----------|-------------------|
| Blog 教程（"how to change voice on Discord"） | ChatGPT/Perplexity/Claude 回答"怎么在 Discord 变声" | **极高** |
| 程序化 Voice Changer 页（/voice-changer/gojo） | AI 回答"best Gojo voice changer" | **极高** |
| 对比/选购内容（"best AI voice changer 2026"） | AI 购物代理进行产品比较 | **高** |
| Soundboard/Sound Gallery 页 | AI 回答"where to find meme sounds" | **高** |
| FAQ（/questions） | AI 直接摘取支持答案 | **高** |
| SDK 文档 | 编码 Agent（Claude Code/Cursor）集成参考 | **中** |
| Dubbing Box 产品页 | AI 购物代理推荐硬件 | **中** |

### 4.3 GEO 目标问题（用户可能在 AI 中提问）

以下问题来自 V1 归档，可作为 `/llm-info`、`/llms.txt` 与 FAQ 的内容覆盖检查清单——确保 AI 代理引用时能链到对应落地页：

| 用户问题 | 建议落地页 |
|----------|------------|
| What are the best free AI voice changer apps for PC/mobile? | 首页或功能页 |
| Which voice changer has the most realistic female/male voice effect? | female/male 落地页 |
| What is the best AI voice changer for Discord? | /discord-voice-changer |
| How do I set up a real-time voice changer with AirPods? | AirPods 页或 /supported-apps |
| How to use an AI voice changer in Discord? | /discord-voice-changer |
| What is the best mobile voice changer right now? | Dubbing Box / /mobile-voice-changer |
| How to change voice on MacBook/Mobile/console/PS5? | /supported-apps 或硬件页 |
| Which voice changer sounds most natural, not robotic? | Features 页 |
| How can I sound like a female/male character in games? | Voice Changer 页、游戏落地页 |
| How to train my own AI model for a custom voice? | /voice-cloning |
| How to sound like Trump/celebrity? | 名人 Voice Changer 页 |
| Can I use a voice changer on Discord mobile while gaming? | 游戏页 + /discord-voice-changer |
| How to change my voice while talking in games like PUBG or COD Mobile? | PUBG、COD 游戏页 |

---

## 五、分级实施建议

### P0 — 紧急（约 1 小时工程投入）

这些是**成本极低、回报明确的**修复，修复后可将站点从 Level 1 提到 Level 2-3。

#### 5.1 修复 sitemap.xml（严重性最高）

**问题**：`/sitemap.xml` 返回 HTML SPA 壳，非标准 XML。搜索引擎和 AI 爬虫均无法通过它发现 URL。

**实施**（Vue + SSG 技术栈）：
- **SSG 构建时生成**：在 `nuxt.config.ts` 中配置 `@nuxtjs/sitemap` 模块，或在 VitePress 的 `config.ts` 中配置 sitemap 生成。SSG 在构建时已掌握所有静态路由，生成 XML sitemap 为天然能力
- **程序化页面**：Voice Changer（/voice-changer/*）、Sound Gallery（/sound-gallery/*）、Community Sounds（/community-sounds/*）等动态路由较多——需要确保在 `nitro.prerender.routes` 或等效配置中完整声明爬取路径，或在构建时从数据源自动生成路由列表
- **多语言**：dubbingai.io 支持 de/fr/ja/ru/es/pt/it/kr/zh/tr 十种语言子路径——sitemap 中需为每个语言版本声明 `<xhtml:link rel="alternate" hreflang="...">`
- 提交至 Google Search Console 和 Bing Webmaster Tools
- 在 robots.txt 中添加 `Sitemap: https://dubbingai.io/sitemap.xml`

#### 5.2 robots.txt 升级

**当前（不完善）**：
```
# 仅 4 条 Disallow，无 AI 爬虫规则
Disallow: /sounds/
Disallow: /login/
Disallow: /terms-of-policy
Disallow: /privacy-policy
```

**建议升级为**：
```
# === AI 搜索爬虫（允许引用和发现） ===
User-agent: OAI-SearchBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /

# === AI 训练爬虫（允许引用，拒绝训练） ===
User-agent: GPTBot
Disallow: /
User-agent: Claude-Web
Disallow: /
User-agent: Google-Extended
Disallow: /

# === 传统搜索引擎 ===
User-agent: *
Allow: /
Disallow: /sounds/
Disallow: /login/
Disallow: /terms-of-policy
Disallow: /privacy-policy

# === Agent 发现信号 ===
Sitemap: https://dubbingai.io/sitemap.xml
Content-Signal: search=yes, ai-input=yes, ai-train=no
```

**注意**：当前 `/privacy-policy` 在 robots.txt 中被 Disallow，但该页在站内 Footer 中被链接。需确认这是有意为之还是历史配置——如果希望隐私政策被搜索引擎索引（通常应该），应移除该 Disallow。

#### 5.3 Content Signals

在 robots.txt 中加一行（已包含在上述 robots.txt 升级中）：

```
Content-Signal: search=yes, ai-input=yes, ai-train=no
```

**策略理由**（适用于 Dubbing AI）：
- `search=yes`：允许出现在搜索结果中——Voice Changer 和 Soundboard 的发现依赖搜索
- `ai-input=yes`：允许被 AI 引用——Blog 教程和程序化页面的核心价值就是被 AI 回答引用
- `ai-train=no`：拒绝无偿训练——Dubbing AI 的 500+ 声音库和 100,000+ 音效数据属于核心 IP，不应被用于训练竞品模型

#### 5.4 首页 Link 响应头

为首页和关键入口添加 Link 响应头。Vue + SSG 技术栈下有两种路径：

**方案 A：部署层/CDN 层（推荐，不改代码）**

如果站点使用 Cloudflare 或 Nginx 作为反向代理，在部署层设置静态页面响应头：

```nginx
# Nginx 示例
location = / {
    add_header Link '</sitemap.xml>; rel="sitemap", </llms.txt>; rel="alternate"; type="text/markdown", </llm-info>; rel="alternate"';
}

location ~ ^/(de|fr|ja|ru|es|pt|it|kr|zh|tr)$ {
    add_header Link '</sitemap.xml>; rel="sitemap", </llms.txt>; rel="alternate"; type="text/markdown"';
}
```

Cloudflare 用户可直接配置 Transform Rules 或 Response Header Modification Rules，无需改动 Vue 代码。

**方案 B：Nuxt 服务端中间件**

如果使用 Nuxt 的 Nitro 服务端引擎：

```ts
// server/middleware/link-headers.ts
export default defineEventHandler((event) => {
  const path = getRequestURL(event).pathname;

  if (path === '/' || /^\/(de|fr|ja|ru|es|pt|it|kr|zh|tr)$/.test(path)) {
    setResponseHeader(event, 'Link',
      '</sitemap.xml>; rel="sitemap", </llms.txt>; rel="alternate"; type="text/markdown"');
  }
});
```

**局限**：SSG 纯静态部署（如直接推送到 CDN 静态存储）时，无法执行服务端中间件。推荐方案 A（CDN 层）。在静态文件部署描述符（如 `_headers` 文件，取决于托管平台）中声明也可达到同样效果。

### P1 — 近期（2-6 小时工程投入）

#### 5.5 部署 llms.txt + llms-full.txt

**基础**：已有的 `/llm-info` 页面可作为 `/llms.txt` 的内容起点。

**`/llms.txt` 结构建议**（基于 /llm-info 内容）：
```markdown
# Dubbing AI

Dubbing AI is a real-time AI voice changer for gamers, streamers, and content creators.
500+ character voices, 100,000+ meme sound effects, <30ms latency.

## Core Products
- Real-time Voice Changer: https://dubbingai.io/
- Soundboard: https://dubbingai.io/soundboard
- Voice Cloning: https://dubbingai.io/voice-cloning
- Online Voice Changer: https://dubbingai.io/online-voice-changer
- Dubbing Box (Hardware): https://shop.dubbingai.io/

## Key Pages
- All Voice Changers: https://dubbingai.io/all-voice-changers
- Community Sounds: https://dubbingai.io/community-sounds
- SDK: https://dubbingai.io/sdk
- Supported Apps: https://dubbingai.io/supported-apps
- FAQ: https://dubbingai.io/questions
- Blog: https://dubbingai.io/blog

## Languages
English: https://dubbingai.io/
Chinese: https://dubbing.tech/
Also available in: de, fr, ja, ru, es, pt, it, kr, tr
```

**`/llms-full.txt`**：在 full 版本中纳入所有产品页面的完整 markdown 正文（或至少前 10 篇最高流量 blog 文章 + 核心产品页）。

#### 5.6 Markdown 内容协商——高优先级页面

**第一阶段覆盖**（按 AI 引用价值排序）：
1. Blog 文章（/blog/*）——教程类内容最常被 AI 引用
2. Voice Changer 程序化页面（/voice-changer/gojo、/valorant-voice-changer 等）——游戏/角色查询
3. FAQ（/questions）——AI 摘取答案的直接来源
4. 核心产品页（首页、/soundboard、/voice-cloning）

**Vue + SSG 技术栈下的三条路径**：

**方案 A：CDN 层（推荐，无需改动 Vue 代码）**

如果站点使用 Cloudflare 或类似 CDN，用 Transform Rules 检测 `Accept: text/markdown` 请求头，自动改写路径到预生成的 Markdown 文件：

```
# Cloudflare Transform Rule 逻辑
if (http.request.headers["accept"] contains "text/markdown") {
  # 将 /blog/my-post 改写为 /md/blog/my-post.md
  rewrite to concat("/md", http.request.uri.path, ".md")
}
```

构建时在 `/md/` 目录下预生成所有目标页面的 `.md` 文件，CDN 按规则映射。零运行时开销，不增加 Vue 应用复杂度。

**方案 B：Nuxt Nitro Server Routes**

如果使用 Nuxt（Nitro 服务端引擎），在 `/server/routes/md/` 下创建 catch-all 路由：

```ts
// server/routes/md/[...path].ts
export default defineEventHandler(async (event) => {
  const accept = getRequestHeader(event, 'accept') || '';

  if (!accept.includes('text/markdown')) {
    throw createError({ statusCode: 406, statusMessage: 'Not Acceptable' });
  }

  setResponseHeader(event, 'Vary', 'Accept');
  // 读取预生成的 .md 文件或从 CMS 按需渲染
  const path = getRouterParam(event, 'path');
  const md = await useStorage().getItem(`content:md:${path}.md`);
  return md;
});
```

**方案 C：纯 SSG 静态文件**

如果 SSG 输出为纯静态文件（无服务端运行时），在构建流程中：
1. 遍历目标页面路由，从数据源渲染 Markdown
2. 将 `.md` 文件写入 `dist/md/{path}.md`
3. 部署后由 CDN 按 `Accept` 头做条件路由（回到方案 A）

**方案对比**：

| | 方案 A（CDN） | 方案 B（Nitro） | 方案 C（纯静态） |
|---|---|---|---|
| 代码改动 | 零 | 少量 | 构建脚本 |
| 运行时开销 | 零 | 低 | 零 |
| 灵活性 | 中 | 高 | 低 |
| 推荐度 | ✅ 首选 | 🟡 Nuxt 用户 | 🟡 静态托管 |

#### 5.7 HTML 头部 Markdown 替代声明

在 Blog 文章和 Voice Changer 页面的 HTML `<head>` 中添加：
```html
<link rel="alternate" type="text/markdown" href="/page-path.md">
```

### P2 — 后续（4-10 小时工程投入）

#### 5.8 sitemap.md

在站点根目录提供 Markdown 格式的站点地图，作为 XML sitemap 的 AI 友好补充。特别列出 Voice Changer 和 Soundboard 的程序化页面层级。

#### 5.9 Agent Skills Index（如有 SDK/API）

如果 Dubbing AI 的 SDK 暴露了可被编程代理调用的接口，在 `/.well-known/agent-skills/index.json` 中声明。即使只是声明"Voice Changer 参数查询"能力，也能在 isitagentready 中获得额外分数并提高对编码 Agent 的可发现性。

#### 5.10 X-Markdown-Tokens 响应头

在 Markdown 端点中返回 token 数估算，帮助 AI 代理进行上下文窗口规划。对长 Blog 文章尤其有用。

### P3 — 远期评估

| 事项 | 触发条件 | 说明 |
|------|---------|------|
| MCP Server Card | SDK 扩展为公开 API | 让编码 Agent 通过 MCP 直接查询 Voice Changer 参数和兼容性 |
| API Catalog（RFC 9727） | 同上 | `/.well-known/api-catalog` |
| UCP/ACP Commerce 协议 | shop 切换 Shopify 或需要被 AI 购物代理发现 | 目前 shop 为子域独立运营，短期不需要 |
| 多语言 llms.txt | 非英文市场（韩语、日语、德语）流量增长 | 为每种语言提供独立的 `/llms-{lang}.txt` |

---

## 六、实施优先级总表

| 优先级 | 事项 | 预算 | 影响 |
|--------|------|------|------|
| **P0** | 修复 sitemap.xml（生成标准 XML） | 30 分钟 | 解除当前最严重的发现障碍 |
| **P0** | robots.txt 升级（AI 爬虫规则 + Sitemap 声明） | 5 分钟 | 让 AI 爬虫知道如何正确抓取 |
| **P0** | Content-Signal 声明 | 1 分钟 | 零成本提升至 Level 2 |
| **P0** | 首页 + Blog 入口 Link 响应头 | 15 分钟 | 代理在 HTML 前即可发现 sitemap 和 llms.txt |
| **P1** | 部署 /llms.txt + /llms-full.txt | 30 分钟 | 基于已有 /llm-info 快速构建 |
| **P1** | Blog + 热门程序化页 Markdown 协商 | 3-4 小时 | 核心内容被 AI 高效消费 |
| **P1** | HTML head link rel alternate markdown | 30 分钟 | 降低代理发现成本 |
| **P2** | sitemap.md | 15 分钟 | 补充发现层 |
| **P2** | Agent Skills Index（如 SDK 可调用） | 1-2 小时 | 面向编码 Agent |
| **P2** | X-Markdown-Tokens 响应头 | 30 分钟 | 代理上下文规划 |

### 预期评分变化

| 扫描项 | 当前 | P0 后 | P1 后 |
|--------|------|--------|--------|
| robots.txt | ⚠️ 不完善 | ✅ | ✅ |
| sitemap.xml | ❌ HTML | ✅ | ✅ |
| AI Bot Rules | ❌ | ✅ | ✅ |
| Content Signals | ❌ | ✅ | ✅ |
| Link Headers | ❌ | ✅ | ✅ |
| Markdown 协商 | ❌ | ❌ | ✅ |
| **估计评分** | **~Level 1** | **Level 2** | **Level 3-4** |

Dubbing AI 作为 SaaS 混合站，P1 完成后的 Level 3-4 已优于 96%+ 的互联网站点。MCP/API Catalog 等项留待远期 SDK 扩展时再做，不应为刷分而部署空壳声明。

---

## 七、站点特有的注意事项

### 7.1 多域名策略

Dubbing AI 有四个域名/子域，Agent-Ready 信号需要覆盖面：

| 域名 | 用途 | Agent-Ready 策略 |
|------|------|-----------------|
| dubbingai.io | 主站 | 全部 P0-P1 策略 |
| blog.dubbingai.io | 博客子域 | 独立 robots.txt + Content Signals + Markdown 协商（博客是 AI 引用最高频的内容） |
| dubbing.tech | 中文品牌站 | 独立 robots.txt + Content Signals + /llms.txt（中文内容） |
| shop.dubbingai.io | 硬件商城 | 最小策略：robots.txt + sitemap；暂不做 Markdown 协商 |

### 7.2 程序化页面的特殊性

Dubbing AI 拥有数百个程序化页面（/voice-changer/*、/sound-gallery/*），全部做 Markdown 协商会造成工程开销。建议策略：
- **Markdown 协商**：仅对高流量程序化页面（Gojo、Valorant 等头部词）+ Blog 文章启用
- **sitemap.xml**：确保所有程序化页面被纳入
- **llms.txt**：汇总 Voice Changer 和 Soundboard 的层级结构，而非逐页列出

### 7.3 与 Voicemod 的 Agent-Ready 竞争

如果 Voicemod 尚未部署 Agent-Ready 标准（根据行业约 4% 的 Content Signals 通过率推算，大概率如此），Dubbing AI 在 P0 完成后即可在 Agent 发现层形成差异化。建议在部署完成后进行一次 isitagentready.com 扫描，与 Voicemod（voicemod.net）的扫描结果做比较——如果 Voicemod 的评分显著低于 Dubbing AI，这一数据点可用于营销内容（"AI 代理更容易找到我们"）。

### 7.4 robots.txt 中的 `/privacy-policy` 冲突

当前 robots.txt 中 `Disallow: /privacy-policy` 与站内 Footer 中公开链接的隐私政策页冲突。建议：
- 如隐私政策页在站内被公开链接且无敏感凭证信息，移除该 Disallow
- 如确需屏蔽，在 robots.txt 中添加注释说明原因

---

## 八、监测验证

部署后按以下顺序验证：

```bash
# 1. 验证 sitemap.xml 为有效 XML
curl -s https://dubbingai.io/sitemap.xml | head -5
# 期望：<?xml version="1.0" encoding="UTF-8"?>

# 2. 验证 robots.txt 含 AI 规则和 Content-Signal
curl -s https://dubbingai.io/robots.txt | grep -E 'GPTBot|Content-Signal|Sitemap'

# 3. 验证 Link 响应头
curl -sI https://dubbingai.io/ | grep -i link

# 4. 验证 llms.txt（部署后）
curl -s https://dubbingai.io/llms.txt | head -20

# 5. 验证 Markdown 协商（部署后）
curl -s -H "Accept: text/markdown" https://dubbingai.io/blog/best-ai-voice-changer | head -20

# 6. isitagentready.com 扫描
# 浏览器打开 https://isitagentready.com
# 输入 dubbingai.io → 记录评分
# 输入 voicemod.net → 对比评分
```

---

## 九、与内部文档的关联

| 关联文档 | 用途 |
|---------|------|
| [dubbingai.md](../dubbingai.md) | 产品上下文、定位、ICP |
| [dubbingai-site-structure.md](../dubbingai-site-structure.md) | 线上 URL 结构、Footer 矩阵、robots.txt 现状 |
| [dubbingai-features.md](../dubbingai-features.md) | 功能页、产品线 |
| [dubbingai-keywords.md](../dubbingai-keywords.md) | 关键词映射——Agent-Ready 应与关键词策略联动 |
| [08-GEO-Agent-Ready与AI代理发现](../../../GEO/08-GEO-Agent-Ready与AI代理发现.md) | 本报告的方法论框架 |

---

*本报告基于 2026-05-12 对 dubbingai.io 的文档审计和框架分析。isitagentready.com 的实际扫描结果可能与估算有差异——建议在 P0 部署前后各做一次实际扫描，建立可测量的基线。Agent-Ready 评分不等同于 GEO 效果，实施后应配合内容新鲜度和 Schema 优化（见 GEO 框架 §六）以获得最大 AI 引用率提升。*
