# Forbidden Loads — 不得触发 hellyeah-blog-article 的场景

> 这些场景若错误触发 blog-article skill = skill 路由失效，须修复 frontmatter description。

## 1. title/description 专项优化

**输入示例**：
- "优化 /blog/programmatic-geo-vs-seo 的 meta description"
- "给 GEO 文章写一个 SERP title"
- "批量检查博客的 description 字符数"

**应触发**：未来 `hellyeah-meta-title-description` 或手动编辑

**若误触发 blog-article**：会加载完整创作工作流，浪费上下文且产出错误。

---

## 2. 运行时读取 hellyeah-*.md

**输入示例**：
- Agent 打开 `hellyeah-keywords.md` 查 JTBD
- Agent 读取 `hellyeah-competitors.md` 写 battlecard

**应触发**：只读 `hellyeah/skills/hellyeah-blog-article/references/*.md`

**若违反**：self-contained 规则失效；事实可能与非蒸馏源不一致。

---

## 3. Capability / 平台落地页

**输入示例**：
- "重写 /capabilities/seo-geo 页面正文"
- "优化 /aima 落地页 Hero"

**应触发**：站点页面模板体系，非 blog skill

---

## 4. 非 hellyeahai.com 博客

**输入示例**：
- "写一篇 Medium 博客讲 programmatic GEO"
- "给客户写 guest post"

**应触发**：通用 blog skill 或无 skill

---

## 5. 非英文内容

**输入示例**：
- "写一篇中文的 GEO 入门"
- "日本語で GEO の記事を"

**应触发**：另建 ZH skill（当前不存在）

---

## 6. 清单化 / 可复制 hook 请求

**输入示例**：
- "50 GEO prompts to copy"
- "100 AI ads manager tips listicle"

**应触发**：Framework 路由 + 拒绝纯清单；或 STOP 并解释

---

## 7. 创作阶段读取 blog/README.md

**输入示例**：
- Phase 4 加载 `hellyeah/blog/README.md` 查序号

**应触发**：序号从 `references/content-graph.md` 读取；README 仅 Phase 6 提示人类更新
