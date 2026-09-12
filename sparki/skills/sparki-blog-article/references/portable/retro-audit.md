# 已发布稿回溯审计（Retro Audit）

> 对已发布 `.md` 做合规扫描，**只输出 diff 清单，不改文**。随 skill 分发。
> sparki 本地化：无 NN · 文件名 = slug · 主站绝对 URL · 无 `## Related articles` 模块 · category 枚举。

---

## 使用方式

```
请按 references/portable/retro-audit.md 对 {path} 做合规扫描，只输出 diff 清单，不改文。
项目配置：Sparki · sparki.io · /blog/ · 禁链未上线主站页
```

加载 skill 内 `content-graph.md`、`project-config.md`、`product-competitors.md` 作互链、白名单与 Gate 补充。

---

## 回溯检查项（14 项）

| # | 检查项 | 查什么 |
|---|--------|--------|
| R1 | 链接形式 | 主站页一律绝对 URL `https://sparki.io/...`；blog 互链相对 `/blog/{slug}`；无相对 `/features` 等失效内链（G6） |
| R2 | 产品数字 as-of | 定价/credits/功能能力是否过时（对照 `product-competitors.md` §1） |
| R3 | 竞品公平性 | 对比/替代文是否有竞品优势段 + ≥1 非 Sparki 更适合场景 |
| R4 | 碎片化 | 长段不足、伪列表堆砌（`**Bold.**` + 单句 ≥3） |
| R5 | 空泛句 / AI 腔 | hype 词、模板化开头（writing-constraints 禁词表） |
| R6 | 列表占比 | 是否超类型上限（article-types §1） |
| R7 | Frontmatter | slug=文件名、category 在枚举内、author=`Kostja`、date 不变 |
| R8 | 模块顺序 | YAML → TL;DR → H2 → Conclusion → FAQ；无 `## Related articles` 模块 |
| R9 | Information Gain | vs SERP 是否仍有增量；Moat 是否被竞品抄平 |
| R10 | Slug 合规 | 文件名 = slug、无 NN、无年份、12 反模式零触发 |
| R11 | Meta title/desc | title 45–60 / desc 120–160（validate 80–320），含主词 |
| R12 | Canonical 引用 | 非 canon 文是否越界展开（content-graph §4 边界） |
| R13 | 证据链 | 裸数字、缺 Source Map、CreatorClone 素材断言无出处 |
| R14 | 跨篇矛盾 | 与同簇其他稿冲突 / hub-spoke 互链断 |

Status：✅ Pass · ⚠️ Partial · ❌ Fail

---

## 输出格式

```markdown
## Retro Audit — {slug}

**Date**: YYYY-MM-DD

| # | 检查项 | Status | Detail |
|---|--------|:------:|--------|
| R1 | 链接形式 | ✅ Pass | 全部绝对/相对符合 |

**P1**: …
**P2**: …
```

Retro **不替代** P0 + 十维终审；修复 P1 后建议跑 `final-audit.md`。

---

*retro-audit · portable · sparki v1.1.0 · 2026-09-04*
