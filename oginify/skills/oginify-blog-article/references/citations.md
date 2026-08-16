# Oginify Citations — 引用分级与 Source Map

> 加载时机：Phase 4 / Phase 5
> 主文件：SKILL.md §3.4 指针 · 无来源数字 = G3 Fail

---

## 1. 引用分级（P0 / P1 / P2）

| 级别 | 触发条件 | 要求 |
|------|---------|------|
| **P0 — 必须引用** | 竞品定价、免费额度、平台尺寸规格、产品机制数字、CTR/统计数字 | **上下文描述性内链**链到原始来源；跨篇重复数字每篇都要链 |
| **P1 — 应当引用** | 行业趋势、竞品版本/GA 状态、产品能力描述、"typically" 类声明 | 链官方 docs/changelog；无法链则 `as of {date}` + "typically" |
| **P2 — 可不引用** | 原创决策框架、作者测试观察、从已引用数据衍生的分析 | 标注方法论 `based on testing n=X` 或 anecdotal |

### P0 引用格式（硬性）

**禁止 `[Source: URL]` 后缀形式**。P0 来源必须嵌入句子，作为**上下文描述性内链**：

- 站外来源 → `<a href="URL" rel="nofollow noopener">描述性锚文本</a>`
- 站内来源 → `[描述性锚文本](/path)`

```markdown
✅ 正确（站外，描述性锚文本）：
…six generations a day per signed-in account, per the
<a href="https://oginify.com/pricing" rel="nofollow noopener">Oginify pricing page</a>.

✅ 正确（站内）：
…which is the size the [Oginify homepage](/) ships by default.

❌ 禁止：
…six generations a day per signed-in account [Source: https://oginify.com/pricing].
```

**锚文本要求**：
- 必须是描述性的（"the Oginify pricing page"、"the Open Graph protocol"、"Gemini API pricing"）
- 禁 "click here" / "learn more" / "source"
- 同一 URL 在同一篇内避免重复链接（第二处不再链或换锚文本）
- Oginify 自有页（首页/工具页/validator）用站内 markdown 链接；`/pricing` 不作正文链接（G6 forbidden），用站外 `https://oginify.com/pricing` 描述性锚文本

---

## 2. P0 固定来源表

| Claim 类型 | 权威来源 |
|------------|----------|
| Oginify 免费额度 6 张/天 | <a href="https://oginify.com/pricing" rel="nofollow noopener">Oginify pricing</a> |
| Oginify 定价 $0.99 / $7.90 / $29 | <a href="https://oginify.com/pricing" rel="nofollow noopener">Oginify pricing</a> |
| Oginify 机制（4 变体 / 30 秒 / 1200×630） | <a href="https://oginify.com/" rel="nofollow noopener">oginify.com</a> |
| 1200×630 平台规格 | <a href="https://ogp.me/" rel="nofollow noopener">Open Graph protocol</a> 或 oginify.com |
| Gemini 3.1 Flash Image 定价 | <a href="https://ai.google.dev/gemini-api/docs/pricing" rel="nofollow noopener">Gemini API pricing</a> |
| GPT Image 2 定价 | <a href="https://developers.openai.com/api/docs/pricing" rel="nofollow noopener">OpenAI API pricing</a> |
| Midjourney 订阅价 | <a href="https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans" rel="nofollow noopener">Midjourney plans</a> |
| Vercel OG | <a href="https://vercel.com/docs/og-image-generation" rel="nofollow noopener">Vercel OG docs</a> |
| social-cards-skills | <a href="https://github.com/kostja94/social-cards-skills" rel="nofollow noopener">GitHub repo</a> |
| Placid / Bannerbear 定价 | 各官方 pricing 页（as-of） |

---

## 3. P1 来源类型

| 类型 | 示例 | 标注方式 |
|------|------|----------|
| 竞品官网 | gemini.google / openai.com / midjourney.com | `as of {month} {year}` + link |
| 第三方评测 | Product Hunt、Stork.AI、社区 | link + note "third-party" |
| 平台文档 | ogp.me、开发者平台 | link |
| 趋势数字 | CTR 统计 | **避免正文具体数字**；或标 "estimated" + 来源 |

---

## 4. P2 允许格式

**内部测试观察**：
> Based on testing {N} prompt variations across {tools} in {month} {year}, {finding}.

**社区轶事**：
> Some builders report {X} on Reddit — anecdotal, not a guarantee.

禁止：单用户案例 → "users always experience X"

---

## 5. Source Map 模板（Phase 6 附表）

```markdown
## Source Map — {slug}

| # | Claim | Level | Source |
|---|-------|-------|--------|
| 1 | Oginify 免费 6 张/天 | P0 | oginify.com/pricing (as of 2026-08) |
| 2 | Gemini 1K 图 ~$0.067 | P0 | ai.google.dev/gemini-api/docs/pricing |
| 3 | 三分类框架 | P2 | Original analysis |
```

每篇 P0 claim ≥1 条须在 Source Map 有对应行。

---

## 6. 站外链接 HTML 格式

```html
<a href="https://example.com/path" rel="nofollow noopener">descriptive anchor text</a>
```

- 锚文本须描述性（非 "click here"）
- 每篇 2–5 条站外链
- 竞品链优先官方域名

---

## 7. 站内链接格式

```markdown
[what is an open graph image](/blog/what-is-open-graph-image)
```

或正文中自然链：`see [how to create one](/blog/how-to-create-open-graph-image)`.

---

## 8. G3 常见 Fail 模式

| Fail | 修复 |
|------|------|
| "6 张/天" 无来源 | 加描述性内链：per the <a href="https://oginify.com/pricing" rel="nofollow noopener">Oginify pricing page</a> (as of {date}) |
| 竞品定价无链 | 描述性锚文本链 pricing 页 + as-of |
| "CTR 提升 300%" 无来源 | 标 estimated 或删具体数字 |
| "1200×630 是标准" 无来源 | 描述性内链 ogp.me 或 oginify.com |
| `[Source: URL]` 后缀残留 | 改为上下文描述性内链（§1 P0 格式） |
