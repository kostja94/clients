# Floatboat 项目任务

> - **正式站**：floatboat.ai（生产环境）
> - **开发环境**：Lovable（https://floatboat.lovable.app/）— 新页面在此构建后部署
>
> 任务排期以 Lovable 开发环境中的页面为主。正式站现有结构与路由见 [floatboat-site-structure.md](../floatboat-site-structure.md)。

**Last updated**: 2026-06-03（增补：定位 pivot 文档同步 + 目录站提交）

---

## 开发环境页面状态

以下页面在 Lovable 中已构建完毕。构建完成后部署至 floatboat.ai。

**✅ 内容已确认（可部署）：**

| 页面 | 说明 |
|------|------|
| `/` | 首页 |
| `/floatim` | FloatIM 功能页 |
| `/ai-file-organizer` | AI 文件整理器 |
| `/use-cases` | 使用场景总页 |
| `/use-cases/for-solopreneur` | 单人创业者场景 |
| `/use-cases/for-creators` | 创作者场景 |
| `/use-cases/for-small-business` | 小企业场景 |
| `/use-cases/for-studio` | 工作室场景 |
| `/models` | 模型聚合页 |
| `/models/auto-mode` | Auto Mode 模型详情 |
| `/pricing` | 定价 |
| `/submit` | 提交 Skills |
| `/may-ai-festival` | 五月 AI 活动 |
| `/creator-program` | 创作者计划 |
| `/leaderboard` | Skills Leaderboard |

**🔶 已上线但内容待调整：**

| 页面 | 说明 |
|------|------|
| `/about` | 关于页面 |
| `/changelog` | 更新日志 |
| `/combo-store` | Combo Store 主页面 |
| `/download` | 下载页 |
| `/features` | 功能总览 |
| `/integrations` | 集成页 |
| `/blog` | 博客列表页 |
| `/blog/introducing-floatim` | Introducing FloatIM 博文 |
| `/blog/floatim-launches-agent-native-messaging` | FloatIM Launches 博文 |
| 模型详情×4 | `/models/deepseek`, `/models/minimax`, `/models/glm`, `/models/kimi` |

**🔶 Combo Store Skills 详情页（已上线，内容待调整）：**
约 200+ skill 详情页（路径模式 `/combostore/{slug}`），中英文双语，需统一内容模板后进行批量填充。

---

## Phase 0：高优先级内容调整（P0）

| # | 任务 | 页面 |
|---|------|------|
| **0.0** | **全站定位同步：Desktop Workspace → Calendar-Driven Proactive Agent OS** | **floatboat.md / features / keywords / competitors / use-cases / brand-visual** |
| 0.1 | 功能总览页内容撰写（Calendar-Driven 叙事） | `/features` |
| 0.2 | 下载页面内容 + CTA 优化 | `/download` |
| 0.3 | 关于页面品牌叙事 | `/about` |
| 0.4 | Combo Store 主页面内容 / 分类优化 | `/combo-store` |
| 0.5 | 集成页面内容 | `/integrations` |
| 0.6 | 更新日志页面内容 | `/changelog` |
| 0.7 | 模型详情页内容调整（4 页） | `/models/deepseek` 等 |
| **0.8** | **导航站/目录站提交（TAAFT + Toolify + Aixploria 等 7 站）** | **[floatboat-directory-submission.md](../floatboat-directory-submission.md)** |

---

## Phase 1：Blog 与品牌内容（P0）

| # | 任务 | 备注 |
|---|------|------|
| 1.1 | 博客列表页内容优化 | `/blog` |
| 1.2 | Introducing FloatIM 博文内容调整 | `/blog/introducing-floatim` |
| 1.3 | FloatIM Launches 博文内容调整 | `/blog/floatim-launches-agent-native-messaging` |

---

## Phase 2：Combo Store 详情页内容（P1）

| # | 任务 | 页数 |
|---|------|------|
| 2.1 | Combo Store 详情页内容模板/风格统一 | 模板定稿 |
| 2.2 | 批量填充 skill 详情页（按优先级分批） | ~200+ 页 |

---

## Phase 3：新增页面（P1）

| # | 任务 | 建议路由 |
|---|------|----------|
| 3.1 | 对比页：vs Claude Cowork | `/vs/claude-cowork` |
| 3.2 | 对比页：vs Manus | `/vs/manus` |
| 3.3 | 功能支柱页：Combo Skills | `/features/combo-skills` |
| 3.4 | 功能支柱页：Tacit Engine | `/features/tacit-engine` |
| 3.5 | FloatIM 子路由：Protocols | `/floatim/protocols` |
| 3.6 | FloatIM 对比页：vs Floatboat | `/floatim/vs-floatboat` |
| 3.7 | 人群落地页：Solopreneur / Creator 等 | `/use-cases/*` 独立页 |

---

## Phase 4：SEO 与技术项（P1-P2）

| # | 任务 | 备注 |
|---|------|------|
| 4.1 | 全站 head() / OG / meta 审计 | 确保每页独立 |
| 4.2 | hreflang 配置（中英文站） | `/zh/` 路由规划 |
| 4.3 | SoftwareApplication JSON-LD | 首页或下载页 |
| 4.4 | sitemap 维护与 GSC 提交 | 新路由加入后更新 |

---

## Legend

| Priority | 含义 |
|----------|------|
| P0 | 立即影响品牌形象与转化 |
| P1 | 高价值但可并行 |
| P2 | 迭代优化 / 前瞻探索 |

> **部署流程**：Lovable 开发 → 内容确认 → 部署至 floatboat.ai
