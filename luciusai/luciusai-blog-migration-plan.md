# Lucius AI Blog 迁移计划：现有 CMS → OpenBlog

> **目标**：用 **Markdown in Git + OpenBlog + Next.js SSG** 替换 luciusai.com 内嵌 CMS；博客独立部署于 `E:\客户部署项目\luciusai-blog`，经主域 Rewrite 挂回 `/blog/*`。
>
> **OpenBlog 源码**：`E:\自有部署项目\openblog`  
> **部署项目**：`E:\客户部署项目\luciusai-blog`  
> **状态**：Phase 2 基础配置 ✅ · 文章迁移待 Phase 1

**Last updated**: 2026-09-02

---

## 当前进度

| 阶段 | 状态 | 说明 |
|------|------|------|
| Phase 0 URL 盘点 | ⏳ 待做 | 以 `luciusai-site-structure.md` §1.9 为基准 |
| Phase 1 CMS 导出 | ✅ 完成 | 38 en + 38 zh，图片已本地化 |
| **Phase 2 OpenBlog 脚手架** | **✅ 完成** | `create-openblog` + Lucius chrome/config |
| Phase 3 反向代理 | ⏳ 待做 | Cloudflare/Railway Rewrite |
| Phase 4 切流 | ⏳ 待做 | |
| Phase 5 质检 | ⏳ 待做 | `luciusai-blog-article` SKILL |

---

## 架构

```
luciusai.com（主站 — Railway + Cloudflare）
  rewrites: /blog/*, /zh/blog/* → BLOG_ORIGIN
       ↓
E:\客户部署项目\luciusai-blog（OpenBlog 独立部署）
  SITE_URL=https://luciusai.com · DEPLOY_MODE=subdirectory
       ↓
e:\clients\luciusai\（策略仓 — skills、site-structure，不混入 Next 应用）
```

---

## Phase 2 已完成项

- [x] `create-openblog` 生成 `luciusai-blog` 项目
- [x] `openblog.config.ts` — Lucius site/chrome/features
- [x] `src/chrome/site-chrome.ts` — nav/footer 对齐 luciusai.com
- [x] `public/brand/lucius-logo.svg` — 从主站下载
- [x] `.env.example` / `.env.local` — subdirectory 模式
- [x] `src/config/i18n.ts` — en/zh/pt-BR 路由规划
- [x] `integrations/DEPLOY.md` — Rewrite runbook
- [x] `content/blog/` 空目录（无示例文章）

---

## 下一步（Phase 0 + 1）

1. **URL 主表**：38 slug × 3 locale，对照 GSC 已索引 URL
2. **CMS 导出脚本**：从现 Railway CMS 或 HTML 抓取 → Markdown
3. **图片镜像**：`public/blog/images/{slug}/`
4. **i18n 路由实现**：`/zh/blog/*` middleware + `content/blog/zh/`

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [luciusai-site-structure.md](./luciusai-site-structure.md) | 38 slug + i18n URL |
| [luciusai-zh-i18n-audit.md](./luciusai-zh-i18n-audit.md) | 中文 blog 质量 |
| [medo/archive/medo-blog-migration-plan.md](../medo/archive/medo-blog-migration-plan.md) | 阶段划分模板 |
| `E:\客户部署项目\luciusai-blog/README.md` | 部署项目说明 |
