# Step 9 — 英文 Markdown（Native 重写）

> **规范**：[`rules/localization-quality.md`](./rules/localization-quality.md) · [`rules/anatomy.md`](./rules/anatomy.md) · [`rules/word-counts.md`](./rules/word-counts.md) · [`rules/presentation.md`](./rules/presentation.md)

---

## 原则（Flagship）

- **结构 parity**：与 ZH **相同** section 类型、顺序、锚点 id
- **禁止逐句翻译 ZH**：从 Brief **Answer Blocks + Author POV** 用英文 **重写**；信息对等，句序与段落可不同
- **Kostja 第一人称**：*I* / *my read* 与 ZH「我」判断对齐
- **BLUF 三处**：EN 40–60 words intro；FAQ 首句即答
- TL;DR / FAQ / References **inline 在 en md**（`#article-intro` / `#faq` / `#references` section；禁止 JSON 注入）

---

## Step 09b — 英文地道化 Pass

- 读 `localization-quality.md` §四；朗读一遍，改 telegraphic 句与 `→`
- 跑 `audit-locale-voice.py --slug {slug}`

---

## 字数

Marketing 叙事须**饱满**（见 `word-counts.md` 建议区间）；Best 产品段 EN ≥280 字符。

---

## 检查

### A 层

- [ ] ZH/EN section 顺序与锚点 id 一致
- [ ] 结论在 FAQ 前（若两者皆有）
- [ ] FAQ 7 问，与 ZH 条数一致，无内链
- [ ] Moat + Author POV 在 EN 侧同样兑现
- [ ] EN 非翻译腔（09b Pass）

### B 层

- [ ] Meta 已在 `*-meta.ts` 注册 en 键

下一步：[10-quality-gates.md](./10-quality-gates.md)
