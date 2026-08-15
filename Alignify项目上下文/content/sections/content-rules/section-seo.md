# SEO 规范（速查入口）

本文档为 **速查入口**，详细规范见 [technical](../technical/)。

> **Meta 文案规则已迁移**：Meta title、meta description、H1、excerpt 的字数、模板、按页面类型差异，统一由 [section-meta-copy](./section-meta-copy.md) 维护。本文档保留像素值参考与截断机制说明，**不再独立维护字数规则**。

**参考**：content-rules、Google 显示限制、[section-heading-best-practices](./section-heading-best-practices.md)（H1-H6 层级与可访问性）、[section-meta-copy](./section-meta-copy.md)（Meta 文案统一规范）

---

## 一、快速导航

| 规范 | 详细文档 |
|------|----------|
| **Sitemap、robots、canonical、IndexNow** | [technical](../technical/README.md) |
| **Meta Title / Description 文案** | [section-meta-copy](./section-meta-copy.md) |
| **H1 / Excerpt 文案** | [section-meta-copy](./section-meta-copy.md) §三–四 |

---

## 二、两类配置的区分

| 类型 | 用途 | 配置项 | 依据 |
|------|------|--------|------|
| **SEO 导向** | 搜索结果展示、爬虫、点击率 | meta title、meta description | Google 显示限制、SERP 截断 |
| **用户可读性导向** | 页面可见、用户阅读体验 | H1 (title)、excerpt | 可读性最佳实践、首屏信息架构 |

**区分原则**：meta title/description 面向搜索引擎与 SERP；H1/excerpt 面向进入页面的用户，需兼顾可读性与信息密度。**完整文案规则见 [section-meta-copy](./section-meta-copy.md)**。

---

## 三、像素值与截断机制（参考）

### 3.1 像素宽度速查

| 项目 | 桌面端 | 移动端 | 字体 |
|------|--------|--------|------|
| **Title** | ~600px（约 60 英文 / 35 中文） | ~550px | 18px Arial |
| **Description** | ~920px（约 158 英文 / 78 中文） | ~680px（约 120 英文 / 60 中文） | 13px Arial |

**中文注意**：全形字宽约等于两个英文字符，600px 约容纳 25-35 个中文字；移动端更窄，建议核心信息前置。

### 3.2 通用原则

- **关键信息前置**：移动端截断更早，核心内容须在前 50 字 / 120 字符内传达
- **Google 可能重写**：title 重写率 61–76%，description 重写率 ~63%
- **年份使用**：常青内容（Marketing 策略、SEO 指南）可不含年份；时效性内容可含年份体现 freshness

### 3.3 Tools 页面

Tools **单篇长文**的 SEO 与首屏，由 **两个位置** 共同承担：`blog-meta.ts`（或 `tools-meta.ts`）的 **meta** 与 JSON 的 **`blogLayout.title`（H1）、`blogLayout.excerpt`（摘要）**。Meta 由 `generateMetadata()` 自动输出。完整规范见 [section-meta-copy](./section-meta-copy.md) 和 [template-tools](../templates/template-tools.md) §二。

- 校验 meta title 硬规则：上下文仓 `scripts/ops/audit-tools-meta-titles.mjs`
- meta + H1 + excerpt 长度等全量：上下文仓 `scripts/ops/audit-tools-page-fields.mjs`

### 3.4 Marketing/SEO 页面

完整规范见 [section-meta-copy](./section-meta-copy.md) §一–二。特有约束：
- 中文不含「指南」，英文不含 "Guide"
- 常青内容不含年份
- 主动语态：探索/掌握…比较…立即学习/开始实践

---

## 四、用户可读性导向（H1、excerpt）

**完整规范**：见 [section-meta-copy](./section-meta-copy.md) §三–四（字数、模板、三段式结构）和 [section-heading-best-practices](./section-heading-best-practices.md)（H1-H6 层级与可访问性）。

---

## 五、关键规则

- **H1**：每页仅一个；heroContent 禁止 H1；H1 与 meta title 可不同（H1 侧重可读性，meta title 侧重 SEO）
- **Conclusion**：必须在 FAQ 之前（位置/篇幅等完整规则见 [alignify-conclusion.md](../alignify-conclusion.md)）
- **FAQ**：禁止内链、禁止手动 H2
- **Schema**：内容必须与页面可见内容一致
- **Article Schema**：详见 [section-article](./section-article.md)（富结果、AI Overview 可见性）
