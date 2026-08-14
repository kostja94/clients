# Lucius AI — Slug Design Gate B

> 加载时机：Phase 2
> 主文件：SKILL.md §3 Phase 2 指针

---

## 6 问检查

| # | 检查项 | 标准 | Fail 动作 |
|---|--------|------|----------|
| 1 | **含 primary keyword？** | slug 核心词与 target keyword 一致 | 改 slug 让关键词居前 |
| 2 | **通过"大声读"测试？** | 去掉连字符大声读 → 通顺 → Pass | 不通顺或含重复词 → 重选 |
| 3 | **不含禁词？** | framework / strategy / guide / diagnosis / complete / ultimate | 移除禁词 |
| 4 | **≤60 字符？** | 计数不含 `/blog/` | 缩短 |
| 5 | **常青无年份？** | 不含 2026 等年份数字 | 去年份 |
| 6 | **语义余量？** | 30% 内容变化后 slug 仍合适 | 改得更通用 |

---

## 12 反模式（创作阶段必检）

| # | 反模式 | 错误示例 | 正确示例 |
|---|--------|---------|---------|
| 1 | 含年份 | `call-deflection-2026` | `what-is-call-deflection` |
| 2 | 含数量 | `top-5-community-bots` | `best-ai-community-bots` |
| 3 | 连续重复词 | `community-community-bot` | `community-ai-bot` |
| 4 | 内部架构词泄漏 | `community-bot-framework` | `how-to-choose-community-bot` |
| 5 | 分类前缀沉积 | `lucius-ai-community-bot` | `community-ai-bot` |
| 6 | 过多词 | `how-to-automate-discord-customer-support` | `automate-discord-support` |
| 7 | 空洞词 | `complete-guide` / `ultimate` | 用描述性词替代 |
| 8 | 品牌名前置 | `lucius-ai-call-deflection` | `what-is-call-deflection` |
| 9 | 含特殊字符 | `call_deflection` / `CallDeflection` | `call-deflection` |
| 10 | 过于具体 | `discord-server-setup-2026` | `discord-community-setup` |
| 11 | misleading | `free-ai-community-bot` | `ai-community-bot`（若非所有计划免费） |
| 12 | 与已有 slug 混淆 | 太接近已有 slug | 用更区分的关键词 |

---

## Slug 命名规范

| 规则 | 说明 |
|------|------|
| 格式 | kebab-case；全小写 + 连字符 |
| 长度 | 5–8 词；≤60 字符 |
| 关键词 | 含 primary keyword 核心词 |
| 常青 | 不含年份、版本号 |
| 品牌名 | 不前置（除非 Alternative 类 vs-X 格式） |

---

## Title 公式

- Research：`What Is {Term}? — {Why It Matters for X}`
- Product：`How to {Action} — {Benefit / Workflow}`
- Comparison：`Best {Category} — {Differentiator Frame}`
- Alternative：`{Competitor} Alternative — {Why Teams Switch}`
- Announcement：`Introducing {Feature} — {Value Proposition}`

Meta description：120–160 chars · benefit + main intent keyword + 差异化一句。

---

*slug-gate · v2.0.0 · 2026-07-06*
