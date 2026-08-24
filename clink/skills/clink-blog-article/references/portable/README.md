# Portable Bundle — 通用 Blog 创作 SSOT

> **Clink 本地副本** — 从 SSOT 同步，**勿手改**。维护通用规范请改 `E:\Agent执行\blog-create\references\portable\` 后重新同步。
> **文档不含具体品牌名**；产品配置只在各项目 skill 的 `references/` 内维护。

## 文件清单

| 文件 | 用途 |
|------|------|
| `gates-master.md` | Gate 总表 + audit-ready / publish-ready / S 级语义 |
| `investment-score.md` | Phase 0 五因子选题投资分 |
| `research-triangle.md` | Phase 0R + Synthesis + IG 三问 + Examples |
| `serp-fit-template.md` | SERP Fit 表 |
| `source-map-template.md` | Source Map + EEAT 速查 |
| `outline-cross-check.md` | Phase 3.5 同批 Outline 对比 |
| `extractability-checklist.md` | Phase 4 BLUF + Claim + Judgment + Answer Blocks |
| `perfect-article-checklist.md` | S 级 + Excellence + Moat 速查 |
| `post-publish-review.md` | T+7/30/90/180 复盘指针 |
| `final-audit.md` | 发布前终审 + Signal of Excellence |
| `retro-audit.md` | 已发稿回溯扫描 |

## 同步到 client skill

```powershell
$ssot = "E:\Agent执行\blog-create\references\portable"
$dest = "e:\clients\{brand}\skills\{brand}-blog-article\references\portable"
Copy-Item -Path "$ssot\*.md" -Destination $dest -Force
```

维护者更新通用规范后：先改本目录 → 再同步到各 client skill。

*portable-bundle · v2.1 · 2026-08-23 · SSOT: E:\Agent执行\blog-create*
