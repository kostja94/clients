# Step 4 — 产品截图（best-ranking）

> **适用**：`articleType: best-ranking`  
> **规范**：[`rules/product-screenshots.md`](./rules/product-screenshots.md)

---

## 硬规则

- 截图 URL = 该条目介绍的**产品/能力页**（非厂商首页）
- 输出：`public/blog/{slug}/{product}.jpg`（或 legacy `/tools/` 路径）
- `fullPage: false`，首屏 viewport

## 脚本（部署仓）

```bash
python scripts/permanent/capture-blog-screenshots.py --slug {slug}
```

## Markdown 引用

```markdown
![Product homepage screenshot](/blog/{slug}/product.jpg)
```

---

## 检查

- [ ] 每个 Best 产品 H3 有对应 jpg
- [ ] manifest / registry 已登记（如使用 Firecrawl 流水线）

下一步：[05-zh-content.md](./05-zh-content.md)
