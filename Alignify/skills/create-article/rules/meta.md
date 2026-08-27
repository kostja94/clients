# Meta 文案统一规范：Title、Description、H1、Excerpt

> **定位**：本文档是 Alignify 全站 meta title、meta description、H1、excerpt 的**唯一文案规范来源**。H1–H6 层级与可访问性见 [`sections.md`](./sections.md) Part 1 / Part 3.2，不得独立维护副本。
>
> **规则来源**：Google 官方文档、Moz/SEMrush/Ahrefs 2025–2026 最佳实践、Alignify 项目内部分析。
> **最后验证**：2026-05-08（Web 搜索验证通过）。

---

## 〇、四要素总览

Alignify 每个内容页有四个关键文案要素，分属两个导向：

| 要素 | 配置位置 | 导向 | 面向 |
|------|----------|------|------|
| **Meta title** | `src/data/blog-meta.ts`（或 `tools-meta.ts`）→ 由 `generateMetadata()` 输出 | SEO | 搜索引擎、SERP |
| **Meta description** | `src/data/blog-meta.ts`（或 `tools-meta.ts`）→ 由 `generateMetadata()` 输出 | SEO | 搜索引擎、SERP |
| **H1** | md frontmatter `title` | 用户可读性 | 进站用户 |
| **Excerpt** | md frontmatter `description` | 用户可读性 | 进站用户 |

**核心区分**：meta title/description 面向搜索结果页，追求点击率（CTR）；H1/excerpt 面向已进站用户，追求可读性与信息密度。

---

## 一、Meta Title

### 1.1 字数 / 字符数

| 语言 | 建议 | 硬上限（像素） | 说明 |
|------|------|---------------|------|
| **中文** | 25–32 字 | ~35 字（桌面 600px 截断） | 小屏手机 ~25 字即截断 |
| **英文** | 50–60 字符 | ~65 字符（桌面 600px 截断） | 宽字符（W/M）占更多像素 |

**计算方式**：中文按「字」（汉字、英文、数字、标点均计 1）；英文按「字符」（含空格）。Google 按像素宽度截断，非固定字符数。

**字数超限处理**：若无法压缩，优先删除品牌词「| Alignify」；或略微超过（如 33–35 字 / 61–65 字符）亦可接受，核心信息优先。

### 1.2 文案规则（跨类型通用）

**必须**：
- 核心关键词前置（前 30 字符 / 前 15 字内）
- 与页面 H1 主题一致但**不必同文**（meta 偏 SEO/时效，H1 偏可读）
- 每页唯一，不得复用同一句仅改一词

**禁止**：
- 关键词堆砌（Google 重写率 61–76%，堆砌是头号触发因素）
- 空 title 或「Untitled」
- 品牌词强行前置（品牌放末尾 `| Alignify`；中文 Tools 页面不强制品牌后缀，优先保证副线完整性）

### 1.3 按页面类型

#### Tools 页面

| 语言 | 格式 | 示例 |
|------|------|------|
| **中文** | `最佳[工具类型]（2026）：[2-4个短标签]`（无需 `\| Alignify`，中文标题偏长，品牌后缀优先省略） | 最佳AI图片生成工具（2026）：Midjourney、Flux、Stable Diffusion对比 |
| **英文** | `Best [Tool Type] (2026): [2-4 tags] \| Alignify` | Best AI Image Generators (2026): Midjourney, Flux, Stable Diffusion | Alignify |

**硬约束**（Tools 专用）：
- 中文**必须**含「最佳」，英文**必须**含 `Best`
- 中文年份用全角 `（2026）` + 全角冒号 `：`；英文用半角 `(2026)` + 半角 `:`
- 年份后**必须有副线**（2–4 个短标签），**禁止** `（2026）| Alignify` 无副线直连
- 索引页（`/zh/tools`、`/tools`）同样适用上述格式

#### Marketing / SEO 页面

| 语言 | 格式 | 示例 |
|------|------|------|
| **中文** | `[策略/主题]：[核心价值] \| Alignify` | 关键词调研：找到好话题与长尾词 | Alignify |
| **英文** | `[Topic]: [Value Proposition] \| Alignify` | Keyword Research: Find Topics & Long-Tail Keywords | Alignify |

**注意**：
- 常青内容（Marketing 策略、SEO 指南）**可不含年份**
- 英文**不含 "Guide"**
- 中文**不含「指南」**

#### 其他页面（Insights、Glossary、Landing）

| 语言 | 格式 | 说明 |
|------|------|------|
| **中文** | `[主题]：[价值] \| Alignify` | 与 Marketing/SEO 一致 |
| **英文** | `[Topic]: [Value] \| Alignify` | 不含 "Guide" |

---

## 二、Meta Description

### 2.1 字数 / 字符数

| 语言 | 建议 | 移动端安全区 | 桌面最大 |
|------|------|-------------|----------|
| **中文** | 60–80 字 | ≤60 字（移动 680px） | ~78 字（桌面 920px） |
| **英文** | 120–158 字符 | ≤120 字符（移动 680px） | ~158 字符（桌面 920px） |

**关键原则**：核心信息放**前 50 字 / 120 字符**内，确保移动端截断时仍传达要点。

**依据**：Google 桌面 description 区约 920px（≈158 英文 / 78 中文），移动端约 680px（≈120 英文 / 60 中文）。中文全形字宽约为英文半形 2 倍。Google 按像素截断，非固定字符数。中文 <60 字过短会影响点击率（用户跳过概率增加 41%）。

### 2.2 文案规则（跨类型通用）

**必须**：
- 自然融入目标关键词（SERP 中匹配部分会加粗）
- 差异化卖点（数字、免费、精选、案例等）
- 末尾含行动号召（CTA），如「立即探索」「免费指南」「Learn more」
- 每页唯一，不得全站复用
- 与页面正文可支撑（TL;DR 和 bestTools 列表覆盖 description 中提到的产品/场景）

**禁止**：
- 关键词堆砌（Google 重写率 ~63%，堆砌是头号触发因素）
- 罗列超过 3 个产品名（易被视为 keyword stuffing）
- 描述与页面内容不匹配（导致高跳出率）
- 全站使用相同或高度相似的描述
- 因字数限制截断单词（英文）

### 2.3 按页面类型

#### Tools 页面

| 语言 | 模板 | 示例 |
|------|------|------|
| **中文** | `探索[年份]年最佳[工具类型]：[2-3个代表产品]等。比较[核心功能]，[用户收益]。立即探索站内完整指南，免费阅读。` | 探索2026年最佳AI图片生成工具：Midjourney、Flux、Stable Diffusion等。比较文生图与定价，选型参考。立即探索站内完整指南，免费阅读。 |
| **英文** | `Best [tool type] 2026: [2-3 tools]. Compare [key features]. Free guide.` | Best AI image generators 2026: Midjourney, Flux, Stable Diffusion. Compare pricing & features. Free guide. |

**产品名列举**：2–3 个代表产品即可，搭配「等」/ 省略，勿全部罗列。

#### Marketing / SEO 页面

| 语言 | 模板 |
|------|------|
| **中文** | `探索[策略/主题]：[核心方法/价值]。学习[具体动作]，[用户收益]。立即学习。` |
| **英文** | `Learn [topic]: [core value]. [Key methods]. Free guide.` |

#### Insights 页面

| 语言 | 模板 |
|------|------|
| **中文** | `[主题]完整指南：[核心案例/人物]。学习[方法/路径]，[用户收益]。免费阅读。` |
| **英文** | `[Topic] guide: [key figures/cases]. Learn [methods]. Free.` |

#### Glossary 页面

| 语言 | 模板 |
|------|------|
| **中文** | `[类别]词汇表：[数量]+术语。[核心领域]。免费查阅。` |
| **英文** | `[Category] glossary: [N]+ terms. [Key domains]. Free.` |

---

## 三、H1（页面主标题）

### 3.1 字数 / 字符数

| 语言 | 建议 | 允许范围 | 说明 |
|------|------|----------|------|
| **中文** | 14–22 字 | 最长 ~36 字（含双段副标、盘点体） | 过短描述性不足，过长稀释焦点 |
| **英文** | 40–60 字符 | 最长 ~70 字符 | 行业共识：40–70 字符为甜区 |

**依据**：Shopify 2026 建议 <70 字符；Ighenatt 建议 40–70 字符；Loud Interactive 建议 20–60 字符。H1 是进站用户的第一锚点，需兼顾可读性与信息聚焦。

### 3.2 文案规则（跨类型通用）

**格式**：`[类型/策略/主题]：[核心价值/卖点]`

**必须**：
- 每页唯一一个 H1
- 含目标关键词，自然融入
- 以价值开头（避免「欢迎来到我们的网站」）
- 与 meta title 主题一致但**不必同文**（H1 侧重可读性）

**禁止**：
- 含「Guide」「指南」
- 含年份（如 2026）——新鲜度由 meta title 和 publishDate/modifiedDate 表达（细则 [`08-meta-config.md`](../08-meta-config.md) §发布日期）
- 疑问句开头（如「如何选择 X」），须转换为陈述式 `[主题]：[价值]`
- 多个 H1（会混淆搜索引擎对页面焦点的判断）

**与 meta title 的关系**：H1 可更长、更叙事；meta title 更紧凑、偏 SEO。例如 meta title 为「最佳AI图片工具（2026）：文生图对比 | Alignify」，H1 可为「AI图片生成工具：从文字到图像的创作革命」。

### 3.3 按页面类型

| 页面类型 | 中文示例 | 英文示例 |
|----------|----------|----------|
| **Tools** | AI变声器：改变声音，创造无限可能 | AI Voice Changers: Transform Your Voice Experience |
| **Marketing** | 关键词调研：找到好话题与长尾词 | Keyword Research: Find Topics & Long-Tail Keywords |
| **SEO** | 网站结构：层级清晰利于抓取 | Site Structure: Clear Hierarchy for Better Crawling |
| **Insights** | 独立开发者指南：从副业到全职 | Indie Hackers: From Side Project to Full-Time |

### 3.4 技术实现

- H1 来自 md frontmatter `title`（动态路由渲染）
- **禁止** frontmatter `heroHtml` / `heroContent`（E44）
- 详见 [`sections.md`](./sections.md) Part 3.2

---

## 四、Excerpt（Hero 摘要）

### 4.1 字数 / 字符数

| 语言 | 建议 | 说明 |
|------|------|------|
| **中文** | 100–150 字 | 过短（<60 字）影响首屏信息密度 |
| **英文** | 200–250 字符 | 约 400–600 字符展示宽度 |

### 4.2 文案规则（跨类型通用）

**三段式结构**：

| 段落 | 中文 | 英文 |
|------|------|------|
| **首句** | 价值主张 / 行动号召（如「让…」「释放…」「通过…」） | Transform/Discover/Unlock/Make/Explore… |
| **中段** | 工具能力 / 方法论 / 适用场景 | Capabilities / use cases |
| **收尾** | 具体场景或目标用户 | Ideal for [target users] |

**禁止**：
- 通用结尾（如「这将显著提升你的创作效率和专业表现」「这将帮助你更好地理解…」）
- 使用 `metadata.description` 作为 excerpt（必须使用独立的 md frontmatter `description`）

### 4.3 各类型示例

#### Tools 中文
```
让音乐创作变得人人可及。AI音乐生成工具能根据文字描述或风格偏好自动创作旋律，从背景音乐到主题曲，让每个人都能成为音乐创作者。无论是音乐爱好者、视频创作者还是播客制作人，都能快速生成高质量背景音乐，大幅提升创作效率。
```

#### Tools 英文
```
Unlock infinite potential in voices and create unique audio experiences. AI voice changer tools provide real-time voice transformation, effect layering, and personalization, suitable for entertainment, education, and professional recording.
```

#### Marketing / SEO
```
[首句：核心价值/行动号召]。[中段：方法论/框架/适用场景]。[收尾：目标用户或具体收益，禁止通用句]。
```

### 4.4 技术实现

- 通过 `BlogLayout` 的 `excerpt` prop 生成（md frontmatter `description`）
- 使用硬编码字面量
- 详见 [`sections.md`](./sections.md) Part 3.2 § 三

---

## 五、四要素一致性原则

同一页面的四个要素虽分属不同文件（`page.tsx` + `content/.../json`），但须保持**主题一致性**：

| 检查项 | 说明 |
|--------|------|
| **主题一致** | 四要素围绕同一核心主题，不出现 meta 写 A 类产品而 H1/excerpt 只谈 B 类 |
| **产品一致** | meta description 中列举的 2–3 个代表产品必须出现在正文 bestTools 中 |
| **语气一致** | CTA 语气（「立即探索」vs「Explore」）与页面语言一致 |
| **互补不重复** | meta title 与 H1 不应完全相同（meta 偏 SEO，H1 偏可读） |

---

## 六、Meta 注册方式（2026-05-20 迁移后）

Meta 不再写在独立 `page.tsx` 中。当前架构：

1. **Meta 唯一维护位置**：`src/data/blog-meta.ts`（新文章）或 `src/data/tools-meta.ts`（旧文章）。由动态路由的 `generateMetadata()` 自动输出到 `<meta>`、OG、Twitter 标签。
2. **无需手动维护六处一致性**：OG/Twitter 标签由框架自动同步。
3. OG 图片：Tools 页面使用 `toolsOpenGraphImages("slug")` / `toolsTwitterImages("slug")`；Blog 页面使用对应图片函数。
4. Canonical 和 hreflang：由动态路由统一处理。

---

## 七、质检命令

| 命令 | 校验内容 |
|------|----------|
| `npm run audit:tools-meta` | Tools 页面 meta title 硬规则（「最佳」/ `Best`、年份后冒号、禁止无副线直连） |
| `npm run audit:tools-page-fields` | Tools 页面全量（meta title + description + H1 + excerpt 长度与可解析性） |
| `--strict` | 将 warning 也视为未通过（适合 CI） |
| `--json` | 输出全量 JSON 报表 |

---

## 八、快速检查清单

创建或优化页面时逐项核对：

### Meta Title
- [ ] 中文 25–32 字 / 英文 50–60 字符
- [ ] 核心关键词前置
- [ ] Tools：含「最佳」/ `Best` + `（2026）`/ `(2026)` + 冒号 + 副线
- [ ] Marketing/SEO：常青内容不含年份；英文不含 "Guide"
- [ ] 每页唯一

### Meta Description
- [ ] 中文 60–80 字 / 英文 120–158 字符
- [ ] 核心信息在前 50 字 / 120 字符
- [ ] 含 2–3 个代表产品/场景（非全量罗列）
- [ ] 含 CTA
- [ ] 每页唯一；与正文可支撑

### H1
- [ ] 中文 14–22 字 / 英文 40–60 字符
- [ ] 格式 `[类型]：[核心价值]`
- [ ] 不含「Guide」「指南」、年份、疑问句开头
- [ ] 每页唯一一个 H1
- [ ] 与 meta title 主题一致但不必同文

### Excerpt
- [ ] 中文 100–150 字 / 英文 200–250 字符
- [ ] 三段式：首句（价值主张）→ 中段（能力/场景）→ 收尾（目标用户）
- [ ] 禁止通用结尾
- [ ] 独立字段，不使用 metadata.description

### 一致性
- [ ] 四要素围绕同一核心主题
- [ ] hreflang + canonical 由动态路由统一处理

---

## 九、相关文档

- [`sections.md`](./sections.md) Part 3.2 — H1-H6 层级、可访问性、SEO 收益（完整规范）
- [meta.md](./meta.md) — SEO 速查入口（像素值、中英文差异、截断机制）
- [templates.md](./templates.md) — 四类页面参考范式（Part 2–5；引用本文档 § 一–四 的 Meta 差异）
- [meta-description-optimization](./meta.md) — P1 优化方案（历史分析，以本文档字数规则为准）
