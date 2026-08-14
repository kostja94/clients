# §12 证据链与引用格式

## 引用分级

| 级别 | 定义 | 用途 |
|------|------|------|
| **P0** | 官网/官方文档/官方定价（qveris.ai、/docs、/pricing、/whats-new） | 产品能力、定价、版本、协议的核心 claim |
| **P1** | 权威第三方（交易所官网、数据源官方、监管公告） | 市场数据、竞品能力、行业事实 |
| **P2** | 行业媒体/博客 | 趋势背景，不作核心论证 |
| **内部** | 实测/内部数据 | 必须标注 n + 时间窗 + 方法（F3） |

## 引用格式

| 场景 | 格式 |
|------|------|
| 站内 | `[锚文本](/blog/{slug})` / `[锚文本](/guides/{slug}/)` |
| 站外权威 | `[Source: URL]` 或 markdown 链接 |
| 竞品/数据源 | HTML：`<a href="URL" rel="nofollow noopener">锚文本</a>` |
| 脚注 | 文章末尾 `---` 后 `## References`（可选，金融文推荐） |

## 数字声明规则

- **P0 级**：10,000+ capabilities、99.99% uptime、credits 成本、定价、版本号 → 必须有来源
- **P1 级**：行情价格、竞品订阅价 → 来源 + `as of {date}`（估算另注）
- **内部实测**：`based on internal analysis, n≈X` / `QVeris Data Test — data retrieved in real time through the QVeris capability routing network`
- **禁止**：无来源精确报价、无来源市场份额、无来源搜索量

## Source Map 模板（Phase 5 输出）

```markdown
| Claim | § | Source | Checked | Confidence |
|-------|----|--------|---------|:---:|
| 10,000+ capabilities | §1 | qveris.ai homepage | 2026-08-05 | High |
| MCP v0.13.0 | §2 | /ecosystem | 2026-08-05 | High |
| Seres closed ¥79.05, -2.66% | §3 | cn_financial_pro via QVeris | 2026-06-03 | High |
| Vendor X costs $99/mo | §4 | vendor pricing page (estimate) | 2026-07-24 | Med |
```

## Confidence 判定

| 级别 | 判定 |
|------|------|
| **High** | 官方来源直接可查 |
| **Med** | 权威第三方但需交叉验证 |
| **Low** | 传闻/推测 → 不得支撑核心论证（G3） |
