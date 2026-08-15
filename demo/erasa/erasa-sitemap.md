# Erasa Sitemap 结构说明

> 数据来源：[https://www.erasa.net/sitemap.xml](https://www.erasa.net/sitemap.xml)（sitemap 索引 + 子文件）  
> **抓取日期**：2026-03-20（`lastmod` 以站点返回为准）

---

## 1. Sitemap 索引（sitemapindex）

| 子 Sitemap | 说明 |
|------------|------|
| [sitemap-0.xml](https://www.erasa.net/sitemap-0.xml) | 核心静态页、多语言镜像、博客部分条目、工具子路径 |
| [server-sitemap.xml?type=article&page=1](https://www.erasa.net/server-sitemap.xml?type=article&page=1) | 文章类型动态分页（新文章会增减页码） |
| [compare-server-sitemap.xml](https://www.erasa.net/compare-server-sitemap.xml) | 程序化对比页（`/compare/*`） |

---

## 2. 英文根域主要 URL（sitemap-0 摘录）

### 2.1 首页与转化

| URL | 备注 |
|-----|------|
| https://www.erasa.net/ | 首页，`priority` 1 |
| https://www.erasa.net/plan | 方案 |
| https://www.erasa.net/guide | DMCA 指南 |

### 2.2 解决方案 / 落地页

| URL | 备注 |
|-----|------|
| https://www.erasa.net/cam-model-protection | Cam 模特保护 |
| https://www.erasa.net/content-monitoring | 内容监测（含子工具，见下） |
| https://www.erasa.net/dmca-takedown | DMCA 下架 |
| https://www.erasa.net/dmca-takedown-service | DMCA 服务（与上可能内容互补，注意 canonical） |
| https://www.erasa.net/remove-fake-account | 移除假账号 |
| https://www.erasa.net/remove-leaked-onlyfans-content | OF 泄露内容移除 |
| https://www.erasa.net/leaked-private-photos | 私密照泄露 |
| https://www.erasa.net/find-and-remove-revenge-porn | 复仇式色情相关移除 |
| https://www.erasa.net/ai-porn-detection-removal | AI 色情检测与移除 |

### 2.3 内容监测子工具（挂在 content-monitoring 下）

| URL |
|-----|
| https://www.erasa.net/content-monitoring/reverse-username-search |
| https://www.erasa.net/content-monitoring/reverse-face-search |
| https://www.erasa.net/content-monitoring/reverse-video-search |
| https://www.erasa.net/content-monitoring/reverse-photo-search |

### 2.4 OnlyFans 工具

| URL |
|-----|
| https://www.erasa.net/onlyfans-caption-generator |
| https://www.erasa.net/onlyfans-restricted-words-checker |

### 2.5 Shadowban（分平台子页）

| URL |
|-----|
| https://www.erasa.net/shadowban-test |
| https://www.erasa.net/shadowban-test/twitter-shadowban-test |
| https://www.erasa.net/shadowban-test/instagram-shadowban-test |
| https://www.erasa.net/shadowban-test/tiktok-shadowban-test |

### 2.6 对比与信任

| URL | 备注 |
|-----|------|
| https://www.erasa.net/compare | 对比入口；**完整列表见 compare-server-sitemap** |
| https://www.erasa.net/dmca-protection-badge | DMCA 徽章页 |

### 2.7 博客（sitemap-0 中出现的条目示例）

| URL |
|-----|
| https://www.erasa.net/blog |
| https://www.erasa.net/blog/onlyfans-statistics-report-2026 |
| https://www.erasa.net/blog/spot-catfishing-dating |
| https://www.erasa.net/blog/duplicate-photo-finder-online |
| https://www.erasa.net/blog/find-people-name-by-photo |
| https://www.erasa.net/blog/how-to-check-if-a-video-is-copyrighted |
| https://www.erasa.net/blog/image-search-techniques |
| https://www.erasa.net/blog/tineye-alternatives |
| https://www.erasa.net/blog/pineyes-face-search-alternative |
| https://www.erasa.net/blog/check-private-photo-leaks |
| https://www.erasa.net/blog/pimeyes-alternatives |

*更多文章以 `server-sitemap.xml?type=article&page=*` 为准。*

### 2.8 法律与系统类（sitemap 中含部分非 HTML 资源 URL，审计时注意）

| URL | 说明 |
|-----|------|
| https://www.erasa.net/privacy-policy | 隐私 |
| https://www.erasa.net/terms-us | 条款（路径为 `terms-us`） |
| https://www.erasa.net/cookie-policy | Cookie |
| https://www.erasa.net/server-sitemap.xml | 索引中列出，通常为机器可读 |
| https://www.erasa.net/compare-server-sitemap.xml | 同上 |

---

## 3. 多语言前缀

以下路径在 **zh / tw / pt / ja / ko / es / de / it** 下有镜像（示例：`https://www.erasa.net/zh/plan`）：

- 首页、login、blog  
- 与各解决方案页：`ai-porn-detection-removal`、`cam-model-protection`、`compare`、`content-monitoring`、`cookie-policy`、`dmca-protection-badge`、`dmca-takedown`、`dmca-takedown-service`、`find-and-remove-revenge-porn`、`leaked-private-photos`、`onlyfans-caption-generator`、`onlyfans-restricted-words-checker`、`plan`、`privacy-policy`、`remove-fake-account`、`remove-leaked-onlyfans-content`、`shadowban-test`、`terms-us`  

*Shadowban 分平台子路径在 sitemap-0 中主要为英文；多语言以实际站点为准。*

---

## 4. 程序化对比页（compare-server-sitemap.xml）

**模式**：`/compare/{platform}-alternatives`、`/compare/{a}-vs-{b}`

**涉及平台名示例**（来自 sitemap）：OnlyFans、Fansly、Patreon、manyVids、fanvue、fanCentro、ko-fi、mym、fansone、umate、fanspicy、brandArmy、loyalfans、pornhub、fantia 等。

**示例 URL**：

- https://www.erasa.net/compare/onlyfans-vs-fansly  
- https://www.erasa.net/compare/onlyfans-alternatives  
- https://www.erasa.net/compare/fansly-vs-patreon  
- …（全量见 [compare-server-sitemap.xml](https://www.erasa.net/compare-server-sitemap.xml)）

**SEO 备注**：大规模对比页利于长尾与程序化 SEO；需关注 **重复模板、内部链接深度、canonical/hreflang** 与核心转化页（`/plan`、监测服务）的内链。

---

## 5. 文档导航

| 文档 | 职责 |
|------|------|
| [erasa.md](./erasa.md) | 产品概览；网站结构摘要 |
| [erasa-features.md](./erasa-features.md) | 功能与 URL 对照 |
| [erasa-keywords.md](./erasa-keywords.md) | 关键词与 URL 映射 |
| [erasa-use-cases.md](./erasa-use-cases.md) | Use Cases 与 Persona |
| [erasa-competitors.md](./erasa-competitors.md) | 竞品分析 |

---

*本文档随站点改版需重新抓取 sitemap 核对。*
