# 域名选择与 SEO · 知识块（非线性笔记）

**文件名与 slug**：本文件 basename `domain` 与站内路由 **`/seo/domain`** 对齐。

**材料范围**：公开网络检索（Google Search Central 官方文档、ICANN/IANA 根区数据库、DomainTools/NameBio 二级市场数据、Anguilla 政府公开报告、Saipx/dotappraisals/TLDFYI 独立域名估值报告、行业投融资与 YC/YC 批次统计、Hostinger 全球 TLD 市场份额数据 2026、Visionary Marketing 2026 10 万页 SEO 排名相关性研究、Archivarix/SpamZilla/NamePros 域名历史检查方法、WhoAPI 域名过期案例记录）；**未**将 Alignify 站内页面 JSON 当作事实来源复述。网摘整理日期 **2026-07-09**。

**规范对照**：[section-seo.md](../../content/sections/section-seo.md) · [technical/README.md](../../technical/README.md) · [knowledgehub/README.md](../README.md)

**本分册说明**：[seo/README.md](./README.md) · 分类：网站架构与导航

**站内文章对照**：[alignify.co/zh/seo/domain](https://alignify.co/zh/seo/domain) · `content/seo/en|zh/domain.md`（已发布；文章覆盖 EMD/PMD 基础概念、选择五步法、品牌重塑流程；本知识块补充：.ai 市场数据、域名历史检查工具链、续费风险案例、防御性注册方法论）

**与相邻知识块的边界**：[ai-product-naming.md](../insights/ai-product-naming.md)（品牌名本身的命名策略、agency案例、命名逻辑分类）；本文覆盖品牌名选定之后的**域名决策**（TLD 选型、注册、历史检查、续费、防御性注册、域名对SEO的影响）。两个知识块是**先后互补关系**：先有名字 → 再有域名；名字的决策约束域名的可行空间。

**与相邻 slug 分流**

| 维度 | **domain（本文）** | **new-domains-tld** | **url-optimization** | **subdomain-vs-subfolder** |
|------|-----|------|------|------|
| 核心问题 | 选什么 TLD？域名对品牌和 SEO 的影响？ | 新顶级域（.app/.dev/.xyz 等）与传统 .com 的差异 | URL 路径段的格式规范和规范化 | 多站点架构用子域还是子目录 |
| 输入 | 品牌名 + 预算 + 目标 TLD | TLD 本身的技术特性与定价 | 页面 URL 字符串 | 站点架构设计 |
| 产出 | 注册或购买的域名 | 对新 TLD 的认知与选型 | 规范化的 URL 结构 | 架构决策 |
| 典型问题 | "AI 产品该用 .ai 还是 .com？" | ".app 和 .dev 有什么区别？" | "同一个内容有两个 URL 怎么办？" | "博客该用 blog.example.com 还是 example.com/blog？" |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **TLD (Top-Level Domain)**：域名系统最顶层的后缀。分为 gTLD（通用顶级域，如 `.com` `.org` `.net`）和 ccTLD（国家/地区代码顶级域，如 `.ai` `.io` `.cn`）。TLD 的选择在 AI 时代已成为核心品牌信号——不同的 TLD 传递不同的品类归属和可信度。
- **ccTLD 的品牌化脱钩**：部分 ccTLD 在实际使用中已完全脱离地理含义，成为全球范围内的"品类 TLD"：`.ai` 表示 AI 公司（本属于加勒比岛国安圭拉，15,000 人口）；`.io` 表示技术/开发者工具（本属于英属印度洋领地，存在地缘政治争议）；`.co` 表示公司/初创（本属于哥伦比亚）。这种现象被称为"ccTLD 的品牌化重定义"。
- **.ai 域名**：安圭拉（Anguilla）的 ccTLD，因与 artificial intelligence 缩写巧合，已成为 AI 公司的标准 TLD。2026 年 1 月总注册量突破 100 万，每周增长约 1%。批发价 $90/年（2026 年 3 月提价 29%，从 $70 涨至 $90），零售价 $100-$220/年。2025 年安圭拉从 .ai 域名获得约 $9300 万美元收入，占全国预算近一半。2025 年 1 月起由 Identity Digital 管理注册局基础设施。
- **.io 域名**：英属印度洋领地（British Indian Ocean Territory）的 ccTLD，因与 I/O（输入/输出）的巧合，成为开发者工具和 SaaS 产品的流行选择。零售价约 $50/年。存在严重的地缘政治风险——英国、毛里求斯和美国之间的领土争议可能导致该 ccTLD 在未来被 ICANN 从根区删除。1,600,000+ 注册域名将受影响。
- **Premium domain / 精品域名**：在二级市场上以远高于注册价交易的域名。在 .ai 空间中，精品域名价格按品类分级：长尾/拼错词 $200-$2K、描述型复合词 $2K-$15K、品牌化中层 $15K-$80K、短通用词 $80K-$500K、1-2 字母/标志级 $500K-$1.2M+。已知交易：bot.ai $120万、fin.ai $100万（2025-2026）；you.ai $70万（2023）；2026 年前半年已有 15+ 个 .ai 域名成交价超 $10 万。
- **Domain Leakage / 域名泄漏**：用户因记忆或输入习惯直接输入错误域名（如把 `yourapp.ai` 输成 `yourapp.com`）导致的流量流失。是选择非 `.com` TLD 时的主要品牌风险——外部链接、口头传播、打字习惯都会产生泄漏。
- **TLD Trust Signal / TLD 信任信号**：不同 TLD 在专业受众心中的可信度不同。对 AI 产品，`.ai` 在开发者/投资人群体中的信任信号**高于** `.com`——它传递"我是 AI 原生"的信号，而 `.com` 对 AI 产品反而可能被解读为"老牌公司试图做 AI 外挂"（Saipx 2026）。但对大众用户，`.com` 的普遍可信度仍是绝对的。
- **Branded search / 品牌搜索量**：用户直接在搜索引擎输入你名称的搜索量。拥有 clean `.com` 域名的产品通常获得更高的品牌搜索量——域名本身就是一个隐形的搜索框。
- **Domain aftermarket / 域名二级市场**：已注册域名在持有人之间的交易市场。平台包括 Sedo、Afternic、Flippa、Namecheap Market。AI 域名（尤其是 .ai 和 .com）的二级市场在 2023-2026 年间价格暴涨 13 倍。
- **Domain privacy / WHOIS 隐私保护**：隐藏域名注册人姓名、邮箱和地址的服务。对 AI 初创公司，WHOIS 隐私保护是标准实践——一个可被公开查询的创始人家庭住址对创始人的安全风险不言而喻。不同 TLD 对 WHOIS 隐私的政策不同；.ai 在 2025 年 Identity Digital 接管后完善了隐私保护。
- **小众 ccTLD 的品牌化**：部分人口极少、地理概念模糊的 ccTLD 在开发者社群中被重新定义为"品类信号"。`.sh`（圣赫勒拿，4,500 人口）因与 Shell script 的 `.sh` 扩展名巧合，成为 CLI/脚本工具的常用域名（如 ngrok.sh）。`.md`（摩尔多瓦）因 `.md` 扩展名与 Markdown 的巧合，成为文档工具的选择。这些 TLD 的信号极其精准——仅对特定受众有效，大众用户几乎没有认知。零售价约 $20-$40/年。风险：总注册量小，市场流动性差；ccTLD 运营依赖单一国家注册局，政策稳定性不如 gTLD。
- **EMD (Exact Match Domain) / 完全匹配域名**：域名与目标关键词完全一致的域名（如 `aicodingassistant.com`）。2012 年 9 月 Google 推出 EMD 算法更新，打击仅靠域名匹配关键词但内容低质的站点。影响范围 0.6% 的美国英语查询，Moz 数据显示 EMD 影响力在 24 小时内下降 10.3%。2026 年 Visionary Marketing 10 万页相关性研究：**EMD 的排名相关性为 -0.34**（负面相关，意味着越是用 EMD 越可能排名更差）。对 AI 产品，EMD 几乎纯粹是负面信号——`aichatbot.com` 在任何有品位的受众眼中看起来像一个 affiliate spam 站。
- **PMD (Partial Match Domain) / 部分匹配域名**：域名中包含部分关键词但不完全匹配的域名（如 `copy.ai`——关键词"AI"部分匹配）。是品牌信号和 SEO 信号之间的折衷策略。比 EMD 风险低，但仍不如纯品牌域名的长期价值。适合产品名本身含品类暗示（如 `cursor.com` 暗示"光标"即编程工具）的场景。
- **Brand Domain / 品牌域名**：域名完全由品牌名构成，不含任何通用关键词（如 `stripe.com`、`notion.so`）。Google 官方推荐方向——长期而言最具 SEO 延续性。品牌域名配合高质量内容和品牌搜索量的积累，形成不可替代的"品牌护城河"。
- **Domain History / 域名历史**：域名从首次注册至今的所有使用记录——包括历任持有人、网站内容存档、重定向链、受罚记录、黑名单状态。在注册或购买一个二手域名前，历史检查是**必须步骤**——一个曾被 Google de-index 或用于垃圾外链的域名，即使低价买到也可能永远无法恢复排名。检查工具链：Wayback Machine + site:domain.com + Google Safe Browsing + Ahrefs 流量图。
- **Domain Renewal / 域名续费**：域名的"拥有权"本质上是按年租赁。**即使是最知名的公司也犯过错**——Microsoft 丢失 passport.com（2001，$35 续费费被忽视导致 Hotmail/MSN/Expedia 瘫痪数亿用户）、Foursquare 忘记续费（2010，主页被 GoDaddy 停放页代替）、Dallas Cowboys 丢失 dallascowboys.com（2010，24-28 小时离线）。99% 的域名丢失根源是**关联邮箱已失效**——非技术问题，是人员流程问题。
- **Defensive Domain Registration / 防御性域名注册**：注册品牌名在所有核心 TLD（`.com`/`.ai`/`.io`/`.co` 等）以及常见拼写错误的域名变体，并通过 301 全部指向主域。关键原则：**只做 301 重定向，不要在多个域名上托管内容**——Google 会将此举视为重复内容或信号分裂。防御性注册的成本：假设防御 5 个变体，约 $135/年起。

---

## 专题对照：AI 产品的域名策略矩阵

| 策略 | 适用阶段 | 优点 | 缺点 | 代表案例 |
|------|:---:|------|------|----------|
| **收购 premium .com** | 融资后（A 轮+） | 品牌搜索量最大、域名泄漏最低、投资人最认可 | 成本极高（$50K-$15M+） | OpenAI 收购 [chat.com](https://chat.com)（价格未披露，推测数百万） |
| **注册 .ai 为主域** | 种子轮到 A 轮 | 品类信号最强、"我是 AI 原生"的信号价值、投资人完全接受 | 年费 $90-$220；精品库存已基本耗尽 | [perplexity.ai](https://perplexity.ai)、[cursor.ai](https://cursor.ai)、[you.ai](https://you.ai)（$70万收购） |
| **注册 .io 为主域** | 早期 | 开发者工具信号强价格适中 | 地缘政治风险（可能被删除） | （2026 年已越来越少，大量迁移到 .ai 或 .com） |
| **注册 .com 变体**（如 `getX.com`、`tryX.com`、`Xapp.com`） | 种子轮（预算有限） | 保留 .com 权威性，成本可控；数十家独角兽走过此路径 | 增加用户记忆负担和输入步骤；长期需升级 | [runwayml.com](https://runwayml.com)（$1.5B 估值仍用变体）· 详见下方 [修饰域名策略详解](#修饰域名modifier-domain策略详解) |
| **注册 .co / .app / .dev** | 验证期 | 成本低、聚焦开发者受众 | 域名泄漏严重、品牌信号弱 | [huggingface.co](https://huggingface.co)（$4.5B 估值却用 .co 是唯一的例外反例） |
| **先注册非 .com 再升级** | 全周期 | 节省早期成本、验证 PMF 后投资品牌 | 升级时旧域名 301 处理成本、品牌切换 | 大量 YC 公司：YC 批次后购买 .com |

### TLD 价格对比表（2026 年批发价，via Cloudflare Registrar）

| TLD | 批发价/年 | 零售价/年（大概） | 备注 |
|:---:|:---:|:---:|------|
| `.com` | $10.18 | $12-$20 | 基准价格 |
| `.dev` | $10.18 | $20-$36 | Google Registry；强制 HTTPS（HSTS preload） |
| `.app` | $12.18 | $24-$36 | Google Registry；强制 HTTPS（HSTS preload） |
| `.sh` | ~$10.00 | $20-$35 | 圣赫勒拿 ccTLD；Shell 脚本/CLI 工具品类暗示 |
| `.md` | ~$12.00 | $20-$40 | 摩尔多瓦 ccTLD；Markdown/文档工具品类暗示 |
| `.tech` | $49.20 | $98-$100 | 科技信号 |
| `.io` | $50.00 | $80-$100 | 地缘政治风险 |
| `.ai` | **$90.00** | **$100-$220** | 2026.3 提价 29%；两年起注册 |

### EMD vs PMD vs Brand Domain 对比

| 维度 | **EMD（完全匹配域名）** | **PMD（部分匹配域名）** | **Brand Domain（品牌域名）** |
|------|------|------|------|
| 定义 | 域名 = 目标关键词 | 域名含部分关键词 | 域名 = 品牌名本身 |
| 例子（AI 产品） | `aicodingassistant.com` | `copy.ai`、`cursor.ai` | `chatgpt.com`、`claude.ai` |
| 2026 SEO 相关性 | **-0.34**（负面相关） | 中性（取决于品牌建设） | 正面（通过品牌搜索积累） |
| Google 态度 | 2012 年起重点审查；低质内容直接打压 | 无特殊处理；内容质量决定排名 | 官方推荐的长期方向 |
| 品牌建设 | 极差——看起来是垃圾站 | 中等——有品牌暗示但偏功能 | 最佳——品牌与域名完全统一 |
| AI 产品是否推荐 | **否**——对任何有品位的 AI 产品是纯粹负面信号 | 可接受（如果品牌名本身就含品类暗示） | **是**——最可持续的路径 |

核心结论：**EMD 在 2026 年已从 SEO 捷径变为 SEO 负资产**——Google 的算法演进使品牌域名成为唯一可持续的策略。Gary Illyes（Google）官方态度："EMD 既不被奖励也不被惩罚——重要的是给用户传递了什么价值。"但 2026 年相关性研究明确表明其负面关联。

---

## 问题域（为何域名选择对 AI 产品是一个独立且高风险的决策）

- **`.com` vs `.ai` 是 AI 早期产品的第一个品牌赌注**：选择 `.com` 意味着投资"通用品牌权威"——适合准备扩展到 AI 之外的赛道。选择 `.ai` 意味着"我是 AI 原生"——品类信号极其清晰，但扩展性可能受限（见下文风险节）。2025 年 28% 的 YC/Techstars AI 初创选用 `.ai`，而 `.com` 在 YC 公司的占比从 2020 年的 64% 降至不足 50%。这不是小趋势，是结构性转移。
- **`.io` 的地缘政治定时炸弹**：1,600,000+ 个 `.io` 域名的命运取决于英国、毛里求斯和美国之间的领土谈判。如果 ICANN 最终从根区删除 `.io`，所有 `.io` 网站将无法访问——这是一个比品牌更严重的**可达性**风险。2026 年大量公司正在从 `.io` 迁移到其他 TLD。
- **精品域名的价格飞涨让早期团队无力负担**：`.ai` 单字词典域名现在起价 $80K+。`bot.ai` 和 `fin.ai` 在 2025-2026 年分别以 $120万和 $100万成交。对于种子轮公司而言，精品域名不再是"可选"，而是"不可及"。
- **域名是永久性的营销广告**：Lexicon Branding 的 David Placek 引用过一句名言："一个公司发布的最有效的广告就是它的名字。它每天在所有语言、所有市场、贯穿公司整个生命周期都在运行。"域名是品牌名的数字载具——一个难记的域名会持续消磨品牌名的价值。
- **域名泄漏是沉默的流量杀手**：如果 `yourapp.ai` 是主域名，但 `yourapp.com` 是一个空白页或竞品，每次用户或链接引用 `/yourapp.com` 都会流失流量。这对消费级 AI 产品尤为严重——大众用户**不会**主动记住非 `.com` TLD。
- **AI 域名的垃圾邮件和钓鱼风险比其他品类更严重**：Spamhaus 在 2026 年首次将 `.ai` 列入"最差 20 个 TLD"（Top 20 worst TLDs），因为冒牌 AI 工具大量使用 `.ai` 域名发送钓鱼邮件。这影响了整个 `.ai` 命名空间的声誉——合法的 AI 产品需要额外的信任建设。
- **ChatGPT 等 AI 产品域名选择的连锁效应**：ChatGPT 使用 [chatgpt.com](https://chatgpt.com) 作为主域，但 OpenAI 仍收购了 [chat.com](https://chat.com)（顶级四字母 `.com`）。Anthropic 让 Claude 使用 [claude.ai](https://claude.ai) 作为独立品牌域——将 AI 服务建立为独立的品牌目的地。Hugging Face 用 [huggingface.co](https://huggingface.co) 证明了只要品牌够强，TLD 不决定性——但这是 $4.5B 的罕见例外。
- **域名是租用而非真正的"拥有"**：所有域名本质上是按年租赁。即使是注册了 10 年的域名，到期不续约就会落入他人之手。AI 产品的域名尤其脆弱——大量域名注册在创始人的个人账户下，创业公司一旦解散或创始人失联，域名可能无声无息地过期。续费系统的核心依赖是**邮箱**——99% 的域名丢失是因为关联邮箱已失效（离职员工的别名邮箱、关闭的初创公司邮箱）。不更新的信用卡、未监测的 WHOIS 邮箱、错过的 30 天宽限期——三个沉默杀手。
- **EMD 策略在 AI 品类中不仅无效，反而有害**：在普通品类中，EMD 可能还残留微弱的"相关性暗示"价值。但在 AI 品类，EMD 与"低质 affiliate 站""AI 套壳工具""骗局"的关联度极高——域名本身就是反向信号。2026 年相关性研究 EMD = -0.34。

---

## 能力栈（概念拆分，非厂商功能表）

- **TLD 策略层**：产品品类信号（AI 原生→.ai；开发工具→.dev；通用→.com）→ 目标受众偏差（开发者还是大众？）→ 投资者预期（投资人看到 .ai 不会减分，但看到一个奇怪的 TLD 可能会减分）→ 五年后的扩展方向（会离开 AI 赛道吗？）。
- **域名注册与获取层**：检查目标域名的 WHOIS 状态 → 评估精品域名在二级市场的可能的要价区间 → 如无法购买，设计变体策略（`getX.com`、`X.ai`、`Xapp.com`）→ 注册防御性变体（品牌名的常见拼写错误和竞争 TLD）。
- **SEO 与技术设置层**：设置 www→非www 或反向的 301 重定向（全站统一 canonical）→ 配置 HTTPS（Let's Encrypt 或付费证书）→ 将域名提交到 Google Search Console 和 Bing Webmaster Tools → 设置 CDN（Cloudflare 等）以提升全球加载速度 → 如果主域名非 `.com`，重点关注品牌搜索的表现。
- **品牌保护层**：注册商标（USPTO Class 9/42——与 AI 产品直接相关）→ 使用 WHOIS 隐私保护 → 注册常见拼写变体、连字符变体和竞争 TLD → 监控竞品域名的注册行为。
- **域名历史检查层**：对购买或注册的二手域名，执行五步检查——① `site:domain.com` 查看是否被 Google de-index ② Wayback Machine 审查历史内容是否有垃圾/赌博/PBN 使用痕迹 ③ Ahrefs/Semrush 有机流量图（骤降 = 可能有过处罚）④ 历史重定向链检查（跨品类重定向 = 过期域名滥用的信号）⑤ Google Safe Browsing + VirusTotal 检查是否被标记为钓鱼/恶意软件。工具：Archive.org（免费）、SpamZilla（付费，自动计算 Spam Score + 历史快照）、ExpiredDomains.net（最大过期域名数据库，7.58亿域名，676 TLD）。
- **域名续费管理层**：设置至少 5 年的预付费（而非逐年自动续费——避免信用卡失效的问题）→ 将注册邮箱设为团队共享邮箱（而非个人邮箱——避免创始人离开后 domain 丢失）→ 在日历中设置域名过期前 90 天、60 天、30 天的三次提醒 → 了解域名的生命周期阶段（活跃期 → 宽限期 30-45 天 → 赎回期 $80-$300 额外费用 → 删除期 5-10 天 → 公开注册）。一旦进入赎回期，恢复成本可能是正常续费价格的 3-10 倍。
- **防御性注册管理层**：注册品牌名在至少 4 个核心 TLD（`.com` + `.ai` + `.io` + `.co`）→ 注册 2-3 个常见拼写错误（如丢失一个字母、交换两个字母）→ 全部通过 301 重定向到主域 → 不要将多个域名指向不同内容（信号分裂）。年维护预算：约 $135-$300。
- **国际化层**：如果产品需要多语言，选择子目录结构（`example.com/zh/`）而非 ccTLD——权重集中、维护成本最低、Google 推荐。
- **域名监控层**：监控域名过期和可用性 → 监控品牌词在域名 Squatting 中的出现 → 设置品牌搜索 Google Alert → 定期检查同名产品的域名使用情况。

---

## 形态谱系（与具体品牌解耦）

- **Type A — Premium .com 型（资金充裕的后期公司）**：直接购买 clean `.com`——如 [chat.com](https://chat.com)、[cursor.com](https://cursor.com)。品牌搜索量最大，域名泄漏最小。成本 $50K-$15M+。适合 Series A 及以上有融资实力的公司。
- **Type B — .ai 原生型（AI 早期公司的主流选择）**：将 `.ai` 作为主域——品类信号最清晰，投资人完全接受，技术受众完全理解。28-30% 的 YC AI 初创选择此策略。零售价 $100-$220/年。适合种子轮到 A 轮。风险：大众用户输入 `.com` 的习惯导致域名泄漏、精品库存已基本耗尽（单字词 $80K+）。
- **Type C — .com 变体型（预算有限但仍然要 .com 的早期公司）**：`getX.com`、`tryX.com`、`useX.com`、`Xapp.com`、`Xhq.com`——保留 .com 权威性，成本可控（通常可作为正常注册获取，无需二级市场购买）。代价是增加用户的记忆负担。典型案例如 [runwayml.com](https://runwayml.com)（Runway，$1.5B 估值仍用变体）。
- **Type D — .io 遗留型（正在迁移中的公司）**：历史原因使用 `.io` 作为主域。2026 年面临强烈的迁出压力——地缘政治风险和品牌信号的双重削弱。已越来越少新公司选择此路径。
- **Type E — 非 .com / 非 .ai 的垂直 TLD（开发者工具的精准选择）**：`.dev`（Google Registry，强制 HTTPS）或 `.app`（Google Registry）——适合纯开发者工具、无需大众辨识度的产品。信任信号对目标受众足矣，成本低廉（$10-$20/年）。进一步细分还有 `.sh`（Shell 工具 / CLI 产品，圣赫勒拿 ccTLD）和 `.md`（文档 / Markdown 工具，摩尔多瓦 ccTLD），信号精准度极高但受众面极窄。不适合有任何 B2C 野心的产品。
- **Type F — "先非.com 再升级"（分阶段品牌投资）**：早期注册 `.ai`/`.co`/`.io` 验证 PMF，获得 A 轮融资后购买 `.com`，通过 301 重定向迁移。是大量 YC 公司的实际路径。

---

---

## 修饰域名（Modifier Domain）策略详解

**定义**：当品牌精确匹配 `.com` 不可获取时，通过在品牌名前加短动词或后加类别词来注册仍保持 `.com` 的域名。这是创业公司最常用的命名空间占位策略。

**术语**：行业内统称 **修饰域名/Modifier Domain**，细分为前缀域名（`get[name]`）、后缀域名（`[name]hq`）。在讨论升级到精确匹配时称 **"Drop the Prefix" 策略**（如 Dropbox 的 `GetDropbox.com` → `Dropbox.com`）。也可称为过渡域名/搭桥域名（Bridge Domain）、占位域名（Placeholder Domain），但都不如"修饰域名"准确。

### 量化数据

一项对 2015-2020 年 **6 万家初创企业** 的域名统计（James Iles, 2021）显示：
- "关键字 + 品牌"组合域名的占比最高
- 其中 **`get` + 品牌名列第一**（`get` 和 `app` 合计覆盖了大多数融资案例）

2025-2026 年补充数据：
- `.com` 精确匹配可用率仅 **46%**；`.io` 和 `.co` 的可用率约为 `.com` 的 100 倍
- 在后市场交易数据中，`get`、`hello`、`the` 位列附加词 Top 3
- 约 **50% 的现代创业公司直接在替代 TLD 或修饰域名上启动**

### 全部可选修饰词清单

#### 前缀（前置动词/限定词）

| 前缀 | 适用场景 | 代表案例 |
|------|----------|----------|
| `get[name].com` | SaaS/产品启动（最流行，行动导向） | GetDropbox, getdbt, getbootstrap, getchorus |
| `try[name].com` | 免费试用/测试版产品 | TryInteract, TryDave |
| `use[name].com` | 工具类 SaaS | 开发者工具常用 |
| `go[name].com` | 行动导向产品 | goShippo |
| `my[name].com` | 个人化产品/仪表盘 | MyFitnessPal |
| `the[name].com` | 权威感 | TheFacebook（后升级为 Facebook） |
| `hey[name].com` | 活泼/消费品牌 | 邮箱客户端风格 |
| `join[name].com` | 社区/协作产品 | 强调归属感 |
| `meet[name].com` | 社交/会议平台 | 见面意涵 |
| `start[name].com` | 新手上路/引导 | 入门感 |
| `build[name].com` | 开发者/创作者工具 | 构建意涵 |
| `app[name].com` | 移动/网页应用 | 偏重功能说明 |
| `weare[name].com` | 团队/组织感 | 归属意涵 |
| `grow[name].com` | 增长类工具 | 成长意涵 |

#### 后缀（后置名词/类别词）

| 后缀 | 适用场景 | 代表案例 |
|------|----------|----------|
| `[name]hq.com` | 总部/官方站点（最经典的后缀方案） | BasecampHQ, SlackHQ |
| `[name]app.com` | 移动/网页应用 | CurtsyApp |
| `[name]labs.com` | 技术创新/研发 | 传达实验感 |
| `[name]studio.com` | 创意/设计工具 | 专业工作室气场 |
| `[name]hub.com` | 平台/聚合 | 平台枢纽感 |
| `[name]tools.com` | 工具集 | 功能说明清晰 |
| `[name]kit.com` | 组件/工具箱 | 模块化感 |
| `[name]tech.com` | 技术类公司 | 行业信号 |
| `[name]cloud.com` | 云服务 | 基础设施感 |
| `[name]way.com` | 方法/路径 | 解决方案感 |
| `[name]works.com` | 服务/工具 | 服务工作意涵 |
| `[name]space.com` | 社区/空间 | 平台感 |
| `[name]now.com` | 即时/快速启动 | 紧迫感 |
| `[name]team.com` | 团队协作 | 协作意涵 |
| `[name]guide.com` | 教育/教程类 | 知识意涵 |
| `[name]dev.com` | 开发者工具 | 开发者专属 |

### 完整案例清单

#### 已成功升级到精确匹配的案例（"Drop the Prefix"）

| 公司 | 起步域名 | 升级到 | 代价/时间 | 备注 |
|------|---------|--------|----------|------|
| **Dropbox** | `GetDropbox.com` | `Dropbox.com` | ~$30万（2009年） | 详见下方 [Dropbox 悖论](#dropbox-悖论) |
| **Facebook** | `TheFacebook.com` | `Facebook.com` | ~$20万（2005年） | Sean Parker："Drop the 'The'" |
| **Tesla** | `TeslaMotors.com` | `Tesla.com` | ~$1100万 + 10年谈判 | 马斯克亲自多年求购 |
| **Stripe** | `GetStripe.com` | `Stripe.com` | 未公开 | 从"获取 Stripe"到"互联网支付基建" |
| **Basecamp** | `BasecampHQ.com` | `Basecamp.com` | 未公开 | 多年后才买到 |
| **Slack** | `SlackHQ.com` | `Slack.com` | 未公开 | "HQ" 是经典创业逃生舱 |
| **Postman** | `GetPostman.com` | `Postman.com` | 未公开 | 从开发者下载工具到完整 API 平台 |
| **Banyan** | `GetBanyan.com` | `Banyan.com` | 融 $1000万后（2021年） | 收据数据分析平台 |
| **Massdrop** | `Massdrop.com` | `Drop.com` | 域名要价 ~$80万（2017年） | 提前两年锁仓，2019年公开更名 |
| **Box** | `Box.net` | `Box.com` | 未公开 | 企业化转型标志 |
| **Zoom** | `Zoom.us` | `Zoom.com` | 未公开 | 品牌认知达到大众后才拿下 |
| **Dave** | `TryDave.com` | `Dave.com` | 未公开 | 金融科技应用 |
| **Tile** | `TheTileApp.com` | `Tile.com` | 未公开 | 蓝牙追踪器 |
| **Cruise** | `GetCruise.com` | 后被 GM $53亿收购 | — | 自动驾驶 |

#### 至今仍使用修饰域名的知名案例

| 公司 | 域名 | 行业 | 估值/规模 |
|------|------|------|----------|
| **dbt Labs** | `getdbt.com` | 数据工程 | 行业标杆，社区日均活跃数十万 |
| **Bootstrap** | `getbootstrap.com` | 前端框架 | 全球最流行 CSS 框架 |
| **Shippo** | `goshippo.com` | 物流 API | 融资数亿美元 |
| **Fabric** | `getfabric.com` | 供应链 | 融资超 $2亿 |
| **Bread** | `getbread.com` | 金融/支付 | 融资超 $2亿 |
| **Chorus** | `getchorus.com` | 销售 AI | 被 ZoomInfo 收购 |
| **Curtsy** | `curtsyapp.com` | 社交电商 | YC 孵化的 Gen Z 二手服饰平台 |
| **Roman** | `getroman.com` | 男性健康 | 后来买下 `roman.co` 做跳转 |
| **Runway** | `runwayml.com` | AI 视频生成 | $1.5B 估值，仍用 `ml` 后缀变体 |

### Dropbox 悖论

这是修饰域名领域最经典的警示案例，揭示了该类域名的核心矛盾——**修饰域名对启动足够好，对规模化同样够坏**。

**GetDropbox.com 时代**：
- 承载了病毒式宣传视频（一晚候补名单从 5000 → 75000）
- 支撑了 YC 批次、A 轮融资、300 万用户
- 但每天有大量用户直接输入 `dropbox.com`——落地在陌生人的停车页
- 竞争对手可在该停车页投放广告，精准收割你的用户

**升级过程**：
- 持有人最初拒绝一切报价
- 创始人 Drew Houston 和联合创始人亲自开车到对方面前
- 带着一瓶香槟和一纸商标诉讼状
- 最终 $30万 现金成交。对方拒绝了等额股票——若持有至今，价值数亿美元

**核心洞察**：早期域名"解释或指导"（GetDropbox = 去拿 Dropbox），伟大域名"拥有"（Dropbox 本身就是品类）。修饰词如 Get、The、Motors 是合理的入门通道，但一旦品牌够强大，域名就应该是品类本身。

### 优劣分析

**优势**：
- **零启动成本**：常规注册 $10-15/年 vs 精确匹配可能 $5K-$1000万+
- **成熟路径**：大量刚拿到融资的创业公司使用，"不被认为是弱品牌信号"
- **SEO 友好**：Google 将修饰域名的品牌部分视为主体，无排名惩罚
- **行动导向**：`GetX.com` 本身就是 Call to Action
- **可升级**：Dropbox 的路径是教科书——待融资后再买纯 `.com`

**劣势（三大系统性风险）**：
1. **用户认知摩擦**：口头传播说"Dropbox"，用户输入 `dropbox.com`——落点错误。每个修饰词都是传播效率的减速带
2. **品牌定位受损**：`GetBolt.com` 永远暗示"真正的 `Bolt.com` 在别人手上"；让人潜意识怀疑你们是不是第三方/附属品
3. **悖论陷阱**：你越成功，精确匹配域名的持有人越清楚你的价值。你越离不开，对方开价越高。Dropbox 是幸运的——有些公司在接触域名持有人后，价格翻了十倍才成交

### 业界观点

| 立场 | 代表声音 |
|------|----------|
| **务实派** | "修饰域名不是失败——在精确匹配不可及时，这是合理的入门通道。" |
| **品牌激进派**（Domavest） | "对独角兽来说是灾难——永远暗示你不是品类的主人。" |
| **投资观察者**（域名市场） | "`get` 前缀是早期信号：公司如果跑通，精确匹配版本必然成为战略刚需。" |
| **主流共识** | "修饰域名是创业期的胶带——好用、常见、但不该永远贴在前门上。" |

### 决策框架（快速参考）

```
精确匹配 .com 被占用？
├── 预算充足 → 通过 Afternic/Sedo 匿名询价（标价通常远高于实际成交价）
│   └── 租约/分期也值得考虑——Domavest 等平台提供域名融资
│
├── 预算有限（种子轮/验证期）
│   ├── B2B / 技术产品 → .io 或 .ai 完全可接受
│   ├── D2C / 大众消费 → 必须保住 .com → 选用修饰域名
│   │   ├── 首选 `get[name].com`（最成熟、案例最多、VC 最熟悉）
│   │   ├── 次选 `[name]hq.com` 或 `[name]app.com`
│   │   └── 坚决避免：连字符、数字、拼写错误——这些永远不如一个干净的替代名
│   │
│   ├── 务必同时注册 .com + 1-2 个替代 TLD（.io/.ai/.co）做防御
│   └── 同时检查社交账号（Twitter/X、GitHub、Instagram）的可用性
│
└── 不管选哪条路 → 把"买回纯品牌 .com"写在你的 A 轮 checklist 里
    └── 核心规律：越早买越便宜，越成功越贵
```

### 升级时机信号

何时从修饰域名升级到精确匹配？三个明确信号：
1. **流量泄漏已可量化**：Google Analytics 中直接输入 `example.com` 而非 `getexample.com` 的流量占比不断上升（特别是品牌搜索量增长时，域名泄漏同步增长）
2. **投资人/客户持续困惑**：邮件发错地址、名片上需要额外解释、媒体报道时使用了错误的 URL
3. **竞争对手可收割**：精确匹配 `.com` 的持有人可能在你的品牌变强后主动变现——在它变成恶意竞争者之前拿下

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **TLD 的地缘政治风险**：`.io` 面临 ICANN 删除的风险（英属印度洋领地领土争议）。`.ai` 的运营依赖安圭拉政府和 Identity Digital 的基础设施——虽目前稳定，但单一加勒比岛国控制硅谷最重要命名空间的权力集中本身是一个系统性风险。替代 TLD 应作为备案列入。
- **域名泄漏的财务代价**：如果你的 `.ai` 域名对应的 `.com` 被第三方持有，每次用户输入 `.com` 都会流失。如果 `.com` 持有人是竞品或恶意方（如展示仿冒页面或负面评论），损失不仅是流量，还包括品牌信誉。解决方案：在发布前至少获取对应的 `.com` 域名——即使只做 301 重定向。
- **精品域名投资泡沫**：`.ai` 的二级市场价格在 2023-2026 年间暴涨 13 倍。65% 的已注册 `.ai` 网站无真实内容（占位页或 parked pages）。61% 是投机持有的。如果 AI 热度下降，精品 `.ai` 域名的估值可能缩水——购买决策需要考虑这层风险。
- **域名续费的长期成本**：`.ai` 的年费是 `.com` 的 9 倍。防御性注册（品牌名在多 TLD 下的变体）每年的维护成本在 $500-$2,000+。对早期团队这不是小数。
- **商标与域名的冲突**：拥有域名 ≠ 拥有商标权；同理，商标不自动赋予域名所有权。在 USPTO 注册商标（Class 9/42）是保护 AI 品牌域名的关键步骤——UDRP（统一域名争议解决政策）投诉依赖商标作为权益证明。
- **Cybersquatting / 域名抢注风险**：AI 领域的域名抢注比其他品类更活跃。如果你的 AI 产品名称在发布会之前泄露，抢注者可以在几小时内注册所有变体。解决方案：在公开名称之前先注册核心域名和商标。
- **域名续费失败——沉默的品牌灾难**：以下是实际发生的案例：

| 公司/组织 | 域名 | 年份 | 后果 |
|-----------|------|:---:|------|
| **Microsoft** | [passport.com](https://passport.com) | 2001 | 凌晨过期自动停机，Hotmail/MSN/Expedia 全部瘫痪。$35 续费被忽视。影响数亿用户 |
| **Foursquare** | [foursquare.com](https://foursquare.com) | 2010 | $10M 融资后主页被 GoDaddy 停放页代替。被投资人发现后紧急续费 |
| **Dallas Cowboys** | [dallascowboys.com](https://dallascowboys.com) | 2010 | 24-28 小时无法访问。1995 年注册的老域名因忘记续费被替换为儿童踢足球图片 |
| **Yatra**（印度最大在线旅游网站） | yatra.com | 2012 | 丢失大量客户和与印度国家银行 $5.7B 产业的合作。至今未恢复之前地位 |
| **Regions Bank**（美国第 22 大银行） | regions.com | 2013 | 1700+ 分行、2400+ ATM 的在线银行服务瘫痪近一周。被迫公开道歉 |
| **Marketo** | marketo.com | 2017 | $10 亿估值的营销巨头——在自动续费已是行业标准的时代仍忘记续费 |

这些案例的共同根因：**99% 的域名丢失是因为关联邮箱已失效**——发给离职员工或已关闭初创公司邮箱的续费提醒无人阅读。不是技术故障，是组织流程漏洞。预防：将域名注册邮箱设为团队共享邮箱，而非任何个人的工作邮箱。

---

## 落地碎片（无先后）

- 如果你是 AI 早期公司、种子轮阶段：优先 `.ai`。TLD 信号与你的品类完美对齐，投资人不会减分，技术受众完全理解。在发布前同时购买对应的 `.com`（即使只做 301 重定向）——防域名泄漏。
- 如果你已经 A 轮+：严肃评估是否需要升级到 `.com`。如果是——最干净的路径是在 Series A 资金中为此分配 $50K-$500K 预算。
- 如果你还在验证期、不确定产品方向：用 `.com` 变体（`getX.com` 或 `tryX.com`）起步——不锁死在 AI 品类上。
- 如果你是一个面向开发者的纯工具（CLI/API/SDK）：`.dev` 或 `.app` 是精准且便宜的选项（$10-$20/年）。不需要为了"好看"多花 $90/年。
- 如果你做的是 Shell 脚本/CLI 工具，`.sh` 是自带品类暗示的小众选择（适合独立开发者，不适合有 B2B 销售场景的产品）。同理，文档/Markdown 编辑器可考虑 `.md`。但需清楚：这两个 TLD 仅对极窄的开发者受众有效。
- 如果你当前在 `.io` 上：**立即开始计划迁移**。即使是三年计划也应该从现在开始——注册目标 `.ai` 或 `.com`，设置 301 测试，在公司还能控制节奏时完成迁移。
- 不要忽视 WHOIS 隐私——尤其是一个人的创业团队。注册域名时打开隐私保护，否则你的家庭住址会对全网公开。
- 注册后立即提交 Google Search Console 和 Bing Webmaster Tools——越早建立索引历史，后续 SEO 工作的起点越高。
- 如果你的候选域名是 EMD：直接排除。`aichatbot.com` 或 `aigenerator.online` 在任何可信受众眼中是垃圾信号。如果域名中恰好包含品类词（如 `cursor` 天然暗示编程工具），这是 PMD 而非 EMD——可接受。
- 在注册或购买二手域名前，至少做三步检查：① `site:domain.com` → 如果零索引表示可能被 de-index ② Wayback Machine → 看看过去是什么网站（从律师事务所突然变减肥药站 = PBN 垃圾）③ 检查是否有历史重定向曾经跨品类跳转。
- 将域名的 WHOIS 管理员邮箱设置为团队共享邮箱（如 domains@yourcompany.com），而非个人 Gmail——这是预防域名丢失成本最低的措施。

---

## AI 行业知名域名案例

| 产品/公司 | 主域名 | TLD 策略 | 备注 |
|-----------|--------|:---:|------|
| **ChatGPT** | [chatgpt.com](https://chatgpt.com) | `.com` premium | 同时拥有 [chat.com](https://chat.com)（收购，价格未披露，推测数百万美元） |
| **Claude** | [claude.ai](https://claude.ai) | `.ai` 原生 | Anthropic 将 Claude 建立为独立于公司主域的品牌目的地 |
| **Perplexity** | [perplexity.ai](https://perplexity.ai) | `.ai` 原生 | AI 搜索品类，`.ai` 是最精确的信号 |
| **Cursor** | [cursor.com](https://cursor.com) | `.com` premium | 同时拥有 [cursor.ai](https://cursor.ai) 作为品牌防御 |
| **Hugging Face** | [huggingface.co](https://huggingface.co) | `.co` | $4.5B 估值的罕见例外——品牌力弥补了 TLD 的差距 |
| **DeepSeek** | [deepseek.com](https://deepseek.com) | `.com` | 全球化策略，`.com` 权威性在中文和非英文市场尤为重要 |
| **Midjourney** | [midjourney.com](https://midjourney.com) | `.com` | —
| **Replit** | [replit.com](https://replit.com) | `.com` | —
| **Runway** | [runwayml.com](https://runwayml.com) | `.com` 变体 | $1.5B 估值仍用 `ml` 后缀变体 |
| **Notion** | [notion.so](https://notion.so) | `.so`（索马里 ccTLD） | $10B 估值的极致例外——品牌力的终极证明 |

---

## 外链索引

### 官方文档与注册局

| 名称 | 一句话 | URL |
|------|--------|-----|
| **ICANN 根区数据库** | 查询所有 TLD 的注册局和运营状态 | [iana.org/domains/root/db](https://www.iana.org/domains/root/db) |
| **Google Search Central · 域名与 SEO** | Google 关于域名选择和多区域/多语言站点的官方指南 | [developers.google.com/search](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) |
| **Identity Digital** | 2025 年起管理 .ai 注册局基础设施 | [identity.digital](https://identity.digital) |
| **Cloudflare Registrar** | 唯一按 wholesale 成本价出售域名的注册商——TLD 价格对比的基准 | [cloudflare.com/products/registrar](https://www.cloudflare.com/products/registrar/) |

### 域名市场数据与分析

| 名称 | 一句话 | URL |
|------|--------|-----|
| **DomainsProject · .ai 专题报告** | 最全面的 .ai 域名市场分析——注册增长率、真实使用率、垃圾邮件指标、投资回报分析 | [domainsproject.org/blog/ai-domains-and-the-ai-gold-rush](https://domainsproject.org/blog/ai-domains-and-the-ai-gold-rush) |
| **NameBio** | 域名二级市场交易数据库——查询具体域名的历史成交价 | [namebio.com](https://namebio.com) |
| **Hostinger · 2026 最流行 TLD 统计** | 全球 TLD 市场份额与增长数据——.ai 突破 100 万注册，每周 +1% | [hostinger.com/blog/most-popular-domain-extensions](https://www.hostinger.com/blog/most-popular-domain-extensions) |
| **NamePros · .ai vs .io 报告** | 深度对比两大 ccTLD 的投资价值、地缘政治风险与二级市场 | [namepros.com](https://www.namepros.com/threads/the-ai-vs-io-report.1384486/) |
| **Google 2012 EMD 更新 · Moz 早期数据** | EMD 影响力 24 小时内下降 10.3% 的早期分析 | [moz.com/blog/googles-emd-algo-update-early-data](https://moz.com/blog/googles-emd-algo-update-early-data) |
| **Visionary Marketing · 2026 SEO 排名因子研究** | 10 万页相关性分析；EMD = -0.34；品牌信号的系统性优势 | [visionary-marketing.co.uk/blog/seo-ranking-factor-study-2026](https://visionary-marketing.co.uk/blog/seo-ranking-factor-study-2026) |

### 域名历史检查工具

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Archive.org / Wayback Machine** | 免费；查看域名的完整历史网页存档——检查是否曾被用于垃圾/PBN/赌博内容 | [web.archive.org](https://web.archive.org) |
| **ExpiredDomains.net** | 最大过期域名数据库（7.58 亿域名，676 TLD）；按 SEO 指标筛选；免费 | [expireddomains.net](https://www.expireddomains.net/) |
| **SpamZilla** | 付费；自动计算 Spam Score（1-100）+ 自带 Wayback Machine 历史快照预览 | [spamzilla.io](https://spamzilla.io) |
| **Google Transparency Report** | 免费；检查域名是否被 Google 标记为危险/钓鱼 | [transparencyreport.google.com](https://transparencyreport.google.com) |
| **WhoAPI · 13 个著名域名过期案例** | 域名过期/丢失的完整历史记录 | [whoapi.com/blog/5-all-time-domain-expirations-in-internets-history](https://whoapi.com/blog/5-all-time-domain-expirations-in-internets-history/) |

### AI 域名策略指南

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Nominus · AI 域名被占怎么办（2026 指南）** | 二级市场价格分级、替代 TLD 评估、谈判策略 | [nominus.com/blog/ai-domain-taken-what-to-do-guide-2026](https://www.nominus.com/blog/ai-domain-taken-what-to-do-guide-2026) |
| **dotappraisals · 2026 AI 初创最佳 TLD 排名** | `.com` vs `.ai` vs 其他 TLD 的定量排名与投资者视角分析 | [dotappraisals.io/blog/best-tlds-for-ai-startups-2026](https://dotappraisals.io/blog/best-tlds-for-ai-startups-2026) |
| **Saipx · 2026 哪个 TLD 值得深耕** | 实战域名经纪人的 TLD 选择框架——以五年为周期的价值评估 | [saipx.com/blog/which-tld-is-worth-building-on](https://saipx.com/blog/which-tld-is-worth-building-on) |
| **Tois · OpenAI 为何收购 chat.com** | 从品牌战略分析 OpenAI 对 chat.com 的收购逻辑 | [tois.com/blog/why-openai-acquired-chat-com](https://tois.com/blog/why-openai-acquired-chat-com) |
| **TLDFYI · 2026 初创 TLD 选型指南** | TLD 信任信号、域名估值（品牌.io 仅值品牌.com 的 5-10%）、分阶段升级路径 | [tldfyi.com/guides/choosing-tld/best-tlds-for-startups](https://tldfyi.com/guides/choosing-tld/best-tlds-for-startups) |
| **Substack · AI 服务的互联网基础设施视角** | 纯学术视角分析 ChatGPT/Claude/DeepSeek/Gemini/Copilot 的域名与网络架构 | [charlesmok.substack.com](https://charlesmok.substack.com/p/an-internet-infrastructure-perspective) |

### 对比与测评（第三方；观点非官方）

**`.com` vs `.ai` 的终极选型框架**：dotappraisals 和 Saipx 一致认为——如果能买到任何版本的 `.com`（哪怕是两词复合词），优先选 `.com`。如果 `.com` 不可及，`.ai` 对 AI 产品完全 OK——投资人不会减分。如果两者都不可及，改名——"一个次优名字在好 TLD 上，胜过你最喜欢的名字在怪 TLD 上。AI 品类一半是同样的五个词在混搭——改名的成本比创始人想的低得多。"

**`.io` 应尽快迁移**：市场上存在广泛共识（NamePros、DomainsProject、TLDFYI）——`.io` 的地缘政治风险是结构性的。2026 年的建议不是"是否迁移"，而是"在哪一年之前完成迁移"。

**精品 `.ai` 域名的投资价值存在分歧**：DomainsProject 指出 61% 的 `.ai` 网站无真实内容。虽然顶级单字域名（如 bot.ai $120万）确有投资价值，但中长尾的 `.ai` 域名估值可能存在泡沫。对于创业公司，域名是成本中心而非投资品——不要用投资者的逻辑评估自己产品的域名支出。

---

## 延伸阅读与参考材料

- **ICANN · New gTLD Program**：了解未来可能出现的与 AI 相关的新通用顶级域。2026 年尚未有专门为 AI 设计的 gTLD 获批，但 `.ai` 的成功证明了品类 TLD 的市场需求。[newgtlds.icann.org](https://newgtlds.icann.org/)
- **Google Search Central · International and multilingual sites**：多语言 AI 产品的域名架构官方指南。[developers.google.com/search/docs/specialty/international](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- **Anguilla Government · .ai Registry Reports**：安圭拉政府关于 .ai 域名收入的公开报告——$9300万/年几乎占全国预算一半。[gov.ai](https://gov.ai)
- **USPTO · Trademark Basics**：AI 产品商标注册（Class 9 / Class 42）与域名保护的关系。[uspto.gov/trademarks/basics](https://www.uspto.gov/trademarks/basics)
