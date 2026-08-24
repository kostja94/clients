# Topic Cluster 文件布局 — Moras blog

> 本地 Markdown 按 cluster 子目录组织。**公开 URL 始终扁平**：`/blog/{slug}`，与文件是否在子目录无关。

## 子目录映射

| folder | Cluster | 示例路径 |
|--------|---------|----------|
| `creator-affiliate/` | A — Creator / Affiliate | `creator-affiliate/01-how-to-make-money-on-tiktok.md` |
| `tiktok-video/` | A + 格式 Spoke | `tiktok-video/03-tiktok-shop-videos-without-filming.md` |
| `content-discovery/` | C — Content & Discovery | `content-discovery/26-how-the-tiktok-algorithm-works.md` |
| `platform-ops/` | B — Platform Ops | `platform-ops/10-tiktok-shop-customer-service.md` |
| `seasonal-campaign/` | F — Seasonal / Campaign | `seasonal-campaign/59-tiktok-shop-sales-calendar.md` |
| *(root)* | D — E-commerce AI | `31-ai-commerce-agent-ecommerce.md` |

## 规则

- **NN 全局递增**，不按子目录重置
- frontmatter `slug` = `/blog/{url-slug}`，**不含**子目录名
- 内链永远 `/blog/{slug}`，禁止 `/blog/creator-affiliate/...`
- Phase 2 路径：`moras/blog/{folder}NN-{slug}.md` 或 `moras/blog/NN-{slug}.md`（Cluster D）

详见 `content-graph.md` §1B Cluster 注册表。

*topic-cluster-layout · v1.0 · moras · 2026-08-24*
