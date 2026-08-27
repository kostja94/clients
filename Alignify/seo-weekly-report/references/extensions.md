# 扩展模块（预留）

本包 **v1.0** 未实现下列能力，schema 已留 `extensions` 占位。接入时扩展 merge 脚本与 SKILL 章节即可。

---

## §1 Paid Ads 流量

**目标**：Google Ads / Meta 花费、转化与 SEO 自然量分开看。

| 待接入 | 说明 |
|--------|------|
| Google Ads API | campaign / ad group 级 metrics |
| 落地页 | final URL → 与 `ga4.topPages.path` join |
| UTM | `utm_medium=cpc` 与 Ads auto-tagging 对账 |

**bundle 占位**：

```json
"extensions": {
  "paidAds": {
    "enabled": false,
    "campaigns": [],
    "spend": null,
    "conversions": null
  }
}
```

---

## §2 Social 自然 / 付费社交

**目标**：Organic Social 渠道 + 各平台 UTM 拆解。

| 待接入 | 说明 |
|--------|------|
| GA4 | sessionSource + sessionMedium 过滤 social |
| 手动 | `===SOCIAL===` 块（未建模板，可复制 OBSERVATIONS） |

---

## §3 落地页 × 转化映射

**目标**：哪些 landing path 带来 signup / purchase。

| 待接入 | 说明 |
|--------|------|
| GA4 | landingPage × eventName 透视 |
| 首触字段 | 注册时固化 first_landing_path（需产品埋点） |

**bundle 占位**：`extensions.landingConversionMap[]`

---

## §4 外链 registry 自动对账

**目标**：`backlink-registry.yaml` × GA4 Referral 自动匹配。

| 待接入 | 说明 |
|--------|------|
| registry | 域名 / utm / referrer 规则 |
| 三级匹配 | referrer → domain → utm |

当前仅 `===BACKLINKS===` 手动块。

---

## §5 看板（WorkBuddy 等）

**原则**：本包只保证 `seo-report-bundle-*.json` 结构稳定。

建议看板读取：

- `period`、`gsc.overall`、`ga4.channels`、`healthCheck`
- 不做复杂 UI 逻辑在本 repo

---

## §6 GSC Gen AI / Bing AI Performance

**现状**：官方 **无稳定公开 API** 或仅 Dashboard CSV。

报告 §6 可粘贴 CSV 摘要；勿写入 bundle  pretending API 数据。
