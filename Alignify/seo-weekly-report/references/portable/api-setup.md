# API 接入清单（人类操作）

按顺序完成。全部在本文件夹 `scripts/` 内配置，无需其他文档。

---

## 1. Google Search Console（GSC）

| 步骤 | 操作 |
|------|------|
| 1 | [Google Cloud Console](https://console.cloud.google.com/) 创建项目 |
| 2 | 启用 **Google Search Console API** |
| 3 | 凭据 → 服务账号 → 创建 JSON 密钥 |
| 4 | [Search Console](https://search.google.com/search-console) 添加 **URL 前缀** 属性 |
| 5 | 设置 → 用户 → 添加服务账号邮箱，权限 **Full** |
| 6 | 写入 `scripts/.env`：`GSC_SITE_URL`（须含尾斜杠，如 `https://example.com/`）、`GSC_CLIENT_EMAIL`、`GSC_PRIVATE_KEY` |

**注意**：GSC 日期为**太平洋时间**；数据延迟约 **2–3 天**。国内拉数可能需要 VPN 访问 Google OAuth 端点。

**核心 API**：`POST .../webmasters/v3/sites/{siteUrl}/searchAnalytics/query`

| 请求字段 | 说明 |
|----------|------|
| startDate, endDate | YYYY-MM-DD |
| dimensions | `page` `query` `country` `device` |
| rowLimit | 最大 25000，超出用 startRow 分页 |
| dataState | `final` |
| type | `web` |

| 响应字段 | 说明 |
|----------|------|
| rows[].keys | 维度值 |
| clicks, impressions, ctr, position | 指标 |

---

## 2. Google Analytics 4（GA4）

| 步骤 | 操作 |
|------|------|
| 1 | 同一 GCP 项目启用 **Google Analytics Data API** |
| 2 | GA4 Admin → Property access → 添加服务账号 **Viewer** |
| 3 | 记录 Property ID（纯数字） |
| 4 | 写入 `.env`：`GA4_PROPERTY_ID`、`GA4_CLIENT_EMAIL`、`GA4_PRIVATE_KEY`（可与 GSC 同账号，留空 GA4_* 则 fallback GSC_*） |

**核心 API**：`runReport` on `properties/{id}`

| 常用 dimension | 用途 |
|----------------|------|
| sessionDefaultChannelGroup | 渠道 |
| landingPage / pagePath | 落地页 |
| eventName | 事件 |
| date | 日趋势 |

| 常用 metric | 用途 |
|-------------|------|
| sessions, totalUsers, newUsers | 体量 |
| screenPageViews, engagedSessions | 参与 |
| eventCount | 转化事件 |

本包脚本对 **current 周 vs previous 周** 各跑一次 report（双 dateRange）。

---

## 3. Bing Webmaster Tools

| 步骤 | 操作 |
|------|------|
| 1 | [Bing Webmaster](https://www.bing.com/webmasters) 验证站点 |
| 2 | Settings → API Access → **Generate API Key** |
| 3 | 写入 `.env`：`BING_API_KEY`、`BING_SITE_URL` |

**端点**：`GET https://ssl.bing.com/webmaster/api.svc/json/{Method}?siteUrl=...&apikey=...`

| Method | 响应 `d[]` 主要字段 |
|--------|---------------------|
| GetPageStats | Query（实为 URL）, Clicks, Impressions, AvgImpressionPosition, Date |
| GetQueryStats | Query, Clicks, Impressions, AvgClickPosition, AvgImpressionPosition |
| GetCrawlIssues | Issue, URL, 等 |

**Date 格式**：`/Date(毫秒)/` — 脚本内已解析。Bing 按**周**返回多条，需按报告周聚合。

**SOAP/POX 已废弃**：仅用 `/json/` 路径。

---

## 4. 报告周

| 变量 | 说明 |
|------|------|
| `REPORT_WEEK_END` | YYYY-MM-DD，**必须是周日**；默认=上周日 |

周期：current = 该周 Mon–Sun；previous = 再上一周 Mon–Sun。

验证：`python tools/week_period.py --week-end 2026-08-23`

---

## 5. 首次跑通

```bash
cd scripts
cp .env.example .env
# 编辑 .env
npm install
npm run fetch-all
python ../tools/validate_bundle.py ../data/seo-report-bundle-*.json
```

失败时见 `SKILL.md` §11 故障排查。
