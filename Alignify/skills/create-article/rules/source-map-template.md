# Source Map 与 EEAT

> Step 10 交付物（**内部**，不发布）。Draft 新增 claim 须补行。

---

## Source Map 模板

```markdown
## Source Map — {slug}

| Claim | Section / ¶ | Source URL | Checked | Confidence |
|-------|---------------|------------|---------|:----------:|
| {产品} 定价 $X/月 | Best H3 | 官方 pricing | YYYY-MM-DD | High |
| {竞品} 不支持 {能力} | 对比表 | 官方 docs | YYYY-MM-DD | High |
```

**Confidence**：High / Medium / Low — **Low 不得用于核心论证或 P0 数字**

须与 Research Log §R3 一致。

**References 边界（策略/Blog 文）**：Source Map 可含竞品 docs 等类型 C 来源；**仅 A/B 类**写入底部 References 列表（见 `sections/references.md` §3.2）。

---

## EEAT 六项（SelfCheck 速查）

| # | 检查项 | Pass 标准 |
|---|--------|----------|
| E1 | 量化数据有来源 | 数字可追溯到 URL 或官方文档 |
| E2 | 竞品信息可核实 | pricing/状态/能力基于官方 docs |
| E3 | 时效性 | 定价/政策 as-of 日期；GA/Preview 标注 |
| E4 | 无绝对化营销语 | 无 unsupported「最好/唯一/碾压」 |
| E5 | 准确率/ROI | 有依据或改写为定性 |
| E6 | 诚实推荐 | ≥1 场景非榜首产品更合适（Tools 对比文） |

---

*source-map-template · v1.0 · 2026-08-26*
