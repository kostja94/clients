# Vofy i18n 修复方案：Cookie 强制跳转 + 缺失翻译 + 语言切换器

---

## 第一部分：人类可读 · 问题与方案概述

### 背景

Vofy.art 当前支持英文（`/`）和西班牙语（`/es`），基于 Next.js + Vercel 部署。通过读取页面 HTML 源码和 HTTP 响应头，发现以下 **4 个需要修复的问题**：

### 问题清单

| # | 问题 | 严重度 | 影响 |
|---|------|--------|------|
| 1 | **Cookie 强制跳转**：用户访问 `/es` 后即使手动改 URL 为 `/`，中间件读取 `vofy_locale=es` 后也会 302 跳回 `/es` | 🔴 高 | 用户被困在某个语言版本，无法自主切换 |
| 2 | **西语 `<title>` 未翻译**：`/es` 的 `<title>` 仍为 `Vofy — Your All-in-One AI Creative Studio`（英文） | 🔴 高 | 搜索引擎 SERP 中西语结果标题与内容语言不匹配 |
| 3 | **西语 `og:title` 未翻译**：与社会化分享卡片标题语言不匹配 | 🟡 中 | 社交分享点击率下降 |
| 4 | **无语言切换器**：侧边栏无任何语言切换入口 | 🟡 中 | 用户只能手动改 URL（但又被 Cookie 跳转阻挡） |

> 注：hreflang、canonical、`twitter:title` 西语翻译均已正确完成，sitemap.xml 也已标注 hreflang。以上 4 个问题是仅存的缺口。

---

### 修复方案概览

#### 方案 1：取消 Cookie 强制跳转（中间件修改）

**当前逻辑（有问题的）：**
```
访问 /es → Set-Cookie: vofy_locale=es → 手动改 / → 读 Cookie es → 302 跳 /es → 死循环
```

**修复后逻辑：**
```
URL 路径优先级 > Cookie > Accept-Language > 默认英文
```

即：当 URL 路径已经有 locale 前缀时，**用路径覆盖 Cookie，不做跳转**。当 URL 无前缀时，才用 Cookie 引导一次。

#### 方案 2：补上西语 title 和 og:title

从已有的 `twitter:title` 翻译资源 `Vofy - Tu estudio creativo de IA todo en uno` 可知翻译已存在，只需在 `generateMetadata()` 中对 `<title>` 和 `og:title` 也应用即可。

#### 方案 3：添加语言切换器 UI

在侧边栏 `<aside>` 底部添加下拉或按钮形式的语言切换组件。

---

### 实现步骤

1. 修改 `middleware.ts` 中的 Cookie 跳转逻辑（URL 优先）
2. 在 `generateMetadata()` 中为 `es` locale 设置正确的 title 和 og:title
3. 编写 `LanguageSwitcher` 组件并嵌入侧边栏
4. 部署验证

---

---

## 第二部分：Agent 可读 · 实现代码

> 以下代码供 Agent 直接实现，所有文件路径和代码块均为自包含。

### 基础数据

```json
{
  "site_url": "https://www.vofy.art",
  "locales": ["en", "es"],
  "default_locale": "en",
  "cookie_name": "vofy_locale",
  "cookie_max_age": 31536000,
  "framework": "Next.js (App Router)",
  "deployment": "Vercel",
  "i18n_strategy": "sub-path routing (/ → en, /es → es)"
}
```

### 当前 HTTP 响应头（已确认）

```
# 访问 / 时：
Set-Cookie: vofy_locale=en; Path=/; Expires=Tue, 29 Jun 2027...; Max-Age=31536000; SameSite=lax

# 访问 /es 时：
Set-Cookie: vofy_locale=es; Path=/; Expires=Tue, 29 Jun 2027...; Max-Age=31536000; SameSite=lax
```

### 当前页面 `<head>` 现状（已确认）

**英文 `/`：**
```html
<html lang="en">
<title>Vofy — Your All-in-One AI Creative Studio</title>
<meta name="description" content="Try fresh viral-style image and video effects..." />
<link rel="canonical" href="https://www.vofy.art" />
<link rel="alternate" hrefLang="en" href="https://www.vofy.art" />
<link rel="alternate" hrefLang="es" href="https://www.vofy.art/es" />
<link rel="alternate" hrefLang="x-default" href="https://www.vofy.art" />
<meta property="og:title" content="Vofy — Your All-in-One AI Creative Studio" />
<meta property="og:description" content="Try fresh viral-style..." />
<meta property="og:url" content="https://www.vofy.art" />
<meta name="twitter:title" content="Vofy - Your All-in-One AI Creative Studio" />
<meta name="twitter:description" content="Try fresh viral-style..." />
<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Organization","name":"Vofy","url":"https://www.vofy.art/","logo":"...","description":"Your All-in-One AI Creative Studio...","sameAs":["..."]}
</script>
<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"WebSite","name":"Vofy","url":"https://www.vofy.art/","description":"Generate videos, images, and more..."}
</script>
```

**西班牙语 `/es`：**
```html
<html lang="es">
<title>Vofy — Your All-in-One AI Creative Studio</title>                    ← ❌ 未翻译
<meta name="description" content="Prueba efectos de imagen y video..." />   ← ✅ 已翻译
<link rel="canonical" href="https://www.vofy.art/es" />
<link rel="alternate" hrefLang="en" href="https://www.vofy.art" />
<link rel="alternate" hrefLang="es" href="https://www.vofy.art/es" />
<link rel="alternate" hrefLang="x-default" href="https://www.vofy.art" />
<meta property="og:title" content="Vofy — Your All-in-One AI Creative Studio" />  ← ❌ 未翻译
<meta property="og:description" content="Prueba efectos de imagen y video..." />   ← ✅ 已翻译
<meta property="og:url" content="https://www.vofy.art/es" />
<meta name="twitter:title" content="Vofy - Tu estudio creativo de IA todo en uno" /> ← ✅ 已翻译（翻译资源存在）
<meta name="twitter:description" content="Prueba efectos de imagen y video..." />
<!-- Schema.org 仍未本地化：url 指向 / 而非 /es，description 为英文 -->
```

### 翻译词典

```json
{
  "en": {
    "title": "Vofy — Your All-in-One AI Creative Studio",
    "title_short": "Vofy - Your All-in-One AI Creative Studio",
    "description": "Try fresh viral-style image and video effects, made to share with friends and followers, powered by the latest AI models.",
    "schema_description": "Generate videos, images, and more with state-of-the-art AI models. All in one place.",
    "lang_label": "English"
  },
  "es": {
    "title": "Vofy — Tu estudio creativo de IA todo en uno",
    "title_short": "Vofy - Tu estudio creativo de IA todo en uno",
    "description": "Prueba efectos de imagen y video con estilo viral, listos para compartir con amigos y seguidores, impulsados por los modelos de IA más recientes.",
    "schema_description": "Genera videos, imágenes y más con los modelos de IA más avanzados. Todo en un solo lugar.",
    "lang_label": "Español"
  }
}
```

---

### 修改 1：`middleware.ts` — Cookie 跳转逻辑修复

**文件路径：** `src/middleware.ts` 或项目根目录 `middleware.ts`

```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const LOCALES = ['en', 'es'] as const;
const DEFAULT_LOCALE = 'en';
const COOKIE_NAME = 'vofy_locale';
const COOKIE_MAX_AGE = 31536000; // 1 year in seconds

type Locale = (typeof LOCALES)[number];

function getLocaleFromPath(pathname: string): Locale | null {
  const segment = pathname.split('/')[1];
  return LOCALES.includes(segment as Locale) ? (segment as Locale) : null;
}

function detectLocaleFromAcceptLanguage(header: string): Locale | null {
  if (!header) return null;
  // Parse the first language code from Accept-Language
  // e.g. "es-ES,es;q=0.9,en;q=0.8" → "es"
  const first = header.split(',')[0];
  if (!first) return null;
  const lang = first.split(';')[0].trim().split('-')[0].toLowerCase();
  return LOCALES.includes(lang as Locale) ? (lang as Locale) : null;
}

function setLocaleCookie(response: NextResponse, locale: Locale): void {
  response.cookies.set(COOKIE_NAME, locale, {
    path: '/',
    maxAge: COOKIE_MAX_AGE,
    sameSite: 'lax',
    secure: process.env.NODE_ENV === 'production',
  });
}

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Skip internal paths
  if (
    pathname.startsWith('/_next') ||
    pathname.startsWith('/api') ||
    pathname.startsWith('/images') ||
    pathname.startsWith('/favicon') ||
    /\.(ico|png|jpg|jpeg|svg|css|js|json|xml|txt|webp|woff2?)$/.test(pathname)
  ) {
    return NextResponse.next();
  }

  const pathLocale = getLocaleFromPath(pathname);

  // Case 1: Path already has a locale prefix (e.g. /es/ai-image-generate)
  // → Sync cookie to match the path (not the other way around)
  if (pathLocale) {
    const response = NextResponse.next();
    setLocaleCookie(response, pathLocale);
    return response;
  }

  // Case 2: No locale prefix (e.g. /, /ai-image-generate)
  // → Check cookie first
  const cookieLocale = request.cookies.get(COOKIE_NAME)?.value as Locale | undefined;

  if (cookieLocale && LOCALES.includes(cookieLocale) && cookieLocale !== DEFAULT_LOCALE) {
    // Cookie says non-default → redirect to locale path (one-time)
    const newUrl = new URL(`/${cookieLocale}${pathname === '/' ? '' : pathname}`, request.url);
    const response = NextResponse.redirect(newUrl);
    // Re-set cookie on redirect to ensure expiry is refreshed
    setLocaleCookie(response, cookieLocale);
    return response;
  }

  // Case 3: Check Accept-Language header for first-time visitors
  const acceptLang = request.headers.get('accept-language') || '';
  const browserLocale = detectLocaleFromAcceptLanguage(acceptLang);

  if (browserLocale && browserLocale !== DEFAULT_LOCALE) {
    const newUrl = new URL(`/${browserLocale}${pathname === '/' ? '' : pathname}`, request.url);
    const response = NextResponse.redirect(newUrl);
    setLocaleCookie(response, browserLocale);
    return response;
  }

  // Case 4: Default — serve English without redirect
  const response = NextResponse.next();
  setLocaleCookie(response, DEFAULT_LOCALE);
  return response;
}

export const config = {
  // Match all paths except excluded ones
  matcher: ['/((?!_next|api|images|favicon|sitemap|robots|icon|apple-icon).*)'],
};
```

**核心变更说明：**

- **旧逻辑**：Cookie `vofy_locale` 在无路径前缀时覆盖一切，导致用户被困
- **新逻辑**：
  - `pathLocale !== null`（路径已有 `/es`）→ 用路径同步 Cookie，**不做任何跳转**
  - `pathLocale === null`（路径无前缀如 `/`）
    - Cookie 有值且非默认 → 跳转一次到对应路径（仅此一次）
    - Cookie 无值/默认 → 检查 Accept-Language → 匹配则跳转
    - 都不满足 → 英文默认，不跳转
- 当用户通过 UI 切换到英文后，Cookie 被更新为 `en`，之后再访问 `/` 就不跳转了

---

### 修改 2：`generateMetadata()` — 补上西语 title/og:title

**文件路径：** `src/app/[locale]/layout.tsx` 或 `src/app/[locale]/page.tsx`

```typescript
import type { Metadata } from 'next';

const TRANSLATIONS: Record<string, {
  title: string;
  titleShort: string;
  description: string;
  schemaDescription: string;
}> = {
  en: {
    title: 'Vofy — Your All-in-One AI Creative Studio',
    titleShort: 'Vofy - Your All-in-One AI Creative Studio',
    description:
      'Try fresh viral-style image and video effects, made to share with friends and followers, powered by the latest AI models.',
    schemaDescription:
      'Generate videos, images, and more with state-of-the-art AI models. All in one place.',
  },
  es: {
    title: 'Vofy — Tu estudio creativo de IA todo en uno',
    titleShort: 'Vofy - Tu estudio creativo de IA todo en uno',
    description:
      'Prueba efectos de imagen y video con estilo viral, listos para compartir con amigos y seguidores, impulsados por los modelos de IA más recientes.',
    schemaDescription:
      'Genera videos, imágenes y más con los modelos de IA más avanzados. Todo en un solo lugar.',
  },
};

const BASE_URL = 'https://www.vofy.art';

function getUrl(locale: string, path: string = ''): string {
  const base = locale === 'en' ? BASE_URL : `${BASE_URL}/${locale}`;
  return path ? `${base}${path}` : base;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const t = TRANSLATIONS[locale] ?? TRANSLATIONS.en;

  return {
    title: t.title,
    description: t.description,
    metadataBase: new URL(BASE_URL),
    alternates: {
      canonical: getUrl(locale),
      languages: {
        en: getUrl('en'),
        es: getUrl('es'),
        'x-default': getUrl('en'),
      },
    },
    openGraph: {
      title: t.title,
      description: t.description,
      url: getUrl(locale),
      siteName: 'Vofy',
      type: 'website',
    },
    twitter: {
      card: 'summary_large_image',
      title: t.titleShort,
      description: t.description,
    },
  };
}
```

**额外需要：在 `<head>` 中注入 Schema.org JSON-LD（已本地化）**

在 `layout.tsx` 中：

```typescript
export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const t = TRANSLATIONS[locale] ?? TRANSLATIONS.en;
  const currentUrl = getUrl(locale);

  const webSiteSchema = {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'Vofy',
    url: currentUrl,
    inLanguage: locale,
    description: t.schemaDescription,
  };

  const orgSchema = {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Vofy',
    url: currentUrl,
    logo: `${BASE_URL}/images/branding/logo-3.png`,
    description: t.schemaDescription,
    sameAs: ['https://discord.gg/AuggThwmXm'],
  };

  return (
    <html lang={locale}>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(orgSchema) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(webSiteSchema) }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

---

### 修改 3：语言切换器 UI 组件

**文件路径：** `src/components/LanguageSwitcher.tsx`

```typescript
'use client';

import { usePathname, useRouter } from 'next/navigation';
import { useState, useCallback } from 'react';

interface Language {
  code: string;
  label: string;
  shortLabel: string;
}

const LANGUAGES: Language[] = [
  { code: 'en', label: 'English', shortLabel: 'EN' },
  { code: 'es', label: 'Español', shortLabel: 'ES' },
];

function getCurrentLocale(pathname: string): string {
  const segment = pathname.split('/')[1];
  return ['en', 'es'].includes(segment) ? segment : 'en';
}

function buildNewPath(pathname: string, targetLocale: string): string {
  const currentLocale = getCurrentLocale(pathname);
  if (currentLocale === targetLocale) return pathname;

  // Remove current locale prefix
  let stripped = pathname;
  if (currentLocale !== 'en' || pathname.startsWith(`/${currentLocale}`)) {
    stripped = pathname.replace(new RegExp(`^/${currentLocale}`), '') || '/';
  }

  // Add target locale prefix (except for default 'en')
  if (targetLocale === 'en') {
    return stripped || '/';
  }
  return `/${targetLocale}${stripped}`;
}

export function LanguageSwitcher({
  variant = 'dropdown',
}: {
  variant?: 'dropdown' | 'toggle';
}) {
  const pathname = usePathname();
  const router = useRouter();
  const [isOpen, setIsOpen] = useState(false);
  const currentLocale = getCurrentLocale(pathname);
  const currentLang = LANGUAGES.find((l) => l.code === currentLocale) ?? LANGUAGES[0];

  const switchLanguage = useCallback(
    (locale: string) => {
      const newPath = buildNewPath(pathname, locale);
      setIsOpen(false);
      router.push(newPath);
    },
    [pathname, router],
  );

  if (variant === 'toggle') {
    return (
      <div className="flex items-center gap-1 rounded-lg border border-border/60 bg-muted p-0.5">
        {LANGUAGES.map((lang) => (
          <button
            key={lang.code}
            onClick={() => switchLanguage(lang.code)}
            className={`rounded-md px-2.5 py-1 text-xs font-medium transition-colors ${
              currentLocale === lang.code
                ? 'bg-background text-foreground shadow-sm'
                : 'text-muted-foreground hover:text-foreground'
            }`}
            aria-label={`Switch to ${lang.label}`}
            aria-current={currentLocale === lang.code ? 'true' : undefined}
          >
            {lang.shortLabel}
          </button>
        ))}
      </div>
    );
  }

  // Default: dropdown variant
  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-1.5 rounded-lg border border-border/60 bg-muted px-3 py-1.5 text-xs font-medium text-foreground transition-colors hover:bg-muted/80"
        aria-haspopup="listbox"
        aria-expanded={isOpen}
        aria-label={`Current language: ${currentLang.label}. Click to change.`}
      >
        <span>{currentLang.shortLabel}</span>
        <svg
          className={`h-3 w-3 text-muted-foreground transition-transform ${isOpen ? 'rotate-180' : ''}`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {isOpen && (
        <>
          {/* Backdrop to close on outside click */}
          <div className="fixed inset-0 z-10" onClick={() => setIsOpen(false)} aria-hidden="true" />
          <ul
            role="listbox"
            className="absolute bottom-full left-0 z-20 mb-1 min-w-[120px] overflow-hidden rounded-lg border border-border bg-background py-1 shadow-lg"
          >
            {LANGUAGES.map((lang) => (
              <li key={lang.code} role="option" aria-selected={currentLocale === lang.code}>
                <button
                  onClick={() => switchLanguage(lang.code)}
                  className={`flex w-full items-center gap-2 px-3 py-2 text-sm transition-colors hover:bg-muted ${
                    currentLocale === lang.code
                      ? 'font-semibold text-foreground'
                      : 'text-muted-foreground'
                  }`}
                >
                  {lang.label}
                  {currentLocale === lang.code && (
                    <svg className="ml-auto h-4 w-4 text-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  )}
                </button>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}
```

---

### 修改 4：将 LanguageSwitcher 嵌入侧边栏

**文件路径：** 找到侧边栏 `<aside>` 组件（位于 `src/components/Sidebar.tsx` 或类似位置）

在 `<aside>` 内，导航列表下方、用户区域上方，插入：

```tsx
import { LanguageSwitcher } from '@/components/LanguageSwitcher';

// 在侧边栏 JSX 中，导航列表 ul 之后添加：
<div className="mt-auto flex flex-col items-center gap-3 pb-2">
  <LanguageSwitcher variant="dropdown" />
</div>
```

建议位置：侧边栏底部，在 Logo 和导航项之后。使用 `mt-auto` 将其推到底部。

`variant` 可选值：
- `"dropdown"` — 下拉菜单（推荐，适合 20px 宽侧边栏）
- `"toggle"` — EN/ES 切换按钮

---

### 验证清单

部署后需要验证以下项：

```
□ 访问 / — 页面显示英文，标题为英文
□ 访问 /es — 页面显示西语
  □ <title> 为 "Vofy — Tu estudio creativo de IA todo en uno"
  □ <meta property="og:title"> 为西语
  □ Schema.org url 指向 /es，description 为西语
  □ inLanguage 为 "es"
□ 访问 /es 后手动改 URL 为 / — 不再被跳转回 /es
□ 语言切换器可见，切换 EN ↔ ES 正常工作
□ 切换语言后 Cookie vofy_locale 同步更新
□ 首次无 Cookie 访问 /，Accept-Language: es 时跳转 /es
□ hreflang 标签仍正确（不变）
```
