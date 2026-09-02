# -*- coding: utf-8 -*-
"""Write restructured submit-website ZH/EN + JSON sidecars."""
import json
import os
import re

BASE = r"E:\自有部署项目\alignify production"

ZH_MD = r'''---
title: "如何向 Google Search Console 提交网站与社媒账号：验证、站点地图与 Bing"
description: "GSC 提交完整指南：Website（Domain/URL-prefix）验证、Platform 社媒 OAuth（2026）、站点地图、URL 检查与 Bing Import。区分监控通道与收录，免费。"
slug: "submit-website"
date: "2025年2月13日"
updated: "2026年9月1日"
readingMinutes: "8 分钟阅读"
pageUrl: "https://alignify.co/zh/seo/submit-website"
locale: "zh"
pillar: "seo"
section: "technical"
contentType: "how-to"
---
<!-- block:section -->
## 提交与收录：先搞清你在做什么 {#submit-vs-index}

向 Google Search Console（GSC）**添加 property**，是在告诉 Google「我有权查看这份搜索数据，并提供一个发现 URL 的通道」。它**不会**自动把全站每一页塞进索引，也**不会**直接提升排名。页面仍须被 Googlebot 抓取、通过质量与重复判断后，才有机会出现在搜索结果中——三阶段原理见 **[搜索引擎如何工作](/zh/seo/how-search-engine-works)**。

许多团队把「提交网站」和「让页面被收录」混为一谈：域名验证通过后，GSC 可能很快出现首页数据，但深层 URL 若缺少内链或 sitemap，仍可能长期处于「已发现—未抓取」状态。正确预期是：**提交 = 开通监控 + 辅助发现**；收录与排名是后续流水线问题，排查路径见 **[网站索引](/zh/seo/website-indexing)**。

本文按**读者实际任务**组织：先选对 property 类型 → 完成验证 → 提交 sitemap / 请求单页索引 → 并行 Bing；若你运营 Instagram、TikTok、X 或 YouTube，后半部分说明 2026 年新增的 **Platform property**（OAuth 连接，与网站验证并行、数据独立）。

<!-- block:section -->
## GSC 三种 property：一张表看懂 {#gsc-property-overview}

2026 年的 GSC 里，「提交」不再只有网站一种形态。按你持有的资产选类型，验证方式与后续动作完全不同。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Property 类型</th><th>绑定对象</th><th>验证方式</th><th>典型后续动作</th></tr></thead><tbody><tr><td><strong>Domain</strong></td><td>整域（全部子域 + 协议 + 路径）</td><td>DNS TXT / CNAME</td><td>提交 sitemap、URL Inspection</td></tr><tr><td><strong>URL-prefix</strong></td><td>单一前缀（如 <code>https://www.example.com/</code> 或 <code>/shop/</code>）</td><td>DNS、HTML 文件、meta、GA、GTM</td><td>同上，仅覆盖前缀内 URL</td></tr><tr><td><strong>Platform</strong>（2026-07）</td><td>单个 IG / TikTok / X / YouTube 账号</td><td>平台 OAuth 登录授权</td><td>读 Performance / Insights；<strong>无</strong> sitemap、无 Request indexing</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

**关键规则**：每添加一个 property，就生成**一套独立的 verification token**（OAuth 除外）。不可把同一串 meta 或 DNS 值复用到另一个 property——验证会失败。Website 与 Platform **可同时存在**，报表互不合并；全球还有哪些站长工具、何时叠加区域引擎，见 **[全球搜索引擎版图](/zh/seo/search-engine)** 中的站长工具分层。

<!-- block:section -->
## Website property：Domain 与 URL-prefix {#website-property-types}

**Domain property** 填根域（如 `example.com`），覆盖 `https://www.`、`https://m.`、`http://` 及全部路径。验证**仅支持 DNS**（TXT 或 CNAME），但一条记录通常管全站——改版、换 CMS 后仍有效，是长期运维成本最低的选择。

**URL-prefix property** 填完整前缀（须含协议；路径前缀须写全，`/en/` 与 `/es/` 各算一个）。覆盖范围严格限定在该前缀之下：`https://blog.example.com/` 不含 `www.example.com`。验证方式更灵活：HTML 文件、`<head>` meta、Google Analytics / Tag Manager、或 DNS 均可。若 URL-prefix 用 DNS 验证成功，Google 会**同时**赋予 Domain 级验证能力。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>粒度</th><th>填法示例</th><th>验证代码套数</th><th>包含</th><th>不包含</th></tr></thead><tbody><tr><td>整域</td><td>Domain <code>example.com</code></td><td><strong>1</strong> 条 DNS</td><td>全部子域与路径</td><td><code>example.org</code> 等其他域</td></tr><tr><td>单子域</td><td><code>https://blog.example.com/</code></td><td><strong>1</strong> 套</td><td><code>blog.example.com/*</code></td><td><code>www.example.com</code></td></tr><tr><td>单路径</td><td><code>https://example.com/shop/</code></td><td><strong>1</strong> 套</td><td><code>/shop/a</code>、<code>/shop/b</code></td><td><code>/blog/</code></td></tr></tbody></table></div>
<!-- childrenHtml:end -->

补充：`http` 与 `https` 在 URL-prefix 模式下各需独立 property；父 URL-prefix 已验证时，其子路径 prefix **有时**可自动验证，但 Domain `example.com` **不会**自动覆盖独立 Domain `blog.example.com`。

<!-- block:section -->
## 如何选 Website property：决策路径 {#choose-website-property}

按下面顺序做选择，可避免最常见的「验证通过但数据范围不对」问题。

**第一步：能否改 DNS？** 能 → 优先 **1× Domain property**，一条 TXT 覆盖全站 KPI；报表内仍可用 Performance 过滤器按 hostname 或路径拆分，不必为 KPI 拆多个 prefix。**不能改 DNS、只能改页面代码** → 为**每一个**需要监控的 URL-prefix 各 Add 一次，各用一套 token。

**第二步：是否要拆 KPI？** 主站与博客子域分开考核时，可选 1× Domain（统一看）或 2× URL-prefix（各管各的 meta）。多语言 `/en/`、`/es/` 若路径规则清晰，1× Domain + 过滤器通常足够；若团队按目录分权，拆 prefix 则**每个路径一条验证串**。

**第三步：`http` 与 `https` 并存？** 优先 Domain 一把收；否则至少 2× URL-prefix，且各需独立验证。

若 `www` 与 `blog` 各建一个 URL-prefix property，首页 `<head>` 可并存两个 meta，**内容必须不同**：

<!-- childrenHtml:start -->
<div class="content-html"><pre><code>&lt;!-- Property A：https://www.example.com/ --&gt;
&lt;meta name="google-site-verification" content="AAAAAA...token_A" /&gt;
&lt;!-- Property B：https://blog.example.com/ --&gt;
&lt;meta name="google-site-verification" content="BBBBBB...token_B" /&gt;</code></pre></div>
<!-- childrenHtml:end -->

有 DNS 权限时，我通常建议客户直接 Domain 验证：一条 TXT 比多环境维护多串 meta 更不易在 deploy 时被误删。多人协作时，**勿覆盖**他人已生效的 token；Settings → Ownership verification 可叠加 ≥2 种方法，防止某次发布删掉唯一验证文件。

<!-- block:section -->
## 验证网站所有权：方法与常见失败 {#verify-website-ownership}

流程固定四步：打开 [search.google.com/search-console](https://search.google.com/search-console) → **+ 添加资源** → 选 **Website** → Domain 或 URL-prefix → 选验证方式 → **验证**（可先 Verify later 暂存，但数据权限以验证通过为准）。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>方法</th><th>适用</th><th>核心要求</th><th>常见失败原因</th></tr></thead><tbody><tr><td><strong>DNS TXT</strong></td><td>Domain；URL-prefix 可选</td><td>Host=<code>@</code>；值含 <code>google-site-verification=…</code></td><td>改错 DNS zone；传播未生效（常需 2–48 小时）</td></tr><tr><td><strong>DNS CNAME</strong></td><td>Domain（apex 已有 CNAME 时）</td><td>target 含 <code>dv.googlehosted.com</code></td><td>与 TXT 选错记录类型</td></tr><tr><td><strong>HTML 文件</strong></td><td>URL-prefix</td><td>根目录匿名可访问；文件名不可改</td><td>需登录才可见；<strong>不跟随跨域</strong> redirect</td></tr><tr><td><strong>HTML meta</strong></td><td>URL-prefix</td><td>前缀「首页」<code>&lt;head&gt;</code> 内</td><td>放在会 302 走的 URL；放错模板</td></tr><tr><td><strong>GA / GTM</strong></td><td>URL-prefix</td><td>同 Google 账号 + 正确 snippet 位置</td><td>旧 UA 代码；snippet 在 body</td></tr><tr><td><strong>Blogger / Sites</strong></td><td>Google 托管站</td><td>同账号</td><td>新 Sites 无自定义域时需 GA</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

**Tag 类 vs HTML 文件**：meta / GA / GTM 会跟随**同域** redirect 的终页；HTML 文件验证**不会**跟跨域跳转——这是排查「明明放了文件却失败」时的第一检查点。WordPress 可用 Site Kit 插件自动完成验证。DNS 排查可用 `nslookup -q=txt example.com 8.8.8.8` 对照 Search Console 显示的串。

验证通过后，**不要删除** DNS 记录或 meta——Google 会周期性复查，失效即失去权限。添加 property **不会改变**搜索排名；未验证前 Google 也可能已开始收集部分数据，但你看不到完整报表。

<!-- block:section -->
## 验证之后：站点地图与单页索引请求 {#after-website-verification}

Website property 验证完成，才进入「让 Google 知道有哪些 URL」的阶段。两件事分工不同：

**提交 XML 站点地图**：在站点发布可访问的 sitemap（仅列**可索引的规范 URL**）→ 用 URL Inspection 确认 Google 能 fetch → GSC **Sitemaps** 粘贴 sitemap URL → Submit。GSC **只接收 sitemap 地址，不上传文件**——本质是告知 URL 列表，加速发现，不保证收录。技术细节见 **[站点地图](/zh/seo/sitemap)**。

**请求编入索引（URL Inspection）**：对单个 URL 使用「网址检查」→ 确认可抓取 → **请求编入索引**。适合新模板上线、重大内容改版、或修复了阻断抓取的问题后。该工具有**日配额**；批量 URL 仍应靠 sitemap + **[站内链接](/zh/seo/internal-links)**，而非逐页狂点。

**等待预期**：新站或外链少的域名，全站索引常需 **1–2 周**；提交后至少观察一周再判断「失败」。Google Indexing API（招聘/直播等有限场景，约 200 URL/天）与 IndexNow（**不适用于 Google**，见下文 Bing 节）属于程序化补充，Alignify 运维文档在仓库 `skills/ops/` 中，本文不展开实施细节。

<!-- block:section -->
## Platform property：社媒与视频账号（2026） {#platform-properties}

**无需自有网站**，也可在 GSC 添加 **Platform property**：绑定单个 Instagram、TikTok、X 或 YouTube 账号，查看该账号内容在 **Google 搜索、Google Discover、Google 新闻** 中的表现。该功能于 2026 年 7 月全球可用；若界面暂未出现，属逐步 rollout，可换账号或稍后重试。

添加步骤：GSC → 资源选择器 → **Add property** → 在支持平台旁点 **Add** → 登录并授权对应社媒账号 → **Go to property**。每个 IG / TikTok / X / YouTube **账号或频道各建一个** property，不可合并。数据通常在验证后**数天**起出现，默认报告窗口 **28 天**；**无历史回填**——连接前的 Google 侧表现不可追溯。

若你已在 Google 搜索拥有 **Search profile**（公开创作者页）且已链接同一平台，GSC 有时已有数据，无需重复 OAuth——但 Search profile 与 Platform property 是不同产品（边界见下一节）。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>平台</th><th>GSC Platform property</th><th>备注</th></tr></thead><tbody><tr><td>Instagram</td><td>✅</td><td>含 Story 出现在 Google 搜索时的展示/点击</td></tr><tr><td>TikTok</td><td>✅</td><td>—</td></tr><tr><td>X</td><td>✅</td><td>—</td></tr><tr><td>YouTube</td><td>✅</td><td>可按 URL 区分 <code>/watch</code> 与 <code>/shorts/</code></td></tr><tr><td>LinkedIn / Facebook / Pinterest 等</td><td>❌</td><td>官方未列；勿按「即将支持」做规划</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Google **周期性复查** OAuth。平台侧登录过期时报告会**暂停**；重新授权后恢复，**无需**重新累积历史。请勿在 IG/TikTok 等设置里撤销 Google 的读取授权，否则 GSC 失去访问。

<!-- block:section -->
## Platform 报告读法：测什么、不测什么 {#platform-reports-and-limits}

Platform property 提供 **Performance**（点击、展示、CTR、平均排名，可按帖子 URL、查询、国家、设备筛选）、**Insights**（28 天趋势、Top 内容、query groups 涨跌）与 **Achievements**（点击里程碑）。Discover / Google 新闻维度**仅在有流量时**出现。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>会测量</th><th>不会测量</th></tr></thead><tbody><tr><td>帖子 URL 在 Google 搜索 / Discover / 新闻中的展示与点击</td><td>TikTok For You、IG 信息流、YouTube 站内推荐算法流量</td></tr><tr><td>Instagram Story 出现在 Google 搜索结果中</td><td>Story 在 IG App 内的浏览量</td></tr><tr><td>用户经 Google 内嵌播放器点击（仍计 click）</td><td>把 Platform 报表与 Website Performance <strong>简单加总</strong>（口径不同）</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Insights 顶部汇总卡含 **全 Google**（web + image + video + news）点击；下方列表明细**侧重 web search**，分项之和可能小于汇总卡——读报表时以 Help 说明为准，勿自行「凑数」。

**限制（2026-07）**：Platform 数据**暂无 Search Console API / BigQuery 导出**，周报需 GSC 界面 Export 后手工合并；**无 sitemap、无 Request indexing**——社媒 URL 由 Google 自行发现。捕捉新帖搜索 spike 可用 Performance 的 **24 hours** 过滤器；对比 Shorts vs 长视频可筛 URL 含 `/shorts/` 或 `/watch`。

<!-- block:section -->
## 三种「属性」别搞混 {#property-boundaries}

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>A</th><th>B</th><th>一句区分</th></tr></thead><tbody><tr><td><strong>Website property</strong></td><td><strong>Platform property</strong></td><td>前者证域名或 URL 前缀；后者 OAuth 社媒账号——本文前两大部分与第七部分</td></tr><tr><td><strong>Platform property</strong></td><td><strong>Search profile</strong></td><td>前者 GSC <strong>私有</strong>分析；后者 Google 搜索上<strong>公开</strong>创作者聚合页</td></tr><tr><td><strong>Search profile</strong></td><td><strong>Platform property</strong></td><td>Search profile 需美国 + ≥3.5 万粉丝等门槛；Platform property <strong>无</strong>粉丝门槛</td></tr><tr><td><strong>Add property</strong></td><td><strong>优化排名</strong></td><td>添加 property 只<strong>读取</strong>数据，不改变 Google 如何展示内容</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

<!-- block:section -->
## Bing 并行：GSC 验证后 5 分钟内 {#bing-parallel}

Bing 索引为 Yahoo、DuckDuckGo 及部分 AI 搜索提供网页结果；仅做 GSC 会在 Bing 生态形成盲区。GSC Website 验证完成后，建议在 **5 分钟内** 接入 Bing Webmaster Tools（BWT）。

**路径 A — 从 GSC 导入（推荐）**：[bing.com/webmasters](https://www.bing.com/webmasters) → **My Sites → Import** → Google 登录授权 → 勾选站点 → **Import**。须对目标站具备 GSC **Verified owner** 权限；单次最多 **100** 个站，自动完成 BWT 验证，sitemap 可同步。BWT 会周期性 sync GSC；若 GSC 失验证，须在 BWT **重新连接**。

**路径 B — 独立添加**：无 GCS 或未验证时，**Add a Site** → 填完整 URL（协议与 www 一致）→ 选手动验证（Domain Connect / meta / DNS / XML；token 与 GSC **独立、可并存**）。验证后在 BWT 提交 sitemap，并配置 **IndexNow**（Google **不支持** IndexNow）。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>维度</th><th>GSC</th><th>BWT</th></tr></thead><tbody><tr><td>从对方导入站点</td><td>❌</td><td>✅ GSC Import</td></tr><tr><td>实时 URL 变更通知</td><td>URL Inspection（有配额）</td><td><strong>IndexNow</strong></td></tr><tr><td>社媒 Platform property</td><td>✅</td><td>❌</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

区域市场（百度、Naver、Yandex）是否在 GSC/Bing 之外单独注册，取决于你的收入市场——决策框架见 **[全球搜索引擎版图](/zh/seo/search-engine)**，本文不重复各国站长工具卡片。

<!-- block:section -->
## 常见反模式 {#anti-patterns}

**把「提交 GSC」当成「会收录」**：验证通过只代表你能看数据、能交 sitemap；robots、noindex、薄内容、孤立 URL 仍会排除在索引外。读 GSC「网页」报告里的**具体原因**，勿对同一 URL 反复无效请求。

**验证后删除 token**：DNS TXT、HTML 文件或 meta 被 deploy 清掉 → 权限静默失效，Merchant Center 等跨服务也可能受影响。

**多个 URL-prefix 共用一串 verification code**：每个 property 的 token **唯一**；复用必失败。

**只做 GSC、不做 BWT**：丢失 Bing/Yahoo/DDG 及 Copilot 相关可见性信号。

**用 Platform 数据衡量 TikTok/IG 站内爆款**：指标错位——Platform 只反映 **Google 面**，不是 For You 播放量。

**等待 Platform API 做自动周报**：2026 年 7 月仍须 Export；勿因「以后会有 API」而拖延手工复盘。

<!-- block:section -->
## 结论 {#conclusion}

GSC 提交的正确顺序是：**按资产类型选对 property**（Website 的 Domain / URL-prefix，或 Platform 的 OAuth）→ **完成对应验证且勿删 token** → Website 侧 **提交 sitemap 并对 strategic URL 使用 URL Inspection** → **5 分钟内 Bing Import** → 每周看索引覆盖率与 Platform/Website 各自 Performance，而非依赖 site: 估算。

Website 与 Platform 可并行配置、数据独立：前者服务站点收录与查询分析，后者服务创作者在 Google 搜索面的可见度。收录与排名仍取决于内容、技术底座与竞争环境——提交是资格赛入场，不是终点。上线前可对照 **[SEO Checklist](/zh/seo/checklist)** 确认 robots、sitemap、HTTPS 与内链就绪后再验证，避免 Search Console 学习闭环从「不可索引」状态开始。
'''

EN_MD = r'''---
title: "Submit to Google Search Console: Websites, Social Accounts & Bing"
description: "Complete GSC setup: Website Domain/URL-prefix verification, 2026 Platform properties (IG/TikTok/X/YouTube OAuth), sitemaps, URL Inspection, and Bing Import. Monitoring vs indexing explained. Free guide."
slug: "submit-website"
date: "February 13, 2025"
updated: "September 1, 2026"
readingMinutes: "9 min read"
pageUrl: "https://alignify.co/seo/submit-website"
locale: "en"
pillar: "seo"
section: "technical"
contentType: "how-to"
---
<!-- block:section -->
## Submission vs indexing: know what you are doing {#submit-vs-index}

Adding a **property** in Google Search Console (GSC) tells Google you control a monitoring channel and a discovery path for URLs. It does **not** automatically index every page on a site, and it does **not** improve rankings. Pages still need to be crawled, evaluated, and stored before they can appear in search — see **[how search engines work](/seo/how-search-engine-works)** for the full crawl → index → serve pipeline.

Teams often confuse “submit the site” with “get pages indexed.” After domain verification, the homepage may show data quickly while deep URLs without internal links or sitemap entries can remain **discovered — not crawled** for weeks. The right expectation: **submission = monitoring + assisted discovery**; indexing and ranking are downstream problems covered in **[website indexing](/seo/website-indexing)**.

This guide follows the reader’s job in order: pick the property type → verify → submit sitemaps / request single URLs → parallelize Bing. If you run Instagram, TikTok, X, or YouTube, the second half covers **Platform properties** (OAuth, July 2026) — parallel to Website setup, separate data.

<!-- block:section -->
## Three GSC property types at a glance {#gsc-property-overview}

In 2026, “submit to GSC” is not website-only. The asset you own determines verification and next steps.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Property type</th><th>What you bind</th><th>Verification</th><th>Typical next steps</th></tr></thead><tbody><tr><td><strong>Domain</strong></td><td>Entire domain (all subdomains, protocols, paths)</td><td>DNS TXT / CNAME</td><td>Sitemap, URL Inspection</td></tr><tr><td><strong>URL-prefix</strong></td><td>One prefix (e.g. <code>https://www.example.com/</code> or <code>/shop/</code>)</td><td>DNS, HTML file, meta, GA, GTM</td><td>Same, scoped to prefix URLs only</td></tr><tr><td><strong>Platform</strong> (Jul 2026)</td><td>One IG / TikTok / X / YouTube account</td><td>Platform OAuth</td><td>Performance / Insights; <strong>no</strong> sitemap, no Request indexing</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

**Hard rule:** each property gets its **own verification token** (OAuth excepted). Never reuse the same meta tag or DNS string across properties — verification will fail. Website and Platform properties **coexist**; reports do not merge. For the global webmaster-tool map and regional consoles, see **[global search engine landscape](/seo/search-engine)**.

<!-- block:section -->
## Website properties: Domain vs URL-prefix {#website-property-types}

A **Domain property** uses the root domain (`example.com`) and covers `https://www.`, `https://m.`, `http://`, and all paths. Verification is **DNS-only** (TXT or CNAME), but one record usually governs the whole estate — resilient across redesigns and CMS migrations.

A **URL-prefix property** uses a full prefix (protocol required; path prefixes must be exact — `/en/` and `/es/` are separate). Scope is strict: `https://blog.example.com/` excludes `www.example.com`. Verification is flexible: HTML file, `<head>` meta, Google Analytics / Tag Manager, or DNS. DNS verification on a URL-prefix also grants **Domain-level** verification for that site.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Granularity</th><th>Example entry</th><th>Token sets</th><th>Includes</th><th>Excludes</th></tr></thead><tbody><tr><td>Whole domain</td><td>Domain <code>example.com</code></td><td><strong>1</strong> DNS</td><td>All subdomains &amp; paths</td><td>Other domains</td></tr><tr><td>Single subdomain</td><td><code>https://blog.example.com/</code></td><td><strong>1</strong> set</td><td><code>blog.example.com/*</code></td><td><code>www.example.com</code></td></tr><tr><td>Single path</td><td><code>https://example.com/shop/</code></td><td><strong>1</strong> set</td><td><code>/shop/a</code>, <code>/shop/b</code></td><td><code>/blog/</code></td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Note: `http` and `https` need separate URL-prefix properties. Child path prefixes may **auto-verify** when a parent URL-prefix is verified, but Domain `example.com` does **not** auto-cover Domain `blog.example.com`.

<!-- block:section -->
## Choosing a Website property {#choose-website-property}

Follow this sequence to avoid “verified but wrong scope” mistakes.

**Step 1 — Can you edit DNS?** Yes → prefer **one Domain property**; filter Performance by hostname or path instead of splitting prefixes. No DNS, page code only → **Add each URL-prefix separately**, each with its own token.

**Step 2 — Split KPIs?** Main site vs blog subdomain can use one Domain (unified) or two URL-prefix properties (separate meta tags). Multilingual `/en/` and `/es/` usually work with one Domain plus filters; split prefixes only when teams need isolated ownership — **one token per path prefix**.

**Step 3 — Both `http` and `https` live?** Prefer Domain; otherwise at least two URL-prefix properties, each verified independently.

For separate `www` and `blog` URL-prefix properties, two meta tags may sit in one `<head>` but **must differ**:

<!-- childrenHtml:start -->
<div class="content-html"><pre><code>&lt;!-- Property A: https://www.example.com/ --&gt;
&lt;meta name="google-site-verification" content="AAAAAA...token_A" /&gt;
&lt;!-- Property B: https://blog.example.com/ --&gt;
&lt;meta name="google-site-verification" content="BBBBBB...token_B" /&gt;</code></pre></div>
<!-- childrenHtml:end -->

When DNS is available, one Domain TXT beats maintaining multiple meta tags across environments — deploys often delete the wrong tag. Stack **≥2 verification methods** under Settings → Ownership verification so one release cannot wipe access. Never overwrite a teammate’s active token.

<!-- block:section -->
## Verifying Website ownership {#verify-website-ownership}

Workflow: [search.google.com/search-console](https://search.google.com/search-console) → **+ Add property** → **Website** → Domain or URL-prefix → pick a method → **Verify** (Verify later is allowed, but full data requires success).

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Method</th><th>Applies to</th><th>Requirement</th><th>Common failures</th></tr></thead><tbody><tr><td><strong>DNS TXT</strong></td><td>Domain; optional for URL-prefix</td><td>Host=<code>@</code>; value contains <code>google-site-verification=…</code></td><td>Wrong zone; propagation delay (often 2–48h)</td></tr><tr><td><strong>DNS CNAME</strong></td><td>Domain when apex uses CNAME</td><td>Target includes <code>dv.googlehosted.com</code></td><td>Wrong record type vs TXT</td></tr><tr><td><strong>HTML file</strong></td><td>URL-prefix</td><td>Anonymous fetch at root; exact filename</td><td>Login wall; <strong>no cross-domain</strong> redirect follow</td></tr><tr><td><strong>HTML meta</strong></td><td>URL-prefix</td><td>In prefix “homepage” <code>&lt;head&gt;</code></td><td>Tag on URL that redirects away</td></tr><tr><td><strong>GA / GTM</strong></td><td>URL-prefix</td><td>Same Google account; snippet placement</td><td>Legacy UA; snippet in body</td></tr><tr><td><strong>Blogger / Sites</strong></td><td>Google-hosted</td><td>Same account</td><td>New Sites without custom domain</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

**Tag vs HTML file:** meta / GA / GTM follow **same-domain** redirect destinations; the HTML file method does **not** follow cross-domain redirects — first check when “the file is there but verification fails.” WordPress Site Kit can automate verification. Probe DNS with `nslookup -q=txt example.com 8.8.8.8`.

After verification, **do not remove** DNS, files, or meta — Google rechecks periodically. Adding a property does **not** change rankings; Google may collect data before you verify, but reports stay incomplete until you pass.

<!-- block:section -->
## After Website verification: sitemaps and URL requests {#after-website-verification}

Verification unlocks “tell Google which URLs matter.” Two tools, different jobs:

**Submit an XML sitemap:** Publish a crawlable sitemap (canonical, indexable URLs only) → confirm fetch in URL Inspection → paste the sitemap URL under GSC **Sitemaps** → Submit. GSC **stores the URL reference, not the file** — discovery hint, not an indexing guarantee. Details: **[sitemap guide](/seo/sitemap)**.

**Request indexing (URL Inspection):** Inspect one URL → confirm crawlability → **Request indexing**. Use for new templates, major content refreshes, or fixed blockers. Daily **quota** applies; bulk URLs should rely on sitemaps plus **[internal links](/seo/internal-links)**, not manual spam.

**Timing:** new or low-link domains often need **1–2 weeks** for broad indexing; wait at least a week before calling failure. Google Indexing API (limited daily quota, job/broadcast use cases) and IndexNow (**not for Google** — see Bing below) are programmatic add-ons documented in ops runbooks, not repeated here.

<!-- block:section -->
## Platform properties: social and video accounts (2026) {#platform-properties}

You can add a **Platform property without owning a website**: bind one Instagram, TikTok, X, or YouTube account and see how that account’s content performs on **Google Search, Discover, and Google News**. Rolled out globally in July 2026; if unavailable, retry later — Google still describes gradual rollout.

Steps: GSC → property picker → **Add property** → **Add** next to the platform → sign in and authorize → **Go to property**. **One property per account** — no merging. Data usually appears within **days**; default window **28 days**; **no backfill** before connection.

If you already have a public **Search profile** linked to the same platform, GSC may already show data without reconnecting — Search profile and Platform property are different products (see boundaries below).

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Platform</th><th>GSC Platform property</th><th>Notes</th></tr></thead><tbody><tr><td>Instagram</td><td>✅</td><td>Includes Stories appearing in Google Search</td></tr><tr><td>TikTok</td><td>✅</td><td>—</td></tr><tr><td>X</td><td>✅</td><td>—</td></tr><tr><td>YouTube</td><td>✅</td><td>Filter <code>/watch</code> vs <code>/shorts/</code></td></tr><tr><td>LinkedIn, Facebook, Pinterest, etc.</td><td>❌</td><td>Not listed; do not plan on imminent support</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Google **rechecks OAuth**. Expired platform login **pauses** reports; re-authorization restores history — do not revoke Google’s access in the social app settings.

<!-- block:section -->
## Reading Platform reports: what counts {#platform-reports-and-limits}

Platform properties expose **Performance** (clicks, impressions, CTR, average position — filter by post URL, query, country, device), **Insights** (28-day trends, top content, query group movers), and **Achievements** (click milestones). Discover / News breakdowns appear **only when traffic exists**.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Measured</th><th>Not measured</th></tr></thead><tbody><tr><td>Post URLs on Google Search / Discover / News</td><td>TikTok For You, IG feed, YouTube home recommendations</td></tr><tr><td>Instagram Stories surfacing in Google Search</td><td>In-app Story views</td></tr><tr><td>Clicks from Google’s inline player (still counts as clicks)</td><td>Summing Platform + Website Performance blindly (different scopes)</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Insights summary cards aggregate **all Google surfaces** (web + image + video + news); detail tables skew toward **web search**, so row sums may fall below the card — read Google’s Help rather than forcing reconciliation.

**Limits (Jul 2026):** no Search Console API or BigQuery export for Platform data — weekly reviews need manual Export. **No sitemap, no Request indexing** — Google discovers social URLs on its own. Use Performance **Last 24 hours** for post-launch spikes; compare Shorts vs long-form via `/shorts/` vs `/watch` filters.

<!-- block:section -->
## Do not confuse these three “profiles” {#property-boundaries}

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>A</th><th>B</th><th>One-line distinction</th></tr></thead><tbody><tr><td><strong>Website property</strong></td><td><strong>Platform property</strong></td><td>Domain/URL-prefix verification vs OAuth social account — sections above</td></tr><tr><td><strong>Platform property</strong></td><td><strong>Search profile</strong></td><td>Private GSC analytics vs public creator page on Google Search</td></tr><tr><td><strong>Search profile</strong></td><td><strong>Platform property</strong></td><td>Search profile has US + follower thresholds; Platform property has <strong>none</strong></td></tr><tr><td><strong>Add property</strong></td><td><strong>Rank better</strong></td><td>Setup only <strong>reads</strong> data; it does not change how Google displays content</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

<!-- block:section -->
## Bing in parallel: within five minutes of GSC {#bing-parallel}

Bing powers Yahoo, DuckDuckGo, and parts of AI search surfaces — GSC-only setups miss that slice. After GSC Website verification, open Bing Webmaster Tools (BWT) within **five minutes**.

**Path A — Import from GSC (recommended):** [bing.com/webmasters](https://www.bing.com/webmasters) → **My Sites → Import** → Google sign-in → select sites → **Import**. Requires GSC **Verified owner** on those sites; up to **100** sites per import; BWT verification auto-completes; sitemaps may sync. BWT syncs periodically — if GSC verification lapses, **reconnect**.

**Path B — Standalone:** **Add a Site** with the exact URL → manual verification (Domain Connect / meta / DNS / XML; tokens **independent** of GSC). Submit sitemaps in BWT and enable **IndexNow** (Google does **not** support IndexNow).

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Dimension</th><th>GSC</th><th>BWT</th></tr></thead><tbody><tr><td>Import from the other console</td><td>❌</td><td>✅ GSC Import</td></tr><tr><td>Real-time URL ping</td><td>URL Inspection (quota)</td><td><strong>IndexNow</strong></td></tr><tr><td>Platform properties</td><td>✅</td><td>❌</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Whether to add Baidu, Naver, or Yandex beyond GSC/Bing depends on revenue markets — use **[search engine landscape](/seo/search-engine)** rather than duplicating regional console cards here.

<!-- block:section -->
## Anti-patterns {#anti-patterns}

**“Submitted to GSC” = “will be indexed”:** Verification opens monitoring; robots, noindex, thin content, and orphan URLs still exclude pages. Read the specific reason in GSC Pages before resubmitting the same URL.

**Deleting tokens after verification:** Removing DNS TXT, HTML files, or meta silently drops ownership — and can break cross-product verification.

**Reusing one verification string across URL-prefix properties:** Each property token is **unique**.

**GSC without BWT:** Blind to Bing/Yahoo/DDG and related Copilot visibility.

**Using Platform data to judge in-app virality:** Platform metrics cover **Google surfaces only**, not For You or feed views.

**Waiting for a Platform API before weekly reviews:** As of July 2026, Export is still manual.

<!-- block:section -->
## Conclusion {#conclusion}

The GSC setup sequence is: **pick the property type for each asset** (Website Domain / URL-prefix, or Platform OAuth) → **verify and keep tokens alive** → on Website properties **submit sitemaps and use URL Inspection for strategic URLs** → **Import into Bing within five minutes** → review index coverage and separate Performance reports weekly instead of trusting `site:` estimates.

Website and Platform properties run in parallel with independent data: sites for crawl/index workflows, creator accounts for Google-search visibility. Rankings still depend on content, technical foundations, and competition — submission is entry to the monitoring loop, not the finish line. Before verifying, walk **[SEO checklist](/seo/checklist)** so robots, sitemap, HTTPS, and internal links are ready — otherwise Search Console learns from a broken baseline.
'''

TLDR = {
    "/seo/submit-website": {
        "id": "article-intro",
        "title": "Key Takeaways",
        "introduction": "GSC submission opens monitoring and discovery — not guaranteed indexing. This guide covers Website verification (Domain vs URL-prefix), 2026 Platform properties for social accounts, sitemaps, URL Inspection, and Bing Import in one workflow.",
        "items": [
            "Pick the property type first: Domain (one DNS TXT), URL-prefix (one token per prefix), or Platform (OAuth per IG/TikTok/X/YouTube account).",
            "Adding a property does not index every URL; uncrawled pages still cannot rank until Googlebot fetches and stores them.",
            "After Website verification: submit an XML sitemap and use URL Inspection for strategic URLs — expect 1–2 weeks on new domains.",
            "Platform properties (Jul 2026) measure Google Search/Discover/News only — not in-app For You or feed views; no sitemap or Request indexing.",
            "Import verified sites into Bing Webmaster Tools within five minutes; IndexNow applies to Bing, not Google."
        ],
    },
    "/zh/seo/submit-website": {
        "id": "article-intro",
        "title": "核心要点",
        "introduction": "GSC 提交开通监控与发现通道，不保证收录。本文涵盖 Website（Domain/URL-prefix）验证、2026 Platform 社媒 OAuth、站点地图、URL 检查与 Bing Import 的完整路径。",
        "items": [
            "先选 property 类型：Domain（一条 DNS TXT）、URL-prefix（每前缀一套 token）、Platform（每个 IG/TikTok/X/YouTube 账号 OAuth 一次）。",
            "Add property 不自动收录全站；未被抓取的 URL 仍无法排名。",
            "Website 验证后：提交 XML 站点地图，对战略 URL 用 URL Inspection；新域常见需 1–2 周。",
            "Platform property（2026-07）只测 Google 搜索/Discover/新闻，不含站内 For You；无 sitemap、无请求编入索引。",
            "GSC 验证后 5 分钟内 Bing Import；IndexNow 仅适用于 Bing 生态，非 Google。"
        ],
    },
}

FAQ = {
    "/seo/submit-website": {
        "items": [
            {
                "question": "Should I choose Domain or URL-prefix in Search Console?",
                "answer": "If you can edit DNS, use one Domain property — a single TXT record covers all subdomains and paths. Use URL-prefix only when DNS is unavailable or you deliberately need isolated KPIs per hostname or path; each prefix requires its own verification token. Never reuse the same meta or DNS string across properties."
            },
            {
                "question": "How many verification codes do I need for multiple subdomains?",
                "answer": "One Domain property on example.com needs one DNS TXT. Separate URL-prefix properties for www and blog need two independent tokens. Splitting www and blog under one Domain still uses one DNS record if you choose Domain verification — filters handle reporting splits inside GSC."
            },
            {
                "question": "How is a Platform property different from a Website property?",
                "answer": "Website properties prove control of a domain or URL prefix via DNS, HTML, or tags, then use sitemaps and URL Inspection. Platform properties connect one social or video account via OAuth, report Google Search/Discover/News performance only, and offer no sitemap or Request indexing. They coexist with separate data — do not merge totals blindly."
            },
            {
                "question": "Does Platform data include TikTok For You or Instagram feed views?",
                "answer": "No. Platform properties measure impressions and clicks when your content URLs appear on Google Search, Discover, or News — not in-app recommendation feeds or For You pages. Use each platform’s native analytics for on-app virality; use GSC Platform for Google-surface visibility."
            },
            {
                "question": "How long does Google indexing take after GSC setup?",
                "answer": "Trusted domains may see pages within hours; new sites with few links often need one to two weeks. Sitemaps accelerate discovery, not guaranteed indexing. Track GSC Pages coverage instead of site: operators, and wait at least a week before declaring failure on new templates."
            },
            {
                "question": "How do I import Search Console sites into Bing?",
                "answer": "Within five minutes of GSC verification, open Bing Webmaster Tools → My Sites → Import → sign in with the Google account that is Verified owner → select sites → Import. Up to 100 sites per batch; BWT auto-verifies. Reconnect if GSC verification later lapses because BWT sync depends on it."
            },
            {
                "question": "Why are pages still not indexed after I verified GSC?",
                "answer": "Verification does not override blockers — robots.txt, noindex, duplicates, orphan URLs, and thin content still exclude pages. Read the specific exclusion reason in GSC Pages before repeatedly requesting the same URL. Fix SSR or template issues first; see the website indexing guide for systematic troubleshooting."
            },
        ]
    },
    "/zh/seo/submit-website": {
        "items": [
            {
                "question": "Domain 和 URL-prefix 应该怎么选？",
                "answer": "能改 DNS 时优先 1× Domain property，一条 TXT 覆盖全部子域与路径，报表内用过滤器拆分即可。只能改页面代码时，为每个需要监控的 URL-prefix 各 Add 一次，各用独立 verification token。禁止多 property 共用同一串 meta 或 DNS 值。"
            },
            {
                "question": "多个子域需要几个 verification code？",
                "answer": "Domain example.com 只需 1 条 DNS TXT。若 www 与 blog 各建 URL-prefix property，则需要 2 套独立 token。选 Domain 验证时，子域数据可在同一 property 内用 hostname 过滤，不必为拆 KPI 而拆 DNS。"
            },
            {
                "question": "Platform property 和 Website property 有何不同？",
                "answer": "Website 通过 DNS/HTML/meta 证明域名或路径控制权，验证后可提交 sitemap 与 URL Inspection。Platform 通过 OAuth 绑定单个社媒账号，只报告 Google 搜索/Discover/新闻表现，无 sitemap、无请求编入索引。两者并行、数据独立，勿简单加总。"
            },
            {
                "question": "Platform 数据包含 TikTok/IG 站内播放吗？",
                "answer": "不包含。Platform property 只统计内容 URL 出现在 Google 搜索、Discover、新闻中的展示与点击，不含 For You、信息流或 App 内浏览量。站内爆款看各平台原生后台；Google 面可见度看 GSC Platform。"
            },
            {
                "question": "提交后 Google 多久收录？",
                "answer": "高信任域可能数小时，新站少外链常见 1–2 周。站点地图加速发现，不保证收录。跟踪 GSC「网页」报告而非 site: 运算符；重大模板上线后至少观察一周再判断失败。"
            },
            {
                "question": "如何从 GSC 导入 Bing？",
                "answer": "GSC Website 验证通过后 5 分钟内打开 Bing 站长工具 → My Sites → Import → 用对该站具备 Verified owner 的 Google 账号授权 → 勾选站点 → Import。单次最多 100 站，BWT 自动验证。GSC 失验证后须在 BWT 重新连接。"
            },
            {
                "question": "验证 GSC 后页面仍不收录怎么办？",
                "answer": "验证不能覆盖 robots、noindex、重复、孤立 URL 或薄内容等阻断。在 GSC「网页」详情查看具体排除原因，勿对同一 URL 反复无效请求。先修复 SSR 或模板问题，再按网站索引专文系统排查。"
            },
        ]
    },
}

REFS = {
    "/seo/submit-website": {
        "items": [
            {
                "title": "Verify your site ownership (Search Console)",
                "url": "https://support.google.com/webmasters/answer/9008080",
                "source": "Google",
                "date": "Updated regularly",
                "description": "Official verification methods for Domain and URL-prefix properties.",
            },
            {
                "title": "About platform properties in Search Console",
                "url": "https://support.google.com/webmasters/answer/17148418",
                "source": "Google",
                "date": "2026",
                "description": "Platform property scope, OAuth, reports, and limitations for social and video accounts.",
            },
            {
                "title": "Import sites from Search Console to Bing Webmaster Tools",
                "url": "https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools",
                "source": "Bing",
                "date": "2019",
                "description": "GSC Import workflow, limits, and sync maintenance requirements.",
            },
        ]
    },
    "/zh/seo/submit-website": {
        "items": [
            {
                "title": "验证网站所有权（Search Console）",
                "url": "https://support.google.com/webmasters/answer/9008080",
                "source": "Google",
                "date": "持续更新",
                "description": "Domain 与 URL-prefix property 的官方验证方式说明。",
            },
            {
                "title": "Search Console 中的平台属性说明",
                "url": "https://support.google.com/webmasters/answer/17148418",
                "source": "Google",
                "date": "2026年",
                "description": "Platform property 范围、OAuth、报告与限制。",
            },
            {
                "title": "从 Search Console 导入站点到 Bing 站长工具",
                "url": "https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools",
                "source": "Bing",
                "date": "2019年",
                "description": "GSC Import 流程、数量限制与 sync 维护要求。",
            },
        ]
    },
}


def patch_json(fname, pages_patch):
    path = os.path.join(BASE, "src", "data", fname)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for k, v in pages_patch.items():
        data["pages"][k] = v
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def patch_seo_meta():
    path = os.path.join(BASE, "src", "data", "seo-meta.ts")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = re.sub(
        r'"submit-website":\s*\{[^}]*en:\s*\{[^}]*\},\s*zh:\s*\{[^}]*\},\s*publishDate:[^,]+,\s*modifiedDate:[^,]+,\s*\},',
        '''"submit-website": {
    en: {
      title: "Submit to Google Search Console: Websites & Social | Alignify",
      description: "GSC setup: Domain/URL-prefix verification, 2026 Platform properties, sitemaps, URL Inspection, Bing Import. Monitoring vs indexing. Free guide.",
    },
    zh: {
      title: "向 Google Search Console 提交网站与社媒账号 | Alignify",
      description: "GSC 完整指南：Website 验证、2026 Platform 社媒 OAuth、站点地图、URL 检查与 Bing Import。区分监控与收录。",
    },
    publishDate: "2025-02-13T00:00:00+08:00",
    modifiedDate: "2026-09-01T00:00:00+08:00",
  },''',
        text,
        count=1,
        flags=re.DOTALL,
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    zh_path = os.path.join(BASE, "content", "seo", "zh", "submit-website.md")
    en_path = os.path.join(BASE, "content", "seo", "en", "submit-website.md")
    for path, content in [(zh_path, ZH_MD), (en_path, EN_MD)]:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print("Wrote", path, "chars", len(content))
    patch_json("tldr-data.json", TLDR)
    patch_json("faq-data.json", FAQ)
    patch_json("references-data.json", REFS)
    patch_seo_meta()
    print("Updated JSON sidecars and seo-meta.ts")


if __name__ == "__main__":
    main()
