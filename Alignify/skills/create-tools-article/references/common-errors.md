# 已归档的常见错误与修复方案

> **来源**：`content/templates/template-tools.md` §十三、Alignify 历次 QA 经验
> **版本**：v3.0 · 2026-08-23

---

## 一、Meta 类

| # | 错误 | 正确做法 |
|---|------|---------|
| E1 | Meta title 缺「最佳」/ `Best` | 中文: `最佳XXX（2026）：... \| Alignify`；英文: `Best XXX (2026): ... \| Alignify` |
| E2 | Meta title 无冒号副线 | 必须加 `：` + 副线 |
| E3 | Meta title 年份格式错误 | 中文全角 `（2026）`；英文半角 `(2026)` |
| E4 | Meta description 未列举产品名 | 必须含 2–3 代表产品 |
| E5 | H1（frontmatter `title`）写了年份 | H1 不写年份；年份仅在 meta title |
| E6 | Meta 与 frontmatter 主题冲突 | `blog-meta.ts` title/description 与 md `title`/`description` 主题须一致、不必同文 |

---

## 二、结构类

| # | 错误 | 正确做法 |
|---|------|---------|
| E7 | 结论在 FAQ 之后 | 结论 md section 在 FAQ 集中 JSON 注册之前 |
| E8 | FAQ 不是 7 问 | 中英文各 **7 问**（`faq-data.json`，与线上一致） |
| E9 | FAQ 答案含内链 | FAQ 答案 plain text，无 `](` / `<a` |
| E10 | md 中手写 FAQ H2 | FAQ 由全局组件渲染，正文不写 FAQ section |
| E11 | 缺少章节 | 10 节顺序不可跳（见 `tools-article-anatomy.md`） |
| E12 | frontmatter 含 `howTo:` | **禁止**；HowTo 仅正文 `## 如何选择…` section |

---

## 三、内容类

| # | 错误 | 正确做法 |
|---|------|---------|
| E13 | Best 产品段字数不足 | ZH ≥100 字 / EN ≥280 字符 |
| E14 | 产品描述空洞 | 核心定位 + 关键差异 + 最佳适用场景 |
| E15 | Excerpt 通用结尾句 | 禁止模板化结尾 |
| E16 | 同页产品 description max/min > 3× | 扩充最短条目 |
| E17 | HowTo 步骤过短 | 每步 ≥80 字；见 `section-how-to.md` |

---

## 四、技术类

| # | 错误 | 正确做法 |
|---|------|---------|
| E18 | 图片路径不存在 | `public/blog/{slug}/` 与 md 引用一致 |
| E19 | Meta 注册位置错误 | `blog-meta.ts` / `tools-meta.ts`；无需改 page.tsx |
| E20 | publishDate 被修改 | 已上线 slug 的 publishDate 永不改 |
| E21 | Tools 仅改 meta 未改 md | Hero 读 frontmatter `updated`；须 meta + en/zh md 同步 |
| E22 | FAQ 答案从正文复制 | FAQ 独立撰写 |
| E23 | 锚文本硬插入导航句 | 链接须自然融入解释性句子 |
| E24 | 使用 JSON howToChoose block | **已废弃**；改用正文 section |
| E25 | 使用 `npm run audit:howto-choose` | **已废弃**；用 `verify-content-md.py` + `section-how-to.md` |

---

## 五、修复流程

```
1. npm run verify:content-json
2. python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} …
3. 对照本表修复
4. npm run build
```

---

*common-errors · v3.0 · 2026-08-23*
