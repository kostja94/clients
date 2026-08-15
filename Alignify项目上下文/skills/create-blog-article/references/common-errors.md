# Common Errors — 已归档的常见错误与修复方案

> **路径**：`skills/create-blog-article/references/common-errors.md`
> **用途**：汇总本 Skill 使用过程中已发现的常见错误，按 Meta / 结构 / 内容 / 技术分类。
> **版本**：v1.0 · 2026-07-16

---

## Meta 类

### E1 — H1 写了年份
**症状**：H1 如「2026年最佳AI图片生成器」
**修复**：删除年份，H1 应为「AI图片生成器：将文字转为惊艳视觉」

### E2 — Meta title 缺 `| Alignify`
**症状**：title 末尾忘记加 `| Alignify`
**修复**：中文加 `| Alignify`，英文加 `| Alignify`

### E3 — 中文 title 用了半角符号
**症状**：`2026年最佳XXX:副线 | Alignify`（半角冒号）
**修复**：中文用全角 `（2026）` `：`，英文用半角 `(2026)` `:`

### E4 — routeCategory 与知识块目录不匹配
**症状**：`knowledge/marketing/xxx.md` 但 `routeCategory: "tools"`
**修复**：`knowledge/marketing/` → routeCategory 必须是 `"marketing"`；`knowledge/tools/` → 必须是 `"tools"`

### E5 — hubCategory 填了不存在的值
**症状**：`toolsHubCategory: "ai-category"` 但 tools-pages-config.ts 中没有这个分组
**修复**：从部署仓 `tools-pages-config.ts` 或 `marketing-pages-config.ts` 中读取现有的分组名

---

## 结构类

### E6 — bestTools 产品的 `description` 不足字数
**症状**：中文 `description` 只有 40 字
**修复**：中文 ≥100 字，英文 ≥280 字符；每个产品三段式：核心定位 + 关键差异 + 最佳适用场景

### E7 — howToChoose steps 用了 `name` 字段
**症状**：`{"id":"1","name":"确定需求","description":"..."}` → 渲染时 title 为空
**修复**：将 `name` 改为 `title`：`{"id":"1","title":"确定需求","description":"..."}`。完整规范见 [section-how-to](../../content/sections/section-how-to.md)（唯一真相源）

### E8 — Conclusion 位置错误
**症状**：Conclusion 出现在 FAQ 之前第 3+ 个 section
**修复**：Conclusion 必须是 blocks 数组中**倒数第 2 个** section（仅 FAQ 之后、References 之前）

### E9 — 缺少必要 block
**症状**：Tools 型文章没有 `howToChoose` 或 `comparisonSection`
**修复**：对照 `references/article-types.md` 中各类型的「必有 block」清单补全

### E10 — SEO 型 `tldr.items` 用了纯字符串
**症状**：`"items": ["要点1", "要点2"]` — SEO 型标准格式是对象
**修复**：改为对象格式：`"items": [{"title": "...", "content": "..."}]`

---

## 内容类

### E11 — FAQ 答案复制了正文内容
**症状**：FAQ 的第 3 题答案与 section 2 的第 3 段完全相同
**修复**：FAQ 答案必须用自己的话重新表达，首句即给直接答案

### E12 — 文案出现 AI 腔模板句
**症状**：
- 「在当今数字化时代……」
- 「随着 AI 技术的不断发展……」
- 「综上所述……」
- 「希望本文能为你带来启发……」
**修复**：全部删除或替换为具体语境下的自然表达

### E13 — useCases 用例过于泛化
**症状**：「设计师可以用 AI 工具提高效率」
**修复**：添加具体场景和数据：「UI 设计师使用 Figma AI 插件后，将原型设计时间从 4 小时压缩到 45 分钟」

### E14 — 数据无来源
**症状**：文中出现「市场年增长 47%」但无引用
**修复**：在正文中直接标注来源（如「据 Gartner 2026 年报告……」），并在 References 中加条目

---

## 技术类

### E15 — `blogLayout.heroImage` 路径错误
**症状**：`"heroImage": "/tools/xxx.jpg"` → 实际图片在 `/public/blog/xxx/hero.jpg`
**修复**：确认图片文件已放到正确目录，路径与部署仓 public 目录匹配

### E16 — 中英文 `publishDate` 格式不一致
**症状**：中文 `"2026年7月16日"` vs 英文 `"2026-07-16"`（用了 ISO 格式）
**修复**：英文展示格式为 `"July 16, 2026"`，ISO 格式 `"2026-07-16"` 仅用于 `blog-meta.ts`

### E17 — 中英文 blocks 数量不一致
**症状**：中文有 12 个 blocks，英文有 11 个（漏了 1 个）
**修复**：逐 block 比对 JSON，确保 type 和数量完全一致

### E18 — `npm run build` 失败：TypeScript 类型错误
**症状**：新增 blog-pages-config.ts 条目后 build 报类型不匹配
**修复**：检查 `BlogPageItem` 接口，确认所有必填字段都已填入（`slug`, `shortTitleEn`, `shortTitleZh`, `routeCategory`）

---

## 流程类

### E19 — 跳过了 Research 步骤直接写作
**症状**：文章内容仅来自知识块，无 SERP 分析无第三方数据
**修复**：回退到 Step 2，完成 Research Log 后再继续

### E20 — 英文版是中文版的逐字翻译
**症状**：英文读起来像机翻，长句结构怪异
**修复**：重写英文版，意译优先。英文自然比中文长 1.2–1.8×，拆分长句

### E21 — 创建了不需要的 page.tsx
**症状**：在 `app/[locale]/blog/` 路径外额外创建了一个页面文件
**修复**：删除。路由和渲染由动态路由 + getPageData() 统一处理

---

*common-errors.md · v1.0 · 2026-07-16*
