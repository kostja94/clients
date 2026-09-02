# Blog Website Builder / 博客建站 · 知识块（非线性笔记）

**材料范围**：公开网络检索（WordPress.org、Wix/Squarespace、Ghost/Substack/beehiiv、Blogger；MDN、W3Techs；Tier 1「best website builder for blogs」对比稿；HN 摘要）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-08-28** · 簇迁自 `blog-cms` / `blogging-platform`。

**站内对照**：KB → 正式文优先 **`/blog/blog-website-builder`** · **`/zh/blog/blog-website-builder`** · Brief [`../../insights/_briefs/blog-website-builder.md`](../../insights/_briefs/blog-website-builder.md)

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../keywords/alignify-keywords-tools.md)（锚点 `#blog-website-builder-tools`）· `keywordEn`: **Blog Website Builder / Website Builder for Blogs** · `keywordZh`: **博客建站 / 博客网站搭建** · 次轴 **Blogging Platform / Blog CMS**（同 SERP，非独立 slug）· 快判 → [KEYWORD-RESEARCH.md](./KEYWORD-RESEARCH.md)

**主题簇**：[README.md](./README.md)（**website-builder 簇** · 搜索量头词驱动）

**站内相邻**（建站姊妹）：[website-builder.md](website-builder.md)（Hub）· [headless-cms.md](../cms/headless-cms.md) · [geo.md](../search-geo/geo.md)

**站内相邻**（跨频道 · 已发布）：[如何不用 CMS，用 AI 搭建博客](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai) · [主域名下的分块建站](https://alignify.co/blog/subdirectory-hosting) · [Git 托管](https://alignify.co/blog/git-hosting) · [创建博客（SEO）](https://alignify.co/seo/create-blog) · [子域名 vs 子目录](https://alignify.co/seo/subdomain-vs-subfolder)

## 与相邻 slug 分流

> Builder 簇 FAQ → [website-builder §簇级 FAQ](website-builder.md#簇级-faq)

| 维度 | **`blog-website-builder`（本文）** | **`website-builder`** | **`headless-cms`** |
|------|-----------------------------------|----------------------|-------------------|
| **检索头词** | blog website builder · best website builder for blogs | website builder · AI website builder | headless CMS · API-first CMS |
| 典型买家问题 | 怎么搭一个能发博客的网站？选哪个平台？ | 怎么最快有一个专业官网（博客非首要）？ | 内容 API 放哪、Next 怎么接？ |
| SERP 形态 | **Listicle**：Wix + WP + Squarespace + Ghost 同页 | Listicle：Wix/Squarespace/GoDaddy 整站 | 开发者选型 / MACH |

| 你的问题 | 看哪个 slug |
|----------|-------------|
| 「Wix / Squarespace / WordPress 写博客选哪个？」 | **本页** §工具与产品类型 |
| 「Ghost / Substack / Blogger 呢？」 | **本页**（同一 SERP 长尾） |
| 「只要公司官网，偶尔一篇博客」 | [`website-builder`](website-builder.md) |
| 「Contentful + Next 产品博客」 | [`headless-cms`](../cms/headless-cms.md) |
| 「不用 CMS，AI 搭整个博客系统」 | [`how-to-build-a-blog-without-a-cms-using-ai`](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai) |
| 「Mintlify / 文档站当博客？」 | [`documentation`](../enterprise-knowledge/documentation.md) |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Blog Website Builder / 博客建站**：检索上常与 *website builder for blogs*、*best blogging platform*、*create a blog* **同 SERP**——指能 **托管或一键发布博客** 的建站器、CMS 或 born-blog 平台，而非纯 API 文档站。
- **Website builder + blog module**：Wix、Squarespace、WordPress.com——**blog website builder 检索的主路径**（拖拽整站 + 博客区块）。
- **Blogging platform / Blog CMS**：消费者与 SEO 长文混用词；本簇 **次关键词**，不单独拆 slug（避免与 SERP 打架）。
- **Born-blog vertical**：Blogger、Ghost(Pro)——从第一天为 **发博客** 设计。
- **Newsletter-first**：Substack、beehiiv——邮件/付费为第一出口；Web 为配套，仍在 blog 选型 SERP 内。
- **Git-based blog**：MDX + SSG；工程路径 → Type E + 跨频道 [无 CMS 搭博客](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai)。
- **Headless blog**：API 存文、自建 UI → [`headless-cms`](../cms/headless-cms.md)。

---

## 专题对照：出版栈 × 买家意图

| 维度 | **Wix / Squarespace** | **WordPress** | **Ghost** | **Substack** | **Blogger** | **Medium** |
|------|----------------------|---------------|-----------|--------------|-------------|------------|
| 在 SERP 中的角色 | **Builder + 博客** | 份额基准 + SEO | 出版垂直 | Newsletter 网络 | 极简免费 | Syndication |
| Alignify 主 slug | **blog-website-builder** | **blog-website-builder** | **blog-website-builder** | **blog-website-builder** | **blog-website-builder** | syndicate only |

---

## 问题域

- **检索量集中在 builder 语言**：`blog website builder` Bing 代理 **~898k** >> `blogging platform` ~45k（2026-08-28）——KB 与正式文锚 **builder**，文内覆盖 platform/CMS 变体。
- **Listicle 混排**：同一篇「best blog website builder」含托管建站器与 Ghost/Substack——**不按内部轴拆成两篇**。
- **SEO 内容营销 vs 创作者订阅**：WordPress 插件生态 vs Substack 10%——在同一选型表解决。
- **工程路径**：Headless / Git 在文末或 FAQ 链出，不占 builder 头词 H1。

---

## 形态谱系（Type 定义 · 产品见 §工具与产品类型）

- **Type A — Website builder + blog（SERP 主路径）**：托管拖拽/AI 整站，博客为内置模块。适合 **「blog website builder」检索意图**、SMB、快启。
- **Type B — Born-blog 托管 SaaS**：Blogger、Ghost(Pro)、WordPress.com 博客档。适合 **极简/出版垂直**。
- **Type C — OSS 自托管 WCM**：WordPress.org、Ghost self-host。适合 **SEO 控制、插件、主权**。
- **Type D — Newsletter-first**：Substack、beehiiv。适合 **付费通讯 + 发现网络**。
- **Type E — Git / SSG 博客**：Astro、Hugo、Tina。适合 **工程 PR 审稿**。
- **Type F — Headless blog**：→ [`headless-cms`](../cms/headless-cms.md)（SERP 不同，[`cms/`](../cms/README.md) 簇）。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **平台锁定**：Substack/Medium、建站器主题格式；迁移需导出与 301。
- **SEO**：WordPress 重度 SEO vs 建站器博客上限；canonical / POSSE（Medium 不宜作主源）。
- **WordPress 攻击面**：插件/主题；最小权限。
- **费用**：Substack 10% vs Ghost flat；Wix/Squarespace 月费 vs 自托管 TCO。
- **与 documentation / knowledge-base 混用**：API 文档站 ≠ 博客建站。

---

## 落地碎片

- **搜的是 blog website builder** → 先看 **Type A**（Wix/Squarespace/WP.com）与 **Type C**（WordPress.org）对比表，再看 Ghost/Substack 是否需要。
- **要发现网络、接受 10%** → Substack。
- **要 0% 订阅抽成** → Ghost(Pro) 或 WordPress + Member。
- **工程已有 Next** → headless-cms 或 Git 路线（链跨频道文）。
- **Wix vs Squarespace 博客**：Squarespace 写作流常更顺；重度 SEO 仍倾向 WordPress。

---

## 工具与产品类型（「blog website builder」SERP 常混品类；非穷尽）

> **列举顺序**：**builder + 博客（Type A）** 先于 born-blog 垂直，再列 Newsletter / Git。份额见 **§市场份额快照**。

| 类型（英文常检索词） | 垂直 / 典型 | 备注 |
|---------------------|------------|------|
| **Website builder + blog** | **Wix**, Squarespace, WordPress.com | **blog website builder 头词主路径** |
| **Born-blog SaaS** | **Blogger**, Ghost(Pro) | 极简 / 出版 |
| **OSS 自托管** | WordPress.org, Ghost self-host | SEO / 插件生态 |
| **Newsletter-first** | Substack, beehiiv | 邮件垂直 |
| **Git / SSG** | Astro, Hugo, Tina | Type E |
| **Headless blog** | — | Type F → headless-cms |
| **分发网络** | Medium | syndicate |

### 按场景 → Type

| 若 PRIMARY 需求是… | Type |
|-------------------|------|
| 拖拽建站 + 博客、快启 | **A** |
| Google 账号即用极简博客 | **B**（Blogger） |
| SEO 内容营销 + 插件 | **C**（WordPress） |
| 付费 Newsletter + 网络 | **D** |
| Git MDX / 无 CMS AI 建系统 | **E** + 跨频道文 |
| API + Next 产品博客 | **F** → headless-cms |

### 市场份额快照（W3Techs · 2026-08 · 占**已知 CMS**网站）

| 产品 | CMS 份额 | 占全部网站 | 来源 |
|------|----------|-----------|------|
| WordPress | **58.9%** | **40.7%** | [w3techs.com/technologies/details/cm-WordPress](https://w3techs.com/technologies/details/cm-WordPress) |
| Shopify | 7.7% | 5.3% | [CMS overview](https://w3techs.com/technologies/overview/content_management/) |
| Wix | 6.1% | 4.2% | 同上 |
| Ghost | ~0.1% | ~0.1% | [Ghost detail](https://w3techs.com/technologies/details/cm-ghost) |

*广义 CMS 份额 ≠ blog-only 最佳；选型结合 Type 表。*

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Wix — Create a blog** | Builder + 博客营销路径 | [wix.com/blog](https://www.wix.com/blog) |
| **Squarespace — Blogging** | 设计向 builder + 博客 | [squarespace.com/blog](https://www.squarespace.com/blog) |
| **WordPress.com — Create blog** | 托管 WP 博客 | [wordpress.com/create-blog](https://wordpress.com/create-blog/) |
| **Blogger** | Google born-blog | [blogger.com](https://www.blogger.com/) |
| **Ghost** | 出版 + Newsletter | [ghost.org](https://ghost.org/) |
| **Substack** | Newsletter-first | [substack.com](https://substack.com/) |
| **W3Techs — CMS** | 份额 | [w3techs.com/technologies/overview/content_management/](https://w3techs.com/technologies/overview/content_management/) |

### 对比与测评（第三方；观点非官方）

- **born-blog vs 通用 builder**：Ghost/Substack 偏出版 Newsletter；Wix/Squarespace 偏营销站点——W3Techs 份额≠ blog-only 最优（§外链索引 W3Techs 行）。
- **托管 vs 自托管**：WordPress.com 与 WordPress.org 勿混——OSS 深度见 [open-source-cms.md](../cms/open-source-cms.md)。

*观点非官方。*

---

## 延伸阅读 · 站内外

**站内 / 底稿**

- 调研底稿：[blog-cms-web-search-2026-08-28.md](../../../temp/blog-cms-web-search-2026-08-28.md)
- 正式文 Brief：[../../insights/_briefs/blog-website-builder.md](../../insights/_briefs/blog-website-builder.md)

---

*档位：B · KB → `/blog/blog-website-builder` · Territory：编程工具链 · 簇：`blog-website-builder`*