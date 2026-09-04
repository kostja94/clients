# 同批跨篇审计（Step 10 · Phase 5.5）

> **触发**：Brief **`BatchCount ≥2`** 且同批均 audit-ready。单篇：Step 10 输出 **`Cross-Article 5.5: N/A — single article`**。  
> **SSOT**：五维验收见 [`copy-quality.md`](./copy-quality.md) Part 1·4 · M2 强制全维。

---

## 检查点（五维 + 网络）

| 维 | 检查点 | Fail 信号 |
|----|--------|-----------|
| **差异性** | 叙事模式雷同 | 3+ 篇相同叙事弧 → 重写 Intro/Conclusion |
| **差异性** | Intro/Conclusion 模板化 | 换 slug 后开篇/收束仍成立 → 重写 |
| **差异性** | Meta 副线雷同 | 多篇 `(2026)：副线` 仅换品类词 |
| **差异性** | FAQ 复制 | 与邻 slug ≥3 问仅差一词 |
| **去模板化** | Swap Test（邻页轴） | Brief `swap neighbors` 并排，Intro + 1 主体 H2 + FAQ 首问仍成立 |
| **相关性** | 概念 canonical | 同一核心概念多篇重复展开 → 1 篇 canonical + 他文链回 |
| **相关性** | **产品 canonical** | 同批或站级：**同一产品** 不得两篇完整 Best H3 → 保留 1 canonical（[`product-coverage.md`](./product-coverage.md)） |
| **一致性** | 内容网络 | Hub-Spoke 互链双向？orphan spoke？ |
| **一致性** | **产品池不交** | 同批 slug 的 `Product roster` **集合不交** |

**M1 同批**：至少过 **差异性 + 去模板化** 行；**M2 同批**：五维全表。

---

## 输出

```markdown
## Cross-Article 5.5 — {slug}
- Mode: M1 | M2
- Neighbors checked: {slug-a}, {slug-b}
- Swap Test (cross): Pass | Fail — {note}
- Result: PASS | FAIL → {回 Step 05–06 | MERGE}
```

**Fail** → 回 Step 05–06 或 MERGE  
**Pass** → 可批量送 Step 11 Final Audit（新会话）

---

*cross-article-audit · v2.0 · 2026-08-27*
