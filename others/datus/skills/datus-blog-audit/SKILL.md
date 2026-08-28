---
name: datus-blog-audit
description: >
  Final audit and retro-audit for datus.ai blog articles after datus-blog-article
  Gate C passes. Self-contained wrapper around portable final-audit.md and
  retro-audit.md. Loads datus-blog-article project-config and product-competitors.
metadata:
  version: 1.0.0
  project: datus.ai
  complements: datus-blog-article
  self-contained: true
---

# Datus Blog Audit（发布前终审 / 回溯）

成稿 **Gate C 全 Pass（audit-ready）** 后执行。不替代 `datus-blog-article` Phase 5 SelfCheck。

---

## §0 触发语

**发布前终审**：

```
按 datus-blog-audit skill 执行终审：
- 文件：{path/to/NN-slug.md}
- ArticleType：{GlossaryTerm|ToolsList|...}
- 主关键词：{primary keyword}
- SelfCheck：{Pass}/12
```

**已发稿回溯**：

```
按 datus-blog-audit skill 执行 retro：
- 文件：{path}
- 模式：retro
```

---

## §1 执行流程

### Final

1. 读 `../datus-blog-article/references/portable/final-audit.md`
2. 读 `../datus-blog-article/references/project-config.md`
3. 读 `../datus-blog-article/references/product-competitors.md`
4. P0 Gate（G1–G7 + 类型 Gate）→ 十维加权 → 等级 + 修复清单

### Retro

1. 读 `../datus-blog-article/references/portable/retro-audit.md`
2. 加载 project-config
3. 输出 Retain / Refresh / Merge / Deprecate

---

## §2 与 datus-blog-article 的关系

```
datus-blog-article Phase 5 SelfCheck → audit-ready
        ↓
datus-blog-audit Final (≥70 + P0 Pass) → publish-ready
        ↓
人类发布 → post-publish-review.md（复盘）
        ↓
datus-blog-audit Retro
```

---

*datus-blog-audit · v1.0.0 · 2026-08-28*
