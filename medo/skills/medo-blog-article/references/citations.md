# 引用分级与 Source Map

> Agent 在 Phase 4（Draft）与 Phase 5（SelfCheck）前加载。无来源数字 = G3 Fail。

---

## 1. 引用分级（P0 / P1 / P2）

| 级别 | 触发条件 | 要求 |
|------|---------|------|
| **P0 — 必须引用** | 竞品定价、政策条款、开发者账户费用、Karpathy 起源、官方 Guideline 编号 | HTML 链到原始来源；跨篇重复数字每篇都要链 |
| **P1 — 应当引用** | 行业趋势、竞品 GA/Beta 状态、builder 功能边界、"typically" 类声明 | 链官方 docs/changelog；无法链则 `as of {date}` + "typically" |
| **P2 — 可不引用** | 原创决策框架、作者测试观察、从已引用数据衍生的分析 | 标注方法论 `based on testing n=X` 或 anecdotal |

---

## 2. P0 固定来源表

| Claim 类型 | 权威来源 |
|------------|----------|
| Vibe coding 起源 | <a href="https://x.com/karpathy/status/1886192187808148483" rel="nofollow noopener">Karpathy Feb 2025 post</a> |
| Collins WOTY 2025 | <a href="https://www.collinsdictionary.com/woty" rel="nofollow noopener">Collins Dictionary WOTY</a> |
| Apple Review Guidelines | <a href="https://developer.apple.com/app-store/review/guidelines/" rel="nofollow noopener">developer.apple.com/app-store/review/guidelines</a> |
| Guideline 4.2 | 同上 Section 4.2 |
| Apple Developer Program $99 | <a href="https://developer.apple.com/programs/" rel="nofollow noopener">developer.apple.com/programs</a> |
| TestFlight | <a href="https://developer.apple.com/testflight/" rel="nofollow noopener">developer.apple.com/testflight</a> |
| Google Play $25 | <a href="https://play.google.com/console" rel="nofollow noopener">play.google.com/console</a> |
| Google account deletion policy | <a href="https://support.google.com/googleplay/android-developer/answer/13327111" rel="nofollow noopener">Google Play User Data policy</a> |
| MeDo 官方文档 | <a href="https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en" rel="nofollow noopener">Baidu AI Cloud MIAODA Overview</a> |

---

## 3. P1 来源类型

| 类型 | 示例 | 标注方式 |
|------|------|----------|
| 竞品官网 | lovable.dev, replit.com, bolt.new | `as of June 2026` + link |
| Product Hunt | MeDo launch narrative | link to PH page |
| 第三方评测 | DEV.to, YouTube tutorials | link + note "third-party" |
| MIT Technology Review | vibe coding explainers | link |
| SEO 搜索量估算 | Ahrefs/Semrush | **避免写入正文具体数字**；或标 "estimated" |

---

## 4. P2 允许格式

**内部测试观察**：
> Based on testing {N} prompt variations across {tools} in {month} {year}, {finding}.

**社区轶事**：
> Some builders report {X} on Reddit — anecdotal, not a guarantee.

禁止：单用户案例 → "users always experience X"

---

## 5. Source Map 模板（Phase 5 附表）

```markdown
## Source Map — {slug}

| # | Claim | Level | Source |
|---|-------|-------|--------|
| 1 | Apple Developer $99/yr | P0 | developer.apple.com/programs |
| 2 | Lovable mobile = Capacitor wrap | P1 | lovable.dev/faq (as of 2026-06) |
| 3 | Three-category framework | P2 | Original analysis |
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
[how to build a mobile app with AI](/blog/how-to-build-mobile-app-with-ai)
```

或正文中自然链：`see [what vibe coding is](/blog/what-is-vibe-coding)`.

---

## 8. G3 常见 Fail 模式

| Fail | 修复 |
|------|------|
| "17k+ apps" 无来源 | 加 "per medo.dev gallery (as of {date})" 或标待验证 |
| 竞品定价无链 | 链 pricing 页 + as-of |
| "vibe coding has 110K searches" | 标 estimated 或删具体数字 |
| 拒审率统计无来源 | 改 qualitative "increasingly common" |

---

## 9. E-E-A-T 增强

| 维度 | MeDo Blog 做法 |
|------|----------------|
| Experience | 真机测试步骤、checklist 来自已发布 publish 文实践 |
| Expertise | 三分类框架、Native vs PWA 技术准确 |
| Authoritativeness | P0 官方政策链 |
| Trustworthiness | 诚实竞品优势、as-of 标注 |
