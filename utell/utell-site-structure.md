# Utell 网站结构与 URL（utell.ai）

> **站点根**：https://utell.ai/  
> **关联**：[utell.md](./utell.md) | [utell-growth-strategy.md](./utell-growth-strategy.md) | [utell-features.md](./utell-features.md)（功能卖点，**非** URL 权威） | [utell-use-cases.md](./utell-use-cases.md) | [utell-keywords.md](./utell-keywords.md) | [utell-platforms.md](./utell-platforms.md)  
> **Skills 对齐**：**website-structure**、**sitemap**、**internal-links**。

**用途**：描述 **线上 URL、双栈结构（主站 SPA / WordPress 子路径）、内链树与 robots**，供 SEO、内链与文档对齐。**站点改版后请更新本文**。

**信息来源**：[robots.txt](https://utell.ai/robots.txt)、对路径的 **HTTP HEAD 抽样**（**2026-04-07**）、站点导航 HTML 片段；`/sitemap.xml` 当前返回 **非 XML**（SPA 壳层），sitemap 以 **Search Console / 后续上线** 为准。

---

## 〇、总则：双栈与同域路径

| 栈 | 基路径 | 说明 |
|----|--------|------|
| **主站（营销 SPA）** | `https://utell.ai/` | 功能页、多数 Use Case 落地、下载、登录、法律页等；**无** `/en` 类语言前缀（抽样 `/zh` → 404）。 |
| **博客** | `https://utell.ai/blog/` | 外链或同域子路径；对比文、教程等。 |
| **Use Case 长文（WordPress）** | `https://utell.ai/use-case/…` | 子站点式路径；例：`/use-case/real-time-whatsapp-translator/`（**200**；无尾斜杠可能 **301**）。 |

**URL 习惯**：路径多为 **kebab-case**；首页区块锚点 **`#features`**、**`#faq`**、**`#first`**（Footer / 首屏）。

---

## 〇.1 树状层级（概览）

```
utell.ai/                          ← 主站 SPA
├── /（首页，含 #features #faq）
├── /download、/login
├── Features（产品线）
│   ├── /accent-conversion
│   ├── /noice-cancellation       ← 线上 slug（*noise* 拼写见 §3 注）
│   ├── /sound-quality
│   ├── /live-translator
│   ├── /meeting-assistant
│   ├── /accent-oracle
│   └── /audio-translator
├── Use Cases（主站路径，与顶栏部分重叠）
│   ├── /education、/sales、/travels、/game-streaming
│   ├── /call-center、/online-meeting
│   ├── /meeting-education、/meeting-business   ← 顶栏「Use Cases」显性入口
│   └── /ai-short-drama                         ← 当前 404，待建（规格见 utell-features §四）
├── 法律：/privacy-policy、/terms-of-use
├── 博客：/blog/*
└── WordPress：/use-case/{slug}/…

外链（站外）：Request Demo（YouForm）、Discord、YouTube 等 — 见线上 Footer。
```

---

## 一、功能页（Features）— 路径与校验

| 路径 | HTTP（2026-04-07 抽样） | 说明 |
|------|-------------------------|------|
| `/accent-conversion` | 200 | Real-time Accent Conversion |
| `/noice-cancellation` | 200 | Noise Cancellation；**slug 为 noice** |
| `/sound-quality` | 200 | Improve Sound Quality |
| `/live-translator` | 200 | Live Translator |
| `/meeting-assistant` | 200 | Meeting Assistant |
| `/accent-oracle` | 200 | Accent Oracle |
| `/audio-translator` | 200 | Audio Translator |
| `/noise-cancellation` | 404 | **非**当前线上路径；勿写进内链 |

**关键词与 Title 分配**：见 [utell-keywords.md](./utell-keywords.md) **§4**；卖点文案见 [utell-features.md](./utell-features.md)。

---

## 二、Use Case 页（主站 SPA）

### 2.1 与顶栏一致的入口（导航抽样）

| 路径 | HTTP | 顶栏/页脚文案（意译） |
|------|------|------------------------|
| `/meeting-education` | 200 | Meeting (Education) |
| `/meeting-business` | 200 | Meeting (Business) |
| `/call-center` | 200 | Call Center |
| `/sales` | 200 | Sales |

### 2.2 营销文档常用路径（与 [utell-use-cases.md](./utell-use-cases.md) 对照）

| 路径 | HTTP | 备注 |
|------|------|------|
| `/education` | 200 | 与 `meeting-education` 并存；内链统一口径需业务选定 |
| `/travels` | 200 | Travels and Business Trips |
| `/game-streaming` | 200 | Games and Streaming |
| `/online-meeting` | 200 | Online Meeting |
| `/ai-short-drama` | **404** | **待建**；落地规格见 [utell-features.md](./utell-features.md) **§四** |

**Persona 叙事**：见 [utell-use-cases.md](./utell-use-cases.md)；**目标词**见 [utell-keywords.md](./utell-keywords.md) **§4.3**。

---

## 三、其他主站路径

| 路径 | HTTP | 角色 |
|------|------|------|
| `/` | 200 | 首页 |
| `/download` | 200 | 下载客户端 |
| `/login` | 200 | 登录 |
| `/privacy-policy` | 200 | 隐私政策 |
| `/terms-of-use` | 200 | 使用条款 |

---

## 四、内链树（权威）

以下为主站 **SPA 内链**推荐结构；博客文章与 `/use-case/` 长文应回链至对应功能页。

```
首页 (/)
  ├── /accent-conversion
  ├── /noice-cancellation
  ├── /sound-quality
  ├── /live-translator
  ├── /meeting-assistant
  ├── /accent-oracle
  ├── /audio-translator
  ├── Use Cases
  │   ├── /education
  │   ├── /sales
  │   ├── /travels
  │   ├── /game-streaming
  │   ├── /call-center
  │   ├── /online-meeting
  │   ├── /meeting-education
  │   ├── /meeting-business
  │   └── /ai-short-drama（待上线）
  ├── /download、/login
  ├── /privacy-policy、/terms-of-use
  └── 外链：/blog/、/use-case/…、Request Demo、Discord…
```

*勿在 [utell-use-cases.md](./utell-use-cases.md) 再维护一份同构树。*

---

## 五、robots.txt 与 sitemap

### 5.1 robots.txt（摘录，以线上为准）

```
User-Agent: *
Disallow:
```

当前为 **Allow 全站**；无 `Sitemap:` 行（**2026-04-07**）。

### 5.2 sitemap

访问 `https://utell.ai/sitemap.xml` 当前返回 **HTML 应用壳**（非标准 `urlset`）。**是否另有 sitemap 路径、或待接入**，以 GSC / 工程配置为准；接入后在本节补充 URL。

---

## 六、与集成平台文档的关系

第三方 App（Zoom、Meet、Teams 等）**不是** `utell.ai` 站内路径；列表与官网 CTA 文案见 [utell-platforms.md](./utell-platforms.md)。站内落地页通过 Features / Use Cases 内链承接。

---

## 七、维护清单

- [ ] 站点新增/重定向路径后，更新 **§一～§三** 与 **§四** 内链树。  
- [ ] `/ai-short-drama` 上线后改 **§2.2** HTTP 状态并去掉「待建」标注。  
- [ ] 若统一 `/education` vs `/meeting-education`，更新内链与 [utell-use-cases.md](./utell-use-cases.md) **§一**。  
- [ ] sitemap 可用后，在本文件 **§5.2** 记录索引 URL 与抓取注意点。  

**Last updated**: 2026-05-11 — 补互链 utell-growth-strategy；更新时效。
