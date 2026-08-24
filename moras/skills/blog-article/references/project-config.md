## §1 项目配置与 G1–G7 阻断规则

> **话题范围感知**：以下配置以 **TikTok Shop affiliate** 为默认上下文（portfolio **64 篇**，见 `content-graph.md` §4.1）。若 Phase 0.0 判定话题范围 ≠ TikTok Shop affiliate，Agent 以声明的话题范围为准——跳过不适用的 Gate（如 I3 对非 TikTok 话题自动通过）、调整 ICP 称谓、放宽市场限制。G1–G7 通用阻断规则对所有话题生效。

### 1.1 项目配置

| 配置项 | Moras 值 |
|--------|----------|
| **品牌/产品名** | Moras、K2 Lab、K2LAB |
| **产品名大小写** | 正文与 frontmatter 统一 **Moras**；K2 Lab / K2LAB 仅公司/页脚语境 |
| **主域名** | moras.ai |
| **blogLayout** | cluster-folders（`moras/blog/{folder}/NN-{slug}.md`；Cluster D 根目录；见 `topic-cluster-layout.md`） |
| **博客路径前缀** | `/blog/`（frontmatter `slug` 已含此前缀） |
| **作者** | `Kostja`（默认） |
| **Primary ICP（默认）** | **TikTok Shop 联盟客**（affiliate creators）、高佣带货达人、副业 side-hustle KOC。**非 TikTok Shop 话题可覆盖**——Agent 在 Phase 0.0 声明 ICP 后，以声明的 ICP 为准 |
| **Secondary ICP（默认）** | 美区卖家/品牌、MCN/机构（TikTok Shop 话题时 metadata 与正文仍以 affiliate 工作流为主轴） |
| **双核心能力 A** | **AI 选品** — TikTok Shop 美区数据驱动高佣/趋势商品 |
| **双核心能力 B** | **TT 商品视频生成** — 商品链接/卖点 → 竖屏可购短视频，批量/多版本 |
| **品类 one-liner** | AI Commerce Producer / Content e-Commerce Agent OS for US TikTok Shop affiliates |
| **技术叙事** | Orchestrator + 11 专精代理 + A2A 协议；选品→成片→数据飞轮 |
| **定价（以官网为准）** | **Pro** ~$1000/mo（600 条/月）；**Agency Partner** ~$20/mo + 50% commission；**Managed Service** $0 base + 70% commission |
| **Proof（可写）** | ~3 min/video、3 cuts/brief、600 videos/mo（Pro）；iOS App「Moras: Create & Earn with AI」；Wall of Love 证言 |
| **Proof（禁写）** | 普适 GMV/收入保证；「TikTok 官方合作/认证」；未验证市场份额数字 |
| **CTA 主链** | `https://moras.ai/` · App Store 下载 |
| **语言/市场（默认）** | 英文；**美区 TikTok Shop**（TikTok Shop 话题）。**非 TikTok Shop 话题**：市场依实际内容，语言仍为英文 |
| **禁止内链** | 404 或 forthcoming 的 `/product-research`、`/hashtag-generator`、`/caption-generator`、`/use-cases/*`；内链前假设需可访问 |

### 1.2 G1–G7 一票否决阻断规则

以下 7 项为发布前硬性阻断——**任一项触发则文章不得发布**，修复后重新过 Gate。Phase 6 SelfCheck 首维即逐项对照此表。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、定价、平台政策与 moras.ai / TikTok Shop US 官方矛盾 | 逐 claim 对照 §6.1 产品事实表。功能不在当前版本 → 不能声称"已发布"。 |
| **G2** | 死链 | 站内或站外链接 404/域名拼写错误 | 逐个检查内链（对照 §1.3 白名单）。外链可有 1–2 失效，但不能全挂。 |
| **G3** | 无来源数字 | 量化 claim（GMV、佣金%、73% creators）无 attribution | P0 级必须 `[Source: URL]` 或脚注；无来源则删或改定性表述。 |
| **G4** | 竞品/平台状态错误 | 工具 GA/Beta、TikTok Shop 政策与官方公告矛盾 | 打开竞品官网/docs 与 [seller.tiktok.com](https://seller.tiktok.com/) 验证。 |
| **G5** | 产品能力夸大 | 超出 GA 能力；禁「全球首个」「唯一支持」 | 定位语言（"designed to"）≠ 已实现功能。 |
| **G6** | 内链指向未上线页面 | 链到禁止内链列表或未发布路径 | 对照 §1.3 白名单；forthcoming ≤1 且仅 Conclusion/脚注。 |
| **G7** | 重大品牌/合规风险 | TikTok 官方暗示、GMV 保证、贬低竞品、品牌误拼 Morris | 对照 §6.4 合规红线。 |

**G6 补充**：forthcoming 上限 ≤1 个，且仅限 Conclusion 脚注。正文核心流程不得含 forthcoming 链接。

### 1.3 双核心意图 → 落地页（创作内链必查）

| 用户意图 | 动作词 | 主链目标 |
|---------|--------|---------|
| **Video / 成片** | generate, link-to-video, hooks, captions, shoppable | `/` · `/tiktok-video-generator` · `/tiktok-video-generator/{category}` |
| **Research / 选品** | product research, winning products, commission fit | `/product-research`（planned）· 博客 `tiktok-product-research` |

**策略**：全链路文通常需 **Both**；Framework/Strategy 文按节链向对应能力。

### 1.4 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}` — 见 §4（slug 不含 NN 前缀） |
| 首页 | `/` |
| TVG Hub | `/tiktok-video-generator`（preview） |
| TVG Vertical | `/tiktok-video-generator/{slug}` — 见 §6.3 |
| 工具页 | `/product-research` · `/hashtag-generator` · `/caption-generator`（planned） |
| 法务 | `/terms` · `/privacy`（live） |
| 外链 | TikTok Shop Seller Center、FTC、Reuters、Oxford Economics 等权威源 |

**内链格式**：Markdown `[锚文本](/blog/{slug})`；slug **不含** `NN-` 文件名前缀，与 frontmatter `slug` 字段一致（已含 `/blog/`）。

**G6 规则**：不链未上线页；forthcoming ≤1 且仅 Conclusion 脚注。

---


## Income Claim Gate（I1–I5，一票否决）

Moras 博客涉及佣金、副业收入、变现预期——此类声明需最严格证据标准。**I1–I5 任一项 Fail = 不得发布。**

| # | 阻断条件 | 严格标准 |
|---|---------|---------|
| **I1** | 收入承诺 | 任何 "you will earn $X"、"quit your job in 90 days"、"guaranteed income" 等无区间+条件的承诺。正确写法：给出范围（"$0–$1,500 in first 90 days"）+ 假设条件（发帖频率、受众有无、品类佣金率） |
| **I2** | 证言滥用 | Wall of Love / 截图 GMV 无 "testimonial" 标注 + 无 "Results vary; not typical guarantees" |
| **I3** | 平台政策无时效 | 佣金率、归因窗口、5k followers 门槛等 TikTok Shop 政策须标注 "as of {month} {year}" + 官方链接 |
| **I4** | Who/How/Why 缺失 | Pillar/Framework/Research 文必须含：作者语境（Who）、研究方法（How）、帮 affiliate 做决策（Why，非推销 Moras）。见 references/article-types.md §Who/How/Why |
| **I5** | 复述 SERP | Phase 0 Information Gain 检查 <2 项独有内容（见 §3 Phase 0 Gate A） |

**I2 补充**：证言数据（"$15,000 commission in 30 days"）仅在正文引用且标注 testimonial 语境，metadata 禁止出现 GMV 数字作承诺。
