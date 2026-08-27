# 品牌词拆分

配置：`config/brand-query-registry.yaml`

---

## 规则

1. 对 `gsc.queries[]` 每条 query 做 classify  
2. **branded**：命中 `brandGroups[].patterns`  
3. **competitor**：命中 `competitorBrandTerms`（标记，不计 branded）  
4. **category**：命中 `categoryTerms`（计入 nonBranded，可单独看 category 汇总）  

匹配默认：忽略大小写、去标点。

---

## merge 输出

| 字段 | 说明 |
|------|------|
| gsc.branded.clicks / share | 品牌词点击及占比 |
| gsc.nonBranded | 非品牌（含 category） |
| queries[].isBranded | 行级标记 |

---

## 注意

- 品牌 regex **过宽** → branded 占比虚高  
- 仅看 overall 不看 branded/nonBranded → 易误判 SEO 拉新效果  
- sitelinks、SSR 框架导致品牌词波动 → 结合 `===OBSERVATIONS===` 人工说明  

---

## 示例 patterns

```yaml
brandGroups:
  - id: main
    label: 主品牌
    patterns:
      - acme
      - acme app
```
