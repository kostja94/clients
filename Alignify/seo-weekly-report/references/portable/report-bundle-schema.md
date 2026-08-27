# report-bundle JSON Schema v1.0.0

文件命名：`data/seo-report-bundle-{YYYY-MM-DD}.json`（日期 = current 周周日）

---

## 顶层

| 字段 | 类型 | 说明 |
|------|------|------|
| schemaVersion | string | `"1.0.0"` |
| source | string | `api-auto` \| `manual` |
| fetchedAt | ISO8601 | 合并时间 |
| project.id | string | 来自 project-config |
| period.current / previous | {start,end} | YYYY-MM-DD |
| gsc | object \| null | GSC 块 |
| ga4 | object \| null | GA4 块 |
| bing | object \| null | Bing 块 |
| content | object | 可选 catalog |
| supplements | object | 预留 + 手动块解析结果 |
| extensions | object | **预留** Ads/Social（见 extensions.md） |
| healthCheck | object | D0–D5 |

---

## gsc

```json
{
  "overall": { "clicks", "impressions", "ctr", "avgPosition" },
  "overallPrev": { "..." },
  "overallChange": { "clicksPct", "impressionsPct" },
  "branded": { "clicks", "impressions", "share" },
  "nonBranded": { "clicks", "impressions", "share" },
  "pages": [{ "url", "clicks", "impressions", "ctr", "position", "clicksPrev", "..." }],
  "queries": [{ "query", "clicks", "isBranded", "..." }],
  "countries": [],
  "devices": []
}
```

---

## ga4

```json
{
  "overall": { "sessions", "totalUsers", "screenPageViews", "engagedSessions" },
  "overallPrev": { "..." },
  "organicSearch": { "sessions", "sessionsPrev" },
  "channels": [{ "channel", "sessions", "sessionsPrev", "screenPageViews" }],
  "topPages": [{ "path", "pageType", "sessions", "sessionsPrev" }],
  "events": [{ "eventName", "eventCount", "eventCountPrev" }],
  "aiAssistant": { "sessions", "sessionsPrev", "sources": [] }
}
```

`aiAssistant`：当渠道含 `AI Assistant` 或 project-config 配置 regex 时填充。

---

## bing

```json
{
  "overall": { "clicks", "impressions", "ctr", "avgPosition" },
  "overallPrev": { "..." },
  "pages": [],
  "queries": [],
  "crawlIssuesCount": 0
}
```

---

## healthCheck

| 键 | 含义 |
|----|------|
| d0_dataSource | api-auto / partial / manual |
| d1_periodAligned | 周期是否 Mon–Sun 对齐 |
| d2_gscDimensionsComplete | pages, queries, countries, devices 是否均有数据 |
| d3_ga4Present | bool |
| d3_bingPresent | bool |
| d4_pageOverlapRate | GSC page path 与 GA4 topPages path 交集比例 |
| d5_magnitudeReasonable | GSC 点击是否在 project-config.health 区间 |

Agent 生成报告时**必须先读 healthCheck**，异常须在文首标注。

---

## supplements（预留）

```json
{
  "manualBlocksParsed": false,
  "backlinksTracked": [],
  "weeklyContent": []
}
```

手动块由 Agent 读 `templates/` 文本，不必写入 JSON；若需程序化可后续扩展 parser。

---

## extensions（空对象占位）

```json
{
  "paidAds": null,
  "social": null,
  "landingConversionMap": null
}
```

见 `references/extensions.md`。
