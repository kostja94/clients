# Alignify 覆盖说明（读完 SKILL.md 后读取）

- **项目根**：`Alignify/seo-weekly-report/`（上下文仓，非部署仓）
- **站点**：https://alignify.co/
- **报告 ID**：`alignify` → 输出 `reports/alignify-seo-weekly-{date}.md`
- **内容发布**：新文章见部署仓 `content/`；可选维护 `config/content-catalog.yaml` 供 merge 读取本周新发
- **CTR/排名审计**：`node scripts/ops/audit-gsc-ctr.mjs`（读 bundle，元数据从部署仓 `app/` 提取时需设 `ALIGNIFY_DEPLOY_ROOT`）
- **Vercel 可删**：`GSC_CLIENT_EMAIL`、`GSC_PRIVATE_KEY`、`GA_PROPERTY_ID`
- **Bing 拉数**：`scripts/.env` 填 `BING_API_KEY` → `npm run fetch-bing` 或 `fetch-all`
