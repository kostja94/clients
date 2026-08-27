# 指标释义（GA4 周报常用）

| 指标 | 含义 | 周报用途 |
|------|------|----------|
| sessions | 会话数 | 与 GSC 点击量级对照 |
| totalUsers | 活跃用户 | 周环比体量 |
| engagedSessions | 参与会话 | 质量 proxy |
| screenPageViews | 页面浏览 | 落地页热度 |
| bounceRate | 非参与会话占比 | 单页落地结合意图解读 |
| eventCount | 事件次数 | Key events 转化 |

---

## 渠道（sessionDefaultChannelGroup）

| 渠道 | 说明 |
|------|------|
| Organic Search | 自然搜索 |
| Direct | 直接访问（含 not set 污染） |
| Referral | 外链引荐 |
| Paid Search | 付费搜索 |
| Organic Social | 自然社交 |
| AI Assistant | GA4 2026+ 默认识别 AI 引荐 |

---

## GSC 字段

| 字段 | 说明 |
|------|------|
| clicks | 搜索结果点击 |
| impressions | 展示 |
| ctr | clicks/impressions |
| position | 平均排名（越低越好） |

---

## 交叉视图

**搜索占比（页级）** ≈ GSC page clicks / GA4 landing sessions（同 path）

仅作方向参考，分母分子定义不同。
