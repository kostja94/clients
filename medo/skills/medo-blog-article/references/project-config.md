# MeDo Blog — 项目配置与 Gate 清单

> Agent 在 Phase 0 / Phase 5 前加载本文件。创作阶段禁止读取 `medo.md` 等外部文档。

---

## 1. 品牌与项目配置

| 配置项 | MeDo 值 |
|--------|---------|
| **品牌/产品名** | MeDo |
| **对外叙事** | MeDo by Baidu（Product Hunt、新闻语境） |
| **文档代号** | MIAODA（Baidu AI Cloud 文档体系） |
| **公司** | Sailai Private Limited（文档披露） |
| **主域名** | medo.dev |
| **文档入口** | https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en |
| **博客 URL 模式** | `https://medo.dev/blog/{slug}` |
| **博客路径前缀** | /blog/ |
| **品类 one-liner** | Build full-stack Apps With No-Code AI Platform |
| **Blog 叙事主轴** | Ship real native iOS/Android apps with AI vibe coding |
| **消费单位** | Credits（按生成/迭代扣费；具体数值 **随版本变化**，正文须 `as of {month} {year}`） |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **署名默认** | Kostja |
| **Lovable 预览** | medo-ai.lovable.app/blog/{slug}（CMS 导入参考，非创作依赖） |

### 1.1 目标受众（ICP）

| 层级 | 画像 |
|------|------|
| **Primary** | 从未打开 Xcode 的非开发者；有 App 想法但无工程团队 |
| **Secondary** | Indie/Solo 创始人、PM/设计师、教培机构创作者 |
| **Tertiary** | Affiliate/KOL 推广 MeDo（30% recurring 佣金叙事，**待验证** 现网条款） |

### 1.2 Blog 差异化叙事（每篇须一致）

1. **真原生 iOS/Android**（Swift/Kotlin），不是 PWA/Capacitor 包装
2. **非开发者友好**：不假装零工作量，但瓶颈已从「写代码」转向「想清楚要什么」
3. **真机测试**：QR 码预览 → TestFlight → 上架路径
4. **诚实对比**：Wirecutter 式，承认竞品长处
5. **working system, not mockup**：全栈真应用，非 Demo UI

### 1.3 可链接 URL 白名单

| 类型 | 路径 | 说明 |
|------|------|------|
| 博客 | `/blog/{slug}` | 见 content-graph.md |
| 移动构建工具页 | `/ai-mobile-app-builder` | 主转化 CTA |
| 组件库页 | `/components` | MeDo Components（Components 簇 CTA） |
| 功能页 | `/features` | 功能细节 |
| 首页 / 广场 | `/` | 社会证明、UGC 广场 |

### 1.4 禁止内链（未上线）

| 路径 | 状态 | 规则 |
|------|------|------|
| `/pricing` | 待建 | 正文不链；可文字提及「定价页 forthcoming」≤1 次 |
| `/vs/lovable`、`/vs/bolt` 等 | 待建 | 用博客 Alternative 文承接；forthcoming ≤1 且仅 Related 脚注 |
| `/templates/*` | 待建 | 不链 |

**G6**：forthcoming 链接全文 ≤1；正文核心流程不得使用 forthcoming 链接。

---

## 2. G1–G7 一票否决阻断规则

以下 7 项为发布前硬性阻断——**任一项触发则文章不得发布**，修复后重新过 Gate。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **G1** | 事实错误 | 产品能力、Credits、移动输出类型与 medo.dev 现网矛盾 | 逐 claim 对照 product-competitors.md §MeDo 事实表。功能不在当前版本 → 不能声称「已发布」。Credits → 标注 `as of [date]`。 |
| **G2** | 死链 | 内链 404；产品页路径错误 | 逐个检查所有内链是否在白名单内。外链可有 1–2 失效，但不能全挂。 |
| **G3** | 无来源数字 | 「17k+ apps」、竞品定价、市占无 attribution | P0 级数字必须可追溯到原始来源或标注内部数据基础 + 时间窗。单案例不能写成复数趋势。 |
| **G4** | 竞品/产品状态错误 | GA/Beta/Deprecated 与官方公告矛盾 | 打开竞品官网/docs 验证。已 Deprecated 功能不能标为 active。 |
| **G5** | 产品能力夸大 | 禁「唯一支持」「全球首个」「唯一能上架 App Store」；Credits 勿写死；禁未验证 fastest/cheapest | 用 "designed to"、"aims to" 表定位；非已实现功能。 |
| **G6** | 内链指向未上线页面 | 对照 §1.3 白名单 | 只链白名单内路径；forthcoming >1 → Fail。 |
| **G7** | 品牌/合规风险 | 对比文贬低竞品；App Store 政策无来源；误导性上架承诺 | 竞品措辞："just"、"merely"、"only does X" 为贬低触发词。上架文须链 Apple/Google 官方政策。 |

---

## 3. A1–A4 MeDo 专属 Gate

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **A1** | 平台分类错误 | 将 Web wrapper 描述为「真原生」；Swift/Kotlin vs RN vs Capacitor 分类错误 | 对照 product-competitors.md 三分类框架。Lovable/Bolt 移动 = web wrapper，非 native generator。 |
| **A2** | 政策无时效 | App Store / Play 政策 claim 无 `as of {month} {year}` 或无可追溯官方链 | 对照 app-store-compliance.md。拒审规则、账户删除、隐私要求须有官方来源。 |
| **A3** | 对比不客观 | 对比/Alternative 文缺少竞品 ≥1 真实优势；或缺少 ≥1 非 MeDo 更合适场景 | 每篇 Comparison/Alternative 须有 "When X is the better choice" 段。 |
| **A4** | 工具页抢词 | 博客 H1/title 抢 `/ai-mobile-app-builder` 工具页 P0 词 | 对照 keywords.md 禁抢词表。Blog 用长尾/场景词；品牌对比词（medo vs lovable）可进 title。 |

**G1–G7 + A1–A4 全部 Pass 方可交付。**

### Gate 补充：待验证声明的处理

project-config.md §5 和 product-competitors.md 中标记「待验证」的数据（17k+ apps、$5/2000 credits、affiliate 30% 等），正文**可以引用**，但须同时满足以下条件，否则触发 G1：

1. 标注来源限定：`per Product Hunt launch narrative` 或 `as of {date} per medo.dev gallery`
2. 不使用确定性语气：用 "reportedly"、"claims to offer" 替代 "offers"、"has"
3. Source Map 中标注 `Unverified — per {source}`
4. 单个 claim 的待验证状态不影响文章其他部分通过 G1

若待验证数据是文章的核心论证支柱（如 DecisionGuide cost 文依赖 $5/2000 credits），则该文应降级为草稿，等人类验证后再发布。

---

## 4. 敏感表述与合规

| 禁止 | 替代 |
|------|------|
| 唯一 / 全球首个 / only platform that | designed for / strongest fit for |
| 保证过审 / guaranteed App Store approval | improves your odds / reduces common rejection reasons |
| 免费无限 / unlimited free | credit-limited free tier（as of date） |
| click here / learn more（锚文本） | 描述性短语锚文本 |

### Disclosure 说明（不使用 frontmatter disclosure 字段）

**frontmatter 不写 `disclosure` 字段**（2026-08-14 起废弃）。对比/选型文的诚实性由正文内容承载：每个竞品 ≥1 真实优势 + ≥1「何时选竞品」场景（A3 Gate），无需额外的披露声明行。定价/政策时效由正文 `as of {month} {year}` + 官方链接承载（A2/G3 Gate）。

### 政策时效模板（PublishGuide / Diagnosis 正文必填，A2）

政策声明由**正文引用块**承载（不入 frontmatter），全文仅 1 处：

> Based on Apple App Store Review Guidelines and Google Play policies as of June 2026. Store rules change — verify current requirements before submitting.

---

## 5. 运营叙事（Blog 可引用，须标注待验证）

| 叙事 | 对外表达 | 验证状态 |
|------|----------|----------|
| 广场规模 | 17k+ apps on the gallery | **待验证** 实时计数 |
| PH 成绩 | Product Hunt #1 | 外部可查证 |
| Hackathon | Build with MeDo Hackathon, $50,000 prize pool | 官网 Banner |
| Affiliate | 30% recurring commission | **待验证** 条款页 |
| Credits 入门 | $5/2000 credits（PH 叙事） | **待验证** 定价页 |
| 每日免费 credits | Product Hunt 叙事 | **待验证** |

正文引用以上数字须加 `as of {date}` 或「per Product Hunt launch narrative」等限定。
