# Audit Article — Alignify 发布前终审

> **版本**：v1.0 · 2026-08-26  
> **用途**：create-article Step 10 产出 **audit-ready** 后，由人类或**另一 Agent** 做加权终审 → **publish-ready**。  
> **质量档位**：Alignify 每篇均为 **flagship**；发布线 **≥80 分 + P0 Pass**；标杆 **S 级 ≥90**。

---

## 与 create-article 的关系

```
create-article Step 01–09 成稿
        ↓
Step 10 SelfCheck（H0–H4 + 12 维）→ audit-ready
        ↓
audit-article Final（十维 ≥80 + P0 Pass）→ publish-ready
        ↓
Step 11 publishDate → 人类发布
        ↓
retro-audit（季度 / 重大变更）
```

**不替代** Step 10 SelfCheck — 自写自审易 blind spot。

---

## 何时使用

- [ ] ZH + EN md 已完成
- [ ] Step 10 SelfCheck **全 Pass**
- [ ] Source Map + SERP Fit + Brief 可查阅

**不适用**：

| 场景 | 改用 |
|------|------|
| 从选题到成稿 | [`../create-article/SKILL.md`](../create-article/SKILL.md) |
| 仅改 Meta title/description | create-article Step 08 + meta 规则 |
| 成稿未过 Gate C | 回 Step 10 / gate-rollback |
| 仅内链优化 | [`../optimize-internal-links/SKILL.md`](../optimize-internal-links/SKILL.md) |
| 发布后 SEO 运维 | [`../ops/README.md`](../ops/README.md) |

---

## 触发语

```
按 Alignify audit-article skill 终审：
- ZH：content/{channel}/zh/{slug}.md
- EN：content/{channel}/en/{slug}.md
- articleType：{type}
- Primary keyword：{kw}
- SelfCheck：12/12 + H0–H4 Pass
- Brief Moat：{一行}
```

**Retro 模式**：

```
按 Alignify audit-article skill retro 审计：
- 文件：content/{channel}/zh/{slug}.md（+ en）
- 模式：retro
```

---

## Final Audit 流程

1. 读 [`rules/final-audit.md`](./rules/final-audit.md)
2. 读 create-article [`rules/article-brief.md`](../create-article/rules/article-brief.md)（Moat、Answer Blocks）
3. 读 [`rules/source-map-template.md`](../create-article/rules/source-map-template.md) 产出物
4. P0 Gate 逐项
5. 十维加权评分
6. 输出 publish-ready / 修复清单

**判定**：

- P0 BLOCKED → **不得发布**
- 总分 **≥80** + P0 Pass → **publish-ready** → 可执行 Step 11
- 总分 **≥90** + Moat + Excellence + 零 P1 → **S 级标杆**

---

## Retro Audit 流程

1. 读 [`rules/retro-audit.md`](./rules/retro-audit.md)
2. P0 快速扫描 + Retain/Refresh/Merge/Deprecate 建议

---

## 文档索引

| 文件 | 用途 |
|------|------|
| [`rules/final-audit.md`](./rules/final-audit.md) | 发布前十维 rubric |
| [`rules/retro-audit.md`](./rules/retro-audit.md) | 已发稿回溯 |
| [`../create-article/rules/gates.md`](../create-article/rules/gates.md) | Gate 语义 |
| [`../create-article/rules/selfcheck.md`](../create-article/rules/selfcheck.md) | audit-ready 标准 |
| [`../create-article/rules/perfect-article-checklist.md`](../create-article/rules/perfect-article-checklist.md) | S 级清单 |

---

*audit-article · v1.0 · 2026-08-26 · complements create-article*
