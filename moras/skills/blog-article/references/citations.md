## §12 证据链与引用标准

将 §5.2 的 P0/P1/P2 分级扩展为完整引用维度。**本维度为创作硬约束（Phase 5 健康分评估维度 #1 — Fact/E-E-A-T）**。

### 12.1 引用分级细化

| 级别 | 触发条件 | 要求 | 示例 |
|------|------|------|------|
| **P0 必须引用** | 任何可外部验证的量化声明 | 链接到原始来源（官方报告/docs/一手数据页）。跨篇出现时每篇都要链。 | "$15.8B US GMV"、"73% 创作者 <$50/月" |
| **P1 应当引用** | 行业趋势、产品能力、竞品状态 | 官方 docs/GitHub/Changelog。常识可加限定词不链。 | "归因窗口 typically 7 days"（+as of date） |
| **P2 可不引用** | 内部 benchmark、框架逻辑推演、衍生分析 | 注明方法论或 "internal observation, n=X"。框架本身不需 citation。 | "CTR >3% 好（internal, n≈200）" |

### 12.2 "怀疑测试"与"竞争对手测试"

- **怀疑测试**：持怀疑态度的读者看到数字，第一反应是"你怎么知道的？"——如果不能用"这是本文框架/分析方法"回应 → 需要引用
- **竞争对手测试**：竞品内容团队能否用这个数字质疑可信度？能 → 需要引用

### 12.3 引用格式标准

**P0 数字**（锚文本语义化）：
> TikTok Shop US crossed **$15.8 billion in GMV in 2025**, according to [Reuters' reporting on TikTok Shop's 2025 performance](https://www.reuters.com/...).

**P1 政策/趋势**（官方 docs + as of）：
> TikTok Shop Affiliate requires 5,000 followers for standard application, per [TikTok Shop Seller Center](https://seller.tiktok.com/), as of June 2026.

**内部数据**（n + 时间 + 限定）：
> Based on internal analysis of ~200 top-performing shoppable videos across kitchen and beauty categories in Q1 2026, videos with click-through rates above 3% were 4× more likely to generate repeat commission events.

**反模式**：裸数字无来源；"studies show"/"industry reports indicate"泛引；锚文本 "click here"/"source"。

### 12.4 跨篇数字一致性

同一数字跨篇出现（$15.8B GMV、73% <$50/月 等）：
- 每篇文章都要给引用链接（不能 Pillar 链了、Spoke 裸引）
- 数字精度完全一致（$15.8 billion vs $15.8B → 统一格式）
- Canonical 定义在 Pillar 文（最完整上下文）。Spoke：数字 + 链接 + 1 句上下文

### 12.5 政策敏感性声明

TikTok Shop 准入门槛、佣金率、归因窗口：
- 引用官方 doc + `updated` 字段反映最后验证日期
- 标注 "as of {month} {year}"
- 超过 90 天未更新 → 视为"可能过时"

### 12.6 Source Map（融入 Phase 6）

创作 SelfCheck 时生成（内部留存，不随文发布）：

```markdown
## Source Map
| Claim | § | Source | Checked | Confidence |
|------|------|------|------|:---:|
| TikTok Shop US $15.8B GMV (2025) | §2 | Reuters | 2026-06-15 | High |
| 73% creators under $50/mo | §1 | TikTok Transparency Report | 2026-06-15 | High |
| Affiliate CTR >3% good | §7 | Internal, n≈200 videos | 2026-06-15 | Medium |
```

Confidence: High = 官方一手 / Medium = 第三方 + 内部 n≥100 / Low = 单案例。**Low 不得用于核心论证**。


