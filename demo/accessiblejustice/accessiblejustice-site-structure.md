# Accessible Justice 网站结构与 URL 架构

> **本文职责**：页面优先级、URL 结构、导航层级、多语言结构、分阶段上线计划。产品概览、关键词、竞品详见各自子文档。
> 关联文档：[accessiblejustice.md](./accessiblejustice.md) | [accessiblejustice-features.md](./accessiblejustice-features.md) | [accessiblejustice-keywords.md](./accessiblejustice-keywords.md) | [accessiblejustice-competitors.md](./accessiblejustice-competitors.md) | [accessiblejustice-use-cases.md](./accessiblejustice-use-cases.md) | [accessiblejustice-growth-strategy.md](./accessiblejustice-growth-strategy.md) | [README.md](./README.md)

---

## 1. 当前网站结构（基于网站分析）

| 路径/区块 | 描述 | 类型 | SEO 状态 |
|-----------|------|------|---------|
| / | 首页（着陆页）— Hero + How It Works + Why + Service Package + Footer | 多区块单页 | 可索引性待验证 |
| /start | 开始申请页 — "Start Your Claim"入口 | 功能页 | 待验证 |

**当前状态**：Accessible Justice 网站结构极简——主要为单页着陆页 + 一个申请入口。这是有限发布阶段的典型特征，SEO 基础设施几乎为空白。核心问题：
1. **极度缺少独立页面**：几乎没有可以承接搜索流量的子页面
2. **缺少多语言页面**：虽宣称中/英/西三语，但未见独立的语言版本 URL
3. **无 Blog**：所有长尾法律教育搜索词无承接载体
4. **无竞品对比页**：DoNotPay、Rentrieve 等竞品截流词无承接
5. **法律内容未被搜索引擎捕获**：California Civil Code §1950.5、21 天规则等核心法律信息仅在首页简略提及

---

## 2. 推荐 URL 结构

### 2.1 核心路径表

| 路径 | 页面 | 目标关键词 | 优先级 | 阶段 |
|------|------|-----------|--------|------|
| / | 首页（英文默认） | landlord didn't return deposit、get security deposit back、AI security deposit help | P0 | 已完成 |
| /zh/ | 中文着陆页（新建） | 加州押金不退怎么办、租房押金被扣怎么办 | P0 | 第一阶段 |
| /es/ | 西语着陆页（新建） | Cómo recuperar mi depósito、el arrendador no me devuelve el depósito | P0 | 第一阶段 |
| /how-it-works | 服务流程页（扩展） | AI demand letter deposit、attorney reviewed demand letter | P0 | 第一阶段 |
| /compare | 竞品对比页（新建） | DoNotPay alternative、Rentrieve alternative | P0 | 第一阶段 |
| /start | 开始申请 | — | P0 | 已完成 |
| /blog | Blog 索引（新建） | — | P1 | 第二阶段 |
| /blog/california-security-deposit-law-21-days | 21 天法则详解 | California security deposit law 21 days | P1 | 第二阶段 |
| /blog/normal-wear-and-tear-vs-damage | 正常损耗 vs 损坏指南 | normal wear and tear security deposit | P1 | 第二阶段 |
| /blog/sc-100-small-claims-guide | SC-100 填表指南 | SC-100 form California、small claims deposit California | P1 | 第二阶段 |
| /blog/tenants-rights-immigrants-california | 移民租客权益指南 | tenant rights security deposit for immigrants | P2 | 第三阶段 |
| /calculator | 押金索赔计算器（新建） | security deposit calculator California | P2 | 第三阶段 |

### 2.2 国际化 URL 策略

```text
accessiblejustice.ai/          → 英文（默认，x-default）
accessiblejustice.ai/zh/       → 简体中文
accessiblejustice.ai/es/       → 西班牙语（Español）
```

设置 hreflang 标签：
- 英文页：`<link rel="alternate" hreflang="en" href="https://accessiblejustice.ai/" />`
- 中文页：`<link rel="alternate" hreflang="zh" href="https://accessiblejustice.ai/zh/" />`
- 西语页：`<link rel="alternate" hreflang="es" href="https://accessiblejustice.ai/es/" />`
- x-default：指向英文页

**多语言内容策略**：
- 首页：三语各自独立着陆页（不自动翻译——母语撰写）
- /how-it-works 和 /compare：仅英文 + 中文（西班牙语用户更可能通过社区渠道直接进入申请流程）
- Blog：英文为主，核心指南翻译为中文版本

### 2.3 URL 设计原则

- 英文路径，短且干净
- 全小写，连字符分隔（如 `/how-it-works`）
- 语言版本使用子目录（`/zh/`、`/es/`）
- 无技术栈后缀
- Blog 使用 `/blog/{slug}` 模式

---

## 3. 导航架构

### 3.1 推荐主导航（Header）

```text
How It Works    |    Compare    |    Blog    |    中文    |    Español    |    Start Your Claim
/how-it-works    /compare        /blog       /zh/         /es/             /start
```

### 3.2 推荐底部导航（Footer）

```text
服务：How It Works | Start Your Claim | Compare
法律：California Civil Code §1950.5 | 21-Day Rule | Your Rights
资源：Blog | Free Legal Resources | FAQ
公司：About | Contact
法律声明：Not a law firm — legal services provided by independent licensed attorneys
```

### 3.3 面包屑导航

```text
Home > How It Works
Home > Blog > California Security Deposit Law: The 21-Day Rule
Home > 中文 > 如何追回加州租房押金
```

---

## 4. 分阶段上线计划

### 第一阶段 — 立即（建立多语言 SEO 基础 + 核心页面）

| 页面 | 理由 |
|------|------|
| /zh/ 中文着陆页 | 承接华人租客核心搜索——"加州押金不退怎么办"——竞品全部缺失的蓝海 SEO 词 |
| /es/ 西语着陆页 | 承接拉丁裔租客核心搜索——西班牙语法律科技几乎零竞争 |
| /how-it-works 扩展 | 将首页"四步流程"扩展为独立 SEO 页面，承接"AI demand letter""attorney reviewed"等差异化关键词 |
| /compare | 紧急建立 DoNotPay alternative 等截流词承接页——DoNotPay FTC 事件产生的搜索流量窗口 |

**第一阶段目标**：为三种语言各自建立独立 SEO 着陆页；为"alternative"截流词和"AI + 律师"差异化词建立承接载体。

### 第二阶段 — 1 个月（教育内容引擎）

| 页面 | 理由 |
|------|------|
| /blog + 3-5 篇核心指南 | 21 天法则详解、正常损耗 vs 损坏、SC-100 填表、清洁费争议、地毯折旧——每个长尾搜索词对应一篇 Blog |
| 中文 Blog 翻译 | 核心指南的中文版本——中文长尾法律搜索词几乎没有竞争 |

**第二阶段目标**：建立内容引擎，开始覆盖长尾法律教育搜索词。

### 第三阶段 — 3 个月（工具 + 深度内容）

| 页面 | 理由 |
|------|------|
| /calculator | 押金索赔计算器——高互动性工具页，计算 2x bad faith 赔偿金额 |
| 深度 Blog 内容 | 移民租客权益、加州各城市租房法规差异、成功案例故事 |
| 合作伙伴页面 | Legal Aid 机构、社区中心、移民服务组织的合作入口 |

**第三阶段目标**：丰富网站内容矩阵，建设实用工具，强化合作渠道。

---

## 5. 技术 SEO 建议

| 项目 | 建议 |
|------|------|
| 渲染 | 确认搜索引擎可完整抓取首页内容 |
| 页面标题 | 每页独立标题：`{页面主题} — Accessible Justice`；中文页：`{页面主题} — Accessible Justice（加州租房押金追回）` |
| Meta Description | 每页独立，150-160 字符；多语言页使用对应语言撰写 |
| Canonical | 每页自指 canonical；多语言版本设置正确 hreflang |
| hreflang | 三语设置（en / zh / es）——这在美国法律科技中极其罕见，是 SEO 蓝海优势 |
| Schema | 首页：Organization schema + LegalService schema（注意正确标记"technonlogy company, not law firm"） |
| Sitemap | 生成 XML sitemap 包含所有语言版本，提交 GSC |
| 性能 | 优先优化 LCP |
| Open Graph | 所有页面完整 OG 标签——租客在社交媒体上分享"追回押金"的故事是强大的获客渠道 |
| 结构化数据 | FAQ 区块使用 FAQ schema；/how-it-works 使用 HowTo schema；Blog 使用 Article schema |

---

## 6. 关键词/场景/增长映射

| 页面 | 关键词 | 场景 | 增长阶段 |
|------|--------|------|---------|
| / (EN) | landlord didn't return deposit、get deposit back | 所有人物第一接触 | 获客 |
| /zh/ | 加州押金不退怎么办 | Wei（华人租客） | 获客（蓝海） |
| /es/ | Cómo recuperar mi depósito | Maria（拉丁裔租客） | 获客（蓝海） |
| /how-it-works | AI + attorney reviewed demand letter | 所有人物（信任建立） | 转化 |
| /compare | DoNotPay alternative、Rentrieve alternative | 对比评估阶段 | 获客 + 转化 |
| /blog | 21 days law、normal wear and tear | 所有人物（法律教育） | 获客 + 留存 |
| /calculator | deposit calculator | Jordan（决策工具） | 激活 + 转化 |

---

*文档创建：2026-07-01 | 模式：Mode A 冷启动 — 国际版 | URL 架构为基于网站结构分析的建议 | 来源：[accessiblejustice.ai](https://accessiblejustice.ai/) 网站结构分析*
