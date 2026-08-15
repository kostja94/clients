# MeDo GEO（生成式引擎优化）全面检查清单

> **主站**：https://miaoda.io（营销主站，canonical 主域）
> **产品站**：https://medo.dev（App 构建器 / UGC 广场 / 工作区）
> **适用**：MeDo 在 ChatGPT / Perplexity / Gemini / AI Overviews / Claude / Copilot 等生成式引擎中的可见度、引用与引荐流量全链路
> **用途**：上线前逐项打勾；月度复盘；作为 GEO 专项验收基准
> **Last updated**：2026-08-14
> **本次核对方式**：2026-08-14 实际抓取 miaoda.io / medo.dev 验证（非推断）

---

## 一、站点架构与域名关系（先对齐口径）

| 域名 | 用途 | 状态（2026-08-14 实测） |
|------|------|------------------------|
| **miaoda.io** | 营销主站：Home / Features / Pricing / Templates / Solutions / Showcase / Comparisons / Blogs / Events / Programs | Next.js SSR，全站首屏 HTML 完整（110–200KB），**canonical 主域** |
| **medo.dev** | App 构建工作区 + 应用广场 + 内容镜像 | SPA 工作区为主；部分营销页（blogs/templates）SSR 镜像且 **canonical 指向 miaoda.io** ✅ |
| **MIAODA docs** | 百度云文档体系 | 第三方域，实体锚点 |

**双域架构要点（本次实测确认）**：
- ✅ medo.dev 上镜像的 blog 文章 `canonical` 正确指向 `https://miaoda.io/...`（重复内容治理正确）
- ❌ **不统一**：medo.dev 的 `/pricing`、`/comparisons/*`、`/llms.txt`、`/skill.md` 返回 **SPA 空壳（约 6.5KB）**，而 miaoda.io 对应页完整——两域状态不同步，AI 若引到 medo.dev 的空壳版本则信息缺失
- ❌ **llms.txt 链接指向错误域**：miaoda.io 的 `/llms.txt` 里所有链接（Home/Pricing/Templates/Blog）写的是 `https://medo.dev/...`，应为 miaoda.io

> **P0 行动**：先定版「营销页 canonical 一律 miaoda.io、medo.dev 上所有营销页要么 SSR 完整要么 301/canonical 到 miaoda.io」。

---

## 二、现状核对总表（2026-08-14 实测）

> 图例：✅ 已达标 · ⚠️ 部分/需优化 · ❌ 未达标/缺失 · **?** 无法外部验证

| 检查域 | 状态 | 实测证据 |
|--------|:----:|----------|
| 全站 SSR / 首屏 HTML | ✅ | 首页 198KB、pricing 180KB、templates、blogs 均完整；非 SPA 空壳 |
| 首页 robots.txt | ✅ | 返回 200 text/plain；检索爬虫 Allow + 训练爬虫 Disallow + Sitemap 声明 |
| robots 训练/检索分离 | ✅ | OAI-SearchBot/PerplexityBot/Claude-SearchBot/Claude-User 单独 Allow |
| Content-Signal | ❌ | robots.txt 无 `Content-Signal:` 行 |
| Sitemap 有效性 | ✅ | `/sitemap.xml` 返回 `application/xml`（非空壳），单文件 176 URL |
| Sitemap hreflang | ✅ | 每个 URL 含 12 语言 `xhtml:link` 互指 |
| llms.txt | ⚠️ | miaoda.io 已存在（text/plain，2232B）但链接指向 medo.dev；数字过时（"10,000+" vs 现网 17,000+）；缺 Integrations/Components/Events/Programs |
| medo.dev/llms.txt | ❌ | 返回 HTML 空壳（head 声明了 alternate 但实际非文本） |
| medo.dev/skill.md | ❌ | 返回 HTML 空壳（声明为 agent 指引但实际非 Markdown） |
| 首页 Schema | ✅ | Organization + WebSite + SoftwareApplication + FAQPage（6 题），`@id` 均用 miaoda.io |
| Organization 完整度 | ⚠️ | 有 name/url/logo，但缺 `legalName` / `sameAs`（schema-spec 附录 A 要求） |
| Pricing Schema | ✅ | SoftwareApplication + AggregateOffer + FAQPage（7 题）+ BreadcrumbList + 25 hreflang |
| 对比页 Schema | ✅ | FAQPage（5 题）+ BreadcrumbList + canonical 正确 |
| Blog Schema | ✅ | BlogPosting + Person + FAQPage + BreadcrumbList + 12 hreflang |
| 多语言 | ✅ | 12 语言（en/de/es/fr/it/zh-CN/zh-HK/ja/ko/hi/ar/pt-BR）+ x-default；首页 13 条 alternate |
| 中文版 | ✅ | `/zh-CN`、`/zh-CN/pricing` 均 200 SSR；`/zh`（无后缀）404、`/en` 307→`/` |
| 页面 URL 规范 | ⚠️ | `/blog`→308→`/blogs`；sitemap 用 `/blogs/`（复数）✅，但 llms.txt 用 `/blogs/`，本地旧文档用 `/blog/` |
| Google-Extended 策略 | ❌ | robots.txt 将 **Google-Extended 设为 Disallow**——按 GEO 方法论 Google 侧 AI（Gemini/AI Overviews）应 Allow 或按需 |
| Link 响应头 | ❌ | 首页无 `Link:` 头（sitemap/RSS/Markdown 未通过 HTTP 头暴露） |
| 营销页薄内容 | ⚠️ | `/programs/affiliate` 仅 3.5KB、`/solutions` 仅 11.7KB（疑似薄内容） |
| GSC/Bing 验证 | **?** | medo.dev 有 `google-site-verification` meta；miaoda.io 无法外部验证，需后台确认 |

---

## 三、第一部分 · 可抓取性与技术基础（AI 爬虫能不能读到）

> 核心原则：**多数 AI 爬虫（GPTBot / ClaudeBot / PerplexityBot）不执行或弱执行 JavaScript**——关键内容必须在首屏 HTML 中可读。✅ miaoda.io 已满足；以下为保留项与双域补齐。

### 3.1 渲染与首屏 HTML

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 3.1.1 | 营销主站全站 SSR | 各页首屏 HTML 含正文（miaoda.io 已达标） | `curl -s <url> \| findstr /C:"root"` | **P0** | ✅ |
| 3.1.2 | **medo.dev 营销镜像页与主站同步** | medo.dev 上的 `/pricing`、`/comparisons/*` 等不再是 6.5KB 空壳；或 301/canonical 到 miaoda.io | `curl -sI https://medo.dev/pricing` 检查体积/跳转 | **P0** | ❌ |
| 3.1.3 | medo.dev/llms.txt 返回纯文本 | HTTP 200 + `Content-Type: text/plain` + Markdown | `curl -sI https://medo.dev/llms.txt` | **P1** | ❌ |
| 3.1.4 | medo.dev/skill.md 返回 Markdown | HTTP 200 + `Content-Type: text/markdown` 或 text/plain | `curl -sI https://medo.dev/skill.md` | **P1** | ❌ |
| 3.1.5 | 关键内容不依赖 JS 渲染 | View Page Source 可读正文 | 禁用 JS 后访问核心页 | **P0** | ✅ |
| 3.1.6 | 无登录墙/付费墙阻断 AI 爬虫 | 匿名 + 爬虫 UA 可读正文 | `curl -A "GPTBot" -s <url>` | **P1** | ✅ |

### 3.2 robots.txt 与爬虫策略

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 3.2.1 | robots.txt 返回 200 text/plain | 可访问且非空 | `curl -sI https://miaoda.io/robots.txt` | **P0** | ✅ |
| 3.2.2 | AI 搜索/引用爬虫 Allow | OAI-SearchBot、PerplexityBot、Claude-SearchBot、Claude-User 均 Allow | 检查 robots.txt | **P0** | ✅ |
| 3.2.3 | AI 训练爬虫 Disallow | GPTBot、ClaudeBot、CCBot、Bytespider、Meta-ExternalAgent 已 Disallow | 检查 robots.txt | **P1** | ✅ |
| 3.2.4 | **Google-Extended 改为 Allow 或按需** | 当前 Disallow 会限制 Google 侧 AI（Gemini/AI Overviews）对内容的训练与引用 | robots.txt `User-agent: Google-Extended` | **P1** | ❌ |
| 3.2.5 | **Content-Signal 声明** | 加 `Content-Signal: search=yes, ai-input=yes, ai-train=no` | `curl -s .../robots.txt \| findstr /i content-signal` | **P1** | ❌ |
| 3.2.6 | `Sitemap:` 声明正确 | 指向 miaoda.io sitemap（已正确） | 检查 robots.txt | **P0** | ✅ |
| 3.2.7 | CDN/WAF 不拦 AI 爬虫 | 各 AI UA 不返回 403/质询页 | 各 UA 抓取测试 | **P1** | ✅ |
| 3.2.8 | 无地理 302 重定向坑 | AI 爬虫拿到完整内容 | 抓取跳转链检查 | **P1** | ✅ |
| 3.2.9 | **双域 robots 一致性** | medo.dev 的 robots 与 miaoda.io 策略不冲突（medo.dev 现有 `Disallow: /apps/`，与主站营销页并存需确认意图） | 分别抓取两域 robots.txt | **P1** | ⚠️ |

### 3.3 Sitemap

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 3.3.1 | `/sitemap.xml` 返回 XML | 非 HTML 空壳（已达标） | `curl -sI https://miaoda.io/sitemap.xml` | **P0** | ✅ |
| 3.3.2 | Sitemap 含 hreflang 标注 | 每 URL 12 语言 `xhtml:link`（已达标） | `curl -s .../sitemap.xml \| findstr /i hreflang` | **P0** | ✅ |
| 3.3.3 | Sitemap 覆盖完整 | 首页/pricing/features/templates/showcase/solutions/blogs/events/programs（当前 176 URL，需确认 blogs 仅 3 篇是否够） | 统计 `<loc>` | **P1** | ⚠️ |
| 3.3.4 | **Sitemap 单文件 vs Index** | 176 URL 未超限，但随内容增长应评估 Sitemap Index 拆分（当前单文件可接受） | 文件体积/URL 数 | **P2** | ✅ |
| 3.3.5 | lastmod 真实 | 与页面实际更新一致（当前 lastmod=2026-08-13 全站同日，需确认是否实质更新） | 抽查对比 | **P1** | ⚠️ |
| 3.3.6 | GSC/Bing 已提交 sitemap | 后台显示成功 | GSC → Sitemaps | **P1** | **?** |

---

## 四、第二部分 · 内容可引用性（AI 能不能摘出好答案）

> 核心原则：结论前置、段落可独立理解、实体清晰、时间语境明确。MeDo Blog 已内建 BLUF / Extractability 体系。

### 4.1 Blog 文章（✅ 已达标，保留维护项）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 |
|---|--------|---------|---------|--------|
| 4.1.1 | TL;DR 直接回答 primary intent | 40–60 词；首 bullet 为 snippet 定义句 | extractability-checklist B1 | **P1** |
| 4.1.2 | 每个 H2 首段先答后铺 | 无「In today's…」式延迟 | 抽查 3 篇 | **P1** |
| 4.1.3 | 段落可独立摘引 | 随机抽 3 段，单段可答一个子问题 | Chunk 独立检查 | **P1** |
| 4.1.4 | FAQ 首句即答、非复制正文 | 每题首句直接回答，相似度 <30% | B3 检查 | **P1** |
| 4.1.5 | 时间语境明确 | 价格/政策 claim 写「as of {month} {year}」 | A2 Gate | **P1** |
| 4.1.6 | 统计数据有来源 | P0 claim 有 attribution | G3 Gate | **P2** |

### 4.2 营销页与 FAQ（✅ 已上线，转为验证/优化）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 4.2.1 | Pricing 计费 FAQ 与现网一致 | Free 500/月 + 100 日登录 / Pro $18 / 2000 credits；数值注明 as-of | 对照现网 | **P1** | ✅ |
| 4.2.2 | 首页 FAQ 可摘引 | 6 题 40–80 词、首句直答 | 对照首页 | **P1** | ✅ |
| 4.2.3 | 对比页客观可摘引 | 对比表 + FAQ；含竞品优势（A3） | 抽查 comparisons | **P1** | ✅ |
| 4.2.4 | **Affiliate 页薄内容修复** | `/programs/affiliate` 3.5KB → 补齐 FAQ/条款/收益说明（AI 常被问 MeDo affiliate） | 抓取检查体积 | **P1** | ❌ |
| 4.2.5 | **Solutions 页内容充实** | `/solutions` 11.7KB 偏薄 → 每方案独立可摘引段落 | 抓取检查 | **P2** | ⚠️ |
| 4.2.6 | 多语言内容质量 | 12 语言非机器直译空洞；中文版承接中文 AI 问询 | 抽查 zh-CN vs en | **P1** | ⚠️ |

### 4.3 内容新鲜度（GEO 最强实证信号）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 |
|---|--------|---------|---------|--------|
| 4.3.1 | 高价值页面定期实质更新 | 30–60 天内更新（实证：Perplexity 引用 30 天内内容 3.2x） | 抽查 dateModified | **P1** |
| 4.3.2 | dateModified 真实 | 仅实质更新时改；展示只显示一个日期 | Blog skill 日期策略 | **P1** |
| 4.3.3 | evergreen 维护节奏 | 5 周不维护内容 AI 可见性可能下降 | 月度 audit | **P2** |

---

## 五、第三部分 · 结构化数据（Schema / JSON-LD）

> 实证：含 Schema 页面 AI 信息提取准确率 16%→54%；含 Schema+FAQ 站点 AI 引用 +44%；作者 Schema 使被引用概率提高 3x。**miaoda.io 的 Schema 已基本完整，本部分为补齐与验证。**

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 5.1 | 首页 Organization + WebSite + SoftwareApplication | `@id` 用 miaoda.io（已达标） | 首页源码 | **P0** | ✅ |
| 5.2 | **Organization 补 legalName + sameAs** | 现缺；补 `legalName: Sailai Private Limited` + `sameAs`（PH、MIAODA docs、GitHub 等） | 对照 schema-spec 附录 A | **P1** | ❌ |
| 5.3 | **Organization 补 contactPoint** | schema-spec 附录 A 含 `Admin@medo.dev`；现网缺 | 对照附录 A | **P2** | ❌ |
| 5.4 | Blog 用 BlogPosting | headline ≤110；日期 ISO 8601 含时区；author+Person（已达标） | 抽查 3 篇 | **P0** | ✅ |
| 5.5 | FAQ 区块 → FAQPage | 问答与 DOM 逐字一致（首页 6 / pricing 7 / 对比 5 已达标） | 对照 schema-spec 附录 D | **P1** | ✅ |
| 5.6 | BreadcrumbList | 内容页有、首页无（已达标） | Rich Results Test | **P1** | ✅ |
| 5.7 | Pricing 用 SoftwareApplication + AggregateOffer | 已达标（非 Product） | 对照 E3 | **P1** | ✅ |
| 5.8 | Templates 页 Schema | CollectionPage/ItemList + SoftwareApplication（需确认） | 抓取验证 | **P1** | **?** |
| 5.9 | 各语言页 inLanguage 正确 | en-US / zh-CN 等 | 抽查 zh-CN | **P0** | ✅ |
| 5.10 | JSON-LD 单块无冲突 | Rich Results Test 无 error | Rich Results Test | **P0** | ✅ |

---

## 六、第四部分 · AI 爬虫治理与数据许可

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 6.1 | OAI-SearchBot 允许 | ChatGPT Search 展示（已达标） | robots + 日志 | **P0** | ✅ |
| 6.2 | PerplexityBot 允许 | Perplexity 索引构建（已达标） | robots.txt | **P0** | ✅ |
| 6.3 | Claude-SearchBot / Claude-User 允许 | Claude 联网（已达标） | robots.txt | **P1** | ✅ |
| 6.4 | **Google-Extended 改为 Allow** | 现为 Disallow——限制 Gemini/AI Overviews 侧引用 | robots.txt | **P1** | ❌ |
| 6.5 | 服务器日志识别 AI 爬虫 | 记录各 AI UA 访问，与答案出现互补验证 | 日志分析 | **P1** | **?** |
| 6.6 | 「被爬 ≠ 被引」认知对齐 | 监测时区分指标 | — | **—** | ✅ |

---

## 七、第五部分 · 索引通知与收录

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 7.1 | GSC 建立 miaoda.io 属性 | 域名验证 + sitemap 提交（medo.dev 有 verification meta，miaoda.io 需确认） | GSC 后台 | **P0** | **?** |
| 7.2 | Bing Webmaster 验证 | 提交 sitemap；IndexNow 可配 | Bing 后台 | **P1** | **?** |
| 7.3 | IndexNow 配置 | `{key}.txt` 200 + 提交流程自动化 | `curl -sI https://miaoda.io/{KEY}.txt` | **P1** | **?** |
| 7.4 | Google Indexing API | GSC 服务账号 Owner（可选增强） | Actions 状态 | **P2** | **?** |
| 7.5 | noindex 与 Sitemap 不矛盾 | noindex 页不在 Sitemap | 交叉检查 | **P0** | ✅ |
| 7.6 | **双域索引边界** | medo.dev 营销镜像 canonical → miaoda.io（blog 已做，pricing/comparisons 未同步） | GSC 属性对比 | **P1** | ❌ |

---

## 八、第六部分 · AI 代理就绪（Agent-Ready）

> 参照 Cloudflare isitagentready（详见通用知识库 GEO/08）。MeDo 属「内容/Blog + SaaS 平台」混合，已比多数站做得好，仍有明显缺口。

### 8.1 基础可发现性

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 8.1.1 | robots + sitemap 双备 | AI 代理可发现全站（已达标） | — | **P0** | ✅ |
| 8.1.2 | **Link 响应头** | 首页/关键页返回 `Link:` 头含 `rel="sitemap"` + RSS/Markdown alternate | `curl -sI https://miaoda.io/ \| findstr /i link` | **P1** | ❌ |
| 8.1.3 | **Content-Signal** | robots.txt 声明 `search=yes, ai-input=yes, ai-train=no` | robots.txt | **P1** | ❌ |

### 8.2 内容消费友好

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 8.2.1 | **/llms.txt 链接域修正** | 内容链接 `https://medo.dev/...` → `https://miaoda.io/...`；与 sitemap canonical 一致 | 读 llms.txt | **P1** | ❌ |
| 8.2.2 | **llms.txt 内容更新** | 数字 "10,000+" → 与现网 17,000+ 一致；补 Integrations/Components/Events/Programs 链接 | 读 llms.txt | **P1** | ❌ |
| 8.2.3 | **llms.txt Blog 列表与 sitemap 对齐** | llms.txt 列 4 篇 blog 与 sitemap 3 篇不一致 | 交叉比对 | **P2** | ❌ |
| 8.2.4 | medo.dev/llms.txt 返回文本 | head 已声明 alternate 但实际返回 HTML 空壳 | `curl -sI https://medo.dev/llms.txt` | **P1** | ❌ |
| 8.2.5 | medo.dev/skill.md 返回 Markdown | AI 指引实际可读 | `curl -sI https://medo.dev/skill.md` | **P1** | ❌ |
| 8.2.6 | Markdown 内容协商（可选） | `Accept: text/markdown` 返回干净 Markdown | curl 测试 | **P2** | **?** |
| 8.2.7 | HTML head 声明 markdown alternate | `<link rel="alternate" type="text/markdown">` | 抓取 head | **P2** | ⚠️ |
| 8.2.8 | `/sitemap.md`（可选） | 人类+AI 可读站点地图 | 访问检查 | **P2** | **?** |
| 8.2.9 | Vary: Accept（若做协商） | CDN 按 Accept 缓存 | 响应头 | **P2** | **?** |

### 8.3 平台能力发现（SaaS 侧）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 8.3.1 | API Catalog（如提供公开 API） | `/.well-known/api-catalog`（RFC 9727） | 访问检查 | **P2** | **?** |
| 8.3.2 | MCP Server / Agent Skills（可选） | medo.dev 已有 `skill.md` 理念，可评估升级 | 按需 | **P2** | **?** |

> **注意**：isitagentready 评分 ≠ GEO 效果；不做的事比做的事更重要——勿部署空 MCP Card / 伪 OAuth。

---

## 九、第七部分 · 第三方分发与引用来源

> 实证：Reddit 为多引擎最高频引用域；YouTube 在 Perplexity/Google AI Overviews 权重高；LinkedIn 专业类查询下为第一被引域。MeDo 重点在**评测/对比/教程/社区**。

| # | 检查项 | 通过标准 | 验证方法 | 优先级 |
|---|--------|---------|---------|--------|
| 9.1 | 权威第三方收录 | Product Hunt、G2、Capterra、GetApp 等 AI 工具目录 | 站点抽查 | **P1** |
| 9.2 | 对比内容可被引用 | /comparisons 各页 AI 可摘录（已上线） | 对照 A3 | **P1** |
| 9.3 | Reddit/社区讨论 | r/vibecoding、r/SaaS 等真实讨论或官方参与（勿刷） | site:reddit.com | **P2** |
| 9.4 | LinkedIn 职业实体 | 公司页 + 作者档案与官网一致 | 搜索 AI 答案 | **P2** |
| 9.5 | YouTube 教程 + 详细描述 | ≥200 词描述 + 手动字幕（描述长度 r=0.31 最强驱动） | 频道抽查 | **P2** |
| 9.6 | 评测/媒体回链 | 评测文与官网互链、UTM 统一 | 检查 UTM | **P2** |
| 9.7 | 分发内容与官网口径一致 | 第三方片段不与官网矛盾 | 对照事实表 | **P1** |

---

## 十、第八部分 · 品牌实体一致性

> AI 答案需要「可验证、不分裂」的品牌实体。MeDo 品牌链：MeDo / miaoda.io / medo.dev / MeDo by Baidu / MIAODA。

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 10.1 | **域名关系定版** | miaoda.io（主）+ medo.dev（产品）关系单一权威表述；营销页 canonical 一律 miaoda.io | 检查页面互链 | **P0** | ❌ |
| 10.2 | 全名拼写跨平台一致 | MeDo / Sailai Private Limited / miaoda.io 在官网/PH/文档一致 | 抽查 | **P1** | ⚠️ |
| 10.3 | Organization legalName + sameAs | 补入 Schema（现缺） | schema-spec 附录 A | **P1** | ❌ |
| 10.4 | 品牌关系口径统一 | MeDo by Baidu / MIAODA 单一权威表述 | 对照 medo.md R6 | **P1** | ⚠️ |
| 10.5 | 定价信息可验证 | credits 与现网 Pricing + FAQ 一致 | /pricing 抽查 | **P1** | ✅ |
| 10.6 | 联系方式公开 | contactPoint 入 Schema | 对照附录 A | **P2** | ❌ |

---

## 十一、第九部分 · 监测与测量

> 核心原则：区分「被提（mention）」与「被引（citation with link）」；区分引擎；多次采样勿单次下结论。

### 11.1 手工抽样（基础）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 |
|---|--------|---------|---------|--------|
| 11.1.1 | 建立 20–50 核心提示词 | 品牌词（MeDo）+ 品类词（AI app builder）+ 竞品（vs lovable）+ 行业问题 | 参照 keywords | **P0** |
| 11.1.2 | 按月多引擎抽样 | AI Overviews/AI Mode、ChatGPT、Perplexity、Gemini、Copilot | 记录出现/来源域名 | **P0** |
| 11.1.3 | 记录品牌出现类型 | 带链接引用 vs 纯提及 vs 错误信息 | 答案快照 | **P1** |
| 11.1.4 | 竞品共现监测 | 同 prompt 下 Lovable/Bolt 出现而 MeDo 缺席 | 对照分析 | **P1** |
| 11.1.5 | 中文生态单独抽样 | 百度 AI、豆包、Kimi、秘塔（百度关联 + 现网中文站） | 手工/定制 | **P2** |

### 11.2 工具辅助

| # | 检查项 | 通过标准 | 验证方法 | 优先级 |
|---|--------|---------|---------|--------|
| 11.2.1 | GA4 AI 流量追踪 | ChatGPT/Perplexity referrer 单独成渠道 | 参照 AI 流量正则 | **P1** |
| 11.2.2 | GSC AI 倾向查询过滤 | 5W/H 正则观察 | GSC Filter | **P2** |
| 11.2.3 | 第三方监测工具（可选） | Profound / Semrush / Otterly 等 ≥5 引擎 | 选型接入 | **P2** |
| 11.2.4 | AI 引荐流量单列 | 与答案内引用率分开看 | 周报双轨 | **P1** |

---

## 十二、第十部分 · 页面与内容规划（AI 引用承接载体）

> AI 答案引用的是「一个 URL」。miaoda.io 页面基本齐备，本节为补齐与优化。

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 12.1 | /pricing 为 AI 定价答案主承接 | 独立 SSR + 计费 FAQ（已达标） | 对照现网 | **P0** | ✅ |
| 12.2 | 对比页拦截「X vs Y」问询 | 4+ 对比页独立 URL + FAQ（已上线） | 抽查 | **P1** | ✅ |
| 12.3 | Templates 承接长尾 | 模板页即长尾词（task management 等） | 抽查 | **P1** | ✅ |
| 12.4 | Showcase / Use Cases | 结构化案例库利于 citation | 抽查 | **P2** | ⚠️ |
| 12.5 | **Affiliate 页充实** | 3.5KB → 补 FAQ/条款 | 抓取 | **P1** | ❌ |
| 12.6 | /faq 聚合页（可选） | 8–15 题覆盖产品类 | 对照 schema-spec | **P2** | **?** |
| 12.7 | Blog 高频 AI 问题选题 | sitemap 仅 3 篇 blog——扩量 + 与 AI 答案意图对齐 | content-graph 排期 | **P1** | ⚠️ |
| 12.8 | 品牌词+描述符承接页 | me do app builder 等 | GSC 品牌词分析 | **P2** | **?** |

---

## 十三、第十一部分 · 中文生态（可选，百度关联 + 现网中文站）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 |
|---|--------|---------|---------|--------|:----:|
| 13.1 | 百度搜索资源平台验证 | miaoda.io 在百度站长平台 | 百度后台 | **P2** | **?** |
| 13.2 | 百度系内容承接 | 百科/百家号/知乎与官网口径一致 | 抽查 | **P2** | **?** |
| 13.3 | 中文 AI 平台抽样 | 豆包/Kimi/元宝/秘塔问询 MeDo | 手工抽样 | **P2** | **?** |
| 13.4 | 中文版承接中文问询 | /zh-CN 非机器直译，承接「AI 建站工具」类 | 抽查 zh-CN | **P1** | ⚠️ |

---

## 十四、优先级汇总执行序列

### 第一梯队（P0 · 本月 · 双域一致性止血）

1. **营销页 canonical 全部定版 miaoda.io**：medo.dev 上的 `/pricing`、`/comparisons/*` 等空壳镜像要么 SSR 同步、要么 301/canonical 到 miaoda.io
2. **llms.txt 修正**（miaoda.io）：链接域 medo.dev → miaoda.io；数字 "10,000+" → 现网 17,000+；补 Integrations/Components/Events/Programs
3. **medo.dev/llms.txt + skill.md 返回真实文本**：当前 HTML 空壳是 agent-ready 的硬伤
4. **Google-Extended 改为 Allow**：解锁 Google 侧 AI（Gemini/AI Overviews）引用
5. **robots.txt 加 Content-Signal**：`search=yes, ai-input=yes, ai-train=no`
6. **GSC 建立 miaoda.io 属性**：域名验证 + sitemap 提交（需后台确认）
7. **建立 20–50 提示词库 + 首次全引擎快照**（基线）

### 第二梯队（P1 · 本季度 · 内容与结构）

8. Organization Schema 补 legalName + sameAs + contactPoint
9. `/programs/affiliate` 薄内容修复（补 FAQ/条款）
10. Blog 扩量（当前 sitemap 仅 3 篇）+ 高频 AI 问题选题
11. 首页/关键页 Link 响应头（rel="sitemap" + RSS）
12. GA4 AI 流量渠道 + 月度抽样复盘制度化
13. 权威第三方收录（G2/Capterra 等）+ YouTube 教程体系

### 第三梯队（P2 · 持续 · 优化）

14. Solutions 页充实、llms.txt Blog 列表与 sitemap 对齐
15. Markdown 内容协商 + sitemap.md
16. LinkedIn/Wikipedia/Reddit 实体与内容
17. 中文生态深化（百度平台 + 中文 AI 抽样）
18. 答案纠错 SOP

---

## 十五、本次实测附录（2026-08-14）

### A. 响应头快照

| URL | HTTP | Content-Type | 体积 | 结论 |
|-----|:----:|--------------|-----:|------|
| https://miaoda.io/ | 200 | text/html; utf-8 | 198,890 | SSR 完整 |
| https://miaoda.io/pricing | 200 | text/html | 180,437 | SSR + 完整 Schema |
| https://miaoda.io/zh-CN | 200 | text/html | 198,063 | 中文版 SSR |
| https://miaoda.io/zh-CN/pricing | 200 | text/html | 178,990 | 中文 pricing SSR |
| https://miaoda.io/comparisons/lovable | 200 | text/html | 205,224 | SSR + FAQPage |
| https://miaoda.io/templates | 200 | text/html | 28,083 | SSR |
| https://miaoda.io/blogs/what-is-vibe-coding | 200 | text/html | 195,060 | SSR + BlogPosting |
| https://miaoda.io/sitemap.xml | 200 | application/xml | 188,934 | 176 URL + hreflang |
| https://miaoda.io/llms.txt | 200 | text/plain | 2,232 | 存在但链接域错误 |
| https://miaoda.io/robots.txt | 200 | text/plain | 518 | 检索 Allow / 训练 Disallow |
| https://medo.dev/ | 200 | text/html | 8,852 | 产品工作区入口 |
| https://medo.dev/pricing | 200 | text/html | 6,552 | **SPA 空壳** |
| https://medo.dev/comparisons/lovable | 200 | text/html | 6,552 | **SPA 空壳** |
| https://medo.dev/llms.txt | 200 | text/html | 6,552 | **非文本，空壳** |
| https://medo.dev/skill.md | 200 | text/html | 6,552 | **非 Markdown，空壳** |
| https://medo.dev/templates | 200 | text/html | 242,729 | SSR 完整 |
| https://medo.dev/blogs/what-is-vibe-coding | 200 | text/html | 195,060 | SSR + canonical→miaoda.io |
| https://miaoda.io/zh | 404 | — | — | 正确路径为 /zh-CN |
| https://miaoda.io/en | 307 | — | — | 重定向到 / |
| https://miaoda.io/blog/ | 308 | — | — | 正确路径为 /blogs |

### B. 首页 Schema 提取

```json
{"@type":"Organization","@id":"https://miaoda.io/#organization","name":"MeDo","url":"https://miaoda.io","inLanguage":"en-US","logo":{"@type":"ImageObject","url":"https://miaoda.io/_next/static/media/logo-icon.0hbw6brpp5d52.svg"}}
{"@type":"WebSite","@id":"https://miaoda.io/#website","url":"https://miaoda.io","name":"MeDo","alternateName":["MeDo AI","miaoda.io"],"inLanguage":"en-US","publisher":{"@id":"https://miaoda.io/#organization"}}
{"@type":"SoftwareApplication","@id":"https://miaoda.io/#software","name":"MeDo","url":"https://miaoda.io","inLanguage":"en-US","description":"AI app builder that turns natural language into production-ready full-stack web and mobile applications..."}
```
> ⚠️ Organization 缺 `legalName`、`sameAs`、`contactPoint`（对照 schema-spec 附录 A）。

### C. robots.txt 现状（miaoda.io）

```
User-Agent: *
Allow: /
Disallow: /api/ /_next/ /static/ /projects/ /plugin/

User-Agent: OAI-SearchBot / PerplexityBot / Claude-SearchBot / Claude-User
Allow: /

User-Agent: GPTBot / ClaudeBot / Google-Extended / CCBot / Bytespider / Meta-ExternalAgent
Disallow: /

Sitemap: https://miaoda.io/sitemap.xml
```
> ⚠️ Google-Extended 被 Disallow（建议 Allow）；无 Content-Signal 行。

### D. llms.txt 现状（miaoda.io，需修正）

- 所有链接指向 `https://medo.dev/...`（应改为 miaoda.io）
- Key Facts 写 "10,000+ apps"（现网营销为 17,000+）
- Blog 列 4 篇，与 sitemap 实际 3 篇不一致
- 缺 Integrations / Components / Events / Programs 链接

---

## 十六、验证命令备忘

```bash
# 检查是否 SPA 空壳
curl -s https://miaoda.io/pricing | findstr /C:"root"

# AI 爬虫可读性
curl -s -A "GPTBot" https://miaoda.io/blogs/what-is-vibe-coding

# robots.txt AI 规则
curl -s https://miaoda.io/robots.txt | findstr /i "searchbot perplexity content-signal google-extended"

# llms.txt 类型与内容
curl -sI https://miaoda.io/llms.txt
curl -s https://miaoda.io/llms.txt

# Link 头
curl -sI https://miaoda.io/ | findstr /i "link"

# sitemap hreflang
curl -s https://miaoda.io/sitemap.xml | findstr /i hreflang

# 首页 Schema
curl -s https://miaoda.io/ | findstr /i "ld+json"

# medo.dev 镜像空壳检查
curl -sI https://medo.dev/pricing | findstr /i "HTTP content-length"
curl -sI https://medo.dev/llms.txt | findstr /i "HTTP content-type"
```

---

## 站内关联

[medo-indexing-diagnosis.md](./archive/medo-indexing-diagnosis.md)（medo.dev 旧站收录诊断——方法论复用）· [medo-schema-spec.md](./archive/medo-schema-spec.md)（JSON-LD——`@id` 已切 miaoda.io，legalName/sameAs 待补）· [medo-indexing-api-indexnow-guide.md](./archive/medo-indexing-api-indexnow-guide.md)（通知 API——host 用 miaoda.io）· [medo-keywords.md](./medo-keywords.md)（关键词与 GEO 建议）· [medo-site-structure.md](./medo-site-structure.md)（页面规划）· [medo-growth-strategy.md](./archive/medo-growth-strategy.md)（渠道）· [medo-blog-article/SKILL.md](./skills/medo-blog-article/SKILL.md)（内容管线）· [通用知识库 GEO 目录](../../通用知识库/01-知识/GEO/01-GEO-基础概念与策略框架.md)（方法论）

---

*MeDo GEO Checklist · v2.0 · 2026-08-14 · 基于 miaoda.io / medo.dev 实际抓取核对。现状：营销站 SEO/GEO 基座已相当完整，主要缺口集中在「双域一致性」（llms.txt 链接域、medo.dev 空壳镜像）与「代理就绪增强」（Content-Signal、Link 头、Google-Extended）。各厂商 AI 引用与爬虫策略以官方当期文档为准。*
