# 周报 Markdown 模板

Agent 输出路径：`reports/{project-id}-seo-weekly-{YYYY-MM-DD}.md`

---

```markdown
# SEO 周报 · {站点名} · {current.start} ~ {current.end}

> 数据来源：{api-auto|manual} · 健康检查：{D0-D5 摘要一句}

## 0. 执行摘要
- GSC 点击 {current} vs {previous} ({pct})
- 品牌/非品牌要点一句
- 本周最重要动作与发现

## 1. 数据健康
| 项 | 结果 | 说明 |
（填 D0-D5 表）

## 2. 搜索总览（GSC）
### 2.1 整体
### 2.2 品牌 vs 非品牌
### 2.3 Top queries 变化
### 2.4 Top pages 变化

## 3. 站内行为（GA4）
### 3.1 渠道结构
### 3.2 Top 落地页
### 3.3 Key events

## 4. 搜索 × 落地交叉
（GSC pages × GA4 topPages，注明 d4 覆盖率）

## 5. Bing 双引擎（若 d3_bingPresent）
### 5.1 整体对比 GSC
### 5.2 Crawl issues（若有）

## 6. AI / 引荐流量（若有 aiAssistant 数据）
（GA4 AI Assistant 渠道；Bing AI Performance 若手动 CSV 可附）

## 7. 本周内容与搜索表现
（===CONTENT=== + catalog 若有）

## 8. 外链与引荐
（===BACKLINKS===）

## 9. 本周执行与下周计划
（===PROJECT_STATUS=== + ===OBSERVATIONS===）

## 附录
- 周期定义
- 降级/跳过章节说明
```

---

## 写作原则

- 中文正文；URL、事件名、渠道英文名保留  
- 每个结论指向 bundle 字段或手动块，不编造数字  
- 环比用 `pctChange` 或自行计算，标注 %  
- 早期站点 0 点击须写「基数低，观察趋势而非绝对值」  
