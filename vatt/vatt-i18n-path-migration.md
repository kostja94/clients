# Vatt — 多语言迁移：`?lang=` → 路径前缀（`/{locale}`）

> **本文档职责**：将 [vatt.ai](https://vatt.ai/) 当前的查询参数多语言方案（`?lang=xx`）迁移为 URL 路径前缀方案（`/it`、`/es`、`/fr`、`/de`、`/zh`、`/pt`、`/ja`）的技术栈、URL 约定、迁移步骤与验收。  
> **引用**：[vatt.md](./vatt.md) 概览 | [vatt-site-structure.md](./vatt-site-structure.md) 站点结构 | [vatt-others.md](./vatt-others.md) 站点观测 | [vatt-features.md](./vatt-features.md) 功能 Status
> **技术栈假定**：Next.js App Router + [next-intl](https://next-intl.dev/docs/routing/configuration)（若官网非 Next，则映射等价 i18n，**公开 URL 约定不变**——见 §3.4）

**最近更新**：2026-08-06

---

## 0. 现状与目标

### 0.1 当前架构（迁移前）

| 维度 | 现状 |
|------|------|
| 多语言机制 | **查询参数** `?lang=xx`，URL 路径不变（`/` 通用于所有语言） |
| 已验证语言 | **en**（默认，无参数）、**it**、**es**、**fr**、**de**、**zh**、**pt**、**ja**（2026-08-05 逐 URL 验证） |
| 语言存储 | Cookie / localStorage + URL 参数双写（推断；`?lang=` 可直达说明语言可从 URL 恢复） |
| 切换行为 | 导航栏语言切换器改写 URL 参数；**无独立语言 URL** |
| 前端栈 | **待验证**（推测 React/Next.js SPA；登录页有 redirect 行为） |
| 站点规模 | 极简 3 页：`/`、`/pricing`（动态加载）、`/login` |
| SEO 状态 | 极差：无 robots.txt、无 sitemap、无 meta description（vatt-site-structure.md §3/§4） |

**`?lang=` 现状验证记录**（2026-08-05）：

| URL | 结果 |
|-----|------|
| `https://vatt.ai/` | 200 英文（默认） |
| `https://vatt.ai/?lang=it` | 意大利语 |
| `https://vatt.ai/?lang=es` | 西班牙语 |
| `https://vatt.ai/?lang=fr` | 法语 |
| `https://vatt.ai/?lang=de` | 德语 |
| `https://vatt.ai/?lang=zh` | 简体中文 |
| `https://vatt.ai/?lang=pt` | 葡萄牙语 |
| `https://vatt.ai/?lang=ja` | 日语 |
| `https://vatt.ai/pricing?lang=it` | 404（定价页为动态渲染；`?lang=` 覆盖范围以现网路由为准） |

### 0.2 目标架构（迁移后）

| 维度 | 目标 |
|------|------|
| i18n 库 | **next-intl**（App Router 集成）；非 Next 见 §3.4 映射 |
| URL 策略 | `localePrefix: 'as-needed'` — 英文根路径无前缀，其他语言 `/{locale}` 前缀 |
| 切换行为 | `router.replace(pathname, { locale })`，**URL 随语言变更** |
| SSR/SSG | 服务端直接输出对应语言 HTML，`<html lang={locale}>` |
| 语言检测 | **`localeDetection: false`** — 不读 Accept-Language / Cookie 自动跳转；语言仅由 URL、切换器、`?lang=` 兼容跳转决定 |
| 兼容 | `?lang=xx` **308** 跳转至 `/{locale}{path}`（去参数）；默认语言 `?lang=en` 308 至无前缀路径 |
| SEO | 每语言独立 URL + hreflang 互指 + self canonical + `x-default`→英文 |

> **英文 URL 原则**：`localePrefix: 'as-needed'` + `defaultLocale: 'en'` → 英文 canonical **永不暴露** `/en/` 前缀。历史与未来全站 canonical、sitemap、内链均不得含 `/en/`。

### 0.3 URL 对照表

| 英文（默认，无前缀） | 其他语言 |
|---------------------|---------|
| `/` | `/{locale}/`（如 `/it/`、`/zh/`） |
| `/pricing` | `/{locale}/pricing`（如 `/it/pricing`） |
| `/login` | `/{locale}/login`（若产品决策登录页参与营销 i18n；见 §4.4） |
| `/features`（规划） | `/{locale}/features` |
| `/blog/{slug}`（规划） | 依 §4.5 决策（默认**英语独占**，不生成 `/{locale}/blog/...`） |
| `/channel/{slug}`（规划） | `/{locale}/channel/{slug}` |

**禁止**：对外暴露 `/en/...` canonical URL。若请求误入 `/en/*`，middleware **防御性 301** 去前缀（见 §2.6）。

### 0.4 语言列表与 hreflang 码

| URL 段 | 语言 | hreflang 码（BCP 47） | 备注 |
|--------|------|----------------------|------|
| （无） | English | `en` | 默认语言，无前缀 |
| `it` | Italiano | `it` | 已验证 |
| `es` | Español | `es` | 已验证 |
| `fr` | Français | `fr` | 已验证 |
| `de` | Deutsch | `de` | 已验证 |
| `zh` | 简体中文 | `zh-Hans` | 已验证；URL 用短码 `zh`，hreflang 用 `zh-Hans`（全站统一，勿混用 `zh-CN`） |
| `pt` | Português | `pt` | 已验证 |
| `ja` | 日本語 | `ja` | 已验证 |

> 语言列表以站点语言切换器实际选项为准；**新增语言只改一处 `locales` 数组**（§2.2）+ 一份翻译文件 + `HREFLANG_MAP`（§2.9），无需改路由代码。

---

## 1. 技术栈选型

| 层 | 选型 | 说明 |
|----|------|------|
| 框架 | Next.js App Router（**待验证**；若不符见 §3.4） | 现站为 SPA，迁移需要 SSR/SSG 才能让每语言 URL 可被爬虫直接访问 |
| i18n | **next-intl** | App Router 官方集成最顺；支持 `localePrefix` 与 middleware |
| 路由 | `app/[locale]/...` | locale 从 URL 段解析 |
| 文案 | `messages/{locale}.json` | UI 文案（导航、按钮、页脚、FAQ 壳）；页面正文分语言存放 |
| 兼容 | middleware 内 `?lang=` 308 分支 | 保留旧书签 / 外部链接可用性 |
| SEO | 页面 `generateMetadata` `alternates` + sitemap `xhtml:link` | 二选一为主，避免三套互相打架 |

**选型理由（对照公开最佳实践）**：Google 将目录前缀视为合法多语言实现；查询参数被视作同一 canonical，无法独立索引。vatt 当前为早期营销站，SEO 尚非重点，但路径前缀是「一次迁移、长期不返工」的正确形态，且 `?lang=` 兼容分支保证平滑。

---

## 2. 完整技术配置（Next.js + next-intl，复制即用）

### 2.1 安装依赖

```bash
npm install next-intl
```

> 若现有站存在其他 i18n 方案（如 i18next + react-i18next + browser-languagedetector），按 §3 迁移后执行 `npm uninstall` 清理。当前 `?lang=` 实现是否基于 i18next 待源码确认。

### 2.2 `i18n/routing.ts`

```typescript
import { defineRouting } from 'next-intl/routing';

export const routing = defineRouting({
  locales: ['en', 'it', 'es', 'fr', 'de', 'zh', 'pt', 'ja'],
  defaultLocale: 'en',
  localePrefix: 'as-needed', // en 无前缀，其余为 /it /es /fr /de /zh /pt /ja
  localeDetection: false,    // 必关：语言仅由 URL 决定，避免 Accept-Language/Cookie 把 / → /zh
  localeCookie: false,       // 建议关：与「不自动跳转」一致，减少 as-needed 下隐式重定向
  alternateLinks: false,     // 不用全局 Link 头，改由页面 metadata 精确声明（含 zh-Hans 映射）
});

export type Locale = (typeof routing.locales)[number];
```

**为何这样配**：

| 项 | 原因 |
|----|------|
| `as-needed` | 英文 URL 保持无前缀，不被 `/en` 污染，利于存量与未来的 SEO |
| `localeDetection: false` | as-needed 开启检测时，Cookie 可能把无前缀路径重定向到上次语言（`/`→`/zh`），伤害爬虫与分享链接 |
| `alternateLinks: false` | 默认 Link 头按「全 locale × 全路径」生成；需要 `zh-Hans` 映射与 per-page 精确性，页面级 metadata 更可控 |

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

### 2.5 `next.config.ts`

```typescript
import type { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./i18n/request.ts');

const nextConfig: NextConfig = {
  // 保留现有配置；新增多语言后建议开启静态导出相关设置（若全站可 SSG）
};

export default withNextIntl(nextConfig);
```

### 2.6 `middleware.ts`（核心：`?lang=` 兼容 308 + 防御性 `/en/` 301）

```typescript
import createMiddleware from 'next-intl/middleware';
import { NextRequest, NextResponse } from 'next/server';
import { routing } from './i18n/routing';

const intlMiddleware = createMiddleware({
  ...routing,
  localeDetection: false,
});

const LOCALES = new Set<string>(routing.locales);

export default function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // 1. 静态资源 / API：跳过
  if (
    pathname.startsWith('/_next') ||
    pathname.startsWith('/api') ||
    pathname.includes('.')
  ) {
    return NextResponse.next();
  }

  // 2. 防御性 /en/* 301 去前缀（英文无前缀，历史与未来均无 /en/ URL）
  if (pathname === '/en' || pathname.startsWith('/en/')) {
    const target = pathname.replace(/^\/en/, '') || '/';
    return NextResponse.redirect(new URL(target, request.url), 301);
  }

  // 3. ?lang= 兼容跳转（308，仅删 lang 参数，保留其他 query）
  const lang = request.nextUrl.searchParams.get('lang');
  if (lang && LOCALES.has(lang)) {
    const url = request.nextUrl.clone();
    url.searchParams.delete('lang');

    if (lang !== 'en') {
      // 已带该前缀时仅删参数，避免 /it/it
      const alreadyPrefixed =
        pathname === `/${lang}` || pathname.startsWith(`/${lang}/`);
      if (!alreadyPrefixed) {
        url.pathname = pathname === '/' ? `/${lang}` : `/${lang}${pathname}`;
      }
    }
    return NextResponse.redirect(url, 308);
  }

  // 4. 其余交给 next-intl（解析 /it /es /fr /de /zh /pt /ja 前缀）
  return intlMiddleware(request);
}

export const config = {
  matcher: ['/((?!_next|api|.*\\..*).*)'],
};
```

### 2.7 `app/[locale]/layout.tsx`

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

> 根 `app/layout.tsx` 保持 minimal（pass-through children）；`<html lang>` 只由 `[locale]/layout.tsx` 输出。

### 2.8 `components/LanguageSwitcher.tsx`

```tsx
'use client';

import { useLocale, useTranslations } from 'next-intl';
import { usePathname, useRouter } from '@/i18n/navigation';
import { routing, type Locale } from '@/i18n/routing';

const LOCALE_LABELS: Record<Locale, string> = {
  en: 'English',
  it: 'Italiano',
  es: 'Español',
  fr: 'Français',
  de: 'Deutsch',
  zh: '中文',
  pt: 'Português',
  ja: '日本語',
};

export function LanguageSwitcher() {
  const locale = useLocale() as Locale;
  const router = useRouter();
  const pathname = usePathname();
  const t = useTranslations('common');

  function handleChange(nextLocale: Locale) {
    // 同 path 换前缀；next-intl 自动处理 as-needed（en 去前缀，其余加前缀）
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

### 2.9 `lib/metadata.ts` — hreflang / canonical 辅助

```typescript
const BASE_URL = 'https://vatt.ai';

/** URL 短码 → BCP 47（zh → zh-Hans；其余同短码） */
const HREFLANG_MAP: Record<string, string> = {
  en: 'en',
  it: 'it',
  es: 'es',
  fr: 'fr',
  de: 'de',
  zh: 'zh-Hans',
  pt: 'pt',
  ja: 'ja',
};

/**
 * 可本地化页：en canonical 指向无前缀 URL，各语言 canonical 指向自身
 * @param pathname 不含 locale 的纯路径（首页传 '/'）
 */
export function buildAlternates(pathname: string, locale: string) {
  const normalized = pathname === '/' ? '' : pathname;
  const url = `${BASE_URL}${normalized}`;

  const languages: Record<string, string> = {
    'x-default': url,
  };

  for (const loc of Object.keys(HREFLANG_MAP)) {
    languages[HREFLANG_MAP[loc]] =
      loc === 'en'
        ? `${BASE_URL}${normalized}`
        : `${BASE_URL}/${loc}${normalized}`;
  }

  const canonical =
    locale === 'en' ? url : `${BASE_URL}/${locale}${normalized}`;

  return {
    alternates: { canonical, languages },
  };
}
```

### 2.10 `generateMetadata` 示例（首页）

```tsx
// app/[locale]/page.tsx
import type { Metadata } from 'next';
import { getTranslations } from 'next-intl/server';
import { buildAlternates } from '@/lib/metadata';

type Props = { params: Promise<{ locale: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'home' });

  return {
    title: t('meta.title'),
    description: t('meta.description'),
    ...buildAlternates('/', locale),
  };
}
```

### 2.11 Sitemap

```typescript
// app/sitemap.ts
import type { MetadataRoute } from 'next';
import { routing } from '@/i18n/routing';

const BASE_URL = 'https://vatt.ai';
// 现网可索引路径（以实际路由表为准；定价/登录依产品决策纳入）
const PATHS = ['/', '/pricing', '/login'];

export default function sitemap(): MetadataRoute.Sitemap {
  return PATHS.flatMap((path) =>
    routing.locales.map((locale) => {
      const url = `${BASE_URL}${locale === 'en' ? '' : `/${locale}`}${
        path === '/' ? '' : path
      }`;
      return {
        url,
        lastModified: new Date(),
        alternates: {
          languages: Object.fromEntries(
            routing.locales.map((loc) => [
              loc === 'zh' ? 'zh-Hans' : loc,
              `${BASE_URL}${loc === 'en' ? '' : `/${loc}`}${
                path === '/' ? '' : path
              }`,
            ])
          ),
        },
      };
    })
  );
}
```

---

## 3. 从 `?lang=` 迁移步骤

### 3.1 文案抽取

1. 在现站源码定位当前多语言实现（搜索 `lang`、`i18n`、`locale`、`messages`、翻译 JSON 资源）
2. 将每语言的完整文案导出为 `messages/{locale}.json`（en/it/es/fr/de/zh/pt/ja）
3. 键名保持各语言一致；**UI 壳文案**（导航、语言切换器、页脚、FAQ 标签）进 messages；**页面正文**按语言分目录存放（如 `content/{locale}/home/` 或维持现有结构）

### 3.2 路由重构

| 迁移前 | 迁移后 |
|--------|--------|
| `app/page.tsx` | `app/[locale]/page.tsx` |
| `app/layout.tsx`（含 html） | `app/layout.tsx`（minimal pass-through）+ `app/[locale]/layout.tsx`（`<html lang>`） |
| `app/pricing/page.tsx` 等 | `app/[locale]/pricing/page.tsx`（若纳入 i18n） |
| 语言切换器改 URL 参数 | `router.replace(pathname, { locale })`（§2.8） |

### 3.3 移除 `?lang=` 读取逻辑

- 删除组件内「从 `searchParams.lang` 读语言」的逻辑（现为 308 兼容分支接管，见 §2.6 第 3 步）
- 删除「写入 cookie/localStorage」的逻辑；next-intl 语言随 URL，`localeDetection: false` 下无自动跳转
- 若现站依赖 `localStorage` 记忆语言，可加一次性 `LegacyLocaleRedirect`（见 §3.5）

### 3.4 非 Next 框架映射

仍采用同一 URL/内容分层（UI messages + 按 locale 内容 + hreflang）。框架层换成该栈官方 i18n，**不得改变** §0.3 的公开 URL 约定：

| 框架 | 等价方案 |
|------|---------|
| Astro | `i18n.routing`（`i18n` config + `Astro.request` 取 locale） |
| Nuxt / Vue | `@nuxtjs/i18n`（`strategy: 'prefix_except_default'`） |
| Remix | `react-intl` + 自建 locale 路由段 |
| 纯静态 SPA | 需改为每个 locale 生成独立静态页（SSG），否则爬虫只能看到一种语言；`?lang=` 参数 URL 无法被独立索引 |

### 3.5 存量用户 Cookie 迁移（可选一次性脚本）

```tsx
'use client';

import { useEffect } from 'react';
import { useRouter } from '@/i18n/navigation';

/** 仅运行一次：把旧的 localStorage/cookie 语言偏好迁移到 URL */
export function LegacyLocaleRedirect() {
  const router = useRouter();

  useEffect(() => {
    const legacy = localStorage.getItem('vatt-lang'); // 以现站实际 key 为准
    if (!legacy || legacy === 'en' || legacy === 'it' /* 仅迁移已支持值 */) return;
    if (['it', 'es', 'fr', 'de', 'zh', 'pt', 'ja'].includes(legacy)) {
      localStorage.removeItem('vatt-lang');
      router.replace('/', { locale: legacy });
    }
  }, [router]);

  return null;
}
```

> middleware 无法读 localStorage；`?lang=` 兼容分支（§2.6）覆盖「带参直达」场景，此脚本只兜底「曾设置过偏好、如今直接访问 `/`」的老用户。

### 3.6 内链替换

```tsx
// 迁移前
import Link from 'next/link';
<Link href="/pricing">Pricing</Link>

// 迁移后
import { Link } from '@/i18n/navigation';
<Link href="/pricing">Pricing</Link>  // 自动带当前 locale 前缀
```

全库范围：Header/Footer、首页锚点、正文内链；**禁止**裸 `next/link` 漏前缀。

---

## 4. 策略决策（针对 Vatt 现状）

### 4.1 默认语言

`defaultLocale: 'en'` + `as-needed`：英文为全球默认（现站目标市场即英文），`x-default` 恒指向英文 URL。

### 4.2 `?lang=` 兼容保留期

| 建议 | 理由 |
|------|------|
| **保留 308 兼容分支 ≥ 3 个月** | 外部已传播的 `?lang=it` 链接、旧书签仍可用 |
| 3 个月后在 GSC/数据中确认旧参数 URL 流量归零后移除 | 减少 middleware 分支 |
| **不**将 `?lang=` 参数 URL 写入 sitemap / canonical | 参数 URL 不参与索引 |

### 4.3 Accept-Language 首访检测

**第一版不做**（`localeDetection: false`）。理由：自动按浏览器语言跳转会（1）让爬虫每次看到跳转而非稳定 URL；（2）无前缀 `/` 被 Cookie 劫持的语言偏好破坏分享链接。可选增强（后续）：仅对 `/` 做一次 **非阻断**提示条，由用户主动点语言切换器。

### 4.4 登录页与产品 App

`/login` 与登录后的编辑器（App）是**产品面**，是否多语言由产品团队决策。本文档默认：营销站路径（`/`、`/pricing`、未来 `/features`、`/channel/*`）纳入路径 i18n；`/login` 默认**不纳入**（保持 `/login`，避免登录态与语言前缀纠缠）；若需纳入，URL 用 `/{locale}/login` 并在 §0.3 登记。

### 4.5 未来内容页（Blog / Features / Channel）

参照 [vatt-site-structure.md §6](./vatt-site-structure.md) 的页面规划：

| 规划页面 | 多语言策略（建议） |
|---------|------------------|
| `/features` | 纳入：`/{locale}/features`（产品价值页，多语言 ROI 高） |
| `/blog/{slug}` | **英语独占**（无 `/{locale}/blog`），理由同行业惯例：Blog 为长尾 SEO 阵地，多语言翻译投入高、早期收益低；hreflang 不声明虚假 alternate |
| `/channel/{slug}` | 纳入：`/{locale}/channel/{slug}`（pSEO 页可随翻译进度增量开放） |
| `/pricing` 静态化（长期） | 纳入：`/{locale}/pricing` |

**未翻译页面**：不生成 `/{locale}/...` 路由、不进 sitemap、不输出对应 hreflang（遵循"缺啥不造啥"原则）。

---

## 5. SEO 与 Sitemap

| 项 | 约定 |
|----|------|
| robots.txt | 迁移时一并补上（当前 404）；allow 全站，`Disallow: /api` 等 |
| sitemap.xml | 新增；每路径 × 每语言一条（§2.11） |
| hreflang | 页面 `alternates.languages` **双向互指 + self + x-default→en**；`zh` 映射为 `zh-Hans` |
| canonical | 各语言指向自身；绝对 URL；与 sitemap / trailing slash 写法一致 |
| `<html lang>` | 与页面语言一致（`en` / `it` / `es` / `fr` / `de` / `zh` / `pt` / `ja`） |
| 参数 URL | 不出现在 sitemap / canonical；旧参数 URL 由 308 收敛到路径 URL |

**迁移后 GSC 动作**：提交新 sitemap；观察 `?lang=` 参数 URL 逐渐被替换为路径 URL；若 Google 已索引少量 `?lang=` 页面，可依赖 308 收敛，无需逐条 301。

---

## 6. 分阶段任务清单（Agent 可执行）

> 格式：**任务 ID** | 操作 | 文件/路径 | 验收标准 | 依赖

### Phase 0 — 基础设施（可并行上线，不破坏现行为）

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P0-M01 | 备份现网：记录当前所有 URL、语言、`?lang=` 行为 | 文档/git | 迁移基线可回滚 | — |
| P0-M02 | `npm install next-intl` | `package.json` | 依赖已添加 | P0-M01 |
| P0-M03 | 创建 `i18n/routing.ts`、`request.ts`、`navigation.ts` | `i18n/*` | `localeDetection: false`；locales 含 8 语言 | P0-M02 |
| P0-M04 | 配置 `next.config.ts` plugin | `next.config.ts` | `next build` 通过 | P0-M03 |
| P0-M05 | 抽取并创建 `messages/{locale}.json` × 8 | `messages/*` | 键覆盖 common/home/... | P0-M02 |
| P0-M06 | 创建 `app/[locale]/layout.tsx` + 根 layout pass-through | `app/**` | `/` 200 英文 SSR；`lang="en"` | P0-M04, P0-M05 |
| P0-M07 | 迁移 `app/page.tsx` → `app/[locale]/page.tsx` | `app/[locale]/page.tsx` | 首页各语言可访问 | P0-M06 |
| P0-M08 | 实现 `middleware.ts`（?lang= 308 + /en/ 301 + intl） | `middleware.ts` | §7 用例 3/4/6/7 通过 | P0-M03 |
| P0-M09 | 实现 `LanguageSwitcher` + `lib/metadata.ts` | `components/**`、`lib/metadata.ts` | 切换语言 URL 变；view-source 含 hreflang | P0-M07, P0-M08 |
| P0-M10 | 上线 `/it` 等 7 条路径（每语言至少首页） | CI/CD | `https://vatt.ai/it/` 200 意大利语 | P0-M09 |
| P0-M11 | 新增 robots.txt + sitemap.xml | `app/robots.ts`、`app/sitemap.ts` | GSC 可抓取；sitemap 含 8 语言 × 路径 | P0-M10 |

### Phase 1 — 全站路径化 + 兼容观察

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P1-M01 | `/pricing` 等现有页迁入 `[locale]`（若纳入） | `app/[locale]/pricing/` | `/{locale}/pricing` 200 | P0-M11 |
| P1-M02 | 全库内链替换为 `@/i18n/navigation` | `components/**` | 无裸 next/link 漏前缀 | P0-M09 |
| P1-M03 | 移除 `?lang=` 读取与 cookie 写入逻辑；加 `LegacyLocaleRedirect` | `app/**`、`components/**` | 语言仅由 URL/切换器决定 | P1-M02 |
| P1-M04 | GSC 提交新 sitemap；监控 `?lang=` 流量曲线 | GSC | 旧参数 URL 流量开始下降 | P0-M11 |

### Phase 2 — 兼容分支收敛（≥3 个月后）

| 任务 ID | 操作 | 文件/路径 | 验收标准 | 依赖 |
|---------|------|-----------|----------|------|
| P2-M01 | 数据确认 `?lang=` 访问归零后移除 308 分支 | `middleware.ts` | 全站无 `?lang=` URL 访问 | P1-M04 |

---

## 7. 测试清单

### 7.1 手动测试（必做）

| # | 用例 | 步骤 | 期望 |
|---|------|------|------|
| 1 | 英文首页 | 访问 `/` | 200；`<html lang="en">`；URL 不变 |
| 2 | 意大利语首页 | 访问 `/it/` | 200；`<html lang="it">`；意大利语文案 |
| 3 | 语言切换 | `/` 选 Italiano | 跳转 `/it/`，URL 变化（非仅 cookie） |
| 4 | `?lang=` 兼容 | 访问 `/?lang=it` | **308** → `/it/`（去掉参数） |
| 4b | `?lang=en` 兼容 | 访问 `/it/?lang=en` | **308** → `/`（去掉参数与前缀） |
| 5 | 防御性 /en/ | 访问 `/en`、`/en/pricing` | **301** 去前缀 → `/`、`/pricing` |
| 6 | 中英全语言抽查 | 访问 `/zh/`、`/es/`、`/fr/`、`/de/`、`/pt/`、`/ja/` | 各 200，语言正确 |
| 7 | hreflang | view-source `/` | 8 语言互指 + self + `x-default`→en；`zh-Hans` |
| 8 | canonical | view-source `/it/` | canonical=`https://vatt.ai/it/` |
| 9 | 无自动跳转 | 中文浏览器直接访问 `/` | 200 英文，不自动跳 `/zh/` |
| 10 | sitemap | 访问 `/sitemap.xml` | 每路径 × 每语言条目；无 `/en/`、无 `?lang=` |
| 11 | 内链 | `/it/` 页内链 | 全部带 `/it` 前缀（除 en-only 目标） |
| 12 | 新增语言 | 临时加 `ko` 至 locales + messages | `/ko/` 可访问，无需改路由代码 |

### 7.2 curl 冒烟

```bash
curl -sI https://vatt.ai/ | grep -i "200\|content-language"
curl -sI https://vatt.ai/it/ | grep -i "200"
curl -sI "https://vatt.ai/?lang=it" | grep -i "308\|location"   # → /it/
curl -sI "https://vatt.ai/it/?lang=en" | grep -i "308\|location" # → /
curl -sI https://vatt.ai/en | grep -i "301\|location"            # 防御性 /en/
curl -s https://vatt.ai/sitemap.xml | grep -c "<url>"             # ≥ 路径×语言
```

---

## 8. Rollback 方案

| 触发条件 | 回滚步骤 |
|---------|---------|
| 英文核心 URL（`/`）非 200 | CI 立即 promote 上一稳定 deployment |
| `/en/` 被意外索引造成 duplicate | 修复 middleware 防御性 301；GSC 移除 `/en/` 条目 |
| 语言切换后 404 / 文案丢失 | 检查 `messages/{locale}.json` 键完整性；确认 `request.ts` fallback |
| `?lang=` 兼容 308 误跳（如 `/it/it`） | 核对 middleware 第 3 步的 alreadyPrefixed 判断 |

**备份清单（Phase 0 前）**：迁移前 main tag `pre-i18n-path-YYYYMMDD`；保存现 `middleware.ts`、`next.config.ts`、现语言切换实现代码；记录现网所有 URL 与 `?lang=` 行为。

---

## 9. 风险与规避

| 风险 | 规避 |
|------|------|
| `/` 与 `/en/` duplicate | 防御性 `/en/*` 301；sitemap / 内链不含 `/en/` |
| `?lang=` 旧链接失效 | 308 兼容分支保留 ≥3 个月（§4.2） |
| 未翻译页面出现错误语言 URL | 只对已翻译路径生成路由与 hreflang（§4.5） |
| 自动语言跳转伤害爬虫 | `localeDetection: false`；不做 Accept-Language 自动跳转 |
| 内链漏前缀 | 全库替换为 `@/i18n/navigation`；Code Review 检查裸 `next/link` |
| 语言列表扩展维护 | locale 单一来源：`routing.ts` locales + messages + `HREFLANG_MAP`，不散落多处 |
| 定价页动态加载与 404 观测 | 以现网路由表为准；迁移范围先确认 `/pricing`、`/login` 实际状态 |

---

## 10. 文档关系

| 文档 | 关系 |
|------|------|
| [vatt-site-structure.md](./vatt-site-structure.md) | 主站 IA；§6 页面规划的多语言策略承接本文档 §4.5 |
| [vatt-others.md](./vatt-others.md) | 站点观测（SEO 现状、`?lang=` 相关数据引用） |
| [vatt-features.md](./vatt-features.md) | 功能 Status（与 i18n 无关，但影响 `/features` 页面上线节奏） |

---

*i18n 路径前缀迁移 · Vatt · 范围：vatt.ai 营销站多语言 URL 化 · 2026-08-06 · 实施前需与 Vatt 工程团队确认前端栈（Next.js 假定）与语言列表。*
