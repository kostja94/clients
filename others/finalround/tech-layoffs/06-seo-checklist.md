# 06 — SEO 发布检查清单

> **每次部署上线前，花 5 分钟逐项过一遍。养成习惯，不要跳过。**  
> 搞完回到 [05-deploy-guide.md](./05-deploy-guide.md) §验证步骤

---

## 基础 SEO（每页必查）

### □ 1. Title 标签

- [ ] 长度在 50–60 个字符之间（含空格）
- [ ] 包含目标关键词（如 "Amazon Layoffs 2026"）
- [ ] 格式统一：`{Company} Layoffs {Year}: {副标题}`

### □ 2. Meta Description

- [ ] 长度在 150–160 个字符之间
- [ ] 包含目标关键词
- [ ] 有行动号召感（"Here's what happened and what it means for job seekers."）

### □ 3. H1 标题

- [ ] 每页只有一个 H1
- [ ] H1 与 Title 一致或高度接近
- [ ] 包含目标关键词

### □ 4. Canonical URL

- [ ] 指向 `https://www.finalroundai.com/tech-layoffs/{slug}`（**不是** vercel.app 域名）
- [ ] 路径全部小写、无尾部斜杠

### □ 5. 结构化数据（JSON-LD）— 自动生成，只需检查

JSON-LD 由 `[slug]/page.tsx` 自动生成以下三种类型，**你不需要手动添加**，只需要验证：

- [ ] **BreadcrumbList**：路径为 Home → Tech Layoffs → {Company Name}，URL 用主域（`www.finalroundai.com`）
- [ ] **FAQPage**：JSON-LD 中的 Q&A 必须与 JSON 文件 `content.faq.items` 中的 Q&A **完全一致**（如果改了 JSON 的 FAQ，JSON-LD 自动跟改）
- [ ] **NewsArticle**：`headline` 与 `content.seo.title` 一致，`datePublished` 与 `updated_at` 一致
- [ ] 所有 schema URL 使用 `https://www.finalroundai.com`（非 vercel.app）

> **验证方法**：在 [Rich Results Test](https://search.google.com/test/rich-results) 输入主域 URL 检查。

### □ 6. 图片

- [ ] OG 图片（`og:image`）URL 是绝对路径（`https://...`），尺寸 ≥ 1200×630px
- [ ] 页面内图片有 `alt` 属性，且描述了图片内容
- [ ] 图片文件名有意义（如 `amazon-layoffs-2026.jpg`，而非 `img001.jpg`）

---

## 内容 SEO（逐页检查）

### □ 7. 关键词自然分布

- [ ] 目标关键词出现在：H1、第一段正文、至少一个 H2 中
- [ ] **不要堆砌关键词**——读起来要自然，关键词出现 2–4 次即可
- [ ] 相关关键词自然出现（如 "laid off"、"job cuts"、"workforce reduction"）

### □ 8. 内链

- [ ] 至少 1 条链接指向产品页（`/ai-mock-interview`、`/interview-copilot`、`/ai-resume-builder`）
- [ ] 至少 1 条链接指向聚合页（`/tech-layoffs`）
- [ ] 至少 1 条链接指向相关内容（其他公司页、Blog 文章）
- [ ] 所有链接的锚文本描述性强（不是 "click here"，而是 "see Amazon layoffs details"）

### □ 9. FAQ 模块

- [ ] 至少 3 条 FAQ
- [ ] 每条 FAQ 的问题与该公司裁员**直接相关**
- [ ] 答案具体、有用、不少于 30 字
- [ ] FAQPage JSON-LD 中的 Q&A 与页面可见 Q&A **完全一致**

---

## 技术 SEO（全站层面）

### □ 10. Sitemap

**新增公司页时**：
- [ ] 新页面已添加到 sitemap（或自动生成）

**聚合页大幅更新时**：
- [ ] sitemap 的 `lastmod` 日期已更新
- [ ] 没有将未上线的「即将推出」页面加入 sitemap

---

## SEO 红线（绝对不能犯）

| 错误 | 后果 | 如何避免 |
|------|------|----------|
| canonical 指向 vercel.app | 搜索引擎可能把 Vercel 域名当作正式页面，主域权重丢失 | 每次发布前检查 JSON 中 `content.seo.canonical` |
| JSON 中的 FAQ 与页面渲染不一致 | Google 可能判定为 spam，富结果被移除 | FAQ 在 JSON 的 `content.faq.items` 中定义，页面直接渲染——改 JSON 就同时改了页面和 JSON-LD |
| Title 过长（> 60 字符） | 搜索结果中截断显示，点击率下降 | 检查 `content.seo.title` 长度 |
| 新增公司后没 run `npm run build` | barrel index 未更新，页面不会生成 | 新增公司后必须 `npm run build` |
| slug 与文件名不一致 | 导致数据查询失败或 canonical 错误 | 用 Python 验证脚本检查 |

---

## 快速检查工具

- **Title/Description 长度**：检查 JSON 文件 `content.seo.title` 和 `content.seo.description`
- **结构化数据验证**：https://search.google.com/test/rich-results → 输入主域 URL（JSON-LD 自动生成，验证是否正确渲染）
- **Canonical 检查**：检查 JSON 中 `content.seo.canonical` 或部署后查看页面源代码搜索 `canonical`
- **Sitemap 检查**：https://www.finalroundai.com/sitemap.xml → 搜索 `tech-layoffs`
- **数据验证**：运行 Python 验证脚本确认 JSON 字段完整 + slug 匹配

---

*回到 [05-deploy-guide.md](./05-deploy-guide.md) 继续验证步骤*
