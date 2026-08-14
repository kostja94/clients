# Floatboat Blog Schema — ARCHIVED / DO NOT USE

> **状态：已停用（2026-07-28）**
>
> Agent **禁止**生成 `floatboat/blog/schema/{slug}.json`（JSON-LD）。
> 结构化数据若需要，由 **CMS / 站点侧**处理，不在 `floatboat-blog-article` 成稿交付物内。
>
> 本文件仅作历史归档；创作时 **不要加载** 本文执行 Phase 6 schema 步骤。
> 现行规则见 `../SKILL.md` §0 交付物表（「禁止」条）与 Phase 6 第 4 步。

---

## 变更说明

| 之前 | 现在 |
|------|------|
| Phase 6 产出 `blog/schema/{slug}.json` | **不产出** |
| Ranking 要求 ItemList JSON-LD 文件 | 正文结构 + `articleFormat: Ranking` 即可 |
| 参考 `floatboat-blog-schema.md` 生成 FAQ/HowTo/Breadcrumb | 由站点实现；Agent 只保证正文含 FAQ 等可抽取内容 |

历史 JSON 样例可留在 `floatboat/blog/schema/`，**禁止新增** JSON-LD 文件。Source Map / SelfCheck 等非 JSON-LD 文档不受此禁令约束（若团队仍放在同目录）。

---

*Archived from floatboat-blog-schema · v1.0.0 · 2026-06-17 · retired 2026-07-28*
