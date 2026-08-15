/**
 * 将 website-traffic / dark-traffic 中英 JSON 改为博客式连贯段落：
 * 去掉 bg-primary/bg-yellow 卡片，合并零碎列表为 prose。
 * 运行：node scripts/permanent/apply-traffic-blog-prose.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..", "..");

function writeJson(rel, doc) {
  fs.writeFileSync(
    path.join(root, rel),
    `${JSON.stringify(doc, null, 2)}\n`,
    "utf8",
  );
}

// --- zh website-traffic: 单块 HTML（保留对比表与漫谈中的示例表） ---
const zhWebsiteTrafficHtml = `<div class="space-y-10" id="types-of-traffic">
<h2 class="text-2xl font-bold" id="types-of-traffic-h">流量类型（Types of Traffic）有哪些？</h2>

<div class="space-y-4" id="direct-traffic">
<h3 class="text-lg font-semibold" id="1-direct-traffic">1. 直接流量（Direct Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">直接流量指用户手动输入网址、使用书签、浏览器自动填充、复制链接到地址栏等方式进入站点；这类访问者往往已认识品牌，也可能是员工访问（需在分析工具里排除内部 IP）。需要牢记：其中常会混入<a href="/zh/seo/dark-traffic" class="text-primary hover:underline">无法归因流量（Dark Traffic）</a>——例如通过即时通讯私聊、加密邮件或部分应用内跳转进入时 Referrer 丢失，会被系统记成「直接」。</p>
<p class="text-base md:text-lg leading-relaxed">常见入口包括：手输域名、历史记录与自动补全、书签、从聊天记录或文档里复制 URL 再粘贴打开等。解读占比时，应结合活动日历、落地页与抽样调研，而不是把「直接」简单等同为品牌自然回访。</p>
</div>

<div class="space-y-4" id="dark-traffic">
<h3 class="text-lg font-semibold" id="2-dark-traffic">2. 无法归因流量（Dark Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">无法归因流量指分析工具难以还原真实来源的访问：点击来自封闭平台、邮件客户端或 App 内网页容器时，常常不带可读的引荐串，报表里便与直接流量堆在一起。技术侧常见触发因素包括 HTTPS→HTTP 降级、应用内浏览器、PDF 等文件内链接，以及过严的 Referrer Policy。</p>
<p class="text-base md:text-lg leading-relaxed">2012 年《大西洋月刊》在文章中提出「暗社交」（Dark Social），描述那些发生在私信、邮件与封闭社群、却难以被常规分析度量的分享行为。若需系统了解定义、成因、识别与治理，可继续阅读<a href="/zh/seo/dark-traffic" class="text-primary hover:underline">无法归因流量（Dark Traffic）完整指南</a>。</p>
</div>

<div class="space-y-4" id="referral-traffic">
<h3 class="text-lg font-semibold" id="3-referral-traffic">3. 推荐流量（Referral Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">推荐流量来自用户在其他站点上点击指向你的链接：行业媒体、论坛帖子、导航站收录、合作伙伴页面以及部分社交平台跳转，都可能落在 referral 桶里。高质量外链会被搜索引擎视为信任信号，但也要注意垃圾引荐与异常爬虫——定期用 Ahrefs、Majestic 等工具做域名级体检，避免低质来源拖累判断。</p>
</div>

<div class="space-y-4" id="organic-traffic">
<h3 class="text-lg font-semibold" id="4-organic-traffic">4. 自然流量（Organic Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">自然流量来自搜索引擎的非付费结果，是多数内容站长期复利最强的来源之一。主流入口包括 Google、Bing、百度、Yahoo、Yandex 等，不同市场占比差异很大，需要对照自家受众而不是照搬全局叙事。</p>
<p class="text-base md:text-lg leading-relaxed">优化上应同时抓内容与工程：持续产出能回答真实问题的稿件，配合<a href="/zh/seo/website-structure" class="text-primary hover:underline">网站结构</a>、性能、结构化数据与<a href="/zh/seo/link-building" class="text-primary hover:underline">外链建设</a>，让页面既可被理解、也可被可靠抓取。</p>
</div>

<div class="space-y-4" id="paid-traffic">
<h3 class="text-lg font-semibold" id="5-paid-traffic">5. 付费流量（Paid Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">付费流量通过搜索、社交、信息流、展示与视频等广告买入，优点是起量快、定向细、可随时加减预算；缺点是停止投放后流量通常同步消失。实务上更宜搭配长尾词与清晰落地页，用质量得分、转化成本与回收周期来迭代，而不是只追热门大词。</p>
</div>

<div class="space-y-4" id="social-traffic">
<h3 class="text-lg font-semibold" id="6-social-traffic">6. 社交流量（Social Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">社交流量来自 Facebook、X/Twitter、LinkedIn、Instagram、Pinterest、小红书、TikTok 等平台的可点击链接；不同业态侧重点不同——B2B 往往吃 LinkedIn 与专业长文，B2C 更依赖视觉平台与达人分发。无论渠道，内容里要有明确 CTA，发布时间、素材形态与评论维护也需要按平台习惯做实验，而不是一套素材全平台硬发。</p>
</div>

<div class="space-y-4" id="email-traffic">
<h3 class="text-lg font-semibold" id="7-email-traffic">7. 邮件流量（Email Traffic）</h3>
<p class="text-base md:text-lg leading-relaxed">邮件流量来自订阅者点击邮件中的链接。列表质量、主题与正文相关性、发送节奏、移动端排版，都会显著影响点击与转化。若不在链接上标注 UTM 等参数，许多桌面与移动邮件客户端会把访问记成「直接」，从而低估邮件渠道；建议在模板层统一拼接 <code class="bg-muted px-2 py-1 rounded text-sm">utm_source=email</code> 等字段，并定期抽查模板版本。进阶做法还包括分段发送、自动化旅程与 A/B 测试；Mailchimp、SendGrid、Constant Contact 等工具能帮助沉淀打开率、点击率与转化路径。</p>
</div>
</div>

<div class="space-y-6" id="traffic-comparison">
<h2 class="text-2xl font-bold" id="traffic-types-comparison-table">流量类型对比表</h2>
<p class="text-base md:text-lg leading-relaxed">不同渠道在获客难度、成本、转化与长期价值上差异很大。下表用于快速对照，实际仍要结合行业、客单价与复购来解读。</p>
<div class="overflow-x-auto my-6"><table class="w-full border-collapse border border-border"><thead><tr class="bg-muted"><th class="border border-border px-4 py-3 text-left font-semibold">流量类型</th><th class="border border-border px-4 py-3 text-left font-semibold">获取难度</th><th class="border border-border px-4 py-3 text-left font-semibold">成本</th><th class="border border-border px-4 py-3 text-left font-semibold">转化率</th><th class="border border-border px-4 py-3 text-left font-semibold">长期价值</th><th class="border border-border px-4 py-3 text-left font-semibold">可控性</th></tr></thead><tbody><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">直接流量</td><td class="border border-border px-4 py-3">高（需要品牌知名度）</td><td class="border border-border px-4 py-3">低（无直接成本）</td><td class="border border-border px-4 py-3">高（用户对品牌有认知）</td><td class="border border-border px-4 py-3">高（忠实用户）</td><td class="border border-border px-4 py-3">低（依赖品牌建设）</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">自然流量</td><td class="border border-border px-4 py-3">中-高（需要SEO优化）</td><td class="border border-border px-4 py-3">低（主要是时间成本）</td><td class="border border-border px-4 py-3">中-高（取决于关键词）</td><td class="border border-border px-4 py-3">非常高（长期复利）</td><td class="border border-border px-4 py-3">中（可优化但需时间）</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">付费流量</td><td class="border border-border px-4 py-3">低（可立即启动）</td><td class="border border-border px-4 py-3">高（需要持续投入）</td><td class="border border-border px-4 py-3">中-高（取决于定位）</td><td class="border border-border px-4 py-3">低（停止付费即停止）</td><td class="border border-border px-4 py-3">非常高（完全可控）</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">推荐流量</td><td class="border border-border px-4 py-3">中（需要外链建设）</td><td class="border border-border px-4 py-3">低-中（可能涉及合作成本）</td><td class="border border-border px-4 py-3">中（取决于来源质量）</td><td class="border border-border px-4 py-3">高（提升SEO权威性）</td><td class="border border-border px-4 py-3">中（需要持续维护）</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">社交流量</td><td class="border border-border px-4 py-3">中（需要内容营销）</td><td class="border border-border px-4 py-3">低-中（时间或广告成本）</td><td class="border border-border px-4 py-3">中（取决于平台和内容）</td><td class="border border-border px-4 py-3">中（需要持续运营）</td><td class="border border-border px-4 py-3">中（受平台算法影响）</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">邮件流量</td><td class="border border-border px-4 py-3">中（需要建立邮件列表）</td><td class="border border-border px-4 py-3">低（邮件服务成本）</td><td class="border border-border px-4 py-3">高（精准用户群体）</td><td class="border border-border px-4 py-3">高（可重复触达）</td><td class="border border-border px-4 py-3">高（完全可控）</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Dark Traffic</td><td class="border border-border px-4 py-3">-（无法准确追踪）</td><td class="border border-border px-4 py-3">-（隐藏在其他流量中）</td><td class="border border-border px-4 py-3">低（通常被误判为直接流量）</td><td class="border border-border px-4 py-3">-（影响数据分析准确性）</td><td class="border border-border px-4 py-3">低（难以控制）</td></tr></tbody></table></div>
<p class="text-base md:text-lg leading-relaxed">上表仅为粗粒度参照；若环境与政策变化，请以官方文档与自家报表为准。</p>
</div>

<div class="space-y-8" id="abnormal-traffic">
<h2 class="text-2xl font-bold" id="other-abnormal-traffic-causes">其他异常流量原因</h2>
<p class="text-base md:text-lg leading-relaxed">除了 Dark Traffic，报表里还会出现技术故障、人为配置失误与外部环境带来的「噪音」。更系统的成因与治理思路，也可对照<a href="/zh/seo/dark-traffic" class="text-primary hover:underline">无法归因流量专文</a>。</p>

<h3 class="text-lg font-semibold" id="1-technical-reasons">一、技术性原因</h3>
<p class="text-base md:text-lg leading-relaxed"><strong>基础设施：</strong>若所有渠道在同一时刻断崖下跌，优先排查宕机、机房或网络设备故障，以及大促下的容量瓶颈；应配合监控、告警、负载均衡与 CDN，把「全站不可用」与「单一渠道波动」区分开。</p>
<p class="text-base md:text-lg leading-relaxed"><strong>攻击与异常爬虫：</strong>若访问量暴涨但跳出率极高、或单 IP 高频扫登录等敏感路径，要怀疑 DDoS、恶意抓取或脚本误触；可通过 WAF、限速与日志审计收敛噪声，再回看业务指标是否恢复正常。</p>

<h3 class="text-lg font-semibold" id="2-human-factors">二、人为操作因素</h3>
<p class="text-base md:text-lg leading-relaxed">内部同事测试、未过滤的公司 IP、错误的跟踪代码部署、误用过滤器或跨域/跨子域未打通，都会让数据突然「归零」或长期偏低。建议把 GA/GTM 变更纳入清单化发布流程，并定期用预览与 DebugView 复核。</p>

<h3 class="text-lg font-semibold" id="3-external-interference">三、外部环境干扰</h3>
<p class="text-base md:text-lg leading-relaxed">政策调整、行业热点、节假日与淡旺季，会让整类站点同向波动。应对方式是建立事件时间轴、订阅关键词快讯、用历史同期与业务日历对照，避免把结构性变化误判为增长团队失误。</p>

<h3 class="text-lg font-semibold" id="4-data-collection">四、采集与处理缺陷</h3>
<p class="text-base md:text-lg leading-relaxed">浏览器缓存、广告拦截与隐私模式会导致部分会话根本打不上点；在合规前提下，可考虑服务端转发、第一方域收集或补充日志级数据，减少「客户端完全看不见」的盲区。</p>
</div>

<div class="space-y-6" id="traffic-discussion">
<h2 class="text-2xl font-bold" id="a-discussion-about-traffic">一点关于流量的漫谈</h2>
<p class="text-base md:text-lg leading-relaxed">从逻辑上，用户进入网站只有两条路：要么「直接」打开（记得域名、书签、手输），要么「点击某个超链接」——后者在 GA 的 source/medium 里大量以 referral、organic、social 等标签出现，本质都是「经链接跳转」。</p>
<div class="overflow-x-auto my-6 md:my-8"><table class="min-w-full border-collapse border border-border"><thead><tr class="bg-muted"><th class="border border-border px-4 py-2 text-left">google / organic</th><th class="border border-border px-4 py-2 text-left">l.instagram.com / referral</th><th class="border border-border px-4 py-2 text-left">(direct) / (none)</th><th class="border border-border px-4 py-2 text-left">Facebook / social</th></tr></thead><tbody><tr><td class="border border-border px-4 py-2">yahoo / organic</td><td class="border border-border px-4 py-2">in.search.yahoo.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">m.facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">l.facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">lm.facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">t.co / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">yandex.ru / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">mp.weixin.qq.com / referral（不确定）</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr></tbody></table></div>
<p class="text-base md:text-lg leading-relaxed">因此，邮件、即时通讯、短链与部分社媒跳转，在报表里常常仍显示为 referral；与「从独立博客点过来」相比，差别更多在场景，而不是技术定义。平台为安全做的 Link Shim、短链跳转，也会改变你看到的引荐域名。</p>
<p class="text-base md:text-lg leading-relaxed">反过来，如果内容场景不允许放可点击链接（例如部分短视频与笔记），用户可能改去搜品牌词，从表现上更像 organic，这会让社交投入难以在原渠道里直接对齐。</p>
<p class="text-base md:text-lg leading-relaxed">把搜索引擎想成「体量极大的中转站」也有帮助：结果页上的每一条蓝色标题，本质上都是临时中转页，用户再点击才到你的落地页——这与导航站、目录列表没有逻辑冲突，只是规模与意图不同。</p>
<p class="text-base md:text-lg leading-relaxed"><strong>结论：</strong>凡是通过链接把用户送到站内的动作，都可以纳入广义的链接运营；它与自然搜索、社交分发同样重要，值得用统一的数据纪律（标记、命名、审计）来管理。</p>
</div>`;

// --- en website-traffic: patch types block (index 2) + abnormal (index 7) + discussion - we'll replace whole blocks content

const enTypesHtml = `<h2 class="text-2xl font-bold" id="types-of-traffic">Types of Traffic</h2><div class="space-y-4" id="direct-traffic"><h3 class="text-lg font-semibold" id="1-direct-traffic">1. Direct Traffic</h3><p class="text-base md:text-lg leading-relaxed">Direct traffic covers typed URLs, bookmarks, autofill, and paste-into-bar visits. These users often already know the brand—filter internal IPs so tests do not pollute production metrics. The same bucket also hides <a href="/seo/dark-traffic" class="text-primary hover:underline">dark traffic</a> when referrers drop (messengers, some mail clients, in-app browsers).</p><p class="text-base md:text-lg leading-relaxed">Treat “high direct” as a hypothesis to validate with landing pages, campaign calendars, and spot checks—not as a pure brand-health score.</p></div><div class="space-y-4" id="dark-traffic"><h3 class="text-lg font-semibold" id="2-dark-traffic">2. Dark Traffic</h3><p class="text-base md:text-lg leading-relaxed">Dark traffic is traffic your analytics cannot attribute cleanly: clicks from closed platforms, email, or mobile shells often arrive without usable referrer data and get folded into <code>(direct) / (none)</code>. Technical causes include HTTPS→HTTP transitions, in-app webviews, file links, and strict Referrer-Policy choices.</p><p class="text-base md:text-lg leading-relaxed">The “Dark Social” idea—coined in a <a href="https://www.theatlantic.com/technology/archive/2012/10/dark-social-we-have-the-whole-history-of-the-web-wrong/263523/" target="_blank" rel="noopener noreferrer nofollow" class="text-primary hover:underline">2012 Atlantic piece</a>—describes sharing that analytics under-counts. For a full playbook, read <a href="/seo/dark-traffic" class="text-primary hover:underline">Dark traffic: definition &amp; solutions</a>.</p></div><div class="space-y-4" id="referral-traffic"><h3 class="text-lg font-semibold" id="3-referral-traffic">3. Referral Traffic</h3><p class="text-base md:text-lg leading-relaxed">Referral traffic is any visit that arrives via a hyperlink on another site: media, forums, directories, partners, and parts of social can all appear here depending on tagging. Strong referrals double as SEO signals; monitor for spam referrers and scraper bursts so they do not distort funnels.</p></div><div class="space-y-4" id="organic-traffic"><h3 class="text-lg font-semibold" id="4-organic-traffic">4. Organic Traffic</h3><p class="text-base md:text-lg leading-relaxed">Organic traffic comes from unpaid search results. Engines differ by market (Google, Bing, Baidu, Yahoo, Yandex, etc.); win by publishing genuinely useful answers, tightening <a href="/seo/website-structure" class="text-primary hover:underline">site structure</a>, performance, structured data, and <a href="/seo/link-building" class="text-primary hover:underline">links</a> that reinforce expertise.</p></div><div class="space-y-4" id="paid-traffic"><h3 class="text-lg font-semibold" id="5-paid-traffic">5. Paid Traffic</h3><p class="text-base md:text-lg leading-relaxed">Paid traffic is bought through search, social, display, video, or programmatic channels. It starts fast and scales with budget, but usually stops when spend stops—pair it with creative testing, landing-page discipline, and blended attribution so you are not fooled by last-click vanity.</p></div><div class="space-y-4" id="social-traffic"><h3 class="text-lg font-semibold" id="6-social-traffic">6. Social Traffic</h3><p class="text-base md:text-lg leading-relaxed">Social traffic flows from platforms such as Facebook, X/Twitter, LinkedIn, Instagram, Pinterest, Xiaohongshu, and TikTok. B2B teams often lean on LinkedIn thought leadership; B2C leans on visual networks and creators. Strong CTAs, native creative formats, and community care matter more than posting the same asset everywhere.</p></div><div class="space-y-4" id="email-traffic"><h3 class="text-lg font-semibold" id="7-email-traffic">7. Email Traffic</h3><p class="text-base md:text-lg leading-relaxed">Email traffic is clicks from newsletters, lifecycle drips, and transactional messages. List quality, relevance, cadence, and mobile rendering drive performance. Without UTM (or equivalent) tags, many clients strip referrers and those visits look “direct”—standardize parameters at the template layer and audit templates when ESPs change layouts.</p></div>`;

const enCompareHtml = `<h2 class="text-2xl font-bold" id="traffic-types-comparison-table">Traffic Types Comparison Table</h2><p class="text-base md:text-lg leading-relaxed">Use the matrix below as a coarse map; your economics and sales motion still rule the final prioritization.</p><div class="overflow-x-auto my-6"><table class="w-full border-collapse border border-border"><thead><tr class="bg-muted"><th class="border border-border px-4 py-3 text-left font-semibold">Traffic Type</th><th class="border border-border px-4 py-3 text-left font-semibold">Acquisition Difficulty</th><th class="border border-border px-4 py-3 text-left font-semibold">Cost</th><th class="border border-border px-4 py-3 text-left font-semibold">Conversion Rate</th><th class="border border-border px-4 py-3 text-left font-semibold">Long-term Value</th><th class="border border-border px-4 py-3 text-left font-semibold">Controllability</th></tr></thead><tbody><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Direct Traffic</td><td class="border border-border px-4 py-3">High (requires brand awareness)</td><td class="border border-border px-4 py-3">Low (no direct cost)</td><td class="border border-border px-4 py-3">High (users know the brand)</td><td class="border border-border px-4 py-3">High (loyal users)</td><td class="border border-border px-4 py-3">Low (depends on brand building)</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Organic Traffic</td><td class="border border-border px-4 py-3">Medium-High (requires SEO optimization)</td><td class="border border-border px-4 py-3">Low (mainly time cost)</td><td class="border border-border px-4 py-3">Medium-High (depends on keywords)</td><td class="border border-border px-4 py-3">Very High (long-term compound effect)</td><td class="border border-border px-4 py-3">Medium (can optimize but takes time)</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Paid Traffic</td><td class="border border-border px-4 py-3">Low (can start immediately)</td><td class="border border-border px-4 py-3">High (requires ongoing investment)</td><td class="border border-border px-4 py-3">Medium-High (depends on targeting)</td><td class="border border-border px-4 py-3">Low (stops when payment stops)</td><td class="border border-border px-4 py-3">Very High (fully controllable)</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Referral Traffic</td><td class="border border-border px-4 py-3">Medium (requires link building)</td><td class="border border-border px-4 py-3">Low-Medium (may involve partnership costs)</td><td class="border border-border px-4 py-3">Medium (depends on source quality)</td><td class="border border-border px-4 py-3">High (improves SEO authority)</td><td class="border border-border px-4 py-3">Medium (requires ongoing maintenance)</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Social Traffic</td><td class="border border-border px-4 py-3">Medium (requires content marketing)</td><td class="border border-border px-4 py-3">Low-Medium (time or ad costs)</td><td class="border border-border px-4 py-3">Medium (depends on platform and content)</td><td class="border border-border px-4 py-3">Medium (requires ongoing operation)</td><td class="border border-border px-4 py-3">Medium (affected by platform algorithms)</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Email Traffic</td><td class="border border-border px-4 py-3">Medium (requires building email list)</td><td class="border border-border px-4 py-3">Low (email service costs)</td><td class="border border-border px-4 py-3">High (precise user group)</td><td class="border border-border px-4 py-3">High (repeatable reach)</td><td class="border border-border px-4 py-3">High (fully controllable)</td></tr><tr class="hover:bg-muted/50"><td class="border border-border px-4 py-3 font-semibold">Dark Traffic</td><td class="border border-border px-4 py-3">- (cannot be accurately tracked)</td><td class="border border-border px-4 py-3">- (hidden in other traffic)</td><td class="border border-border px-4 py-3">Low (usually misidentified as direct traffic)</td><td class="border border-border px-4 py-3">- (affects data analysis accuracy)</td><td class="border border-border px-4 py-3">Low (difficult to control)</td></tr></tbody></table></div><p class="text-base md:text-lg leading-relaxed">Figures are directional; validate with your own funnels.</p>`;

const enAbnormalHtml = `<h2 class="text-2xl font-bold" id="other-abnormal-traffic-causes">Other Abnormal Traffic Causes</h2><p class="text-base md:text-lg leading-relaxed">Beyond dark traffic, analysts still see spikes or cliffs from infrastructure failures, human misconfiguration, and macro shocks. Keep <a href="/seo/dark-traffic" class="text-primary hover:underline">the dark-traffic guide</a> open when you are auditing “weird direct.”</p><h3 class="text-lg font-semibold" id="1-technical-reasons">1. Technical Reasons</h3><p class="text-base md:text-lg leading-relaxed"><strong>Infrastructure:</strong> If every channel drops in the same minute, suspect outages, networking faults, or capacity limits during launches. Monitoring, autoscaling, CDNs, and incident playbooks matter more than tweaking creatives.</p><p class="text-base md:text-lg leading-relaxed"><strong>Abuse &amp; bots:</strong> Sudden surges paired with 90%+ bounce or credential stuffing patterns warrant WAF rules, rate limits, and log review before you reinterpret marketing ROI.</p><h3 class="text-lg font-semibold" id="2-human-factors">2. Human Factors</h3><p class="text-base md:text-lg leading-relaxed">Internal testers, unfiltered office IPs, broken tags, bad filters, and missing cross-domain linking can zero out data or silently mislabel sessions. Treat analytics changes like code releases—review, stage, and verify in DebugView.</p><h3 class="text-lg font-semibold" id="3-external-interference">3. External Interference</h3><p class="text-base md:text-lg leading-relaxed">Regulation, news cycles, and seasonality move whole categories together. Maintain a timeline of external events and compare year-over-year with care; otherwise a macro swing looks like an internal regression.</p><h3 class="text-lg font-semibold" id="4-data-collection-and-processing-defects">4. Data Collection Defects</h3><p class="text-base md:text-lg leading-relaxed">Ad blockers, strict consent modes, and cached pages shrink client-side coverage. Server-side tagging, first-party endpoints, and (where legal) log-level backups help close the gap without chasing impossible precision.</p>`;

const enHowAnalyzeHtml = `<h2 class="text-2xl font-bold" id="how-to-analyze-traffic">How to Analyze Website Traffic</h2>
<p class="text-base md:text-lg leading-relaxed"><strong>Tooling:</strong> Pair <a href="https://analytics.google.com/?utm_source=kostja&amp;utm_medium=blog" target="_blank" rel="noopener noreferrer" class="text-primary hover:underline">Google Analytics</a> with <a href="https://search.google.com/search-console?utm_source=kostja&amp;utm_medium=blog" target="_blank" rel="noopener noreferrer" class="text-primary hover:underline">Search Console</a> so acquisition reports sit next to query and landing-page reality.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Metrics:</strong> Anchor reviews on sessions, engaged users, engagement rate, conversions, and pathing—not raw hits. Quality beats volume when budgets are finite.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Sources and behavior:</strong> Compare organic, paid, referral, email, and social side by side, then inspect landing pages, exit pages, and funnels. Tie insights back to <a href="/seo/website-structure" class="text-primary hover:underline font-semibold">site structure</a> and <a href="/seo/internal-links" class="text-primary hover:underline font-semibold">internal links</a> so UX fixes follow the data.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Attribution:</strong> Most journeys are multi-touch; read assisted conversions and path reports before you starve a channel for lacking last-click credit.</p>`;

const enHowTrackHtml = `<h2 class="text-2xl font-bold" id="how-to-track-traffic-sources">How to Track Traffic Sources</h2>
<p class="text-base md:text-lg leading-relaxed">Campaign links need consistent <code class="bg-muted px-2 py-1 rounded">utm_source</code>, <code class="bg-muted px-2 py-1 rounded">utm_medium</code>, <code class="bg-muted px-2 py-1 rounded">utm_campaign</code>, plus optional <code class="bg-muted px-2 py-1 rounded">utm_content</code> and <code class="bg-muted px-2 py-1 rounded">utm_term</code>—document the dictionary once and reuse it everywhere.</p>
<p class="text-base md:text-lg leading-relaxed">Example: <code class="bg-muted px-2 py-1 rounded text-xs break-all">https://example.com/?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=weekly_update</code>. Without that discipline, email and social clicks masquerade as direct traffic.</p>
<p class="text-base md:text-lg leading-relaxed">Inside GA4, lock in conversions, filters for internal IPs, spam defenses, cross-domain measurement, and (when needed) enhanced commerce or server-side tagging. For referrals, maintain deny/allow lists and periodically audit backlinks with <a href="https://ahrefs.com/?utm_source=kostja&amp;utm_medium=blog" target="_blank" rel="noopener noreferrer nofollow" class="text-primary hover:underline">Ahrefs</a> or <a href="https://majestic.com/?utm_source=kostja&amp;utm_medium=blog" target="_blank" rel="noopener noreferrer nofollow" class="text-primary hover:underline">Majestic</a> so scrapers do not dominate your trends.</p>`;

const enBestPracticesMerged = `<h2 class="text-2xl font-bold" id="traffic-analysis-best-practices">Traffic Analysis Best Practices</h2>
<p class="text-base md:text-lg leading-relaxed">Optimize for converting visits, not vanity traffic. Compare cohorts and assisted conversions before reallocating spend.</p>
<p class="text-base md:text-lg leading-relaxed">Let editorial calendars follow performance data: double down on URLs that earn engaged sessions and retire ideas that bounce.</p>
<p class="text-base md:text-lg leading-relaxed">Pick an attribution story (first-touch for awareness, data-driven for commerce, etc.) and keep it stable quarter to quarter so leadership sees a coherent narrative.</p>
<p class="text-base md:text-lg leading-relaxed">Schedule weekly or monthly reviews with anomaly alerts—traffic is only a lagging indicator when nobody watches it.</p>`;

const enDiscussionHtml = `<h2 class="text-2xl font-bold" id="a-discussion-about-traffic">A Discussion About Traffic</h2><p class="text-base md:text-lg leading-relaxed">Conceptually, visitors either type you in or click a hyperlink. Everything in the acquisition reports is a refinement of “clicked something” plus the metadata your tools can still see.</p><div class="overflow-x-auto my-6 md:my-8"><table class="min-w-full border-collapse border border-border"><thead><tr class="bg-muted"><th class="border border-border px-4 py-2 text-left">google / organic</th><th class="border border-border px-4 py-2 text-left">l.instagram.com / referral</th><th class="border border-border px-4 py-2 text-left">(direct) / (none)</th><th class="border border-border px-4 py-2 text-left">Facebook / social</th></tr></thead><tbody><tr><td class="border border-border px-4 py-2">yahoo / organic</td><td class="border border-border px-4 py-2">in.search.yahoo.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">m.facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">l.facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">lm.facebook.com / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">t.co / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">yandex.ru / referral</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr><tr class="bg-muted/50"><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2">mp.weixin.qq.com / referral (uncertain)</td><td class="border border-border px-4 py-2"></td><td class="border border-border px-4 py-2"></td></tr></tbody></table></div><p class="text-base md:text-lg leading-relaxed">That is why newsletters, messengers, shorteners, and parts of social can still appear as referral—even when you mentally bucket them elsewhere. Link shims and privacy-preserving redirects also rewrite what you see in reports.</p><p class="text-base md:text-lg leading-relaxed">When a network discourages outbound links (short video, certain feeds), people search the brand instead; social effort then shows up under organic branded queries, which complicates channel accounting.</p><p class="text-base md:text-lg leading-relaxed">Search itself is a giant hop: each SERP line is an intermediate surface until someone clicks through—so organic and referral narratives are complements, not opposites.</p><p class="text-base md:text-lg leading-relaxed"><strong>Conclusion:</strong> Any strategy that earns a tracked click is part of your link ecosystem; fund it with the same rigor you apply to SEO and paid media.</p>`;

// --- zh dark-traffic: all html after tldr
const zhDarkHtmlBlocks = [
  {
    type: "html",
    className: "space-y-6 pt-8 border-t border-border",
    html: `<h2 class="text-2xl font-bold" id="what-is-dark-traffic">Dark Traffic 是什么？</h2>
<p class="text-base md:text-lg leading-relaxed">Dark Traffic（无法归因流量）指分析工具难以准确还原来源的访问：用户从封闭平台、邮件或 App 内网页容器点链接进来时，往往不带可用的 Referrer，报表里便与「直接流量」混在一起。</p>
<p class="text-base md:text-lg leading-relaxed">在 Google Analytics 等产品中，这会让 Direct 桶虚高、其余渠道被低估，进而扭曲渠道 ROI 与内容复盘。对搜索引擎和营销团队来说，这类访问像是「看不见」的——不是不存在，而是默认报表没有把它们放回真实场景。</p>
<p class="text-base md:text-lg leading-relaxed">2012 年<a href="https://www.theatlantic.com/technology/archive/2012/10/dark-social-we-have-the-whole-history-of-the-web-wrong/263523/?utm_source=kostja&amp;utm_medium=blog" target="_blank" rel="noopener noreferrer nofollow" class="text-primary hover:underline">《大西洋月刊》</a>在一篇文章中提出「暗社交」（Dark Social），描述那些发生在私信、邮件与封闭分享场景、却难以被常规分析完整度量的传播行为。</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="causes">Dark Traffic 的成因</h2>
<p class="text-base md:text-lg leading-relaxed"><strong>技术侧：</strong>HTTPS 降级到 HTTP、应用内浏览器、PDF/Office 等本地文件里的链接、以及站点配置的 Referrer Policy，都会让引荐信息变短甚至为空；用户开启更严格的隐私设置时，情况会更常见。</p>
<p class="text-base md:text-lg leading-relaxed"><strong>平台侧：</strong>WhatsApp、微信、Discord、Slack 等私聊，短信、加密邮箱、App 内私信，以及部分短链默认参数，都会把流量「推」向不可见来源；这与渠道是否重要无关，只与浏览器愿不愿意交出上一跳有关。</p>
<p class="text-base md:text-lg leading-relaxed"><strong>合规与隐私：</strong>ATT、Cookie 同意、GDPR/CCPA 与广告拦截叠加后，跨站、跨设备的连续叙事更难拼齐；这不是分析团队「不努力」，而是采集边界整体收紧。</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="impact">Dark Traffic 的影响</h2>
<p class="text-base md:text-lg leading-relaxed">当 Dark Traffic 偏高时，你会看到直接渠道异常「胖」、社交/邮件等渠道偏「瘦」，进而误判哪条链路真正带来转化，也可能把预算从有效的私域运营上挪走。内容团队同样吃亏：看不清哪篇素材在微信或邮件里被转发，就无法迭代话术与落地页。</p>
<p class="text-base md:text-lg leading-relaxed">一个典型场景是：某电商站发现 Direct 占到六成但转化很差，复盘后才发现大量链接来自微信私聊分享——没有 UTM 与专用落地参数时，这些访问只能堆在 Direct 里，微信运营的贡献被系统性低估。</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="identify">如何识别 Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed">把它当作诊断问题而不是道德问题：若 Direct 占比长期高于经验区间、且伴随低转化、偏高新或活动期尖峰，就要怀疑未标记活动与丢 Referrer。对比移动端 vs 桌面、不同落地页与活动日历，常能很快缩小范围。</p>
<p class="text-base md:text-lg leading-relaxed">在 Google Analytics 中，可结合「获取 &gt; 流量获取」里的来源/媒介、着陆页与行为指标，对照投放清单做抽样；对外发链接统一加 UTM 或规范化的自定义参数后，再看 Direct 是否回落，是最便宜的验证实验。</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="reduce">如何减少 Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed"><strong>工程：</strong>尽量全站 HTTPS，避免混合内容；审慎设置 Referrer Policy；多域名场景配好跨域与第一方 Cookie 策略；必要时引入服务端转发，减轻浏览器拦截对报表的冲击。</p>
<p class="text-base md:text-lg leading-relaxed"><strong>运营：</strong>对外分享的每一条链接都应能映射回活动——统一命名 <code class="bg-muted px-2 py-1 rounded text-sm">utm_source / utm_medium / utm_campaign</code>，在短信、私域、邮件与线下二维码上同样执行。短链工具要选能携带参数、且团队能审计跳转日志的方案。</p>
<p class="text-base md:text-lg leading-relaxed"><strong>流程：</strong>用 GTM 或脚本减少手工拼参错误，把「带参分享」写进活动模板；每月做一次 Direct 审计，看是否出现新的未标记活动或追踪回归。</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="related-issues">其他导致归因漂移的问题</h2>
<p class="text-base md:text-lg leading-relaxed">未标记的营销活动、SPA 路由切换时未触发测量、HTTP/HTTPS 混用、以及跨设备同意模式不一致，都会让「看起来像 Dark Traffic」的噪声放大。处理顺序应是：先修标记与采集，再讨论渠道战略；否则 Direct 桶会把结论带偏。</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="best-practices">Dark Traffic 的最佳实践</h2>
<p class="text-base md:text-lg leading-relaxed">把 UTM 规范写进协作手册并用工具自动落参；为社交、邮件、短信与线下物料分别保留可读的活动名；定期培训投放与增长团队，让「每条外链可还原」成为默认纪律；技术侧保持 HTTPS、Referrer Policy 与跨域配置与测量代码同步迭代。</p>
<p class="text-base md:text-lg leading-relaxed">当治理到位后，Direct 才更接近「真实的品牌直达」，其余灰色流量会被挪回可行动的活动维度，复盘与预算讨论也会轻松得多。</p>`,
  },
  {
    type: "section",
    id: "conclusion",
    level: 2,
    title: "结论",
    paragraphs: [
      "Dark traffic 多数是归因与标记问题：先统一 UTM、同意模式与跨端旅程，再讨论投放与内容策略，否则「Direct」桶会把结论带偏。",
      "让 Search Console 的查询与着陆路径、分析工具里的渠道定义对齐，管理层才能看到同一套叙事。",
    ],
    subSections: [],
    showDivider: true,
  },
];

const enDarkHtmlBlocks = [
  {
    type: "html",
    className: "space-y-6 pt-8 border-t border-border",
    html: `<h2 class="text-2xl font-bold" id="what-is-dark-traffic">What is Dark Traffic?</h2>
<p class="text-base md:text-lg leading-relaxed">Dark traffic (unattributable traffic) describes visits where analytics cannot recover a trustworthy referrer—common when users come from messengers, mail clients, or in-app browsers that strip or shorten the previous hop.</p>
<p class="text-base md:text-lg leading-relaxed">In Google Analytics those sessions often land in <code>(direct) / (none)</code>, inflating direct share and starving social, email, or partner channels of credit. That makes ROI stories wrong even when marketing execution is fine.</p>
<p class="text-base md:text-lg leading-relaxed">Journalists at <a href="https://www.theatlantic.com/technology/archive/2012/10/dark-social-we-have-the-whole-history-of-the-web-wrong/263523/?utm_source=kostja&amp;utm_medium=blog" target="_blank" rel="noopener noreferrer nofollow" class="text-primary hover:underline">The Atlantic</a> popularized the term “Dark Social” in 2012 to highlight sharing that happens off the public feed graph yet still drives real clicks.</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="causes-of-dark-traffic">Causes of Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed"><strong>Technical:</strong> HTTPS→HTTP downgrades, embedded document links, in-app webviews, and aggressive Referrer-Policy headers all remove or truncate referrer data before your tag fires.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Platform:</strong> Private chats (WhatsApp, WeChat, Slack, etc.), SMS, encrypted mail, and some shorteners simply never expose the original publisher URL to your analytics endpoint.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Privacy &amp; consent:</strong> ATT, cookie banners, ad blockers, and regional privacy rules reduce cross-site continuity—expect more unattributed hops, not fewer, over time.</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="impact-of-dark-traffic">Impact of Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed">Mis-labeled traffic hides which creative, community, or lifecycle program actually works. Teams over-invest in what looks like “brand search” and under-fund high-performing dark social loops.</p>
<p class="text-base md:text-lg leading-relaxed">A classic pattern: direct share spikes with awful conversion quality until you discover WeChat or email links lacked tracking parameters—nothing mystical, just missing tags.</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="how-to-identify-dark-traffic">How to Identify Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed">Look for direct sessions that break brand baselines: too many new users, suspicious landing pages, campaign-shaped time windows, or mobile-heavy mixes. Compare behavior to known good channels and validate with annotated marketing calendars.</p>
<p class="text-base md:text-lg leading-relaxed">In GA4, pair acquisition reports with landing-page and device dimensions; run a controlled experiment where you add UTMs to outbound shares and watch whether direct falls—if it does, you found leakage, not “more brand love.”</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="how-to-reduce-dark-traffic">How to Reduce Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed"><strong>Engineering:</strong> Enforce HTTPS, tighten Referrer Policy deliberately (not accidentally), wire SPA transitions to measurement, and adopt server-side tagging when client scripts are blocked.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Marketing ops:</strong> Require UTMs (or your equivalent) on every external surface—paid, owned, and partner—and document naming conventions. Short links must preserve parameters and remain auditable.</p>
<p class="text-base md:text-lg leading-relaxed"><strong>Governance:</strong> Automate parameter injection via GTM or CI templates, and schedule monthly direct-traffic reviews so regressions surface before quarterly business reviews.</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="other-issues-causing-dark-traffic">Other Issues Causing Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed">Unlabeled campaigns, SPA measurement gaps, mixed HTTP/HTTPS environments, and broken cross-domain linking all mimic dark traffic. Fix instrumentation first; channel strategy second.</p>`,
  },
  {
    type: "html",
    className: "space-y-6",
    html: `<h2 class="text-2xl font-bold" id="best-practices-for-dark-traffic">Best Practices for Dark Traffic</h2>
<p class="text-base md:text-lg leading-relaxed">Publish a short UTM style guide, enforce it with tooling, train every stakeholder who can paste a link, and pair technical SEO hygiene (TLS, policy headers) with analytics QA whenever you ship a new front-end architecture.</p>
<p class="text-base md:text-lg leading-relaxed">Once direct traffic mostly reflects true navigational intent, downstream forecasting, creative testing, and exec reporting all get easier.</p>`,
  },
  {
    type: "section",
    id: "conclusion",
    level: 2,
    title: "Conclusion",
    paragraphs: [
      "Dark traffic is mostly an attribution labeling problem: fix UTM discipline, consent-mode gaps, and cross-device journeys before you rewrite strategy based on inflated \"direct\" buckets.",
      "Keep Search Console queries, landing paths, and analytics channel definitions aligned so stakeholders see one coherent story.",
    ],
    subSections: [],
    showDivider: true,
  },
];

function main() {
  // zh website-traffic
  const zhWt = JSON.parse(
    fs.readFileSync(path.join(root, "content/seo/zh/website-traffic.json"), "utf8"),
  );
  zhWt.blogLayout.modifiedDate = "2026年4月21日";
  zhWt.blocks[1].html = zhWebsiteTrafficHtml;
  zhWt.blocks[2].paragraphs = [
    "本文从七种流量类型出发，把可读性与数据纪律放在一起看：先弄清标记与口径，再谈投放与内容。",
    "建议把文中的检查项拆成可验证的小任务，用报表与实验复盘，而不是凭感觉调渠道。若平台政策或测量接口有变，以官方说明为准并回写站内表述。",
  ];
  writeJson("content/seo/zh/website-traffic.json", zhWt);

  // en website-traffic
  const enWt = JSON.parse(
    fs.readFileSync(path.join(root, "content/seo/en/website-traffic.json"), "utf8"),
  );
  enWt.blogLayout.modifiedDate = "April 21, 2026";
  enWt.blocks[3].html = enTypesHtml;
  enWt.blocks[4].html = enCompareHtml;
  enWt.blocks[5].html = enHowAnalyzeHtml;
  enWt.blocks[6].html = enHowTrackHtml;
  enWt.blocks[7].html = enBestPracticesMerged;
  enWt.blocks[8].html = enAbnormalHtml;
  enWt.blocks[9].html = enDiscussionHtml;
  writeJson("content/seo/en/website-traffic.json", enWt);

  // zh dark-traffic
  const zhDt = JSON.parse(
    fs.readFileSync(path.join(root, "content/seo/zh/dark-traffic.json"), "utf8"),
  );
  zhDt.blocks = [zhDt.blocks[0], ...zhDarkHtmlBlocks, ...zhDt.blocks.slice(-2)];
  writeJson("content/seo/zh/dark-traffic.json", zhDt);

  // en dark-traffic
  const enDt = JSON.parse(
    fs.readFileSync(path.join(root, "content/seo/en/dark-traffic.json"), "utf8"),
  );
  enDt.blocks = [enDt.blocks[0], ...enDarkHtmlBlocks, ...enDt.blocks.slice(-2)];
  writeJson("content/seo/en/dark-traffic.json", enDt);

  console.log("apply-traffic-blog-prose: updated 4 JSON files.");
}

main();
