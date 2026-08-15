# Oginify 功能拆解

> **本文档职责**：逐一拆解 Oginify 各产品的功能、用户路径、差异化能力；链至 Keywords、Competitors，严格区分「能力描述」与「关键词策略」。  
> **引用**：[主文档](./oginify.md) 概览 | [site-structure](./oginify-site-structure.md) URL | [keywords](./oginify-keywords.md) 关键词 | [competitors](./oginify-competitors.md) 竞品 | [others](./oginify-others.md) 定价与成本

---

## 产品矩阵总览

| # | 产品 | 类型 | URL | 状态 | 一句话 |
|---|------|------|-----|------|--------|
| 1 | OG Generator | 核心 SaaS | `/` | 已上线 | 粘贴 URL → 2 张 1200×630 OG 图（截图 + 模板） |
| 2 | Above the Fold | 轻量工具 | `/above-the-fold` | 已上线 | 首屏截图 → 转 1200×630，无配额 |
| 3 | OG Validator | 辅助工具 | `/open-graph-validator` | 已上线 | 校验 OG 标签 → 0–100 分 → 多平台预览 |
| 4 | Twitter Card Generator | 产品 | `/twitter-card-generator` | 已上线 | 1200×675 X 专用卡片 + meta 标签 |
| 5 | Templates | 内容/工具 | `/templates` | 已上线 | 6 风格模板库 + 可编辑布局 |
| 6 | Gallery | 内容资产 | `/gallery` | 已上线 | 知名品牌 OG 图灵感库（约 100，待核实） |
| 7 | Websites Without OG | 内容资产 | `/websites-without-og-image` | 已上线 | 21 个知名站点缺 OG 的反面清单 |
| 8 | social-cards-skills | 开源 | GitHub | 已开源 | Agent Skills：程序化 OG + Twitter Card |

**漏斗关系**：

```
Generator（2 张输出，6 张/天免费）
  + Above the Fold（截图，无配额）
    → Validator（校验 OG 标签）
      → Gallery（看好案例被启发）
        → Websites Without（看反面教材被警示）
          → 付费转化（待上线）

social-cards-skills（并行渠道，MIT 永久免费）
```

---

## 1. OG Generator

### 功能描述

用户粘贴任意 URL → Firecrawl 抓取首屏截图 + 页面元数据 → 输出 2 张 1200×630 社交分享图（截图 + Next.js 模板渲染）。不满意可 Regenerate 用 AI 单独补生成。

### 生成流程

```
URL 输入
  → Firecrawl 轻度抓取（~3 次 scrape）→ 获取首屏截图 + 页面 meta
    → 第 1 张: 首屏截图 → top-crop 裁切 1200×630（非 AI）
      → 第 2 张: Next.js 模板渲染 1200×630（Satori/resvg，非 AI）
        → 返回 2 张 1200×630 PNG

（可选）Regenerate:
  对某张不满意 → 单独 AI 生成 1 张
    管线: Firecrawl scrape → aiBrief (Gemini 3 Flash) → Gemini/GPT 出图
```

### 输出策略 vs 风格库

**每次输出 2 张**：
- **第 1 张（截图）**: 首屏 → top-crop 1200×630，100% 保真
- **第 2 张（模板）**: Next.js + Satori/resvg 渲染，6 风格可选

**风格库（6 种）**，与 [Templates](/templates) 和 social-cards-skills 对齐：

| 风格 | 英文名 | 适用场景 |
|------|--------|----------|
| 瑞士极简 | Swiss Minimal | SaaS、dev tools、benchmark |
| 杂志风 | Magazine Editorial | 博客、长文、品牌故事 |
| 终端风 | Terminal / CLI | 技术文档、changelog、DevTool |
| 粗野主义 | Brutalist | 创意机构、campaign、个人站 |
| 复古印刷 | Newspaper | 新闻、深度报道、研究 |
| 像素风 | Pixel Retro | 独立游戏、hackathon、复古社区 |

### 用户路径

1. 首次用户：粘贴 URL → 看到 2 张图 → 下载或复制
2. 对某张不满意 → 单独 Regenerate 1 张（消耗 1 张配额 + AI 成本 $0.030/$0.024）
3. 满意后 → 下载 PNG → 上传到网站 / CMS
4. 超额用户 → PAYG $0.99 / Bundle 10 $7.90 / Bundle 50 $29.00

### 免费额度

匿名用户 **6 张/天**（`src/lib/quota.server.ts`，单桶模型无关）。详见 [oginify-others.md](./oginify-others.md#定价依据)。

### 技术特点

- 主流程非 AI：截图 + 模板渲染，~$0.005/次，几乎零成本
- Regenerate 按需调用 AI：Gemini Fast ($0.030) 或 GPT Precise ($0.024)
- 多风格模板：6 种风格，Next.js 模板与 social-cards-skills 共用视觉语言
- Markdown 截断：Regenerate 时 8000 字符保护，避免长页面 token 浪费

### 技术路线对比：OG 图生成的四种方式

| 方式 | 代表 | 速度 | 成本 | 灵活性 |
|------|------|------|------|--------|
| ① 代码模板渲染 | @vercel/og、Satori | 毫秒级 | 几乎 0 | 低 |
| ② 无头浏览器截图 | Puppeteer、Urlbox | 秒级 | 高 | 高 |
| ③ 模板 SaaS | OG Image API、Placid | 快 | 低-中 | 中 |
| ④ 混合（Oginify） | 截图 + 模板 + AI Regenerate | 秒级（主流程）| ~$0.005/次 | 最高 |

#### 为什么 Oginify 选混合路线

| 理由 | 说明 |
|------|------|
| 主流程零 AI 成本 | 截图 + 模板渲染即可覆盖 80% 场景 |
| AI 按需补充 | Regenerate 仅在用户不满意时触发，成本可控 |
| 内容多样性 | 模板库 + AI Regenerate = 兼顾速度与创意 |
| 用 AI 做差异化 | Regenerate 时 AI 风格不易撞脸 |

### 关键指标（待追踪）

- 生成次数 / 天
- 下载率、Regenerate 率
- 免费额度用尽 → 付费转化

---

## 2. Above the Fold — 首屏截图转 OG

首屏截图功能已整合入 Generator 主流程，作为输出的第 1 张图。独立 `/above-the-fold` 页面保留作为免费工具入口。

| | Generator 主流程 | Above the Fold 独立页 |
|---|---|---|
| 适合 | 日常 OG 图需求 | 只需要截图、不需要模板 |
| 成本 | ~$0.005/次 | 几乎 0 |
| 配额 | 6 张/天 | 无配额 |
| 速度 | 秒级 | 秒级 |
| 保真度 | 100% 忠实还原 | 100% 忠实还原 |

### 技术实现

```
URL → 无头浏览器渲染（JS 启用）→ 捕获首屏 1200×800
  → 浏览器端裁切上方 630px → 1200×630 PNG
```

---

## 3. OG Validator

粘贴 URL → 解析 OG / Twitter Card 标签 → 0–100 评分 → pass/warn/fail 清单 → X / Facebook / LinkedIn / Slack / Discord 预览。

校验维度、评分规则、用户路径同前。漏斗顶部工具，免费无配额。

---

## 4. Gallery（OG 图库）

curated 知名品牌真实 `og:image`，按 SaaS / AI / Dev tools / Design / E-commerce / Media / Fintech 分类。约 **100** 条（待后台核实）。

灵感 → 行动：看案例 → 跳转 Generator。

---

## 5. Websites Without OG Image

server-side 自动快照，追踪 **21** 个知名站点缺失 OG 或关键标签。支持 issue 过滤、takedown 入口、methodology 说明。

与 Gallery 形成正反对照。清单含 HN、xkcd、Berkshire Hathaway、W3.org、GNU、arXiv 等（完整列表见线上页）。

---

## 6. Templates

[/templates](https://oginify.com/templates) — 6 风格完整设计系统（ typography、spacing、anti-pattern），可点击预填 Generator。另含可编辑布局（Site Hero、Brand Card 等）。

风格来源 social-cards-skills，SaaS 与开源共用同一视觉语言。

**规划扩展（P1，详见 [by-style.md](./use-cases/by-style.md)）**：Text Overlay · Cinematic · Collage · Risograph — 搜索量与 CTR 潜力已调研，尚未上线。

---

## 7. Twitter Card Generator

[/twitter-card-generator](https://oginify.com/twitter-card-generator) — 输出 **1200×675**（2:1），针对 X timeline 优化：dark-mode 测试、20px edge inset、summary_large_image meta 标签一并输出。

与 OG Generator（1200×630）互补，详见 [by-image-size.md](./use-cases/by-image-size.md)。

---

## 8. social-cards-skills（开源）

MIT 许可，**永久免费**，与 SaaS 付费无关。

| 维度 | 内容 |
|------|------|
| **Skills** | `og-image-generator`（1200×630）+ `twitter-card-image-generator`（1200×675） |
| **视觉风格** | 6 种（Terminal / Magazine / Swiss / Pixel / Brutalist / Newspaper） |
| **渲染** | Satori + resvg |
| **安装** | `npx skills add kostja94/social-cards-skills` |

| | Oginify SaaS | social-cards-skills |
|---|---|---|
| 用户 | 站长、SEOer | 开发者、Agent 用户 |
| 收费 | 6 张/天免费 → PAYG $0.99 / Bundle | MIT 永久免费 |
| 方式 | 浏览器粘贴 URL | CLI / Agent 程序化 |

---

*Last updated: 2026-06-03. Generator 管线重构：主流程非 AI（截图+模板），AI 仅用于 Regenerate；定价方案锁定。*
