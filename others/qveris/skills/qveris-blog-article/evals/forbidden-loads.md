# Forbidden Loads — 不得触发完整创作工作流的场景

> 下列场景可加载 skill 主文件做路由，但 **不得** 跑 Phase 0–6 全文创作。title/description 专项只读 `references/meta-title-description.md`。

## 1. title/description 专项优化（轻量路径）

**输入示例**：
- "优化 /blog/stock-api-free-comparison 的 meta description"
- "给免费股票 API 对比文写一个 SERP title"
- "批量检查博客的 description 字符数"

**应触发**：`qveris-blog-article` → **仅** `references/meta-title-description.md`（禁止 Phase 0–6、禁止改正文）

**若误跑完整创作**：浪费上下文且可能覆写已有稿。

---

## 2. 非博客页面（Landing / Docs）

**输入示例**：
- "为 /apps/earnings-copilot 写落地页正文"
- "重写 /pricing 的说明文案"

**应触发**：产品仓 SEO / 页面模板体系（非本 skill 范围）

**若误触发 blog-article**：会按博客类型路由，产出 editorial 风格内容而非 transactional 落地页。

---

## 3. 非 qveris.ai 博客

**输入示例**：
- "帮我写一篇 Medium 博客讲 capability routing"
- "给客户写 guest post 关于金融数据 API"

**应触发**：通用 blog skill 或无 skill（手动创作）

**若误触发 blog-article**：会强制注入 QVeris 产品上下文、品牌后缀和金融合规规则。

---

## 4. 中文博客内容

**输入示例**：
- "写一篇中文的 QVeris CLI 入门教程"
- "给 qveris 写一篇中文博客"

**应触发**：另建 ZH skill（当前不存在；官网有拼音 slug 中文博客但本 skill 仅英文）

**若误触发 blog-article**：所有语言策略、Voice 标准均为英文设计，中文输出质量不可控。

---

## 5. 纯数据/报告类内容

**输入示例**：
- "整理 2026 年金融数据 API 市场报告"
- "做一份 capability providers 对比表格"

**应触发**：通用数据分析 skill 或手动

**若误触发 blog-article**：会套用博客叙事弧和 H2 模板，产出 editorial 格式而非数据报告格式。

---

## 6. 官网 sitemap / 站点结构分析

**输入示例**：
- "分析 qveris.ai 的 sitemap 结构"
- "做站点信息架构研究"

**应触发**：`qveris-site-structure.md`（项目文档），非本 skill

**若误触发 blog-article**：会跑选题门禁与类型路由，产出文章而非 IA 分析。
