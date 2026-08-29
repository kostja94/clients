# Nova Scientia 运维脚本

脚本读写**部署仓** `E:\自有部署项目\nova-scientia-main` 的 `content/`、`public/`、`config/`。路径解析见 `lib/deploy-root.js`。

在**部署仓根目录**执行：

```powershell
cd E:\自有部署项目\nova-scientia-main
```

## audit/

| 命令 | 说明 |
|------|------|
| `node ..\..\clients\Nova-Scientia\scripts\audit\audit-seo-meta.js` | SEO title/description 长度审计 |
| `node ..\..\clients\Nova-Scientia\scripts\audit\audit-product-tags.js` | Hero tag 覆盖率 |
| `npx tsx ..\..\clients\Nova-Scientia\scripts\audit\simulate-product-categories.ts` | 分类映射 dry-run |
| `python ..\..\clients\Nova-Scientia\scripts\audit\capture-screenshots.py --target products` | 产品截图 |
| `python ..\..\clients\Nova-Scientia\scripts\audit\capture-screenshots.py --target companies` | 公司 logo 截图 |
| `python ..\..\clients\Nova-Scientia\scripts\audit\capture-screenshots.py --target all` | 两者 |

## archive/

| 脚本 | 说明 |
|------|------|
| `backfill-indexed-products.js` | VC indexed_products 一次性回填（已完成，备查） |

## ref/

| 命令 | 说明 |
|------|------|
| `node ..\..\clients\Nova-Scientia\scripts\ref\generate-redirects-from-gsc.js <file.xlsx>` | GSC → 301（需 `npm i xlsx`） |
| `node ..\..\clients\Nova-Scientia\scripts\ref\glossary\merge-glossary.mjs` | glossary 分片合并 |

## 部署仓保留脚本

| 命令 | 位置 |
|------|------|
| `npm run validate:products` | `scripts/permanent/validate-products-json.js` |
| `npm run indexnow:all` | `scripts/permanent/indexnow-submit.ts` |
| `node scripts/permanent/download-product-images.js` | 维护：Supabase → `public/images/products/`（非 npm） |

## 环境变量

| 变量 | 用途 |
|------|------|
| `NOVA_SCIENTIA_DEPLOY_ROOT` | 覆盖默认部署仓路径 |
| `FIRECRAWL_API_KEY` | 截图脚本（必填） |
| `INDEXNOW_KEY` | 部署仓 IndexNow（`.env`） |
