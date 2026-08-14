# OpenMart 关键词与目标页面映射

> 关联主文档：[openmart.md](./openmart.md) | 功能页：[openmart-features.md](./openmart-features.md) | Use Cases：[openmart-use-cases.md](./openmart-use-cases.md) | Solutions：[openmart-solutions.md](./openmart-solutions.md) | 竞品：[openmart-competitors.md](./openmart-competitors.md) | Database：[openmart-database.md](./openmart-database.md) | 基于 [sitemap](https://www.openmart.com/sitemap.xml)、GSC、竞品分析

---

## 1. 主关键词表（唯一完整来源）

| 意图 | 关键词 | 目标页 | 覆盖 | P |
|------|--------|--------|------|---|
| 获取 Google Maps 商户数据 | Google Maps scraper, scraping, extractor, data extraction, extract data from Google Maps, scrape for leads | /products/google-maps-scraper | ✅ | 0 |
| 获取 Google Maps 评论 | Google Maps reviews scraper | 同上 | ❌ | 1 |
| 获取 Google Maps 电话 | Google Maps phone number scraper | 同上 | ❌ | 1 |
| 获取 Google Maps 邮箱 | Google Maps email extractor | 同上或 owner-finder | ❌ | 1 |
| API 接入 | local business API, Google Places API alternative, business data API, get data not in official API | /products/local-business-api | ✅ | 0 |
| 查找决策者 | owner finder, find business owner email, local business email finder, business owner contact finder | /products/owner-finder | ✅ | 1 |
| 数据补充/验证 | data enrichment, contact enrichment, lead enrichment, firmographic enrichment, contact verification | /products/enrichments | ✅ | 1 |
| 批量导出 | download local business data, export Google Maps to CSV/Excel, bulk export | /products/download-local-business-data | ✅ | 1 |
| 监控新商户 | Google Maps monitoring, new business alerts, business listing monitoring | /products/monitoring | ✅ | 1 |
| Prospecting | SMB prospecting tool, local business lead finder, AI prospecting for SMB | /products/prospecting | ✅ | 1 |
| 竞品替代 | ZoomInfo alternative, Apollo alternative, OpenMart vs ZoomInfo/Apollo（✅）；Outscraper alternative, Apify alternative（❌） | /comparison/* | 部分 | 1 |
| 品类 database | {category} database, {category} leads（如 restaurant database, plumbers database） | /data/* | ✅ | 0 |
| 地域+品类 | {city} {category}（如 Atlanta bakery, Chicago plumber） | /database/* | ✅ | 1 |
| 用例 | lead generation, local business lead generation, SMB lead generation, B2B lead generation, lead qualification, SMB prospect list | /use-case/* | ✅ | 0 |
| 通用 | local business data, local business database, business contact database, local business leads, business lead generation | 首页、/data | ✅ | 0 |
| 工具选型 | best local business lead generation tool | 首页、博客 | ✅ | 1 |
| 集成 | Clay OpenMart, CRM local business data integration | /product-tutorials/* | ✅ | 2 |
| 品牌 | OpenMart, Openmart, OpenMart vs ZoomInfo, OpenMart vs Apollo | 全站、/comparison/* | ✅ | — |
| 地域 | local business data USA/Canada/Australia；local business leads California, business database Los Angeles, SMB leads New York | 首页、/database/* | ✅ | 1 |

**覆盖**：✅ 已覆盖 | ❌ 未覆盖 | 部分 = 部分已覆盖。API 页需补充 Google Places API alternative 说明。

---

## 2. 品类关键词表（/data/*）

> 完整品类数据、模板规范、内链规划见 [openmart-database.md](./openmart-database.md) §三、§四、§五。

| 品类 | 关键词 | URL |
|------|--------|-----|
| Bakery | bakery database, US bakery database, bakery contacts | /data/bakery |
| Cafe | cafe database, cafe leads | /data/cafe |
| Restaurants | restaurant database, restaurant leads | /data/restaurants |
| Grocery | grocery database | /data/grocery |
| Vegan | vegan restaurants database | /data/vegan |
| Dentists | dentists database, dentist contacts | /data/dentists |
| Nail salons | nail salons database | /data/nail-salons |
| Beauty salons | beauty salons database | /data/beauty-salons |
| Car repair | car repair database | /data/car-repair |
| Property management | property management database | /data/property-management |
| Tax prep | tax prep database | /data/tax-prep |
| Bookkeeping | bookkeeping database | /data/bookkeeping |

---

## 3. 待办（优先级）

| P | 待办 | 说明 |
|---|------|------|
| **0** | google-maps-scraper 页补充 reviews/phone/email 子功能 | 覆盖 reviews scraper、phone number scraper、email extractor |
| **0** | Local business lead generation 完整指南 | 博客/用例 |
| **1** | 新建 vs Outscraper、vs Apify 对比页 | 竞品替代词有搜索量 |
| **1** | local-business-api 页增加 Google Places API alternative | API 对比说明 |
| **1** | 强化 ZoomInfo/Apollo 对比页 | 展示高、CTR 低 |
| **1** | 扩展 /industry/* | real estate、private equity、retail |
| **2** | 博客 How-to 长尾 | how to scrape Google Maps、how to find business owner email |
| **2** | Clay/集成教程 | 已有页面加强布局 |

---

## 4. 不覆盖

| 关键词 | 说明 |
|--------|------|
| LinkedIn profiles scraper | 产品聚焦本地商户，非 LinkedIn |
| 纯消费端搜索（如 "hanks market"） | business.openmart.com 被动收录，非主动目标 |

---

## 5. URL 模式

| 类型 | 模式 | 示例 |
|------|------|------|
| 功能页 | /product/{feature} | google-maps-scraper, owner-finder, local-business-database |
| **Database 聚合** | **/data** | [openmart.com/data](https://www.openmart.com/data) |
| **品类页** | **/data/{category}** | /data/bakery, /data/cafe, /data/dentists |
| **地域+品类** | **/database/{city}-{category}** | /database/atlanta-bakery |
| 对比页 | /comparison/{slug} | openmart-vs-zoominfo |
| 用例页 | /use-case/{slug} | lead-generation |
| 案例页 | /case-study/{slug} | clipboard-health |
| 博客 | /blog | /blog |
