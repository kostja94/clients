# Nova Scientia — 多语言多地区路由规划

> **Status**: 实施中（阶段 0 完成）
> **Last updated**: 2026-08-08（v2：精简为 5 市场）

---

## 一、目标

在现有 pt-BR 巴西站基础上，新增 **葡萄牙语（葡萄牙）**、**西班牙语（墨西哥 + 西班牙）** 与 **英语（美国）** 语言版本，URL 采用**扁平 locale 前缀**，pt-BR 保持根路径不动。

## 二、地区 ↔ 语言 ↔ 路由映射

| 地区 | 语言 | Locale | 路由前缀 | 说明 |
|------|------|--------|----------|------|
| 巴西 🇧🇷 | 葡萄牙语 | `pt-BR` | `/`（根路径） | 现有主站，URL 完全不动 |
| 葡萄牙 🇵🇹 | 葡萄牙语 | `pt-PT` | `/pt-pt/` | 欧葡，与 pt-BR 同源，翻译成本最低 |
| 西班牙 🇪🇸 | 西班牙语 | `es-ES` | `/es-es/` | 卡斯蒂利亚西语，欧洲标准 |
| 墨西哥 🇲🇽 | 西班牙语 | `es-MX` | `/es-mx/` | 西语最大市场（1.38 亿），拉美基准变体 |
| 美国 🇺🇸 | **英语** | `en-US` | `/en/` | 英语市场（覆盖全美，含 6500 万西语人口） |

> **v2 变更**（2026-08-08）：移除 `es-CO`、`es-AR`、`es-CL`（维护成本高于回报）；新增 `en`（美国英语）——美国是西语母语者全球第二多的国家，但用**英语**覆盖整个美国市场更高效。
> 不做 `es-419` 区域兜底——其余拉美国家暂不建站。

## 三、路由表（现有 + 新增）

现有 pt-BR 全部路由原样保留在根路径；每个语言前缀下镜像同一套结构：

| 现有（pt-BR，根路径） | 新增：`/{locale}/`（locale ∈ {pt-pt, es-es, es-mx, en}） |
|---|---|
| `/`（首页） | `/{locale}/` |
| `/products` | `/{locale}/products` |
| `/products/{slug}` | `/{locale}/products/{slug}` |
| `/topic` | `/{locale}/topic` |
| `/{slug}`（主题） | `/{locale}/{slug}` |
| `/company` `/company/{slug}` | `/{locale}/company` `/{locale}/company/{slug}` |
| `/glossary` | `/{locale}/glossary` |
| `/image` `/video` `/voice` `/3d` `/design` `/coding` `/productivity` | `/{locale}/image` 等（7 个分类 hub） |
| `/about` | `/{locale}/about` |

**关键决策**：URL slug 不本地化。产品 slug（`chatgpt`）、主题 slug（`llm`、`image-generator`）跨语言保持一致，只有 H1/标题/正文翻译。避免重定向矩阵和 hreflang 混乱，是 Google 国际站标准做法。

## 四、技术实现架构

复用 Alignify 已验证的 `next-intl` + `app/[locale]/` 模式，用 **middleware 重写** 让 pt-BR 留在根路径：

```
app/
├── [locale]/                  # 统一语言树（包含 pt-br 镜像）
│   ├── layout.tsx             # <html lang={locale}> + next-intl Provider
│   ├── page.tsx               # 首页
│   ├── products/[slug]/page.tsx
│   ├── [slug]/page.tsx        # 主题（RESERVED_SLUGS 守卫照旧）
│   ├── company/[slug]/page.tsx
│   ├── glossary/page.tsx
│   ├── topic/page.tsx
│   └── ...
├── middleware.ts              # 核心：无前缀请求 → 重写为 /pt-br/...（URL 不变）
├── i18n/
│   ├── routing.ts             # locales: ['pt-br','pt-pt','es-mx','es-es','en']
│   └── request.ts
└── messages/
    ├── pt-br.json             # UI 文案（导航/按钮/页脚）
    ├── pt-pt.json
    ├── es-mx.json
    ├── es-es.json
    └── en.json
```

**middleware 逻辑**：
- 请求 `/products/chatgpt` → 内部重写为 `/pt-br/products/chatgpt`，浏览器地址栏仍是 `/products/chatgpt`，现有外链/Google 收录全部不失效
- 请求 `/es-mx/...`、`/en/...` 等 → 直接走对应 locale
- 非法 locale（如 `/fr/`）→ `notFound()`

## 五、数据层方案（部分翻译 + 优雅回落）

现有 `content/products/` 是 pt-BR，原样保留。新增翻译采用**覆盖层**结构：

```
content/
├── products/                    # pt-BR 默认（现有 435，不动）
├── topics/
├── companies/
├── glossary.json
└── locales/
    ├── pt-pt/
    │   ├── manifest.json        # 已翻译 slug 索引
    │   ├── products/            # 只放已翻译的产品
    │   └── topics/
    ├── es-mx/                   # 同上
    ├── es-es/                   # 同上
    └── en/                      # 同上
```

**读取逻辑**（改 `src/lib/content/products.ts` 等数据层，加 `locale` 参数）：

```
readProducts(locale) {
  // 1. 读 content/locales/{locale}/products/*.json
  // 2. 未翻译 slug → 该语言下页面 notFound()（不回落 pt-BR 原文）
}
```

**SEO 原则**：未翻译的页面在对应语言下直接 404，绝不回落显示 pt-BR 原文。混合语言页面会被 Google 判定为 hreflang 冲突/低质量。

## 六、SEO 配套

### hreflang（每页 6 条）

```html
<link rel="alternate" hreflang="pt-BR" href="https://novascientia.com.br/products/chatgpt" />
<link rel="alternate" hreflang="pt-PT" href="https://novascientia.com.br/pt-pt/products/chatgpt" />
<link rel="alternate" hreflang="es-ES" href="https://novascientia.com.br/es-es/products/chatgpt" />
<link rel="alternate" hreflang="es-MX" href="https://novascientia.com.br/es-mx/products/chatgpt" />
<link rel="alternate" hreflang="en-US" href="https://novascientia.com.br/en/products/chatgpt" />
<link rel="alternate" hreflang="x-default" href="https://novascientia.com.br/products/chatgpt" />
```

`x-default` 指向 pt-BR 根路径（无语言偏好用户的兜底）。

### 其他

- **Sitemap**：`app/sitemap.ts` 扩为多语言版，每个 `<url>` 配 `<xhtml:link rel="alternate">`；未翻译 slug 的语言版本不进 sitemap
- **Canonical**：各语言页面 canonical 指向自己
- **IndexNow**：`getAllPageUrls()` 扩展，全语言 URL 批量提交
- **`<html lang>` + OG locale**：pt-BR `pt_BR`、pt-PT `pt_PT`、es-MX `es_MX`、es-ES `es_ES`、en `en_US`
- **语言切换器**：Header 加跨语言跳转（保持同 slug），显示 `Português` / `Español` / `English`

## 七、变体差异内容注意点

| 变体 | 关键差异 | 内容策略 |
|------|----------|----------|
| pt-PT | `telemóvel`→`celular` 反向、`estou a` 结构 | 与 pt-BR 同源，只改词汇/结构 |
| es-ES | `ordenador`、`móvil`、`vosotros`、`gratuito` | 欧洲标准，书面语 |
| es-MX | `computadora`、`celular`、`gratis`、口语化程度低、最接近书面中立 | 内容写作基准 |
| en-US | 全英语 | 面向美国市场，元数据用英语关键词（`AI tools`、`best image generator`） |

**关键词映射**：每个语言做独立关键词映射（`gerador de imagem`→`generador de imágenes`→`image generator`）。

## 八、分阶段实施规划

| 阶段 | 内容 | 产出 |
|------|------|------|
| **0. 架构** | middleware + `[locale]` 树迁移 + 数据层加 locale 参数 | ✅ 已完成 |
| **1. UI 文案** | `messages/*.json` 翻译导航/按钮/页脚/横幅 | 界面多语言可切换 |
| **2. 内容翻译** | 按优先级翻译主题/产品到各 locale | 各语言内容上线 |
| **3. 葡语低成本铺开** | pt-PT 内容：与 pt-BR 同源，只改词汇/结构 | pt-PT 全量覆盖 |
| **4. 产品扩量** | 产品评测逐步翻译，按 GSC 流量排序 | 覆盖率持续上升 |
| **5. 验收** | sitemap/hreflang/IndexNow 全量接入，GSC 分语言验证 | 各市场 SEO 独立运转 |

## 九、翻译优先级

**en-US（美国，最大英语市场）> es-MX（西语最大市场）> pt-PT（成本最低）> es-ES（单市场）**

拉美/英语主题关键词需对照现有 `keyword-map.md` 分别做西语版、英语版映射。
