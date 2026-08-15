# 单页优化 Checklist

参照 `apply-agent-sandbox-links.py` 模式。**必须遵守 R-LINK-ONLY**（§1.5.4 第 8 条）。

## 禁止清单（Agent 必读）

- 禁止删除「Related tools include…」整段
- 禁止 FAQ 答案从长段缩成 2 句
- 禁止用「Next steps: …」一句替换结论第三段
- 禁止未读 `git show HEAD:` 就对 useCases / `technologyBase` 做 StrReplace
- 禁止为满足 R1 用短 description 替换 useCases 全文

## 1. 审计现状

```bash
python ../../项目文档/Alignify项目上下文/scripts/audit/audit-tools-internal-links.py --slug {slug} --locale both
```

记录：违规规则编号 + JSON 字段路径。

## 2. 建立 baseline

```bash
git show HEAD:content/tools/en/{slug}.json   # 对将改字段核对原文
```

## 3. 选链

- [ ] 读附录 B 邻居行 + keywords 表
- [ ] 正文目标 5–8 distinct；FAQ 0–3（不与正文 slug 重复）
- [ ] Blog 邻居可能是 `/tools/` 或 `/blog/`
- [ ] EN/ZH 目标 slug 集合对称

## 4. 分配区块（只改 `<a>`）

| 区块 | 动作 |
|------|------|
| TL;DR introduction | **0–1 链**；违规时删/移 `<a>`，**不重写 intro  prose** |
| 什么是 · 第二段 | Hub 辐条首次链；Spoke 邻居；与 TLDR 零交集 |
| useCases | R1 不足时在**现有句**外包链或段末加 1 句 |
| howItWorks / howToChoose | 0–1 链；禁止重复 section 已链 slug |
| 结论 | 重复 slug **unwrap**；保留叙述；可保留 `/tools` 目录 |
| FAQ | 重复 slug unwrap；≤3 新 slug |

## 5. 写入 JSON

```bash
python scripts/permanent/patch-tools-internal-links.py --slug {slug} --locale both --yaml patches/{slug}.yaml
```

或 `unwrap-duplicate-internal-links.py` + 手工 ≤5 处 StrReplace。

**禁止** Agent 无 baseline 对大型 JSON 整段 Write/StrReplace。

## 6. 台账

- [ ] 更新附录 C（§blog-* 或 §tools-*）
- [ ] 专册修订日志一行

## 7. 验收（顺序固定）

```bash
npm run audit:internal-links
npm run audit:text-regression
npm run verify:content-json
npm run build
```

- [ ] high = 0
- [ ] text-regression：无字段 ≥25% 缩水（≥200 字原字段）、无文件 ≥2% 缩水
- [ ] spot-check：结论/FAQ 仍含产品说明，非只剩 Next steps
