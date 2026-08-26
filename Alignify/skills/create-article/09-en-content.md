# Step 9 — 英文 Markdown（Native 重写）

> **规范**：[`rules/localization-quality.md`](./rules/localization-quality.md) · [`rules/anatomy.md`](./rules/anatomy.md) · [`rules/word-counts.md`](./rules/word-counts.md) · [`rules/presentation.md`](./rules/presentation.md)

---

## 原则（Flagship · 双语同等质量）

- **结构 parity**：与 ZH **相同** section 类型、顺序、锚点 id（对齐**实际采用的**架构，非模板全节）
- **禁止逐句翻译 ZH**：从 Brief **Answer Blocks + Author POV** 用英文 **重写**；EN 须与 ZH **同等论证深度与 Moat 兑现**
- **Kostja 第一人称**：*I* / *my read* 与 ZH「我」判断对齐
- **BLUF 三处**：各 major H2 首段 **≥3 句**；若采用 TL;DR 则 EN intro 40–60 words；若采用 FAQ 则首句即答
- **结构 parity 含呈现**：ZH 若有表前短桥接 / 孤立标签，EN **不得**镜像；Step 09 应一并修复为长段
- TL;DR / FAQ / References **若 ZH 有则 EN 须有**，inline 在 en md（禁止 JSON 注入）

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

- [ ] ZH/EN section 顺序与锚点 id 一致（含省略 TL;DR/FAQ 的对称省略）
- [ ] 结论在 FAQ 前（若两者皆有）
- [ ] FAQ：**若采用**则 7 问，与 ZH 条数一致，无内链
- [ ] Moat + Author POV 在 EN 侧**同等深度**兑现（非摘要版）
- [ ] EN 非翻译腔（09b Pass）
- [ ] E40–E42 Pass（与 ZH 对称跑 `audit-marketing-md-render.py`）

### B 层

- [ ] Meta 已在 `*-meta.ts` 注册 en 键
- [ ] **Final CTA**：`cta-config.json` → `slugs.{slug}.en` title/description 已按 EN 结论定稿（见 [`rules/final-cta.md`](./rules/final-cta.md)）

下一步：[10-quality-gates.md](./10-quality-gates.md)
