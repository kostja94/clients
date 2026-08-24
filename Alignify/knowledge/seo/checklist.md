# SEO Checklist（技术 + On-page + 发布前）· 知识块（非线性笔记）

**材料范围**：公开网络检索（2025–2026 常见「Technical SEO checklist」类文章对爬取、收录、CWV、HTTPS、移动与国际化的归纳）；本地 **Agent Skills** 中 **seo-audit** 的分阶段框架与核对行；本地客户笔记中与**站点级 SEO**直接相关的《SEO 页面代码规范》《多语言网站 SEO 实践指南》及**脱敏**后的「交付执行清单」技术项（仅保留与任意商业站点可复用的条目，**不**迁入客户专有信息）。**未**将 Alignify 站内页面 JSON 当作事实来源复述。网摘整理日期 **2026-04-19**。

**规范对照**：[section-seo.md](../../section/section-seo.md) · [technical/README.md](../../technical/README.md) · 本分册说明：[seo/README.md](./README.md)

以下条目可任意顺序阅读；**不是**文章体例。文末 **「一页核对表」** 可直接当工单用。

---

**词汇锚点**

- **SEO Checklist**：把可重复验证的项写成**可勾选**列表，用于上线前、改版后或周期性审计；与「策略叙事」互补，**不替代**根因分析（为何某类 URL 不被收录仍需单独排查）。
- **Technical SEO**：爬取、渲染、状态码、索引指令、canonical、sitemap、robots、HTTPS、重定向链、CWV 等**基础设施**层。
- **On-page SEO**：title、meta description、H1–H6、内链、图片 alt、结构化数据等**单页**层。
- **GSC / Google Search Console**：收录与体验类报告的常用入口；与**服务器日志**、**爬虫模拟**结论需交叉验证。
- **Indexable**：允许收录且内容独特、有检索价值；与「可访问但 noindex」区分。
- **Self-referencing canonical**：页面指向自身的 canonical，减少参数化 URL 重复信号（实现细节见 technical 文档）。
- **CWV / Core Web Vitals**：LCP、INP、CLS 等体验指标；业界常引用 **LCP ≤ 2.5s、INP ≤ 200ms、CLS < 0.1** 作为经验阈值（以官方文档与实测为准）。
- **Hreflang + x-default**：多语言/多区域时标注语言与地区关系及默认回退；须与 **URL 稳定**、**canonical** 一致。
- **Crawl budget（爬取预算）**：大型站、弱服务器或大量低价值 URL 时更敏感；清单上常体现为「减少链长、控制 faceted URL、修 5xx」。

---

**专题对照 / 扩展定义**

| 维度 | **清单驱动审计** | **仅看 GSC 报表** |
|------|-------------------|-------------------|
| **强项** | 不漏项、可分配 owner | 真实索引与查询数据 |
| **弱项** | 易变成「打勾表演」 | 不主动则漏技术债 |
| **建议** | 清单 + GSC + 爬虫抽样 **三角** | 同上 |

| 维度 | **代码层（HTML/CSS/JS）** | **索引层（HTTP/robots/meta）** |
|------|----------------------------|----------------------------------|
| **典型项** | `lang`、语义 landmark、H1 唯一 | `noindex`、canonical、sitemap 只含可收录 URL |
| **工具** | W3C Validator、Lighthouse | 爬虫、GSC URL Inspection |

---

**问题域（为何会出现这类产品）**

- **分工细**：开发、内容、市场、代理各管一段，若无清单易出现「meta 已写但 robots 挡了」「sitemap 含 noindex URL」等**接口型**事故。
- **算法与文档双变**：官方指南与 Rich Results 规则会更新；清单需**标日期与来源**，避免把旧闻当硬规则。
- **多语言与路由**：IP / `Accept-Language` **强制跳转**、同 URL 靠 Cookie 换语言等实现会伤害**可抓取的多语版本**与 hreflang 一致性。
- **JS 站点**：首屏与关键正文是否在**首包 HTML** 或可被 Google 渲染路径稳定访问，常与传统「静态 SEO」假设冲突。

---

**能力栈（概念拆分，非厂商功能表）**

- **可爬性**：robots 不误伤、状态码干净、链不过深、重要页非孤儿页。
- **可索引性**：canonical 一致、重复与薄页有策略（合并、差异化或 noindex）。
- **可度量性**：GSC、CWV、（可选）爬虫调度与 diff。
- **单页相关性**：标题与 H1 与意图对齐；结构化数据**有效**且与可见内容一致。
- **多语与品牌一致性**：hreflang、x-default、OG/Twitter 多语言字段与主站 canonical 策略对齐。
- **发布流水线**：预发环境可跑 Lighthouse；上线后 IndexNow / sitemap 更新（若项目已接入，见 technical）。

---

**形态谱系（与具体品牌解耦）**

- **电子表格型**：按 P0/P1/P2 分owner，适合季度大扫除。
- **爬虫任务型**：Screaming Frog、Sitebulb、云审计（Ahrefs / Semrush 等）出**差异列表**，适合大规模站。
- **GSC 驱动型**：以索引覆盖、体验报告、手动操作为轴，适合中小站快速迭代。
- **代码评审型**：以 PR 模板嵌入「HTML 语义 + meta + 性能」子清单，适合前端主导的团队（与客户侧《SEO 页面代码规范》思路一致）。

---

**风险 · 合规 · 工程治理（外部框架可对照，非法律意见）**

- **过度依赖「审计分数」**：第三方总分与 Google 实际收录/排名**非线性**相关；优先修 **P0 索引阻断**。
- **多司法辖区营销**：对比类页面避免**不可验证的贬损**表述（客户笔记中对比页 SEO 要求可复用到任意 B2B SaaS）。
- **隐私与认证页**：登录/注册页常见 `noindex`；**勿**仅用 robots.txt `Disallow` 替代 `noindex` 意图（与「需从索引移除」场景易混淆，详见 indexing 类文档与官方说明）。
- **AI 爬虫**：是否允许训练/摘要爬虫属于**品牌与法务策略**，与经典 SEO 清单**并列维护**，勿与 `User-agent: Googlebot` 混为一谈。

---

**落地碎片（无先后）**

- **robots.txt**：语法有效；不误挡 CSS/JS（影响渲染理解时）；AI 爬虫规则单独评审。
- **XML sitemap**：仅含**应被收录**的 URL；大站拆分 sitemap；在 GSC 提交（若使用 GSC）。
- **HTTPS**：全站 TLS；混合内容修复。
- **HTTP 状态**：关键着陆页无长链 302/301；软 404 与真实 404 区分处理。
- **Canonical**：全站唯一、与 hreflang 不冲突；参数化 URL 有统一偏好 URL。
- **noindex**：关键着陆页无意外 `noindex`；测试环境勿对生产泄露。
- **移动**：响应式或等价移动 URL 策略；内容对等；避免干扰性插屏（以 Google 文档为准）。
- **CWV**：按官方阈值监控 LCP / INP / CLS；大图、三方 embed、字体为常见杠杆。
- **Title / Meta**：唯一、与内容一致；长度控制在常见展示区间（title ~50–60 字符、description ~150–160 为经验值，非排名「公式」）。
- **H1–H6**：每页单一 H1；层级不断档。
- **图片**：有意义 `alt`；装饰图不堆砌关键词。
- **Schema**：JSON-LD 校验通过；类型与页面类型匹配；FAQ 等勿写可见文本外的「隐藏」答案。
- **内链**：重要页有入口；锚文本可读、勿全站同一锚点灌向一页。
- **国际化**：语言由**稳定 URL**表达；避免仅靠 IP / `Accept-Language` **强制跳转**；`hreflang` 互链 + `x-default`。
- **HTML 文档骨架**：`<!DOCTYPE html>`、`html lang`、viewport、charset；`main`/`nav` 等语义 landmark 有助于解析与无障碍（客户《SEO 页面代码规范》与 web.dev 方向一致）。
- **节奏**：全站深度审计常见建议为**季度**；GSC 与 CWV **月度**看板对中大站更稳（业文常见表述，按团队资源裁剪）。

---

**工具与产品类型（检索里常混在一起的品类；非穷尽）**

- **云 SEO 套件**：全站爬取 + 排名 + 外链 + 清单模板（Ahrefs、Semrush、Moz 等）。
- **桌面爬虫**：高可控、可导出详表（Screaming Frog、Sitebulb 等）。
- **免费入口**：Google Rich Results Test、PageSpeed Insights、Lighthouse、W3C Markup Validator。
- **CMS 插件**：Yoast、Rank Math 等——产出仍要过**索引与渲染**实测，勿盲信「绿灯」。

---

**外链索引（检索整理；非广告、无排序优先级）**

### 官方与权威参考

- [Google Search Central — 搜索基础](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)（入门与原则）
- [Page Experience / Core Web Vitals](https://web.dev/articles/vitals)（指标与优化方向）
- [Managing multi-regional sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)（多区域、hreflang 相关官方入口）

### 对比与测评（第三方；观点非官方）

英文 SEO 社区与科技媒体对「**清单长度**」分歧明显：一类主张 **50+ 点**覆盖企业站边缘情况（如重定向链、JavaScript 渲染、国际化组合）；另一类主张 **10–15 个高杠杆项**以免团队疲劳。云爬虫工具评测中常见结论是：**桌面爬虫**在「自定义提取、内存内二次过滤」上更灵活，**订阅型云审计**在「历史对比、团队分配、定时任务」上更省力；**GSC** 仍是索引真相的重要来源，但**不能**替代站外链接与竞争内容审计。把「审计分数」当 KPI 的做法常被独立作者批评为**游戏化**——更稳妥的是绑定**索引 URL 数、关键查询展示、CWV 通过比例**等业务可感知指标。网摘综合、非本站实测。

### 站内索引（Alignify 仓库）

- [section-seo.md](../../section/section-seo.md)
- [technical/README.md](../../technical/README.md)
- [technical-sitemap.md](../../technical/technical-sitemap.md)、[technical-robots.md](../../technical/technical-robots.md)（若项目已文档化）
- [knowledgehub/seo/README.md](./README.md)

---

**延伸阅读与参考材料**

- W3C [Markup Validator](https://validator.w3.org/)（HTML 有效性；与富结果解析、移动可用性的关系见社区与 Google 讨论，**非**单一「排名因子」叙事）
- Smartling 等行业博客对 **language selector UX** 的讨论（与多语 SEO 配套，**非** Google 官方）

---

### 一页核对表（可粘贴为工单）

**P0 — 索引阻断**

| ☐ | 项 |
|---|-----|
| ☐ | 关键模板无意外 `noindex` / 错误 canonical |
| ☐ | robots.txt 不误挡整类重要资源或整站 |
| ☐ | 核心着陆页非 5xx、非无限 redirect 环 |
| ☐ | sitemap 仅含应收录 URL，且与 robots/GSC 策略一致 |

**P1 — 体验与渲染**

| ☐ | 项 |
|---|-----|
| ☐ | HTTPS 全站；无严重混合内容 |
| ☐ | CWV：LCP / INP / CLS 在官方阈值内或可解释例外 |
| ☐ | 移动可用：viewport、可点区域、无遮挡式插屏（按官方定义） |
| ☐ | 关键正文在 HTML 或可被 Google 稳定渲染（JS 站必查） |

**P2 — On-page 与结构化**

| ☐ | 项 |
|---|-----|
| ☐ | 每页唯一 title、合理 meta description |
| ☐ | 单一 H1，标题层级不断档 |
| ☐ | 有意义图片 `alt`；大图懒加载与 LCP 权衡 |
| ☐ | 结构化数据校验通过且与可见内容一致 |
| ☐ | 重要页有内链入口；锚文本自然 |

**P3 — 多语与社交预览（若适用）**

| ☐ | 项 |
|---|-----|
| ☐ | 语言/区域用独立 URL；无 IP / Accept-Language **强制**跳转主方案 |
| ☐ | hreflang 互链 + `x-default`；与 canonical 一致 |
| ☐ | `og:image` 绝对 URL；多语言 `og:locale`（若站点多语） |
