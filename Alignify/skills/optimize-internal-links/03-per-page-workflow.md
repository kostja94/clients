# 单页优化 Checklist

> 入口：[`SKILL.md`](SKILL.md) · 审计 baseline：[`02-audit-and-baseline.md`](02-audit-and-baseline.md) · 规则速查：[`references/rules-quickref.md`](references/rules-quickref.md) · **R-LINK-ONLY** 必读 · Phase 4：[`04-reverse-links.md`](04-reverse-links.md)

## 禁止

- 删结论/FAQ 整段以满足「条数」
- 未读 `git show HEAD:` 就 StrReplace 大段 prose
- 机械指路链（详见 / 见 XXX 指南）

## 流程

### 1. 审计

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --locale both --violations-only
```

### 2. Baseline

```bash
git show HEAD:content/{channel}/{locale}/{slug}.md
```

### 3. 选链

- [ ] 附录 B / [`references/site-structure-internal-links.md`](references/site-structure-internal-links.md) Hub / [`knowledge/tools/territory-map.md`](../../knowledge/tools/territory-map.md)
- [ ] 点击意图三问（marketing-internal-links §一）
- [ ] EN/ZH 目标 slug 对称

### 4. 写入（只改 `<a>`）

| 区块 | 动作 |
|------|------|
| TL;DR | 0–1 链；违规 unwrap |
| 主体 | 任务句内链；每段 ≤1 |
| 结论 | 0–2 链；重复 slug unwrap |
| FAQ | **无链** |

### 5. 验收

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --locale both --violations-only
npm run verify:content-json && npm run build
python ../../clients/Alignify/scripts/audit/build-site-internal-links-doc.py
```
