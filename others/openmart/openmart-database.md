# OpenMart Database 专用文档

> **SEO 流量主驱动板块**：独立文档，驱动 local business database、{category} database、{city} {category} 等核心关键词  
> 关联：[openmart.md](./openmart.md) | [openmart-features.md](./openmart-features.md) | [openmart-solutions.md](./openmart-solutions.md) | [openmart-keywords.md](./openmart-keywords.md)

**定位**：Database 是 OpenMart 主要 SEO 流量来源，需单独规划、执行、优化。本文档集中该板块的页面结构、品类数据、程序化 SEO、内链与待办。

---

## 〇、板块概览

| 项目 | 内容 |
|------|------|
| **核心关键词** | local business database, {category} database, {city} {category}, business contact database |
| **聚合页** | [/data](https://www.openmart.com/data) — All local business categories |
| **品类详情页** | /data/{category} — 如 /data/bakery、/data/dentists |
| **地域+品类页** | /database/{city}-{category} — 如 /database/atlanta-bakery |
| **程序化** | 300+ 品类单页 + 地域×品类组合 |
| **SEO 价值** | 高——主流量驱动；多长尾（restaurant database、Atlanta plumber、dentist leads） |

---

## 一、URL 模式与页面层级

| 层级 | URL 模式 | 示例 | 目标关键词 |
|------|----------|------|------------|
| **聚合 Hub** | /data | [openmart.com/data](https://www.openmart.com/data) | local business database, business categories |
| **品类详情** | /data/{category} | /data/bakery, /data/dentists, /data/car-repair | bakery database, dentists database, dentist leads |
| **地域+品类** | /database/{city}-{category} | /database/atlanta-bakery, /database/chicago-plumber | Atlanta bakery, Chicago plumber |

**URL 规范**：小写、连字符；slug 与目标关键词一致（如 restaurant database → /data/restaurants）。

---

## 二、核心关键词

### 2.1 主关键词

| 类型 | 关键词 | 目标页 | 优先级 |
|------|--------|--------|--------|
| **核心** | local business database, business contact database | 首页、/data、/product/local-business-database | P0 |
| **核心** | {category} database, {category} leads | /data/{category} | P0 |
| **长尾** | {city} {category}, {city} {category} database | /database/{city}-{category} | P1 |
| **长尾** | US {category} database, {category} contacts | /data/{category} | P1 |

### 2.2 品类关键词模式

| 模式 | 示例 | 目标页 |
|------|------|--------|
| {category} database | restaurant database, dentist database | /data/restaurants, /data/dentists |
| {category} leads | bakery leads, plumber leads | /data/bakery, /data/plumbers |
| {category} contacts | cafe contacts, nail salon contacts | /data/cafe, /data/nail-salons |
| US {category} database | US bakery database | /data/bakery |
| {city} {category} | Atlanta bakery, Chicago plumber | /database/atlanta-bakery, /database/chicago-plumber |

---

## 三、品类数据（Programmatic SEO 数据源）

> **数据来源**：[Openmart Data](https://www.openmart.com/data) 聚合页、官网导航、竞品品类覆盖。

### 3.1 行业分组与品类（含记录数）

| 行业 | 品类 | 记录数 | URL | 目标关键词 |
|------|------|--------|-----|------------|
| **Food & Beverage** | bakery | 50K+ | /data/bakery | bakery database, bakery leads |
| | burger shop | 187K | /data/burger-shop | burger shop database |
| | cafe | 55K | /data/cafe | cafe database, cafe leads |
| | grocery | 30K | /data/grocery | grocery database |
| | ice cream shop | 72K | /data/ice-cream-shop | ice cream shop database |
| | restaurants | 307K | /data/restaurants | restaurant database, restaurant leads |
| | vegan | 40K | /data/vegan | vegan restaurant database |
| | tea | — | /data/tea | tea shop database |
| **Personal Care** | beauty salons | 153K | /data/beauty-salons | beauty salon database |
| | nail salons | 38K | /data/nail-salons | nail salon database |
| **Health & Medical** | dentists | 140K | /data/dentists | dentist database, dentist leads |
| | dermatologists | 117K | /data/dermatologists | dermatologist database |
| | doctors | 169K | /data/doctors | doctor database |
| | orthodontist | 22K | /data/orthodontist | orthodontist database |
| **Automotive & Transportation** | car dealer | 68K | /data/car-dealer | car dealer database |
| | car repair | 139K | /data/car-repair | car repair database |
| | fleet maintenance | 115K | /data/fleet-maintenance | fleet maintenance database |
| | trucking companies | 81K | /data/trucking-companies | trucking database |
| **Home & Local Services** | heating and cooling | 61K | /data/heating-and-cooling | HVAC database |
| | landscapers | 112K | /data/landscapers | landscaper database |
| | pest control | 18K | /data/pest-control | pest control database |
| | property management | 221K | /data/property-management | property management database |
| | waste management | 35K | /data/waste-management | waste management database |
| **Professional Services** | bank | 40K | /data/bank | bank database |
| | bookkeeping | 75K | /data/bookkeeping | bookkeeping database |
| | tax prep | 75K | /data/tax-prep | tax prep database |

### 3.2 字母索引品类（来自 /data 聚合页）

> 聚合页按 A–O 等字母分组展示 300+ 品类，以下为部分示例，完整列表需从官网抓取或 API 获取。

| 字母 | 品类示例 |
|------|----------|
| A | ATM, Accountant, Addiction treatment center, Adoption agency |
| B | Bail bonds service, Band, Bar, Barbers School, Beautician, Beauty Salon |
| C | Cafe, Car dealer, Car repair, Dentists, Dermatologists |
| D | Doctors, Orthodontist |
| … | 300+ 品类 |

**扩展建议**：新建品类页时，优先覆盖 openmart-keywords.md §2 已列品类；其次按搜索量扩展（restaurant、plumber、dentist、bakery、cafe 等）。

### 3.3 详情页「You may also be interested in」关联逻辑

| 当前页 | 推荐关联品类（同行业或高相关） |
|--------|------------------------------|
| bakery | cafe, grocery, vegan, property management, dentists, nail salons, tax prep, tea, car repair |
| cafe | bakery, restaurants, grocery, tea |
| dentists | dermatologists, doctors, orthodontist, nail salons, beauty salons |
| car repair | car dealer, fleet maintenance, trucking |

---

## 四、详情页模板规范

### 4.1 页面结构（以 /data/bakery 为例）

| 区块 | 内容要点 |
|------|----------|
| **H1** | Complete US {category} database & intelligence |
| **Hero** | 记录数、准确率、数据点数、更新频率 |
| **Challenges** | 3–4 个行业痛点（决策者难触达、数据过时、资质数据缺失等） |
| **Data points** | 50+ 数据点列表（基础 + 增强） |
| **Who benefits** | 4–6 个买家角色（如 Food & beverage distributors、POS & payment systems、Marketing agencies） |
| **Case study** | 1 个行业相关案例（含数据：转化率、销售周期、收入） |
| **FAQ** | 5–6 个品类相关 FAQ |
| **Related** | You may also be interested in — 8–10 个关联品类 |

### 4.2 关键词布局

| 位置 | 规则 |
|------|------|
| Title | {Category} business database with verified contacts \| Openmart |
| H1 | Complete US {category} database & intelligence |
| 首段 | 含 {category} database、{category} leads、decision-maker、verified |
| 内链 | 链至 /data（聚合）、/product/local-business-database、相关品类页 |

### 4.3 待修复

- **拼写**：/data/bakery 页 CTA「Get backery data」→「Get bakery data」

---

## 五、内链规划

```
/product/local-business-database（产品页）
  └── 链至 /data（浏览入口）

/data（聚合 Hub）
  ├── 字母索引 → 品类详情页
  ├── 行业分组区块 → 品类详情页
  └── CTA → 注册、Book demo

/data/{category}（品类详情）
  ├── 链至 /data（返回浏览）
  ├── 链至 /product/local-business-database
  ├── You may also be interested in → 8–10 关联品类
  └── 链至 /database/{city}-{category}（若有地域页）

首页、Solutions、Use Cases → /data、/product/local-business-database
```

---

## 六、SEO 待办（Database 板块）

| 优先级 | 动作 |
|--------|------|
| **P0** | 聚合页 /data 强化 local business database、300+ business types |
| **P0** | 修复 /data/bakery 拼写「backery」→「bakery」 |
| **P1** | 品类详情页统一模板：Challenges、Who benefits、FAQ 需品类定制 |
| **P1** | 扩展品类页至 openmart-keywords.md 未覆盖高搜索量品类 |
| **P1** | 地域+品类页 /database/* 批量建页或程序化 |
| **P2** | 聚合页字母索引完整展示 300+ 品类 |
| **P2** | 品类页结构化数据（LocalBusiness、FAQPage） |
| **P2** | 博客长尾：best {category} database、how to find {category} leads |

---

## 七、与主文档关联

| 文档 | 关联内容 |
|------|----------|
| 主文档 | openmart.md §4 网站结构、§6 优化建议 — Database 引用本文档 |
| 关键词 | openmart-keywords.md §2 品类关键词表 — 品类扩展见本文档 §三 |
| 产品页 | /product/local-business-database — 链至 /data、品类页 |

---

**Last updated**：2025-03-02
