# Golden Brief — E10 medo-vs-lovable（Alternative / #29）

> eval-manifest E10 的 golden 输入样例。变更路由表、Gate A、content-graph 序号或 Mini-Example 后，用本输入回归验证 #29 仍路由为 KEEP + 序号 29。

## 输入（触发语）

```
按 medo-blog-article skill，为关键词 "MeDo vs Lovable" 创建一篇 Alternative 文章。
发布目的：SEO + Conversion。目标读者：有移动 App 想法、在 MeDo 与 Lovable 间选型的非开发者。
Mode：standard（未指定默认）。
```

## 期望路由（断言）

- **ArticleType** → `Alternative`（`vs` / `alternative` 意图 → §2 路由表）
- **GrowthFunction** → `SearchCapture`
- **Cluster** → C2 对比选择；`Cluster ID: ai-mobile-app`；Cluster role: Spoke
- **Pillar link** → `/blog/how-to-build-mobile-app-with-ai`
- **Gate A** → KEEP
  - 搜索意图独立：`medo vs lovable` 无已有文（content-graph §5）
  - 读者阶段：Tool selection（Evaluation）
  - 深度不可压缩：native-vs-wrap 论证 >800 词
- **信息增量（≥1，Phase 0R R2+R3 验证）**：
  1. Native Swift/Kotlin vs Lovable Capacitor web-wrap 深度对比
  2. QR 真机测试 / TestFlight 路径 vs 额外 wrap 步骤
  3. Wirecutter 式：≥1 Lovable 优势场景（A3）
- **文件序号 / 路径** → `medo/blog/29-medo-vs-lovable.md`（下一文件序号 29）
- **Mode** → standard（Alternative 默认；产品提及 ≤45%）
- **词数** → 2000–2800
- **A4** → title 可用 `MeDo vs Lovable`（对比词允许）；不得抢 `ai mobile app builder` 工具页词
- **A3** → §6 须含 "When Lovable is the better choice"（Web SaaS / landing 场景）

## 防回归断言

- [ ] Phase 0 首行 `ArticleType` 输出为 `Alternative`（非增长职能枚举）
- [ ] `GrowthFunction` 独立标注 `SearchCapture`
- [ ] 未读 skill 文件夹外文档
- [ ] mini-example.md 仍是 #29 范例（若已改 #30，更新本文件头部说明）

---

*golden-brief medo-vs-lovable · eval E10 · 2026-09-09*
