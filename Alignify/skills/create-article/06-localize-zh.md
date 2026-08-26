# Step 6 — 中文地道化 & Extractability

> **规范**：[`rules/localization-quality.md`](./rules/localization-quality.md) · [`rules/marketing-glossary.json`](./rules/marketing-glossary.json) · [`rules/terminology.md`](./rules/terminology.md) · [`rules/presentation.md`](./rules/presentation.md) · [`rules/extractability-checklist.md`](./rules/extractability-checklist.md)

---

## 流程

```
1. 术语统一（marketing-glossary.json + terminology.md）
2. 去英译腔 — 箭头链改 prose；英文术语降频，中文主称
3. BLUF 三处复核（B1 TL;DR · B2 每 major H2 首段 · B3 FAQ 首句）
4. Author POV — 第一人称判断可读、可证伪
5. Extractability — Answer Blocks 可独立成 40–60 字段
6. 段落节奏 — 长段≥3；伪列表清零；**E40–E42**（表前 BLUF、孤立标签、单句段预算）
7. FAQ vs 正文 spot-check（相似度 <30%）
8. audit-locale-voice.py --slug {slug}（Fail 则回改）
9. **audit-marketing-md-render.py**（Marketing/Blog 策略文；E40–E42 Fail 则回改）
```

---

## Flagship 检查

- [ ] 无英译腔（产品名/URL 除外）
- [ ] BLUF 三处 Pass
- [ ] Extractability Pass（`extractability-checklist.md`）
- [ ] Judgment 信号 — 无裸「最佳/唯一」无限定
- [ ] section 锚点与 EN 版将一致
- [ ] E40–E42 Pass（策略/Blog 文跑 `audit-marketing-md-render.py`）

下一步：[07-internal-links.md](./07-internal-links.md)
