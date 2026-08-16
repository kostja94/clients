# Oginify Proof Gate — P1–P6

> 加载时机：Phase 0 / Phase 5
> 主文件：SKILL.md §1 指针 · 项目配置 §3

---

## P1 — 产品数字 as-of

**触发**：任何可外部验证的 Oginify 量化 claim。

| Claim | 必须含 | 来源 |
|-------|--------|------|
| 免费额度 6 张/天 | `as of {month} {year}` | oginify.com + pricing 页 |
| 定价 $0.99 / $7.90 / $29 | `as of {month} {year}` | oginify.com/pricing |
| 生成约 30 秒 | `as of {month} {year}` | oginify.com |
| 4 变体（1 on-brand + 3 wildcards） | `as of {month} {year}` | oginify.com |
| 1200×630 输出 | `as of {month} {year}` | oginify.com |

**反例**：`Oginify gives you 6 free generations a day`（无 as-of、无来源）→ **FAIL**。
**正确**：`Oginify gives you up to 6 free generations a day for signed-in accounts, per the <a href="https://oginify.com/pricing" rel="nofollow noopener">Oginify pricing page</a> as of August 2026`。

---

## P2 — URL-first vs prompt 边界

**触发**：Comparison / Ranking / Alternative 中涉及通用生图工具（Gemini / GPT Image / Midjourney）。

| 正确表述 | 反例（FAIL） |
|---------|-------------|
| 「通用生图工具能做 OG 卡片，但需要你手动指定 1200×630、渲染文字、导出并托管 PNG，再写 meta tags」 | 「通用生图工具不适合做 OG 图片」 |
| 「Oginify 以 URL 为唯一输入；通用工具以 prompt 为输入」 | 「只有 Oginify 不用写 prompt」 |
| 「选择取决于你想让工具替你完成多少步骤」 | 「Oginify 是唯一正确选择」 |

**判定**：若正文将通用生图写成「不能做 OG」或「必然更差」，或把 Oginify 写成「唯一」，→ **FAIL**。

---

## P3 — 1200×630 规格声明

**触发**：任何平台尺寸/裁剪行为 claim（X / LinkedIn / Slack / Discord / iMessage / Facebook）。

| 正确 | 反例 |
|------|------|
| 「1200×630 at 1.91:1 is the large-card size X, LinkedIn, Slack, Discord, iMessage and Facebook render, per the <a href="https://ogp.me/" rel="nofollow noopener">Open Graph protocol</a>」 | 「1200×630 是标准」（无来源） |
| 「anything narrower than 600px on the long edge falls back to a small thumbnail」+ 来源 | 无来源的裁剪行为 claim |

---

## P4 — SaaS vs 开源边界

**触发**：正文提及 `social-cards-skills` 或「开源版」。

| 事实 | 表述 |
|------|------|
| social-cards-skills = Oginify 的 MIT 开源发行版 | 「social-cards-skills is the MIT-licensed Agent Skills distribution of the same engine」 |
| 开源版需要自己运行（npx + Satori + fonts + 自带模型/资产） | 「run it yourself on your own infrastructure with no SaaS dependency」 |
| Oginify = 托管 SaaS | 「Oginify is the managed version」 |
| 两者输出一致但交付不同 | 「run it yourself, let us paint the cards for you, or compare against generic generators」 |

**反例**：把 Oginify 说成「完全开源」或把 social-cards-skills 说成「SaaS」→ **FAIL**。

---

## P5 — 竞品公平

**触发**：Comparison / Ranking / Alternative / 竞品提及。

| 要求 | 反例 |
|------|------|
| 每竞品 ≥1 真实优势 | 只写竞品缺点 |
| 每竞品 ≥1 非 Oginify 更合适场景 | 全场景都推 Oginify |
| 禁 just / merely / only does X | 「Gemini is just a chat tool」 |

**判定**：任一竞品被写成「无优点」或全文无「何时不选 Oginify」→ **FAIL**。

---

## P6 — 禁夸大措辞

| 禁词/模式 | 替代 |
|----------|------|
| magic / magical | 具体机制（读取页面品牌 → 生成变体） |
| zero-work / zero-effort | 「removes the design step」「the URL is the entire input」 |
| promptless（作为绝对 claim） | 「no prompt box on the home page」+ as-of |
| 「自动提升 CTR 300%」 | 无来源 CTR 承诺一律禁；如需写须描述性内链 + 限定（见 citations.md §1 P0） |
| revolutionary / game-changing | 具体改进（native reasoning、文本渲染） |

---

## 判定流程

```
Draft 完成后：
1. 对照 P1–P6 逐条检查
2. 任一 FAIL → 标记修复动作 → 按 SKILL.md §3.G 回退 Phase 4
3. 全 Pass → 进入 Phase 5 加权 12 维评分
```
