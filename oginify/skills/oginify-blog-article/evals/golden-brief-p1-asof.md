# Golden Brief — P1 定价 as-of 回归（E07）

**关联 Eval**：E07

## 期望输出断言

- [ ] 所有 Oginify 量化 claim 含 `as of {month} {year}`（免费 6 张/天、$0.99、$7.90、$29、30 秒、4 变体、1200×630）
- [ ] 每个 claim 带 `[Source: URL]`（oginify.com / oginify.com/pricing）
- [ ] 竞品定价（Gemini / GPT Image / Midjourney / Placid / Bannerbear / Canva）带官方来源 + as-of
- [ ] Source Map 中 P0 claim 均有对应行

## 反例（FAIL 触发 — P1）

- "Oginify gives you 6 free generations a day"（无 as-of/来源）
- "Midjourney costs $10/month"（无来源）
- 定价用旧数据无更新
