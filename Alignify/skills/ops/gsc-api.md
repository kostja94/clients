# Google Search Console / GA4 数据接入

> **2026-08-28 起**：GSC / GA4 不再通过部署仓 API Route 暴露。所有拉数在上下文仓 [`seo-weekly-report/`](../../seo-weekly-report/README.md) 完成，直连 Google API。

---

## 入口

| 任务 | 位置 |
|------|------|
| 配置凭据 | `seo-weekly-report/scripts/.env`（见 `.env.example`） |
| 拉数 + 合并 | `cd seo-weekly-report/scripts && npm run fetch-all` |
| API 逐步配置 | [`seo-weekly-report/references/portable/api-setup.md`](../../seo-weekly-report/references/portable/api-setup.md) |
| 周报生成 | [`seo-weekly-report/SKILL.md`](../../seo-weekly-report/SKILL.md) |
| 索引健康检查 | `node scripts/ops/audit-gsc-index-health.mjs` |
| CTR / 排名审计 | `scripts/ops/audit-gsc-ctr.mjs`、`audit-gsc-position-drop.mjs` |

---

## 环境变量（`seo-weekly-report/scripts/.env`）

| Key | 用途 |
|-----|------|
| `GSC_SITE_URL` | Search Console 属性 URL，如 `https://alignify.co/` |
| `GSC_CLIENT_EMAIL` | GCP 服务账号邮箱 |
| `GSC_PRIVATE_KEY` | 服务账号私钥 |
| `GA4_PROPERTY_ID` | GA4 媒体资源 ID |
| `BING_SITE_URL` / `BING_API_KEY` | Bing Webmaster（可选） |

---

## GCP 配置快照

| 项目 | 值 |
|------|----|
| GCP 项目 ID | `crypto-reality-485804-j5` |
| 服务账号 | `zyjstc@crypto-reality-485804-j5.iam.gserviceaccount.com` |
| 已启用 API | Search Console API、Google Analytics Data API |
| Search Console 属性 | `https://alignify.co/`（URL 前缀，Full 权限） |

---

## 部署仓保留项

部署仓 **仅保留** Google **Indexing API**（`npm run google-index`），用于向 Google 提交 URL 更新通知。与 GSC 绩效拉数无关。

| 文件 | 说明 |
|------|------|
| `src/lib/google-indexing.ts` | Indexing API 客户端 |
| `scripts/permanent/submit-to-google-index.ts` | 单 URL / 批量提交 |

Indexing 凭据：`GOOGLE_INDEXING_KEY_FILE`（见部署仓 `.env.example`）。

---

## 已知限制

- **国内需 VPN**：直连 `oauth2.googleapis.com` / Google API 时
- **GSC 数据延迟**：约 2–3 天
- **Search Analytics 匿名过滤**：按 query 分组合计低于无维度汇总

Indexing 凭据：`GOOGLE_INDEXING_KEY_FILE`（见部署仓 `.env.example`）。

**Vercel 可删**：`GSC_CLIENT_EMAIL`、`GSC_PRIVATE_KEY`、`GA_PROPERTY_ID`（已无 `/api/gsc/*`、`/api/ga4/*`）。

---

## 变更记录

| 日期 | 内容 |
|------|------|
| 2026-05-09 | 初始：部署仓 `/api/gsc/*` 三端点 |
| 2026-08-28 | 移除部署仓 GSC/GA4 API Route；统一迁至 `seo-weekly-report/` |
