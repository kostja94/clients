# Frontier Rounds — 项目记录索引

> **定位**：AI 融资额度的英文内容站（融资追踪 / 排行榜 / 投资机构档案）
> **域名**：[frontierrounds.com](https://frontierrounds.com)（已购）
> **代码来源**：`E:\自有部署项目\AI Funding Hub`（Lovable 导出的 TanStack Start + Vite 项目，现品牌名 "AI Capital"）
> **目标态**：Next.js App Router 项目（对齐 nova-scientia / alignify 等参考项目），部署于 **Cloudflare Workers**（不再用 Vercel）
> **记录创建**：2026-09-07

---

## 文件清单

| 文件 | 内容 | 状态 |
|------|------|------|
| [frontier-rounds-nextjs-build-plan.md](./frontier-rounds-nextjs-build-plan.md) | **完整构建 + 部署方案**：现状盘点、Next.js 迁移映射表、图片资产回填脚本、品牌换标、SEO 就位、Cloudflare（OpenNext）部署全步骤、上线验收清单 | ✅ 完成（2026-09-07） |
| [branding/](./branding/) | **最终品牌 SVG**：`fr-icon.svg`（黑底白图）、`fr-icon-mono.svg`（透明底纯黑）、`fr-wordmark.svg`（Instrument Serif 轮廓化 wordmark） | ✅ 完成（2026-09-07） |
| [funded-products/](./funded-products/) | **融资的 AI 产品**（25 份档案 + `_index.md`）：网站 Funding Leaderboard 上的真实融资 AI 产品，字段含累计融资/最大轮/估值/领投方/来源 URL/可信度 | ✅ 完成（2026-09-08；2026-09-10 增 Cognition） |
| [product-histories/](./product-histories/) | **产品融资时间线**（15 份档案 + `_index.md`）：Lovable / Mistral AI / OpenAI / Anthropic / xAI / Scale AI / SSI / Zhipu / Thinking Machines Lab / Ineffable Intelligence / AMI Labs / World Labs / Harvey / Clay / Cognition。网站 Product Histories（`/products`）逐轮融资档案，rounds[] 含每轮金额/估值/领投/参投/来源 | ✅ 完成（2026-09-08 首档；2026-09-10 扩至 15） |
| [funding-investors/](./funding-investors/) | **融资的投资方**（22 份档案 + `_index.md`）：网站 Investor Atlas 上的真实投资方，字段含基本档案/投资逻辑/投资组合（全部可溯源公司）；含 2026-09-08 新增的 Llama Ventures、5 家 AI 专项基金与 Menlo Ventures，及 2026-09-09 新增的 Lightspeed/Index/General Catalyst/Eric Schmidt（见下节） | ✅ 完成（2026-09-08；2026-09-09 扩至 22） |

## 执行进度

| 阶段 | 内容 | 状态 |
|------|------|------|
| 阶段 A（重构） | 代码仓 `E:\自有部署项目\frontierrounds`：Next.js 16 + Tailwind v4 + shadcn 全套组件 + 数据层迁移；图片 189 张回填 `public/logos\|portraits`；品牌换标 Frontier Rounds；sitemap/robots/404/error/metadata 就位 | ✅ 完成（2026-09-07） |
| 本地验证 | `npm run build` 通过（18 页全 SSG）；冒烟测试全绿 | ✅ 完成 |
| 阶段 B（部署） | GitHub 仓 `kostja94/frontier-rounds`（SSH 推送）+ Actions CI（ubuntu 构建 OpenNext）；wrangler routes 绑 `frontierrounds.com` + www；SSG 经 static-assets incremental cache 修复动态路由 404 | ✅ 上线（2026-09-07 21:5x） |

## 线上验收（2026-09-07）

- `https://frontierrounds.com` 200；`www` 200
- `/`、`/leaderboard`、`/investors`、`/investors/{11 个 slug}` 全部 200，无 "AI Capital" 残留，canonical 均指向 frontierrounds.com
- `/sitemap.xml`（含全部 investor slug）、`/robots.txt`、`/logos/*.png` 200；未知 investor slug 正确 404

## 数据治理：移除虚构演示轮次（2026-09-07）

- **问题**：首页 "Latest Funding Rounds" 区块的 25 条数据全部来自 Lovable 演示/样例（含 `Helion Labs`、`Mistral Forge`、`Quanta Vision` 等虚构公司），对真实内容站属误导性信息。
- **处置**：`src/data/fundingRounds.ts` 置为 `[]`（保留类型与 format 工具函数）；首页改为空态引导页（H1 "The money behind frontier AI, one round at a time." + Investor Atlas / Leaderboard CTA）；footer "Sample data / illustrative" 声明删除。
- **保留**：leaderboard（`fundingLeaderboard.ts`）与 investor 档案为另一套含真实公司 + sourceUrl 的数据，未受影响；investor 页 "Related rounds" 已有空态文案。
- **验收**：commit `cfe6252` 经 CI 部署；线上 `/` 已无虚构公司名与 sample 声明，4 条主路由全部 200。

## 站内真实数据归档（2026-09-08）

将网站现有的**两套真实数据**转录为可阅读/可追溯的 Markdown 档案，落在本记录仓：

- **[funded-products/](./funded-products/)** — "融资的 AI 产品"：24 家（OpenAI → Sarvam AI，按累计融资降序）。数据源 `fundingLeaderboard.ts`，每份档案含国家/赛道/累计融资/最大一轮/估值/最近融资日期/领投方/来源机构/数据可信度（Disclosed / Reported），并附 `sourceUrl` 溯源。
- **[funding-investors/](./funding-investors/)** — "融资的投资方"：18 家（Sequoia、a16z、HongShan、Peak XV、Shunwei、Lollapalooza、Llama Ventures、Gradient、Conviction、AIX、Air Street、Radical Ventures、Menlo Ventures、YC、MiraclePlus、Elad Gil、Naval、Nat Friedman）。数据源 `investors/profiles/*.json`，每份档案含基本档案表、投资逻辑（thesis）、投资组合（含官网链接与中文别名）、别名。

> 生成方式：临时解析脚本（`@temp/parse_fr_ts.py`）忠实转录站点 TS 数据层，字段与线上页面一致，未增删事实。**注意**：若线上站点后续增删条目，可重跑该脚本刷新本目录。

## 事实核查与数据修复（2026-09-08）

用 subagent 对 `funded-products/`（24 家）与 `funding-investors/`（11 家/人）档案逐项联网核查（公司存在性、金额/日期/估值/领投方、人物事实），**只依据公开来源**判定，无证据者不保留。发现的问题已同步修复线上数据层（`fundingLeaderboard.ts`、`investors/*.ts`）与本目录 md：

- **融资数据纠偏（约 30 处）**：OpenAI 领投方改为官方披露财团；Anthropic 累计 US$74.6B→US$118B、xAI→US$37B、Databricks→US$25B、SSI→US$8B、ElevenLabs→US$781M、Cerebras→US$2.85B、MiniMax→US$3.4B、Unitree→US$1.15B 等累计修正；Zhipu 更正为 2026-07 IPO 后配售（US$4B / 估值 US$64B，原"2024 Series D US$420M"为过时数据）；Harvey（US$200M G 轮 / US$11B / 2026-03-25）、Abridge（Series E / US$300M / 2025-06-24）、Physical Intelligence（2025-11-20 / CapitalG）、Mistral（2025-09-09 / ASML）、Scale AI（2025-06-12）等日期/轮次/领投方修正；**弱来源一律替换为官方或权威媒体 sourceUrl**（公司 blog、Reuters/CNBC/Bloomberg/STCN/36kr 等）。
- **机构档案修复**：a16z AUM US$45B→~US$106B（2026-03 Form ADV）；HongShan 对 Unitree 进入时点 2020→2019-12、MiniMax 轮次角色表述修正；Sequoia Doug Leone 2026-03 回归 chairman 时点、Harvey G 轮为 co-led。
- **个人天使档案修复**：Elad Gil 组合删除 **Cursor / Runway / Glean** 三项（CB Insights/融资报道查无投资记录，其中 Runway 属同名金融科技公司混淆），补入官网自证的 **OpenAI**，披露数 ~140 → 250+；Nat Friedman 组合删除 **Ideogram**（多源交叉无 NFDG 记录），SSI 备注补 Gross 联合创始人语境，Meta 任职表述精确化（Friedman=VP of Product & Applied Research 与 Alexandr Wang 共领 MSL，NFDG 停止新投资）。

> 修复原则：改前逐项复核实证，改后 TS（站点展示层）与本地 md（归档层）逐字一致；本次不涉及新增融资事件，仅修正既有条目。

## 新增投资方档案：Llama Ventures（2026-09-08）

在「融资的投资方」目录新增第 12 家/人档案 **Llama Ventures**（同步上线 Investor Atlas，双向实施）：

- **为什么入档**：用户在 Visko AI 融资报道中注意到该机构（US$10M Pre-Seed 领投方），随后在 `funding-investors` 请求创建其档案页面，并选择了「双向实施」方案。
- **档案内容**：`investors/llamaVentures.ts` + 本地 `llama-ventures.md`。含 2024 年成立（Sunnyvale, CA）、创始人 Jack Feng（WandouLabs 联创 / iHealth CEO）与 Herman Zhou（易到用车创始人）；US$300M+ 直投基金 + US$600M+ FoF；典型支票 US$500K–5M；**官网披露的组合公司 61 家全部转录**，按官网 7 个赛道分类（Models & Research / AI Infrastructure / Enterprise Applications / Consumer & Media / Healthcare & Life Sciences / Education / Robotics & Hardware），每家含官网简介与官网链接，来源 URL 可逐个溯源。
- **数据来源**：Llama Ventures 官网（llamaventures.vc portfolio 页结构化披露），非二手聚合。
- **logo 资产**：新增 `public/logos/llama-mark.png`（官网图标）、`llama-lockup.png` 及 61 张组合公司官方 logo（`llamaLogos.ts` 索引），全部下载自该公司官网。
- **注册**：`profiles.ts` 导入并加入 `investorProfiles`，Investor Atlas 列表/详情页、sitemap 自动包含 `/investors/llama-ventures`。
- **同步状态**：TS 与 md 公司数一致（61/61）；typecheck 通过。

## 扩充 AI-only 专项基金档案 ×5（2026-09-08）

用户问「还有没有其他像 Llama 一样只投资 AI 的 VC」，据此在 Investor Atlas 补入 **5 家 100% AI 专项（AI-only）基金**——此前站内 12 家中无一家是纯 AI mandate 机构，此批恰好补上这一层，并新增欧洲/加拿大地理覆盖。全部经 5 个调研 subagent 并行转录官网数据（宁缺毋滥、零虚构），双向实施同步上线：

| 档案 | 机构 | 组合转录 | 亮点 |
| --- | --- | --- | --- |
| `gradient.ts` / `gradient.md` | Gradient（2017 谷歌孵化，2025-10 独立，Fund V $220M，~$1.2B AUM） | 16 家（官网 Featured 视图） | 500+ AI founders；Lambda/Writer/Oura/Krea |
| `conviction.ts` / `conviction.md` | Conviction（Sarah Guo，Fund I $101M→II $230M） | 19 家 | Harvey/OpenEvidence/Sierra 等 software 3.0 |
| `aixVentures.ts` / `aix-ventures.md` | AIX Ventures（研究者创立，Fund II $202M） | **73 家**（=官网全量） | Perplexity/Hugging Face/Weights & Biases |
| `airStreetCapital.ts` / `air-street-capital.md` | Air Street Capital（Benaich solo GP，Fund III $232M 欧洲最大） | **66 家**（Epoch I-III + 天使期 4 组） | State of AI Report；Synthesia/BFL/Poolside |
| `radicalVentures.ts` / `radical-ventures.md` | Radical Ventures（多伦多，~US$2.4B AUM 全球最大 AI-dedicated） | **59 家**（The Vanguard 全量） | Cohere/Waabi/Sanctuary；Geoffrey Hinton 任 LP/advisor |

- **logo 资产**：新增 5 个 mark + 213 张组合 logo（总计 218 引用全部落地 `public/logos/`，来自各公司官网）；个别因官网停用/网络不可达无 logo 的公司按站点约定显示灰框（如 Air Street 12 家被并购遗留项、Conviction 3 家网络受限域名）。每家 logos 独立索引文件（`gradientLogos.ts` 等）。
- **一致性**：5 份 md 与 TS 公司数逐家核对一致（16/16、19/19、73/73、66/66、59/59）；`_index.md` 12→17；typecheck 通过。
- **口径注明**：Radical AUM 公开报道差异大（Bloomberg ~US$1.8B vs CPP >US$2.5B），档案取 ~US$2.4B 并注明两口径；Air Street 的 pre-fund 天使投资（Stripe/Niantic 等）按官网原样入档并单列一组。

## 新增投资方档案：Menlo Ventures（2026-09-08）

用户此前在 Lovable C 轮（US$400M / US$13.3B）中确认 Menlo Ventures 为领投方后要求「把 Menlo Ventures 纳入 Investor Atlas」。Menlo 官网组合实测 **245 家**（`menlovc.com/portfolio/`，官方 9 个 Focus 标签互斥核对），与预设"已有 logo 名单"交集极小——仅 Anthropic/Lovable/Suno/OpenEvidence/Wispr Flow/Pinecone/Uber 7 家真正在站，Mistral/Cerebras/Harvey/Cursor 等 24 家**并未**出现在 Menlo 官网（宁缺毋滥，不入档）。建档执行：

- **档案**：`investors/profiles/menlo-ventures.json` + 本地 `menlo-ventures.md`。机构事实与投资逻辑经调研 subagent 交叉核实（Newcomer/Bloomberg/TechCrunch/官网），组合转录 subagent 实测逐家核验（logoUrl HTTP 200）后转录。
- **组合**：AI portfolio 25 家（前沿模型 Ndea/Axiom → AI 基建 Fireworks/Modal/Neon/Pinecone/OpenRouter → 应用层 Lovable/Suno/Wispr/OpenEvidence/Chai Discovery…）+ Beyond AI 5 家（Uber/Roku/Warby Parker/Siri/Gilead，50 年历史语境）；收购标注 Graphite→Cursor、Neon→Databricks、Siri→Apple、Astrix→Cisco。Siri 无独立官网故 logo 取自 Menlo 站内资源。
- **logo（复用优先）**：Anthropic/Lovable/Suno/OpenEvidence/Wispr Flow/Pinecone/Ndea/Prime Intellect/Slingshot/Skild/Recursion/Uber 12 家直接 resolve 共享 canonical 索引（`src/data/logos.ts`）**零下载复用**；其余 17 家新下载（官方公司站图标直连），Astrix/Roku 官网图标不可达按约定灰框。Menlo 自身 mark `menlo-mark.png` 前阶段已就位。新增条目已回写 canonical 索引（412→429）。
- **注册**：`profiles.ts` 加入 → Investor Atlas/sitemap 自动含 `/investors/menlo-ventures`。
- **一致性**：md 与 JSON 公司数一致（30/30）；`_index.md` 17→18；validate:content + typecheck + build（31 页 SSG）全绿。

> 注：本档案为当日 Lovable B/C 轮 Menlo 领投事实的延伸建档，非官方背书口径。

## 新增投资方档案 ×4：Lightspeed / Index / General Catalyst / Eric Schmidt（2026-09-09）

承接 Mistral 历史投资人梳理：用户拟为 Mistral 的 4 位重要历史投资方（**Lightspeed Venture Partners / Index Ventures / General Catalyst / Eric Schmidt**；Elad Gil 已有档案故跳过）构建 Investor Atlas 页面，先调研 AI 出手密度后全部建档。此前 Atlas 以 AI-only/专项机构与个人天使为主，此批补齐**通用多阶段大基金梯队**与**顶级个人**两层：

| 档案 | 类型 | 定位一句话 | 组合转录 |
| --- | --- | --- | --- |
| `lightspeed-venture-partners.md` | 机构 | 165 家 AI-native / $5.5B+ 累计，领投 Anthropic $3.5B E 轮，Mistral seed 领投全勤 | AI 12 家 + 旗舰 legacy 5 家 |
| `index-ventures.md` | 机构 | 跨大西洋旗舰，Mistral 首张支票起全勤，Scale AI 五轮 + Anthropic | AI 13 家 + legacy 6 家 |
| `general-catalyst.md` | 机构 | 医疗起家通用平台，Mistral B 轮领投 + Anthropic 2025 进入 + River AI $1.1B 领投（open-weight 叙事） | AI 10 家 + legacy 6 家 |
| `eric-schmidt.md` | 个人天使 | Hillspire 家族办公室 2019 起 22 家 AI 私企（2022 年 75%+ 出手），Anthropic A 轮进入 | AI 14 家 + 早期 3 项 |

- **口径注记**：GC 官方为通用平台基金，档案定位「healthcare 起家 generalist + AI 独立 thesis（Creation 策略 $1.5B / River AI 主权叙事）」，避免写成 AI-only；AUM 引双口径（Wikipedia US$43B+ Dec 2024 / Form ADV US$45.5B Jul 2026）。Lightspeed AUM Wikipedia US$50B vs 官方 >US$40B，取保守口径并注。Index 不披露官方 AUM，引 GP Intel €11.7B / Dealroom US$13B 区间。
- **组合原则**：宁缺毋滥——仅收录官网/公司融资公告/Bloomberg/CNBC 等可溯源公司；Schmidt 无统一公开组合页，金额/估值均为对应融资轮公开数字，备注已逐条标注。
- **与 Mistral 的关联**：4 家均为 Mistral 历史投资方（Lightspeed seed 领投全勤 / Index seed 起全勤 / GC B 轮领投 / Schmidt seed 个人股东），构成「Mistral 投资方全景」档案侧的完整闭环。

## 新增产品融资时间线：Lovable（2026-09-08）

用户此前询问「是否有单产品的融资 timeline 页面（类似 /products 详情页）」，确认现状缺失后本次以 **Lovable** 为首档产品落地全新 section **Product Histories**（`/products`），从快照级（Leaderboard）升级到**逐轮级**数据模型：

- **站点**：新增 `src/data/products/`（schema.ts + lovable.json + 薄 loader，延续 JSON 化模式）；新路由 `app/products/[slug]/page.tsx`（逐轮时间线：金额/估值/领投/参投/来源，附叙事章节）+ `app/products/page.tsx` 索引；sitemap 增 `/products` 与 `/products/lovable`；nav + 首页 CTA 加入口。
- **数据（全部经官方 blog + TechCrunch/Reuters/Forbes/Bloomberg 核实）**：Pre-Seed US$7.5M（2024-10-07，公开库口径）→ Seed US$15M（2025-02-25，Creandum 领投）→ Series A US$200M @ US$1.8B（2025-07-17，Accel 领投，欧洲当时最大 A 轮）→ Series B US$330M @ US$6.6B（2025-12-18，CapitalG + Menlo(Anthology) 联合领投）→ **Series C US$400M @ US$13.3B（2026-08-12，Menlo Ventures 领投 + EQT Scaleup Europe Fund 联合领投）**，累计 ~US$953M。
- **与用户提供材料的口径差异**：用户材料未给 A 轮日期（实为 2025-07-17）与 B/C 轮领投方（B=CapitalG+Menlo；C=Menlo+EQT）；C 轮日期补齐（2026-08-12）；ARR 时点细化为 Feb 2026 $400M → Jun 2026 ~$500M → Aug tracking $600M。
- **logo**：自 `public/logos/aixVentures-lovable.png`（AIX 组合官网下载）复制为 `public/logos/lovable.png`（485×256）。
- **质量闸门**：`validate-content.mts` 扩展 products JSON 校验（schema/logo 存在/rounds 按日期升序/slug 唯一）；`npm run validate:content` + typecheck + build（30 页 SSG，含 `/products/lovable`）全部通过。

> 档案仓同步：本 README 文件清单新增 `product-histories/`（Lovable 首档 + `_index.md`），与站点 `/products/lovable` 双向一致。

## 新增产品融资时间线：Mistral AI（2026-09-09）

承接 D 轮调研（见对话记录，2026-09-08 宣布 €3B / >€21B / 三星领投），以 **Mistral AI** 为 Product Histories 第二档在记录仓建档（`product-histories/mistral.md`，仿 lovable.md 结构），缺项经网络逐轮补齐并一线信源交叉核实：

- **完整融资链（5 轮股权 + 背景债务）**：Seed €105M（2023-06-13，Lightspeed 领投，@€240M）→ Series A €385M（2023-12-11，a16z 领投，@~US$2B）→ Series B €600M（2024-06-11，General Catalyst 领投，@€5.8B；含 €132M 债务；**三星经其风投 Samsung Venture Investment 首次参投**）→ Series C €1.7B（2025-09-09，ASML 领投 €1.3B / ~11% 成最大股东，@€11.7B）→ **Series D €3B（2026-09-08，Samsung Electronics 领投，@>€21B）**。累计 ~€5.8B（≈US$6.6B）。
- **叙事章节**：从 Meta/DeepMind 到欧洲 AI 旗手 → 开放权重 + 主权 AI 全栈 → 产业冠军（ASML→三星）作战略股东 → compute-landlord 转型（44MW 巴黎数据中心、2030 年 1GW、ECU 预售、2026-07 微软角色反转）→ 市场与竞争（OpenAI/Anthropic ~35-40× 估值对比、Cohere、主权悖论争议）。
- **口径注记**：三星 D 轮投资额 ~€1B 系媒体估计（FT 源），官方未披露；微软 €15M 可转债（2024-02）不构成独立股权轮，已在叙事中交代；微软未参投 C/D 轮股权。
- **记录仓先行**：本档为本地归档，站点侧待部署仓新增 `src/data/products/mistral.json` + `/products/mistral` 路由（schema 同 lovable）后双向一致。

## 新增产品融资时间线 ×4：巨形种子轮 Labs（2026-09-09）

用户调研「融资额度最高」「种子轮最快/最大」后,为四个「创始人光环巨型种子轮」AI lab 建档(Product Histories,经 4 个调研 subagent 并行联网核实、宁缺毋滥):

| 档案 | 定位 | 轮次 |
| --- | --- | --- |
| `thinking-machines-lab.md` | Mira Murati(前 OpenAI CTO)的 collaborative general intelligence lab | Seed US$2B @ US$12B(2025-07-15,史上最大首轮);$50B 轮 2026-01 破裂(单列 Note);2026-09 在谈 $5–6B @ ≥$40B pre(未 close,不记为融资) |
| `ineffable-intelligence.md` | David Silver(AlphaGo 之父)的 experience-based "superlearner" lab | Seed US$1.1B @ ≈US$5.1B post(2026-04-27,**欧洲史上最大种子轮**;两档结构单源标注) |
| `ami-labs.md` | Yann LeCun 的 JEPA 世界模型 lab | Seed ~US$1.03B @ US$3.5B pre(2026-03-09,欧洲最大种子轮之一;post ≈US$4.5B 推算无官方) |
| `world-labs.md` | Fei-Fei Li 的 spatial intelligence / 世界模型公司 | Seed US$230M(2024-09,两 tranche)@ >US$1B reported;后续轮 US$1B(2026-02-18,Autodesk $200M 锚定)@ ~US$5B reported |

- **口径纪律**:在谈/破裂轮一律不写入 rounds[](Thinking Machines $50B/$40B 单列 Note 并标注 in-talks);官方未确认估值标 reported(World Labs 两轮);pre/post 口径逐条注明(AMI pre $3.5B 官方);单源申报文件口径(如 Ineffable 两档结构)如实标注不入主表。
- **共同主题**(可作未来 Leaderboard/列表内容):2024-2026「顶级研究者一离开大厂就被天价抢投」的巨型种子轮时代——从 Mistral(€105M/1 个月,2023)到 Thinking Machines($2B/5 个月,2025)到 Ineffable/AMI(~$1.1B,2026),金额三年膨胀近 20 倍。

## Product Histories 扩至 8 家：OpenAI / Anthropic / xAI / Scale AI / SSI / Zhipu（2026-09-09）

承接「融资最高的 AI 公司」调研，将 6 家头部融资方补档为逐轮时间线：

| slug | 赛道 | 累计/最大轮 | 时间线要点 |
| --- | --- | --- | --- |
| `openai` | Frontier models | ~US$142B 保守口径 / US$122B @ US$852B (2026-03) | 2015 创始承诺 → 2019 MSFT US$1B → 2023 US$10B → 2024 US$6.6B @157B → 2025 US$40B @300B → 2026 史上最大轮 |
| `anthropic` | Frontier AI safety | ~US$118B / US$65B Series H @ US$965B (2026-05) | 2021 A US$124M → FTX/Alameda B → Google/Amazon 双云承诺 → E/F/G/H 十五个月 16x 估值 |
| `xai` | Frontier + infra | ~US$37B+ / US$20B E @ US$230B (2026-01) | 2023 seed → B/C (24→50B) → X 收购 (80B) → 2025 D/E → **2026-02 SpaceX US$250B 收购** |
| `scale-ai` | AI data infra | ~US$15.9B / US$14.3B Meta (2025-06, 49% 无投票权) | 2016 YC seed → Accel A/F → Meta ~49% @ US$29B；客户流失事件 |
| `safe-superintelligence` | SSI research | ~US$8B / US$5B Nvidia (2026-07) | 2024-09 US$1B @5B → 2025-04 US$2B @32B (Greenoaks) → Nvidia 战略轮；零产品零收入 |
| `zhipu` | GLM + 政企 MaaS | 上市前 RMB 8.3B / 2026-07 配售 US$4B @~US$64B | 清华系 2019 → 8 轮 50+ 股东 → **2026-01-08 港股 2513.HK「全球大模型第一股」** → 配售 + A 股科创板拟上市 |

- **口径注记**：累计金额口径差已逐档注明（OpenAI US$142B 保守 vs 第三方 US$180–197B；Anthropic Series H「US$65B vs ~US$8B 新增」；xAI Series D 为 Reported；Zhipu 早期为人民币口径、配售为 Reported）。
- **记录仓先行**：6 档 md 已建档，待部署仓落地 6 份 `products/*.json` + `/products/{slug}` 路由后与站点双向一致。

## 新增 Cognition（Devin 母公司）双档案：Leaderboard 快照 + Product Histories（2026-09-10）

承接用户问询「Devin 母公司 Cognition 完成 $2B 融资、估值 $48B 是否有页面」：此前站内无 Cognition 独立档案（仅作为组合公司出现在 Conviction/Menlo/Llama/YC 等档案），本次双向补齐：

- **Series E（2026-09-08，Reuters/TechCrunch 确认）**：US$2B @ US$48B，**a16z + Accel 领投（新进）**，Founders Fund/General Catalyst/Avenir 返回，30+ 家参投（Benchmark/Bessemer/Kleiner/Greylock/Lightspeed/Nvidia 等）。估值较 5 月 Series D（US$26B）四个月近翻倍；ARR US$492M → ~US$900M。
- **完整融资链（6 轮）**：Seed US$21M（2024-03-12，Founders Fund，与 Devin 发布同日）→ Series A ~US$175M @~US$2B（2024-04）→ Series B 金额未披露 @~US$4B（2025-03，Lux + 8VC）→ Series C US$400M+ @US$10.2B（2025-09-08，Founders Fund）→ Series D US$1B+ @US$26B（2026-05-27，Lux/GC/8VC）→ Series E US$2B @US$48B（2026-09-08）。估值弧线 ~$350M→$48B。
- **关键事件**：2025-07 收购 Windsurf IDE（带 ~US$82M ARR；Google 并行 ~$2.4B 挖走 CEO 等 40 人）；2026-07 再收购 TierZero、Interaction/Poke；客户含 Mercedes-Benz/NASA JPL/Goldman Sachs/Citi/美国陆海军。
- **落地**：`funded-products/cognition.md`（Leaderboard 25 家，累计 US$3.60B 披露主轮口径，插在 Mistral 与 MiniMax 之间）+ `product-histories/cognition.md`（14→15 家）；部署仓 `fundingLeaderboard.json` 25 条 + `products/cognition.json` + 注册，logo 复用 canonical `conviction-cognition.png`。commit `469a659`。
- **口径注记**：Series B 金额未披露故累计融资按披露主轮计 ~US$3.6B；Series A/B 金额估值为报道口径（公司未单独公告）；累计融资字段已注明。

## 首页复活：Latest Rounds 真实数据 + 滚动跑马灯（2026-09-10）

首页此前因 `fundingRounds.ts` 置空(9/7 移除虚构演示轮)长期停留在空态引导页。本次以**真实近期轮次**回填并新增滚动融资条：

- **数据**：`src/data/fundingRounds.ts` 回填 10 条真实可溯源事件(2026-07-01～09-09：Mistral €3B D / Harvey US$550M / Databricks US$5B / SSI-Nvidia US$5B / Moonshot US$3.5B / MiniMax US$2.05B / Zhipu 配售 US$4B / Lovable US$400M / Unitree IPO / Together US$800M)，每条带 `logo/slug/sourceUrl`。维护约定：滚动新增、>12 条裁最旧、宁少勿假。
- **新组件 `WeeklyTicker`**：header 正下方的「Latest rounds」反白跑马灯——纯 CSS 无缝循环（双份渲染 translateX(-50%)）、hover 暂停、`prefers-reduced-motion` 降级为横向滚动；每条链到对应 `/products/{slug}`。
- **首页区块全部复活**：`LeadStory`（最新大轮）+ `StatStrip`（批次统计）+ `FundingTable`（Latest Funding Rounds）因数据到位自动恢复渲染；空态引导页保留作兜底。
- **文案校准**：因数据为「近期批次」滚动窗口（非严格单周），将组件内 "this week / Updated daily" 措辞改为 "recent batch / Updated as rounds are recorded"，避免口径失真。
- 本地 build + `next start` 渲染验证通过；部署仓 commit `4ffd383` 上线。

## SEO/分析就位（2026-09-07）

- **GSC**：网域属性 `frontierrounds.com`（Domain 验证，DNS TXT）已验证通过；sitemap.xml 含 14 个 URL（/、/leaderboard、/investors + 11 investor 档案），逐一 curl 全部 200。
- **GA4**：属性 ID `G-YCMXNXZENN`，经 `@next/third-parties/google` `<GoogleAnalytics>` 接入根布局（`src/lib/site.ts` 暴露 `GA_MEASUREMENT_ID`，可用 `NEXT_PUBLIC_GA_ID` 覆盖）。commit `8facb9c` 部署；线上 HTML 含 gtag.js，端点 200。
- **踩坑**：`package-lock.json` 早期曾被跟踪，`.gitignore` 对已跟踪文件无效——`git add -A` 会重新带入；需 `git rm --cached`（commit `65fa848`）后才会被忽略。CI 用 `npm install` 不依赖 lock，故两轮部署均成功。

## 品牌系统落地：替换 Lovable favicon/icon/OG（2026-09-07）

- **设计源**（本记录仓 `branding/`，已定稿）：基于 Apineed+GPT-Image v3 反白小样重绘的**黑白两色** SVG——
  - `fr-icon.svg`：黑圆角方块 + 白色开环（缺口右上）+ 内节点弧链 + 缺口外探点（深底/图标用）
  - `fr-icon-mono.svg`：同形，透明底纯黑（浅底/单色/可改色）
  - `fr-wordmark.svg`：品牌名 "Frontier Rounds"，Instrument Serif Regular **轮廓化 path**（不依赖字体安装）
- **过程文件已清理**（2026-09-08）：branding-samples 概念小样 PNG、APINEED 生图/生成/派生脚本、OG 模板、字体源均已删除，只保留最终定稿 SVG。未来若需调整 logo 形状，直接编辑 `fr-icon.svg` 即可（几何结构见 commit 历史）。
- **站点接入**（deploy 仓 commit `f8755b1`，已 CI 上线验收）：
  - `app/favicon.ico`（16/32/48 多尺寸**极简标**：仅开环+缺口+外探点，小尺寸可辨）+ `app/icon.png`(512) + `app/apple-icon.png`(180) —— Next 约定式自动注入 `<link rel=icon/apple-touch-icon>`
  - `app/manifest.ts`：PWA manifest（paper/ink 主题色，192+512 icon）；`public/icons/icon-192.png`
  - `public/og/og-default.png`（1200×630，Wordmark+图标+tagline 组合）；`layout.tsx` 补 `openGraph.images` + `twitter:image`（指向 `OG_IMAGE`）
  - `public/favicon.ico`（Lovable 旧图）已删，避免与 `app/favicon.ico` 双源
  - **验收**：构建产物含 `/icon.png`、`/apple-icon.png`、`/manifest.webmanifest` 路由；线上 `<head>` 已含全部 icon/manifest/og:image 标签，`/favicon.ico`、`/icon.png`、`/og/og-default.png` 等端点全部 200，无 lovable 残留
- **又一次踩坑**：`.gitignore` 中 `/package-lock.json   # 注释` 的**行内注释无效**——gitignore 仅行首 `#` 为注释，行内 `#` 视为模式一部分，整条规则失效（`git check-ignore` 静默不匹配）。已改为独立注释行。

### www → 裸域 301（防重复内容，2026-09-07 已生效）

四象限 URL 全部收敛到 canonical `https://frontierrounds.com`（路径保留）：

| 入口 | 行为 |
|---|---|
| `https://www.*` | 301 → `https://frontierrounds.com/...`（1 hop） |
| `http://www.*` | 301 → https://www → 301 → 裸域（2 hops） |
| `http://frontierrounds.com` | 301 → https 裸域（1 hop） |
| `https://frontierrounds.com` | 直接 200（0 hop，canonical） |

**实现方式（重要踩坑）**：域名是绑定在 Worker 上的 Custom Domain，流量判定为 Worker route，**Page Rules 的 Forwarding URL 会被 CF 静默忽略**（官方文档确认）→ 必须用 **Redirect Rules**（新版规则引擎，`http_request_dynamic_redirect` 阶段，先于 Worker 执行）。CF 自带模板 **"Redirect from WWW to root"**：`https://www.*` → `https://${1}`（`*` 捕获 `www.` 后的主机名+路径，天然保留路径）301；http 变体同理另建一条 `http://www.*` → `https://${1}`。

## 部署链路备忘（下次更新发版）

```
1. 本地改数据/内容 → commit
2. git push origin main（走 SSH remote：git@github.com:kostja94/frontier-rounds.git）
   ※ HTTPS 到 github.com:443 在本网络不可达，务必用 SSH
3. Actions workflow "Deploy Frontier Rounds" 自动：npm install → opennextjs-cloudflare build → wrangler deploy
4. 等 run 绿（约 1.5–2 min）：gh run watch $(gh run list --repo kostja94/frontier-rounds -L1 --json databaseId -q '.[0].databaseId') --repo kostja94/frontier-rounds --exit-status
```

> 经验教训（踩坑记录）：
> - Windows 上 OpenNext build 不可用（官方不支持，缺 edge config 产物）；必须在 ubuntu CI 构建
> - 勿把 Windows npm 生成的 package-lock.json 入库（@emnapi 等平台依赖导致 Linux `npm ci` 失败）；CI 用 `npm install`
> - wrangler 4.129 已弃用顶层 `custom_domains`，绑自定义域要用 `routes: [{pattern, custom_domain:true, zone_name}]`
> - OpenNext + Next 16 SSG 动态页 404：必须 `dynamicParams=false` + open-next.config.ts 用 `staticAssetsIncrementalCache`

## 关键结论速览

1. **技术选型**：Next.js App Router（React 19 + Tailwind CSS v4，保留原 editorial 设计系统）+ 数据层 TS 硬编码迁移。
2. **部署选型**：Cloudflare Workers + `@opennextjs/cloudflare`（OpenNext，成熟稳定）；`vinext` 为官方实验性新路线，留作备选。
3. **图片资产**：`src/assets/*.png.asset.json` 仅是 Lovable 云端指针，实体图在
   `https://id-preview--1e49e127-78ec-480f-9a11-53fbb3437103.lovable.app/__l5e/assets-v1/{asset_id}/{原文件名}`
   ——已实测可访问，需脚本回填到 `public/logos`（脚本见方案 §A4）。
4. **品牌与 SEO 遗留**：现文案品牌为 "AI Capital"；leaderboard 页 canonical 残留 Lovable preview URL（`id-preview--….lovable.app/leaderboard`）；无 sitemap。均须在重构中替换/补齐。
5. **双仓结构**：源码仓 `E:\自有部署项目\frontierrounds`（Next + CF 配置）；策略/记录仓 `E:\clients\frontierrounds`（本目录）。

---

*本目录为策略记录仓，不混入 Next 应用代码。最后更新：2026-09-09（Product Histories 扩至 8 家 + Investor Atlas 4 家；Mistral 上线）*
