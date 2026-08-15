
# Intent — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./intent.md) | [features](./intent-features.md) | [keywords](./intent-keywords.md) | [competitors](./intent-competitors.md) | [use-cases](./intent-use-cases.md) | [growth-strategy](./intent-growth-strategy.md)

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（产品展示 + Download CTA） | real-time translation app, cross language communication | P0 |
| `/tools` | 工具集页 | AI image translator, document translation, video subtitle generator | P0 |
| `/blog` | 博客首页 | translation blog, cross language tips | P1 |
| `/blog/{slug}` | 单篇博文 | 长尾关键词（如 "translate voice messages automatically"） | P1 |
| `/faq` | FAQ 页（含详细使用教程） | Intent app guide, how to use translation app | P1 |
| `/privacy` | 隐私政策 | — | P3 |
| `/terms` | 服务条款 | — | P3 |
| [App Store] `apps.apple.com/.../id6752899958` | iOS 下载页 | Intent app iOS, translation app | P0 |
| [Google Play] `play.google.com/.../app.intent.android` | Android 下载页 | Intent app Android, translation app APK | P0 |

---

## 2. URL 层级

```
intent.app/
├── /                          # 首页："Don't just translate, Meet at Intent."
│   ├── Real-Time Translation 区块
│   ├── Voice Cloning 区块
│   ├── Face to Face 区块
│   ├── AI Agent 区块
│   ├── Tools 展示
│   ├── Reviews 展示
│   └── Download CTA（iOS / Android / APK）
├── /tools                     # 工具集页（AI Image Translator + 6 工具卡片）
├── /blog                      # 博客首页（6 篇文章）
│   ├── /blog/{slug}           # 单篇博文
│   └── /blog/{locale}/{slug}  # 本地化博文（如 /blog/en-US/...）
├── /faq                       # FAQ（含详细用户指南和截图教程）
├── /privacy                   # 隐私政策
└── /terms                     # 服务条款（推测路径）

外部入口：
├── App Store 页面
├── Google Play 页面
└── APK 直接下载链接
```

> **注意**：intent.app 是 App 导向的单页式落地站。无 `/pricing`（免费）、`/about`、`/features`（功能内嵌首页）、`/login` 等传统页面。产品即 App。sitemap.xml 返回 500 错误。

---

## 3. 技术架构

| 维度 | 内容 | 识别方式 |
|------|------|---------|
| 产品形态 | iOS + Android 原生 App | App Store + Google Play |
| App 大小 | iOS 175.4 MB，Android ⚠️ 待验证 | App Store |
| 最低系统 | iOS 16.0+，Android ⚠️ 待验证 | App Store |
| 翻译引擎 | AI 实时翻译（231 语言文字、39 语言语音），底层模型未披露 | 官网 + App 描述 |
| 语音克隆 | 10 秒样本 → 多语言语音合成，保留音色/语调/情感 | 官网 + FAQ |
| 网站技术栈 | 未确认（疑似 Next.js/SSG 静态网站） | 推测 |
| 实时通信 | 内置聊天系统（类似 WhatsApp/微信），消息经服务器中转 | FAQ（无端到端加密声明） |
| 订阅服务 | 当前免费，高级功能后续可能收费 | FAQ |

---

## 4. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| robots.txt 声明 | `sitemap.xml` | 返回 500 | 不可用 |
| 首页 | `/`, `/tools`, `/blog`, `/faq` | 4 页 | 2026-07 |
| 博客列表 | `/blog/{slug}` | 6 篇 | 2026-05 ~ 2026-07 |
| App Store | `apps.apple.com/.../id6752899958` | 1 页 | 2026-06-30 |
| Google Play | `play.google.com/.../app.intent.android` | 1 页 | 2026-06-29 |

> sitemap.xml 返回 HTTP 500 错误。当前站点页面极少，核心流量依赖 App Store 搜索和社交媒体广告。

---

## 5. robots.txt 要点

- **Allow**: `/`（全站开放）
- **Disallow**: 无
- **AI Crawler 策略**: 未特别声明
- **Sitemap**: 声明 `https://intent.app/sitemap.xml`（返回 500）

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 | Download CTA（iOS/Android/APK）、功能区块锚点、Reviews、Tools 卡片 | App 下载转化 |
| /tools | AI Image Translator 工具 + 6 个工具卡片（指向 App 内功能） | 功能认知 → App 下载 |
| /blog | 6 篇文章卡片 | SEO 内容引流 |
| /faq | 详细使用指南（含截图）、客服邮箱 | 自助支持，降低客服压力 |
| 页脚 | Contact Us, Brand Materials, FAQ, Terms, Privacy | 合规、品牌资源 |

---

## 7. 多语言

| 维度 | 内容 |
|------|------|
| 主语言 | 英语（首页）+ 博文有多语言版本（如 `/blog/en-US/...`） |
| 产品内 | App 内支持 231 种语言实时翻译 |
| App Store 本地化 | 英文 + 12 种语言 |
| hreflang | ⚠️ 待验证 |

---

## 8. URL 分阶段规划

| 阶段 | 建议新增页面 | 对标关键词优先级 |
|------|-------------|----------------|
| 短期 | `/about` 公司/团队页面 | P1 |
| 短期 | `/languages` 支持语言全列表 | P1 |
| 短期 | 博客扩展至 15+ 篇 | P0 |
| 中期 | `/use-cases` 场景页（跨国情侣/留学生/商务/旅行） | P0 |
| 中期 | `/compare/intent-vs-google-translate` 等对比页 | P0 |
| 长期 | `/pricing`（若推出付费版） | P0 |

---

*Last updated: 2026-07-16*
*来源：robots.txt 读取、网站抓取、App Store、Google Play、LinkedIn、第三方评测*
