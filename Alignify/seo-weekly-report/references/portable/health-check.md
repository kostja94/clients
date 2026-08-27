# 数据健康检查 D0–D5

报告生成前必须检查。自动化模式读 `healthCheck`；手动模式人工对照。

| ID | 检查项 | 通过标准 | 失败处理 |
|----|--------|----------|----------|
| **D0** | 数据来源 | bundle 存在且 `source=api-auto` | 标注「手动数据」，降级部分章节 |
| **D1** | 周期对齐 | current/previous 各 7 天 Mon–Sun；与手动块 week 一致 | 暂停生成，修正 `REPORT_WEEK_END` |
| **D2** | GSC 维度 | pages、queries、countries、devices 均有行 | 缺则标注「§X 无法生成」 |
| **D3** | GA4 / Bing | `d3_ga4Present` / `d3_bingPresent` | 无 GA4 跳过行为章节；无 Bing 跳过双引擎章 |
| **D4** | 页面对齐 | `d4_pageOverlapRate` ≥ 配置阈值（默认 0.2） | 文首 ⚠️ 覆盖率低，交叉视图谨慎解读 |
| **D5** | 量级 | GSC 周点击在 project-config.health 区间 | ⚠️ 可能导出错周期/属性 URL 错误 |

---

## 多源对账要点

| 现象 | 原因 |
|------|------|
| GSC 点击 ≠ GA4 Organic sessions | 定义不同；GA4 含 JS 拦截、采样 |
| query 维度加总 < overall | **匿名 query 过滤**（约半数 query 被隐藏） |
| Bing URL 字段名 Query | 实为 page URL，需 stripDomain 后与 GSC 对齐 |
| 双计 | 页面硬编码 gtag + GTM 同时存在 |

**三角验证**：GSC（搜索侧）+ GA4（到站行为）+ Bing（第二搜索引擎）趋势同向即可；不要求数值相等。
