# Enter Pro — 杂项归档

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[enter-site-structure.md](./enter-site-structure.md) | [enter.md](./enter.md)

**Last updated**: 2026-06-25

---

## 1. Sitemap 明细

### 1.1 索引结构

```
https://enter.converge.ai/sitemap.xml   # 单文件平铺（非 sitemap 索引）
lastmod 抽样：2026-06-25T02:25:54.849Z（批量营销页）
```

**估算 URL 总量**：**~3,870**（2026-06-25 解析 sitemap.xml 全文计数）

### 1.2 URL 模式统计

| 模式 | 说明 | 估算占比 |
|------|------|---------|
| `/{lang}/features/{slug}` | 多语言功能着陆 | 高 |
| `/{lang}/blog/{slug}` | 多语言博客 | 高 |
| `/forum/t/{uuid}` | 社区帖子 | 中 |
| `/features/{slug}` | 英文功能页 | 中 |
| `/blog/{slug}` | 英文博客 | 低 |
| `/{lang}/` | 语言首页 | 低 |
| `/templates`、`/components` 及语言镜像 | 资源库 | 低 |

### 1.3 语言前缀（sitemap 观测）

`de` · `pt` · `es` · `fr` · `id` · `it` · `ja` · `ko` · `ru` · `ar` · `tr` · `zh` · `hi`（及默认无前缀英文）

### 1.4 Features slug 抽样（英文）

| slug | 类型 |
|------|------|
| ai-app-builder | 核心能力 |
| ai-website-builder | 核心能力 |
| ai-agent-builder | 核心能力 |
| visual-editor | 核心能力 |
| collaborative-coding | 核心能力 |
| website-template | 模板 |
| code-editor | 编辑器 |
| ai-for-developers | 角色 |
| ai-for-product-manager | 角色 |
| ai-for-small-businesses | 角色 |
| ai-startup | 角色 |
| saas-website-builder | 行业 |
| online-shop-builder | 行业 |
| ai-page-generator | 行业 |
| ai-coding-assistant | 行业 |
| ai-for-marketing / finance / health / education / hr / operations / productivity | 行业 |

### 1.5 Blog slug 抽样

| slug | 分类（导航） |
|------|-------------|
| enter-april-launch | Announcement |
| enter-cloud | Announcement |
| introducing-enter-skills | Announcement |
| enter-pro-multi-session | Changelog |
| enters-changelog | Changelog |
| web-development-best-practices | Guide |
| ai-vs-traditional-programming | Insight |
| adalo-app-builder | Guide（竞品向） |

### 1.6 Forum 说明

sitemap 含大量 `/forum/t/{uuid}` URL（lastmod 2026-04–06）。体量大但单帖 SEO 价值参差；**待验证** 是否与 noindex 策略并存。

---

## 2. 数据引用

| 数据项 | 数值/描述 | 来源 | 日期 |
|--------|----------|------|------|
| Sitemap URL 数 | ~3,870 | sitemap.xml 解析 | 2026-06-25 |
| 定价档 | Free / Basic / Pro-1 / Pro-2 / Ultimate | [converge.ai/pricing?product=enter](https://converge.ai/pricing?product=enter) | 2026-06-25 |
| 月 Credits | 一次性 / 1,500 / 4,000 / 8,200 / 21,000 | 同上 | 2026-06-25 |
| 免费额度 | Daily Free Credits（登录领取） | 首页 FAQ | 2026-06-25 |
| 代码所有权 | 100% 用户拥有，可导出 | 首页 FAQ | 2026-06-25 |
| 技术栈 | React + Tailwind | 首页 FAQ | 2026-06-25 |
| 运营主体 | Enter Pro by Converge AI（LinkedIn: EnterProAI） | 官网 + LinkedIn | 2026-06-25 |
| 流量 / DR | **待验证** Semrush | — | — |

---

## 3. 待验证项

| 项 | 说明 |
|----|------|
| 各档月费美元价 | pricing 页抓取未含具体 $ 数字（动态渲染 **待验证**） |
| Enter Desktop | 首页提及，**待验证** 独立下载页与 sitemap 收录 |
| MCP / Skills | 博客提及 Enter Skills、Cloud；**待验证** 与 CLI 产品边界 |
| Forum SEO | 大量 forum URL 进 sitemap 的索引策略 |
| hreflang | 多语言 canonical 一致性 |

---

*归档规则：sitemap 完整 URL 列表 >200 行，仅保留模式统计与抽样*
