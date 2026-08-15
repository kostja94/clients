# Oginify Content Graph — Hub-Spoke 图谱

> 加载时机：Phase 0 / Phase 0R / Phase 3 / Phase 5
> 主文件：SKILL.md §4 指针

---

## 1. 文件表与下一序号

| NN | 文件 | slug | 类型 | 角色 | 主关键词 |
|----|------|------|------|------|---------|
| 01 | 01-best-ai-og-image-generators.md | `best-ai-og-image-generators` | Ranking | Spoke（发布先行） | best AI open graph image generators |
| 02 | 02-what-is-open-graph-image.md | `what-is-open-graph-image` | Glossary | **Hub** | what is open graph image |

**下一序号：03**

---

## 2. Hub-Spoke 结构

```
                    ┌──────────────────────────────────────────┐
                    │  02 what-is-open-graph-image (Hub)       │
                    │  Glossary — category definition          │
                    └────────────────────┬─────────────────────┘
                                         │
        ┌────────────────────────────────┼───────────────────────────────┐
        │                    │                    │             │
  ┌─────▼──────┐   ┌─────────▼───────┐   ┌────────▼───────┐   ┌─────▼──────────┐
  │ 01 Ranking │   │ 03 HowTo        │   │ 04 SizeGuide   │   │ 05 MetaGuide   │
  │ best AI    │   │ how to create   │   │ og image size  │   │ og:image tags  │
  │ OG gens    │   │ OG image        │   │ (Track T)      │   │ + validator    │
  └────────────┘   └─────────────────┘   └────────────────┘   └────────────────┘
        │                    │                    │             │
        └─────────────────── 全 Spoke 双向互链 Hub ─────────────┘
```

**阅读旅程**：Awareness（Hub 定义）→ Tool selection（Ranking）→ Build（HowTo / MetaGuide）→ Publish（SizeGuide / Validator）。

---

## 3. P0 战略队列（Track S）

| 状态 | 优先级 | 类型 | slug | 主关键词 | 备注 |
|------|--------|------|------|---------|------|
| **Done** | P0 | Ranking | `best-ai-og-image-generators` | best AI OG generators | #01 · 2026-08-15 |
| **Next** | P0 | Glossary | `what-is-open-graph-image` | what is open graph image | **Hub #02** |
| Backlog | P1 | HowTo | `how-to-create-open-graph-image` | how to create OG image | #03 候选 |
| Backlog | P1 | SizeGuide | `open-graph-image-size` | og image size | Track T #04 |
| Backlog | P1 | MetaGuide | `open-graph-meta-tags-guide` | og:image meta tags | #05 |
| Backlog | P2 | Alternative | `oginify-vs-vercel-og` | oginify vs vercel og | 竞品拦截 |
| Backlog | P2 | DeveloperGuide | `social-cards-skills-guide` | social-cards-skills | 开源 |
| Backlog | P2 | UseCase | `refresh-blog-og-images` | refresh blog og images | 场景 |

---

## 4. Canonical Concept Registry

| 概念 | Canonical | 引用方式 |
|------|-----------|---------|
| Open Graph image 定义 | `/blog/what-is-open-graph-image`（Hub） | 1–2 句 + link |
| 1200×630 规格 | `/blog/what-is-open-graph-image` H2 | 其他文 1 句 + link 或 P3 来源 |
| Best AI OG generators | `/blog/best-ai-og-image-generators` | Ranking canonical |
| URL-first vs 通用生图 vs 代码驱动 | `/blog/best-ai-og-image-generators` H2 | 三分类框架 canonical |
| OG image 尺寸 | `/blog/open-graph-image-size` | SizeGuide canonical |
| meta tags 设置 | `/blog/open-graph-meta-tags-guide` | MetaGuide canonical |

---

## 5. 冲突表（MERGE 对照）

| 新选题关键词 | 已有 canonical | 判定 |
|-------------|---------------|------|
| best open graph image generator / top og tools | `best-ai-og-image-generators` | 链 #01；`best-og-image-generator` 变体 STOP（C4，301 到 hub） |
| open graph image definition / meaning | `what-is-open-graph-image` | KEEP Hub；Spoke 文不抢定义词（C2） |
| og image dimensions / size | `open-graph-image-size` | KEEP Track T |
| how to add og image | `how-to-create-open-graph-image` | KEEP HowTo；平台-specific 可拆 |
| oginify vs vercel | `oginify-vs-vercel-og` | KEEP Alternative；单竞品 head-to-head |
| free og image maker | `/free-og-image-maker`（工具页） | **ToolGuide 短稿** + 链工具页；不复制工具页全文（C3） |

---

## 6. Blog 互链矩阵（Track S — 以本表为准）

| slug | 正文应链 | 最低 |
|------|---------|:---:|
| `what-is-open-graph-image`（Hub） | → `best-ai-og-image-generators` · → 后续各 Spoke | ≥3 |
| `best-ai-og-image-generators` | → `what-is-open-graph-image` · → `open-graph-meta-tags-guide`（若存在） | ≥2 |
| `how-to-create-open-graph-image` | → `what-is-open-graph-image` · → `best-ai-og-image-generators` | ≥2 |
| `open-graph-image-size`（T） | → `what-is-open-graph-image` | ≥1 |
| `open-graph-meta-tags-guide` | → `what-is-open-graph-image` · → `/open-graph-validator` | ≥2 |

---

## 7. 301 计划（人类执行）

| 旧 URL slug | 新目标 |
|-------------|--------|
| `best-og-image-generator` | `best-ai-og-image-generators` |
| `top-5-og-tools` | `best-ai-og-image-generators` |

---

## 8. Golden Examples

| 类型 | 标杆稿 | 说明 |
|------|--------|------|
| Ranking | `01-best-ai-og-image-generators.md` | #1 Oginify + 三分类框架 + 每竞品优势（已发布 #01） |
| Hub | 待写 #02 | Glossary canonical |

---

## 9. 发布后人类 checklist

1. bump SKILL.md §0 + §4「下一文件序号」
2. bump 本文件 §1「下一文件序号」
3. 更新 §1 已发布文章登记表
4. 更新 §3 排期表（标记 ✅）
5. bump SKILL.md frontmatter `version` patch
6. 更新 `blog/README.md` 文章表
