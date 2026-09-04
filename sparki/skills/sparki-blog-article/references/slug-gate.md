# Sparki — Slug Design Gate B

> 加载时机：Phase 2
> 主文件：SKILL.md §3 Phase 2 指针

---

## 6 问检查

| # | 检查项 | 标准 | Fail 动作 |
|---|--------|------|----------|
| 1 | **含 primary keyword？** | slug 核心词与 target keyword 一致 | 改 slug 让关键词居前 |
| 2 | **通过"大声读"测试？** | 去掉连字符大声读 → 通顺 → Pass | 不通顺或含重复词 → 重选 |
| 3 | **不含禁词？** | guide / complete / ultimate / 2026 等年份 | 移除禁词 |
| 4 | **≤60 字符？** | 计数不含 `/blog/` | 缩短 |
| 5 | **常青无年份？** | 不含 2025/2026 等年份数字（历史旧文例外，新稿禁止） | 去年份 |
| 6 | **语义余量？** | 30% 内容变化后 slug 仍合适 | 改得更通用 |

## 文件名约束（sparki 特有，最高优先级）

- **文件名 = frontmatter `slug`**（去 `.md`）——`validate:posts` 硬性校验
- **无 NN 序号前缀**（对比：luciusai/moras 用 `NN-`，sparki 不用）
- 落盘：`E:\客户部署项目\sparki-blog\content\blog\{slug}.md`

---

## 12 反模式（创作阶段必检）

| # | 反模式 | 错误示例 | 正确示例 |
|---|--------|---------|---------|
| 1 | 含年份 | `ai-video-editor-2026` | `ai-video-editing-agent-vs-tools` |
| 2 | 含数量 | `top-5-ai-video-editors` | `best-ai-video-editors` |
| 3 | 连续重复词 | `video-editor-editor` | `ai-video-editor` |
| 4 | 内部架构词泄漏 | `sparki-agent-framework` | `how-ai-video-editing-agents-work` |
| 5 | 品牌名前置 | `sparki-caption-workflow` | `ai-caption-workflow` |
| 6 | 过多词 | `how-to-edit-a-vlog-like-a-professional-creator` | `edit-vlog-15-minutes-smart-cut`（风格参考，非字面） |
| 7 | 空洞词 | `complete-guide` / `ultimate` | 用描述性词替代 |
| 8 | 过于营销 | `best-ai-video-editor-ever` | `ai-video-editor-vs-human-editor` |
| 9 | 含特殊字符 | `caption_workflow` / `CaptionWorkflow` | `caption-workflow` |
| 10 | 过于具体时效 | `sparki-summer-sale-2026` | 避免营销时效 slug |
| 11 | misleading | `free-ai-video-editing`（若含付费层） | `ai-video-editing-free-tier-vs-paid` |
| 12 | 与既有 slug 混淆 | 太接近 content-graph 中某 slug | 用更区分的关键词 |

---

## Slug 命名规范

| 规则 | 说明 |
|------|------|
| 格式 | kebab-case；全小写 + 连字符；**文件名 = slug** |
| 长度 | 4–9 词；≤60 字符 |
| 关键词 | 含 primary keyword 核心词 |
| 常青 | 不含年份、版本号 |
| 品牌名 | 不前置（例外：`sparki-vs-{tool}` Comparison 类沿用既有惯例） |
| CreatorClone | `how-to-edit-{format}-like-{creator}` / `how-to-master-{content}-like-{creator}`（对照 2A 查重） |

---

## Title 公式

- CreatorClone：`How to Edit {Style/Content} Like {Creator}`
- WorkflowHowTo：`How to {Task} — {Benefit/Workflow}`
- FeatureGuide：`{X}: How to Pick the Right Workflow`
- Comparison：`{A} vs {B} — {Frame}`；含 Sparki：`{A} vs {B} vs Sparki: …`
- AlternativeRoundup：`{Tool} Alternative — {Why/Angle}` / `Best {Category} Alternatives`
- CategoryPOV：问题式/观点式（`Can AI {Verb}…?`）
- Announcement：`Introducing {Feature} — {Value}`

Meta description：120–160 chars（validate 80–320）· benefit + main intent keyword + 差异化一句。

---

*slug-gate · sparki v1.0.0 · 2026-09-04*
