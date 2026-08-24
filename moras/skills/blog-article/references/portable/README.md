# Portable Bundle — 通用 Blog 创作 SSOT

> **本目录为 Single Source of Truth（SSOT）**，位于 `E:\Agent执行\blog-create\references\portable\`。
> 各 client 的 `{brand}-blog-article` skill 应从此处同步复制到其 `references/portable/`。
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

## 同步到 client skill（客户交付包）

客户收到的 skill 文件夹必须**自带完整副本**，不可引用内网路径：

```powershell
$ssot = "E:\Agent执行\blog-create\references\portable"
$dest = "e:\clients\{brand}\skills\{brand}-blog-article\references\portable"
Copy-Item -Path "$ssot\*.md" -Destination $dest -Force
```

同步后 client skill 的 `SKILL.md` 应写 `self-contained: true`，工作流与终审均指向本目录内 `references/portable/`。

维护者更新通用规范后：先改本目录 → 再同步到各 client skill → bump client skill 版本。

*portable-bundle · v2.1 · 2026-08-23 · SSOT: E:\Agent执行\blog-create*
