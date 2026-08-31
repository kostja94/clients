# Clink 任务看板

> 内部进度记录 · **Last updated**: 2026-08-31  
> 本文件只记 **是什么 + 谁做 + 状态**；细则见各任务单。

**用法**：待办 → 进行中 → 已完成；任务单关闭后移 [archive/](./archive/)。

---

## 负责分工

| 负责 | 任务 |
|------|------|
| **对方** | 001 · 002 · 005 |
| **我方** | 003 · 004 |

---

## 看板

### 待办

| ID | 任务 | P | 负责 | 任务单 | 依赖 |
|----|------|:-:|------|--------|------|
| clink-001 | www / 裸域 301 统一 | P0 | 对方 | [canonical-host](./clink-fix-canonical-host.md) | — |
| clink-002 | 全站 canonical + og:url | P1 | 对方 | [canonical-tag](./clink-fix-canonical-tag.md) | 001 |
| clink-003 | Agentic Payment 页优化 | P1 | 我方 | — | — |
| clink-004 | X 涨粉 vendor 调研 | P1 | 我方 | [买粉调研](./clink-x-growth-vendor-research.md) | — |
| clink-005 | Blog GA4 与主站统一 | P2 | 对方 | [blog-ga4](./clink-fix-blog-ga4-attribution.md) | — |

### 进行中

| ID | 任务 | 负责 | 开始 | 备注 |
|----|------|------|------|------|
| | | | | |

### 已完成

| ID | 任务 | 负责 | 完成 | 交付物 |
|----|------|------|------|--------|
| | | | | |

### 已阻塞

| ID | 任务 | 负责 | 原因 |
|----|------|------|------|
| | | | |

---

## 任务是什么（一句话）

| ID | 是什么 | 负责 |
|----|--------|------|
| 001 | 选定首选 host，`clinkbill.com` ↔ `www` 301，sitemap/内链 host 一致 | 对方 |
| 002 | 主站 + Blog 可索引页补 `<link rel="canonical">`，Blog 补 `og:url` | 对方 |
| 003 | `/agentic-payment` SEO、sitemap、内链与 Early Access 转化 | 我方 |
| 004 | @clinkglobal 涨粉/增长 vendor 对比调研（非代运营） | 我方 |
| 005 | Blog 仓库接入 GA4 `G-0YGZ90TPXH`（与首页同 property） | 对方 |

**顺序建议**：对方线 001 → 002 → 005；我方 003 / 004 可并行。

---

## 其它

| 任务 | P | 负责 | 任务单 | 状态 |
|------|:-:|------|--------|------|
| 面包屑 Schema 绝对 URL | P1 | 对方 | [archive/breadcrumb-schema](./archive/clink-fix-breadcrumb-schema.md) | 待处理 |

---

*Clink · `clients/clink/TASKS.md`*
