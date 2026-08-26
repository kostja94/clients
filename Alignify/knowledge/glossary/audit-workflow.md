# Glossary 运维审计（Deploy 仓库）

部署仓路径：`E:\自有部署项目\alignify production`

## 一键命令

```bash
npm run audit:glossary:all
```

等价于：去重 → 同步 JSON meta → strict gap → 链接审计。

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `glossary-gap-report.mjs` | 内链覆盖 + EN/ZH parity + ZH 跨章节重复组 |
| `glossary-link-audit.mjs` | 校验 glossary 内链 locale 与 404（CI 已接入） |
| `glossary-dedupe-terms.mjs --write` | 删除同 key 重复项；跨章节保留 canonical section |
| `glossary-bulk-link-terms.mjs --write` | 为无内链术语批量补链（仅空链术语） |
| `glossary-sync-meta.mjs` | 写回 `termCount`、meta title/description、excerpt |
| `glossary-parity-sync.mjs` | 从 ZH-only 补 EN 术语（seo 大表） |
| `glossary-sync-content.mjs` | 新术语、内链补丁、定义更新 |

## 去重规则（ZH SEO）

跨章节保留 canonical section：

- 链接类 → `website-structure` 或 `link-building`
- `redirect chain` → `link-building`
- `sitemap` 同节内保留「站点地图」删「网站地图」

## SSOT

- 页面 SEO 计数：`src/lib/glossary-stats.ts` → `src/data/glossary-meta.ts`
- 术语 JSON：`content/glossary/{en,zh}/{seo,marketing,ai}.json`

## OG Brief 术语数（2026-08）

| Slug | EN | ZH |
|------|-----|-----|
| seo | 290+ | 300+ |
| marketing | 170+ | 170+ |
| ai | 155+ | 155+ |
| 索引合计 | 617 | 626 |

## Phase 历史

1. locale 内链、compact UI、meta SSOT  
2. 侧栏、A–Z、锚点  
3. 内链扩展  
4–5. blog/SEO 100% 覆盖  
6. SEO EN/ZH parity  
7. marketing/ai parity + 「亦见」badge  
8. 去重、meta 同步、CI strict、索引 JSON-LD  
9. 术语级内链批量补链（SEO/Marketing/AI 覆盖率 ≥60%）
