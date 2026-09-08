# Clink — Slug Design Gate B

> 加载时机：Phase 2

---

## 6 问检查

| # | 检查项 | 标准 |
|---|--------|------|
| 1 | 含 primary keyword 核心词？ | slug 与 target keyword 对齐 |
| 2 | 大声读测试？ | kebab-case 读通顺 |
| 3 | 不含禁词？ | framework / strategy / guide / complete / ultimate / diagnosis |
| 4 | ≤60 字符？ | 不含 `/blog/` |
| 5 | 常青无年份？ | 无 2026 等 |
| 6 | 语义余量？ | 30% 内容变化后仍适用 |

---

## 12 反模式

| # | 反模式 | 错误 | 正确 |
|---|--------|------|------|
| 1 | 含年份 | `smart-routing-2026` | `smart-routing` |
| 2 | 品牌前缀 | `clink-payment-routing` | `smart-payment-routing` |
| 3 | 内部架构词 | `mor-vs-psp-comparison-guide` | `mor-vs-psp` |
| 4 | 过长 | `how-to-reduce-involuntary-churn-with-smart-payment-routing` | `reduce-involuntary-churn-routing` |
| 5 | 与已有混淆 | `what-is-clink-billing` | 新角度 slug |
| 6 | 下划线 | `mor_vs_psp` | `mor-vs-psp` |
| 7 | 空洞词 | `complete-guide-payment` | 描述性 slug |
| 8 | misleading free | `free-payment-orchestration` | 准确 intent |
| 9 | vs 格式错误 | `stripe-clink` | `clink-vs-stripe` |
| 10 | 重复词 | `payment-payment-routing` | `payment-routing` |
| 11 | 过大写 | `MoR-vs-PSP` | `mor-vs-psp` |
| 12 | 缺 intent | `clink-blog-post-5` | keyword-driven |

---

## Title / Description

> SSOT → `references/meta-title-description.md`（每类型 Title 公式 + Description 规则 + 字符范围）。本文件不复述。

---

*slug-gate · v1.1.0 · 2026-09-08 · Title 公式迁至 meta-title-description*
