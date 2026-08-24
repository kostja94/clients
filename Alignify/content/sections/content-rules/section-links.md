# 链接规范（内链、外链、按钮及全站链接规则）

本文档定义网站中**所有链接**的使用规范，包括内链、外链、按钮样式及各组件的链接规则。

**适用范围**：所有工具介绍页面、文章页面、导航、Banner、分享按钮等含链接的组件。

**参考**：section-what-is（内链放置）、section-faq（FAQ 禁链；Tools JSON FAQ 例外见该文档）、section-best-tools（产品链接）、section-references（引用链接）、section-share-buttons（分享按钮组件）

**内链规范（Alignify 唯一真相源）**：[alignify-internal-links.md](../../alignify-internal-links.md)（Tools / SEO / 编辑方法论 / R1–R7 / 附录 B/C）。

---

## 一、内链规则

### 1.1 唯一性与分布

- **同一内链只出现一次**：同一个内链 URL 在整个页面中只能出现一次
- **不在同一 H2 中重复**：同一个内链不能在同一 H2 章节中出现多次
- **分布在不同章节**：内链应分布在不同的 H2 或 H3 章节中
- **「提高内链频率」的含义**：指增加**不同目标 URL**（不同 `/tools/{slug}` 或频道页）的出现次数，并让它们落在 TLDR、什么是、如何工作、场景、如何选择、结论等不同区块；**不是**在同一页内对同一 slug 重复加链。试点类目（如 Avatar、Background Changer）可在不违反本条的前提下，比「仅在什么是放 2 条」再多链向若干互补 spoke；细则见 [alignify-internal-links.md §3.1.5](../../alignify-internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留)
- **优先位置**：放在最相关、最自然的章节中
- **场景匹配**：放在最能体现相关性的场景

### 1.2 内链放置

- **中文优先**：「什么是 XXX」章节
- **英文优先**：「What Are XXX」章节
- 参见 [section-what-is](./section-what-is.md)、[section-tldr](./section-tldr.md)

### 1.3 内链相关性原则

**内链目标必须与当前主题有强功能关联或工作流关联**，避免为凑数而强行链接。

| 关联类型 | 说明 | 示例 |
|----------|------|------|
| **功能互补** | 同一工作流中上下游工具 | 音乐生成 → 视频编辑（为视频配乐）、MV 生成 |
| **同质替代** | 解决同类问题的不同工具 | 变声器 ↔ 文字转语音 ↔ 声音克隆（均为人声处理） |
| **场景延伸** | 同一使用场景下的不同需求 | 视频制作：视频编辑 + 音乐生成 |

**避免**：仅因同属某大类而链接。例如音乐生成与文字转语音、声音克隆虽同属「音频」，但音乐是旋律创作、后两者是人声处理，功能边界不同，不宜作为内链目标。详见 [section-what-is 3.4、3.6](./section-what-is.md#34-内链相关性原则)。

### 1.4 内链样式

- **正文内链**：`.link-internal` 或 `.blog-post-content a`（非外链）
- **样式**：`text-inherit font-medium underline underline-offset-2 decoration-foreground/30`，hover 加深下划线 `decoration-foreground/50`（由 `src/index.css` 全局控制）
- 参见 [section-also-interested-in](./section-also-interested-in.md)

### 1.5 FAQ 内链规则

- **MDX `<FAQ />` 组件**：答案中禁止内链与外链。参见 [section-faq §3.1](./section-faq.md#31-faq-组件mdx-页面)。
- **`content/tools` 与 `content/blog` 的 `faq` 块**（Markdown 或 JSON；Tools 型 Blog 文含 `agent-sandbox` 等）：允许站内链，上限与全文唯一性见 [alignify-internal-links.md §3.1.5](../../alignify-internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留) 与 [section-faq §3.2](./section-faq.md#32-tools--blog-json-的-faq-块)。

### 1.6 正文内链密度（目标频次）

用于**新写与大改版**时控制可读性与主题相关内链的疏密；**不强制**短期内对存量全文批量回刷。[alignify-internal-links.md](../../alignify-internal-links.md) 中的**区块上限**（如 Tools TLDR ≤2 条不同 slug、FAQ 合计 ≤3 条等）**仍须同时满足**。

| 项目 | 规则 |
|------|------|
| **默认目标** | **正文**中约 **每 1000 个英文单词** 配置 **约 3 条**指向 **不同路径** 的站内链（与 §1.1「同一 URL 全页仅一次」一致；每条链计 1 个 distinct 目标）。 |
| **合理区间** | **约 2～4 条/千词** 即视为合格；极短正文不必硬凑，超长正文避免明显高于 4 条/千词（资源索引类专题若另有专册说明可从其规定）。 |
| **「正文」范围** | **计入密度语境**：TLDR 引言与要点中的叙述、「什么是 / What are」、How it works、应用场景、如何选择、结论、对比表前的 `introHtml` 等**连贯说明性**段落。 |
| **不计入** | MDX FAQ 答案（仍禁链）；Tools/Blog JSON 的 FAQ 内链另遵守专册条数上限；BestTools 产品卡描述、References、纯表体文案、AlsoInterestedIn / Header / Footer 等全局组件。 |
| **中文稿** | 以汉字为主的正文，可近似 **每 350～450 汉字** 配 **约 1 条**站内链作等量参照（稀疏度与上表英文目标同档）；或以导出正文用工具统计后再换算。 |
| **专册** | SEO / Tools / Insights 等频道细节见 [alignify-internal-links.md](../../alignify-internal-links.md) §3–§5；密度为正文层总控，与区块规则不冲突时一并执行。 |

---

## 二、外链规则

### 2.1 链接处理

- **UTM**：所有外部链接使用 `addUtmToExternalLink()` 添加 UTM 参数（`utm_source=kostja&utm_medium=blog`）
- **Rel**：使用 `getExternalLinkRel()` 设置 rel 属性（默认 `noopener noreferrer nofollow`）
- **例外**：Google、VoiSpark 链接使用 dofollow，不添加 nofollow
- **已有参数**：若 URL 已有查询参数（如 `?vsource=xxx`），则不添加通用 UTM

### 2.2 按钮样式

- **产品 CTA 按钮**：使用 `.btn-external-link` 样式类
- **文案**：中文 `试试 [产品名称]`，英文 `Try [产品名称]`
- **居中**：BestTools 中按钮居中展示

### 2.3 链接格式

- 完整的绝对 URL（含 `https://`）
- 优先产品官方页面链接，非公司首页

---

## 三、全站链接使用场景汇总

| 位置/组件 | 链接类型 | 规则 | 实现 |
|-----------|----------|------|------|
| **TopBanner** | 外链 | UTM、rel；链接到 VoiSpark 等 | `addUtmToExternalLink`、`getExternalLinkRel` |
| **ShareButtons** | 分享链接 | 分享到 Twitter/LinkedIn/Facebook；复制当前页绝对 URL | 组件内部 `getAbsoluteUrl(pageUrl)`，不添加 UTM |
| **Header** | 内链 | 导航菜单，Next.js `Link` | 相对路径，`getLocalizedHref` |
| **Footer** | 内链 + 外链 | footerLinks 为内链；socialLinks 为外链，需 UTM、rel | `Link` / `<a>` + `addUtmToExternalLink` |
| **BreadcrumbNav** | 内链 | 面包屑导航 | `Link`，相对路径 |
| **BlogLayout 作者** | 内链 | 作者页链接 | `/author/kostja` 或 `/zh/author/kostja` |
| **BestTools** | 内链或外链 | 产品链接：外链用 UTM、rel、`btn-external-link`；内链直接 `href` | 根据 `linkUrl` 判断 |
| **References** | 外链 | 组件列表：UTM、getExternalLinkRel；正文中引用：UTM、rel="noopener noreferrer" | 参见 [section-references](./section-references.md) |
| **YouTubeThumbnail** | 外链 | YouTube 链接，UTM、rel | 组件内部已处理 |
| **AlsoInterestedIn** | 内链 | 四卡片内链，`link-internal` | `Link` + `item.href` |
| **AITrafficTable** | 外链 | 产品链接，UTM、rel | `addUtmToExternalLink`、`getExternalLinkRel` |

### 3.1 ShareButtons 链接说明

- **分享**：打开 Twitter/LinkedIn/Facebook 分享对话框，URL 为当前页面（alignify.co）
- **复制链接**：复制当前页面的绝对 URL 到剪贴板
- **不添加 UTM**：分享的是本站 URL，无需 UTM
- 组件规范参见 [section-share-buttons](./section-share-buttons.md)

### 3.2 邮件链接

- **mailto**：如 `mailto:zyjstc@gmail.com`，无需 UTM、rel

---

## 四、产品链接验证与优化（Tools 页面）

**已迁移**至 [alignify-internal-links.md §3 第五节](../../alignify-internal-links.md#五产品链接验证与优化tools-页面)（含验证流程、无效链接处理、产品文案检查）。本节保留标题便于旧链接锚定；实质内容以该文档为准。

---

## 五、检查清单

- [ ] 每个内链 URL 在整个页面中只出现一次
- [ ] 同一内链不在同一 H2 章节中重复
- [ ] 内链分布在不同的 H2 或 H3 章节中
- [ ] **（新稿/大改版）** 正文内链密度大致符合 §1.6（约 3 条/千词，2～4 可；FAQ/产品卡等按专册排除）
- [ ] 内链目标与当前主题有强功能/工作流关联（非仅因同属某大类）
- [ ] 所有外链使用 `addUtmToExternalLink()` 和 `getExternalLinkRel()`
- [ ] 产品 CTA 按钮使用 `.btn-external-link`
- [ ] MDX FAQ 组件无内链、无外链；Tools/Blog JSON FAQ 内链符合专册 §1.5（全文唯一、FAQ ≤3 slug）
- [ ] 产品链接已验证有效
