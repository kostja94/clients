# Scripts

可执行脚本集中在此目录。**部署仓库** `alignify-by-kostja/` 仅保留 IndexNow 相关脚本；其余运维、审计、内容检查脚本均在此。

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

内容合规、引用规范化、GSC/Bing/GA4 拉取、部署前检查等。从**部署仓库**运行示例（路径按本机调整）：

```bash
cd D:\部署项目\alignify-by-kostja
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
node ../../clients/Alignify/scripts/ops/audit-tldr-length.mjs
node ../../clients/Alignify/scripts/ops/fetch-gsc-data.mjs
node ../../clients/Alignify/scripts/ops/check-deploy.mjs
```

也可在 `Alignify项目上下文` 根目录直接 `node scripts/permanent/...`（脚本内路径需指向部署仓库的 `content/` 等）。

> **说明**：`alignify-by-kostja/package.json` 不再注册这些命令，避免部署项目混入非必需脚本。

### audit/

| 脚本 | 用途 |
|------|------|
| `audit-product-urls.mjs` | **已迁至** `C:\Users\zyjst\Downloads\alignify-product-url-audit\` |
| `apply-product-url-fixes.py` | **已迁至** 同上 `scripts/` |
| `audit-tools-internal-links.py` | Tools + Blog（`routeCategory: tools`）内链合规；`--source tools\|blog\|both` |
| `audit-md-internal-links.py` | **Markdown 版全站内链快照**：扫描 `content/**/*.md`，输出 JSON 报告（`scripts/reports/`）与文档（`content/alignify-internal-links-status.md`） |
| `audit-internal-href-registry.py` | **R0** 无效 slug / 错误 `/tools` vs `/blog` 路由（404 阻断） |
| `audit-link-distribution.py` | 每页区块分布、FAQ 堆链、单区块过稀疏 |
| `run-tools-internal-links-baseline.py` | 一键 baseline（internal-links + anchor + cross-page） |
| `generate-appendix-c-from-json.py` | 从 JSON 扫描生成附录 C 草稿 |
| `report-en-zh-link-parity.py` | EN/ZH distinct href 对称性报告 |
| `audit-cross-page-links.py` | 跨页链接图（合并 EN+ZH）：孤页、入链<3、PageRank |
| `audit-anchor-text-diversity.py` | 锚文本多样性 |
| `audit-article-optimization.py` | 文章 vs knowledgehub 优化信号（自 `public/` 迁入） |
| `file-inventory-audit.py` | 部署仓库文件清单审计（报告见 `technical/file-inventory-audit.md`） |
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
| `audit-alt-text.mjs` | BestTools / HTML 图片 alt 质量审计 |
| `screenshot-tools-images.py` | **已废弃** — 仅 12 条硬编码 backlog，请用 `screenshot-tools-products.py` |

规范见 `content/sections/section-best-tools.md` §5.1–5.3。

#### 产品 URL 审计

脚本与报告已移至 **`C:\Users\zyjst\Downloads\alignify-product-url-audit\`**，详见该目录下 `README.md`。

`file-inventory-audit.py` 默认假定部署仓库位于 `../部署项目/alignify-by-kostja`；否则设置环境变量 `ALIGNIFY_DEPLOY_ROOT`。

### ref/

一次性修复脚本，包括自部署仓库 `public/` 迁入的：

- `fix-format-mismatches.py`
- `fix-fullpage-screenshots.py`

以及历史归档：`final_supplement.py`、`fix_all_dupes.py`、`sync_en_zh_links.py` 等。

### 根目录其他文件

| 文件 | 说明 |
|------|------|
| `skills-lock.json` | Cursor