# Agent Skills 页面模板

本文档定义 Alignify Agent Skills 落地页的标准模板，供 AI / Coding Agent 安装 marketing-skills 使用。

**参考**：[content-rules](../../.cursor/rules/content-rules.mdc)

---

## 一、适用范围

| 路径 | 文件位置 | 说明 |
|------|----------|------|
| `/skills` | `app/skills/(landing)/page.tsx` | Agent Skills 主页面（Terminal 风格落地页） |
| `/zh/skills` | `app/zh/skills/(landing)/page.tsx` | 中文主页面 |

**特点**：中英文双版本、Terminal/CLI 风格落地页、无 Navbar/Footer、红色强调色

---

## 二、主页面结构

- **布局**：`app/skills/(landing)/layout.tsx` 与 `app/zh/skills/(landing)/layout.tsx` 提供黑底 Terminal 风格
- **技能**：160+ skills，9 类 — SEO、Content、Paid Ads、Pages (40+)、Components、Channels、Platforms、Strategies、Analytics（嵌套结构，与 marketing-skills 同步）
- **组件**：`SkillsTerminal` 终端命令块、`CopyCommand` 风格复制
- **内容**：安装命令（命令块优先）、9 大技能分类（终端风格）、Built by、CTA 按钮

---

## 三、Metadata 规范

### 3.1 标题

- **格式**：`Marketing Skills for AI Agents | Alignify`

### 3.2 描述

- **英文**：Marketing Skills for Cursor, Claude Code, OpenClaw. SEO, content, 40+ pages, paid ads, channels, strategies — 160+ skills.
- **中文**：Marketing Skills for Cursor、Claude Code、OpenClaw。SEO、内容、40+ 种页面、付费广告、渠道、策略 — 160+ 项技能。

### 3.3 其他

- **authors**：`[{ name: "Kostja" }]`
- **alternates**：`canonical` + `languages`（zh、en、x-default）
- **openGraph / twitter**：与 title、description 一致
