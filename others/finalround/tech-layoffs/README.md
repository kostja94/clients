# Tech Layoffs — Bella 的运营手册

> **Hi Bella，这个文件夹就是你的地盘了。**

你是 Tech Layoffs 板块的**唯一负责人**——从数据采集、JSON 编辑，到构建部署、SEO 验证，全流程由你掌控。Kostja 会在一开始带你走通整个流程，之后你就可以独立运作了。

---

## 这个板块是干什么的

Final Round AI 主站上有一个 Tech Layoffs 栏目（`www.finalroundai.com/tech-layoffs`），追踪全球 146 家科技公司裁员动态，吸引被裁员或担心裁员的求职者访问，最终引导他们使用 Final Round 的面试产品。

**你的工作就是让这个栏目保持新鲜、准确、有流量。**

具体来说：
- 监控全球裁员新闻 → 决定要不要新增公司 JSON 文件
- 维护已有公司的 JSON 数据（比如某公司又裁第二轮）
- 确保每次改动正常构建、部署、线上生效

---

## 技术速查

| 项 | 值 |
|----|-----|
| 本地开发端口 | **8080**（`npm run dev` → `http://localhost:8080`） |
| 构建命令 | `npm run build`（prebuild → next build → 151 静态页） |
| Vercel 生产 URL | `https://finalround-nextjs.vercel.app` |
| 公司数据位置 | `src/data/companies/{slug}.json`（146 个 JSON 文件） |
| Barrel index | `src/data/companies/index.ts`（自动生成，不手动编辑） |

---

## 文件夹地图

按**你需要什么、什么时候看**排列：

| 如果你要… | 看这个 |
|-----------|--------|
| 搞清楚整体情况 | [01-overview.md](./01-overview.md) — 板块定位、146 家公司、数据架构、技术栈 |
| 知道每天/每周该干嘛 | [02-sop.md](./02-sop.md) — 操作 SOP：日常监控、周常更新、事件响应 |
| 查某个数据该从哪找 | [03-data-guide.md](./03-data-guide.md) — 数据来源、更新频率、验证规则 |
| 新增一家公司页 | [04-page-template.md](./04-page-template.md) — JSON 字段模板 + 数据验证 |
| 把改好的内容部署上线 | [05-deploy-guide.md](./05-deploy-guide.md) — 本地 → 构建 → Vercel → 主域验证 |
| 发布前做 SEO 检查 | [06-seo-checklist.md](./06-seo-checklist.md) — 发布前必查清单 |
| 查找原始裁员数据 | [data/layoff-data.md](./data/layoff-data.md) — 180+ 家公司裁员记录 |
| 看竞品怎么做、找外部参考 | [reference/resources.md](./reference/resources.md) — 外部资源与竞品 |
| 排查技术问题（Kostja 带你看） | [reference/architecture.md](./reference/architecture.md) — Rewrite、路由、数据流 |

---

## 3 步上手

**先读再动手，顺序很重要：**

1. **先读 [01-overview.md](./01-overview.md)** — 了解板块全貌：做什么、给谁看、数据怎么组织的。15 分钟。

2. **再读 [02-sop.md](./02-sop.md)** — 知道你的日常工作节奏。10 分钟。

3. **跟着 [05-deploy-guide.md](./05-deploy-guide.md) 做一遍** — 让 Kostja 带你走一次完整流程：改 JSON → `npm run build` → 部署 → 验证。这是你最常操作的动作。

---

## 遇到问题怎么办

| 问题类型 | 看哪里 / 找谁 |
|----------|-------------|
| 数据对不上 | [03-data-guide.md](./03-data-guide.md) §数据冲突处理 |
| `npm run build` 失败 | [05-deploy-guide.md](./05-deploy-guide.md) §故障排查 |
| 部署后线上没变化 | [05-deploy-guide.md](./05-deploy-guide.md) §验证步骤 |
| 主域 Rewrite 有问题（origin 正常但主域不对） | 找 **Mohit**（主站 Rewrite 规则维护） |
| 页面打不开/样式错乱/Vercel 构建问题 | 找 Kostja |
| 不知道该不该新增一个公司页 | [02-sop.md](./02-sop.md) §事件驱动 |
| SEO 排名掉 | [06-seo-checklist.md](./06-seo-checklist.md) 逐项复查 |

---

## 谁负责什么

| 范围 | 负责人 |
|------|--------|
| 公司数据、JSON 内容、FAQ | **Bella** |
| 代码/组件/样式修改 | **Bella**（Kostja 指导） |
| Vercel 项目配置、环境变量 | Kostja |
| 主站 Rewrite 规则（/tech-layoffs → Vercel） | **Mohit** |
| Final Round 其他板块 | 其他人 |

---

*Last updated: 2026-06-03*
