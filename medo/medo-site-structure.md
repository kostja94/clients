# MeDo 网站结构

> **本文档职责**：URL、导航、阶段规划；来源 [medo.dev](https://medo.dev/)（2026-06-04）。  
> **引用**：[medo.md](./medo.md) | [medo-keywords.md](./medo-keywords.md)

**Last updated**: 2026-06-04 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [medo.md](./medo.md) |
| 关键词 | [medo-keywords.md](./medo-keywords.md) |
| 增长策略 | [medo-growth-strategy.md](./archive/medo-growth-strategy.md) |
| 结构化数据 | [medo-schema-spec.md](./archive/medo-schema-spec.md) |

---

## 一、当前线上 IA

### 首页核心模块

| 模块 | 说明 |
|------|------|
| **分类 Tab** | Recommended、Education、Website、Marketing、Productivity、E-commerce、Tool、Game、Survey、Others |
| **运营 Banner** | Hackathon（$50,000）；Affiliate（30% commission） |
| **应用网格** | UGC 卡片：标题、描述、缩略；部分含 *Generate APP* / PRD 跳过流程 |
| **分页** | Page 1 … Next（站内标注 **17317 apps in total**） |

### 推断的用户路径（产品内，**待验证** URL）

| 路径 | 说明 |
|------|------|
| 创建入口 | 从首页或 Banner 进入 Chat / Editor |
| 应用详情 | 点击广场卡片 → 预览/打开他人 App |
| 发布页 | Publish 后生成 public URL |
| Hackathon | Banner 链出活动页 |
| Affiliate | Banner 链出联盟落地页 |

### 外部触点

| 触点 | URL |
|------|-----|
| 官方文档 | https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en |
| Quickstart | https://intl.cloud.baidu.com/en/doc/MIAODA/s/quick-start-en（**待验证**） |
| 联系/招聘 | Admin@medo.dev（About 文档） |
| 社区评测 | Product Hunt、DEV、YouTube |

---

## 二、核心路径表（≥5）

| 路径 | 用户目标 | 现状 |
|------|----------|------|
| 发现 | 看别人做了什么 → 获得灵感 | 广场 + 分类 ✓ |
| 创建 | 描述想法 → 预览 | 对话/PRD 流 ✓ |
| 迭代 | 改 UI/逻辑 | 对话 + 截图标注 ✓ |
| 变现 | 接 Stripe | 插件 ✓（文档/教程） |
| 发布 | 分享链接 | Publish ✓ |
| 裂变 | 参赛/推广赚钱 | Hackathon + Affiliate Banner ✓ |
| 学习 | 上手教程 | 外链 Baidu 文档 ✓ |

---

## 三、首页内容架构（信息层次）

1. **顶部分类**：意图分流（教育/游戏/电商等）  
2. **运营位**：Hackathon、Affiliate（转化与裂变）  
3. **UGC 瀑布流**：社会证明 + SEO 长尾（每个 App 标题即长尾词）  
4. **分页**：深度浏览与收录（**待验证** 各 App 是否独立 canonical URL）  

---

## 四、技术/SEO 观察（**待验证**）

| 项 | 说明 |
|----|------|
| SSR/CSR | 广场可能 CSR 为主，分类页需可抓取 HTML |
| 结构化数据 | 见 [medo-schema-spec.md](./archive/medo-schema-spec.md) — SoftwareApplication / ItemList / FAQPage |
| 国际化 | 广场含多语言 UGC；官网 UI 语言 **待验证** |
| llms.txt | **待验证** 是否存在官方 AI 索引文件 |

---

## 五、分阶段建议（SEO 增量）

### Phase 1 — 已有，优化内链

- 分类 Tab 改为可索引 URL（query → path）  
- 每个 App 详情页：标题 H1、描述 meta、链回「用 MeDo 创建同类」CTA  
- Hackathon / Affiliate 页脚全局链接  

### Phase 2 — 建议新建

| 路径 | 目的 |
|------|------|
| `/pricing` | 商业意图、credits FAQ |
| `/templates/{category}` | 对齐 9 类分类词 |
| `/vs/lovable` | 对比转化 |
| `/vs/bolt` | 对比转化 |
| `/showcase` | 精选案例（编策展广场） |
| `/developers` | 链文档、插件、Quickstart |
| `/affiliate` | 联盟 SEO（若 Banner 仅为相对路径） |
| `/hackathon` | 活动长尾与外链建设 |

### Phase 3 — 内容与程序化

| 路径 | 目的 |
|------|------|
| `/learn/{topic}` | full stack vs UI、Supabase 集成教程 |
| `/blog/{slug}` | PH 故事、客户案例 |
| `/compare` | 多竞品矩阵页 |

---

## 六、导航建议（营销站增强）

| 标签 | 路径 |
|------|------|
| Product | /#features 或 /product |
| Templates | /templates |
| Showcase | /showcase |
| Pricing | /pricing |
| Docs | 外链 MIAODA |
| Hackathon | /hackathon |
| Affiliate | /affiliate |
| Sign in | 应用后台（**待验证**） |

---

*Phase 2 与 [medo-growth-strategy.md](./archive/medo-growth-strategy.md) 战役对齐*
