# Topic Cluster 文件布局 — 主题子目录 vs 根目录

> 本地 Markdown 仓库的组织约定。**公开 URL 始终扁平**：`/blog/{slug}`，与文件是否在子目录无关。
> **本文件随 floatboat-blog-article skill 分发**，不依赖 skill 文件夹外路径。

---

## 1. 两种布局

| 布局 | 本地路径示例 | 公开 URL | 适用 |
|------|-------------|----------|------|
| **根目录** | `blog/07-ai-follow-up-automation.md` | `/blog/ai-follow-up-automation` | 独立单篇、未归入命名簇 |
| **主题子目录** | `blog/claude/35-what-is-claude-cowork.md` | `/blog/what-is-claude-cowork` | 已注册主题簇内的 Hub / Spoke |

**关键**：子目录仅用于**本地组织**；内链、slug 一律 `/blog/{slug}`，**不含**子目录名。

---

## 2. 全局序号 NN（跨目录连续）

- 文件名格式：`NN-{slug-kebab}.md`
- **NN 全 blog 递增**，不按子目录重置
- 下一序号以 `content-graph.md` 为准

---

## 3. Phase 0 / Phase 2 输出

```
## Cluster: {cluster-id | standalone}
## File path: floatboat/blog/{folder}NN-{slug}.md | floatboat/blog/NN-{slug}.md
```

Phase 2 Gate B 校验：

- [ ] NN 与 content-graph「下一序号」一致
- [ ] 路径与 cluster 注册表一致
- [ ] slug 不含子目录前缀
- [ ] 内链仍写 `/blog/{slug}`

---

## 4. Floatboat Cluster 映射

详见 `content-graph.md` §1B。摘要：

| 子目录 | 主题簇 |
|--------|--------|
| `claude/` | Claude Cowork / Tag / Code |
| `deepseek/` | DeepSeek Agent / Harness |
| `openai/` | OpenAI 模型族 / Codex Harness |
| `voice/` | Voice × Agent（dictation / voice agent） |
| `worldcup/` | World Cup 2026 |
| `Updates/` | 产品公告与内置能力 |
| *(根目录)* | Scheduling Agent 02–07、Model 单篇等 |

*topic-cluster-layout · v1.0 · floatboat · self-contained*
