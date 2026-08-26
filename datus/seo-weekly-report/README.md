# Datus SEO 周报

本目录为 **独立自包含工具包**：GSC + GA4 搜索周报 Skill、Blog 目录同步、品牌/内容簇注册表、API 脚本与历史报告。**执行与 Agent 生成周报均只需本文件夹内文件。**

> 范围：`datus.ai` 的 Google 搜索表现 + GA4 行为 + **`datus/blog` 每周新发布** 交叉分析。不含 docs.datus.ai / studio.datus.ai 分域。

---

## 文件清单

| 文件 | 用途 |
|------|------|
| [SKILL.md](./SKILL.md) | **唯一 Skill 文件** — 分析规则、报告模板、Agent 约束 |
| [datus-gsc-ga4-api-guide.md](./datus-gsc-ga4-api-guide.md) | GSC + GA4 API 接入 |
| [brand-query-registry.yaml](./brand-query-registry.yaml) | 品牌词 / 拼写变体 |
| [content-cluster-registry.yaml](./content-cluster-registry.yaml) | 内容簇 + blog category 映射 |
| [blog-catalog.yaml](./blog-catalog.yaml) | 从 `datus/blog` 同步的文章清单（`npm run sync-blog`） |
| [references/project-config.md](./references/project-config.md) | 站点事实（内嵌） |
| [templates/content-weekly-block.txt](./templates/content-weekly-block.txt) | 每周手工填写模板 |
| `scripts/` | sync-blog / fetch / merge |
| `data/` | JSON 输出（不入库） |
| `reports/` | 历史周报 |

---

## 分发给同事

可将 **整个 `seo-weekly-report/` 文件夹** 单独打包分享，无需附带仓库其他目录。

**若同事没有 monorepo 里的 `datus/blog`：**

1. 一并提供 `blog/` 目录，或
2. 在 `scripts/.env` 设置 `BLOG_DIR=/path/to/blog`

---

## 快速开始

### 1. 配置凭据

```bash
cd seo-weekly-report/scripts
cp .env.example .env
# 编辑 .env — 见 datus-gsc-ga4-api-guide.md
npm install
```

### 2. 每周拉数（推荐：周一）

```bash
npm run fetch-all
```

等价于：

```text
sync-blog  →  blog-catalog.yaml（读取 ../blog/*.md frontmatter）
fetch-gsc  →  data/gsc-weekly-YYYY-MM-DD.json
fetch-ga4  →  data/ga4-weekly-YYYY-MM-DD.json
merge      →  data/seo-report-bundle-YYYY-MM-DD.json
```

### 3. 填写项目执行块

复制 [templates/content-weekly-block.txt](./templates/content-weekly-block.txt)，填入本周实际发布的 slug。

### 4. 提交 AI 生成报告

将以下内容一起提交给 AI（Claude / Cursor Agent 等）：

1. **SKILL.md 全文**
2. `brand-query-registry.yaml` + `content-cluster-registry.yaml` + `blog-catalog.yaml`
3. `data/seo-report-bundle-YYYY-MM-DD.json`
4. 上周 `reports/datus-seo-weekly-report-YYYY-MM-DD.md`（如有）
5. 填好的 `===CONTENT===` / `===OBSERVATIONS===`

**指令：**

```text
按 datus-seo-weekly-report skill（识别 seo-report-bundle.json 自动化模式），
生成本周 Datus SEO 周报。
```

### 5. 保存报告

```text
reports/datus-seo-weekly-report-YYYY-MM-DD.md
```

---

## 手动模式（无 API）

1. GSC → 效果 → Compare 导出 xlsx
2. GA4 UI 导出 CSV（可选）
3. `npm run sync-blog`
4. 按 SKILL.md §0.3 提交

---

## 报告回答的五个问题

| # | 问题 | 数据来源 |
|---|------|----------|
| 1 | 本周搜索点击/曝光变化？ | `gsc.overall` |
| 2 | 哪几篇 `/blog/*` 在起量？ | `gsc.pages` + `contentClusters` |
| 3 | 品牌 vs 非品牌结构是否健康？ | `gsc.branded` / `queries[]` |
| 4 | 本周新发布的文章搜索表现如何？ | `blog.weeklyNewPosts` × `===CONTENT===` |
| 5 | 搜索流量有没有导向产品/GitHub？ | `ga4.events` + 落地页 |

---

## 每周 SOP

| 步骤 | 动作 | 负责人 |
|------|------|--------|
| 1 | 内容同事更新 `datus/blog` 并部署 | 内容 |
| 2 | `npm run sync-blog` | 增长 |
| 3 | 填写 `===CONTENT===`（实际上线 slug） | 内容/增长 |
| 4 | `npm run fetch-all`（需 VPN） | 增长 |
| 5 | 提交 AI 生成周报 | 增长 |
| 6 | Review §11 新文表现 + §14 行动项 | 全员 |
| 7 | 报告存 `reports/`，上周建议录入下周 §13 | 增长 |

---

## Blog 联动说明

- **自动**：`blog-catalog.yaml` 从 frontmatter 读取 `slug`、`date`、`category`
- **手工**：`===CONTENT===.published_slugs` 补充 CMS 实际上线日（可能与 git date 不同）
- **交叉**：merge 脚本将「本周 date 范围内的新文」与 GSC 页面数据自动匹配
- **复盘**：第二周表现见 §11.3（需上周报告）

---

## 版本

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | 2026-08-24 | 初版：GSC+GA4+blog 联动，自包含分发 |

*Last updated: 2026-08-24*
