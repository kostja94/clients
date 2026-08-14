# 02 — 操作 SOP

> **这一篇告诉你每天/每周/事件发生时该做什么。**  
> 下一步 → [03-data-guide.md](./03-data-guide.md)（数据从哪找）

---

## 日常（5–10 分钟，每天早上）

### 快速扫描

打开以下网站，扫一眼有没有新的**大公司裁员公告**：

1. [Layoffs.fyi](https://layoffs.fyi/) — 看首页最新条目
2. [TrueUp Layoffs](https://www.trueup.io/layoffs) — 交叉验证
3. 科技媒体头条（TechCrunch、The Verge、Reuters Tech）

### 判断：要不要新增公司页？

满足以下**至少 2 条**才新增：

- [ ] 裁员规模 ≥ 1,000 人
- [ ] 知名科技公司（FAANG 级别或知名度类似的）
- [ ] 有详细的公开信息（时间、原因、受影响部门）
- [ ] 搜索量可预期（公司名 + layoffs 有人搜）

**不满足条件** → 在 [data/layoff-data.md](./data/layoff-data.md) 中添加一行记录即可，暂不上线专属页面。

### 判断：要不要更新已有页面？

如果已有公司页的公司**又宣布了新一轮裁员**：
- 更新该公司的页面数据
- 在时间线中新增一条
- 更新聚合页的 YTD 总数

---

## 每周（30 分钟，每周一或周五）

### 1. 刷新聚合页统计数据

打开 [data/layoff-data.md](./data/layoff-data.md)，核对以下数字：

| 需更新的指标 | 数据来源 | 更新位置 |
|-------------|----------|----------|
| YTD 科技行业裁员总人数 | Layoffs.fyi 首页 | 聚合页 `LayoffsHeroSection` 组件 |
| 受影响公司总数（146 家） | Layoffs.fyi | 同上 |
| 日均裁员数 | 总人数 ÷ 当年已过天数 | 同上 |

### 2. 检查公司页数据新鲜度

快速过一遍有更新的公司 JSON 文件，看有没有：
- 数据还是上个月的老数字 → 查最新来源更新
- 引用的来源链接已失效 → 替换为有效链接

### 3. 查看搜索数据（可选，熟练后做）

在 Google Search Console 中查看：
- `/tech-layoffs` 聚合页 → 展示量和点击趋势
- `/tech-layoffs/{各公司}` → 哪些公司页有流量、哪些没有

---

## 事件驱动：大公司宣布裁员（24–48 小时内响应）

这是最高优先级的操作。当一家知名公司宣布大规模裁员时：

### 时间线

| 时间段 | 动作 |
|--------|------|
| **0–4 小时** | 在 [data/layoff-data.md](./data/layoff-data.md) 中新增数据记录（公司名、规模、时间、来源链接） |
| **4–12 小时** | 收集更多信息：原因（官方声明）、受影响部门、遣散方案、媒体报道 |
| **12–24 小时** | 用 [04-page-template.md](./04-page-template.md) 创建公司详情页、写 FAQ |
| **24–48 小时** | 部署上线（按 [05-deploy-guide.md](./05-deploy-guide.md)）、做 SEO 检查（按 [06-seo-checklist.md](./06-seo-checklist.md)） |

### 新增公司页 Checklist

```
□ 数据采集：规模、时间、原因、部门、来源链接
□ 创建 JSON 文件：按 04-page-template.md 模板 → src/data/companies/{slug}.json
□ 运行 npm run build：自动生成 barrel index + 构建验证
□ 数据验证：运行 Python 脚本确认所有字段完整、slug 匹配
□ SEO 检查：按 06-seo-checklist.md（JSON-LD 自动生成，重点检查 SEO 字段和 canonical）
□ git add + commit + push
□ 部署：按 05-deploy-guide.md Vercel 自动部署
□ 验证线上：先查 origin（vercel.app），再查主域（finalroundai.com）
□ 通知 Kostja：新页面已上线，附带公司名和 slug
```

---

## 每月（1–2 小时，月初）

### 1. 宏观趋势更新

- 本月新增裁员人数
- 本月受影响公司数
- 与上月的环比变化
- 行业分布变化（哪个行业裁员最多）
- 更新聚合页的「本月趋势」模块（如有）

### 2. 竞品内容扫描

打开 [reference/resources.md](./reference/resources.md) §2–§3 中的竞品页面，看他们有没有新增内容、新增了哪些公司页。如果有我们没覆盖但值得覆盖的 → 加入待建清单。

### 3. SEO 月度复盘

- 聚合页自然搜索展示量（目标：环比增长）
- Top 5 公司页的自然搜索展示量
- 哪些公司页有展示但点击率低（< 2%）→ 优化 Title/Description
- 哪些公司页完全没展示 → 检查是否被 noindex、canonical 是否正确

---

## 季度（每年 Q1 / Q3）

### 年度数据刷新

每年 Q1 和 Q3 做一次全面刷新：
- 所有公司页的「2026」→ 改年份引用（如适用）
- YTD 数据重置（新一年从 0 开始）
- 创建新一年的聚合页数据基准

---

## 快速参考：我该做什么？

| 我现在有… | 我该做… |
|-----------|---------|
| 15 分钟空闲 | 日常扫描 Layoffs.fyi |
| 30 分钟空闲 | 做周常：刷新聚合页统计 + 检查公司页新鲜度 |
| 刚看到 Meta 又裁了 5,000 人 | 启动「事件驱动」流程：先记数据 → 收集信息 → 更新页面 |
| 第一次操作 | 打开 [05-deploy-guide.md](./05-deploy-guide.md)，让 Kostja 带你走一遍 |

---

*下一步 → [03-data-guide.md](./03-data-guide.md) 了解数据从哪来、怎么验证*
