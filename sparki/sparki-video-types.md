# Sparki 剪辑视频类型(多维分类)

## 〇、维度说明(可扩展)

本分类采用**多维结构**,每个维度独立、可单独扩展。当前已启用 3 个维度:

| 维度 | 名称 | 取值数量 | 说明 |
|------|------|---------|------|
| **维度 1** | **内容形态(Format)** | 5 大类 / 21 种 | 视频「长什么样」——按镜头结构、剪辑节奏、叙事目的划分,**当前主分类** |
| **维度 2** | **行业(Industry)** | 2 子域:消费品牌品类(C01–C06)+ 本地商户服务(B1–B7 / 21 细分) | 视频「给谁做的」——按客户行业划分。**拆分两个子域**:消费品牌品类(卖产品)与本地商户服务(卖服务),互不混用(详见第二节) |
| **维度 3** | **目标与转化(Goal)** | 4 种 | 视频「用来干什么」——按营销/运营目标划分 |

> 后续新增维度(如**平台渠道 Platform**:YouTube Shorts / TikTok / Reels / 电商主图;**视频时长 Duration**:Short / Long;**语言 Localization**:英语/西语/中文 等)可直接追加到本节。

---

## 一、维度 1:内容形态(Format)· 主分类

按**镜头结构、剪辑节奏、叙事目的**划分,是页面/模板/SEO 的主分类维度。

### A. 产品与带货类(Product & Commerce)

| 编号 | 细分分类 | 说明 |
|------|----------|------|
| F01 | **Unboxing Video 开箱** | 开箱过程、包装体验、初印象反应 |
| F02 | **Product Demo Video 产品展示** | 展示产品外观、结构与核心卖点 |
| F03 | **Product Ad / Commercial 产品广告** | 面向投放的短广告/商业片 |
| F04 | **Product Review Video 产品测评** | 真实使用体验、优缺点评价 |
| F05 | **Product Tutorial / How-to Video 产品使用教程** | 教用户如何使用产品 |
| F06 | **E-commerce Product Video 电商商品视频** | 电商平台商品主图/详情页视频 |

### B. 内容创作者类(Creator)

| 编号 | 细分分类 | 说明 |
|------|----------|------|
| F07 | **Vlog 生活记录** | 日常记录、第一人称叙事 |
| F08 | **Commentary 解说/评述** | 边展示边解说、发表观点(含游戏解说) |
| F09 | **Talking-head 口播/访谈** | 人物对镜头讲述、访谈式 |
| F10 | **Montage / Highlight Reels 混剪/集锦** | 高光片段、节奏混剪(含游戏高光) |
| F11 | **Copy Style 风格拷贝** | 参考一条视频的风格应用到新素材(Sparki 核心功能) |

### C. 游戏类(Gaming)

| 编号 | 细分分类 | 说明 |
|------|----------|------|
| F12 | **Gaming Highlight 游戏高光** | 精彩操作/名场面集锦(归类于 Montage/Highlight) |
| F13 | **Gameplay Video 游戏实况** | 纯游戏过程录制,侧重画面与操作 |
| F14 | **Gaming Commentary 游戏解说** | 边玩边解说/评述(归类于 Commentary) |
| F15 | **Let's Play Video 实况互动** | 玩家游玩+实时反应解说的陪伴式实况 |
| F16 | **Game Tutorial / Guide Video 游戏教程** | 攻略、技巧教学 |
| F17 | **Game Review Video 游戏测评** | 游戏评测、推荐/避雷 |

> 注:F12/F14 与 F10/F08 同属一形态,Gaming 单独列出便于游戏模板库与 SEO 落地,避免重复建页。

### D. 本地商户推广类(Local Business Promotion)

本地商户的引流/促销视频,**形态上复用 A/B/C 各形态**,只是素材来自本地商户。

| 编号 | 细分分类 | 说明 |
|------|----------|------|
| F18 | **Local Ad / Promo 商户推广** | 商户促销、活动、引流短视频(复用餐饮/美业等行业素材) |
| F19 | **Storefront / Tour 店铺探访** | 探店、环境展示、服务流程展示 |
| F20 | **Service Before-After 服务前后对比** | 改造/清洁/美容等服务效果对比 |
| F21 | **Owner Interview 店主访谈** | 店主口播、品牌故事(归类于 Talking-head) |

---

## 二、维度 2:行业(Industry)· 矩阵

「内容形态 × 行业」可组合使用:如 **F19 店铺探访 × B1 餐饮**、**F20 前后对比 × B2 美业**。标注 **P0/P1** 为制作优先级。

**维度 2 拆分两个子域,互不混用**:

| 子域 | 对象 | 素材来源 | 适用形态 | 目标客户 | 长尾 URL |
|------|------|---------|---------|---------|---------|
| **2-A 消费品牌品类**(C01–C06) | 卖**产品**的品牌/电商 | 产品图、产品剪辑 | F01–F06 产品类 | B2C 品牌市场部/电商运营 | `/product-video/{品类}` |
| **2-B 本地商户服务**(B1–B7) | 卖**服务**的本地商户 | 门店、服务过程、店主口播 | F18–F21 为主,复用 A/B/C | B2B 本地商户主 | `/local-business-video/{行业}` |

### 子域 2-A:消费品牌品类(Consumer Category)· 新增

> 来源:/product-video 页 "By industry & channel" 组,原为页面新冒出口径,现已归档为维度 2 正式子域。

| 编号 | 品类 | 说明 | 页面对应 |
|------|------|------|---------|
| C01 | **Beauty & Personal Care 美妆个护** | 美妆、护肤、个护品牌的产品视频/广告 | Beauty |
| C02 | **Fashion & Apparel 时尚服饰** | 服装、鞋履、配饰的穿搭与单品展示 | Fashion |
| C03 | **Consumer Electronics 消费电子** | 3C 数码、智能硬件的功能展示与测评 | Electronics |
| C04 | **Home & Kitchen 家居厨房(产品)** | 家居用品、厨具、小家电等实体产品 | Home & Kitchen |
| C05 | **Food & Beverage 食品饮料** | 食品、饮品的产品展示与促销 | —(扩展位) |
| C06 | **SaaS & App 软件与 App** | 软件/SaaS 演示、App 录屏(区别于实体产品) | SaaS & App Demos |

> 注:C01–C04 对应线上页面已有品类,C05 为预留扩展位。子域对象是「卖产品的品牌/电商」,素材=产品图/产品剪辑,适用形态 F01–F06。

### 子域 2-B:本地商户服务(Local Business Service)· 现有

> 文档原有 7 大行业,编号改为 B 系列以区别于 C 系列。

### B1. 餐饮【P0】

| 细分分类 |
|----------|
| 餐厅/咖啡馆/酒吧 |
| 甜品店/烘焙店 |

### B2. 美业与个护【P0】

| 细分分类 |
|----------|
| 美甲美睫/美发沙龙 |
| 美容 SPA/医美诊所 |
| 纹身店 |

### B3. 健康与健身【P0】

| 细分分类 |
|----------|
| 健身房/私教工作室 |
| 瑜伽/普拉提馆 |
| 按摩/理疗诊所 |

### B4. 房产与中介服务【P0】

| 细分分类 |
|----------|
| 房产经纪人 |
| 房屋租赁中介 |
| 民宿/Airbnb 房东 |

### B5. 家居与家政服务【P1】

| 细分分类 |
|----------|
| 装修/室内设计 |
| 清洁保洁服务 |
| 园艺/草坪维护 |
| 水电维修 |

### B6. 宠物服务【P1】

| 细分分类 |
|----------|
| 宠物美容/寄养 |
| 宠物训练 |
| 兽医诊所 |

### B7. 汽车服务【P1】

| 细分分类 |
|----------|
| 汽车美容/贴膜 |
| 汽修/保养 |
| 二手车经销 |

### 易混淆判定(两子域边界)

| 相似名 | 归属 | 判据 |
|--------|------|------|
| C04 家居厨房 vs B5 家居与家政 | 产品线 vs 服务线 | 卖**家居产品**(吸尘器/锅具)→ C04;卖**装修/清洁服务** → B5 |
| C01 美妆个护 vs B2 美业个护 | 产品线 vs 服务线 | 卖**美妆产品**给消费者 → C01;提供**美甲/美发服务**的门店 → B2 |
| (扩展)C 宠物用品 vs B6 宠物服务 | 产品线 vs 服务线 | 卖**宠物用品** → C 扩展位;提供**美容/寄养服务** → B6 |
| 判据统一 | — | 素材是「产品图/产品剪辑」→ 2-A;素材是「门店/服务过程/店主口播」→ 2-B |

---

## 三、维度 3:目标与转化(Goal)

按**营销/运营目标**划分,每个目标可套用维度 1 中多种形态。

| 编号 | 目标 | 适用形态示例 |
|------|------|-------------|
| G01 | **获客拉新(Reach)** | 短视频广告、平台种草、SEO 长尾页 |
| G02 | **转化带货(Conversion)** | 电商商品视频、产品广告、促销 |
| G03 | **信任背书(Trust)** | 测评、教程、店主访谈、前后对比 |
| G04 | **留存复购(Retention)** | 系列化内容、Copy Style 风格延续 |

---

## 四、组合示例(多维度组合)

| 内容形态 | 行业 | 目标 | 组合说明 |
|---------|------|------|---------|
| F06 电商商品视频 | C01 美妆个护 | G02 转化带货 | 美妆产品电商主图视频 |
| F02 产品展示 | C04 家居厨房(产品) | G02 转化带货 | 厨具产品详情页演示 |
| F20 前后对比 | B5 家居与家政 | G03 信任背书 | 清洁保洁服务效果对比 |
| F18 商户推广 | B1 餐饮 | G01 获客拉新 | 餐厅新品促销短视频 |
| F15 Let's Play | —(泛游戏) | G01 获客拉新 | 游戏实况解说 |
| F11 Copy Style | —(泛创作者) | G04 留存复购 | 系列风格视频 |

---

## 五、备注

- **P0/P1** 为**本地商户服务子域(2-B)** 的制作优先级,便于分阶段排期。
- **行业维度拆分为两子域**:消费品牌品类(C01–C06,服务于电商/品牌方)与本地商户服务(B1–B7,服务于本地商户)。两子域素材来源、适用形态、目标客户不同,SEO 长尾 URL 分别走 `/product-video/{品类}` 与 `/local-business-video/{行业}` 两条线,不可互相替换。
- **内容形态是主分类**,行业/目标为组合维度;页面/模板/SEO 建议以「形态」为主键建页,行业作长尾。
- 后续新增维度(平台渠道、时长、语言等)直接补充到「〇、维度说明」并相应建表。

---

## 六、`/product-video` 页面快照与差异分析

> 页面:[sparki-ai.lovable.app/product-video](https://sparki-ai.lovable.app/product-video) · 抓取日期 2026-08-12
> 定位:本文档是「分类骨架」,本节记录线上页面现状,用于发现并追踪**分类漂移**。

### 1. 页面结构(自上而下)

| 区块 | 内容 | 对应维度 |
|------|------|---------|
| Hero | H1「AI Product Video Maker」+ 产品图 | — |
| 上传框 | Upload product footage → Try For Free | — |
| Showcase | 4 帧 9:16 成片(Beauty / Unboxing / Lifestyle / Fashion) | 维度 2 示例 |
| Why Choose | 6 卡(Clone Styles / Auto Cuts / Auto Captions / Aspect Ratio / Batch Variants / No Skills) | 功能线(维度外) |
| **Types of Product Video** | 见下表(核心冲突区) | **维度 1 × 维度 2 混用** |
| Use Cases | 6 卡(Ecom Sellers / DTC / Agencies / UGC Creators / SaaS Marketers / SMB) | Persona 视角 |
| How It Works | 3 步(Upload → Pick Format or Reference → Export) | — |
| FeatureNav | Copy Style / Product Video / Gaming Video / Long to Short / AI Caption / AI Commentary / Video Resizer / Highlight Reels | 功能线 |
| FAQ | 6 条 | — |
| CTA | Turn your product footage into a finished video | — |

### 2. "Types of Product Video" 与维度 1(A 类)映射

| 编号 | 形态 | 页面状态 | 判定 |
|------|------|---------|------|
| F01 | Unboxing Video | 有卡片(TikTok · 15–45s · 9:16) | ✅ 对齐 |
| F02 | Product Demo Video | 有卡片(Landing · 30–60s · 16:9),且是页面主线 | ✅ 对齐 |
| F03 | Product Ad | 有卡片(Product Video Ad · Paid social · 6–30s) | ✅ 对齐 |
| F04 | Product Review Video | 有卡片但写成 **UGC Product Review** | ⚠️ 变形:加 UGC 定语混入创作者维度;测评不限于 UGC 形式 |
| F05 | Product Tutorial | 无 | ❌ 缺失 |
| F06 | E-commerce Product Video | 拆成「Amazon & Ecommerce Listings」放进行业组 | ❌ 错位:属维度 1 却占维度 2 位置 |

### 3. 页面多余、文档无编号的内容

| 卡片 | 判定 |
|------|------|
| Product Explainer Video | F05×F02 的混合;裸词意图偏「动画外包服务」,与素材重剪工具不匹配 → 建议不占独立形态位 |
| Product Launch Video | F03 的一个投放场景,非独立形态 → 建议并入 Product Ad |
| "By industry" 整组(Beauty / Fashion / Electronics / Home & Kitchen / SaaS) | 属维度 2,但**口径与本文档行业矩阵不一致**(见下) |
| SaaS & App Demos | 软件演示(F02 的软件变体),与实体产品视频不同源 |

### 4. 行业口径冲突(关键发现)

页面 "By industry & channel" 与本文档维度 2 是**两套行业体系**,不可混用:

| | 页面行业组 | 本文档维度 2 |
|---|---|---|
| 对象 | 消费品牌/电商品类(美妆、时尚、3C、家居、SaaS) | 本地商户服务(餐饮、美业、健康健身、房产、家居家政、宠物、汽车) |
| 素材来源 | 产品图/产品剪辑 | 门店、服务过程、店主 |
| 适用形态 | F01–F06 产品类 | F18–F21 为主,复用 A/B/C |
| 目标客户 | B2C 品牌市场部/电商运营 | B2B 本地商户主 |

**结论(2026-08-12 已拆分)**:页面行业组与文档维度 2 确认为**两套体系**。维度 2 已在[第二节](#二维度2行业industry矩阵)拆分为「消费品牌品类 C01–C06」(对应页面行业组,含 C05 扩展位)与「本地商户服务 B1–B7」(文档原有 7 行业)。页面行业组不应作为维度 1 的子分类与格式卡片混排在同一 H2 下;长尾 URL 分两条线 `/product-video/{品类}` 与 `/local-business-video/{行业}`。

### 5. 待定决策(2026-08-12 讨论中)

- [x] 落地页策略:按「形态×意图后缀」筛选建页,先跑 A 类验证再用数据定页数
- [x] 维度 2 拆分:文档层已完成(第二节,消费品牌品类 C01–C06 + 本地商户服务 B1–B7);**行业长尾页落地暂缓**,先专注形态层
- [x] A 类 6 形态工具意图验证 → **结论:建 4 个独立页**(Demo / Review / Ad / E-commerce),Unboxing 与 Tutorial 并入 section(详见 [sparki-keywords.md](./sparki-keywords.md) 第四节)
- [ ] 本地商户 P0 四行业(餐饮/美业/健康/房产)建页优先级
- [ ] 代码层:VideoTypes 卡片 href + `src/content/taxonomy.ts` 数据源化(taxonomy.ts 行业字段按第二节两子域结构实现)

---

*遵循 [客户文档规范](../demo/client-template.md)*
*关联：[主文档](./sparki.md) | [features](./sparki-features.md) | [creators](./sparki-creators.md)*
*Last updated: 2026-08-12*
*Demo 文档包 · Sparki · 剪辑视频类型多维分类*
