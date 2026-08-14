# Moras i18n 路由迁移执行文档

> **关联**：[moras-site-structure.md](./moras-site-structure.md) · [moras.ai](https://moras.ai/)  
> **最后更新**：2026-06-24（审校：Phase 页数对齐 · 删 invite · Blog/法务 Shell 恒英文 · `/?lang=en` · sitemap 分工 · SEO `[locale]` 方案 · root layout）  
> **执行对象**：Moras 工程 Agent / 开发团队

---

## 0. 现状与目标

### 0.1 当前架构（迁移前）

| 维度 | 现状 |
|------|------|
| 框架 | Next.js App Router + React |
| i18n 库 | **i18next** + **react-i18next** + browser-languagedetector |
| 语言存储 | `localStorage` 键 `i18nextLng` |
| 切换行为 | `changeLanguage()`，**URL 不变** |
| 文案来源 | en/es JSON **内联打包**进 JS bundle（namespace: `common`, `home`, `landing`） |
| 西语覆盖 | **仅营销 SPA**（`/`, `/landing` 等）；Blog 等 SEO 页**仅英文** |
| 双应用 | **主应用**（moras.ai，`/` SPA）+ **SEO 子应用**（独立子域/集群 `moras-seo`，middleware **rewrite** 转发；用户 URL 仍为 `moras.ai/...`） |
| 半成品路由 | `/?lang=es` → 308 `/es` → **404**（路径 i18n 未落地） |

### 0.2 目标架构（迁移后）

| 维度 | 目标 |
|------|------|
| i18n 库 | **next-intl**（App Router 集成） |
| URL 策略 | `localePrefix: 'as-needed'` — 英文根域名，西语 `/es/` |
| 切换行为 | `router.replace(pathname, { locale })`，**URL 随语言变更** |
| SSR | 服务端直接输出对应语言 HTML，`<html lang={locale}>` |
| 语言检测 | **`localeDetection: false`** — 不读 Accept-Language；语言仅由 URL、`LanguageSwitcher`、`?lang=` 兼容跳转决定 |
| SEO | 可本地化页独立 URL + hreflang；**Blog + 法务** 英语独占（见 §0.3、§4.5）；**除首页/landing 外 SEO 页在独立子应用**（§0.5） |

> **英文 URL 原则**：`localePrefix: 'as-needed'` + `defaultLocale: 'en'` → 英文 canonical **永不暴露** `/en/` 前缀。Moras **历史上从未**对外使用 `/en/` URL；全站 canonical、sitemap、内链均不得含 `/en/`，**仅 `/es/` 为西语前缀**。

### 0.3 URL 对照表

| 英文（默认，无前缀） | 西语 |
|---------------------|------|
| `/` | `/es/` |
| `/blog` | —（**英语独占**，无西语 URL） |
| `/blog/{slug}` | —（**英语独占**，无西语 URL） |
| `/tiktok-video-generator` | `/es/tiktok-video-generator` |
| `/tiktok-video-generator/{slug}` | `/es/tiktok-video-generator/{slug}` |
| `/use-cases` | `/es/use-cases` |
| `/use-cases/{persona}` | `/es/use-cases/{persona}` |
| `/tools/{tool}` | `/es/tools/{tool}` |
| `/product-research` | `/es/product-research` |
| `/landing` | `/es/landing` |
| `/terms` | —（**英语独占**） |
| `/privacy` | —（**英语独占**） |
| `/precheck-guidance` | —（**英语独占**） |
| `/subscription` | —（**英语独占**） |

**禁止**：对外暴露 `/en/...` canonical URL（全站 canonical / sitemap / 内链均不得含 `/en/`；仅 `/es/` 为西语前缀）。若请求误入 `/en/*`，middleware **防御性 301** 去前缀（见 §7）——非历史 URL 迁移。

**英语独占路径（Blog + 法务）**：`/blog`、`/blog/{slug}`、`/terms`、`/privacy`、`/precheck-guidance`、`/subscription` **不参与** locale 前缀路由，**不生成** `/es/...` 西语 URL。与 TVG、Use Cases、Tools 等需渐进 i18n 的栏目不同，上述路径**永久仅英语**；访问 `/es/blog*`、`/es/terms` 等应 **301 → 对应英文 URL**（见 §5.2）。法务页不做机翻，待法务审定前保持英文正文。

### 0.4 站点页面规模（来自 moras-site-structure.md）

| 栏目 | 英文页数 | 西语 Phase 1 | 西语 Phase 2 | 西语 Phase 3 |
|------|---------|-------------|-------------|-------------|
| 静态页 | 6 | **2**（`/`、`/landing`，主应用） | — | — |
| Product | 1 | — | 1（Hub） | — |
| Tools | 3 | — | 3 | — |
| Use Cases | 6 | — | Hub ×1 | 5 vertical |
| TikTok Video Generator | 16 | — | Hub ×1 | 15 vertical |
| Blog | 20 | **0**（英语独占） | — | — |
| 法务（含于静态 6） | 4 | **0**（en-only，SEO 子应用渲染） | — | — |
| **可本地化小计** | **28** | **2** | **6** | **20** |
| **全站合计** | **52** | | | |

> **规模说明**：52 页**并非**主应用单仓库 `generateStaticParams` 可覆盖。主应用仅渲染 `/`、`/landing`（及西语变体）；其余 **~50 页**在 **SEO 子应用仓库**独立构建。Blog 20 页 + 法务 4 页**不参与**西语 rollout（28 = 52 − 20 − 4）。

### 0.5 双应用部署架构（真实拓扑）

**除首页 `/`（及 `/es/` 西语首页）与 `/landing` 外**，用户访问的 Blog、TVG、Use Cases、Tools、Product、法务等路径，均由 **主域 middleware rewrite** 转发至 **独立部署的 SEO Next.js 子应用**（占位名：`seo.moras.ai` / 集群服务 `moras-seo`）。两个应用的**正文内容分开编辑**——不同仓库、不同 CMS/内容源、不同团队；**不存在**主应用 `messages/*.json` 与子应用 MDX/CMS **自动同步**。

| 维度 | 主应用（moras.ai 首页） | SEO 子应用（rewrite 目标） |
|------|------------------------|---------------------------|
| **职责** | 仅 `/`、`/es/`（西语首页）、`/landing`、`/es/landing` | Blog、TVG、Use Cases、Tools、Product、法务静态页等 **~50 页** |
| **部署** | moras.ai 主 Vercel/集群 | **独立子域名或内部 upstream**（如 `https://seo.moras.ai` 或 `moras-seo.prod.svc`） |
| **内容编辑** | `messages/en.json`、`messages/es.json`（首页/landing shell） | 独立 `content/` 或 CMS；西语正文在 **`content/es/...`** 或 CMS `translations.es` |
| **i18n 实施** | next-intl `app/[locale]/` **仅 `/`、`/landing`** | **`app/[locale]/...`** 渲染可本地化 SEO 页；Blog/法务裸路径 layout 读 `x-moras-locale`（恒 `en`） |
| **rewrite** | middleware 解析 locale → 改内部 pathname + ingress 至子域 | 接收内部请求；对用户浏览器 URL **始终**为 `moras.ai/...` |
| **静态资源** | `moras.ai/_next/...` | `moras.ai/seo-static/_next/...` 或子域 `/_next/...`（ingress 按 path 分流） |

**`/seo-static/` 前缀含义**：文档与 middleware 示例中的 `/seo-static/...` 是 **rewrite 目标路径的抽象**——表示「转发至 SEO upstream 的内部路由前缀」。实际上可能是：

- `NextResponse.rewrite` 至同集群 path `/seo-static/...`，再由 ingress 反代至 SEO 服务；或
- 直接 rewrite 至 `https://{SEO_ORIGIN}/...`（见 `next.config.ts` `rewrites()`）

上线前须与 DevOps 确认 **SEO_ORIGIN** 与 path 映射；staging 必须跑通完整 rewrite 链。

#### 内容协作流程（跨团队）

| 场景 | 子应用（SEO 仓库） | 主应用（首页仓库） | 负责方 |
|------|-------------------|-------------------|--------|
| 新增 TVG vertical | 先部署 slug 页 + 英文正文 | middleware `SEO_PATH_PREFIXES` 无需改（已覆盖前缀）；**主域 sitemap index** 增量条目 | SEO 团队部署 → 平台/DevOps 更新 sitemap |
| 新增可本地化 Hub 西语 | `content/es/...` 或 CMS 发布 | 无正文变更；确认 middleware 对 `/es/{path}` rewrite 带 locale 段 | SEO 团队 |
| 西语翻译 | 子应用 `content/es/tiktok-video-generator/` 等 | `messages/es.json` **仅**首页/landing shell | 各管各库，不假设 monorepo 自动同步 |
| Blog 新文 | `content/en/blog/{slug}.mdx` | 无；Blog **永不开** `/es/blog` | SEO 团队 |
| 法务页更新 | 子应用 `app/terms/` 等（en-only） | 无 | SEO/法务 |

---

## 1. 目标目录结构

> **两仓库**：下列 §1.1 与 §1.2 **不可合并**为单棵主应用目录树；实施者须分别在两个仓库落地。

### 1.1 主应用（moras.ai 首页仓库）

```
moras-main/                           # 主应用仓库（moras.ai 首页）
├── middleware.ts                     # next-intl + SEO rewrite + 防御性 /en/ 拦截
├── next.config.ts                    # next-intl plugin + rewrites → SEO_ORIGIN
├── i18n/
│   ├── routing.ts
│   ├── request.ts
│   └── navigation.ts
├── messages/
│   ├── en.json                       # 仅 home / landing / common shell
│   └── es.json
├── lib/
│   ├── i18n-paths.ts                 # EN_ONLY_PREFIXES（与 SEO 仓库同源或 monorepo 共享）
│   └── metadata.ts                   # buildAlternates() — 首页/landing
├── app/
│   ├── [locale]/
│   │   ├── layout.tsx                # NextIntlClientProvider, html lang
│   │   ├── page.tsx                  # 首页 SPA
│   │   └── landing/page.tsx          # 备用 Landing（/landing、/es/landing）
│   ├── layout.tsx                    # minimal root（pass-through children）
│   └── sitemap.ts                    # index：聚合 site-* + 拉取/代理 seo-* sitemap
├── components/
│   └── LanguageSwitcher.tsx
└── ...
```

**主应用 `app/` 下不应出现**：`product-research/`、`tools/`、`use-cases/`、`tiktok-video-generator/`、`blog/`、`terms/` 等——这些路由 **仅存在于 SEO 子应用**，经 middleware rewrite 访问。

### 1.2 SEO 子应用（moras-seo / seo.moras.ai 仓库）

```
moras-seo/                            # SEO 子应用仓库（独立部署）
├── middleware.ts                     # 可选：内部直连时补 locale；经主域 rewrite 时可省略
├── i18n/                             # next-intl（与主应用 routing 一致）
│   ├── routing.ts
│   ├── request.ts
│   └── navigation.ts
├── messages/
│   ├── en.json                       # SEO Header/Footer shell（与主应用 messages 不同步）
│   └── es.json
├── lib/
│   ├── i18n-paths.ts                 # 与主应用同源，或 monorepo packages/i18n-paths
│   └── metadata.ts                   # buildAlternates / buildEnOnlyAlternates
├── content/
│   ├── en/
│   │   ├── blog/
│   │   ├── tiktok-video-generator/
│   │   └── use-cases/
│   └── es/                           # 西语正文（Phase 2 Hub · Phase 3 vertical）
│       ├── tiktok-video-generator/
│       └── use-cases/
├── app/
│   ├── layout.tsx                    # root pass-through（见 §2.14）
│   ├── [locale]/                     # 可本地化 SEO 页（TVG / Use Cases / Tools / Product）
│   │   ├── layout.tsx                # `<html lang>`；locale 来自 params.locale
│   │   ├── use-cases/
│   │   │   ├── page.tsx
│   │   │   └── [persona]/page.tsx
│   │   ├── tiktok-video-generator/
│   │   │   ├── page.tsx
│   │   │   └── [slug]/page.tsx
│   │   ├── tools/[tool]/page.tsx
│   │   └── product-research/page.tsx
│   ├── blog/                         # 英语独占，不在 [locale] 下
│   │   ├── layout.tsx                # en-only shell；LanguageSwitcher 行为见 §4.6
│   │   ├── page.tsx
│   │   └── [slug]/page.tsx
│   ├── terms/page.tsx                # 法务 en-only（若确认在 SEO 子应用）
│   ├── privacy/page.tsx
│   ├── precheck-guidance/page.tsx
│   ├── subscription/page.tsx
│   └── sitemap.ts                    # seo-sitemap.xml + seo-es-sitemap.xml
└── ...
```

> **说明**：对用户 URL 始终是 `moras.ai/...` 或 `moras.ai/es/...`，**不暴露** `/seo-static/` 或子域名。主应用 middleware 负责 locale 解析与 rewrite；SEO 子应用负责 **52 页中除首页/landing 外的全部页面**渲染。**Blog + 法务** 为英文裸路径（无 `/es` 前缀），但 **物理代码在 SEO 子应用仓库**。

---

## 2. 完整技术配置（复制即用）

> **仓库标注**：§2.2–§2.10 为 **[MAIN] 主应用**；§2.11–§2.12、§2.14 为 **[SEO] 子应用**；§2.5、§2.12 `LanguageSwitcher` **两仓库均需**（或 monorepo 共享包）。

### 2.1 安装依赖

```bash
# 安装
npm install next-intl

# 卸载（Phase 1 移除 i18next 时，见 P1-M04）
npm uninstall i18next react-i18next i18next-browser-languagedetector
```

### 2.2 `i18n/routing.ts`

```typescript
import { defineRouting } from 'next-intl/routing';

export const routing = defineRouting({
  locales: ['en', 'es'],
  defaultLocale: 'en',
  localePrefix: 'as-needed', // en 无前缀，es 为 /es/
  localeDetection: false,    // 不自动检测 Accept-Language
});

export type Locale = (typeof routing.locales)[number];
```

### 2.3 `i18n/request.ts`

```typescript
import { getRequestConfig } from 'next-intl/server';
import { hasLocale } from 'next-intl';
import { routing } from './routing';

export default getRequestConfig(async ({ requestLocale }) => {
  const requested = await requestLocale;
  const locale = hasLocale(routing.locales, requested)
    ? requested
    : routing.defaultLocale;

  return {
    locale,
    messages: (await import(`../messages/${locale}.json`)).default,
  };
});
```

### 2.4 `i18n/navigation.ts`

```typescript
import { createNavigation } from 'next-intl/navigation';
import { routing } from './routing';

export const { Link, redirect, usePathname, useRouter, getPathname } =
  createNavigation(routing);
```

### 2.5 `lib/i18n-paths.ts`（共享路径常量，单源维护）

> **middleware** 与 **LanguageSwitcher**（及 SEO Header）均 import 此文件；新增 en-only 路径**只改一处**。

```typescript
import type { Locale } from '@/i18n/routing';

/** 英语独占：无 /es/ 变体、不进 seo-es-sitemap（Blog + 法务） */
export const EN_ONLY_PREFIXES = [
  '/blog',
  '/terms',
  '/privacy',
  '/precheck-guidance',
  '/subscription',
] as const;

export function isEnOnlyPath(path: string): boolean {
  return EN_ONLY_PREFIXES.some(
    (prefix) => path === prefix || path.startsWith(`${prefix}/`)
  );
}

/** 从 pathname 解析 locale；返回值恒为 'en' | 'es'（非 null） */
export function stripLocale(pathname: string): { locale: Locale; path: string } {
  if (pathname === '/es' || pathname.startsWith('/es/')) {
    const path = pathname.replace(/^\/es/, '') || '/';
    return { locale: 'es', path };
  }
  return { locale: 'en', path: pathname };
}
```

**双仓库共享**：主应用与 SEO 子应用各一份 `lib/i18n-paths.ts`，或通过 monorepo `packages/i18n-paths` 发布为 npm workspace 包；**禁止**在两边 middleware / Switcher 内各写一份列表。变更 en-only 路径须 **两仓库同步发版**（或 monorepo 一次 PR）。

### 2.6 `next.config.ts`（主应用）

```typescript
import type { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./i18n/request.ts');

const SEO_ORIGIN = process.env.SEO_ORIGIN ?? 'http://moras-seo.internal';

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/seo-static/:path*',
        destination: `${SEO_ORIGIN}/:path*`, // 实际可能是 https://seo.moras.ai/:path*
      },
    ];
  },
  // 保留现有 headers 等；勿删除 seo-static 相关配置
};

export default withNextIntl(nextConfig);
```

> middleware 将 pathname 改为 `/seo-static/...` 后，由上述 `rewrites()` 转发至 SEO 子应用 upstream。

### 2.7 `middleware.ts`（核心：locale + seo-static + 301）

```typescript
import createMiddleware from 'next-intl/middleware';
import { NextRequest, NextResponse } from 'next/server';
import { routing } from './i18n/routing';
import {
  isEnOnlyPath,
  stripLocale,
} from './lib/i18n-paths';

const intlMiddleware = createMiddleware({
  ...routing,
  localeDetection: false,
});

/** SEO 子应用内部前缀（对用户不可见；实际 upstream 可能是 https://{SEO_ORIGIN}/...） */
const SEO_INTERNAL_PREFIX = '/seo-static';

/** 需转发至 SEO 子应用的路径段（与 moras-site-structure.md 对齐） */
const SEO_PATH_PREFIXES = [
  '/blog',
  '/use-cases',
  '/tiktok-video-generator',
  '/tools',
  '/product-research',
  '/terms',
  '/privacy',
  '/precheck-guidance',
  '/subscription',
] as const;

/** 主应用本地渲染的可本地化 SPA（仅首页与 landing） */
const LOCALIZED_SPA_PATHS = new Set(['/', '/landing']);

function isSeoPublicPath(path: string): boolean {
  if (LOCALIZED_SPA_PATHS.has(path)) return false;
  return SEO_PATH_PREFIXES.some(
    (prefix) => path === prefix || path.startsWith(`${prefix}/`)
  );
}

function buildSeoInternalPath(
  locale: ReturnType<typeof stripLocale>['locale'],
  publicPath: string
): string {
  const localeSegment =
    locale === 'es' && !isEnOnlyPath(publicPath) ? '/es' : '';
  return `${SEO_INTERNAL_PREFIX}${localeSegment}${publicPath === '/' ? '' : publicPath}`;
}

export default function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // ── 1. 静态资源 / API：跳过 ──
  if (
    pathname.startsWith('/_next') ||
    pathname.startsWith('/api') ||
    pathname.startsWith(SEO_INTERNAL_PREFIX) ||
    pathname.includes('.')
  ) {
    return NextResponse.next();
  }

  // ── 2. 防御性 /en/* 301（线上历史无 /en/）──
  if (pathname === '/en' || pathname.startsWith('/en/')) {
    const target = pathname.replace(/^\/en/, '') || '/';
    return NextResponse.redirect(new URL(target, request.url), 301);
  }

  const { locale, path } = stripLocale(pathname);

  // ── 3. ?lang= 兼容跳转（308，去掉 query）──
  const langParam = request.nextUrl.searchParams.get('lang');
  if (langParam === 'es') {
    if (isEnOnlyPath(path)) {
      const url = new URL('/es', request.url);
      url.search = '';
      return NextResponse.redirect(url, 308);
    }
    const esPath = path === '/' ? '/es' : `/es${path}`;
    const url = new URL(esPath, request.url);
    url.search = '';
    return NextResponse.redirect(url, 308);
  }
  if (langParam === 'en') {
    const enPath = path === '/' ? '/' : path;
    const url = new URL(enPath, request.url);
    url.search = '';
    return NextResponse.redirect(url, 308);
  }

  // ── 4. /es/{en-only}* → 301 英文 canonical ──
  if (locale === 'es' && isEnOnlyPath(path)) {
    return NextResponse.redirect(new URL(path, request.url), 301);
  }

  // ── 5. SEO 路径（含 Blog、法务、TVG 等）：rewrite → SEO 子应用 ──
  if (isSeoPublicPath(path)) {
    const rewriteUrl = request.nextUrl.clone();
    rewriteUrl.pathname = buildSeoInternalPath(locale, path);
    const response = NextResponse.rewrite(rewriteUrl);
    response.headers.set(
      'x-moras-locale',
      isEnOnlyPath(path) ? 'en' : locale
    );
    return response;
  }

  // ── 6. 可本地化 SPA：next-intl（/、/landing、/es/...）──
  return intlMiddleware(request);
}

export const config = {
  matcher: [
    '/',
    '/(es)/:path*',
    '/en/:path*',
    '/((?!_next|api|favicon|.*\\..*).*)',
  ],
};
```

> **Agent 注意（主应用 middleware）**：`NextResponse.rewrite` 仅改 `pathname` 为 `/seo-static/...`（见 §2.6 `rewrites()` → `SEO_ORIGIN`）。Blog、法务、TVG 等 **均** 走 rewrite，**不在**主应用 `app/` 下实现 page。上线前 staging 验证：用户 URL → 主 middleware → SEO 子应用 200。

### 2.8 `app/[locale]/layout.tsx`（主应用 — 仅首页/landing）

```tsx
import { NextIntlClientProvider, hasLocale } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import { routing } from '@/i18n/routing';
import { LanguageSwitcher } from '@/components/LanguageSwitcher';

type Props = {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
};

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }));
}

export default async function LocaleLayout({ children, params }: Props) {
  const { locale } = await params;

  if (!hasLocale(routing.locales, locale)) {
    notFound();
  }

  setRequestLocale(locale);
  const messages = await getMessages();

  return (
    <html lang={locale}>
      <body>
        <NextIntlClientProvider messages={messages}>
          <header>
            {/* 现有 Header */}
            <LanguageSwitcher />
          </header>
          {children}
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
```

### 2.9 `lib/metadata.ts` — hreflang 辅助

```typescript
const BASE_URL = 'https://moras.ai';

/**
 * 可本地化页的 hreflang 语言映射（canonical 恒为英文 URL，西语页请用 buildEsCanonical + languages）
 * @param pathname 不含 locale 的纯路径
 * @param options.includeEs 西语版是否已发布（未发布则不输出 es alternate）
 * @note Blog / 法务（`/blog/*`、`/terms` 等）英语独占，用 buildEnOnlyAlternates()
 */
export function buildLanguageAlternates(
  pathname: string,
  options?: { includeEs?: boolean }
) {
  const includeEs = options?.includeEs ?? true;
  const normalized = pathname.startsWith('/') ? pathname : `/${pathname}`;
  const enUrl = `${BASE_URL}${normalized === '/' ? '' : normalized}`;
  const esUrl = `${BASE_URL}/es${normalized === '/' ? '' : normalized}`;

  const languages: Record<string, string> = {
    en: enUrl,
    'x-default': enUrl,
  };

  if (includeEs) {
    languages.es = esUrl;
  }

  return languages;
}

/** 英文页 metadata：canonical + hreflang */
export function buildAlternates(
  pathname: string,
  options?: { includeEs?: boolean }
) {
  const normalized = pathname.startsWith('/') ? pathname : `/${pathname}`;
  const enUrl = `${BASE_URL}${normalized === '/' ? '' : normalized}`;

  return {
    alternates: {
      canonical: enUrl,
      languages: buildLanguageAlternates(pathname, options),
    },
  };
}

/** Blog + 法务等英语独占页：仅 en + x-default，无 hreflang es */
export function buildEnOnlyAlternates(pathname: string) {
  const normalized = pathname.startsWith('/') ? pathname : `/${pathname}`;
  const url = `${BASE_URL}${normalized}`;
  return {
    alternates: {
      canonical: url,
      languages: {
        en: url,
        'x-default': url,
      },
    },
  };
}

/** 西语页的 canonical 应指向西语 URL */
export function buildEsCanonical(pathname: string) {
  const normalized = pathname.startsWith('/') ? pathname : `/${pathname}`;
  return `${BASE_URL}/es${normalized === '/' ? '' : normalized}`;
}
```

### 2.10 `generateMetadata` 示例 — 首页（主应用）

```tsx
// app/[locale]/page.tsx
import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { buildAlternates, buildEsCanonical, buildLanguageAlternates } from '@/lib/metadata';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'home' });

  const pathname = '/';
  const alternates =
    locale === 'es'
      ? {
          alternates: {
            canonical: buildEsCanonical(pathname),
            languages: buildLanguageAlternates(pathname),
          },
        }
      : buildAlternates(pathname);

  return {
    title: t('meta.title'),
    description: t('meta.description'),
    ...alternates,
  };
}
```

### 2.11 `generateMetadata` 示例 — 英语独占页（SEO 子应用：Blog / 法务）

```tsx
// moras-seo/app/blog/[slug]/page.tsx 或 app/terms/page.tsx — 不在 [locale] 下
import type { Metadata } from 'next';
import { buildEnOnlyAlternates } from '@/lib/metadata';

type Props = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const pathname = `/blog/${slug}`; // 法务页改为 '/terms' 等

  return {
    title: '...',
    description: '...',
    ...buildEnOnlyAlternates(pathname),
  };
}
```

### 2.12 `components/LanguageSwitcher.tsx`（主应用 + SEO 子应用各一份或共享组件）

```tsx
'use client';

import { useLocale, useTranslations } from 'next-intl';
import { usePathname, useRouter } from '@/i18n/navigation';
import { routing, type Locale } from '@/i18n/routing';
import { isEnOnlyPath } from '@/lib/i18n-paths';

const LOCALE_LABELS: Record<Locale, string> = {
  en: 'English',
  es: 'Español',
};

export function LanguageSwitcher() {
  const locale = useLocale() as Locale;
  const router = useRouter();
  const pathname = usePathname();
  const t = useTranslations('common');

  function handleChange(nextLocale: Locale) {
    // en-only 页（Blog / 法务）：无西语等价 URL，切 Español → /es/
    if (isEnOnlyPath(pathname)) {
      if (nextLocale === 'es') {
        router.replace('/', { locale: 'es' });
        return;
      }
    }
    router.replace(pathname, { locale: nextLocale });
  }

  return (
    <div aria-label={t('language')}>
      <select
        value={locale}
        onChange={(e) => handleChange(e.target.value as Locale)}
      >
        {routing.locales.map((loc) => (
          <option key={loc} value={loc}>
            {LOCALE_LABELS[loc]}
          </option>
        ))}
      </select>
    </div>
  );
}
```

### 2.13 组件迁移：`useTranslation` → `useTranslations`

```tsx
// 迁移前（i18next）
import { useTranslation } from 'react-i18next';
const { t } = useTranslation('home');
<h1>{t('hero.title')}</h1>

// 迁移后（next-intl）
import { useTranslations } from 'next-intl';
const t = useTranslations('home');
<h1>{t('hero.title')}</h1>
```

```tsx
// 服务端组件
import { getTranslations } from 'next-intl/server';
const t = await getTranslations('home');
```

### 2.14 SEO 子应用 layout 分层（`[SEO]`）

**Root** — pass-through（与主应用相同）：

```tsx
// moras-seo/app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return children;
}
```

**可本地化页** — `[locale]/layout.tsx` 输出 `<html lang>`：

```tsx
// moras-seo/app/[locale]/layout.tsx
import { NextIntlClientProvider, hasLocale } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import { routing } from '@/i18n/routing';
import { LanguageSwitcher } from '@/components/LanguageSwitcher';

type Props = {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
};

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }));
}

export default async function SeoLocaleLayout({ children, params }: Props) {
  const { locale } = await params;
  if (!hasLocale(routing.locales, locale)) notFound();

  setRequestLocale(locale);
  const messages = await getMessages();

  return (
    <html lang={locale}>
      <body>
        <NextIntlClientProvider messages={messages}>
          <header>
            <LanguageSwitcher />
          </header>
          {children}
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
```

Blog / 法务 layout 各自输出 `<html lang="en">`（§4.6），**不要**嵌套在 `[locale]` 下。

---

## 3. 从 i18next 迁移步骤

### 3.1 文案 JSON 抽取

**任务**：从 `layout-*.js` bundle 或源码中的 `JSON.parse('...')` 提取 en/es 文案。

**i18next namespace → next-intl messages 映射**：

| i18next namespace | messages/*.json 顶层 key |
|-------------------|-------------------------|
| `common` | `common` |
| `home` | `home` |
| `landing` | `landing` |

**目标文件结构**：

```json
// messages/en.json
{
  "common": {
    "language": "Language",
    "download": "Download",
    "contact": "Contact"
  },
  "home": {
    "meta": {
      "title": "Moras - AI Commerce Producer for Viral Videos | K2 Lab",
      "description": "..."
    },
    "hero": {
      "title": "World-Leading Content e-Commerce Agent OS"
    }
  }
}
```

```json
// messages/es.json
{
  "common": {
    "language": "Idioma",
    "download": "Descargar",
    "contact": "Contacto"
  },
  "home": {
    "meta": {
      "title": "...",
      "description": "..."
    },
    "hero": {
      "title": "Agent OS líder mundial para comercio de contenido"
    }
  }
}
```

**Agent 操作**：
1. 在源码中搜索 `i18next`、`initReactI18next`、`resources:` 定位原始 JSON
2. 若无源码，从生产 bundle `/_next/static/chunks/app/layout-*.js` 提取 `JSON.parse` 内容
3. 写入 `messages/en.json`、`messages/es.json`
4. 键名保持一致，便于机械替换 `t('key')` 调用

### 3.2 删除 i18next 初始化

移除类似以下代码（通常在 `app/layout.tsx` 或 `lib/i18n.ts`）：

```typescript
// 删除
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n.use(LanguageDetector).use(initReactI18next).init({
  resources: { en: {...}, es: {...} },
  fallbackLng: 'en',
  detection: { order: ['localStorage', 'navigator'], lookupLocalStorage: 'i18nextLng' },
});
```

### 3.3 路由重构

| 迁移前 | 迁移后 |
|--------|--------|
| `app/page.tsx` | **主应用** `app/[locale]/page.tsx` |
| `app/layout.tsx`（根） | **主应用** `app/layout.tsx`（minimal）+ `app/[locale]/layout.tsx` |
| `app/landing/page.tsx` | **主应用** `app/[locale]/landing/page.tsx` |
| SEO 页在 seo-static / moras-seo 包 | **SEO 子应用** 独立仓库；**主应用** middleware rewrite + `x-moras-locale` |
| Blog / 法务 | **SEO 子应用** `app/blog/`、`app/terms/` 等（en-only，不进 `[locale]`） |
| TVG / Use Cases / Tools / Product | **SEO 子应用** `app/[locale]/...`；**不在**主应用 `app/` 下 |

**根 layout**（`app/layout.tsx`）仅传递 children：

```tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return children;
}
```

### 3.4 localStorage 迁移

`localeDetection: false` 下，语言**仅由 URL**（`/` vs `/es/`）与 **LanguageSwitcher** 决定；next-intl 切换后写入 `NEXT_LOCALE` cookie。

**一次性客户端迁移**（Phase 1 删除 i18next 前，放在主应用 `app/[locale]/layout.tsx` 内的 client 组件，仅运行一次）：

```tsx
'use client';

import { useEffect } from 'react';
import { useRouter } from '@/i18n/navigation';

export function LegacyLocaleRedirect() {
  const router = useRouter();

  useEffect(() => {
    const legacy = localStorage.getItem('i18nextLng');
    if (legacy !== 'es') return;
    localStorage.removeItem('i18nextLng');
    router.replace('/', { locale: 'es' });
  }, [router]);

  return null;
}
```

- 在 en-only 页（Blog/法务）上若 `i18nextLng=es`，用户需先经首页触发上述脚本，或手动访问 `/es/`；**不**生成 `/es/terms` 等。
- middleware **无法**读取 `localStorage`；`?lang=` 兼容见 §2.7、`§7`。

**完成后**：全局搜索确认无 `i18nextLng` 读写；可移除 `LegacyLocaleRedirect`。

### 3.5 内链替换

```tsx
// 迁移前
import Link from 'next/link';
<Link href="/blog">Blog</Link>

// 迁移后
import { Link } from '@/i18n/navigation';
<Link href="/blog">Blog</Link>       // en-only：始终 /blog
<Link href="/terms">Terms</Link>     // en-only：始终 /terms
<Link href="/use-cases">Use cases</Link>  // 西语上下文 → /es/use-cases
```

**全库搜索替换范围**：**主应用** Header/Footer、首页锚点导航；**SEO 子应用** SEO 页正文内链（两仓库分别改）。

---

## 4. SEO 站（52 页）纳入 locale 方案

> **范围**：本节 **§4.2–§4.6** 的实施对象为 **SEO 子应用仓库**（`moras-seo`）。主应用仅参与 §4.1 Phase 0–1 的 sitemap index 聚合与 middleware rewrite（§5）。

### 4.1 策略总览

| Phase | 范围 | 西语 URL | sitemap | hreflang |
|-------|------|---------|---------|----------|
| **Phase 0** | 基础设施 | — | 不变 | — |
| **Phase 1** | SPA 可本地化 2 页（`/`、`/landing`）+ Shell | `/es/`、`/es/landing` | `site-es-sitemap` **2 条** | 仅首页/landing hreflang |
| **Phase 2** | SEO Hub 3 个 + tools | `/es/use-cases`, `/es/tiktok-video-generator`, `/es/product-research` + tools×3 | `seo-es-sitemap.xml` 起始 | Hub hreflang（**不含 Blog / 法务**） |
| **Phase 3** | SEO Vertical 滚动 | `/es/tiktok-video-generator/{slug}`、`/es/use-cases/{persona}` 等 | 按 `status:published` 增量 | 仅已译页 |
| **—** | **Blog + 法务（英语独占）** | 无 `/es/blog*`、`/es/terms` 等 | 仅 `seo-sitemap` 英文条目（法务/Blog 在 SEO 子应用） | **无** hreflang es |

### 4.2 内容模型（SEO 页）

```yaml
# 每篇 SEO 页 / 每个 slug
slug: skincare                    # 跨语言共用
translations:
  en:
    title: "..."
    h1: "..."
    meta_description: "..."
    body: "..."                  # MDX 或 CMS
    status: published
  es:
    title: "..."
    h1: "..."
    meta_description: "..."
    body: "..."
    status: published | draft | missing
```

**规则**：
- `status: missing` → 不生成 `/es/...` 路由、不进 sitemap、不输出 `hreflang="es"`
- `status: draft` → preview only，noindex
- **禁止** 未译页 301 到英文（除非产品明确要求 fallback）

**英语独占例外**：Blog 与法务（`/terms`、`/privacy`、`/subscription`、`/precheck-guidance`）**不在** `translations.es` 模型内。Blog 内容源仅 `content/en/blog/`；法务正文保持英文直至法务审定翻译版。

### 4.3 SEO 子应用改造要点（moras-seo 仓库）

SEO 站为 **独立 Next 应用**，独立部署在 `seo.moras.ai` / `moras-seo` 集群；主域 middleware rewrite 转入。

**i18n 方案（已选定）**：

| 页面类型 | 路由 | locale 来源 |
|----------|------|-------------|
| 可本地化 SEO 页 | `app/[locale]/...` | URL 段 `params.locale`（主 middleware rewrite 带 `/es` 前缀） |
| Blog + 法务 en-only | `app/blog/`、`app/terms/` 等（**不在** `[locale]` 下） | `x-moras-locale` header（主 middleware 恒注入 `en`） |

1. 可本地化页统一 **`app/[locale]/...`** + `setRequestLocale(locale)`；内部直连 SEO 子域时也走同一套路由
2. 静态资源：用户仍访问 `moras.ai/_next/...`（主应用）与 `moras.ai/seo-static/_next/...`（SEO）；ingress 按 path 分流
3. `generateStaticParams` **仅在 SEO 子应用**按 `{ locale, slug }` 组合，仅生成已发布翻译（**Blog 无 locale 维度**）
4. 西语正文来自 SEO 仓库：`content/es/...` 或 CMS `translations.es`；Phase 2 Hub 可先用 `messages/es.json` 翻译 UI shell
5. **`lib/i18n-paths.ts`** 与主应用同源；en-only **301** 在主 middleware，子应用不重复拦截
6. **Root layout**：`app/layout.tsx` pass-through；`<html lang>` 在 `[locale]/layout.tsx`（可本地化页）或 `blog/layout.tsx`（en-only）输出——见 §2.14

### 4.4 Phase 2 Hub 页最小交付

| 路径 | 优先级 | 说明 |
|------|--------|------|
| `/blog` | — | **英语独占**；Header/Footer shell **恒英文**（与正文一致）；选 Español → `/es/` |
| `/es/use-cases` | P0 | Hub |
| `/es/tiktok-video-generator` | P0 | Hub |
| `/es/product-research` | P1 | Product |
| `/es/tools/*` ×3 | P1 | Tools |

### 4.5 英语独占路径策略（Blog + 法务）

Blog、法务与 TVG / Use Cases / Tools 等栏目**刻意区分**：

| 维度 | Blog + 法务 | TVG / Use Cases / Tools / landing 等 |
|------|-------------|--------------------------------------|
| 路径 | `/blog*`、`/terms`、`/privacy`、`/subscription`、`/precheck-guidance` | `/path` + `/es/path` |
| 西语路由 | **不生成**；`/es/...` → **301** 英文 | 按 `status:published` 渐进开放 |
| 正文语言 | **永久英语** | 西语独立正文（或 landing 用 messages） |
| sitemap | 仅英文 sitemap 条目 | `seo-sitemap.xml` + `seo-es-sitemap.xml` |
| hreflang | 仅 `en` + `x-default` | en ↔ es 配对 |
| `x-moras-locale` | 恒 `en` | 随用户 locale |

**实施要点**：
- Blog → **SEO 子应用** `app/blog/`；法务 → **SEO 子应用** `app/terms/` 等；均**不在** `app/[locale]/`，也**不在**主应用 `app/`
- **主应用** middleware：`EN_ONLY_PREFIXES` + `/es/{en-only}` **301**；匹配路径 **rewrite** 至 SEO upstream（非 `next()` 本地渲染）
- 语言切换器在 en-only 页选 Español → **`/es/`**（不生成 `/es/terms` 等）；Switcher 使用共享 `isEnOnlyPath()`
- Footer Connect 区 Terms / Privacy 链始终 `/terms`、`/privacy`（裸路径）
- Blog 正文链 Blog 用裸路径；链可本地化 SEO 页用 locale-aware Link

### 4.6 英语独占页的 Shell 与 layout（SEO 子应用）

Blog 与法务 **物理在 SEO 子应用**。因 `localeDetection: false` 且无 `/es/blog` 等 URL，**Shell 与正文均保持英文**；用户选 Español 时 Switcher 跳转 `/es/`（§2.12）。

| 页面 | 仓库 | layout | `x-moras-locale` | Shell 语言 |
|------|------|--------|------------------|------------|
| `/blog`、`/blog/{slug}` | moras-seo | `app/blog/layout.tsx` | 恒 `en` | **英文** Header/Footer；正文英文 |
| `/terms` 等法务 4 页 | moras-seo | 各页 layout 或共享 `app/(legal)/layout.tsx` | 恒 `en` | **英文** Shell + 英文正文 |

**SEO 子应用 Blog layout 示例**：

```tsx
// moras-seo/app/blog/layout.tsx
import { NextIntlClientProvider } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { LanguageSwitcher } from '@/components/LanguageSwitcher';

export default async function BlogLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // en-only：Shell 与正文均英文；不读 cookie / 不做 Shell 西语化
  const locale = 'en';
  setRequestLocale(locale);
  const messages = await getMessages();

  return (
    <html lang="en">
      <body>
        <NextIntlClientProvider locale={locale} messages={messages}>
          <header>
            <LanguageSwitcher />
          </header>
          {children}
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
```

> **注意**：Blog/法务 **无** `/es/blog`、`/es/terms` URL。hreflang 用 `buildEnOnlyAlternates()`（§2.9）。可本地化 SEO 页的 `<html lang>` 在 `app/[locale]/layout.tsx`（§2.14）。

---

## 5. middleware 与 SEO 子应用转发详解

> **执行位置**：§5.1–§5.2 的 middleware 逻辑在 **主应用**（moras.ai）。§5.4 契约由 **SEO 子应用**消费。

### 5.1 请求流（双域拓扑）

```mermaid
flowchart TD
  User["用户浏览器\nmoras.ai/es/use-cases"]
  Edge["moras.ai\n主应用 Next.js"]
  MW["middleware.ts\nstripLocale · en-only 301"]
  Rewrite["rewrite pathname\n/seo-static/es/use-cases"]
  Ingress["ingress / next.config rewrites\n→ SEO_ORIGIN"]
  SEO["SEO 子应用 Next.js\nseo.moras.ai / moras-seo"]
  Header["x-moras-locale: es"]
  Render["app/[locale]/use-cases/page.tsx"]
  SPA["主应用 app/[locale]/page.tsx\n仅 / 与 /landing"]

  User --> Edge --> MW
  MW -->|"/" 或 "/landing"| SPA
  MW -->|"Blog/TVG/法务等"| Rewrite --> Ingress --> SEO
  MW -->|"注入 header"| Header --> SEO --> Render
```

**英文 Blog 示例**：`moras.ai/blog/foo` → middleware rewrite `/seo-static/blog/foo` → SEO 子应用 `app/blog/[slug]/page.tsx`，`x-moras-locale: en`。

**西语 TVG 示例**：`moras.ai/es/tiktok-video-generator/skincare` → rewrite `/seo-static/es/tiktok-video-generator/skincare` → SEO 子应用 `app/[locale]/tiktok-video-generator/[slug]/page.tsx`。

**首页示例**：`moras.ai/es/` → **不** rewrite；主应用 next-intl → `app/[locale]/page.tsx`。

### 5.2 路径分类

| 用户 URL | 主应用 middleware 动作 | 内部 rewrite 路径 | 渲染方 |
|----------|------------------------|-------------------|--------|
| `/blog` | rewrite | `/seo-static/blog`（`x-moras-locale: en`） | SEO 子应用 |
| `/blog/{slug}` | rewrite | `/seo-static/blog/{slug}` | SEO 子应用 |
| `/es/blog` | **301** | — | 重定向至 `/blog` |
| `/es/blog/{slug}` | **301** | — | 重定向至 `/blog/{slug}` |
| `/terms` | rewrite | `/seo-static/terms`（`x-moras-locale: en`） | SEO 子应用 |
| `/es/terms` | **301** | — | `/terms` |
| `/privacy` | rewrite | `/seo-static/privacy` | SEO 子应用 |
| `/es/privacy` | **301** | — | `/privacy` |
| `/precheck-guidance` | rewrite | `/seo-static/precheck-guidance` | SEO 子应用 |
| `/es/precheck-guidance` | **301** | — | `/precheck-guidance` |
| `/subscription` | rewrite | `/seo-static/subscription` | SEO 子应用 |
| `/es/subscription` | **301** | — | `/subscription` |
| `/use-cases` | rewrite | `/seo-static/use-cases` | SEO 子应用 |
| `/es/use-cases` | rewrite | `/seo-static/es/use-cases` | SEO 子应用 |
| `/` | intl middleware → `[locale]=en` | — | **主应用** |
| `/es/` | intl middleware → `[locale]=es` | — | **主应用** |
| `/landing` | intl middleware | — | **主应用** |
| `/en/blog` | **301**（防御性） | — | `/blog` |
| `/?lang=es` | **308** | — | `/es/` 或 `/es{path}` |
| `/?lang=en` | **308** | — | `/` 或 `{path}`（去 query） |

### 5.3 `_next` 静态资源

| 请求 | 处理 |
|------|------|
| `/_next/static/...` | 主应用资源；middleware **跳过** |
| `/seo-static/_next/static/...` | SEO 子应用资源；ingress 转发至 SEO 服务 |
| 西语 SEO 页引用的 JS/CSS | 必须 200；验证「西语页无样式」类问题 |

### 5.4 与子应用契约

主应用 middleware 通过 **rewrite 路径中的 `/es` 段** 传递 locale（可本地化页），并通过 header 传递 en-only 页的固定 locale：

```
x-moras-locale: es | en   # Blog/法务恒 en；可本地化页与 URL 段一致
```

SEO 子应用 **可本地化页** — locale 来自 `params.locale`（推荐，与 rewrite `/seo-static/es/...` 对齐）：

```typescript
// moras-seo/app/[locale]/layout.tsx
import { hasLocale } from 'next-intl';
import { setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import { routing } from '@/i18n/routing';

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  // ...
}
```

SEO 子应用 **Blog/法务** — 不经过 `[locale]`；layout 固定 `locale = 'en'`（§4.6），header 仅作 staging 直连调试。

**两仓库对齐检查清单**：
- [ ] `SEO_PATH_PREFIXES`（主）与 SEO 子应用 `app/` 路由一致
- [ ] `EN_ONLY_PREFIXES` 两边 `lib/i18n-paths.ts` 一致
- [ ] SEO 子应用 staging 可独立访问（内部 URL）且经主域 rewrite 200
- [ ] `/_next` 与 `/seo-static/_next` ingress 规则已配置

---

## 6. Sitemap 更新规则

> **分工**：`site-sitemap.xml` / `site-es-sitemap.xml` 由 **主应用**生成；`seo-sitemap.xml` / `seo-es-sitemap.xml` 由 **SEO 子应用**生成；主应用 `sitemap.xml` index **聚合**四者。

**跨应用 URL 登记**：法务 4 页（`/terms` 等）**物理在 SEO 子应用**，但 URL 属于「站点静态页」，由 **主应用 `site-sitemap.ts` 硬编码** 4 条英文 URL（与现网 `site-sitemap.xml` 一致），**不**指望 SEO 子应用 sitemap 产出这 4 条。Blog 20 页仅在 **`seo-sitemap.xml`**（SEO 子应用）。

### 6.1 当前结构

```
/sitemap.xml          → index
  ├── site-sitemap.xml    → 6 条：/、/landing + 法务 4 页（主应用登记；法务由 SEO 渲染）
  └── seo-sitemap.xml     → 46 条：Product + Tools + Use Cases + TVG + Blog（SEO 子应用）
```

### 6.2 目标结构

```
/sitemap.xml
  ├── site-sitemap.xml        → 英文：/、/landing + 法务 4 页（**主应用** hardcode；法务页 SEO 渲染）
  ├── site-es-sitemap.xml     → 西语 SPA（**仅** `/es/`、`/es/landing`）
  ├── seo-sitemap.xml         → 英文 SEO 46 页（**SEO 子应用**）
  └── seo-es-sitemap.xml      → 西语 SEO（Phase 2+ 增量；**不含 Blog / 法务**）
```

### 6.3 生成规则

```typescript
// app/sitemap.ts 伪代码
const BASE = 'https://moras.ai';

function enEntry(path: string) {
  return { url: `${BASE}${path}`, alternates: { languages: {...} } };
}

function esEntry(path: string) {
  const esPath = path === '/' ? '/es' : `/es${path}`;
  return { url: `${BASE}${esPath}`, alternates: { languages: {...} } };
}

// 规则
// 1. 禁止出现 https://moras.ai/en/...（历史无 /en/ URL；防 next-intl 误配）
// 2. x-default 始终指向英文根 URL
// 3. seo-es-sitemap 仅含 hasEsTranslation === true 的 slug（**排除 Blog / 法务**）
// 4. 未译西语页不得出现在任何 sitemap
// 5. Blog + 法务：仅 seo-sitemap / site-sitemap 英文条目；不进 site-es / seo-es
// 6. site-sitemap 中法务 4 URL 由主应用 hardcode（页面由 SEO 子应用渲染）
```

### 6.4 示例条目

```xml
<!-- site-es-sitemap.xml — 仅可本地化 SPA -->
<url>
  <loc>https://moras.ai/es</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://moras.ai"/>
  <xhtml:link rel="alternate" hreflang="es" href="https://moras.ai/es"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://moras.ai"/>
</url>
<url>
  <loc>https://moras.ai/es/landing</loc>
  ...
</url>

<!-- site-sitemap.xml — 法务仅英文，无 es alternate -->
<url>
  <loc>https://moras.ai/terms</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://moras.ai/terms"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://moras.ai/terms"/>
</url>

<!-- seo-sitemap.xml — Blog 仅英文，无 es alternate -->
<url>
  <loc>https://moras.ai/blog/my-slug</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://moras.ai/blog/my-slug"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://moras.ai/blog/my-slug"/>
</url>
```

---

## 7. 防御性 /en/ 拦截（历史上无此 URL）

> Moras **从未**对外使用 `/en/` 前缀 URL。本节规则为**预防性**：防止 next-intl 误生成、爬虫误链、开发误配导致 `/en/` 被索引或与无前缀 canonical 重复。若请求误入 `/en/*`，**301 去前缀**至英文 canonical；**不是**历史 URL 迁移任务。

| 误入 URL（预防性拦截） | 状态码 | 目标 |
|------------------------|--------|------|
| `/en` | 301 | `/` |
| `/en/` | 301 | `/` |
| `/en/blog` | 301 | `/blog` |
| `/en/blog/{slug}` | 301 | `/blog/{slug}` |
| `/en/tiktok-video-generator/{slug}` | 301 | `/tiktok-video-generator/{slug}` |
| `/en/{any}` | 301 | `/{any}`（去掉 `/en` 前缀） |

**禁止** 对 `/es/...` 做重定向（**例外**：英语独占路径 `/es/blog*`、`/es/terms`、`/es/privacy`、`/es/subscription`、`/es/precheck-guidance` → **301** 英文 canonical，见 §4.5、§5.2）。

**兼容**：

| 旧 URL | 状态码 | 目标 |
|--------|--------|------|
| `/?lang=es` | 308 | `/es/` 或 `/es{path}` |
| `/?lang=en` | 308 | `/` 或 `{path}`（去掉 query） |

---

## 8. 分阶段任务清单（Agent 可执行）

> 格式：**任务 ID** | 操作 | 文件/路径 | 验收标准 | 依赖  
> **仓库列**：`[MAIN]` = moras.ai 主应用 · `[SEO]` = moras-seo 子应用

---

### Phase 0 — 基础设施

#### [MAIN] 主应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P0-M01 | 创建 feature 分支 `feat/i18n-next-intl` | git | 分支存在 | — |
| P0-M02 | `npm install next-intl` | `package.json` | 依赖已添加 | P0-M01 |
| P0-M03 | 创建 `i18n/routing.ts`, `request.ts`, `navigation.ts` | `i18n/*` | `localeDetection: false` | P0-M02 |
| P0-M04 | 配置 `next.config.ts` plugin + SEO rewrites | `next.config.ts` | `next build` 通过；`/seo-static/*` → SEO_ORIGIN | P0-M03 |
| P0-M05 | 创建 `messages/en.json`, `messages/es.json`（从 i18next 抽取，**仅首页 shell**） | `messages/*` | 键覆盖 common/home/landing | P0-M02 |
| P0-M06 | 创建 `app/[locale]/layout.tsx` | `app/[locale]/layout.tsx` | `/` 200 英文 SSR | P0-M03, P0-M05 |
| P0-M07 | 迁移 `app/page.tsx` → `app/[locale]/page.tsx` | `app/[locale]/page.tsx` | 首页文案正确 | P0-M06 |
| P0-M08 | 实现 `middleware.ts`（next-intl、SEO rewrite、`?lang=` 308、en-only 301、防御性 `/en/*`） | `middleware.ts` | §9.1 用例 1–4、6–8、6b 通过 | P0-M03, P0-S02 |
| P0-M09 | 实现 `LanguageSwitcher` + `lib/i18n-paths.ts` | `components/**`, `lib/i18n-paths.ts` | `/` ↔ `/es/` 切换 URL 变 | P0-M07, P0-M08 |
| P0-M10 | 创建 `lib/metadata.ts` | `lib/metadata.ts` | 首页 view-source 含 hreflang | P0-M07 |
| P0-M11 | staging 部署 | CI/CD | preview URL 可访问 | P0-M09 |

#### [SEO] SEO 子应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P0-S01 | 确认 SEO 仓库路径与 `SEO_ORIGIN` 环境变量 | DevOps | staging 内部 URL 文档化 | — |
| P0-S02 | 同步 `lib/i18n-paths.ts`（与 MAIN 同源或 monorepo） | `lib/i18n-paths.ts` | `EN_ONLY_PREFIXES` 一致 | P0-S01 |
| P0-S03 | 落地 `app/[locale]/layout.tsx` + Blog/法务 layout（§2.14、§4.6） | `app/**/layout.tsx` | 可本地化页 `lang` 正确；Blog `lang=en` | P0-S02 |
| P0-S04 | staging 独立部署 SEO 子应用 | CI/CD | 内部 URL `/blog` 200 | P0-S03 |

**Phase 0 完成门控**：英文 URL 与线上一致；`/es/` 可访问；`/blog` 经主域 rewrite 200；i18next **仍可并存**（未删除）。

---

### Phase 1 — SPA 可本地化页 + 移除 i18next

#### [MAIN] 主应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P1-M01 | 迁移 `landing` 至 `[locale]` | `app/[locale]/landing/` | `/`、`/landing` ×2 语言 200 | P0-M11 |
| P1-M02 | 替换首页/landing 内链为 `@/i18n/navigation` | `components/**` | Footer 链 SEO 页用 locale-aware Link | P1-M01 |
| P1-M03 | 删除 i18next 初始化与 Provider | 原 `lib/i18n.ts`, `layout.tsx` | 无 i18next import | P1-M01 |
| P1-M04 | `npm uninstall i18next react-i18next i18next-browser-languagedetector` | `package.json` | 包已移除 | P1-M03 |
| P1-M05 | 更新 `site-es-sitemap.xml` + 主应用 hardcode 法务 4 URL | `app/sitemap.ts` | **2 条** es SPA + site 含 terms 等 4 条 | P1-M01 |
| P1-M06 | 移除 `localStorage.i18nextLng`；加入 `LegacyLocaleRedirect`（§3.4） | `components/**` | 无 i18nextLng 读写；legacy es 跳 `/es/` | P1-M04 |

#### [SEO] SEO 子应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P1-S01 | Blog/法务 layout（Shell 恒英文）+ `buildEnOnlyAlternates` | `app/blog/`, `app/terms/` 等 | §4.6；hreflang 无 es | P0-S04 |
| P1-S02 | SEO Header/Footer 使用共享 `isEnOnlyPath` Switcher | `components/LanguageSwitcher.tsx` | `/terms` 选 Español → `/es/` | P1-S01 |
| P1-S03 | 确认法务 4 页 rewrite 200（不经主应用本地渲染） | — | `/terms` 等 200 | P0-M08 |

**Phase 1 完成门控**：`/`、`/landing` hreflang 完整；法务 en-only 无 `/es/terms`；主应用 bundle 不含 i18next；Blog/法务在 SEO 仓库可访问。

---

### Phase 2 — SEO Hub 页西语

> middleware 全量 rewrite 与 en-only 301 已在 **Phase 0（P0-M08）** 实现；本 Phase 聚焦 SEO 子应用 Hub 西语内容与 sitemap。

#### [MAIN] 主应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P2-M01 | 回归 middleware：Hub 西语 rewrite + en-only 301 | `middleware.ts` | `/es/use-cases` rewrite 200；`/es/blog` **301** | P1-M06 |
| P2-M02 | sitemap index 聚合 `seo-es-sitemap.xml` | `app/sitemap.ts` | index 含 seo-es 入口 | P2-S04 |

#### [SEO] SEO 子应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P2-S01 | Hub 路由 + `messages/es.json` shell | `app/[locale]/use-cases/` 等 | 西语 Hub UI 正确 | P2-M01 |
| P2-S02 | 上线 Hub：`/es/use-cases`, `/es/tiktok-video-generator` | `content/es/` 或 CMS | 2 Hub 200（经主域 URL） | P2-S01 |
| P2-S03 | 上线 `/es/product-research` + 3 tools | `app/[locale]/` | 4 页 200 | P2-S01 |
| P2-S04 | 创建 `seo-es-sitemap.xml` | `app/sitemap.ts` | 仅含已发布 es Hub | P2-S02, P2-S03 |
| P2-S05 | 内链：Footer/Header locale-aware Link | SEO 组件 | 西语页链 `/es/...` | P2-S02 |

**Phase 2 完成门控**：全站 52 英文 URL 不变；6 个西语 Hub 可访问（**不含** `/es/blog`）；Blog `/es/*` 均 301 至英文。

---

### Phase 3 — SEO Vertical 滚动（TikTok Video Generator + Use Cases）

#### [SEO] SEO 子应用（主应用无正文任务）

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P3-S01 | 建立 `translations` 状态登记 | `content/i18n-registry.json` | 含 TVG/Use Cases slug（**不含 Blog / 法务**） | P2-S05 |
| P3-S02 | 翻译 TVG 15 vertical（批次 5+5+5） | `content/es/tiktok-video-generator/` | 每批 sitemap 增量 | P3-S01 |
| P3-S03 | 翻译 Use Cases 5 vertical | `content/es/use-cases/` | 5 页 200 | P3-S01 |
| P3-S04 | `generateStaticParams` 过滤 `status !== published` | SEO `[locale]/**/page.tsx` | 未译 slug 西语 404 | P3-S02 |
| P3-S05 | 更新 `seo-es-sitemap.xml` | `app/sitemap.ts` | 与 registry 一致 | P3-S02, P3-S03 |

#### [MAIN] 主应用

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P3-M01 | 确认 sitemap index 拉取最新 seo-es | `app/sitemap.ts` | 与 P3-S05 一致 | P3-S05 |

---

### ~~Phase 4 — Blog 滚动~~（已取消）

Blog **不做多语种**，无西语翻译任务。Phase 3 完成后 i18n SEO 滚动即告段落；Blog 维持 `seo-sitemap.xml` 英文条目即可。

---

## 9. 测试清单

### 9.1 手动测试（必做）

| # | 用例 | 步骤 | 期望 |
|---|------|------|------|
| 1 | 英文首页 | 访问 `/` | 200；`<html lang="en">`；URL 不变 |
| 2 | 西语首页 | 访问 `/es/` | 200；`<html lang="es">`；西语文案 |
| 3 | 语言切换 | `/` 选 Español | 跳转 `/es/`，非 localStorage |
| 4 | 语言切换 | `/terms` 选 Español | 跳转 `/es/`（法务无西语 URL） |
| 4b | en-only 301 | 访问 `/es/blog`、`/es/terms`、`/es/blog/{slug}`、`/es/privacy` | **301 → 英文 canonical** |
| 5 | 防御性 /en/ 拦截 | 访问 `/en/blog` | 301 → `/blog`（冒烟；历史无 `/en/`） |
| 6 | ?lang=es | 访问 `/?lang=es` | 308 → `/es/` |
| 6b | ?lang=en | 访问 `/es/?lang=en` 或 `/use-cases?lang=en` | 308 → 去 query 的英文 path |
| 7 | SEO 英文 | 访问 `/blog/tiktok-video-hooks` | 200；英文 |
| 8 | SEO 西语 Hub | 访问 `/es/use-cases` | 200；西语 shell |
| 9 | 未译西语 | 访问 `/es/tiktok-video-generator/{未译slug}` | **404**（非 fallback 英文） |
| 10 | hreflang | view-source `/blog`、`/terms` | 仅 en、x-default；**无** hreflang="es" |
| 10b | localeDetection | 西语浏览器直接访问 `/` | **200 英文**，不自动跳 `/es/` |
| 11 | canonical | view-source `/es/` | canonical=`https://moras.ai/es` |
| 12 | sitemap | 访问 `/sitemap.xml` | 含 site-es、seo-es index |
| 13 | 静态资源 | 西语 SEO 页 Network | `/_next/*` 或 `/seo-static/_next/*` 全 200 |
| 14 | 旧 i18next | Application → LocalStorage | 切换语言不依赖 `i18nextLng` |
| 15 | 内链 | 西语页 Footer | 链至 `/es/product-research` 等 |

### 9.2 可选自动化

```typescript
// tests/i18n-routing.spec.ts (Playwright 示例)
import { test, expect } from '@playwright/test';

test('en home at root', async ({ page }) => {
  await page.goto('https://staging.moras.ai/');
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page).toHaveURL(/\/$/);
});

// 防御性 /en/ 拦截冒烟（历史无 /en/ URL）
test('/en/* 301 去前缀', async ({ request }) => {
  const res = await request.get('https://staging.moras.ai/en/blog', {
    maxRedirects: 0,
  });
  expect(res.status()).toBe(301);
  expect(res.headers()['location']).toContain('/blog');
});

test('language switcher changes URL', async ({ page }) => {
  await page.goto('https://staging.moras.ai/');
  await page.selectOption('select', 'es');
  await expect(page).toHaveURL(/\/es\/?$/);
});
```

```bash
# curl 冒烟脚本（/en/ 为防御性拦截，历史无此 URL）
curl -sI https://moras.ai/en/blog | grep -i "301\|location"   # 防御性 /en/ 拦截
curl -sI "https://moras.ai/?lang=es" | grep -i "308\|location"
curl -sI "https://moras.ai/es/?lang=en" | grep -i "308\|location"
curl -sI https://moras.ai/es/blog | grep -i "301\|location"
curl -sI https://moras.ai/es/terms | grep -i "301\|location"
curl -sI https://moras.ai/es | grep "200"
```

---

## 10. Rollback 方案

### 10.1 触发条件

- 英文核心 URL（`/`, `/blog` 等）非 200
- 防御性 `/en/*` 拦截未生效，next-intl 或误配产生 `/en/` canonical 导致 duplicate content
- SEO 子应用 rewrite 失败大面积 502/404
- 西语页错误 fallback 英文且被 Google 判 duplicate

### 10.2 回滚步骤

| 步骤 | 操作 | 负责人 |
|------|------|--------|
| R1 | 在 Vercel/CI **立即 promote 上一稳定 deployment** | DevOps |
| R2 | 若已合并 main，执行 `git revert` 迁移 PR | Dev |
| R3 | 确认 `middleware.ts` 恢复为迁移前版本（仅 seo-static 转发，无 next-intl） | Dev |
| R4 | 确认 i18next 依赖恢复（若已卸载则 `npm i i18next react-i18next`） | Dev |
| R5 | 验证 `/`、`/blog` 200；语言切换回 localStorage 模式 | QA |
| R6 | 在 GSC 提交「未变更」或撤销新 sitemap（若已推送） | SEO |
| R7 | 记录 incident：失败 Phase、根因、重试计划 | PM |

### 10.3 部分回滚（仅 SEO 西语）

若 SPA 迁移成功但 SEO 西语有问题：

1. 关闭 `seo-es-sitemap.xml` index 入口
2. middleware 对 `/es/use-cases` 等西语 SEO 路径返回 **404** 或临时 302 → 英文（302 仅应急，≤48h）；Blog / 法务本即 **301 → 英文**，无需额外处理
3. 保留 SPA `/es/` 与 next-intl 基础设施

### 10.4 备份清单（Phase 0 前必须做）

- [ ] 迁移前 `main` tag：`pre-i18n-routing-YYYYMMDD`
- [ ] 导出当前 `messages`（从 bundle 提取的 en/es JSON）
- [ ] 保存当前 `middleware.ts`、`next.config.ts` 副本
- [ ] 记录当前 `sitemap.xml` 全量 URL 列表

---

## 11. 风险与规避

| 风险 | 规避 |
|------|------|
| `/` 与 `/en/` duplicate | 防止 next-intl 或误配产生 `/en/` canonical；防御性 `/en/*` 301；sitemap / 内链不含 `/en/` |
| SEO rewrite 丢 locale | `buildSeoInternalPath` 单元测试；staging 全路径抽检 |
| 未译页被索引 | 404 + 不进 sitemap + 无 hreflang es |
| Blog / 法务误开西语 URL | `EN_ONLY_PREFIXES` + `/es/*` 301；sitemap 不含 es 条目 |
| 内链漏改 | ESLint：可本地化路径禁止裸 `href`；**Blog / 法务允许裸路径** |
| 浏览器语言误跳西语 | **`localeDetection: false`**（已默认） |
| 双应用 `_next` 冲突 | ingress 规则分 path 转发 |

---

## 12. 进度跟踪表（实施时填写）

| Phase | 范围 | 状态 | 完成日期 |
|-------|------|------|----------|
| 0 | 基础设施 | Pending | — |
| 1 | SPA + 移除 i18next | Pending | — |
| 2 | SEO Hub 西语 | Pending | — |
| 3 | TVG + Use Cases vertical | Pending | — |
| — | Blog + 法务（英语独占） | N/A | — |

**西语已发布 slug 登记**：（随 Phase 3 填写，同步 `content/i18n-registry.json`；**不含 Blog / 法务**）

---

## 13. 参考

- 站点 IA：[moras-site-structure.md](./moras-site-structure.md)
- 线上 sitemap：[moras.ai/sitemap.xml](https://moras.ai/sitemap.xml)
- next-intl 文档：[next-intl.dev](https://next-intl.dev/docs/getting-started/app-router)

---

*Demo 执行文档 · 实施前需与 Moras 工程团队确认 **SEO 子应用仓库路径**、`SEO_ORIGIN` 与 ingress 配置。主应用与 SEO 子应用 **分仓库发版**，勿假设单仓库 `generateStaticParams` 覆盖 52 页。*
