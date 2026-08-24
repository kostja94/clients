# Step 6 — 质量门控

> **产出**：P0 通过 + `npm run build` 成功
> **引用**：[`references/quality-checklist.md`](./references/quality-checklist.md)

---

## Gate P0（一票否决）

| # | 检查项 | 验证方式 |
|---|--------|---------|
| P0-1 | Meta 四要素合规 | 对照 `references/meta-requirements.md` |
| P0-2 | FAQ **7 问** | `faq-data.json` 计数 |
| P0-3 | **无 frontmatter `howTo:`** | `verify-content-md.py` |
| P0-4 | 结论在 FAQ 之前 | md 区块顺序 |
| P0-5 | heroImage 或 heroHtml | frontmatter 人工确认 |
| P0-6 | 日期双源一致 | meta ISO ↔ md `date`/`updated` 同日历日 |
| P0-7 | `npm run build` 成功 | 部署仓 |

> **已废弃**：`npm run audit:howto-choose`、JSON `howToChoose` block、HowTo JSON-LD

---

## 自动化

```bash
npm run verify:content-json
npm run build
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --locale both --violations-only
```

---

## 叙事字数（H3 参考）

| 类型 | 中文 | 英文 |
|------|------|------|
| Tools | ≥2,000 字 | ≥12,000 字符 |
| Marketing | ≥2,500 字 | ≥14,000 字符 |
| SEO | ≥2,000 字 | ≥12,000 字符 |
| Insights | ≥2,500 字 | ≥14,000 字符 |

---

## 最终清单

- [ ] Gate P0 全部 ✓
- [ ] HowTo 正文 section 符合 `section-how-to.md`（如适用）
- [ ] 内链 audit 零 high
- [ ] 页面源码无 `"@type":"HowTo"`

---

*06-quality-gates · v2.0 · 2026-08-23*
