# Oginify Product & Competitors — 产品事实 + 竞品矩阵

> 加载时机：Phase 0R / Phase 4 / Phase 5
> 数据基线：oginify.com 官网、pricing 页、GitHub、各竞品官方页，**R3 验证后用**

---

## 1. Oginify 产品事实（Proof Ledger 快照）

| Proof ID | 事实 | as-of |
|----------|------|-------|
| OG-01 | 粘贴任意 URL → 读取页面 title/description/品牌色/logo → 生成 4 张 1200×630 卡片（1 on-brand + 3 wildcards：editorial / terminal / swiss-minimal） | 2026-08 |
| OG-02 | 无 prompt 框、无模板选择、无注册；生成约 30 秒 | 2026-08 |
| OG-03 | 免费额度 6 张/天（签名账号），无需绑定卡片 | 2026-08 |
| OG-04 | 定价按张付费、无订阅：Single $0.99 · Pack 10 $7.90（$0.79/张）· Pack 50 $29（$0.58/张）；credits 不过期 | 2026-08 |
| OG-05 | 免费版可无账号每日生成（网站称 6 images/day without account） | 2026-08 |
| OG-06 | 输出严格 1200×630 PNG，含 ready-made Open Graph + Twitter Card meta tags | 2026-08 |
| OG-07 | 开源版 `social-cards-skills`（MIT）：同一引擎的 Agent Skills 发行版，支持 Satori+resvg 与 AI/混合纹理双管线、16 视觉风格、Agent-Native v3 内容感知工作流（100+ 页面类型分类、S/A/B/C 页面优先级、35 站点类型画像） | 2026-08 |
| OG-08 | 官方定位：与 @vercel/og（JSX 代码渲染）和 Cloudinary（URL 变换已有素材）是「相邻问题，不是同一问题」 | 2026-08 |
| OG-09 | 免费工具矩阵：text-to-og · image-to-og · bulk generator · twitter card generator · github social preview · og-scorer · open-graph-validator · free maker | 2026-08 |
| OG-10 | 案例：launch feature / refresh blog / defend landing page / ship ad set | 2026-08 |

---

## 2. 三分类决策框架（Oginify 博客差异化核心）

```
┌─────────────────────────────────────────────────────────────────────┐
│ 目标：从「我有一个 URL」到「链接被分享时好看」的最短路径            │
├──────────────┬──────────────────────────┬──────────────────────────┤
│ URL-first    │ 通用生图 AI              │ 代码驱动                │
│ (Oginify)    │ (Gemini/GPT/Midjourney)  │ (Vercel OG / Satori)     │
├──────────────┼──────────────────────────┼──────────────────────────┤
│ 输入 = URL   │ 输入 = prompt + 尺寸     │ 输入 = JSX/markup        │
│ 自动品牌读取 │ 手动指定品牌/尺寸/文字   │ 布局写死在代码           │
│ 4 变体/次    │ 1 图/次                  │ 1 模板/次                │
│ meta tags 现成│ meta tags 自己写        │ meta tags 自己写         │
│ 托管 PNG     │ 自己托管                 │ edge 渲染                │
└──────────────┴──────────────────────────┴──────────────────────────┘
```

**写作规则**：任何 Comparison/Ranking/Alternative 必须使用此三分类框架（P2 + C2 相关）。**不得**写「Gemini/GPT Image 不能做 OG 卡片」——它们能做，只是需要用户手动处理尺寸、文字渲染、导出与托管（P2 反例）。

---

## 3. 竞品矩阵（R3 验证后使用）

| 竞品 | 分类 | 关键事实 | 优势（≥1 必写） | 非 Oginify 更合适场景 |
|------|------|---------|----------------|---------------------|
| **Gemini（Google）** | 通用生图 | Gemini 3.1 Flash Image（Nano Banana 2）GA 2026-05-28；API 无免费 tier；1K 图约 $0.067/张（$60/1M output tokens） | 文本渲染强、多语言、对话式多轮编辑、便宜 | 已在 Google AI Studio / Gemini app 生态中、愿意自己裁剪与托管 |
| **GPT Image 2（OpenAI）** | 通用生图 | ChatGPT Images 2.0 发布 2026-04-21；native reasoning；API token 计费（image output $30/1M tokens，1K 图约 $0.006–$0.21/张看质量档） | 图像内文字最清晰（headline 缩略图可读）、2K 分辨率、多图一致性 | 文字密集型卡片 DIY、ChatGPT 订阅用户 |
| **Midjourney** | 通用生图 | V8.1（2026-04）；无免费 tier；Basic $10 / Standard $30 / Pro $60 / Mega $120 每月；年付 8 折 | 艺术质感最强、默认审美「art-directed」 | 纯艺术、少文字的视觉卡（essay cover、podcast art） |
| **Vercel OG (@vercel/og)** | 代码驱动 | 免费（含 Vercel free tier）；JSX→Satori→SVG→resvg→PNG；edge 渲染 + CDN 缓存；CSS 子集（flexbox + absolute，无 grid） | 免费、Next.js 深度集成、布局是代码可版本化 | Next.js 团队、要完全控制布局 |
| **Placid** | 模板自动化 | 起 $19/月（500 credits）→ $39/月（2500）；模板编辑器 + REST API + webhook 自动化 | CMS 发布量大的内容管线自动化 | 数百张/月的 CMS 管线 |
| **Bannerbear** | 模板自动化 | 起 $49/月（1000 credits）→ $149/$299；模板编辑器 + API + Node/Ruby/PHP SDK | 设计者管模板、工程管集成的角色分离 | 设计治理严格的团队 |
| **Canva** | 手动设计 | 免费 tier 可用；付费约 $13/月；含 AI 生成 | 熟悉、模板多、一次性手工卡 | 每季度 1 张手工卡 |
| **Cloudinary** | URL 变换 | 免费 tier 慷慨；付费约 $99/月起；变换 API 合成文字/logo 到已有素材 | 已有 Cloudinary CDN 用户零新增服务 | 已有 CDN 资产管线 |

---

## 4. 竞品措辞红线

| 禁止 | 正确 |
|------|------|
| 「just a prompt tool」 | 「通用生图工具需要你手动指定尺寸与导出」 |
| 「Gemini can't do OG images」 | 「Gemini 能画卡片，但你要自己处理 1200×630 与 meta tags」 |
| 「only Oginify is promptless」 | 「Oginify 以 URL 为唯一输入；通用工具以 prompt 为输入」 |
| 「Vercel OG is for nerds」 | 「Vercel OG 需要开发者为布局写 JSX」 |

---

## 5. 合规红线

- 禁「全球首个」「唯一」「自动提升 CTR 300%」（G5/P6）
- 竞品定价必须 `as of {month} {year}` + `[Source: URL]`（G3/P1）
- 不称竞品 dead/failed；不贬低（G7/P5）
- AI 生成视觉提及需标注（若文中提到 AI 生成图）
- 1200×630 规格 claim 链 oginify.com 或 ogp.me（P3）
