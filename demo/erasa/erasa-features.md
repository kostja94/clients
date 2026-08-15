# Erasa Features 功能与页面总结

> 关联：[erasa.md](./erasa.md) | [erasa-sitemap.md](./erasa-sitemap.md) | [erasa-keywords.md](./erasa-keywords.md) | [erasa-use-cases.md](./erasa-use-cases.md) | [erasa-competitors.md](./erasa-competitors.md)  
> **URL 以 [sitemap-0.xml](https://www.erasa.net/sitemap-0.xml) 为准**（2026-03-20 抓取）

**Features 与 Use Cases 区分**：Features 回答「产品**能做什么**」；Use Cases 回答「**谁**在**什么情境**下用」。

---

## 一、解决方案与落地页 URL（英文根路径）

| 产品线 | URL | 目标关键词（示例） |
|--------|-----|-------------------|
| Cam 模特保护 | [/cam-model-protection](https://www.erasa.net/cam-model-protection) | cam model content protection |
| 内容监测（总览） | [/content-monitoring](https://www.erasa.net/content-monitoring) | content monitoring, brand monitoring |
| DMCA 下架 | [/dmca-takedown](https://www.erasa.net/dmca-takedown) | DMCA takedown |
| DMCA 服务 | [/dmca-takedown-service](https://www.erasa.net/dmca-takedown-service) | DMCA takedown service |
| 移除假账号 | [/remove-fake-account](https://www.erasa.net/remove-fake-account) | remove fake account, impersonation |
| 移除泄露 OF 内容 | [/remove-leaked-onlyfans-content](https://www.erasa.net/remove-leaked-onlyfans-content) | remove leaked OnlyFans |
| 私密照泄露 | [/leaked-private-photos](https://www.erasa.net/leaked-private-photos) | leaked private photos |
| 复仇式色情相关 | [/find-and-remove-revenge-porn](https://www.erasa.net/find-and-remove-revenge-porn) | revenge porn removal（YMYL） |
| AI 色情检测与移除 | [/ai-porn-detection-removal](https://www.erasa.net/ai-porn-detection-removal) | AI porn detection |
| 方案 | [/plan](https://www.erasa.net/plan) | pricing, plans |
| 指南 | [/guide](https://www.erasa.net/guide) | DMCA guide |
| DMCA 徽章 | [/dmca-protection-badge](https://www.erasa.net/dmca-protection-badge) | DMCA badge |

*多语言：上述路径可加前缀 `/zh`、`/tw`、`/pt`、`/ja`、`/ko`、`/es`、`/de`、`/it` — 详见 [erasa-sitemap.md §3](./erasa-sitemap.md)。*

### 1.1 解决方案页 × 检索词簇（循环优化第二轮）

| URL | 除表中示例外可覆盖的检索簇 |
|-----|---------------------------|
| /remove-leaked-onlyfans-content | fansly leak, stolen onlyfans pack, telegram leaked content（高敏感，合规审核） |
| /cam-model-protection | chaturbate piracy, cam recording leak, stream rip dmca |
| /content-monitoring | bulk infringing links, monitor stolen videos |
| /remove-fake-account | catfish using my photos, fake creator account |
| /find-and-remove-revenge-porn | StopNCII, NCII hash（页内教育+外链） |
| /ai-porn-detection-removal | synthetic intimate media, AI nude fake |
| /leaked-private-photos | where is my photo posted, face match leak check |

---

## 二、内容监测子工具（反向搜索）

| URL |
|-----|
| [/content-monitoring/reverse-username-search](https://www.erasa.net/content-monitoring/reverse-username-search) |
| [/content-monitoring/reverse-face-search](https://www.erasa.net/content-monitoring/reverse-face-search) |
| [/content-monitoring/reverse-video-search](https://www.erasa.net/content-monitoring/reverse-video-search) |
| [/content-monitoring/reverse-photo-search](https://www.erasa.net/content-monitoring/reverse-photo-search) |

---

## 三、OnlyFans 工具

| URL |
|-----|
| [/onlyfans-caption-generator](https://www.erasa.net/onlyfans-caption-generator) |
| [/onlyfans-restricted-words-checker](https://www.erasa.net/onlyfans-restricted-words-checker) |

---

## 四、Shadowban

| URL |
|-----|
| [/shadowban-test](https://www.erasa.net/shadowban-test) |
| [/shadowban-test/twitter-shadowban-test](https://www.erasa.net/shadowban-test/twitter-shadowban-test) |
| [/shadowban-test/instagram-shadowban-test](https://www.erasa.net/shadowban-test/instagram-shadowban-test) |
| [/shadowban-test/tiktok-shadowban-test](https://www.erasa.net/shadowban-test/tiktok-shadowban-test) |

---

## 五、程序化对比页（/compare）

- **入口**：[/compare](https://www.erasa.net/compare)
- **子页**：仅 Fans / Fansly / Patreon / manyVids 等与彼此 **alternatives**、**a-vs-b** 组合，**全量列表**见 [compare-server-sitemap.xml](https://www.erasa.net/compare-server-sitemap.xml)
- **文档说明**：[erasa-sitemap.md §4](./erasa-sitemap.md)
- **内链**：对比页集群 → 核心服务与方案（`/plan`、DMCA、泄露/监测落地页）；关键词与意图见 [erasa-keywords.md](./erasa-keywords.md)

---

## 六、博客与文章 sitemap

- 索引页：[/blog](https://www.erasa.net/blog)
- sitemap-0 中部分文章：`/blog/pimeyes-alternatives`、`/blog/tineye-alternatives`、`/blog/check-private-photo-leaks` 等
- **完整文章 URL**：`server-sitemap.xml?type=article&page=1`（及后续 page）

---

## 七、法律与其他

| URL |
|-----|
| [/privacy-policy](https://www.erasa.net/privacy-policy) |
| [/terms-us](https://www.erasa.net/terms-us) |
| [/cookie-policy](https://www.erasa.net/cookie-policy) |

---

## 八、内链规划（建议）

```
首页 (/)
  ├── /plan, /guide
  ├── 解决方案（上表各路径）
  ├── /content-monitoring → reverse-* 四页
  ├── /shadowban-test → 三平台子页
  ├── /onlyfans-*
  ├── /compare → 高价值对比页 → /plan
  ├── /blog/*
  └── Use Cases 文档中的 /for/*（若后续建站）
```

---

## 九、文档导航

| 文档 | 职责 |
|------|------|
| [erasa.md](./erasa.md) | 产品概览、定位、ICP |
| [erasa-sitemap.md](./erasa-sitemap.md) | Sitemap 索引、URL 全量 |
| [erasa-use-cases.md](./erasa-use-cases.md) | Use Cases、Persona + 情境 |
| [erasa-keywords.md](./erasa-keywords.md) | 关键词映射 |
| [erasa-competitors.md](./erasa-competitors.md) | 竞品分析 |

---

*文档生成日期：2026-03-20 | 多轮优化：2026-03-20 | URL 来源：[sitemap.xml](https://www.erasa.net/sitemap.xml)*
