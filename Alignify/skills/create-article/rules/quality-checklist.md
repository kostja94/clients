# 综合质量检查表

> **版本**：v3.0 · 2026-08-26  
> **质量档位**：Alignify **每篇 flagship**  
> **Gate 语义**：Step 10 SelfCheck → **audit-ready** → Step 11 Final Audit（新会话）→ **publish-ready**

---

## 状态与 Gate 对应

| 状态 | 达成 |
|------|------|
| audit-ready | [`selfcheck.md`](./selfcheck.md) H0–H4 + 12 维全 Pass + 脚本绿 |
| publish-ready | [`final-audit.md`](./final-audit.md) P0 Pass + 十维 ≥**80** |
| S 级 | 十维 ≥**90** + Moat + Excellence + 零 P1 |

---

## 一、自动化检查

**部署仓** `E:\自有部署项目\alignify production`：

```bash
npm run verify:content-json
npm run build
node ../../clients/Alignify/scripts/ops/merge-cta-slugs.mjs --check
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
python ../../clients/Alignify/scripts/audit/audit-frontmatter.py   # E44–E48；0 issues
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

---

## 二、P0（阻断 audit-ready / publish-ready）

### 事实 G1–G7

见 [`gates.md`](./gates.md)。量化 claim 须有 Source Map 行。

### Alignify 结构 / Meta P0

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P0-1 | 结论收束 md 正文 | md 以 `#conclusion` 结尾；FAQ 在页底全局组件 |
| P0-2 | FAQ 数量 | **若** 有 FAQ：中英文各 **7 问** |
| P0-3 | FAQ 内链 | **若** FAQ 含内链：同 URL 全文仅 1 次（R4） |
| P0-4 | 图片 | `public/` 存在 |
| P0-5 | Best 产品段 | **若** 有 Best H3：ZH ≥100 字 / EN ≥280 字符 |
| P0-5b | 产品数量/独占 | 新文 H3 **≤5**（默认 **3**）；Brief roster = 正文 H3；**无**站级 duplicate canonical（E51 · [`product-coverage.md`](./product-coverage.md)） |
| P0-7 | Meta title | best-ranking：含「最佳」/ `Best` |
| P0-8 | Meta description | ≥2 产品名（Tools） |
| P0-9 | Meta 格式 | 年份 + 冒号副线 |
| P0-10 | HowTo | 无 frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44） |
| P0-11 | Frontmatter schema | `audit-frontmatter.py` 0 issues（E44–E48）；ZH/EN 键 parity |
| P0-11b | TL;DR/FAQ/Refs JSON | Brief 采用时：`tldr-data.json` / `faq-data.json` / `references-data.json` 已注册 pathname 键（E10）；Brief 省略时无键 |
| P0-12 | Gate 0R | Research + Brief + Moat 已完成 |
| P0-13 | 双语 parity | ZH/EN section 对齐 |

---

## 三、P1（Flagship 须清零方可 publish-ready）

| # | 检查项 |
|---|--------|
| P1-1 | Moat 在正文兑现（非仅 Brief） |
| P1-2 | BLUF 三处 Pass |
| P1-3 | FAQ 与正文非复制（相似度 <30%） |
| P1-4 | 内链：点击意图 + 同 URL 1 次；无机械指路链/结论堆链 |
| P1-5 | Extractability / Answer Blocks Pass |
| P1-6 | 对照参考菜单 intentional |
| P1-7 | Presentation 节奏（长段、无伪列表） |
| P1-8 | Source Map 完整 |

---

## 四、Build 后验证

- [ ] 对应 channel URL 可访问
- [ ] 无 HowTo JSON-LD

---

*quality-checklist · v3.0 · 2026-08-26*
