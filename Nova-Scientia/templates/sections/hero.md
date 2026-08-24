# Hero — 写作规则

ProductHeroSection（`/products/[slug]`）与 TopicHero（`/[slug]`）的内容写作规范。

**字段定义**：[content-model.md](../../specs/content-model.md) · **结构**：[page-types.md](../../specs/page-types.md)

---

## ProductHeroSection

### 内容规则

- **H1**：含产品名 + 当前年份。格式：`"{Nome}: Review Completo, Preços e Alternativas (2026)"`（50–70 字符）
- **Description**：300–600 字符，定位 + 差异化
- **Tags**：3–6 个，对应 `TAG_ALIAS_ROWS` 分类
- **Stats**：3–4 项（评分、用户量、价格、年份等），数据可核实
- **Screenshot alt**：≤125 字符，`"Interface do [Nome], [categoria], exibindo funcionalidades"`

### SEO

- Meta title：优先 `seo_title`，fallback `"{name}: Análise Completa | Nova Scientia"`
- Meta description：优先 `seo_description`，fallback hero description

---

## TopicHero

### 内容规则

- **H1**：`"Melhores [Categoria] com IA em [ANO]: [Prods] Comparados"`（50–70 字符）
- **Badge**（可选）：≤20 字符，如 `"Guia 2026"`
- **Description**：120–180 字符，含主关键词 + 2–3 代表产品
- **Stats**（可选）：工具数量、阅读时间、更新日期

---

## Checklist

- [ ] H1 含产品/类别名 + 年份
- [ ] Description 在字数范围内
- [ ] Tags/stats 准确可核实
- [ ] Product screenshot 有 alt text
- [ ] seo_title / seo_description 已填或有有效 fallback
