# optimize-tools-internal-links

存量 Tools / Tools 型 Blog 文章的内链审计、选链、写入、台账更新与验收。

## 与 create-tools-article 的分工

| Skill | 用途 |
|-------|------|
| `create-tools-article` | 新文从零创建（含内链初稿） |
| **`optimize-tools-internal-links`** | 存量页内链审计、选链、写入、附录 C 台账、验收 |

## 何时使用

- 单页或批次内链不达标（R1–R7）
- Wave 0–4 全库优化（见专册 §1.5.7）
- 补反向互链（Phase 4）
- 更新附录 C 台账

## 前置阅读

1. [alignify-internal-links.md §1](../../content/alignify-internal-links.md#part-1-编辑层单篇怎么改best-practice) — 单篇编辑 DoD（优先）
2. [alignify-internal-links.md §3.1.5](../../content/alignify-internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留) — R1–R7 底线
3. [01-rules-and-neighbors.md](./01-rules-and-neighbors.md) — 规则速查 + 附录 B
4. [02-audit-and-baseline.md](./02-audit-and-baseline.md) — 审计命令
5. [03-per-page-workflow.md](./03-per-page-workflow.md) — 单页 checklist
6. [04-reverse-links.md](./04-reverse-links.md) — 反向互链 SOP

## 标准流程

```
附录 B / keywords 选邻居
    → git show HEAD 建立 baseline（R-LINK-ONLY）
    → 单页或批次 audit
    → 只改 <a>（unwrap 重复 / 补 R1 链）
    → patch-tools-internal-links.py 或 unwrap 脚本
    → 更新附录 C + 修订日志
    → audit:internal-links（零 high）
    → audit:text-regression（零缩水）
    → verify:content-json + npm run build
```

**R-LINK-ONLY**：见 §1.5.4 第 8 条、`03-per-page-workflow.md` 禁止清单。

## 区块配额（速查）

| 区块 | 配额 |
|------|------|
| TL;DR | **0–1 条**（硬上限 2 distinct）；Hub 页 TLDR **禁止**枚举 3+ spoke |
| R-TLDR-2 | 相邻两链间距 ≥40 字符 |
| R-TLDR-3 | TLDR slug 不得再出现在「什么是」/ section |
| 什么是 · 第二段 | 1–4 条（Hub 辐条首次 `<a>`），与 TLDR 去重 |
| 场景 useCases | 0–1 条/条 |
| FAQ | ≤3 distinct slug，与正文去重；单答 ≤2 `<a>` |
| 全文 | ≥5 distinct href；同一目标 slug 仅出现一次（R4） |

**创建阶段**：见 `create-tools-article/02c-internal-links-drafting.md`。

## 脚本索引

| 脚本 | 位置 |
|------|------|
| `audit-tools-internal-links.py` | 上下文仓 `scripts/audit/` |
| `run-tools-internal-links-baseline.py` | 上下文仓 `scripts/ops/` |
| `patch-tools-internal-links.py` | 部署仓 `scripts/permanent/` |
| `batch-internal-links-wave.py` | 部署仓 `scripts/permanent/` |
| `apply-reverse-backlinks.py` | 部署仓 `scripts/permanent/` |

模板页：`content/blog/*/agent-sandbox.json` + `apply-agent-sandbox-links.py`。
