# OpenMart Features 功能页总结

> 关联：[openmart.md](./openmart.md) | [openmart-database.md](./openmart-database.md) | [openmart-use-cases.md](./openmart-use-cases.md) | [openmart-solutions.md](./openmart-solutions.md) | [openmart-competitors.md](./openmart-competitors.md) | [openmart-keywords.md](./openmart-keywords.md)

**Features 与 Use Cases、Solutions 严格区分**（基于 skills：features-page-generator、use-cases-page-generator、solutions-page-generator）：

| 类型 | 回答的问题 | 聚焦 | 示例 |
|------|------------|------|------|
| **Features** | 产品**能做什么**？ | Capabilities（能力） | 本文档 |
| **Use Cases** | **谁**在**什么情境**下用？ | Scenarios、Personas | Lead Generation、Lead Qualification → [openmart-use-cases.md](./openmart-use-cases.md) |
| **Solutions** | 该**行业**能获得什么**业务结果**？ | Business value、ROI | Real estate、Private equity → [openmart-solutions.md](./openmart-solutions.md) |

---

## 一、功能概览与价值评估

| 功能 | 核心/非核心 | 目标关键词 | 价值评估 | 说明 |
|------|-------------|------------|----------|------|
| **Google Maps Scraper** | 核心 | Google Maps scraper, scraping, extractor | **高** | 抓取商户数据、reviews、phone、email；导出 CSV/XLSX |
| **Local Business Database** | **核心** | local business database, {category} database | **高** | 200M+ 预验证记录，300+ 品类；/data、/data/{category}；见 [openmart-database.md](./openmart-database.md) |
| **Local Business API** | 核心 | local business API, Google Places API alternative | **高** | RESTful API，实时数据，替代 Google Places API |
| **Owner Finder** | 核心 | owner finder, find business owner email | **高** | 决策者联系方式，邮箱/电话验证 |
| **Data Enrichment** | 核心 | data enrichment, contact enrichment, lead enrichment | **高** | 40+ 字段补充、验证 |
| **Download** | 核心 | download local business data, export to CSV/Excel | **高** | 批量导出/下载 |
| **Monitoring** | 核心 | Google Maps monitoring, new business alerts | **中** | 监控新商户/变更 |
| **Prospecting** | 核心 | SMB prospecting tool, AI prospecting | **中** | AI 驱动获客、lead finder |

### 竞品功能重叠（SEO 差异化参考）

| 功能 | OpenMart | ZoomInfo | Apollo | Outscraper |
|------|----------|----------|--------|------------|
| 本地商户数据 | ✅ 200M+ | 弱 | 弱 | 抓取为主 |
| 预建数据库 | ✅ 300+ 品类 | 企业级 | 企业级 | — |
| 决策者联系人 | ✅ | ✅ | ✅ | 有限 |
| Google Maps 抓取 | ✅ | — | — | ✅ |
| API | ✅ | ✅ | ✅ | ✅ |
| 定价起点 | $149 | 高 | 中 | $3/1K |

*竞品核心关键词、功能详见 [openmart-competitors.md](./openmart-competitors.md)。*

---

## 二、功能关键词汇总

### 2.1 Google Maps Scraper

| 类型 | 关键词 |
|------|--------|
| 核心 | **Google Maps scraper**, **scraping**, **extractor** |
| 扩展 | data extraction, extract data from Google Maps, scrape for leads |
| **待覆盖** | Google Maps reviews scraper, phone number scraper, email extractor |

### 2.2 Local Business Database

| 类型 | 关键词 |
|------|--------|
| 核心 | **local business database**, **business contact database** |
| 扩展 | {category} database, {category} leads（restaurant database, bakery leads） |
| **长尾** | US {category} database, {city} {category} |

*完整品类关键词见 [openmart-database.md](./openmart-database.md) §二。*

### 2.3 Local Business API

| 类型 | 关键词 |
|------|--------|
| 核心 | **local business API**, **Google Places API alternative** |
| 扩展 | business data API, get data not in official API |

### 2.4 Owner Finder / Enrichment / Download / Monitoring / Prospecting

| 功能 | 核心关键词 |
|------|------------|
| Owner Finder | owner finder, find business owner email, local business email finder |
| Enrichment | data enrichment, contact enrichment, lead enrichment, contact verification |
| Download | download local business data, export Google Maps to CSV/Excel, bulk export |
| Monitoring | Google Maps monitoring, new business alerts, business listing monitoring |
| Prospecting | SMB prospecting tool, local business lead finder, AI prospecting for SMB |

---

## 三、功能页内容摘要

### 1. Google Maps Scraper | /product/google-maps-scraper

**目标关键词**：Google Maps scraper, scraping, extractor

**核心卖点**：
- **商户数据**：名称、地址、电话、邮箱、网站、类别、经纬度、营业时间、Place ID
- **评论与评分**：reviews、ratings（待补充子功能说明）
- **导出**：CSV、XLSX
- **覆盖**：200+ 国家、500+ 行业类别

**待办**：补充 reviews scraper、phone number scraper、email extractor 子功能说明。

---

### 2. Local Business Database | /product/local-business-database

**目标关键词**：local business database, business contact database

**核心卖点**：
- **200M+ 记录**：预验证，97–99% 准确率
- **300+ 品类**：按行业、地域筛选
- **40+ 数据点**：基础 + 增强（决策者、收入估算、技术栈等）
- **入口**：[/data](https://www.openmart.com/data) 聚合；/data/{category} 品类详情

*详情见 [openmart-database.md](./openmart-database.md)。*

---

### 3. Local Business API | /product/local-business-api

**目标关键词**：local business API, Google Places API alternative

**核心卖点**：
- **RESTful API**：实时数据
- **Google Places API alternative**：获取官方 API 未覆盖的数据
- **集成**：HubSpot、Salesforce、Clay

**待办**：增加 Google Places API alternative 对比说明。

---

### 4. Owner Finder | /product/owner-finder

**目标关键词**：owner finder, find business owner email

**核心卖点**：
- **决策者**：owner names、direct phone、verified email
- **多源**：网站、税务记录、评论等，非仅 LinkedIn
- **验证**：邮箱/电话实时验证

---

### 5. Data Enrichment | /product/data-enrichment

**目标关键词**：data enrichment, contact enrichment, lead enrichment

**核心卖点**：
- **40+ 字段**：收入估算、员工规模、技术栈、广告支出信号
- **验证**：contact verification、firmographic enrichment

---

### 6. Download | /product/download-local-business-data

**目标关键词**：download local business data, export to CSV/Excel

**核心卖点**：
- **批量导出**：Starter 100K、Pro 200K、Scale 更高
- **格式**：CSV、Excel
- **集成**：CRM、营销自动化

---

### 7. Monitoring | /product/monitoring

**目标关键词**：Google Maps monitoring, new business alerts

**核心卖点**：
- **新商户**：new business alerts
- **变更**：business listing monitoring
- **Scale 计划**：新开业/趋势发现

---

### 8. Prospecting | /product/prospecting

**目标关键词**：SMB prospecting tool, local business lead finder

**核心卖点**：
- **AI 驱动**：AI prospecting for SMB
- **高意图**：Smart Prospecting、Buying intent data
- **自动化**：发现、评分、触达

---

## 四、URL 与内链

| 功能 | URL | 内链至 |
|------|-----|--------|
| Google Maps Scraper | /product/google-maps-scraper | /data、Owner Finder |
| Local Business Database | /product/local-business-database | /data（聚合）、品类页 |
| Local Business API | /product/local-business-api | /data、Database |
| Owner Finder | /product/owner-finder | /data、Enrichment |
| Data Enrichment | /product/data-enrichment | Owner Finder、Download |
| Download | /product/download-local-business-data | /data、Database |
| Monitoring | /product/monitoring | /data、Prospecting |
| Prospecting | /product/prospecting | /data、Use cases |

---

## 五、与主文档关联

| 文档 | 关联内容 |
|------|----------|
| 主文档 | openmart.md §1 产品信息 — 功能页 URL 见本文档 |
| 关键词 | openmart-keywords.md — 功能页 URL 见本文档 §四 |
| Database | openmart-database.md — Local Business Database 产品页链至 /data |
| Use Cases | openmart-use-cases.md — 各 Use Case 内链至功能页 |
| Solutions | openmart-solutions.md — 行业方案调用 Features |
| 竞品 | openmart-competitors.md — 功能对比见本文档 §一 |

---

**Last updated**：2025-03-02
