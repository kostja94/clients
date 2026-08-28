# Eval — Forbidden Loads

> Agent 执行 `datus-blog-article` 时 **不得** 读取以下路径。违反 → eval Fail。

## Forbidden paths

| Path pattern | Reason |
|--------------|--------|
| `datus/datus.md` | 策略源；已 distilled 至 references |
| `datus/datus-*.md` | 外部策略文档 |
| `datus/blog/README.md` | 人类维护；序号在 content-graph.md |
| `datus/blog/internal-external-links-checklist.md` | 规则在 presentation.md |

## Allowed paths

| Path | When |
|------|------|
| `datus/skills/datus-blog-article/SKILL.md` | 默认 |
| `datus/skills/datus-blog-article/references/*.md` | Phase 按需 ≤2 |
| `datus/skills/datus-blog-article/references/portable/*.md` | 按 Phase 指针 |
| `datus/blog/**/*.md` | 仅当用户明确要求对照已发布成稿（非默认 Phase 流程） |

## Eval procedure

1. 启动任务：为 `lakehouse` 创建 GlossaryTerm 文章
2. 检查 Agent 读取列表
3. **Pass**：仅 skill 文件夹内文件
4. **Fail**：出现任一 forbidden path
