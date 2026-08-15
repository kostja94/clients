# Erasa

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)

**Last updated**: 2026-03-20

---

## 文档体系（各文档职责与引用关系）

| 文档 | 职责 | 引用 |
|------|------|------|
| **erasa.md**（本文） | 产品概览、定位、ICP、关键词摘要、竞品摘要、网站结构 | 详细内容见各专项文档 |
| [erasa-features.md](./erasa-features.md) | 功能/解决方案页、工具、URL、链至 Use Cases | 关键词见 erasa-keywords；Use Cases 见 erasa-use-cases |
| [erasa-use-cases.md](./erasa-use-cases.md) | Persona 与情境、Use Case 页面内容 | 功能页内链见 erasa-features |
| [erasa-keywords.md](./erasa-keywords.md) | 关键词与目标页映射、待办、URL 模式 | 功能页 URL 见 erasa-features |
| [erasa-competitors.md](./erasa-competitors.md) | 竞品分析、差异化、Gaps | [erasa-features.md](./erasa-features.md) |
| [erasa-sitemap.md](./erasa-sitemap.md) | **Sitemap 索引与子文件、完整 URL 清单、多语言与 /compare 程序化页** | 基于 [sitemap.xml](https://www.erasa.net/sitemap.xml) |

**原则**：各文档负责各自领域；互相引用，不重复罗列。erasa.md 为入口，专项细节在对应文档。

*产品入口*：Web [erasa.net](https://www.erasa.net/) | 多语言路径见 [erasa-sitemap.md §3](./erasa-sitemap.md)（如 `/zh`、`/ja`、`/de` 等）

---

## 1. 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C / 数字内容保护 / DMCA 下架 / 创作者与个人反泄露 |
| 网站 | https://www.erasa.net/ |
| 当前阶段 | 成长期（宣称 10,000+ 用户、数百万案例处理） |
| 核心产品 | **Erasa**：盗用内容检测、冒充账号处理、DMCA 自动化下架、私人照片泄露扫描（AI 人脸识别）、OnlyFans/创作者专项保护 |
| Slogan | The All-In-One Platform To Protect Your Digital Presence |
| 价值主张 | 全网监测盗用与冒充，代表用户发起下架流程；强调自动化工作流与仪表盘追踪 |
| 目标市场 | **创作者**（OnlyFans、Cam、社媒变现）+ **个人**（私密照泄露、复仇式色情、AI 图像滥用） |
| 产品形态 | **SaaS 订阅** + 免费泄露扫描；付费含自动 DMCA、社媒下架、冒充处理等 |
| 更新日期 | 2026-03-20 |

---

## 2. 产品定位

### 产品摘要

**Erasa** 面向**内容创作者**与**普通个人**，提供「检测 → 自动/半自动下架 → 仪表盘追踪」的一站式数字形象保护。创作者侧侧重**盗用内容、冒充账号、DMCA 工作流**；个人侧侧重**私密照是否已出现在网上**（AI 人脸扫描）、**非自愿亲密图像（NCII）**相关移除与指引。站内同时提供**免费工具**（各平台 Shadowban 检测、OnlyFans 违禁词检测、标题生成器等）作为流量与教育入口。

### 产品定位

| 维度 | 说明 |
|------|------|
| **创作者** | 关键词与品牌监测、冒充识别与移除、DMCA 自动化、OnlyFans 等垂类场景 |
| **个人** | 上传照片扫描网络曝光、复仇式色情/勒索情境下的合规移除支持、AI 图像滥用检测 |
| **工具矩阵** | Shadowban（X / Instagram / TikTok）、创作者平台对比、OnlyFans 工具等，服务于拉新与长尾 SEO |
| **合规叙事** | 强调伦理与合法边界、版权与隐私尊重（官网表述） |

| Persona | 需求 | 痛点 |
|---------|------|------|
| **订阅制创作者** | 防盗链、防盗卖、冒充号 | 手动 DMCA 耗力、平台规则不一 |
| **Cam / 成人内容创作者** | 泄露站、论坛传播 | 扩散快、难穷举 |
| **社媒网红** | 冒充、盗图 | 举报流程分散 |
| **私密照泄露受害者** | 确认是否已传播、请求下架 | 恐慌、不知从何查起 |
| **被 AI 换脸/滥用者** | 发现滥用痕迹 | 技术门槛高 |

*详细 Persona 与场景*：见 [erasa-use-cases.md](./erasa-use-cases.md)

---

## 3. 目标受众 / ICP

- **OnlyFans / Fan 平台创作者**：内容被盗卖、泄露站列表焦虑
- **Cam 模特**：多平台身份、冒充与高仿账号
- **Instagram / TikTok / X 创作者**：Shadowban 与增长工具需求并存
- **非自愿影像当事人**：需合规指引与移除渠道（强调配合执法建议）
- **品牌或个人 IP 持有者**：持续监测与 DMCA

*Persona 详情与 Use Case 映射*：见 [erasa-use-cases.md](./erasa-use-cases.md)

---

## 4. 核心产品线

| 产品线 | 说明 |
|--------|------|
| **Content Protection（创作者）** | 监测盗用、保护收入与声誉 |
| **Impersonation Detection & Removal** | 冒充账号识别与下架 |
| **DMCA Takedown Service** | 自动化 DMCA 流程，批量/工作流 |
| **Private Photo Protection（个人）** | AI 人脸识别扫描是否出现在公开网络 |
| **Revenge Porn Removal** | 非自愿亲密内容相关移除（需符合法律与平台政策） |
| **AI Image Abuse Detection** | AI 生成/滥用图像相关检测与处置 |
| **Free Tools** | Shadowban 测试、OnlyFans 工具、反向搜索类等 |

### 工作流程（官网叙事）

1. **Detect**：AI 监测 + 多平台扫描（含 X、Instagram、Facebook、TikTok 等）
2. **Automated Takedowns**：代发 DMCA / 平台投诉，统一工作流
3. **Track**：仪表盘查看案件状态与报告

### 定价（公开信息摘要，以官网为准）

| 档位 | 要点（来自公开页面摘要，可能变更） |
|------|--------------------------------------|
| **免费试用/扫描** | 基础泄露扫描，了解风险 |
| **Starter** | 约 $79/月量级：多账号、日常扫描、自动 DMCA |
| **Advanced** | 约 $119/月量级：增强监测、社媒下架、冒充处理 |
| **Elite** | 约 $239/月量级：高阶/团队向 |

*下架成功率*：官网 FAQ 等处常见「约 97%」类表述；部分落地页写「约 95%」——**依平台与案件类型变化，非保证**。

### 市场洞察

- **创作者经济**：订阅与成人向平台增长带来盗版与泄露「产业化」
- **NCII 与 AI 滥用**：立法与平台政策演进，搜索与教育内容需求高
- **工具 + 服务**：纯工具（如反向人脸搜索）与「检测+代下架」组合易形成转化漏斗
- **信任与合规**：代理投诉是否使用公司名义、隐私与法律效力是用户决策关键

*功能与 URL 详情*：见 [erasa-features.md](./erasa-features.md)

---

## 5. 关键词摘要

| 类型 | 示例 |
|------|------|
| **Primary** | DMCA takedown service, remove leaked content, OnlyFans content protection, impersonation removal |
| **Secondary** | reverse image search leaked photos, revenge porn removal, AI deepfake detection, creator content monitoring |
| **Long-tail** | how to remove leaked OnlyFans content, Twitter shadowban test, OnlyFans restricted words |
| **平台/泄漏长尾** | Fansly DMCA, leaked content telegram, stolen Fansly videos（与 `/compare`、垂类落地页协同） |
| **个人 YMYL** | NCII removal, StopNCII, Take It Down（教育/外链与付费服务边界清晰） |
| **品牌** | Erasa, Erasa DMCA |

*完整映射*：见 [erasa-keywords.md](./erasa-keywords.md)  
*搜索意图与场景承接*：见 [erasa-use-cases.md](./erasa-use-cases.md)

---

## 6. 竞品摘要

- **直接竞品**：RemoveYourMedia、**Rulta**、**Ceartas**、**BranditScan**、Takedowns.ai / LeakRemover / Content Shield 等创作者向代理、DMCA.com 类通用服务
- **间接竞品**：BrandShield、Red Points（偏品牌大客户）、**FaceCheck.ID**、PimEyes/FaceSeek 类（偏发现）；**StopNCII.org**、**NCMEC Take It Down**（偏免费官方哈希移除，与商业服务互补）
- **冒充垂类**：Impersonation Takedown、Unphish、ContentRemoval.ai 等（社媒假号专项）
- **差异化**：Erasa 强调 **创作者 + 个人双产品线**、**自动化 DMCA 工作流**、**仪表盘追踪**、**免费扫描降低门槛** + **工具矩阵引流**

*详细拆解*：见 [erasa-competitors.md](./erasa-competitors.md)

---

## 7. 网站结构（与 [sitemap.xml](https://www.erasa.net/sitemap.xml) 对齐）

**Sitemap 索引**：`sitemap-0.xml`（核心页）+ `server-sitemap.xml?type=article&page=*`（文章分页）+ `compare-server-sitemap.xml`（对比页集群）。**全量 URL、lastmod、多语言列表**见 [erasa-sitemap.md](./erasa-sitemap.md)。

| 路径 | 说明 |
|------|------|
| / | 首页 |
| /plan、/guide | 方案、DMCA 指南 |
| /dmca-takedown、/dmca-takedown-service | DMCA 相关落地（两页均在 sitemap） |
| /content-monitoring、/content-monitoring/reverse-* | 内容监测 + 反向用户名/人脸/视频/图片搜索 |
| /cam-model-protection、/remove-leaked-onlyfans-content、/remove-fake-account | 创作者/冒充/OF 泄露 |
| /leaked-private-photos、/find-and-remove-revenge-porn、/ai-porn-detection-removal | 个人向敏感场景 |
| /onlyfans-caption-generator、/onlyfans-restricted-words-checker | OF 工具 |
| /shadowban-test、/shadowban-test/*-shadowban-test | Shadowban 总览 + X/IG/TikTok 子页 |
| /compare、/compare/* | **创作者平台对比/替代方案**（程序化 SEO，量大，见 compare-server-sitemap） |
| /dmca-protection-badge | DMCA 徽章 |
| /blog、/blog/* | 博客；更多文章见 server-sitemap |
| /privacy-policy、/terms-us、/cookie-policy | 合规页 |
| /zh、/ja、/de、/es、/pt、/it、/ko、/tw 等 | 多语言镜像（与上列路径组合） |

**转化路径**：免费扫描 / 连接账号 → 付费监测与下架 → 仪表盘留存。

---

## 8. 内容营销

- **已有**：Blog、`/guide`、工具页（Shadowban、OF、反向搜索）、**大规模 `/compare/*` 程序化页**（OnlyFans vs Fansly、各平台 alternatives 等，见 [erasa-sitemap.md §4](./erasa-sitemap.md)）
- **可加强**：在对比页与工具页向 `/plan`、核心服务页加强内链；YMYL 页配权威外链
- **服务向竞品页**（可选）：Erasa vs Rulta 等 — 与现有「平台对比」矩阵不同，需单独策划
- **GEO**：AI 搜索中「best DMCA service for creators」「how to remove leaked photos」类答案可见性

### 页面落地顺序（建议）

| 阶段 | 页面 | 理由 |
|------|------|------|
| **P1** | 强化 /dmca-takedown、/plan、核心工具页 Title/H1 | 商业词与工具词并重 |
| **P2** | /for/creators、/for/individuals（或按现有 Solutions 扩展） | 意图清晰分流 |
| **P3** | 优化已有 `/compare/*` 内链与模板差异化 | 程序化页已上线；避免薄内容与重复 |
| **P4** | 博客集群：OnlyFans leak、DMCA 流程、NCII 资源 | 长尾与信任 |

---

## 9. 优化建议

- 统一「成功率」表述与免责声明，避免与竞品绝对化承诺冲突
- 工具页与付费页之间加强内链（工具 → 扫描 → 方案）
- YMYL 场景页需配权威外链（执法、危机热线）与法律免责声明

---

## 10. 文档导航

| 文档 | 用途 |
|------|------|
| [erasa-features.md](./erasa-features.md) | 功能、工具、URL、内链规划 |
| [erasa-use-cases.md](./erasa-use-cases.md) | Use Cases、Persona + 情境 |
| [erasa-keywords.md](./erasa-keywords.md) | 关键词映射、待办 |
| [erasa-competitors.md](./erasa-competitors.md) | 竞品分析、差异化 |
| [erasa-sitemap.md](./erasa-sitemap.md) | Sitemap 结构、URL 全量参考 |

---

*文档生成日期：2026-03-20 | 多轮优化：2026-03-20 | 来源：[erasa.net](https://www.erasa.net/)、[sitemap.xml](https://www.erasa.net/sitemap.xml)、公开网页检索摘要*
