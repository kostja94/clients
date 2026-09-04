# Scripts

可执行脚本集中在此目录。**创作规范**已迁至 [`skills/create-article/`](../skills/create-article/SKILL.md)。

## 目录结构

```
scripts/
├── README.md          # 本文档
├── data/              # 截图 URL 注册表 tools-screenshot-registry.json
├── reports/           # audit-tools-images 输出（自动生成）
├── ops/               # Firecrawl 截图、alt 审计等
├── permanent/         # 可重复执行的运维 / 内容审计（.mjs / .py）
├── audit/             # 独立审计脚本（多数无 npm 注册）
└── ref/               # 一次性修复脚本（归档备查）
```

### 部署仓库中的脚本（alignify-by-kostja）

仅以下脚本必须在部署项目中，用于构建后向搜索引擎提交 URL：

| 脚本 | npm 命令 |
|------|----------|
| `scripts/permanent/submit-to-indexnow.ts` | `npm run indexnow` |
| `scripts/permanent/submit-all-pages-to-indexnow.ts` | `npm run indexnow:all` |

在部署仓库根目录执行上述命令即可。

### permanent/（本目录，外部上下文）

内容合规、GSC 审计等。SEO 拉数见 [`seo-weekly-report/`](../seo-weekly-report/README.md)。

```bash
# SEO 周报拉数
cd seo-weekly-report/scripts && npm install && npm run fetch-all

# CTR / 排名 / 索引健康审计（需先有 .env 或 bundle）
node scripts/ops/audit-gsc-ctr.mjs
node scripts/ops/audit-gsc-position-drop.mjs
node scripts/ops/audit-gsc-index-health.mjs
```

> **说明**：`alignify-by-kostja/package.json` 不再注册这些命令，避免部署项目混入非必需脚本。

### audit/

| 脚本 | 用途 |
|------|------|
| `audit-product-urls.mjs` | **已迁至** `C:\Users\zyjst\Downloads\alignify-product-url-audit\` |
| `apply-product-url-fixes.py` | **已迁至** 同上 `scripts/` |
| `audit-tools-internal-links.py` | Tools + Blog（`routeCategory: tools`）内链合规；`--source tools\|blog\|both` |
| `audit-md-internal-links.py` | **Markdown 版全站内链快照**：扫描 `content/**/*.md`，输出 JSON 报告（`scripts/reports/`）与文档（`scripts/reports/md-internal-links-status-*.json`） |
| `audit-marketing-md-render.py` | **Marketing 正文渲染 + 呈现债**：E33/E34/E36（P0 阻断）与 E37/E38 告警；报告见 [`knowledge/marketing/marketing-md-audit-2026-08-27.md`](../knowledge/marketing/marketing-md-audit-2026-08-27.md) |
| `audit-internal-href-registry.py` | **R0** 无效 slug / 错误 `/tools` vs `/blog` 路由（404 阻断） |
| `audit-link-distribution.py` | 每页区块分布、FAQ 堆链、单区块过稀疏 |
| `run-tools-internal-links-baseline.py` | 一键 baseline（internal-links + anchor + cross-page） |
| `generate-appendix-c-from-json.py` | 从 JSON 扫描生成附录 C 草稿 |
| `report-en-zh-link-parity.py` | EN/ZH distinct href 对称性报告 |
| `audit-cross-page-links.py` | 跨页链接图（合并 EN+ZH）：孤页、入链<3、PageRank |
| `audit-anchor-text-diversity.py` | 锚文本多样性 |
| `audit-article-optimization.py` | 文章 vs knowledgehub 优化信号（自 `public/` 迁入） |
| `file-inventory-audit.py` | 部署仓库文件清单审计 |
| `sync-skills-catalog.py` | 生成 `src/data/skills-catalog.json`（在部署仓库运行，脚本存于此） |
| `check_urls.py` | URL 可访问性批量检查（旧版硬编码列表，建议改用 `audit-product-urls.mjs`） |
| `validate-tools-llm-json-links.mjs` | Tools LLM JSON 链接验证 |
| `audit-tools-images.mjs` | Tools 产品图全站审计（P0/P1/P2 分级报告） |

### ops/ — Tools 产品图 Firecrawl 流水线

从**部署仓库**运行（需 `pip install firecrawl-py`，环境变量 `FIRECRAWL_API_KEY` 可选）：

```bash
cd D:\部署项目\alignify-by-kostja

# 1. 全站审计
node ../../clients/Alignify/scripts/audit/audit-tools-images.mjs
node ../../clients/Alignify/scripts/audit/audit-tools-images.mjs --page search-engine --severity P0

# 2. 截图状态 / 执行（注册表：scripts/data/tools-screenshot-registry.json）
python ../../clients/Alignify/scripts/ops/screenshot-tools-products.py --report
python ../../clients/Alignify/scripts/ops/screenshot-tools-products.py --severity P0 --page search-engine --force --update-json

# 3. 从审计结果合并注册表（仅新增 key，不覆盖已有 URL）
python ../../clients/Alignify/scripts/ops/generate-registry-from-audit.py \
  ../../clients/Alignify/scripts/reports/tools-images-audit-2026-06-17.json --severity P0 --merge

# 4. Alt 文本审计
node ../../clients/Alignify/scripts/ops/audit-alt-text.mjs
```

| 脚本 | 用途 |
|------|------|
| `screenshot-tools-products.py` | **主脚本**：JSON 注册表驱动 Firecrawl 截图（`--force` / `--page` / `--only` / `--from-audit`） |
| `generate-registry-from-audit.py` | 从审计 JSON 生成/合并 `tools-screenshot-registry.json` |
| `screenshot-customer-products.py` | 客户故事精选产品截图 |
| `screenshot-social-cards.py` | Social Cards 工具页截图 + JSON 更新 |
| `generate-og-cover.py` | GPT Image 2 生成 OG（`--provider fal` 默认 · `--provider apineed`）；**默认直写部署仓** `public/`（`--to-staging` 仅预览）。双提供方质量对照见 [`API-PROVIDER-QUALITY-VERIFICATION.md`](../../API-PROVIDER-QUALITY-VERIFICATION.md) |
| `batch-generate-og-covers.py` | 批量生图；`--workers 8` 并行（对齐 fal 并发）；`--skip-existing` 断点续跑 |
| `migrate-og-covers.py` | 历史 staging → deploy **move**（非 copy）+ 可选注册 `OG_LOCALE_READY` |
| `audit-og-coverage.mjs` | deploy OG 覆盖审计（`--staging` 查遗留副本） |
| `next-publish-date.mjs` | **新 slug** 分配全站唯一 `publishDate`（`--check` / `--from` / `--list`） |
| `list-article-dates.mjs` | 扫描 `*-meta.ts` 生成全站发布/更新清单 [`article-dates.md`](../skills/ops/article-dates.md) |
| `merge-cta-slugs.mjs` | Final CTA 覆盖审计（`--check`）或批量合并（`--batch batch.json`）→ `cta-config.json` |
| `audit-alt-text.mjs` | BestTools / HTML 图片 alt 质量审计 |
| `screenshot-tools-images.py` | **已废弃** — 仅 12 条硬编码 backlog，请用 `screenshot-tools-products.py` |

规范见 `skills/create-article/rules/sections.md` Part 3.3。

> **2026-09-04**：APINEED 已下线同步 `POST /v1/images/generations`，`--provider apineed` 改走**异步** `POST /v1/media/generations`（`workflow: text_to_image`，提交→轮询→下载 `outputs[0].url`）。新接口**不接受 `size` 参数**，宽幅 16:9 比例靠 prompt 指定（脚本已自动注入），post trim 到 1200×630 保留。`batch-generate-og-covers.py` 同通道。

#### 产品 URL 审计

脚本与报告已移至 **`C:\Users\zyjst\Downloads\alignify-product-url-audit\`**，详见该目录下 `README.md`。

`file-inventory-audit.py` 默认假定部署仓库位于 `../部署项目/alignify-by-kostja`；否则设置环境变量 `ALIGNIFY_DEPLOY_ROOT`。

### ref/

可重复使用的维护脚本：

| 脚本 | 用途 |
|------|------|
| `fix-rules-section-links.py` | 修复 `skills/create-article/rules/` 内 `../section/` 等断链 |
| `migrate-tables-to-childrenhtml.py` | 裸 HTML / GFM 管道表 → `childrenHtml` 围栏（格式 A） |

历史一次性脚本（已归档或移除）：`migrate-doc-paths.py`、`fix-format-mismatches.py`、`fix-fullpage-screenshots.py` 等。