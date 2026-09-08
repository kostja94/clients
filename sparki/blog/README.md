# Sparki / Blog

本目录存放 Sparki（sparki.io）博客的内容规划与英文成稿（`*.md` + YAML frontmatter），按主题簇组织。正文风格与结构遵循自包含 skill [`sparki-blog-article`](../skills/sparki-blog-article/SKILL.md)（v1.1.0 · 9 Phase）。

## 目录结构

```
blog/
├── README.md                    ← 本文件
├── vlog-topic-cluster.md        ← Vlog 主题簇规划（选题、hub-spoke、发布节奏）
│
└── vlog/                        ← Vlog 簇（AI Vlog Editor，hub /vlog）
    ├── how-to-edit-a-vlog-with-ai.md
    └── how-to-edit-a-travel-vlog.md
```

## 约定

| 项 | 规则 |
|----|------|
| 语言 | 正文 en-US（上线稿为英文） |
| 命名 | `{slug}.md`；**无 NN 序号前缀**（sparki 特有，对比 luciusai/moras）；常青 slug 无年份 |
| frontmatter | `title/description/slug/date/author/category/tags`；`category` 取枚举（ai-video-editor 等）；`author: Sparki Team` |
| 落盘 | **成稿只放本工作区仓** `sparki/blog/{cluster}/{slug}.md`；不写入客户部署仓（部署/发布由单独流程处理） |
| 过程产物 | Brief / SelfCheck / Source Map 等辅助交付物**只进对话，不落盘**（生成完文章后不再保留） |

> 完整创作与质量门槛见 skill：`sparki-blog-article`（Phase 0–6、Gate A/0R/B/C、tools/ 三脚本、12 维 SelfCheck）。

## Vlog 簇

Hub：[`/vlog`](https://sparki.io/vlog)（AI Vlog Editor）· Canonical 品类词：[`what-is-a-vlog`]（部署仓已上线）

### 文章

| 文件 | Slug | 类型 | 状态 | 说明 |
|------|------|------|:---:|------|
| [vlog/how-to-edit-a-vlog-with-ai.md](./vlog/how-to-edit-a-vlog-with-ai.md) | `how-to-edit-a-vlog-with-ai` | WorkflowHowTo | 📝 成稿 | 双模态分类（对白 vs B-roll）+ 4 步工作流 + 工具决策表；簇内流程 canonical |
| [vlog/how-to-edit-a-travel-vlog.md](./vlog/how-to-edit-a-travel-vlog.md) | `how-to-edit-a-travel-vlog` | WorkflowHowTo | 📝 成稿 | C1 的 travel 实例化：行程时间线 → 每地 beats → recap + Shorts |

> 状态：📝 成稿（本地）→ 🚀 待发布（进入部署仓并置 `draft:false`）。当前两篇均为 📝，date 已占位（2026-09-09 / 2026-09-10 UTC，每自然日 ≤1 篇）。

## 相关文档（仓外）

| 文档 | 用途 |
|------|------|
| [../sparki.md](../sparki.md) | 产品定位与文档索引 |
| [../sparki-site-structure.md](../sparki-site-structure.md) | 站点结构与 /blog 路由 |
| [../sparki-keywords.md](../sparki-keywords.md) | 关键词梯队 |
| [../sparki-use-cases.md](../sparki-use-cases.md) | 受众与场景 |
| [../skills/sparki-blog-article/](../skills/sparki-blog-article/) | 创作 skill（references + tools） |
