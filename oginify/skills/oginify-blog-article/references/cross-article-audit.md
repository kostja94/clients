# Oginify Cross-Article Audit — CA1–CA10

> 加载时机：Phase 5.5（同批 ≥2 篇触发）
> 主文件：SKILL.md §3.5.5 指针

---

## 1. 触发条件

同批规划或并行创作 **≥2 篇**（同一 cluster、同一 campaign、或 content-graph 排期相邻）。

---

## 2. 检查项 CA1–CA10

| # | 检查点 | 检测方法 | Fail 示例 |
|---|--------|---------|----------|
| CA1 | 叙事模式雷同 | 多篇是否共享相同叙事弧？3+ 篇 → 标记 | 3 篇都是「定义→列表→对比→FAQ→CTA」 |
| CA2 | 互链双向 | 新文互链是否双向？ | A 链 B 但 B 不链 A |
| CA3 | 产品描述重复 | 同 cluster 产品描述重复率 >30% | 两篇都整段复述 Oginify 机制 |
| CA4 | Intro 模板化 | 多篇 intro 是否共享相同函数序列？ | 定义句→场景句→路标句→数据句 |
| CA5 | Conclusion 模板化 | 多篇 conclusion 是否可互换首段？ | 都是「总之 Oginify 最好」 |
| CA6 | 核心概念跨篇重复 | 每概念是否只有一篇 canonical？ | 两篇都展开 1200×630 完整定义 |
| CA7 | 事实矛盾 | 同 cluster 数字/版本/定价是否矛盾？ | 一篇写 6 张/天一篇写 5 张/天 |
| CA8 | 关键词 Cannibalization | 两篇是否抢同一 P0 词？ | 两篇 title 都含 "best OG generators" |
| CA9 | 表现形式雷同 | 列表/表格占比模式是否雷同？ | 都是 50% 列表 |
| CA10 | 署名一致性 | 同一 cluster 作者署名是否一致？ | 一篇 Oginify 一篇 Kostja 混用 |

---

## 3. 判定与处置

| 结果 | 处置 |
|------|------|
| 任一 ❌ | 批量交付前必修 → 改文或标注差异原因 |
| 全 Pass | 输出 `Cross-Article Audit: PASS — {slugs}` |

---

## 4. Canonical 引用规则

| 概念 | Canonical | 引用方式 |
|------|-----------|---------|
| Open Graph image 定义 | `what-is-open-graph-image`（Hub） | 1–2 句 + link |
| 1200×630 规格 | Hub H2 + ogp.me | 1 句 + link 或 P3 来源 |
| 三分类框架 | `best-ai-og-image-generators` | 1 段 + link |
| 尺寸指南 | `open-graph-image-size` | SizeGuide canonical |
| meta tags | `open-graph-meta-tags-guide` | MetaGuide canonical |
