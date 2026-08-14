# Today AI — 多语言 SEO 技术栈切换方案

> **状态**: 提案 · **更新**: 2026-08-12
> **依据**: 2026-08-12 对 [today.ai](https://today.ai/) 的实测（SSR 输出 + 客户端 JS 反编译） + 多语言 SEO 最佳实践（独立语言 URL、禁用自动跳转、hreflang 规范）与 next-intl 路径前缀迁移方案
> **一句话**: 把现网「Cookie + 同 URL 换文」的多语种，切换为「独立语言 URL（`/` 英文 + `/zh-Hans/` 中文）+ hreflang」的 SEO 友好架构；`i18next` 字典资产保留复用，仅改造路由层与切换器。

---

## 1. 现状诊断

### 1.1 现网实测（2026-08-12）

today.ai 当前多语种实现为 **i18next + Cookie + 同 URL 换文**：

| 观测项 | 实测结果 |
|--------|----------|
| 切换器位置 | `/` 首页 header Download Now 左侧，`aria-label="Language"` 下拉框，当前显示 EN |
| 切换行为 | 点选中文 → 写 `i18next=zh` Cookie（`max-age=31536000`，1 年）→ `i18next.changeLanguage('zh')` + `router.refresh()` → **URL 不变（仍为 `/`）**，页面变中文 |
| 服务端输出 | 带 `Cookie: i18next=zh` 请求 `/` 时 SSR 直接返回 `<html lang="zh">` + 中文字典（"立即下载 / 加入候补名单"） |
| 语言资源 | 已内置 4 套字典：`en / zh / ja / zhHant`（`settings.languageOption.*` 实证） |
| 查询参数 | `?lng=zh`、`?locale=zh` **无效**，仍返回英文 |
| 语言 URL | `/zh`、`/en` 均 **404**（`X-Matched-Path: /_not-found`） |
| hreflang / canonical / og:locale | 均无 |
| sitemap.xml / robots.txt | 均 **404** |
| 框架 | Next.js（Vercel 托管），`/` 映射到 `/waitlist` 路由，`/landing` 独立长页 |

### 1.2 问题清单

| ID | 问题 | 对应规范 | 严重度 |
|----|------|----------|--------|
| P1 | **中文版无独立 URL**——语言只存 Cookie，Googlebot 不带 Cookie 抓取时只能看到英文，中文版对搜索引擎完全不可见 | 同 URL + Cookie 换语言（爬虫难感知，对 SEO 几乎无效） | 🔴 阻断 |
| P2 | **无法落地 hreflang / canonical**——无 URL 可互指，中英版本永远指向同一 canonical | hreflang 须自引用 + 互指 + x-default，canonical 与当前页一致 | 🔴 阻断 |
| P3 | **分享/书签不可预期**——把中文页链接发给别人，对方打开仍是英文 | 可读性三原则之「可预期」 | 🟠 高 |
| P4 | **切换器不可抓取**——Radix combobox 无 `<a href>`，爬虫无法跟随语言切换 | 语言切换用真实链接（`<a href>`）优于纯 JS | 🟠 高 |
| P5 | **回访依赖 Cookie**——换设备/清 Cookie 后偏好丢失，且无法表达"我分享的是中文版" | 记住偏好须最终落到独立 URL | 🟡 中 |
| P6 | **站点级 SEO 基建缺失**——无 sitemap/robots，与多语言改造须一并补齐 | 站点级 P0 基建缺口 | 🟡 中 |

### 1.3 影响评估

- **SEO 损失**：中文搜索市场（healthcare、旅行、生活场景等长尾中文词）完全拿不到自然流量；英文版也因缺 hreflang/canonical 有 duplicate/signal 模糊风险。
- **机会**：现网已内嵌完整中文字典 + 服务端 SSR 已支持按语言渲染（实测 `<html lang="zh">` 与中文正文可正常输出）——**文案资产零浪费**，缺的只是 URL 结构、hreflang 与切换器改造。
- **风险提示**：Cookie 方案下部分搜索引擎与抓取工具可能把 "带 cookie 的 `/` "视为非标准页面，引入多余抓取；`router.refresh()` 同 URL 换文对 SPA 内网翻页也有状态回退问题。

---

## 2. 目标架构

### 2.1 目标 URL 策略：默认语言无前缀 + 其余语言路径前缀

```
/                  # 英文（默认语言，x-default 指向此处）
/zh-Hans/          # 简体中文
/zh-Hans/landing   # （若中文营销长页后续纳入）
```

关键决策：

| 决策点 | 选择 | 理由 |
|--------|------|------|
| locale 代码 | **`zh-Hans`**（URL 用 `zh` 短码亦可，但 hreflang 必须输出 `zh-Hans`） | BCP 47 规范；`zh` 在 hreflang 中不合法 |
| 默认语言 | 英文**无前缀**（`as-needed`） | 简洁、存量链接零破坏、x-default 清晰 |
| 自动检测 | **关闭**（`localeDetection: false`） | 禁 IP/Accept-Language 强制跳转 |
| Cookie 记忆 | **降级为可选回访偏好**：点选后跳到语言 URL，不依赖 Cookie 输出语言 | 无 Cookie 时 `/` 恒为英文可索引页 |
| 语言范围（第一版） | `en` + `zh-Hans` | 字典已有 4 套，但 ja/zhHant 页面未翻译完之前**不建路由、不写 hreflang**（"缺啥不造啥"） |
| 切换器 | 真实 `<a href>`，母语自称 | 链接可抓取、母语自称 |

### 2.2 信息架构映射表（第一版）

| 现网路径 | 英文（默认，不变） | 简体中文（新增） |
|----------|--------------------|------------------|
| `/`（waitlist 首页） | `/` | `/zh-Hans/` |
| `/landing` | `/landing` | `/zh-Hans/landing` |
| `/waitlist` | `/waitlist` | `/zh-Hans/waitlist` |
| `/downloads` | `/downloads` | `/zh-Hans/downloads` |
| `/privacy` `/terms` | 保持英文 | 第一版不译（不进 hreflang） |
| **`/healthcare`（即将上线）** | `/healthcare` | `/zh-Hans/healthcare` |
| **healthcare spoke** | `/healthcare/meal-planner` 等 | `/zh-Hans/healthcare/meal-planner` 等 |

---

## 3. 技术实现（Next.js + next-intl）

> 当前技术栈为 Next.js（App Router + Vercel），直接采用 next-intl 路径前缀方案。**i18next 字典（`en/zh/ja/zhHant`）导出为 `messages/{locale}.json` 复用**，不重写文案。

### 3.1 依赖与路由配置

```bash
npm install next-intl
# 迁移完成后移除：npm uninstall i18next react-i18next
```

```typescript
// i18n/routing.ts —— 单一事实来源
import { defineRouting } from 'next-intl/routing';

export const routing = defineRouting({
  locales: ['en', 'zh'],
  defaultLocale: 'en',
  localePrefix: 'as-needed',  // en 无前缀，zh → /zh-Hans
  localeDetection: false,     // 必关：语言仅由 URL 决定
  localeCookie: false,        // 语言偏好不依赖 cookie
  alternateLinks: false,      // 用页面级 metadata 精确声明（zh → zh-Hans 映射）
});
```

```typescript
// i18n/request.ts
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

### 3.2 路由重构（Locale 布局输出 `<html lang>`）

```tsx
// app/[locale]/layout.tsx
import { NextIntlClientProvider, hasLocale } from 'next-intl';
import { getMessages, setRequestLocale } from 'next-intl/server';
import { notFound } from 'next/navigation';
import { routing } from '@/i18n/routing';
import { LanguageSwitcher } from '@/components/LanguageSwitcher';

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }));
}

export default async function LocaleLayout({ children, params }) {
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

现有页面整体上移一层：`app/page.tsx → app/[locale]/page.tsx`、`app/landing/page.tsx → app/[locale]/landing/page.tsx`；`app/layout.tsx` 改为 pass-through（不含 `<html>`）。

### 3.3 语言切换器：URL 驱动（替代 Cookie 同 URL 换文）

```tsx
'use client';
// components/LanguageSwitcher.tsx
import { useLocale, useTranslations } from 'next-intl';
import { usePathname, useRouter } from '@/i18n/navigation';

export function LanguageSwitcher() {
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();
  const t = useTranslations('common');

  return (
    <div aria-label={t('language')}>
      <select
        value={locale}
        onChange={(e) => router.replace(pathname, { locale: e.target.value })}
      >
        <option value="en">English</option>
        <option value="zh">中文</option>
      </select>
    </div>
  );
}
```

要点：语言名用**母语自称**（English / 中文）；`router.replace(pathname, { locale })` 自动完成无前缀 ↔ `/zh-Hans/` 切换，**URL 随语言变化**。可选回访增强：保留 Cookie 仅记录偏好，首访 `/` 时**非阻断**提示条引导（不自动跳转）。

### 3.4 存量迁移兼容

1. **`?lng=` / `?locale=` 查询参数**（现网实测无效，但保险起见）在 middleware 中加 308 收敛到路径 URL。
2. **存量 `i18next` Cookie 迁移**（一次性脚本）：老用户带 `i18next=zh` 访问 `/` → 客户端 `useEffect` 读到后 `router.replace('/', { locale: 'zh' })` 并删除 Cookie（一次性 `LegacyLocaleRedirect` 脚本）。
3. **防御性 301**：`/en/*` 不属于合法 URL，middleware 去前缀（现网无 `/en` 链接，但防历史/外链）。

### 3.5 hreflang / canonical / sitemap

```typescript
// lib/metadata.ts —— zh → zh-Hans 映射，全站统一
const BASE_URL = 'https://today.ai';
const HREFLANG_MAP = { en: 'en', zh: 'zh-Hans' };
const DEFAULT_LOCALE = 'en';

export function buildAlternates(pathname: string, locale: string) {
  const normalized = pathname === '/' ? '' : pathname;
  const url = `${BASE_URL}${normalized}`;
  const languages = { 'x-default': url };
  for (const [code, bcp47] of Object.entries(HREFLANG_MAP)) {
    languages[bcp47] =
      code === DEFAULT_LOCALE ? url : `${BASE_URL}/${code}${normalized}`;
  }
  const canonical =
    locale === DEFAULT_LOCALE ? url : `${BASE_URL}/${locale}${normalized}`;
  return { alternates: { canonical, languages } };
}
```

```typescript
// app/[locale]/page.tsx —— generateMetadata
export async function generateMetadata({ params }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'home' });
  return {
    title: t('meta.title'),
    description: t('meta.description'),
    ...buildAlternates('/', locale),
  };
}
```

- **sitemap**：`/`、`/landing`、`/waitlist`、`/downloads`、`/healthcare`、`/healthcare/meal-planner` 等 × `[en, zh]`，中文条目不输出 `/en/`、无 `?lng=`。
- **robots.txt** 一并补齐：allow 全站、`Disallow: /api`（现网 404，属 P0 基建）。

---

## 4. Example：即将上线的 Healthcare 页面

> 以下为 `/healthcare`（hub + spoke）在本方案下的落地示例。文案与关键词取自 [today-ai-healthcare.md](./today-ai-healthcare.md)（原型 today-ai.lovable.app/healthcare 的 hub 页 + 3 个 spoke 页）。

### 4.1 URL 规划

| 页面 | 英文（默认） | 简体中文 | 目标关键词（英文 / 中文） |
|------|--------------|----------|---------------------------|
| Healthcare hub | `/healthcare` | `/zh-Hans/healthcare` | ai personal assistant healthcare / AI 健康助理 |
| Meal Planner spoke | `/healthcare/meal-planner` | `/zh-Hans/healthcare/meal-planner` | ai meal planner / AI 饮食计划生成器 |
| Sleep Tracker spoke | `/healthcare/sleep-tracker` | `/zh-Hans/healthcare/sleep-tracker` | ai sleep coach / AI 睡眠教练 |
| Fitness Coach spoke | `/healthcare/fitness-coach` | `/zh-Hans/healthcare/fitness-coach` | ai personal trainer / AI 私人教练 |

### 4.2 页面元数据与 hreflang 输出示例（meal-planner spoke）

```tsx
// app/[locale]/healthcare/meal-planner/page.tsx
export async function generateMetadata({ params }) {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'healthcare.mealPlanner' });

  return {
    title: t('meta.title'),      // en: "AI Meal Planner — Today" / zh: "AI 饮食计划生成器 — Today"
    description: t('meta.description'),
    ...buildAlternates('/healthcare/meal-planner', locale),
  };
}
```

生成的 `<head>`（以英文页为例，中文页自引用同理）：

```html
<!-- /healthcare/meal-planner -->
<link rel="canonical" href="https://today.ai/healthcare/meal-planner">
<link rel="alternate" hreflang="en" href="https://today.ai/healthcare/meal-planner">
<link rel="alternate" hreflang="zh-Hans" href="https://today.ai/zh-Hans/healthcare/meal-planner">
<link rel="alternate" hreflang="x-default" href="https://today.ai/healthcare/meal-planner">
```

### 4.3 Sitemap 条目示例

```xml
<url>
  <loc>https://today.ai/healthcare/meal-planner</loc>
  <lastmod>2026-08-12</lastmod>
  <xhtml:link rel="alternate" hreflang="en" href="https://today.ai/healthcare/meal-planner"/>
  <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://today.ai/zh-Hans/healthcare/meal-planner"/>
</url>
<url>
  <loc>https://today.ai/zh-Hans/healthcare/meal-planner</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://today.ai/healthcare/meal-planner"/>
  <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://today.ai/zh-Hans/healthcare/meal-planner"/>
</url>
```

### 4.4 双语文案映射（messages 示例）

```jsonc
// messages/zh.json（healthcare 命名空间，节选）
{
  "healthcare": {
    "meta": {
      "hubTitle": "AI 个人健康助理 — Today",
      "hubDescription": "记录不是难点，行动才是：压力、饮食、睡眠、训练四大健康能力，Today 替你办掉。",
      "mealPlannerTitle": "AI 饮食计划生成器 — Today",
      "mealPlannerDescription": "会计划、会采购、会自适应的每周餐单。仅生活方式支持，不做医疗诊断。"
    },
    "nav": { "mealPlanner": "饮食计划", "sleepTracker": "睡眠跟踪", "fitnessCoach": "训练教练" }
  }
}
```

### 4.5 Healthcare 内链（spoke ↔ hub 双向）

```tsx
// 在任意 healthcare 页，使用 i18n 导航 Link，自动带当前语言前缀
import { Link } from '@/i18n/navigation';

// en 页渲染 /healthcare，zh 页渲染 /zh-Hans/healthcare
<Link href="/healthcare">AI Personal Agent for Healthcare</Link>
```

hub-spoke 闭环（见 healthcare 文档）同步到双语：hub 能力卡 → 3 个 spoke 的英文内链 + 中文内链各自独立成环，互不串语言。

---

## 5. 迁移步骤与测试清单

### 5.1 实施步骤（建议排期）

| # | 步骤 | 产出 |
|---|------|------|
| 1 | 导出 i18next 字典 → `messages/{locale}.json`（en/zh 先行，ja/zhHant 冻结待译） | 文案资产复用 |
| 2 | 接入 next-intl：routing/request/navigation + `[locale]` 路由重构 | 双语 URL 上线 |
| 3 | 切换器改 URL 驱动 + 存量 Cookie 一次性迁移脚本 | 老用户平滑过渡 |
| 4 | hreflang/canonical/sitemap/robots 全站补齐 | SEO 基建 |
| 5 | 上线 Healthcare hub + spoke 双语页 | 首批双语内容页 |
| 6 | GSC 提交 sitemap，验证 `/zh-Hans/*` 索引 | 数据闭环 |

### 5.2 验收清单

- [ ] `/` 恒为英文 200；`/zh-Hans/` 中文 200；无 Accept-Language/IP 自动跳转
- [ ] 切换器选中文 → URL 变为 `/zh-Hans/`（非仅 Cookie）
- [ ] 每页 hreflang 自引用 + 互指 + `x-default`，`zh-Hans` 正确（勿用 `zh`）
- [ ] canonical 与当前页 URL 一致；sitemap 每路径 × 每语言，无 `/en/`、无 `?lng=`
- [ ] `/en`、`/en/landing` 返回 301 去前缀；`?lng=zh` 返回 308 → `/zh-Hans/`
- [ ] `npm run build` 无 locale 报错；未翻译页面（ja/zhHant）不建路由、不写 hreflang
- [ ] robots.txt 与 sitemap.xml 可访问

---

## 6. 参考

| 来源 | 说明 |
|------|------|
| [today-ai-healthcare.md](./today-ai-healthcare.md) | Healthcare hub+spoke 页面内容与关键词 |
| [today-ai-site-structure.md](./today-ai-site-structure.md) | 现网 IA 与 SEO 基建缺口 |
| [today-ai-keywords.md](./today-ai-keywords.md) | 中英文关键词映射 |

---

## 站内关联

[主文档](./today-ai.md) · [site-structure](./today-ai-site-structure.md) · [keywords](./today-ai-keywords.md) · [healthcare](./today-ai-healthcare.md) · [style](./style.md)

*Last updated: 2026-08-12*
