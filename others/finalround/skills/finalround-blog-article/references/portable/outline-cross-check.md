# FinalRound Outline Cross-Check（Skill reference · portable）

> **Phase 3.5 交叉检查模板。** 同批 ≥2 篇强制；单篇 `N/A — single article`。

---

## 检查项

- [ ] **H2 标题重复度**：同 cluster 内是否有 ≥2 篇同一 H2 措辞？
- [ ] **叙事弧相似**：是否都是「定义→列表→对比→FAQ→CTA」且无角度差异？
- [ ] **Canonical 越界**：非 canon 文 Outline 是否计划展开 hub 才该全量写的概念？
- [ ] **Synthesis 冲突**：两篇 One-line thesis 是否互相重叠 >50%？
- [ ] **内链缺口**：对照 internal-links.md，新文章是否满足互链要求？

## 输出

```markdown
## Outline Cross-Check — {slugs}

| Check | Result | Note |
|-------|--------|------|
| H2 重复度 | PASS/FAIL | |
| 叙事弧 | PASS/FAIL | |
| Canonical | PASS/FAIL | |
| Synthesis | PASS/FAIL | |
| 内链缺口 | PASS/FAIL | |

**Result**: PASS | FAIL → {修复动作}
```

**Fail** → 改 Outline / 改 Synthesis / MERGE 建议 / 补内链规划 → 重过 3.5
**Pass** → 输出 `Outline cross-check: PASS — {slugs}` → Phase 4

---

*outline-cross-check · portable · 可跨项目复用*
