# Alignify 12 维 SelfCheck（Step 10 · Gate C）

> **Flagship 固定**：H0–H4 + 12 维 **全 Pass** → **audit-ready**。  
> 细则：[`gates.md`](./gates.md) · 回溯：[`gate-rollback.md`](./gate-rollback.md)

---

## Hard Gates H0–H4（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Gate 0R | Research Log + SERP Fit + Synthesis + IG 三问 |
| **H1** | P0 | G1–G7 + `quality-checklist` P0-1–P0-11 零触发 |
| **H2** | Brief | Moat ≥1；Answer Blocks 3–5；Brief 与大纲一致 |
| **H3** | 双语 parity | ZH/EN section 类型、顺序、锚点 id 一致 |
| **H4** | Flagship 深度 | 叙事字数 ≥ `word-counts.md` 该类型 flagship 下限 |

---

## 12 维 Pass/Fail

| # | 维度 | Pass 标准（摘要） |
|---|------|------------------|
| 1 | **Publishability** | H0–H4 全 Pass |
| 2 | **Fact / E-E-A-T** | Source Map 完整；P0 数字有来源（E1–E6） |
| 3 | **Differentiation** | Moat 在正文兑现；Synthesis 非 paraphrase |
| 4 | **Depth** | 主体节覆盖 Brief；FAQ 7 问独立（非复制） |
| 5 | **Presentation** | BLUF 三处；长段≥3；伪列表 0；见 `presentation.md` |
| 6 | **Writing / Voice** | 术语统一；无 hype 套话 |
| 7 | **Objectivity** | Tools：≥1 竞品优势 + ≥1 非榜首场景 |
| 8 | **Structure / Links** | distinct 内链 ≥5；Hub/Spoke 合规；A 层结构 |
| 9 | **SEO / SERP** | Meta/H1 规则；SERP Fit 复核 Pass |
| 10 | **Bilingual parity** | EN 非机翻腔；信息对等 |
| 11 | **Architecture** | 内容驱动大纲 intentional；主体节完整 |
| 12 | **Flagship extras** | Extractability Pass；Excellence 类型已标注 |

**Gate C**：12 维 + H0–H4 全 Pass → 输出 **audit-ready**，移交 [`audit-article`](../../audit-article/SKILL.md)。

---

## Step 10 自动化预检（部署仓根目录）

```bash
npm run verify:content-json
npm run build
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

---

## Step 10 交付物（audit-ready 包）

1. ZH + EN md 路径  
2. SelfCheck 表（12 维 + H0–H4，全 Pass）  
3. Source Map（`source-map-template.md`）  
4. Internal Link Plan（distinct slug 列表 + 锚文本）  
5. SERP Fit 最终版  
6. **终审指令**（复制给 audit-article）：

```markdown
请按 Alignify audit-article skill 终审：
- ZH：content/{channel}/zh/{slug}.md
- EN：content/{channel}/en/{slug}.md
- articleType：{type}
- Primary keyword：{kw}
- SelfCheck：12/12 + H0–H4 Pass
- Moat：{Brief 中 1 行摘要}
```

---

*selfcheck · v1.0 · 2026-08-26*
