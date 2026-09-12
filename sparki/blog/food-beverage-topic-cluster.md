# Sparki Blog — Food & Beverage Topic Cluster（主题簇规划）

> **簇 Hub（主站落地页）**：聚合页 [https://sparki.io/industries](https://sparki.io/industries) + **7 个 Food & Beverage 已上线详情页**（restaurant / cafe / bar / bakery / food-truck / pizza / bubble-tea）
> **簇工作区**：本文件 + 文件夹 `sparki/blog/food-beverage/`（未来文章 Brief/成稿；成稿落部署仓 `E:\客户部署项目\sparki-blog\content\blog\{slug}.md`）
> **调研依据**：web-deep-search-spec v1.4（2026-09-11 多轮检索：七类餐饮业态的视频类型矩阵）+ sparki-blog-article skill（类型路由 / content-graph 62 篇禁抢 / slug-gate / project-config URL 白名单）
> **选题原则（本次用户指定）**：**不考虑竞争度**，只按「搜索量高 + 符合用户意图」筛选；搜索量为定性判断（SERP 抽样），精确量须 SEMrush/Ahrefs 复核后定稿优先级。

---

## 1. Hub 落地页解析（可写依据）

### 1.1 聚合页 `/industries`

`https://sparki.io/industries`（Industry Video Editor）把本地商户按 7 大行业分组，Food & Beverage 是 **B1 餐饮【P0】**，聚合页列出 7 个细分 + Typical videos（store tour / dish showcase / deal video / customer review），**7/7 详情页均已上线**。

### 1.2 七个详情页（均为已上线、可链 G6 白名单）

| 细分 | 详情页 URL | 页面给的编辑诉求（写文可引） |
|------|-----------|------------------------------|
| Restaurant | [industries/restaurant](https://sparki.io/industries/restaurant) | 厨房/用餐区/菜单素材 → 把客人带进门的视频 |
| Cafe & Coffee Shop | [industries/cafe](https://sparki.io/industries/cafe) | 咖啡拉花、吧台时刻、每日特调 → 温暖快节奏社交短片 |
| Bar & Pub | [industries/bar](https://sparki.io/industries/bar) | 调酒、现场之夜、场地氛围 → 卖出「下一晚」 |
| Bakery & Dessert | [industries/bakery](https://sparki.io/industries/bakery) | 质地、工艺、最终 reveal 居中 |
| Food Truck | [industries/food-truck](https://sparki.io/industries/food-truck) | 备餐、出餐高峰、流动地点 → 可行动的短片 |
| Pizza & Fast Food | [industries/pizza](https://sparki.io/industries/pizza) | 拉丝、滋滋、组装、限时优惠 → 食欲导向 |
| Bubble Tea Shop | [industries/bubble-tea](https://sparki.io/industries/bubble-tea) | 彩色配料、饮品 build、加料选择 → 满足感短片 |

**Restaurant 详情页格式卡示例**（其它餐饮细分结构相同，文案按业态调整，写文时对齐这些格式名）：

| 分组 | 格式 | 时长 · 画幅 |
|------|------|------------|
| Bring people through the door | Business Intro (Store tour) | 20–30s · 9:16 |
| | Service Showcase (Dish & prep) | 10–20s · 9:16 |
| | Deal Video | 8–15s · 9:16 |
| Build trust and reach | Menu Ideas Video | 15–25s · 9:16 |
| | Social Media Video (Multi-platform) | 9:16 / 1:1 / 16:9 |
| | Brand & Team Introduction Video | 30–60s · 9:16 / 16:9 |

> **可链性（G6）**：`/industries` + 7 个详情页全部已上线（对照 project-config §2「Industries」行，线上 21 页）。写文时**一律绝对 URL** `https://sparki.io/industries/{slug}`。

---

## 2. 簇边界：既有 62 篇中的相关资产（禁抢/引用基线）

### 2.1 既有但**非本簇**（区分意图，避免 cannibalization）

| 既有资产 | 角色 | 规则 |
|----------|------|------|
| `how-to-master-viral-food-content-creation-like-bayashitv`（CreatorClone，Bayashi TV） | 红人「快速食谱剪辑」风格拆解 | **消费者/创作者视角**，非「本地商家自拍视频」；新文不复制其「rapid recipe cuts」切点教学 |
| `how-to-master-hyper-realistic-illusion-content-like-amauryguichonchef`（CreatorClone，甜点师） | 红人「超写实甜点 illusion」风格 | 同上；不写「illusion 甜点」第二角度 |
| `jenn-im-toddler-meals-content` / `jenn-im-viral-content-strategy` | 红人饮食内容 | 同上，非商家向 |
| `long-video-to-short-video`（canonical） | 长改短总流程 | 餐饮「一镜到底出餐 → 剪 Shorts」引用它，1–2 句 + `/blog/long-video-to-short-video` |
| `raw-footage-to-montage-ai` | 原始素材→montage | 餐饮「服务高峰素材 → 氛围 montage」引用 |
| `resize-video-for-shorts-reels-tiktok` | 平台尺寸 canonical | 餐饮「竖屏/多画幅」引用 |
| `ai-caption-generator-how-to-pick-the-right-workflow` | 字幕 canonical | 餐饮「静音观看字幕」引用 |
| `ai-video-editor`（canonical） | 泛「AI video editor」概念 | 餐饮新文不重定义「AI video editor」，只 1–2 句引 `/blog/ai-video-editor` |

### 2.2 建议新增 canonical

| 概念 | 建议 canonical slug | 理由 |
|------|-------------------|------|
| **AI 餐厅视频主流程**（手机素材 → Agent 剪成店招/出餐/优惠/团队视频） | `how-to-edit-restaurant-videos-with-ai` | 全簇 vertical 文都引用它；餐厅是最大细分，作为簇流程 canonical |
| **美食过程视频剪辑**（plating / ASMR / 拉丝 / 横切，感官工艺向） | `how-to-edit-food-videos-with-ai` | format 族 spoke 引用它，覆盖用户示例「招牌菜 plating/上菜瞬间」 |

### 2.3 词级禁抢清单

- **大类词**：`AI video editor`（P0，已有 `ai-video-editor` canonical）——新文只做「餐饮/本地商家」垂直化，不做泛 AI video editor 评测。
- **`best-capcut-alternatives`** 等泛竞品词——不重复，餐饮向竞品选型归入本簇自己的 `ai-food-video-editor`（FeatureGuide）。
- **CreatorClone 24 篇**——本簇**不做**红人风格拆解（Bayashi/Amaury 已覆盖 food 向），全部走「本地商家工作流」路线，避免与红人簇混淆。

---

## 3. 搜索量定性验证（2026-09-11 SERP 抽样）

> 依据：web-deep-search + Exa/Perplexity SERP 抽样。以下为**高搜索量 + 高意图**词族，作为选题优先级依据（精确量待 SEMrush/Ahrefs 复核）。

| 词族 | 代表 query（高量） | 意图 | 热度判断 |
|------|-------------------|------|:---:|
| 餐厅视频营销 | `restaurant video marketing` / `restaurant social media` / `restaurant tiktok ideas` / `restaurant reels ideas` | 商业（餐厅老板要获客） | ★★★★★ |
| 餐厅/美食视频剪辑 | `how to edit food videos` / `food video editing` / `AI food video editor` / `restaurant video editor` | 商业（要工具/流程） | ★★★★★ |
| 厨房幕后 | `behind the scenes restaurant video` / `kitchen video` / `chef pov` | 商业+信息 | ★★★★（BTS=餐厅 TikTok 内容 29% 占比，第一格式） |
| 食物感官/ASMR | `food asmr` / `food asmr video editing` / `cheese pull` | 信息+商业 | ★★★★ |
| 咖啡/咖啡馆 | `coffee shop social media` / `cafe reels ideas` / `latte art video` | 商业 | ★★★★ |
| 酒吧 | `bar social media` / `cocktail video` / `bar marketing` | 商业 | ★★★ |
| 烘焙/甜品 | `bakery social media` / `cake decorating video` / `bakery marketing` | 商业 | ★★★ |
| 披萨/快餐 | `pizza reels` / `cheese pull video` | 商业 | ★★★ |
| 餐车 | `food truck marketing` / `food truck social media` / `food truck location video` | 商业 | ★★★（长尾但意图极强） |
| 奶茶/boba | `bubble tea social media` / `boba shop content` | 商业 | ★★★（Gen Z 增长快） |

**SERP 现状**：以 restaurantvelocity / profiletree / evokad / superdirector / poppify / datalatte 等 agency/行业站为主，**几乎没有「本地餐饮 × AI 编辑 Agent」的长文占位**；多为「拍什么」的 idea 清单或「CapCut/FluxNote 模板」教程，缺「已有手机素材 → 对话式 Agent 剪成可发视频」的叙事。

---

## 4. 可构建文章清单（规划文档版，不含正文）

> 字段：Slug / 类型 / Mode / category / 主关键词 / Intent / Investment 预判 / 内链 / 差异化（≥2 信息增量）。成稿时按 skill Phase 0–6 逐篇执行。
> **注**：Investment 五因子中「搜索需求/商业相关性」按上文热度给高分；「差异化能力」因用户要求**不设门槛**，但仍标注可用的差异化点（Moat/一手工作流）。

### P0 — 先发 3 篇（簇骨架：canonical + POV + format canonical）

| # | Slug | 类型 | Mode | category | 主关键词 | Intent | Invest | Hub/内链 |
|---|------|------|:---:|---------|---------|--------|:---:|---------|
| C1 | `how-to-edit-restaurant-videos-with-ai` | WorkflowHowTo | standard | `ai-video-editor` | AI restaurant video editor / edit restaurant videos with AI | 商业 | ≥4.5 | **流程 canonical**；回链 `https://sparki.io/industries` + `…/restaurant` 绝对 URL；引 `/blog/ai-video-editor`（概念）+ `/blog/long-video-to-short-video`（长改短） |
| C2 | `restaurant-video-marketing` | CategoryPOV | flagship | `ai-video-editor` | restaurant video marketing | 信息/商业 | 4.5 | 最高量词；论点「视频已成为餐厅被发现的第一渠道，编辑才是瓶颈」；回链 `…/restaurant` + 其余 6 详情页；引 C1 |
| C3 | `how-to-edit-food-videos-with-ai` | WorkflowHowTo | standard | `Video Editing Features` | how to edit food videos / food video editing | 商业 | 4.5 | **format 族 canonical**（plating/ASMR/拉丝/横切）；回链 `…/restaurant`；引 C1；覆盖用户示例「招牌菜 plating / 上菜瞬间」 |

### P1 — 分垂直铺开（6 篇，一页一篇，覆盖 7 详情页剩余 6 个）

| # | Slug | 类型 | Mode | category | 主关键词 | Intent | Invest | 内链 | 差异化 |
|---|------|------|:---:|---------|---------|--------|:---:|---------|---------|
| V1 | `how-to-edit-coffee-shop-videos` | WorkflowHowTo | standard | `ai-video-editor` | coffee shop social media / cafe video ideas / latte art | 商业 | 4.2 | 回链 `…/cafe`；引 C1 | 拉花/手冲/吧台 BTS 的「拍前 shot list + 对话式剪」；latte art 有 90 秒「保鲜期」痛点（第三方口径） |
| V2 | `how-to-edit-cocktail-videos` | WorkflowHowTo | standard | `Video Editing Features` | cocktail video / bar social media | 商业 | 4.0 | 回链 `…/bar`；引 C1 | 调酒 build/啤酒 pour/活动预告；低光拍摄锁定曝光技巧 |
| V3 | `how-to-edit-bakery-videos` | WorkflowHowTo | standard | `Video Editing Features` | bakery social media / cake decorating video | 商业 | 4.0 | 回链 `…/bakery`；引 C3 | 开炉/time-lapse/横切/裱花；定制蛋糕客群买「能力」非口味 |
| V4 | `how-to-edit-pizza-videos` | WorkflowHowTo | standard | `Video Editing Features` | pizza reels / cheese pull video | 商业 | 3.9 | 回链 `…/pizza`；引 C3 | 拉丝/抛饼/烤炉特写；限时优惠 CTA |
| V5 | `how-to-edit-bubble-tea-videos` | WorkflowHowTo | standard | `Video Editing Features` | bubble tea social media / boba content | 商业 | 3.9 | 回链 `…/bubble-tea`；引 C3 | drink build/配料/封口摇杯/渐变；「5 秒拍照测试」选品 |
| V6 | `how-to-edit-food-truck-videos` | WorkflowHowTo | standard | `ai-video-editor` | food truck marketing / food truck location video | 商业 | 3.9 | 回链 `…/food-truck`；引 C1 | **每日 location drop** 模板化（命脉）；售罄/排队实时播报 |

### P2 — 格式深钻 + 选型（3 篇）

| # | Slug | 类型 | Mode | category | 主关键词 | Intent | Invest | 内链 | 差异化 |
|---|------|------|:---:|---------|---------|--------|:---:|---------|---------|
| F1 | `how-to-edit-food-asmr-videos` | WorkflowHowTo | standard | `Video Editing Features` | food asmr video editing | 信息/商业 | 4.0 | 回链 `…/restaurant`；引 C3 | 原声保留/微距/慢动作节奏；ASMR 完播最高的证据链 |
| F2 | `how-to-edit-kitchen-behind-the-scenes-videos` | WorkflowHowTo | standard | `Video Editing Features` | behind the scenes restaurant video / kitchen video | 信息/商业 | 4.2 | 回链 `…/restaurant` + `…/cafe`；引 C1 | chef POV 胸前机位/非营业时段批拍；BTS=29% 餐厅 TikTok 内容（第三方） |
| S1 | `ai-food-video-editor` | FeatureGuide | standard | `ai-video-editor` | AI food video editor / food video editor app | 商业 | 4.0 | 回链 `/industries` + `…/restaurant`；引 C1/C3 + `/blog/ai-video-editor` | 决策表（手动模板 vs 转录长改短 vs 生成 vs Agent）；红海词但靠「本地商家」垂直化 |

### P2b — 延后/观察

| # | Slug（草） | 类型 | 理由 |
|---|-----------|------|------|
| X1 | `best-restaurant-video-editors` | AlternativeRoundup | 与 S1「AI food video editor」重叠度高；待 S1 发布后决定是否拆开做「restaurant video editor」榜单（捕获 `restaurant video editor` 词） |
| X2 | `restaurant-video-ideas` | AlternativeRoundup / WorkflowHowTo | 「restaurant video ideas」高量但偏 listicle；可做「30 个可重复视频格式库」，与 C2/C1 错位后开 |
| X3 | 各细分 CreatorClone（如咖啡博主、调酒博主） | CreatorClone | 与红人簇 24 篇边界；仅当有「未覆盖 creator + 本地商家可学」角度才开 |

---

## 5. Hub/Spoke 内链图（G6 合规：只链已上线）

```
https://sparki.io/industries  ←—— 聚合 hub（所有文章至少 1 次绝对 URL 回链）
        │ 7 个 F&B 详情页（各 vertical 文回链其对应页）
        │   restaurant / cafe / bar / bakery / food-truck / pizza / bubble-tea
        ▼
  /blog/...（blog 相对链接，互链）
        │
C1  how-to-edit-restaurant-videos-with-ai   ← 流程 canonical（所有 vertical 文引用）
C2  restaurant-video-marketing              ← POV（引 C1 + 7 详情页）
C3  how-to-edit-food-videos-with-ai         ← format canonical（plating/ASMR/拉丝/横切）
        │
        ├─ V1 coffee-shop（引 C1 + cafe 页）
        ├─ V2 cocktail（引 C1 + bar 页）
        ├─ V3 bakery（引 C3 + bakery 页）
        ├─ V4 pizza（引 C3 + pizza 页）
        ├─ V5 bubble-tea（引 C3 + bubble-tea 页）
        ├─ V6 food-truck（引 C1 + food-truck 页）
        ├─ F1 food-asmr（引 C3 + restaurant 页）
        ├─ F2 kitchen-bts（引 C1 + restaurant/cafe 页）
        └─ S1 ai-food-video-editor（引 C1/C3 + industries 页）

既有簇锚点：/blog/ai-video-editor（概念）· /blog/long-video-to-short-video（长改短）· /blog/resize-video-for-shorts-reels-tiktok（尺寸）· /blog/ai-caption-generator-how-to-pick-the-right-workflow（字幕）
```

**互链规则**：
1. 每篇**至少 1 次**回链 `/industries` 绝对 URL；vertical 文回链其对应详情页绝对 URL。
2. 每篇**至少 1 次**链 C1（或 C3，视 format/vertical 归属）。
3. 6 个 vertical 文彼此 **1 处**交叉（如 V1 coffee↔V3 bakery 因「咖啡馆面包/甜品」相关），避免雷同。
4. 禁止链 coming-soon/未上线细分页（如 yoga、pet、real estate）。

---

## 6. 排期与发布节奏建议

| 波次 | 文章 | 建议间隔 | 备注 |
|------|------|---------|------|
| 第一波 | C1 → C2 → C3 | 每 1–2 天 ≤1 篇（content-graph 日期避让） | 先立骨架（流程 canonical + POV + format canonical） |
| 第二波 | V1–V6 | 每周 2–3 | 6 个垂直铺开，覆盖 7 详情页 |
| 第三波 | F1 → F2 → S1 | 后续周 | 格式深钻 + 选型 |
| 延后 | X1/X2/X3 | 视数据 | X2 待 C2/C1 稳定后开 |

- 每篇发布后：更新 `skills/sparki-blog-article/references/content-graph.md` §2/§3/§4/§5。
- 每篇开工前：跑 skill Phase 0 KEEP/MERGE 判定 + 与 §2.3 禁抢清单复核。

---

## 7. 打开项（给人工/后续任务的 TODO）

- [ ] 精确搜索量：用 SEMrush/Ahrefs 复核第 §3 词族的量级，定稿 P0/P1 发布优先级（当前为定性判断）。
- [ ] `project-config.md` §2 白名单确认 `/industries` 聚合页 URL（当前白名单只列了 `industries/{slug}` 详情页；聚合页 `https://sparki.io/industries` 需人工加入白名单表）。
- [ ] `product-competitors.md` 竞品矩阵补「本地商户/餐饮视频」赛道玩家（Captions /solutions/food-creators、FluxNote、ppl.studio、Restaurant Velocity 等）。
- [ ] `keywords.md` 补餐饮垂直词族（restaurant video marketing / AI restaurant video editor / food video editing / cafe/bar/bakery/pizza/boba/food-truck 词）。
- [ ] X2「restaurant video ideas」是否独立成篇（与 C2/C1 边界），待 C1/C2 定稿后决策。

---

## 8. 参考来源（web-deep-search 关键链接）

- 品类/竞品：[Restaurant Velocity — video marketing](https://restaurantvelocity.com/blog/restaurant-video-marketing/)（7 种视频类型 + 平台）· [Restaurant Velocity — Reels ideas](https://restaurantvelocity.com/blog/restaurant-reels-ideas/)（30 格式库）· [Superdirector — restaurants](https://superdirector.app/industries/restaurants)（品牌案例 Crumbl/Sweetgreen/Joe & The Juice）· [Captions /solutions/food-creators](https://captions.ai/solutions/food-creators)（竞品垂直页）· [FluxNote — coffee shop video marketing](https://fluxnote.io/guides/coffee-shop-video-marketing-social-media)
- 垂直/格式：[DataLatte — Reels for coffee shops](https://datalatte.pro/blog/instagram-reels-for-coffee-shops) · [Poppify — cafe reels](https://poppify.ai/research/instagram-reel-ideas-cafe) · [Poppify — bakery reels](https://poppify.ai/research/instagram-reel-ideas-bakery) · [socialmon — pizza](https://www.socialmon.ai/blog/71-pizza-shop-instagram-post-ideas-with-examples-that-drive-orders) · [socialmon — bubble tea](https://www.socialmon.ai/blog/60-bubble-tea-shop-instagram-post-ideas-with-examples-that-sell) · [Versely — food truck](https://www.versely.studio/blog/food-truck-video-marketing-with-ai) · [ppl.studio — boba](https://ppl.studio/blog/ai-ugc-for-boba-tea-and-bubble-tea-shop-marketing) · [Byter — cocktail bars](https://byter.com/instagram-and-content-strategy-for-london-cocktail-bars/)
- 官方：TikTok for Business F&B 指南（80/20、前 3 秒 hook、Spark Ads）· Toast TikTok marketing
- 痛点/风险：[The Guardian — viral queues](https://www.theguardian.com/food/2026/sep/10/people-waited-24-hours-for-a-potato-how-viral-queues-help-and-harm-restaurants) · Reddit r/restaurant 店主 DIY 时间成本

> 事实口径：产品 claim 以 sparki.io 官方页为准（对照 product-competitors.md / proof-library.md）；第三方耗时/竞品数据属 T2 舆情，写作时按 skill 引用分级处理，不做无源数字。

---

*sparki · blog/food-beverage topic cluster · planning v0.1 · 2026-09-11 · web-deep-search baseline 2026-09-11*
*关联：[SKILL](../skills/sparki-blog-article/SKILL.md) · [content-graph](../skills/sparki-blog-article/references/content-graph.md) · [industries-pages](../video-types/industries-pages.md)（B1 餐饮 7 详情页）· [use-cases](../sparki-use-cases.md)*
