# 2mv — 增长策略

> 本策略基于 **Google Keyword Planner 真实数据**（2026-07-14 导出 CSV）+ **Reddit 用户语言调研**（r/SaaS、r/digital_marketing 等真实需求帖）+ **Features 版块规划**。与 [keywords](./2mv-keywords.md) 意图分类、[features](./2mv-features.md) 产品能力、[competitors](./2mv-competitors.md) 差异化对齐。

---

## 0. 数据口径与决策原则

| 项 | 内容 |
|----|------|
| 数据来源 | Google Keyword Planner（2026-07-14 导出，含月均搜索量 / 3 个月变化 / 年同比 / 竞争度 / 首页出价） |
| 用户语言来源 | Reddit 真实需求帖（r/SaaS、r/digital_marketing 等，作为长尾词与 FAQ 语料） |
| 覆盖词量 | 2,600+ 关键词，15 大词根，累计月搜索量约 37 万 |
| 页面决策原则 | 搜索量足够大 + Cluster 完整 + 搜索意图独立 → 独立建 SEO Landing Page；搜索量大但意图不纯的词**先不抢** |
| 层级原则 | `Research Lab → Feature Hub → 高价值 Keyword Landing Page`；Landing Page 仍归属于某个 Feature，不包装成独立产品 |

---

## 1. 词根全景（真实数据）

| # | 词根 / 类别 | 词数 | 月搜总量 | 建议主页面 | 阶段决策 |
|---|------------|------|---------|-----------|---------|
| 1 | **Social Media Analytics / Analysis** | 331 | 79,280 | `/research` | **Phase 1 核心词池**（P0） |
| 2 | **AI Social Media Tools / Broad** | 60 | 136,960 | `/tools` | Phase 1 承接 Tools Hub 入口；生成类暂缓 |
| 3 | **Platform Analytics** | 228 | 78,540 | 暂缓平台页 | Phase 2/3 平台页后置 |
| 4 | **Sentiment / Listening / Monitoring** | 79 | 19,960 | `/research` comment signals 模块 | 暂缓，不独立建页 |
| 5 | **竞品品牌词 / 参考不主攻** | 75 | 12,630 | 不作为目标页面 | 仅记录竞品词 |
| 6 | **Reporting / Dashboard** | 70 | 10,370 | `/research` Sample Output 模块 | 暂缓，不建独立页 |
| 7 | **Competitor Analysis** | 68 | 6,720 | `/tools/competitor-content-analyzer` + `/research/social-media-competitor-analysis` | Phase 1/1.5：工具页先行，场景页后置 |
| 8 | **Audit / Template** | 7 | 4,710 | `/resources/social-media-audit` | Phase 2 候选（lead magnet） |
| 9 | **偏学术/网络分析/站点统计** | 27 | 3,420 | Exclude | 排除 |
| 10 | **Post Analysis / Content Dimensions** | 27 | 2,580 | `/tools/post-analysis` | Phase 1 候选工具页 |
| 11 | **Benchmark / Report** | 2 | 960 | `/resources/social-media-benchmarks` | Phase 2/3 候选 |
| 12 | **Social Video / Short-form Analytics** | 7 | 940 | `/research` 短视频分析语义 | Watch，不作为独立工具页 |
| 13 | **广告/投放分析** | 15 | 590 | Exclude | 排除（2mv 只做 Organic） |
| 14 | **Tools - Trend / Discovery** | 3 | 430 | `/tools/tiktok-trend-analyzer` | Phase 2 后置 |
| 15 | **Tools - Hook** | 1 | 140 | 待验证 | Watch，不足以独立建页 |

> **核心结论**：2mv 的 SEO 主引擎是 **`/research`（analytics / analysis / research 主词池）**；**`/tools` Hub 必须后置**（等至少 2–3 个可用小工具确认后再上线，避免空壳 Hub）；平台页、舆情、报告类均不进入 Phase 1。

---

## 2. 页面规划与阶段决策

| 建议页面 | 词数 | 月搜总量 | 阶段 | 决策 |
|---------|------|---------|------|------|
| **`/research`** | 331 | 79,280 | **Phase 1** | **建设：Research 核心工具入口**（系统级 Research/Analytics，不等同普通 dashboard） |
| **`/research/social-media-competitor-analysis`** | 18 | 3,130 | **Phase 1/1.5** | **提前建设：Research 第一个下级页**（意图明确，Rival IQ / Social Status 等竞品有真实页面支撑） |
| `/tools`（Tools Hub） | 52 | 129,770 | Phase 1.5/2 | 后置；等工具页模板跑通后再上线 |
| `/tools/competitor-content-analyzer` | 68 | 6,720 | Phase 1.5/2 | 工具意图先行承接，复用工具页模板 |
| `/tools/post-analysis` | 27 | 2,580 | Phase 1/1.5 | 候选工具页（hashtag/engagement/caption 是否合并待产品确认） |
| `/research/social-media-audit` | 待补充 | 待补充 | Phase 2 | 候选（需补关键词与竞品依据） |
| `/resources/social-media-audit` | 7 | 4,710 | Phase 2 | 资源页 / lead magnet |
| `/resources/social-media-benchmarks` | 2 | 960 | Phase 2/3 | 候选，依赖数据/报告资产 |
| `/research/tiktok-analytics` | 27 | 45,510 | Phase 2/3 | 平台页后置，先作 `/research` 平台覆盖 |
| `/research/instagram-reels-analytics` | 88 | 15,930 | Phase 2/3 | 平台页后置；统一用 instagram reels analytics 语义 |
| `/research/youtube-shorts-analytics` | 9 | 3,070 | Phase 2/3 | 平台页后置 |
| `/tools/tiktok-trend-analyzer` | 3 | 430 | Phase 2/3 | 趋势类工具后置 |
| Viral Video Analyzer 方向 | 0 | 0 | 观察 | **不作为关键词驱动结论**（无直接数据，仅产品功能候选） |
| Hook Analyzer 方向 | 1 | 140 | 观察 | 仅 1 词月搜 140，不足以支撑独立工具页 |

---

## 3. 各页面关键词落位

### 3.1 Homepage（品牌与服务品类定义）

| 关键词角色 | 关键词 | 月搜量 | 落位 | 说明 |
|-----------|--------|-------|------|------|
| 市场与品牌桥梁词（P0） | short-form video growth | 无明确数据 | 首页整体主题 | 核心语义中心，不强行改写成工具/Agency 标题 |
| 品类限定词（P0） | organic social media growth | 待验证 | 首屏说明/正文 | 明确 Organic 边界，避免被理解为 Paid Social |
| 品牌定位词（P0） | AI-native organic growth service | 无数据 | 品牌声明 | 不按搜索量评价 |
| 市场辅助词（P1） | short-form video marketing | 880 | Meta Description/正文 | 连接存量市场，近期趋势下降谨慎使用 |
| 策略辅助词（P1） | social media content strategy | 390 | 流程/策略模块 | 解释「不只是制作，还包括研究与策略」 |
| 宽泛主题语义（P2） | short form content / short form video / social media content | 1,300–1,900 | 正文自然出现 | 只建立主题相关性，不进入 Meta/H1 |
| 市场比较词（P2） | short form video agency | 40 | 比较内容/定位说明 | 避免被定义为传统视频制作 Agency |
| **排除** | seo ai (8,100)、ai seo optimization (720)、ai seo software (390) 等 AI/SEO 扩展词 | — | 不使用 | 与短视频自然增长业务不匹配 |

### 3.2 Research（主要 SEO 获客页）

| 关键词角色 | 关键词 | 月搜量 | 落位 |
|-----------|--------|-------|------|
| **主市场关键词（P0）** | **viral video finder** | 70（3个月 +1.33） | Title/H1 附近、首屏说明 |
| 品类定义词（P0） | viral video research / viral content research | 10 / 无数据 | Meta Description、产品解释 |
| 重要商业辅助词（P0） | social media competitor analysis | 390 | Competitor Research 模块/H2/FAQ |
| 重要商业辅助词（P0） | social media competitor analysis tools | 210（3个月 +1.43） | Competitor Research 功能模块 |
| 核心词池（P0） | social analytics tool / social media analytics tool / social network analytics tools | 8,100 | 整页语义覆盖（analytics + research + organic growth） |
| Reddit 原生长尾（P1） | find viral videos in your niche / find viral videos | 30 | 首屏说明/FAQ |
| 分析能力辅助词（P1） | viral video analysis | 10 | 分析模块/H2 |
| 平台趋势辅助词（P2） | TikTok trend finder | 20 | 平台与趋势模块（Reels/Shorts 同等呈现） |
| 问题型内容词（P2） | how to find viral videos 等 | 10–30 | Blog（未来文章）+ Research FAQ |
| **排除** | sprout/hootsuite 竞品品牌词、viral content sites、facebook 平台词、paid social 词 | — | 不进入 Research 页面规划 |

> **防内耗边界**：`viral video finder` 等产品型关键词由 Research 独占；Blog 只做问题型文章并内链至 Research；竞品分析长尾统一收敛到 Research，不另起页面。

### 3.3 Blog（信息型内容入口）

| 关键词角色 | 关键词 | 优先级 |
|-----------|--------|-------|
| 品牌导航词 | 2mv Blog | P0 |
| 主题集群词 | short-form content strategy / social media content strategy | P1 |
| 问题型长尾（首批内容） | how to find viral videos | P1 |

### 3.4 转化/法务页

- **Book a Demo**：`2mv demo`（P0 品牌转化词）、`organic growth consultation`（P2）——不承担非品牌获客
- **Contact / Privacy Policy / Terms of Use**：仅品牌导航与法律表达，不参与关键词规划

---

## 4. Features 版块规划（Research 产品化）

**三层架构**：`Research Lab → Feature Hub → 高价值 Keyword Landing Page`

- `/research` 承接 Research 产品本身和泛类目大词
- **Feature Hub 收敛为 4 个核心**：

| Feature Hub | 对应能力 |
|-------------|---------|
| **Content Discovery** | 找爆款内容与信号（对应 Market Signals / Watch） |
| **Tracking Center** | 追踪竞品与对标账号（对应 Target Tracking） |
| **Profile & Channel Analysis** | 账号/频道维度分析 |
| **Viral Video Analysis** | 逐帧解码与模式聚类（对应 Viral Breakdown / Content Patterns） |

- 在 4 个 Feature 下，对真正大的 Keyword Cluster 单独建 SEO Landing Page（仍属于某个 Feature，不包装成新独立产品）
- **Keyword Landing Page 拆分判断（6 因素）**：搜索量足够大、Cluster 完整、搜索意图独立（结合关键词表数据逐条验证）
- **上线计划**：Phase 1（P0）建完整 4 个 Feature Hub + 上线最确定的第一批 SEO Landing Page；Phase 2（P1）第二批；其余 Hold

---

## 5. Blog & Tools 内容架构

### 5.1 Blog Tag 分类

| 分类 | Tag |
|------|-----|
| **平台类** | YouTube Shorts、TikTok、Instagram Reels、Cross-Platform |
| **内容与研究类** | Video Ideas、Hooks、Outliers、Content Patterns、Viral Research、Competitor Research、Content Strategy、Content Creation、Organic Growth |
| **行业洞察类** | Expert Opinion、Interview、Podcast、Industry Events、Platform Updates、Creator Economy、AI Content Tools |

**使用规则**：每篇 2–4 个 Tag；初期 Tag 归档页统一 `noindex, follow`。

### 5.2 Tools Hub 四阶段

| 阶段 | 用户价值 |
|------|---------|
| **Discover** | Find breakout content and signals worth studying |
| **Analyze** | Understand why content works and where it can improve |
| **Create** | Turn research and ideas into original short-form content |
| **Track & Optimize** | Measure results and improve the next content cycle |

### 5.3 目标 URL 架构

```
/
├── research/
│   └── social-media-competitor-analysis/   （Phase 1 首个下级页）
├── tools/
│   ├── competitor-content-analyzer/
│   ├── post-analysis/           （候选）
│   ├── outlier-finder/          （规划）
│   ├── hook-analyzer/           （观察）
│   ├── video-idea-generator/    （规划）
│   └── 具体工具页/
├── insights/
│   ├── guides/
│   ├── trending/
│   ├── industry-insights/
│   ├── research-reports/
│   ├── how-to-find-viral-content-ideas/
│   └── 具体文章页/
└── resources/
    ├── social-media-audit/       （Phase 2 候选）
    └── social-media-benchmarks/  （Phase 2/3 候选）
```

---

## 6. 增长渠道规划

| 渠道方向 | 目标 Persona | 内容类型 | 优先级 | 承接页 |
|----------|-------------|---------|--------|--------|
| 内容 SEO（`/research` 词池 + Blog） | 增长/社媒负责人、创始人 | 「如何找爆款」系列、竞品分析、analytics 词池落地 | **P0** | `/research`、`/research/social-media-competitor-analysis`、`/insights` |
| 工具页 SEO（Tools Hub） | 创作者、代理机构 | Competitor Analyzer、Post Analyzer | P1.5/2 | `/tools/*` |
| GEO / AI 检索（llms.txt + schema） | 用 AI 检索工具的人群 | llms.txt、结构化数据、产品知识库 | P0 | 全站 |
| 自有内容示范（三平台） | 品牌创始人、创作者 | 用自身引擎跑出的病毒案例 | P1 | `/`、`/research` |
| 创作者/UGC 生态 | 创作者/UGC、代理机构 | niche 解码内容、教程、免费额度钩子 | P1 | `/insights` |
| 代理机构合作 | 增长负责人、代理机构 | 白标/API、多账号案例 | P2 | 复用 Research Lab 底座 |

---

## 7. 战役节奏

**短期（0–3 个月）**
- 建设 `/research` 核心词池（analytics / analysis / research 主词），定位为系统级 Research，而非普通 dashboard
- 提前建设 `/research/social-media-competitor-analysis`（Research 第一个下级页，Phase 1 提前）
- 修复 sitemap.xml（当前 500）、发布 llms.txt 与 `SoftwareApplication` schema
- Blog 落地首批问题型内容（`how to find viral videos` 等，内链至 `/research`）

**中期（3–6 个月）**
- `/tools/competitor-content-analyzer` 等工具页模板跑通，再决定是否上线 `/tools` Hub（避免空壳）
- 独立 `/pricing` 页 + `/service` 代运营落地页，打通「研究→试用→代运营」转化漏斗
- 启动三平台自有账号，用自身引擎产出案例，形成「用 2mv 证明 2mv」的增长飞轮

**长期（6–12 个月）**
- 在 4 个 Feature Hub（Content Discovery / Tracking Center / Profile & Channel Analysis / Viral Video Analysis）下，为高价值 Keyword Cluster 独立建 Landing Page
- 平台页（TikTok/Instagram Reels/YouTube Shorts）按 Phase 2/3 规划落地
- 发布年度病毒内容趋势报告，建立品类定义权

---

## 8. 竞品差异化方向

> 基于 [competitors](./2mv-competitors.md) 的 SWOT 差距。

1. **抢占「上游研究层」空白**：竞品（Arcads/Predis）都在抢「生产」，Blaze 在抢「全栈代运营」，唯独「病毒研究/逐帧解码」层 2mv 有最明确的产品化表达——`/research` 词池与 Blog 内容都应反复强化「先研究、再生产」的差异化。关键词表修正也印证：Viral Video Analyzer / Hook Analyzer 因无直接关键词数据，不作为 Phase 1 页面。
2. **「有机」叙事 vs 「付费」叙事**：Superscale/Arcads 主攻付费广告创意，2mv 旗帜鲜明打「有机增长、按结果付费、-60% 广告支出」；对应关键词层面，所有 paid social / 广告投放词（ads insights facebook 等）明确排除。
3. **平台词后置的战略取舍**：TikTok analytics（33,100 月搜）等平台词量大，但 Phase 1 不拆平台页——先在 `/research` 内作平台覆盖，避免与产品主线（跨平台 Research）争夺语义。

---

## 9. 度量指标

| KPI | 说明 | 建议工具 |
|-----|------|---------|
| 有机搜索流量 | `/research`、`/research/social-media-competitor-analysis`、`/insights` 自然流量 | GA4 / Search Console |
| 商业型词排名 | viral video finder、social media competitor analysis、social analytics tool 等 P0 词 | Semrush / Ahrefs |
| 核心词池覆盖 | `/research` 对 analytics 词池（8,100 级主词）的整页语义覆盖效果 | Search Console 查询页 |
| AI 检索提及率 | 品牌是否被 AI 检索工具引用 | 自定义监控 |
| 试用→付费转化 | Research Lab free credits → 订阅 | Stripe / 产品分析 |
| Demo 预约量 | `/book-a-demo` 表单提交 | 表单分析 |
| 自有内容播放量 | 三平台示范内容的增长 | 平台后台 |
| 工具页健康度 | 工具页上线后搜索曝光与转化（决定 Tools Hub 是否上线） | GA4 / Search Console |

---

> 关联：[主文档](./2mv.md) | [keywords](./2mv-keywords.md) | [features](./2mv-features.md) | [competitors](./2mv-competitors.md) | [use-cases](./2mv-use-cases.md) | [site-structure](./2mv-site-structure.md)

*Last updated: 2026-08-14（基于 Keyword Planner 2026-07-14 真实数据重构）*
