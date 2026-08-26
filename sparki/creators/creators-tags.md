# Sparki Creators · 红人标签体系

> 收集、聚类红人时使用的多维打标规范。**大词(Hub Tag) 仅允许 [video-types](../video-types/) 四维分类已有或规划中的 slug**;Creators 自建细分、手法、主题一律归入小词。

---

## 一、为什么要打标

| 用途 | 说明 |
|------|------|
| **聚类** | 按形态、行业、平台批量找「同类红人」扩页 |
| **落地页关联** | 大词 → video-types 对应 hub / solution / industry / platform 页,便于内链与 SEO 集群 |
| **采集一致** | 新人入库时必填结构化字段;细分主题放小词,避免 `food` / `grwm-vlog` / `food-craft` 等多套口径并存 |

**原则**

- **大词(Hub Tag)**:受控词表 = **video-types 维度 1–4 + Goal** 的官方 slug;Sidebar **可点击**,链至已有或规划中的 taxonomy 落地页。
- **小词(Display Tag)**:自由文本 — GRWM、Beat-sync、Korean Idol 等**仅展示**,不可点击;**不得**冒充大词或新建 taxonomy 类别。
- **Creators 列表 tab**(`creators_tab`):仅 `/creators` 列表筛选用 UI 维度,**不是** taxonomy 大词;须可映射回 F/C/B,但本身不入 Hub 词表。
- 打标以 **Signature Video** 为准;频道次要内容放 `notes`。

---

## 二、与 video-types 对齐：对比与调整

### 2.1 原词表问题(已废弃为 Hub 来源)

| 原大词来源 | 问题 | 调整 |
|-----------|------|------|
| `format.l2`(如 `grwm-vlog`, `food-craft`, `dance-montage`) | Creators 自建 L2,**无** video-types 对应项 | → **小词**(`display_tag` / `subject.*`);聚类用 `format` 列写 F 编号 |
| `creators_tab`(如 `food-craft`, `comedy-entertainment`) | 列表 UI 分组,非 taxonomy 行业/形态 | → **仅** `creators_tab` 列保留;Hub 改填 C/B/F |
| `use_case`(vlog / montage / commentary) | 与维度 1 F07/F08/F09/F10 **重复** | → 删除独立词表;统一用 `format` slug |
| L1 变体 `craft-process`, `skit-comedy`, `transformation` | 非 F01–F21 官方形态 | → 映射到 F02/F07/F10/F20 等;细分放小词 |
| `/creators/tags/{slug}` 聚合页 | 规划路径不在 video-types 站内 IA | → 废弃;Hub `href` 改指 taxonomy 正式 URL |

### 2.2 Hub Tag 合法来源(唯一)

大词 slug **必须**来自下表;新增 slug 须先在 [video-types-taxonomy.md](../video-types/video-types-taxonomy.md) 登记。

| 维度 | 字段前缀 | slug 数量 | 落地页文档 |
|------|---------|----------|-----------|
| 维度 1 形态 Format | `format.*` | F01–F21 | [product-video](../video-types/product-video-pages.md) · [gaming](../video-types/gaming-pages.md) · 规划 Creator/Local 形态页 |
| 维度 2-A 消费品类 | `industry.consumer.*` | C01–C06 | [product-video](../video-types/product-video-pages.md) |
| 维度 2-B 本地商户 | `industry.local.*` | B1–B7 + 21 细分 | [industries](../video-types/industries-pages.md) |
| 维度 3 目标 Goal | `goal.*` | G01–G04 | 无独立页,可作 Hub(plan)或仅内部列 |
| 维度 4 平台 Platform | `platform.*` | P01–P15 | [platforms](../video-types/platforms-pages.md) |

### 2.3 `creators_tab` → video-types 映射(UI 筛选用)

列表 tab **保留现状**,但采集时须同时填 taxonomy 字段;**禁止**把 tab slug 写入 `hub_tag_*`。

| creators_tab(UI) | 映射 video-types | 说明 |
|------------------|------------------|------|
| `fashion-beauty` | C01 `beauty` + C02 `fashion` | 红人频道偏消费品牌,非 B2 门店 |
| `food-craft` | F10 `montage` 或 F02 `product-demo` | 「craft」不是行业;食品主题进小词 |
| `lifestyle-travel` | F07 `vlog` | 旅行/生活方式进小词 |
| `fitness` | B3 `health-fitness` 或 F07 `vlog` | 健身红人偏创作者形态,非 gym 门店 |
| `comedy-entertainment` | F07 `vlog` 或 F09 `talking-head` | 喜剧不是独立 taxonomy 类 |

---

## 三、Creators 卡片 Sidebar

```
┌─ Creator Card (Sidebar) ─────────────┐
│  [缩略图]                               │
│  JISOO · @sooyaaa__                    │
│                                        │
│  [ Fashion ] [ Vlog ]        ← 大词·可点 │
│  (taxonomy: C02 + F07)                 │
│                                        │
│  GRWM · Luxury · Korean Idol · Macro   │
│                    ← 小词·纯文字不可点  │
└────────────────────────────────────────┘
```

| 呈现层 | Excel 列 | 交互 | 说明 |
|--------|----------|------|------|
| **大词 Hub Tag** | `hub_tag_1_*`, `hub_tag_2_*` | **可点击** | slug 必须 ∈ 第四节词表;每红人最多 2 个 |
| **小词 Display Tag** | `display_tag_1`–`display_tag_4` | **纯文字** | 含原 L2 细分(GRWM、Food Craft、Beat-sync 等) |
| **列表 tab** | `creators_tab` | 列表页筛选 | UI 专用,≠ Hub |

**Hub `href` 规则**

| 大词类型 | href 示例 | status |
|----------|-----------|--------|
| F 形态(已上线) | `/video-editor/unboxing` | `live` |
| F 形态(未建页) | `/video-editor/vlog`(规划) | `plan` |
| F11 Copy Style | `/features/copy-style` | `live` |
| C 品类 | `/product-video/fashion`(规划) | `plan` |
| B 细分(已上线) | `/industries/gym` | `live` |
| P 平台(聚合) | `/platforms` | `live` |
| P 平台(详情) | `/platforms/tiktok`(规划) | `plan` |
| G 目标 | — | 通常不上 Hub,写 `video_types_goal` |

> 无聚合页时 `hub_tag_*_status=plan`,前端降级纯文字;**禁止**标 `live` 但 slug 不在词表内。

---

## 四、结构化词表(S · Hub Tag 唯一来源)

### 4.1 维度 1 · 内容形态 `format`(F01–F21)

slug 与 [video-types-taxonomy](../video-types/video-types-taxonomy.md) 一致;有详情页的填 `live` href。

| slug | F | 说明 | 落地页 status |
|------|---|------|--------------|
| `unboxing` | F01 | 开箱 | live → `/video-editor/unboxing` |
| `product-demo` | F02 | 产品展示 / 工艺过程 | live |
| `product-ad` | F03 | 产品广告 | live |
| `product-review` | F04 | 产品测评 | live |
| `product-tutorial` | F05 | 产品教程 | live |
| `ecommerce-product-video` | F06 | 电商商品视频 | plan(仅聚合 section) |
| `vlog` | F07 | 生活记录、小剧、情侣日常 | plan |
| `commentary` | F08 | 解说评述 | plan |
| `talking-head` | F09 | 口播访谈 | plan |
| `montage` | F10 | 混剪集锦、卡点、ASMR 料理 | live 能力;形态页 plan |
| `copy-style` | F11 | 风格拷贝 | live → `/features/copy-style` |
| `gaming-highlight` | F12 | 游戏高光 | live |
| `gameplay` | F13 | 游戏实况 | live |
| `gaming-commentary` | F14 | 游戏解说 | live |
| `lets-play` | F15 | 实况互动 | live |
| `game-tutorial` | F16 | 游戏教程 | live |
| `game-review` | F17 | 游戏测评 | live |
| `local-ad` | F18 | 商户推广 | plan |
| `storefront-tour` | F19 | 店铺探访 | plan |
| `before-after` | F20 | 服务前后对比 | plan |
| `owner-interview` | F21 | 店主访谈 | plan |

**原 L1/L2 细分 → 映射示例(写入 `format` + 小词,不再作 Hub slug)**

| 原 L2(废弃 Hub) | format slug | 小词示例 |
|----------------|-------------|---------|
| `grwm-vlog`, `food-vlog`, `couple-vlog` | `vlog` | GRWM, Food, Couple |
| `food-craft`, `food-asmr` | `montage` 或 `product-demo` | Craft, ASMR, Beat-sync |
| `dance-montage`, `travel-montage` | `montage` | Dance, Travel |
| `food-review` | `product-review` | Food Review, Theme Park |
| `expectation-reality`, `prank-couple` | `vlog` 或 `talking-head` | Comedy, Prank |
| `body-transformation` | `montage` 或 `before-after` | Transformation, Fitness |

### 4.2 维度 2-A · 消费品牌 `industry.consumer`(C01–C06)

| slug | 编号 | 规划落地页 |
|------|------|-----------|
| `beauty` | C01 | `/product-video/beauty` |
| `fashion` | C02 | `/product-video/fashion` |
| `electronics` | C03 | `/product-video/electronics` |
| `home-kitchen` | C04 | `/product-video/home-kitchen` |
| `food-beverage` | C05 | `/product-video/food-beverage` |
| `saas-app` | C06 | `/product-video/saas-app` |

> C 系列指**卖产品的品牌/电商**,与 B 系列本地门店互斥。食品工艺红人(Amaury/Bayashi)通常标 F 形态 + 小词 Food,**不**标 B1 餐饮。

### 4.3 维度 2-B · 本地商户 `industry.local`(B1–B7)

**行业组 slug**(Hub 用大词):

| slug | 编号 | 聚合页 |
|------|------|--------|
| `food-beverage` | B1 | `/industries` |
| `beauty-personal-care` | B2 | `/industries` |
| `health-fitness` | B3 | `/industries` |
| `real-estate-rentals` | B4 | `/industries` |
| `home-property-services` | B5 | `/industries` |
| `pet-services` | B6 | `/industries` |
| `auto-services` | B7 | `/industries` |

**细分 slug**(Hub 可选,详情页已上线者标 `live`):`restaurant`, `cafe`, `bar`, `bakery`, `food-truck`, `pizza`, `bubble-tea`, `hair-salon`, `barber`, `nail-salon`, `tattoo`, `massage`, `spa`, `gym`, `interior-design`, `landscaping` 等 — 完整清单见 [industries-pages.md](../video-types/industries-pages.md)。

> 当前 14 位红人均为创作者频道,**默认不标 B**;仅内容明确服务某类本地门店时再标。

### 4.4 维度 3 · 目标 `goal`(G01–G04)

| slug | 编号 | Hub 用法 |
|------|------|---------|
| `reach` | G01 | 通常仅写 `video_types_goal`,不上卡片 |
| `conversion` | G02 | 同上 |
| `trust` | G03 | 同上 |
| `retention` | G04 | 同上 |

### 4.5 维度 4 · 平台 `platform`(P01–P15)

与 [platforms-pages.md](../video-types/platforms-pages.md) 一致。

| slug | P | 说明 |
|------|---|------|
| `tiktok` | P01 | |
| `instagram-reels` | P02 | |
| `youtube-shorts` | P03 | 14 位红人主战场 |
| `facebook-reels` | P04 | |
| `snapchat` | P05 | |
| `pinterest` | P06 | |
| `youtube` | P07 | |
| `twitch` | P08 | |
| `linkedin` | P09 | |
| `x` | P10 | |
| `amazon` | P11 | |
| `tiktok-shop` | P12 | |
| `shopify` | P13 | |
| `meta-ads` | P14 | |
| `etsy` | P15 | |

`platform` 列必填,**一般不上 Hub 卡片**(除非频道定位极端单一);以内部字段 + 详情页「YouTube Shorts」展示为主。

---

## 五、自由标签(F · 小词 / Display Tag)

小词**不入 Hub 词表**,仅 `display_tag_1–4` 上屏。

| 分组 | 前缀 | 示例 |
|------|------|------|
| 内容细分(原 L2) | `subject.*` | `grwm`, `food-craft`, `travel`, `couple`, `theme-park`, `self-care` |
| 剪辑手法 | `style.*` | `beat-sync`, `light-leak`, `macro-detail`, `jump-cut`, `asmr-only`, `no-music` |
| 身份属性 | `identity.*` | `korean-idol`, `celebrity`, `couple-creator`, `faceless`, `gen-z` |
| 传播属性 | `subject.*` | `viral-short`, `high-retention` |

---

## 六、落地页关联(L · Hub href 数据源)

| 关联键 | 指向 | 示例 | Hub |
|--------|------|------|:---:|
| `landing.creator_page` | Creators 详情 | `/creators/jisoo` | — |
| `landing.creators_tab` | 列表 tab 筛选 | `/creators?tab=fashion-beauty` | — |
| `landing.format` | 形态 solution | `/video-editor/montage` | ✅ |
| `landing.industry_consumer` | 消费品类 | `/product-video/fashion` | ✅ |
| `landing.industry_local` | 本地商户 | `/industries/gym` | ✅ |
| `landing.platform_hub` | 平台 | `/platforms` · `/platforms/tiktok` | ✅ |
| `landing.feature` | Features | `/features/copy-style` | ✅(F11) |
| `video_types.format` | F 编号 | `F07` | 内部 |

~~`landing.format_hub` → `/creators/tags/…`~~ **已废弃**。

---

## 七、Excel 采集格式

### 7.1 表头(第 1 行)

```
creator_id	display_name	handle	status	creator_page	creators_tab	format	industry_consumer	industry_local	platform	hub_tag_1_slug	hub_tag_1_label	hub_tag_1_href	hub_tag_1_status	hub_tag_2_slug	hub_tag_2_label	hub_tag_2_href	hub_tag_2_status	display_tag_1	display_tag_2	display_tag_3	display_tag_4	style_tags	subject_tags	identity_tags	signature_video_title	signature_video_url	video_types_format	video_types_industry	video_types_goal	notes
```

> 变更:`format_l1`/`format_l2`/`use_case` 合并为 **`format`**(taxonomy slug,可逗号多值);新增可选 **`industry_local`**(B 系列);`hub_tag_*` slug 必须 ∈ 第四节。

### 7.2 列说明

| 列名 | 必填 | 大/小 | 说明 |
|------|:--:|:---:|------|
| creators_tab | ✅ | UI | 列表 tab;∈ 五类 UI slug,≠ Hub |
| format | ✅ | 大词源 | taxonomy format slug,如 `vlog` 或 `montage,vlog` |
| industry_consumer | | 大词源 | C01–C06 slug,逗号分隔 |
| industry_local | | 大词源 | B 组/细分 slug;创作者频道通常留空 |
| platform | ✅ | 内部 | P slug,如 `youtube-shorts` |
| hub_tag_1/2_* | ✅ | **大词** | slug/label/href/status;slug ∈ 第四节 |
| display_tag_1–4 | ✅ | **小词** | 含 GRWM、Food Craft 等原 L2 文案 |
| video_types_format | | 内部 | F 编号,如 `F07,F11` |
| video_types_industry | | 内部 | `C01,C02` 或 `B3` |
| video_types_goal | | 内部 | `G02,G04` |

---

## 八、打标示范 · JISOO(Excel 第 2 行)

> [sparki.io/creators/jisoo](https://sparki.io/creators/jisoo) · Signature: First Met Gala, JISOO In New York(41s)

**Sidebar 效果**

```
JISOO · @sooyaaa__
[Fashion] [Vlog]              ← hub: C02 + F07 · 可点(plan)
GRWM · Luxury · Korean Idol · Macro Detail   ← 小词
```

**复制以下整行 → Excel A2**:

```
jisoo	JISOO	@sooyaaa__	live	https://sparki.io/creators/jisoo	fashion-beauty	vlog,montage	fashion,beauty		youtube-shorts	fashion	Fashion	/product-video/fashion	plan	vlog	Vlog	/video-editor/vlog	plan	GRWM	Luxury	Korean Idol	Macro Detail	macro-detail,light-leak,center-frame,warm-to-cool-grade,felt-rhythm	grwm,luxury,red-carpet,fashion-editorial,event-coverage	korean-idol,celebrity,blackpink	First Met Gala, JISOO In New York #JISOO #Dior #Cartier #MetGala	https://youtube.com/shorts/yOjCkemrzQQ	F07,F11	C01,C02	G02,G04	creators_tab仅列表筛选;GRWM改小词;hub对齐C02+F07
```

| 字段 | JISOO 取值 |
|------|-----------|
| 大词 Hub | Fashion(C02) · Vlog(F07) |
| 小词 Display | GRWM · Luxury · Korean Idol · Macro Detail |
| UI tab | `fashion-beauty`(≠ Hub) |
| 聚类主键 | `format=vlog,montage` + `industry=fashion,beauty` |

---

## 九、已上线 14 人 · Hub / Display 速查

> Hub 仅用 taxonomy slug;Display 可保留原风格语义。`creators_tab` 见 2.3 映射。

| creator_id | creators_tab | hub_tag 建议(slug) | display_tag 建议 |
|------------|--------------|-------------------|-----------------|
| jisoo | fashion-beauty | *(见第八节)* | *(见第八节)* |
| jenn-im | fashion-beauty | `fashion`, `vlog` | Motherhood, Food, Warm Grade |
| amaury-guichon | food-craft | `montage`, `product-demo` | Beat-sync, Macro Texture, Food Craft |
| bayashi-tv | food-craft | `montage` | ASMR, Open Loop, Faceless, Food |
| elysian-living | lifestyle-travel | `vlog`, `beauty` | Self-care, Cozy, NYC, ASMR |
| nicole-laeno | lifestyle-travel | `montage`, `vlog` | Beat-sync, Dance, Travel |
| kara-and-nate | lifestyle-travel | `vlog`, `montage` | Adventure, Drone POV, Travel |
| spencer-barbosa | lifestyle-travel | `vlog` | Work-play-hard, Lifestyle |
| brooke-monk | lifestyle-travel | `product-review`, `vlog` | Comedy, Theme Park, Food Review |
| katie-feeney | fitness | `vlog` | Sports, Vulnerability Hook, NYC |
| pamela-reif | fitness | `montage`, `vlog` | Transformation, Fitness, Dual Timeline |
| lilly-singh | comedy-entertainment | `vlog`, `talking-head` | Comedy, Silence Punchline, Pet |
| candy-superstar | comedy-entertainment | `montage`, `vlog` | Prank, Multi-hook, High Saturation |
| theabnormalcouple | comedy-entertainment | `vlog` | Couple, Polished-then-real |

---

## 十、采集与维护流程

1. **定 taxonomy**:先填 `format` / `industry_consumer` / `platform` / `video_types_*`。
2. **选 Hub**:从第四节选 1–2 个 slug 写入 `hub_tag_*`;href 指向第六节正式 URL。
3. **写小词**:原 L2 细分、手法、身份 → `display_tag_*` + `style/subject/identity_tags`。
4. **填 UI tab**:`creators_tab` 仅用于列表筛选,与 Hub 可不一致但须满足 2.3 映射。
5. **校验**:`hub_tag_*_slug` ∈ 第四节;`status=live` 时 href 必须可访问;禁止 `/creators/tags/` 路径。
6. **扩页**:video-types 新建落地页后,批量把对应行 `hub_tag_*_status` 从 `plan` 改为 `live`。

---

*遵循 [客户文档规范](../../demo/client-template.md)*  
*关联：[creators-roster.md](./creators-roster.md) | [creators-pages.md](./creators-pages.md) | [video-types/](../video-types/)*  
*Last updated: 2026-08-26*
