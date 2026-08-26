# 同批跨篇审计（Step 10 · Phase 5.5）

> **触发**：同批 **≥2 篇** 均达 audit-ready。单篇：跳过。

---

## 检查点

| 检查点 | 检测 |
|--------|------|
| 叙事模式雷同 | 3+ 篇相同叙事弧 → 标记并重写 Intro/Conclusion |
| 内容网络 | Hub-Spoke 互链双向？orphan spoke？ |
| 概念 canonical | 同一核心概念是否多篇重复展开（应 1 篇 canonical + 他文链回） |
| Intro/Conclusion 模板化 | 多篇 Intro 可互换？→ 重写 |
| Meta 副线雷同 | 多篇 `(2026)：副线` 仅换品类词 → 差异化副线 |

**Fail** → 回 Step 05–06 或 MERGE  
**Pass** → 可批量送 audit-article

---

*cross-article-audit · v1.0 · 2026-08-26*
