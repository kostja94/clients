# -*- coding: utf-8 -*-
"""Rewrite submit-website with long prose paragraphs and minimal internal links."""
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
readingMinutes: "9 分钟阅读"
pageUrl: "https://alignify.co/zh/seo/submit-website"
locale: "zh"
pillar: "seo"
section: "technical"
contentType: "how-to"
---
<!-- block:section -->
## 提交与收录：先搞清你在做什么 {#submit-vs-index}

向 Google Search Console（GSC）添加 property，本质是在声明「我有权查看这份搜索数据，并愿意为 Google 提供一个结构化的 URL 发现通道」。这一步**不会**自动把全站每一页写进索引，也**不会**直接改变排名；页面仍须被 Googlebot 抓取、通过质量与重复判断后，才有机会出现在搜索结果中。若你对抓取、索引、结果呈现三阶段还不熟悉，可先读 **[搜索引擎如何工作](/zh/seo/how-search-engine-works)**，再回来按本文完成 GSC 配置——本文聚焦「怎么在 GSC 里把监控与发现通道接好」，而不是重复讲解整个搜索流水线。

许多团队把「提交网站」和「让页面被收录」混为一谈：域名验证通过后，GSC 可能很快出现首页的查询与展示数据，但深层 URL 若缺少内链或站点地图入口，仍可能长期停留在「已发现—未抓取」状态。正确预期是：**Add property = 开通监控 + 辅助发现**；收录是否发生、排名是否出现，取决于后续的内容、技术与竞争环境。若验证完成后数周仍大量 URL 未进索引，应转到 **[网站索引](/zh/seo/website-indexing)** 按 GSC「网页」报告里的具体原因排查，而不是反复点击「请求编入索引」碰运气。

本文按实际操作顺序写：先区分 GSC 三种 property 类型 → 完成 Website 验证与 sitemap → 按需连接 2026 年新增的 Platform property（Instagram / TikTok / X / YouTube）→ 并行 Bing。读完后你应能独立完成从「零 property」到「Website + Platform 并行、Bing 已 Import」的全套 setup，并知道哪些动作属于监控通道、哪些仍须交给索引排查流程。

<!-- block:section -->
## GSC 三种 property：一张表看懂 {#gsc-property-overview}

2026 年的 GSC 里，「提交」不再等于「只验证一个网站」。你持有的资产不同——整站域名、某个 URL 前缀、或单个社媒账号——property 类型、验证方式和上线后能做的动作完全不同；选错类型常见于「验证通过但报表范围不对」，或「在 Website property 里找社媒 OAuth 入口」这类浪费时间的路径。

Domain 与 URL-prefix 都属于 Website property：前者用一条 DNS 记录覆盖全部子域与路径，后者把监控范围锁在一个前缀之内，并可用 HTML、meta 或 GA/GTM 验证。Platform property 则绑定单个 Instagram、TikTok、X 或 YouTube 账号，走 OAuth，**没有** sitemap 提交或单页「请求编入索引」入口，报表只反映该账号内容在 Google 搜索、Discover、新闻中的展示与点击。三种类型可并行存在、数据互不合并；每添加一个 property，就对应**一套独立的 verification token**（Platform 为 OAuth 授权），不可把同一串 meta 或 DNS 值复用到另一个 property。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Property 类型</th><th>绑定对象</th><th>验证方式</th><th>验证后典型动作</th></tr></thead><tbody><tr><td><strong>Domain</strong></td><td>整域（全部子域 + 协议 + 路径）</td><td>DNS TXT / CNAME</td><td>提交 XML 站点地图、网址检查</td></tr><tr><td><strong>URL-prefix</strong></td><td>单一前缀（如 <code>https://www.example.com/</code>）</td><td>DNS、HTML 文件、meta、GA、GTM</td><td>同上，仅覆盖前缀内 URL</td></tr><tr><td><strong>Platform</strong>（2026-07）</td><td>单个 IG / TikTok / X / YouTube 账号</td><td>平台 OAuth</td><td>Performance / Insights；无 sitemap</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

上表是后文 Website 与 Platform 两部分的索引：有自有站点时几乎总是先完成 Website 侧；若你还在运营上述四个平台之一，且关心内容在 Google 面上的可见度，可在 Website 验证之后追加 Platform property，两者报表独立，读数时勿简单加总。

<!-- block:section -->
## Website property：Domain 与 URL-prefix {#website-property-types}

**Domain property** 填写根域（如 `example.com`），覆盖 `https://www.`、`https://m.`、`http://` 及该域下全部路径。验证**仅支持 DNS**（TXT 或 CNAME），但通常只需一条记录即可长期生效——站点改版、换 CMS、甚至迁移 hosting，只要 DNS zone 仍在你控制之下，验证往往比 HTML 文件或 meta 更耐 deploy 误删。对能改 DNS 的团队，这也是我在客户项目里默认推荐的路径：一条 TXT 换全站统一报表，Performance 里再按 hostname 或路径过滤，比维护多个 URL-prefix 的 meta 串更不易出错。

**URL-prefix property** 必须填完整前缀（含协议；路径前缀须写全，`/en/` 与 `/es/` 各算一个）。覆盖范围严格限定在该前缀之下：`https://blog.example.com/` 的数据不会出现在 `www.example.com` 的 prefix property 里。验证方式更灵活——HTML 文件、首页 `<head>` meta、Google Analytics / Tag Manager、或 DNS 均可；若 URL-prefix 用 DNS 验证成功，Google 会同时赋予 Domain 级验证能力。`http` 与 `https` 若并存，在 prefix 模式下各需独立 property；父 prefix 已验证时，子路径 prefix **有时**可自动验证，但 Domain `example.com` **不会**自动覆盖独立 Domain `blog.example.com`。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>粒度</th><th>填法示例</th><th>验证代码套数</th><th>包含</th><th>不包含</th></tr></thead><tbody><tr><td>整域</td><td>Domain <code>example.com</code></td><td><strong>1</strong> 条 DNS</td><td>全部子域与路径</td><td>其他顶级域</td></tr><tr><td>单子域</td><td><code>https://blog.example.com/</code></td><td><strong>1</strong> 套</td><td><code>blog.example.com/*</code></td><td><code>www.example.com</code></td></tr><tr><td>单路径</td><td><code>https://example.com/shop/</code></td><td><strong>1</strong> 套</td><td><code>/shop/*</code></td><td><code>/blog/</code></td></tr></tbody></table></div>
<!-- childrenHtml:end -->

拆几个 property，就要准备几套互不相同的 verification token：这是 GSC 最容易踩坑的规则之一。根域与子域共用同一 DNS zone 时，一条 Domain TXT 通常已覆盖全部子域，不必为 `blog.` 再建第二条 DNS——除非你 deliberately 要用 URL-prefix 把 KPI 隔离到不同 property。

<!-- block:section -->
## 如何选 Website property {#choose-website-property}

选型可以收敛成一条决策链：若你能编辑 DNS，优先添加 **1× Domain property**，用一条 TXT 覆盖全站；报表内用过滤器按 hostname 或目录拆分 KPI，通常比为 `www`、`blog`、`/shop/` 各建 prefix 更易维护。若完全无法动 DNS、只能在页面里插代码，则为**每一个**需要监控的 URL-prefix 各 Add 一次 property，各生成一套 meta 或 HTML 文件——`www` 与 `blog` 若各需独立 property，首页 `<head>` 里可以并存两个 meta，但 `content` 值必须不同，禁止复用。

多语言站点若路径规则清晰（如 `/en/`、`/es/`），多数情况下 1× Domain 加 Performance 过滤即可；只有当不同目录由不同团队分权、且必须在 GSC 里物理隔离权限时，才值得为每个路径 prefix 单独验证并承担多套 token 的运维成本。`http` 与 `https` 仍同时对外服务时，仍应优先用 Domain 一把收；若必须保留 prefix 模式，则至少两个 prefix、两套验证，且 redirect 策略要在验证前理顺，避免 Google 检查的 URL 与最终 landing 不一致。

<!-- childrenHtml:start -->
<div class="content-html"><pre><code>&lt;!-- Property A：https://www.example.com/ --&gt;
&lt;meta name="google-site-verification" content="AAAAAA...token_A" /&gt;
&lt;!-- Property B：https://blog.example.com/（须不同串） --&gt;
&lt;meta name="google-site-verification" content="BBBBBB...token_B" /&gt;</code></pre></div>
<!-- childrenHtml:end -->

多人协作时，Settings → Ownership verification 建议叠加两种以上验证方式，防止某次发布删掉唯一 HTML 文件或 meta；也勿在 deploy 中覆盖同事已生效的 token。Google 托管的 Blogger、Sites 在同账号下常可自动验证，自定义域名的 WordPress 站点可用 Site Kit 插件减少手工步骤。

<!-- block:section -->
## 验证网站所有权 {#verify-website-ownership}

Website 验证的入口固定：打开 [Google Search Console](https://search.google.com/search-console) → **+ 添加资源** → 选 **Website** → Domain 或 URL-prefix → 按提示完成验证（可先 Verify later，但完整报表与 sitemap 提交以验证通过为前提）。验证方法的选择取决于你能控制 DNS、服务器根目录，还是只能改首页模板；选错方法的表现往往是「文件明明上传了却失败」，多数情况是 HTML 文件验证不跟随跨域 redirect，而 meta / GA / GTM 会跟随同域 redirect 的终页——排查时先对照这一差异，再查 DNS 传播或文件是否被登录墙挡住。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>方法</th><th>适用</th><th>核心要求</th><th>常见失败</th></tr></thead><tbody><tr><td><strong>DNS TXT</strong></td><td>Domain；URL-prefix 可选</td><td>Host=<code>@</code>；值含 <code>google-site-verification=…</code></td><td>改错 zone；传播 2–48 小时</td></tr><tr><td><strong>DNS CNAME</strong></td><td>Domain（apex 有 CNAME 时）</td><td>target 含 <code>dv.googlehosted.com</code></td><td>与 TXT 记录类型选错</td></tr><tr><td><strong>HTML 文件</strong></td><td>URL-prefix</td><td>根目录匿名可访问；文件名精确</td><td>需登录；不跟跨域 redirect</td></tr><tr><td><strong>HTML meta</strong></td><td>URL-prefix</td><td>前缀首页 <code>&lt;head&gt;</code></td><td>放在会跳走的 URL</td></tr><tr><td><strong>GA / GTM</strong></td><td>URL-prefix</td><td>同 Google 账号；snippet 位置正确</td><td>旧 UA；snippet 在 body</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

验证通过后，**不要删除**已生效的 DNS、文件或 meta——Google 会周期性复查，失效即失去 Verified owner 权限，Merchant Center 等跨产品验证也可能连带中断。添加 property 本身**不改变**自然排名；Google 可能在验证前已开始收集部分信号，但你看不到完整数据，也无法提交 sitemap，直到 ownership 确认完成。

<!-- block:section -->
## 验证之后：站点地图与单页索引请求 {#after-website-verification}

Website property 验证完成，才进入「告诉 Google 有哪些 URL 值得优先发现」的阶段。XML 站点地图应只列出可索引的规范 URL，并在上线后可被匿名 fetch；在 GSC 的 **Sitemaps** 里粘贴 sitemap 的 URL 并 Submit——注意 GSC **只登记 sitemap 地址，不上传文件本体**，作用是加速发现而非保证收录。提交前用「网址检查」对 sitemap URL 本身做一次 fetch，能提前发现 404、重定向链或权限问题，避免「提交了但 Google 读不到」的假动作。

对战略 URL——新模板首篇、重大改版后的核心落地页、或刚修复 robots/noindex 误伤的页面——可用「网址检查」确认 Google 能渲染该页，再点 **请求编入索引**。该工具有日配额，适合点对点使用；整批新 URL 仍应依赖站点地图与站内链接结构，而不是对列表页下几百条 URL 逐一手动请求。新域或外链极少的站点，全站索引常见需要 **1–2 周**；提交后至少观察一周，再结合 GSC「网页」报告判断是正常延迟还是技术阻断。Google Indexing API 与 IndexNow 属于程序化补充（前者主要服务 Google 有限场景，后者服务于 Bing 等），不在本文展开配置细节。

<!-- block:section -->
## Platform property：社媒与视频账号（2026） {#platform-properties}

**无需自有网站**，也可以添加 GSC 的 **Platform property**：绑定单个 Instagram、TikTok、X 或 YouTube 账号，查看该账号发布的内容在 **Google 搜索、Google Discover、Google 新闻** 中的展示与点击。该功能于 2026 年 7 月全球可用；界面若暂未出现，属于 Google 仍描述的逐步 rollout，可换账号或稍后重试，不必反复删除重建 property。

连接流程与 Website 完全不同：GSC → 资源选择器 → **Add property** → 在支持平台旁点 **Add** → 登录并授权对应社媒账号 → **Go to property**。每个 IG / TikTok / X / YouTube **账号或频道各建一个** property，不可把多账号合并为一个报表。数据通常在 OAuth 成功后**数天**内开始出现，默认窗口 **28 天**，且**无历史回填**——连接之前的内容在 Google 侧的表现不可追溯。若你已在 Google 搜索拥有 **Search profile**（公开创作者页）且已链接同一平台，GSC 有时已有部分数据，无需重复 OAuth；但 Search profile 面向公开展示与粉丝门槛，Platform property 面向私有分析，二者不可互换（见下文边界表）。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>平台</th><th>Platform property</th><th>备注</th></tr></thead><tbody><tr><td>Instagram</td><td>✅</td><td>含 Story 出现在 Google 搜索时</td></tr><tr><td>TikTok</td><td>✅</td><td>—</td></tr><tr><td>X</td><td>✅</td><td>—</td></tr><tr><td>YouTube</td><td>✅</td><td>可筛 <code>/shorts/</code> vs <code>/watch</code></td></tr><tr><td>LinkedIn / Facebook 等</td><td>❌</td><td>官方未列；勿按「即将支持」规划</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Google 会周期性复查 OAuth 授权；平台侧登录过期时报告会暂停，重新授权后恢复且不必重累积历史。请勿在 Instagram、TikTok 等应用设置里撤销 Google 的读取权限，否则 GSC 会静默失去数据接入。

<!-- block:section -->
## Platform 报告读法与限制 {#platform-reports-and-limits}

Platform property 提供 **Performance**（点击、展示、CTR、平均排名，可按帖子 URL、查询、国家、设备筛选）、**Insights**（28 天趋势、Top 内容、query groups 涨跌）与 **Achievements**（点击里程碑）。Discover 与 Google 新闻的维度仅在该账号确有相应流量时出现，不应期待每个 property 都看到完整的多表面 breakdown。

读数时务必守住测量边界：Platform 统计的是帖子 URL 出现在 **Google 搜索、Discover、新闻** 中的次数，**不是** TikTok For You、Instagram 信息流或 YouTube 首页推荐带来的站内播放与互动。把 Platform 报表当作「Google 面可见度」，把各平台原生后台当作「App 内表现」——混读会导致错误的选题与投放判断。Insights 顶部汇总卡含 web + image + video + news 的合计点击，下方明细表侧重 web search，分项之和可能小于汇总卡，这是 Google Help 已说明的口径差异，勿强行凑平。

2026 年 7 月仍存在的硬限制包括：Platform 数据**暂无 Search Console API 与 BigQuery 批量导出**，跨平台周报需在各 property 内 Export 后手工合并；**无 sitemap、无 Request indexing**，社媒 URL 由 Google 自行发现。捕捉新帖在 Google 侧的 spike 可用 Performance 的 **24 hours** 过滤器；YouTube 可对比 URL 含 `/shorts/` 与 `/watch` 的表现差异。

<!-- block:section -->
## Website、Platform 与 Search profile 的边界 {#property-boundaries}

三类「属性」名称相近，职责却完全不同：Website property 证明你对域名或 URL 前缀的控制权，验证后走 sitemap 与网址检查；Platform property 通过 OAuth 绑定单个社媒账号，只读 Google 面上的 Performance；Search profile 则是 Google 搜索上**公开**的创作者聚合页，有地区与粉丝等门槛，与 GSC 私有报表不是同一产品。添加任意一种 property 都**不会**改变 Google 如何排名或展示你的内容——它们只是监控与分析的入口。

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>A</th><th>B</th><th>一句区分</th></tr></thead><tbody><tr><td>Website property</td><td>Platform property</td><td>DNS/HTML 证站点 vs OAuth 证社媒账号</td></tr><tr><td>Platform property</td><td>Search profile</td><td>GSC 私有分析 vs 搜索上公开创作者页</td></tr><tr><td>Add property</td><td>Get indexed</td><td>监控通道 ≠ 收录保证</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

若你同时运营网站与上述社媒账号，实践上应并行添加两类 property，各自看各自的 Performance，而不是假设「验证了网站就能在 GSC 里看到 TikTok 站内数据」，或「连接了 Platform 就不需要 Website 验证」。

<!-- block:section -->
## Bing 并行：GSC 验证后尽快 Import {#bing-parallel}

Bing 索引为 Yahoo、DuckDuckGo 及部分 AI 搜索入口提供网页结果；只做 GSC、不做 Bing Webmaster Tools（BWT），会在 Bing 生态形成可见性盲区。Website property 在 GSC 验证通过后，建议尽快（通常 **5 分钟内**）打开 [Bing Webmaster Tools](https://www.bing.com/webmasters) → **My Sites → Import** → 用对该站具备 GSC **Verified owner** 的 Google 账号授权 → 勾选站点 → **Import**。单次最多 **100** 个站，BWT 会自动完成验证且 sitemap 可同步；BWT 会周期性 sync GSC，若日后 GSC 失验证，须在 BWT **重新连接**，否则 Bing 侧数据与提交状态也会中断。

无法使用 GSC Import 时（例如尚未在 GSC 验证），可在 BWT **Add a Site** 并选手动验证——Domain Connect、meta、DNS、XML 等 token 与 GSC **独立、可并存**。验证后在 BWT 提交 sitemap，并配置 **IndexNow** 以通知 URL 变更；IndexNow **不适用于 Google**，Google 侧仍依赖 sitemap 与网址检查。BWT 目前**不提供**与 GSC 对等的 Platform property，社媒 Google 面分析只在 GSC 完成。

<!-- block:section -->
## 常见反模式 {#anti-patterns}

最常见的一类误判，是把「已在 GSC 验证」等同于「页面会被收录或会排名」。验证只解锁监控与 sitemap 通道；robots.txt 阻断、noindex、重复 URL、孤立页面或质量不足的模板仍会被排除在索引之外。正确做法是在 GSC「网页」报告里阅读**具体排除原因**，修复后再对少量战略 URL 请求编入索引，而不是对同一低价值 URL 反复消耗配额。

另一类高频错误是验证后删除 DNS TXT、HTML 验证文件或 meta tag——权限会在 Google 复查时静默失效，且可能影响 Merchant Center 等共用同一 verification 的服务。多个 URL-prefix property **共用一串** verification code 必然失败；父域 DNS 也不能替代子域独立 Domain property 的边界。只做 GSC、不做 BWT Import，则 Bing/Yahoo/DDG 及相关 Copilot 路径上的可见性难以解释与优化。Platform 侧，用 GSC 数据去衡量 TikTok For You 或 IG 信息流爆款属于指标错位；等待「Platform API 上线再做周报」在 2026 年仍不现实，Export 仍是必做动作。

<!-- block:section -->
## 结论 {#conclusion}

GSC 提交的正确顺序可以概括为：按资产类型添加 **Domain、URL-prefix 或 Platform** property → 用对应方式完成验证并**长期保留 token** → 在 Website property 中提交 XML 站点地图、对关键 URL 使用网址检查 → 在 GSC 验证后尽快 **Bing Import** → 每周查看索引覆盖率，以及 Website 与 Platform 各自独立的 Performance，而不是依赖 site: 运算符做精确计数。

Website 与 Platform 并行、数据独立：前者服务站点 URL 的发现与收录监控，后者服务创作者内容在 Google 搜索面的可见度。收录与排名仍取决于内容质量、技术底座与竞争环境——提交是进入监控闭环的起点，不是 SEO 的终点。上线 GSC 前，建议先对照 **[SEO Checklist](/zh/seo/checklist)** 确认 robots、HTTPS、站点地图与核心内链就绪，再开始验证，避免 Search Console 从「不可索引」的基线学习错误信号。
'''

EN_MD = r'''---
title: "Submit to Google Search Console: Websites, Social Accounts & Bing"
description: "Complete GSC setup: Website Domain/URL-prefix verification, 2026 Platform properties (IG/TikTok/X/YouTube OAuth), sitemaps, URL Inspection, and Bing Import. Monitoring vs indexing explained. Free guide."
slug: "submit-website"
date: "February 13, 2025"
updated: "September 1, 2026"
readingMinutes: "10 min read"
pageUrl: "https://alignify.co/seo/submit-website"
locale: "en"
pillar: "seo"
section: "technical"
contentType: "how-to"
---
<!-- block:section -->
## Submission vs indexing: know what you are doing {#submit-vs-index}

Adding a property in Google Search Console (GSC) declares that you control a monitoring channel and a structured discovery path for URLs. It does **not** automatically index every page on a site, and it does **not** change rankings. Pages still need to be crawled, evaluated, and stored before they can appear in search. If the crawl → index → serve pipeline is new to you, read **[how search engines work](/seo/how-search-engine-works)** first, then return here for GSC setup — this guide covers **how to wire monitoring and discovery in GSC**, not the full search stack.

Teams often treat “submit the site” and “get pages indexed” as the same milestone. After domain verification, homepage queries may appear quickly while deep URLs without internal links or sitemap entries can sit in **discovered — not crawled** for weeks. The right expectation: **Add property = monitoring + assisted discovery**; whether indexing happens depends on content, technical health, and competition. If many URLs stay out of the index weeks after verification, move to **[website indexing](/seo/website-indexing)** and read the specific exclusion reasons in GSC Pages — not repeated URL Inspection clicks on the same broken template.

This guide follows the job in order: distinguish the three GSC property types → complete Website verification and sitemaps → optionally connect 2026 **Platform properties** (Instagram, TikTok, X, YouTube) → parallelize Bing. When you finish, you should reach “Website + Platform (if needed) + Bing Import” with a clear line between monitoring setup and index troubleshooting.

<!-- block:section -->
## Three GSC property types at a glance {#gsc-property-overview}

In 2026, “submit to GSC” is not website-only. The asset you own — whole domain, one URL prefix, or one social account — determines verification, report scope, and what you can do next. Picking the wrong type usually shows up as “verified but data scope is wrong” or wasted time hunting OAuth inside a Website property.

Domain and URL-prefix are both **Website** properties: one DNS record can cover an entire estate, while a URL-prefix locks scope and allows HTML, meta, or GA/GTM verification. **Platform** properties bind one Instagram, TikTok, X, or YouTube account via OAuth — no sitemap, no Request indexing — and report only how that account’s URLs perform on Google Search, Discover, and News. Types coexist with **separate data**; each new property gets its **own verification token** (OAuth for Platform). Never reuse the same meta or DNS string across properties.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Property type</th><th>What you bind</th><th>Verification</th><th>After verification</th></tr></thead><tbody><tr><td><strong>Domain</strong></td><td>Entire domain (subdomains, protocols, paths)</td><td>DNS TXT / CNAME</td><td>XML sitemap, URL Inspection</td></tr><tr><td><strong>URL-prefix</strong></td><td>One prefix (e.g. <code>https://www.example.com/</code>)</td><td>DNS, HTML file, meta, GA, GTM</td><td>Same, prefix-scoped only</td></tr><tr><td><strong>Platform</strong> (Jul 2026)</td><td>One IG / TikTok / X / YouTube account</td><td>Platform OAuth</td><td>Performance / Insights; no sitemap</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Use the table as a map for the rest of the guide: almost always complete Website setup first when you control a site; add Platform when you care about Google-surface visibility for one of the four supported networks — and never merge their metrics blindly.

<!-- block:section -->
## Website properties: Domain vs URL-prefix {#website-property-types}

A **Domain property** uses the root domain (`example.com`) and covers `https://www.`, `https://m.`, `http://`, and all paths under that domain. Verification is **DNS-only** (TXT or CNAME), but one record often lasts through redesigns and CMS migrations as long as you keep the zone — which is why I default clients with DNS access to Domain verification instead of multiple meta tags that deploys delete by accident.

A **URL-prefix property** requires the full prefix (protocol included; `/en/` and `/es/` are separate). Scope is strict: `https://blog.example.com/` never includes `www.example.com`. Verification can be HTML file, `<head>` meta, Google Analytics / Tag Manager, or DNS; DNS success on a URL-prefix also grants Domain-level verification for that site. Separate `http` and `https` prefixes need separate properties; child prefixes may auto-verify when a parent prefix is verified, but Domain `example.com` does **not** auto-cover Domain `blog.example.com`.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Granularity</th><th>Example</th><th>Token sets</th><th>Includes</th><th>Excludes</th></tr></thead><tbody><tr><td>Whole domain</td><td>Domain <code>example.com</code></td><td><strong>1</strong> DNS</td><td>All subdomains &amp; paths</td><td>Other TLDs</td></tr><tr><td>Single subdomain</td><td><code>https://blog.example.com/</code></td><td><strong>1</strong> set</td><td><code>blog.example.com/*</code></td><td><code>www.example.com</code></td></tr><tr><td>Single path</td><td><code>https://example.com/shop/</code></td><td><strong>1</strong> set</td><td><code>/shop/*</code></td><td><code>/blog/</code></td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Split properties mean split tokens — the rule GSC breaks most often. When root and subdomains share one DNS zone, one Domain TXT usually covers all hosts; you only add a second property when you deliberately isolate KPIs under URL-prefix scope.

<!-- block:section -->
## Choosing a Website property {#choose-website-property}

The decision chain is short: if you can edit DNS, add **one Domain property** and one TXT; filter Performance by hostname or path instead of maintaining many prefix properties. If DNS is impossible and you only control page code, **Add each URL-prefix separately** — each gets its own meta or HTML file. When both `www` and `blog` need isolation, two meta tags may live in one `<head>` but **must differ**; reuse fails verification.

Multilingual paths like `/en/` and `/es/` usually work with one Domain plus filters; split prefixes only when teams need physically separate GSC permissions, accepting the cost of multiple tokens. When both `http` and `https` remain public, prefer Domain; if you must stay on prefixes, verify each stack and fix redirects before Google checks the wrong landing URL.

<!-- childrenHtml:start -->
<div class="content-html"><pre><code>&lt;!-- Property A: https://www.example.com/ --&gt;
&lt;meta name="google-site-verification" content="AAAAAA...token_A" /&gt;
&lt;!-- Property B: https://blog.example.com/ --&gt;
&lt;meta name="google-site-verification" content="BBBBBB...token_B" /&gt;</code></pre></div>
<!-- childrenHtml:end -->

Stack **≥2 verification methods** under Settings → Ownership verification so one release cannot wipe access; never overwrite a teammate’s active token. Google-hosted Blogger and Sites often auto-verify; WordPress on custom domains can use Site Kit to reduce manual steps.

<!-- block:section -->
## Verifying Website ownership {#verify-website-ownership}

Website verification starts at [Google Search Console](https://search.google.com/search-console): **+ Add property** → **Website** → Domain or URL-prefix → complete verification (Verify later is allowed, but sitemaps and full reports need success). Method choice depends on whether you control DNS, the web root, or only templates — when “the file is uploaded but verification fails,” HTML file verification often fails on **cross-domain redirects**, while meta / GA / GTM follow **same-domain** redirect destinations; check that before chasing DNS propagation.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Method</th><th>Applies to</th><th>Requirement</th><th>Common failures</th></tr></thead><tbody><tr><td><strong>DNS TXT</strong></td><td>Domain; optional URL-prefix</td><td>Host=<code>@</code>; <code>google-site-verification=…</code></td><td>Wrong zone; 2–48h propagation</td></tr><tr><td><strong>DNS CNAME</strong></td><td>Domain with apex CNAME</td><td>Target includes <code>dv.googlehosted.com</code></td><td>Wrong record type vs TXT</td></tr><tr><td><strong>HTML file</strong></td><td>URL-prefix</td><td>Anonymous root fetch; exact filename</td><td>Login wall; no cross-domain follow</td></tr><tr><td><strong>HTML meta</strong></td><td>URL-prefix</td><td>Prefix homepage <code>&lt;head&gt;</code></td><td>Tag on redirecting URL</td></tr><tr><td><strong>GA / GTM</strong></td><td>URL-prefix</td><td>Same Google account; snippet placement</td><td>Legacy UA; snippet in body</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

After success, **do not remove** DNS, files, or meta — Google rechecks periodically and cross-product verification can break. Adding a property does **not** change rankings; Google may collect signals before you verify, but you cannot submit sitemaps until ownership is confirmed.

<!-- block:section -->
## After Website verification: sitemaps and URL requests {#after-website-verification}

Verification unlocks telling Google which URLs deserve priority discovery. Publish a crawlable XML sitemap of **canonical, indexable URLs**, confirm the sitemap URL itself fetches in URL Inspection, then paste it under GSC **Sitemaps** and Submit — GSC **registers the URL, not the file**, to accelerate discovery, not to guarantee indexing.

Use URL Inspection → **Request indexing** for strategic URLs: new templates, major refreshes, or pages you just fixed after robots or noindex mistakes. Quota is daily and should stay point-targeted; bulk launches still depend on sitemaps and site structure, not hundreds of manual clicks. New or low-link domains often need **1–2 weeks** for broad indexing; wait at least a week before calling failure, then read GSC Pages. Google Indexing API and IndexNow are programmatic add-ons (Google API is narrow; IndexNow serves Bing) — setup details sit in ops runbooks, not here.

<!-- block:section -->
## Platform properties: social and video (2026) {#platform-properties}

You can add a **Platform property without a website**: bind one Instagram, TikTok, X, or YouTube account and see how that account’s content performs on **Google Search, Discover, and Google News**. Available globally since July 2026; if the UI is missing, retry later during gradual rollout — do not delete and recreate properties repeatedly.

Flow: GSC → property picker → **Add property** → **Add** beside the platform → authorize the account → **Go to property**. **One property per account** — no merged reports. Data usually appears within **days**; default window **28 days**; **no backfill** before connection. If you already have a public **Search profile** linked to the same platform, GSC may show data without reconnecting — but Search profile and Platform property are different products (see boundaries below).

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>Platform</th><th>Platform property</th><th>Notes</th></tr></thead><tbody><tr><td>Instagram</td><td>✅</td><td>Includes Stories on Google Search</td></tr><tr><td>TikTok</td><td>✅</td><td>—</td></tr><tr><td>X</td><td>✅</td><td>—</td></tr><tr><td>YouTube</td><td>✅</td><td>Filter <code>/shorts/</code> vs <code>/watch</code></td></tr><tr><td>LinkedIn, Facebook, etc.</td><td>❌</td><td>Not listed; do not plan on imminent support</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

Google rechecks OAuth; expired platform login **pauses** reports until you re-authorize without losing history. Do not revoke Google access in the social app settings.

<!-- block:section -->
## Platform reports and limits {#platform-reports-and-limits}

Platform properties expose **Performance** (clicks, impressions, CTR, average position — filter by post URL, query, country, device), **Insights** (28-day trends, top content, query group movers), and **Achievements** (click milestones). Discover and News dimensions appear only when traffic exists — not every property shows every surface.

Read metrics with the boundary in mind: Platform counts URLs on **Google Search, Discover, and News**, **not** TikTok For You, Instagram feeds, or YouTube home recommendations. Use GSC Platform for Google-surface visibility and each platform’s native analytics for in-app performance — mixing them misguides content bets. Insights summary cards aggregate web + image + video + news clicks; detail tables skew toward web search, so row sums may fall below the card — that is documented behavior, not a bug to reconcile away.

Hard limits as of July 2026: **no Search Console API or BigQuery export** for Platform data — weekly reviews need manual Export; **no sitemap, no Request indexing**. Use Performance **Last 24 hours** for post-launch spikes; on YouTube, compare `/shorts/` vs `/watch` filters.

<!-- block:section -->
## Website, Platform, and Search profile {#property-boundaries}

Three “profile” names collide in conversation but serve different jobs. Website properties prove control of a domain or URL prefix, then use sitemaps and URL Inspection. Platform properties OAuth one social account and read Google-surface Performance only. Search profiles are **public** creator pages on Google Search with eligibility rules — not private GSC analytics. Adding any property **does not** change how Google ranks or displays your content; it only opens monitoring.

<!-- childrenHtml:start -->
<div class="content-html"><table><thead><tr><th>A</th><th>B</th><th>Distinction</th></tr></thead><tbody><tr><td>Website property</td><td>Platform property</td><td>DNS/HTML site proof vs OAuth social account</td></tr><tr><td>Platform property</td><td>Search profile</td><td>Private GSC analytics vs public creator page</td></tr><tr><td>Add property</td><td>Get indexed</td><td>Monitoring channel ≠ indexing guarantee</td></tr></tbody></table></div>
<!-- childrenHtml:end -->

When you run both a site and supported social accounts, add both property types and read each Performance report on its own terms — Website verification does not show TikTok in-app views, and Platform connection does not replace site verification.

<!-- block:section -->
## Bing in parallel: Import soon after GSC {#bing-parallel}

Bing indexes pages that also feed Yahoo, DuckDuckGo, and parts of AI search — GSC-only setups miss that slice. After GSC Website verification, open [Bing Webmaster Tools](https://www.bing.com/webmasters) within **five minutes**: **My Sites → Import** → Google sign-in with **Verified owner** on those sites → select → **Import**. Up to **100** sites per batch; BWT auto-verifies and may sync sitemaps. BWT syncs periodically — if GSC verification lapses, **reconnect** or Bing data and submissions stall.

Without GSC Import, **Add a Site** in BWT and verify manually — tokens are **independent** of GSC. Submit sitemaps in BWT and enable **IndexNow** for URL change pings; IndexNow does **not** apply to Google. BWT has **no** Platform property equivalent; social Google-surface analytics stay in GSC.

<!-- block:section -->
## Anti-patterns {#anti-patterns}

The most common mistake is equating “verified in GSC” with “will be indexed or will rank.” Verification unlocks monitoring and sitemap submission; robots blocks, noindex, duplicates, orphan URLs, and thin templates still exclude pages. Read the **specific reason** in GSC Pages, fix the blocker, then request indexing for a few strategic URLs — not the same low-value URL on a loop.

Deleting DNS TXT, HTML verification files, or meta tags after success silently drops ownership on Google’s recheck and can break Merchant Center and other shared verification. Reusing one verification string across URL-prefix properties always fails; parent-domain DNS does not substitute for a separate subdomain Domain property. GSC without BWT Import leaves Bing/Yahoo/DDG and related Copilot paths hard to explain or improve. On Platform, treating GSC metrics as For You or feed virality is a category error; waiting for a Platform API before weekly Export was still unrealistic as of July 2026.

<!-- block:section -->
## Conclusion {#conclusion}

The GSC setup sequence is: add **Domain, URL-prefix, or Platform** properties for each asset → verify with the matching method and **keep tokens alive** → on Website properties submit XML sitemaps and use URL Inspection for key URLs → **Import into Bing** soon after GSC verification → review index coverage weekly plus separate Website and Platform Performance — not `site:` guesses.

Website and Platform run in parallel with independent data: sites for URL discovery and index monitoring, creator accounts for Google-search visibility. Rankings still depend on content, technical foundations, and competition — submission starts the monitoring loop, it does not finish SEO. Before verifying, walk **[SEO checklist](/seo/checklist)** so robots, HTTPS, sitemaps, and core internal links are ready — otherwise Search Console learns from a broken baseline.
'''


def patch_json(fname, pages_patch):
    path = os.path.join(BASE, "src", "data", fname)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for k, v in pages_patch.items():
        data["pages"][k] = v
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def audit_prose(text, loc):
    body = re.sub(r"^---.*?---\n", "", text, flags=re.S)
    paras = [
        p.strip()
        for p in re.split(r"\n\n+", body)
        if p.strip()
        and not p.strip().startswith("<!--")
        and not p.strip().startswith("##")
    ]
    short = [p for p in paras if len(p) < 80 and "childrenHtml" not in p]
    links = re.findall(r"\]\((/[^)]+)\)", text)
    long_paras = [p for p in paras if len(re.findall(r"[。！？]", p)) >= 4 or len(re.findall(r"[.!?]", p)) >= 4]
    print(loc, "paras", len(paras), "short", len(short), "long(4+sent)", len(long_paras), "internal links", links)


def main():
    for path, content in [
        (os.path.join(BASE, "content/seo/zh/submit-website.md"), ZH_MD),
        (os.path.join(BASE, "content/seo/en/submit-website.md"), EN_MD),
    ]:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        audit_prose(content, path)
    print("done")


if __name__ == "__main__":
    main()
