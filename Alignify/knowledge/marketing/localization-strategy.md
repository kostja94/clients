# 本地化策略 · 知识块（非线性笔记）

**文件名与 slug**：本文件 basename `localization-strategy` 与站内路由 **`/marketing/localization-strategy`** 对齐。

**材料范围**：公开网络检索（Google hreflang 文档、next-intl / i18n 实践、Similarweb 市场流量分析用法、多语言 SEO 与「翻译 vs 本地化」讨论、Alignify 站内 **`content/marketing/*/localization-strategy.md`** 及本站 `/zh` 路由实现经验）；并归纳 Agent skill **localization-strategy**。**未**把 LSP 厂商营销页当作普适真理。网摘整理日期 **2026-06-24**。

**规范或长文对照**：Alignify 站内长文 [本地化策略（ZH）](https://alignify.co/zh/marketing/localization-strategy)；英文：`content/marketing/en/localization-strategy.md`。相邻专题：[keyword-research.md](./keyword-research.md)（各语言独立选词）、[geo.md](./geo.md)（多语言 AI 可见度）。

**Agent skill 对照**：locale 优先级与 hreflang 清单见 **localization-strategy**；本页为概念锚点。

以下条目可任意顺序阅读；**不是**文章体例。

---

**词汇锚点**

- **Localization（本地化）**：产品、内容、营销、定价与合规对特定语言/市场的系统适配；**≠** 直译。
- **Internationalization（i18n）**：代码与内容结构可扩展多语言；字符串外置、locale 路由、日期/货币格式。
- **Locale**：语言+地区标识（如 `zh`、`en-US`）；影响 hreflang 与内容变体。
- **Hreflang**：向搜索引擎声明语言/地区 URL 对应关系；避免 duplicate 与错误定向。
- **Subdirectory vs subdomain**：`/zh/` vs `zh.domain.com`；Alignify 采用 subdirectory + next-intl。
- **Translation memory / TMS**：翻译记忆与术语库；保证 product UI 与 marketing 用语一致。
- **Market prioritization**：按流量潜力、竞争、支付与合规选 locale 顺序。
- **Transcreation**：创意与营销文案的文化再创作；非字面翻译。

---

**专题对照 / 扩展定义**

| 维度 | **Translation** | **Localization** |
|------|-----------------|------------------|
| **目标** | 语言转换 | 市场适配 |
| **SEO** | 常 miss 本地 query | 独立 keyword research |
| **示例** | 英译中 UI | 中文定价、案例、支付 |
| **风险** | 术语不一致 | 过度延后 launch |

| 维度 | **Subdirectory** | **Subdomain** |
|------|------------------|---------------|
| **SEO 权威** | 常集中主域 | 分散（视实现） |
| **工程** | 单站 i18n | DNS/证书/部署分裂 |
| **Alignify** | `/zh/*` | — |

---

**问题域（为何会出现这类产品/方法论）**

- **Organic 流量国际化**：GSC/Similarweb 显示非英语市场已有 demand；不本地化等于放弃免费增长。
- **AI 产品全球 PLG**：注册无国界；仅英文 onboarding 造成非英语激活断层。
- **搜索意图语言差异**：同一概念在不同语言 SERP 结构不同；翻译词无排名。
- **合规与信任**：本地语言 support、隐私条款、发票与支付方式影响转化。
- **工程债**：后期补 i18n 比 launch 即 i18n-ready 贵一个数量级。

---

**能力栈（概念拆分，非厂商功能表）**

- **市场优先级**：流量、ARPU、竞争、support 能力、法规（GDPR、数据驻留）。
- **URL 与 hreflang 架构**：canonical、x-default、语言切换器、避免 machine-translate 薄内容。
- **各 locale 关键词研究**：本地工具、母语审校、非翻译 seed list。
- **术语与 style guide**：产品名、功能名、禁止译法；与 UI strings 同步。
- **Workflow**：MT + human post-edit vs 全人工；更新 sync 与 outdated 检测。
- **定价与 GTM 本地化**：货币、trial 长度、case study 人物本地化。
- **测量**：分 locale 的 GSC、激活、付费；勿用全球 aggregate 掩盖失败 locale。

---

**形态谱系（与具体品牌解耦）**

- **English-first 延后型**：先验证 PMF 再开第二语言——适合极小团队。
- **Parallel locale 型**：中英同步更新——适合 content-driven（Alignify 模式）。
- **Market-led 型**：按国家开 landing + 本地 payment——偏 enterprise。
- **MT-heavy 型**：机器翻译全站 + 人工审校 TOP 页——偏 breadth。
- **Partner-led 型**：本地 reseller/ agency 写内容——偏 B2B 区域扩张。

---

**风险 · 合规 · 边界**

- **Hreflang 错误**：互指缺失导致 wrong locale 排名或 duplicate。
- **Thin auto-translate**：低质量 MT 全站可能触发 helpful content 负面信号。
- **术语分裂**：UI 称「工作区」、marketing 称「项目空间」——损害 trust。
- **法律与隐私**：GDPR、PIPL 等；隐私政策与 DPA 需 locale 版本。
- **资源分散**：10 个 locale 各做半套不如 2 个 locale 做全套。
- **RTL 与排版**：阿拉伯语等需 UI 与 CSS 预留；非仅翻译字符串。

---

**落地碎片（无先后）**

- 第二语言上线前完成 **hreflang + sitemap locale** 与 x-default。
- **每个 locale 独立 keyword list**；禁止从英文 SERP 直译做主词。
- 建立 **glossary CSV**（EN/ZH/…）；PR 与 UI 共用。
- Similarweb / GSC **国家维度** 定下一批 locale 优先级。
- 语言切换器链到 **同等深度 URL**；缺翻译页显式 fallback 策略。
- 与 **geo/SEO** 同步：中文 FAQ 同样服务 AI 中文答案检索。
- 季度 **locale parity audit**：英文新文是否滞后翻译超过 30 天。

---

**工具与产品类型（检索里常混在一起的品类；非穷尽）**

| 类型 | 代表方向 | 备注 |
|------|----------|------|
| **i18n framework** | next-intl, react-i18next | 路由与字符串 |
| **TMS** | Lokalise, Phrase, Crowdin | UI + marketing 协作 |
| **MT** | DeepL, Google Translate API | 初稿 + 审校 |
| **SEO** | Ahrefs/Semrush 多语言、GSC | 分 locale 监测 |
| **Analytics** | GA4 国家/语言 | 与 GSC 交叉 |

---

**外链索引（检索整理；非广告、无排序优先级）**

### 框架与方法论

| 名称 | 说明 | URL |
|------|------|-----|
| **Google · Hreflang** | 多语言/多地区 URL 声明 | [developers.google.com/search/docs/specialty/international](https://developers.google.com/search/docs/specialty/international/localized-versions) |
| **W3C · i18n** | 国际化基础 | [w3.org/International](https://www.w3.org/International/) |

### 站内索引（Alignify）

| 说明 | URL |
|------|-----|
| **本地化策略长文（中文）** | [alignify.co/zh/marketing/localization-strategy](https://alignify.co/zh/marketing/localization-strategy) |
| **关键词调研（相邻）** | [alignify.co/zh/marketing/keyword-research](https://alignify.co/zh/marketing/keyword-research) |

### 对比与测评（第三方；观点非 official）

对 **「subdirectory vs subdomain」**：Google 称均可，工程与品牌偏好主导。对 **MT-first**，一方求速度，另一方警告 thin content；**TOP 20% 流量页 human-first** 是常见折中。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

**延伸阅读与参考材料**

- **next-intl 文档**：App Router locale 路由（Alignify 栈）。
- **Alignify keyword-research**：各语言 Topical Map。
- **Alignify pricing-strategy**：区域定价与 packaging。
