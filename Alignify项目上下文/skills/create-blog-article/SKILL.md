# Create Blog Article — Alignify 通用 Blog 文章创建 Skill

> **用途**：从知识块（`knowledge/{tools,marketing,seo,insights}/{slug}.md`）到发布就绪的正式文章（中文 JSON + 英文 JSON + Meta 注册 + 配置注册）的完整流程。
> **版本**：v1.0 · 2026-07-16
> **适用范围**：Alignify 新 Blog 文章创建。所有新文章统一走 `/blog/{slug}` 路由；通过 `routeCategory` 区分在 Tools/Marketing/SEO/Insights Hub 的展示位置。
> **文章类型**：本 Skill 面向 **4 种文章类型**（Tools 榜单/对比、Marketing 策略/案例、SEO 指南/教程、Insights 行业分析），各类型有独立的章节结构、Meta 规则和 JSON 字段约定。

---

## 路由决策（先读此节）

| 场景 | 路由 | 内容目录 | Meta 注册 | Config 注册 |
|------|------|---------|-----------|-------------|
| **新文章（默认）** | `/blog/{slug}` | `content/blog/{en,zh}/{slug}.json` | `src/data/blog-meta.ts` | `src/data/blog-pages-config.ts` |
| 旧文章（保持不变） | `/tools/{slug}` | `content/tools/{en,zh}/{slug}.json` | `src/data/tools-meta.ts` | `src/data/tools-pages-config.ts` |

**`blog-pages-config.ts` 的 `routeCategory` 决定 Hub 归属**：

```typescript
// src/data/blog-pages-config.ts
export type BlogRouteCategory = "tools" | "marketing";
export interface BlogPageItem {
  slug: string;
  shortTitleEn: string;
  shortTitleZh: string;
  routeCategory: BlogRouteCategory;  // 决定该文出现于哪个 Hub
  // tools 类还需指定：
  toolsHubCategory?: string;
  // marketing 类还需指定：
  marketingHubCategory?: string;
}
```

---

## 何时使用本 Skill

当以下条件**全部满足**时加载本 Skill：

- [ ] `knowledge/{tools,marketing,seo,insights}/{slug}.md` 知识块已创建并通过分类模板核对
- [ ] 需要创建对应的 `/blog/{slug}` 正式页面
- [ ] 该 slug 尚未在 `blog-pages-config.ts` 中注册

**不适用场景**：
- 知识块尚未完成 → 先完成知识块
- 仅为已有文章做局部优化 → 使用 `optimize-tools-internal-links` Skill 或 `content/sections/section-optimization-playbook.md`
- 创建的是纯事件页(/events)或词汇表(/glossary) → 路由模型不同，使用各自的 template

---

## 流程总览

```
Step 1 — Intake & 文章分类（Gate A）
   ├── 核查知识块所在目录（tools/marketing/seo/insights）
   ├── 判定文章类型 → 选择 Meta 规则组（Best 型 / 指南型 / 策略型 / 分析型）
   ├── 在对应 README 注册 slug
   └── 在关键词文件中新增锚点
        ↓
Step 2 — Research（Gate 0R）
   ├── R1：知识块 SSOT 素材梳理
   ├── R2：SERP 搜索 → 竞品文章结构 + 排名前 3–5 页分析
   ├── R3：URL 原文 Fetch（第三方数据、官方定价、案例详情）
   └── Synthesis Statement + Candidate Examples + Research Log
        ↓
Step 3 — 创建中文文章 JSON
   ├── 按类型章节结构组装（4 种类型的结构见 references/article-types.md）
   ├── 创建 content/blog/zh/{slug}.json
   ├── 从知识块 + Research 素材提取数据填入
   └── 内链初稿同步写入
        ↓
Step 3b — 中文本地化润色（必做）
   ├── 加载 skills/localize-content-zh/SKILL.md
   ├── 术语统一、References title 中文化、blogLayout 日期
   └── 运行 deploy 仓 polish-zh-page.py
        ↓
Step 4 — Meta 注册 + Config 注册
   ├── 在 blog-meta.ts 新增 slug 条目（含 publishDate）
   ├── 在 blog-pages-config.ts 新增条目（含 routeCategory + hubCategory）
   ├── 确认 routeCategory 与 knowledge/ 目录一致性
   └── 工具型文章需确认 toolsHubCategory，营销型需确认 marketingHubCategory
        ↓
Step 5 — 创建英文文章 JSON
   ├── 中文完成后再创建 content/blog/en/{slug}.json
   └── 意译非逐句，适当本地化（示例、定价单位、FAQ）
        ↓
Step 6 — 质量门控（Gate P0 + H3 + SelfCheck）
   ├── Gate P0：7 项一票否决（Meta 四要素、FAQ≥3、howToChoose title/name、
   │    结论位置、图片存在、publishDate 双重位置、build 成功）
   ├── H3：叙事字数硬门槛（各类型不同，见 references/quality-checklist.md）
   ├── SelfCheck 12 维 Pass/Fail
   └── 加权评分（A–J 十维，≥70 分 publish-ready）
        ↓
Step 7 — 发布日期错开（Blog 新文，成批上线前）
   ├── 仅 /blog/{slug} 未上线 slug
   ├── 从今天往前一天一篇（避让已占用日）
   └── stagger-unpublished-publish-dates.py（三处同步）
```

**关键原则**：
- **新文章走 `/blog/`**：JSON 放 `content/blog/`，Meta 注册到 `blog-meta.ts`
- **routeCategory 决定 Hub 归属**：tools → /tools hub，marketing → /marketing hub
- **先中文，后英文**：中文定稿后再一次性创建英文
- **先 Research，后写作**：素材不足时回退补 Research，不硬写
- **知识块 ≠ 文章**：知识块是非线性笔记，文章需改写为叙事体例
- **无需创建 page.tsx**：路由和页面渲染由动态路由 + `getPageData("blog", slug, locale)` 统一处理

---

## 各步骤详细文档

| 步骤 | 文档 | 产出 |
|------|------|------|
| 1 | [`01-intake-and-classify.md`](./01-intake-and-classify.md) | 文章类型判定 + Gate A 通过 + 关键词注册 + README 条目 |
| 2 | [`02-research.md`](./02-research.md) | Research Log + Synthesis Statement + Candidate Examples |
| 3 | [`03-article-structure.md`](./03-article-structure.md) | `content/blog/zh/{slug}.json` + 内链初稿 |
| 3b | [`../localize-content-zh/SKILL.md`](../localize-content-zh/SKILL.md) | 中文地道化 + References 中文化 |
| 4 | [`04-meta-and-config.md`](./04-meta-and-config.md) | `blog-meta.ts` + `blog-pages-config.ts` 更新 |
| 5 | [`05-english-localization.md`](./05-english-localization.md) | `content/blog/en/{slug}.json` |
| 6 | [`06-quality-gates.md`](./06-quality-gates.md) | Gate P0 通过 + H3 通过 + SelfCheck Pass + 加权评分 ≥70 |
| 7 | [`07-publish-date-stagger.md`](./07-publish-date-stagger.md) | Blog 未上线 slug `publishDate` 三处同步错开 |

---

## 核心引用

| 引用 | 用途 | 路径 |
|------|------|------|
| 知识块模板（Tools） | 验证 tools 知识块合规 | `knowledge/tools/_TEMPLATE.md` |
| 知识块模板（Marketing） | 验证 marketing 知识块合规 | `knowledge/marketing/` 现有文件结构 |
| 知识块模板（SEO） | 验证 seo 知识块合规 | `knowledge/seo/` 现有文件结构 |
| 知识块模板（Insights） | 验证 insights 知识块合规 | `knowledge/insights/` 现有文件结构 |
| 部署仓 blog-meta.ts | 确认 Meta 格式与现有条目 | `src/data/blog-meta.ts`（部署仓） |
| 部署仓 blog-pages-config.ts | 确认 config 字段与 Hub 分组 | `src/data/blog-pages-config.ts`（部署仓） |
| 部署仓 tools-pages-config.ts | 确认 toolsHubCategory 可用值 | `src/data/tools-pages-config.ts`（部署仓） |
| 部署仓 marketing-pages-config.ts | 确认 marketingHubCategory 可用值 | `src/data/marketing-pages-config.ts`（部署仓） |
| Section 规范 | 各章节组件格式 | `content/sections/` 对应文件 |
| 内链 Skill | 存量内链优化 | `skills/optimize-tools-internal-links/SKILL.md` |
| 中文本地化 Skill | 中文润色 | `skills/localize-content-zh/SKILL.md` |
| **clients 质量体系** | Gate 设计、Research 三角、SelfCheck、加权评分 | `D:\项目文档\clients\skills for clients\blog-create\` + `blog-audit\` |

---

## 快速参考：四种文章类型速查

| 类型 | Knowledge 目录 | routeCategory | Meta 规则组 | 典型范例 |
|------|---------------|---------------|------------|---------|
| **Tools 榜单/对比** | `knowledge/tools/` | `"tools"` | Best 型（含「最佳」/`Best`） | `/blog/image-generator` |
| **Marketing 策略/案例** | `knowledge/marketing/` | `"marketing"` | 策略型（含「指南」/`Guide`） | `/blog/github-for-marketing` |
| **SEO 指南/教程** | `knowledge/seo/` | `"tools"` 或 `"marketing"` | 指南型（含「如何」/`How to`） | `/blog/domain` |
| **Insights 行业分析** | `knowledge/insights/` | `"tools"` 或 `"marketing"` | 分析型（含「分析」/`Analysis`） | `/blog/ai-product-naming` |

> **注意**：SEO 和 Insights 类型的 `routeCategory` 需根据内容主题判断归属——偏工具选型归 tools，偏策略思考归 marketing。

### 各类型章节结构差异

| 类型 | 必有 block | 可选 block | 特有差异 |
|------|-----------|-----------|---------|
| **Tools** | `tldr`, `section(什么是)`, `howItWorks`, `bestTools`, `comparisonSection`, `useCases`, `howToChoose`, `section(结论)`, `faq`, `references` | — | `bestTools` 每产品含 `shortDescription`/`imageSrc`/`linkUrl` |
| **Marketing** | `tldr`, `section(概念)`, `section(策略)×N`, `useCases`, `section(结论)`, `faq`, `references` | `bestTools`, `howItWorks`, `comparisonSection`, `html` | 可用 `heroHtml` 做 Hero CTA；`childrenHtml` 嵌复杂表格 |
| **SEO** | `tldr`, `section(概念)`, `section(操作)×N`, `useCases`, `section(结论)`, `faq`, `references` | `howItWorks`, `bestTools`, `howToChoose` | `tldr.items` 可用 `{title, content}` 对象格式；`subSections` 重使用 |
| **Insights** | `tldr`, `html`（核心正文）, `section(结论)`, `faq`, `references` | `section`, `useCases` | 主体内容走 `type: "html"` 长文块；无固定 `bestTools`/`howToChoose` |

---

## 质量检查脚本与命令

**部署仓** `alignify-by-kostja`：

```bash
npm run verify:content-json    # JSON 结构校验
npm run audit:howto-choose     # howToChoose 字段检查
npm run audit:internal-links   # 内链拓扑检查
npm run build                  # 全量构建验证
```

**clients 工具** `D:\项目文档\clients\skills for clients\tools\`：

```bash
# 按需在对应文章路径运行
python frontmatter_validator.py   # Gate C / 维度 9（F1–F8 字段检查）
python word_count_narrative.py    # H3 叙事字数硬门槛
python link_checker.py            # P0 G2/G6 死链检测
```

---

## 参考速查表

| 文档 | 内容 |
|------|------|
| [`references/article-types.md`](./references/article-types.md) | 4 种文章类型的完整结构 × JSON 字段映射 × 差异对照 |
| [`references/meta-requirements.md`](./references/meta-requirements.md) | 4 种 Meta 规则组（Best/指南/策略/分析）× publishDate 双位置 × routeCategory 填写规则 |
| [`references/quality-checklist.md`](./references/quality-checklist.md) | P0 7 项 + H3 字数门槛 + SelfCheck 12 维 + 十维加权评分（100 分制） |
| [`references/common-errors.md`](./references/common-errors.md) | 已归档的常见错误与修复方案 |
| [`01-intake-and-classify.md`](./01-intake-and-classify.md) | Step 1 完整流程：知识块核查 + 类型判定 + 关键词注册 |
| [`02-research.md`](./02-research.md) | Step 2 Research 三角（R1/R2/R3）+ Research Log 模板 |
| [`03-article-structure.md`](./03-article-structure.md) | Step 3 各类型 JSON 创建流程 + 内链初稿规则 |
| [`04-meta-and-config.md`](./04-meta-and-config.md) | Step 4 Meta + Config 三层注册 + routeCategory 决策 |
| [`05-english-localization.md`](./05-english-localization.md) | Step 5 中→英意译 + 各类型本地化差异 |
| [`06-quality-gates.md`](./06-quality-gates.md) | Step 6 Gate P0 + H3 + SelfCheck + 加权评分汇总 |
| [`07-publish-date-stagger.md`](./07-publish-date-stagger.md) | Step 7 Blog 新文 publishDate 三处同步错开 |

---

*create-blog-article · v1.0 · 2026-07-16*
