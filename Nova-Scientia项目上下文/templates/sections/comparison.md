# 对比表 — 写作规则

ProductAlternativesSection 与 TopicComparisonTable 内容规范。

**字段定义**：[content-model.md](../../specs/content-model.md) · **版本数据**：[knowledge/topics/](../../knowledge/topics/)

---

## ProductAlternativesSection

- **数量**：4–8（推荐 5–6），均为直接竞品
- **desc**：80–150 字符，突出 vs 本页产品的差异
- **slug**：竞品有站内页时必须填，生成内链
- **顺序**：最直接竞品优先

---

## TopicComparisonTable

- **列**：4–6 列（名称、价格 + 2–4 属性）
- **行**：4–8 产品，同品类
- **单元格**：10–40 字符，简洁
- **价格**：US$ 入门价，注明是否有免费层

### 按品类推荐列

| 品类 | 建议列 |
|------|--------|
| 生图 | 工具、价格、分辨率、API、风格 |
| 视频 | 工具、价格、最长时长、分辨率、API |
| 语音 | 工具、价格、语言数、克隆、API |
| LLM | 工具、价格、上下文、联网、API |
| CLI | 工具、价格、模型、IDE、开源 |

---

## 禁止

- 已关停产品（如 Sora）
- 跨品类凑数
- 未验证的价格/版本
- 把需信用卡的套餐标为「Gratuito」

---

## Checklist

- [ ] 4–8 项，同品类
- [ ] 无关停产品
- [ ] 价格/版本已查 knowledge/topics/
- [ ] 单元格简洁
- [ ] 最佳选项排前
