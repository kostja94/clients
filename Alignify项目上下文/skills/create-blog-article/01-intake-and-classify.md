# Step 1 — Intake & 文章分类（Gate A）

> **定位**：创作流水线的前置门控。确认知识块合规、判定文章类型、选择 Meta 规则组、注册 slug 到关键词表和 README。
> **产出**：文章类型判定 + Gate A 通过 + 关键词表更新 + README 条目

---

## Gate A：独立成文判定

在开始创作之前，确认以下条件全部通过：

- [ ] **知识块已创建**：`knowledge/{tools,marketing,seo,insights}/{slug}.md` 文件存在
- [ ] **知识块通过对应模板核对**：
  - tools → 核对 `knowledge/tools/_TEMPLATE.md` 的 13 项清单
  - marketing → 核对 `knowledge/marketing/` 现有文件的结构字段完整性
  - seo → 核对 `knowledge/seo/` 现有文件的结构字段完整性
  - insights → 核对 `knowledge/insights/README.md` 的文档结构要求
- [ ] **slug 未在 blog-pages-config.ts 中注册过**
- [ ] **与现有文章无 cannibalization 风险**：在部署仓 `content/blog/` 中搜索同类主题，确认本 slug 有独立的搜索意图
- [ ] **Investment Score ≥ 3.0**（见下方计算方式）

若任何一项 ❌ → 回退。完成知识块补充后再回到 Gate A。

---

## 文章类型判定

### 判定逻辑

```
知识块在 knowledge/tools/     → Tools 榜单/对比型
知识块在 knowledge/marketing/ → Marketing 策略/案例型
知识块在 knowledge/seo/       → 视内容偏工具选型/策略方法而定
知识块在 knowledge/insights/  → Insights 行业分析型
```

### 判定后产出

| 判定项 | 需要确认的内容 |
|--------|--------------|
| **文章类型** | Tools / Marketing / SEO / Insights |
| **routeCategory** | `"tools"` 或 `"marketing"` |
| **Meta 规则组** | Best 型 / 策略型 / 指南型 / 分析型 |
| **hubCategory** | toolsHubCategory 或 marketingHubCategory 的具体值 |

---

## Investment Score 五因子

| 因子 | 1–5 分 | 权重 |
|------|--------|------|
| **搜索需求** | 目标关键词月搜索量估计 | 1× |
| **商业相关性** | 对 Alignify 转化路径的直接度 | 1× |
| **差异化能力** | 相比 SERP 已有内容的独特增量 | 1× |
| **证据可得性** | 可用数据/案例/一手素材丰富度 | 1× |
| **内容生命周期** | 1 年内不过时的概率 | 1× |

**算术平均** ≥3.0 为通过 Gate A。

---

## 关键词注册

### 在关键词文件中新增 slug

**Tools 类** → 在 `alignify-keywords-tools.md` 新增：

```markdown
### your-slug

**意图**：[用户搜索此主题时想解决的核心问题]

**关键词表**：

| 主关键词 | 搜索量 | 竞争度 |
|---------|--------|--------|
| ...     | ...    | ...    |

**目标 URL**：`/zh/blog/your-slug`

**数据源**：`knowledge/tools/your-slug.md`
```

**Marketing / SEO / Insights 类** → 使用对应的关键词文件或创建新表。

### 在知识块目录 README 新增条目

按字母序插入 slug 条目，含分流说明（与相邻 slug 的主题区分）。

---

## 输出清单

- [ ] 文章类型：_______
- [ ] routeCategory：_______
- [ ] Meta 规则组：_______
- [ ] hubCategory 值：_______
- [ ] Investment Score：\_\_\_\_ (≥3.0 ✓)
- [ ] 关键词表已更新
- [ ] README 条目已新增
- [ ] `blog-pages-config.ts` 中确认不存在此 slug

---

*01-intake-and-classify.md · v1.0 · 2026-07-16*
