## §12 证据链与引用标准

### 12.1 引用分级

| 级别 | 触发条件 | 要求 |
|------|---------|------|
| **P0 必须引用** | 客户案例指标、能力页统计、第三方市场数字 | 链 `/customers/{slug}` 或 capability 页或原始报告 URL |
| **P1 应当引用** | 竞品能力/定价、行业趋势、平台政策 | 官方 docs/官网 + `as of {month} {year}` |
| **P2 可不引用** | 框架逻辑推演、内部 benchmark | 注明 "based on internal analysis" 或方法论限定 |

### 12.2 B2B 案例引用格式（P0）

> Final Round AI reached [$12M ARR in 14 months with 4.2× ROAS improvement](https://www.hellyeahai.com/customers/final-round-ai), per Hellyeah's published case study. Results vary by category, spend level, and baseline performance.

**硬规则**：
- 单案例不得写成 "typical" 或 "you will achieve"
- 多案例并列时每个指标各自链案例页
- 首页卡片数字 = 案例页数字，精度一致

### 12.3 能力页统计引用（P1）

> Hellyeah's performance marketing capability page cites an average **3.2× ROAS** improvement among customers using its optimization workflows — [see the capability page](https://www.hellyeahai.com/capabilities/performance-marketing) for context and scope.

### 12.4 竞品引用（P1）

> [Cometly's AI Ads Manager](https://www.cometly.com/features/ads-manager) emphasizes unified ad views and in-platform budget adjustments across Meta, Google, TikTok, and other networks, as of June 2026.

竞品链接：`rel="nofollow noopener"` HTML 或 Markdown 外链。

### 12.5 合规/Trust 引用（P1）

> Hellyeah lists **SOC 2 certification as in flight** on its AIMA product page — not as a completed Type II attestation. Enterprise buyers should verify current status on the [Trust Center](/security).

### 12.6 反模式

| 反模式 | 修复 |
|--------|------|
| 裸引 3.2× ROAS 无链 | 链 capability 页 |
| "studies show" 泛引 | 具体来源或删 |
| 案例 GMV/ROAS 作保证 | 加 "results vary" + 链案例 |
| SOC 2 Type II certified | SOC 2 in flight |
| 锚文本 "click here" | 语义化锚文本 |

### 12.7 Source Map 模板（Phase 5 内部留存）

```markdown
## Source Map
| Claim | § | Source | Checked | Confidence |
|------|------|------|------|:---:|
| Final Round AI $12M ARR | §4 | /customers/final-round-ai | 2026-06-15 | High |
| 3.2× ROAS avg | §6 | /capabilities/performance-marketing | 2026-06-15 | Medium |
| Cometly unified ad view | §3 | cometly.com/features/ads-manager | 2026-06-15 | High |
```

Confidence: High = 官网一手 / Medium = 能力页宣称+产品确认 / Low = 单案例。**Low 不得支撑核心论证。**

### 12.8 跨篇数字一致性

同一数字跨篇出现须：
- 每篇都给引用链接
- 精度一致（$12M ARR vs $12 million ARR → 统一）
- Canonical 最完整上下文在 Pillar 或 capability 页
