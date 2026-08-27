# Alignify · SEO 周报

Alignify 的 SEO 分析已从部署仓迁出，统一在本目录的 **周报引擎**。

## 凭据（只配一处）

文件：`scripts/.env`（从 `scripts/.env.example` 复制，**勿提交 Git**）

| 变量 | 必填 | 说明 |
|------|:---:|------|
| `GSC_SITE_URL` | ✅ | `https://alignify.co/`（须含尾斜杠） |
| `GSC_CLIENT_EMAIL` | ✅ | GCP 服务账号 |
| `GSC_PRIVATE_KEY` | ✅ | 私钥（含 `\n`） |
| `GA4_PROPERTY_ID` | ✅ | GA4 媒体资源 ID |
| `BING_SITE_URL` | Bing 时 ✅ | 通常同 GSC |
| `BING_API_KEY` | Bing 时 ✅ | 见下方「Bing 拉数」 |
| `REPORT_WEEK_END` | 可选 | 报告周周日，如 `2026-08-23` |

**Vercel / 部署仓可删除**（已无对应 API）：`GSC_CLIENT_EMAIL`、`GSC_PRIVATE_KEY`、`GA_PROPERTY_ID`、以及旧的 `config/gsc-key.json`。

部署仓若仍用 Indexing API，只需 `GOOGLE_INDEXING_KEY_FILE`（见部署仓 `.env.example`）。

## 拉数命令

```bash
cd seo-weekly-report/scripts
cp .env.example .env    # 首次：编辑凭据
npm install

npm run fetch-all       # GSC + GA4 + Bing（有 BING_API_KEY 时）+ merge
# 或单独：
npm run fetch-gsc
npm run fetch-ga4
npm run fetch-bing
npm run merge
```

产出：

- `data/gsc-weekly-{周日}.json`
- `data/ga4-weekly-{周日}.json`
- `data/bing-weekly-{周日}.json`（若跑了 Bing）
- `data/seo-report-bundle-{周日}.json` — **合并包，Agent 读这个**

## Bing 拉数

### 1. 获取 API Key

1. 打开 [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. 确认 **alignify.co** 已验证
3. **Settings → API Access → Generate API Key**
4. 写入 `scripts/.env`：

```env
BING_SITE_URL=https://alignify.co/
BING_API_KEY=你的-key
```

### 2. 运行

```bash
cd seo-weekly-report/scripts
npm run fetch-bing    # 仅 Bing → data/bing-weekly-*.json
# 或
npm run fetch-all     # GSC + GA4 + Bing + merge 一次完成
```

未设 `BING_API_KEY` 时，`fetch-all` 会**跳过 Bing** 但仍会 merge（bundle 里 `bing: null`）。

### 3. 验证

- 成功：控制台输出 `保存 → ../data/bing-weekly-YYYY-MM-DD.json ✓`
- 合并后：打开 `data/seo-report-bundle-*.json`，检查 `bing.overall`、`bing.pages`

### 4. 常见问题

| 现象 | 处理 |
|------|------|
| HTTP 401 | 重新 Generate API Key；确认站点已验证 |
| `bing: null` in bundle | 先 `npm run fetch-bing`，或 `.env` 缺 `BING_API_KEY` |
| 数据偏少 | Bing 更新约 **1 周**延迟，比 GSC 慢；看报告周是否选对（周日） |

详细 API 说明：`references/portable/api-setup.md` §3。

## 已从部署仓移除

`/dash`、`/api/gsc/*`、`/api/ga4/overview`、旧 `scripts/ops/fetch-*-data.mjs`。

## 审计脚本（Alignify 根目录）

```bash
node scripts/ops/audit-gsc-ctr.mjs
node scripts/ops/audit-gsc-position-drop.mjs
node scripts/ops/audit-gsc-index-health.mjs   # 读 scripts/.env 凭据
```

## 文档

- Agent 周报：[`SKILL.md`](./SKILL.md)
- API 逐步配置：[`references/portable/api-setup.md`](./references/portable/api-setup.md)
- 运维索引：[`../skills/ops/README.md`](../skills/ops/README.md)
