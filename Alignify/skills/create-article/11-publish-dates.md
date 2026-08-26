# Step 11 — publishDate 分配（全站唯一日历日）

> **前置**：**publish-ready**（audit-article 终审 ≥80 + P0 Pass）  
> **不适用**：仅 audit-ready、未终审通过  
> **锚定日**：执行本步时的**实际日历日（UTC+8）**——禁止把文档示例日期当作「今天」。

---

## 核心规则

| 规则 | 说明 |
|------|------|
| **R1 新 slug 唯一** | 每个**新注册** slug 的 `publishDate` 日历日，在**全站所有** `*-meta.ts` 中**不得与任何已有 slug 重复** |
| **R2 已上线不改** | 已上线 slug 的 `publishDate` **永不更改**（内容大改只更新 `modifiedDate`） |
| **R3 双源一致** | `*-meta.ts` ISO 与 md frontmatter `date` **同一日历日**；`updated` / `modifiedDate` = 本次内容变更日 |
| **R4 时区** | 一律 `T00:00:00+08:00` |
| **R5 批量错开** | 同批多篇新文：每篇占用**不同**日历日，按脚本顺序分配 |

**区分新建 vs 更新**：

| 场景 | `publishDate` / md `date` | `modifiedDate` / md `updated` |
|------|---------------------------|-------------------------------|
| **新 slug 首发** | 分配**新的唯一**日历日（通常 ≈ 锚定日） | 与 publishDate **相同** |
| **已上线 slug 改版**（如 rate-limit-reset） | **不变** | 更新为锚定日 |

---

## 执行流程（新 slug 必做）

### 1. 查占用 & 取下一天

部署仓根目录（或设 `ALIGNIFY_DEPLOY_ROOT`）：

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs
```

输出示例（锚定日 2026-08-26）：

```
Next free publishDate: 2026-08-26
ISO: 2026-08-26T00:00:00+08:00
ZH md date: 2026年8月26日
EN md date: August 26, 2026
```

同批第二篇起：

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --from 2026-08-27
```

### 2. 注册前校验

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --check 2026-08-26
```

- 输出 `OK` → 可用  
- 输出 `BLOCKED` → 换 `--from` 再取下一空闲日

### 3. 写入三处（须同一日历日）

| 位置 | 字段 | 示例 |
|------|------|------|
| `src/data/{channel}-meta.ts` | `publishDate` | `"2026-08-26T00:00:00+08:00"` |
| `src/data/{channel}-meta.ts` | `modifiedDate`（新 slug） | 同 publishDate |
| `content/.../zh/{slug}.md` | `date` / `updated` | `"2026年8月26日"` |
| `content/.../en/{slug}.md` | `date` / `updated` | `"August 26, 2026"` |

### 4. 审计占用（可选）

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --list
```

标记 `[DUPLICATE]` 的为历史遗留；**新 slug 禁止再占用这些日**。

---

## 多频道

扫描范围含全部 meta 文件，**不限频道**：

`blog-meta.ts` · `tools-meta.ts` · `seo-meta.ts` · `marketing-meta.ts` · `insights-meta.ts` · `events-meta.ts`

新 marketing 文占用 2026-08-26 后，同日不能再注册 blog/seo 新 slug。

---

## Gate 11 Checklist

- [ ] audit-article **publish-ready: Yes**
- [ ] **新 slug**：已跑 `next-publish-date.mjs` 且 `--check` Pass
- [ ] **新 slug**：publishDate 在全站 `*-meta.ts` 中唯一
- [ ] **改版 slug**：仅 `modifiedDate` / `updated` 变为锚定日；publishDate / `date` 未改
- [ ] meta ISO 与 md frontmatter 日历日一致

---

## 常见错误

| 错误 | 正确 |
|------|------|
| 把 skill 示例 `2026-06-23` 当今天 | 以执行日为准，跑脚本取日 |
| 新 slug 与已有 slug 同日 publishDate | `--check` 后换下一空闲日 |
| 大改版改掉 publishDate | 只改 modifiedDate |
| meta 与 md `date` 差一天 | 三处同一日历日 |

见 [`rules/common-errors.md`](./rules/common-errors.md) **E20**、**E26**。

---

发布后运维 → [`../ops/README.md`](../ops/README.md)  
已发稿回溯 → [`../audit-article/SKILL.md`](../audit-article/SKILL.md) retro 模式

---

*11-publish-dates · v2.0 · 2026-08-26*
