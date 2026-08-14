# Meta Title / Description（博客专用）

> 独立优化任务入口：用户要求"仅优化 title/description"时，**只读本文件**执行工作流；禁止改正文 H2 / TL;DR / FAQ 之外的正文结构。
> **v1.1 变更**：`title` 已移到正文 `# H1`；frontmatter 只有 `metaTitle`/`description`。独立任务可改 frontmatter `metaTitle`/`description` 与正文 `# H1`。

## 长度基准

| 字段 | 位置 | 目标区间 | 硬限 | 说明 |
|------|------|---------|------|------|
| `title` | 正文 `# H1` | 45–70 字符 | 45–90 | 含主关键词；品牌后缀放 metaTitle |
| `metaTitle` | frontmatter | ≤70 字符 | — | 以 `\| QVeris` 结尾；SERP 展示 title |
| `description` | frontmatter | 120–160 字符 | 100–280 | 收益 + 关键词 + 数据时效（如含行情） |
| `excerpt` | 正文 H1 后首段 | 2–3 句 | ≥40 字符 | 斜体引言，可复用 description 扩充 |

## 规则

1. **正文 H1 title** 前端放主关键词（对齐 SERP 点击习惯）；避免标题党（clickbait 与 QVeris 专业调性不符）
2. **metaTitle** 复用正文 H1 title + `| QVeris` 后缀；超 70 字可截断前部
3. **description** 首句给答案/收益，次句给独特性（数据规模/时间窗/方法）；金融文含 `as of {date}` 语境
4. **excerpt** 与 description 不同——excerpt 是读者进入页面后读到的引言，比 description 更口语、更可执行
5. 禁用全部大写、连续感叹号、emoji
6. 与已发文章 title 不重复（对照 `content-graph.md`）

## 四条自检（写完逐条打勾）

- [ ] 正文 H1 含 primary keyword（工具 `--keyword` 校验）
- [ ] 正文 H1 45–70 字符
- [ ] description 120–160 字符
- [ ] metaTitle 以 `| QVeris` 结尾且 ≤70 字符

## 独立优化工作流（title-only 任务）

```
1. 读目标文章 frontmatter（metaTitle/description）与正文 # H1、excerpt 段
2. 对照 §长度基准 + §规则
3. 生成 2–3 组候选，标推荐（每组含：正文 H1、metaTitle、description、excerpt）
4. 跑四条自检 → 交付候选（不改正文 H2/结构）
5. 提示人类确认后手动替换
```
