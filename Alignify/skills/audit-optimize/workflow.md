# 内链优化 Workflow

> 入口：[`SKILL.md`](SKILL.md) · 规则：[`references/rules-quickref.md`](references/rules-quickref.md) · 快照：[`references/site-structure-internal-links.md`](references/site-structure-internal-links.md)

---

## 0. 读上下文

1. [`references/site-structure-internal-links.md`](references/site-structure-internal-links.md) — 出链/入链、P0–P3 队列、**§七 Marketing/GTM 专项**  
2. [`../create-article/rules/internal-links.md`](../create-article/rules/internal-links.md) 附录 B — 邻居矩阵  
3. [`../../knowledge/tools/territory-map.md`](../../knowledge/tools/territory-map.md) — 同 Territory 选题  

---

## 1. 全站 Baseline（可选，开批次前一次）

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --locale both --violations-only
npm run verify:content-json
```

**阻断项**（见 quickref）：R0 无效 href · R4 同 URL 重复 · 机械指路链 / 同段堆链

报告：`Alignify/scripts/reports/`

---

## 2. 单页 Loop

### 2.1 审计

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
git show HEAD:content/{channel}/{locale}/{slug}.md   # baseline
```

### 2.2 选链

- 点击意图三问（[`internal-links.md` Part 4.5 §一](../create-article/rules/internal-links.md#一第一原则读者想点click-intent)）
- EN/ZH 目标 slug 对称
- 不为主页 distinct 计数加弱相关链

### 2.3 写入

| 区块 | 建议 |
|------|------|
| TL;DR（`tldr-data.json` intro） | 0–1 链 |
| 正文 section | 任务句内链；每段 ≤1 |
| 结论 | 0–2 链 |
| FAQ（`faq-data.json` 答案） | **允许内链**，算正文一部分；同 URL 全文仍只 1 次 |

**编辑策略**（存量大批量修复时 SSOT 定稿）：见 [`internal-links.md`](../create-article/rules/internal-links.md) Part 6–7；本 skill 不预设 R-LINK-ONLY / R-QUALITY-REWRITE，按任务 Brief 选。

### 2.4 验收

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
npm run verify:content-json && npm run build
python ../../clients/Alignify/scripts/audit/build-site-internal-links-doc.py
```

---

## 3. 禁止

- 为凑 distinct 删结论/FAQ 整段  
- 未读 baseline 就大段 StrReplace  
- 机械指路链（「详见 XXX 指南」式堆链）

Phase 4 反向互链 → [`reverse-links.md`](reverse-links.md)

*workflow · v1.1 · 2026-09-03 · 自 optimize-internal-links 迁入*
