# Topic Cluster 文件布局 — 主题子目录 vs 根目录

> 本地 Markdown 仓库的组织约定。**公开 URL 始终扁平**：`/blog/{slug}`，与文件是否在子目录无关。
> 参考实现：`e:\clients\floatboat\blog\`（`claude/`、`deepseek/`、`worldcup/` + 根目录散放）。

---

## 1. 两种布局

| 布局 | 本地路径示例 | 公开 URL | 适用 |
|------|-------------|----------|------|
| **根目录** | `blog/07-ai-follow-up-automation.md` | `/blog/ai-follow-up-automation` | 独立单篇、未归入命名簇、或簇尚未建子目录 |
| **主题子目录** | `blog/claude/35-what-is-claude-cowork.md` | `/blog/what-is-claude-cowork` | 已注册主题簇内的 Hub / Spoke |

**关键**：子目录仅用于**本地组织与 content-graph 维护**；内链、slug、frontmatter 中的路径一律用 `/blog/{slug}`，**不含**子目录名。

---

## 2. 全局序号 NN（跨目录连续）

- 文件名格式：`NN-{slug-kebab}.md`
- **NN 全 blog 递增**，不按子目录重置
- 示例：根目录 `07-…` 之后，DeepSeek 簇可从 `41-…` 开始；Claude 簇 `35-…` 可与 World Cup `09-…` 交错

下一序号以项目 `content-graph.md` 的「下一序号」为准，**不**以子目录内文件数为准。

---

## 3. 何时用主题子目录

Phase 0 / Phase 2 对照 `content-graph.md` 的 **Cluster 注册表** 决定：

| 条件 | 动作 |
|------|------|
| 文章属于已注册簇，且 content-graph 声明了 `folder: {cluster-id}/` | 写入 `blog/{cluster-id}/NN-{slug}.md` |
| 文章 standalone，或簇无 folder 字段 | 写入 `blog/NN-{slug}.md`（根目录） |
| 新簇规划 ≥2 篇且主题边界清晰 | 人类在 content-graph 注册 cluster + folder；首篇即可建子目录 |
| 仅 1 篇、无后续 spoke 计划 | **默认根目录**（如 MiniMax H3 单篇 `45-what-is-minimax-h3.md`） |

### Floatboat 参考映射

| 子目录 | 主题簇 | 示例 |
|--------|--------|------|
| `claude/` | Claude Cowork / Tag / Code | `35-what-is-claude-cowork.md` |
| `deepseek/` | DeepSeek Agent / Harness / V4 | `41-what-is-deepseek-agent.md` |
| `worldcup/` | World Cup 2026 | `09-world-cup-2026-guide.md` |
| *(根目录)* | Scheduling Agent 系列 | `02`–`07`（含 `07-ai-follow-up-automation.md`） |
| *(根目录)* | Model 单篇 | `45`、`51`、`53`–`55` |
| *(根目录)* | 其他 standalone | `01-introducing-floatim-2026.md` |

---

## 4. frontmatter 与簇分类（可选模式）

部分站点在子目录内使用**双分类** frontmatter：

```yaml
# claude/ 内文章
category: "Claude"              # 簇主分类（= folder 主题名）
secondaryCategory: "Research"   # 文章形态分类

# 根目录 scheduling 文
category: "Product"             # 仅主分类，无 secondaryCategory 亦可
```

是否在子目录内覆盖 `category` 为簇名——**由项目 skill 的 `article-types.md` / `content-graph.md` 声明**，通用引擎不强制。

---

## 5. Phase 0 / Phase 2 输出

Phase 0 首行追加（若项目启用 cluster layout）：

```
## Cluster: {cluster-id | standalone}
## File path: blog/{cluster-id}/NN-{slug}.md | blog/NN-{slug}.md
```

Phase 2 Gate B 校验：

- [ ] NN 与 content-graph「下一序号」一致
- [ ] 路径与 cluster 注册表一致（有 folder → 必须在子目录；standalone → 必须在根目录）
- [ ] slug 不含子目录前缀（❌ `claude/what-is-x`，✅ `what-is-x`）
- [ ] 内链仍写 `/blog/{slug}`，不写 `/blog/claude/{slug}`

---

## 6. content-graph 注册表（项目 skill 必含字段）

项目 `content-graph.md` 建议维护：

```markdown
| Cluster ID | folder | Hub slug | 说明 |
|------------|--------|----------|------|
| scheduling-agent | *(root)* | what-is-agentic-calendar | 02–07 根目录 |
| claude | claude/ | what-is-claude-cowork | 35–49 |
| deepseek | deepseek/ | what-is-deepseek-agent | 41–44, 46, 50, 52 |
| worldcup | worldcup/ | world-cup-2026-guide | 09–19 |
| model-singles | *(root)* | — | 45, 51, 53–55 单篇 |
```

未注册 cluster → 默认 **standalone → 根目录**。

---

## 7. 与 vomo / 2mv 等差异

| 项目 | 布局 |
|------|------|
| floatboat | 根目录 + 主题子目录 |
| 多数 client（medo、qveris…） | 仅 `blog/NN-{slug}.md` 扁平 |
| vomo | `vomo/blog/` 或 `/guide/` 前缀，通常无子目录 |
| 2mv | `/insights/` 前缀，扁平 |

项目 skill 在 `project-config.md` 声明 `blogLayout: flat | cluster-folders`；默认 **flat**。

*topic-cluster-layout · v1.0 · 2026-08-23 · ref: floatboat/blog*
