# Oginify Platform Routing — CTA 与意图→落地页

> 加载时机：Phase 4 / Phase 5
> 主文件：SKILL.md §9 指针

---

## 1. CTA 分层

| 读者阶段 | 主 CTA 目标 | 说明 |
|---------|------------|------|
| Awareness | `/`（首页体验） | 让读者粘贴 URL 试试 |
| Tool selection | `/` 或对应工具页 | 引导生成 |
| Build | `/bulk-og-image-generator` 等 | 批量场景 |
| Publish | `/open-graph-validator` | 测试 meta tags |
| Diagnosis | `/open-graph-validator` | 检查为什么预览坏了 |

---

## 2. 意图→落地页路由

| 搜索意图 | 落地页 | 适用文章 |
|---------|--------|---------|
| best / top | `/`（首页展示 4 变体） | Ranking |
| how to create | `/`（三步流程） | HowTo |
| what is | `/blog/what-is-open-graph-image`（Hub） | Glossary |
| size | `/free-og-image-maker` | SizeGuide |
| meta tags | `/open-graph-validator` | MetaGuide |
| bulk | `/bulk-og-image-generator` | UseCase / ToolGuide |
| twitter card | `/twitter-card-generator` | ToolGuide |
| open source | GitHub（外链） | DeveloperGuide |

---

## 3. CTA 约束

- 单一主行动；正文 CTA ≤2 次
- 锚文本描述性（非 click here）
- 不链 `/pricing` 为主 CTA（G6 白名单允许但非首选；定价作正文事实而非 CTA）
- CTA 匹配读者阶段；无虚假承诺（P6）

---

## 4. 内链白名单（可链路径）

- 博客：`/blog/{slug}`（见 content-graph）
- 工具页：`/text-to-og-image` · `/image-to-og-image` · `/bulk-og-image-generator` · `/twitter-card-generator` · `/github-social-preview-generator`
- 检查页：`/og-scorer` · `/open-graph-validator` · `/free-og-image-maker`
- 探索：`/gallery` · `/explore`
- 首页：`/`

**G6 规则**：不链未上线路径；forthcoming ≤1 且仅脚注。
