# 已归档的常见错误与修复方案

> **来源**：`content/templates/template-tools.md` §十三、Alignify 历次 QA 经验
> **版本**：v2.0 · 2026-06-23

---

## 一、Meta 类

| # | 错误 | 正确做法 |
|---|------|---------|
| E1 | Meta title 缺「最佳」/ `Best` | 中文: `最佳XXX（2026）：... \| Alignify`；英文: `Best XXX (2026): ... \| Alignify` |
| E2 | Meta title 无冒号副线（`（2026）\| Alignify` 直连） | 必须加 `：` + 副线：`最佳XXX（2026）：标签1、标签2 \| Alignify` |
| E3 | Meta title 年份格式错误 | 中文用全角括号 `（2026）`；英文用半角 `(2026)` |
| E4 | Meta description 未列举产品名 | 必须含 2–3 个代表产品：`产品A、产品B等` 或 `Product A, Product B, and more` |
| E5 | H1 写了年份 | H1 不写年份；年份仅在 meta title 中体现 |
| E6 | Meta 两处冲突 | `blog-meta.ts` 的 title/description 与 JSON `blogLayout` 的 H1/excerpt 主题不一致。两者主题须一致但不必同文，OG/Twitter 由 `generateMetadata()` 自动输出 |

---

## 二、结构类

| # | 错误 | 正确做法 |
|---|------|---------|
| E7 | Conclusion 在 FAQ 之后 | Conclusion 必须在 FAQ 之前（页面结构顺序不可变） |
| E8 | FAQ 不足 8 问 | 中英文各 ≥8 问 |
| E9 | FAQ 内链违规 | **Tools/Blog JSON**：允许 FAQ 内放站内 `<a>`，须全文 href 唯一、单条答案 ≤2 个 `<a>`、FAQ 合计 ≤3 个不同 slug（见 [section-faq §3.2](../../content/sections/section-faq.md#32-tools--blog-json-的-faq-块)）。**MDX FAQ** 仍禁止任何链接 |
| E10 | FAQ 前手动写了 H2 | FAQ 组件自带 H2，不在 JSON 中额外添加 |
| E11 | 缺少章节 | 10 节结构（TL;DR→什么是→如何工作→BestTools→对比→场景→如何选择→结论→FAQ→References）不可跳 |

---

## 三、内容类

| # | 错误 | 正确做法 |
|---|------|---------|
| E12 | BestTools description 字数不足 | ZH ≥100 字 / EN ≥280 字符；不达标的需扩充 |
| E13 | BestTools 产品描述空洞 | 每款含：核心定位 + 关键差异 + 最佳适用场景 |
| E14 | Excerpt 通用结尾句 | 禁止「这将帮助你更好地理解和应用这些先进的技术工具，提升工作效率和创造力」 |
| E15 | 如何工作 advantages 不足 3 项 | 至少 3 项，每项 name + description |
| E16 | 产品描述 max/min > 3× | 同页 BestTools 最长和最短描述差距不超过 3 倍 |

---

## 四、技术类

| # | 错误 | 正确做法 |
|---|------|---------|
| E17 | 图片路径不存在 | 所有 imageUrl 必须在 `public/blog/{slug}/` 下有对应文件（新文章 `/blog/` 路由） |
| E18 | Meta 注册位置错误 | Meta 注册到 `blog-meta.ts`（或 `tools-meta.ts`），由 `generateMetadata()` 输出。**无需创建或修改 page.tsx** |
| E19 | publishDate 被修改 | 创建后 publishDate 永不更改；更新时只改 modifiedDate |
| E24 | Tools `modifiedDate` 仅改 meta 未改 JSON | `/tools/` 页 Hero 读 JSON `toolsLayout.modifiedDate`；须 **meta + en/zh JSON 三处同步** |
| E25 | Tools 日期全站拉到跨数月 | 用 `rebalance-tools-dates-conservative.py`；以 `origin/main` 为基准，仅错开大簇，每天 ≤2 篇，禁止 108 天一天一篇 |
| E20 | FAQ 答案从正文复制粘贴 | FAQ 答案为独立撰写，不直接复制正文段落 |
| E21 | howToChoose 用 `steps[].name` 而非 `title` | 组件只渲染 `title`——页面上会出现「1. 」空标题。必用 `title`，并补 block `id`、`introduction`、每步 `id`。完整规范见 [section-how-to](../../content/sections/section-how-to.md)（唯一真相源） |
| E22 | howToChoose 步骤过短（stub） | 每步 description 须有实质判断信号，勿写「A→B」一句箭头式；内容优先，字数仅质检参考（见 [section-how-to](../../content/sections/section-how-to.md) Part 3） |
| E23 | howToChoose block id 泛化 | 勿全站用 `"id": "how-to-choose"`；用 `how-to-choose-{slug}` |
| E24 | 锚文本是硬插入的导航句而非自然融入 | 禁止「相邻品类：X。」「若需要X，参见Y。」「详见 Y 专页。」「Related to X. / See also X.」「与 X 一并评估。」等句式。链接必须出现在对工作流的解释性内容中——删除测试：去掉带链接的整句后，文章解释链是否被打断？未打断则为硬插入。 |

---

## 五、修复流程

```
1. 运行 audit 脚本定位错误
2. 对照本表找到对应错误编号
3. 按右侧正确做法修复
4. 重跑 audit 脚本确认修复
5. npm run build 验证整体
```

---

*common-errors · v2.1 · 2026-06-25*
