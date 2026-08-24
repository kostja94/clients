# Floatboat 产品营销知识库

本文件夹为 **Floatboat.ai** 的自包含产品营销与内容策略文档包，可直接打包分享给文案、SEO、运营或 AI Agent 使用。所有链接均指向本文件夹内文件，无需访问上级目录或其他项目。

**官网**：[floatboat.ai](https://floatboat.ai/) · **开发预览**：[floatboat.lovable.app](https://floatboat.lovable.app/)

---

## 从哪里开始

| 角色 | 建议入口 |
|------|----------|
| 新人 / 全局了解 | [floatboat.md](./floatboat.md) |
| 写落地页 / Meta | [floatboat-features.md](./floatboat-features.md) → [floatboat-keywords.md](./floatboat-keywords.md) |
| Obsidian 落地页 / Integrations | [floatboat-obsidian.md](./floatboat-obsidian.md) |
| 写对比页 / 竞品文 | [floatboat-competitors.md](./floatboat-competitors.md) |
| DeepSeek Agent 小产品（SEO + 原生竞品） | [floatboat-deepseek-agent.md](./floatboat-deepseek-agent.md) |
| 写人群场景 | [floatboat-use-cases.md](./floatboat-use-cases.md) |
| 建站 / 路由 / SEO 技术 | [floatboat-site-structure.md](./floatboat-site-structure.md) · [floatboat-page-composition-guide.md](./floatboat-page-composition-guide.md) |
| 写博客 | [blog/README.md](./blog/README.md) |
| 全站 SEO/GEO 审计 | [site-seo-geo-audit/](./site-seo-geo-audit/)（清单 + Skill + tools，可整包外发） |
| SEO 周报 | [seo-weekly-report/floatboat-seo-weekly-report-skill.md](./seo-weekly-report/floatboat-seo-weekly-report-skill.md) |
| 历史归档 | [_archive/README.md](./_archive/README.md) |

**推荐阅读顺序**（详见 [floatboat.md](./floatboat.md)）：主文档 → 功能 → 关键词 → 竞品 → 场景 → 站点结构 → Skills 生态 → 落地页指南。

---

## 文件夹结构

```
floatboat/
├── README.md                          ← 本文件（入口）
├── floatboat.md                       ← 主文档 / 战略中枢
├── floatboat-features.md              ← 功能与关键词映射
├── floatboat-keywords.md              ← SEO 关键词梯队
├── floatboat-competitors.md           ← 竞品与截流词
├── floatboat-deepseek-agent.md        ← DeepSeek Agent：SEO 关键词 + 原生竞品简报
├── floatboat-use-cases.md             ← 人群与场景
├── floatboat-obsidian.md              ← Floatboat for Obsidian 落地页 + Integrations 方案
├── floatboat-page-composition-guide.md← Landing 页面搭建指南
├── floatboat-site-structure.md        ← 正式站路由结构
├── site-seo-geo-audit/                ← 全站 SEO/GEO 审计包（清单 + Skill + tools，可整包外发）
├── floatboat-skills-ecosystem.md      ← Combo Store / Leaderboard 生态
├── _archive/                          ← 已停用历史文档（含世界杯规划、目录站提交等）
│   └── README.md
├── seo-weekly-report/                 ← SEO 周报 Skill + 数据规范 + 历史样例
│   ├── README.md
│   ├── floatboat-seo-weekly-report-skill.md
│   ├── floatboat-seo-weekly-report-data-guide.md  ← GSC/Semrush 提交规范
│   └── floatboat-seo-weekly-report-*.md
└── blog/
    ├── README.md                      ← 博客工作流说明
    ├── scheduling-agent-article-plans.md  ← 主题簇构建方案
    ├── 01–08 *.md                     ← 博客草稿与终稿
    ├── schema/                        ← JSON-LD 样例
    ├── images/README.md               ← OG 图片说明（图片在现网）
    └── skills/floatboat-blog-article/ ← 博客创作 Skill（自包含）
```

---

## 给 AI Agent 的用法

1. 将 [floatboat.md](./floatboat.md) 复制为 `.cursor/product-marketing-context.md` 或 `.claude/product-marketing-context.md`。
2. 写博客时引用 [blog/skills/floatboat-blog-article/SKILL.md](./blog/skills/floatboat-blog-article/SKILL.md)。
3. 生成 SEO 周报时使用 [seo-weekly-report/floatboat-seo-weekly-report-skill.md](./seo-weekly-report/floatboat-seo-weekly-report-skill.md)（自包含，无需外部文档）；历史样例见同目录 `floatboat-seo-weekly-report-*.md`。
4. 全站 SEO/GEO 审计：整包见 [site-seo-geo-audit/](./site-seo-geo-audit/)，入口 [README.md](./site-seo-geo-audit/README.md)。

---

## 不包含在本包内的内容

| 内容 | 说明 |
|------|------|
| floatboat.ai 网站源码 | 本包无源码；以现网与 page-composition-guide 为准 |
| 博客 OG 图片文件 | 见 [blog/images/README.md](./blog/images/README.md)；图片托管于现网 `/blog/images/` |
| 现网 CMS 数据 | 正式站约 65+ 篇已发布博文；本包 `blog/` 为本地草稿与主题簇 |
| 历史 Campaign / 任务表 | 见 [_archive/](./_archive/README.md)，**活跃文档不引用** |

---

*Last updated: 2026-08-20*
