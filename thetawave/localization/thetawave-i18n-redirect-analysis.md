# ThetaWave i18n 首页自动跳转机制分析

> 分析日期：2026-07-03  
> 网站：https://thetawave.ai  
> 托管平台：Vercel  
> 框架：Next.js (App Router)

---

## 一、现象描述

访问 `https://thetawave.ai/` 时，服务器返回 **307 Temporary Redirect** 自动跳转到 `https://thetawave.ai/ko`（韩语版首页）。即使用户手动删除 URL 中的 `/ko` 再次访问，仍会被重定向回 `/ko`。

---

## 二、触发条件（多重）

### 2.1 Cookie 触发 — `NEXT_LOCALE`

**这是最主要的原因。** 用户首次访问 `/ko` 页面时，服务器在响应中写入 Cookie：

```http
Set-Cookie: NEXT_LOCALE=ko; Path=/; SameSite=lax
```

此后每次访问 `https://thetawave.ai/`，浏览器都会携带此 Cookie。服务器检测到 `NEXT_LOCALE=ko` 后执行 307 重定向到 `/ko`。

验证测试：

| 测试条件 | 结果 |
|----------|------|
| 无 Cookie，无特殊 Accept-Language | `200 OK`，返回英文页 ✅ |
| `Cookie: NEXT_LOCALE=ko` | `307 → /ko` ❌ |
| `Cookie: NEXT_LOCALE=en` | `200 OK`，返回英文页 ✅ |

### 2.2 Accept-Language 请求头触发

即使用户清除 Cookie，如果浏览器 `Accept-Language` 请求头包含韩语优先级，服务器同样会触发重定向：

```bash
# 携带韩语 Accept-Language 时触发重定向
curl -H "Accept-Language: ko-KR,ko;q=0.9" https://thetawave.ai/
# → HTTP/1.1 307 → Location: /ko

# 携带英语 Accept-Language 时不触发
curl -H "Accept-Language: en-US,en;q=0.9" https://thetawave.ai/
# → HTTP/1.1 200 OK
```

### 2.3 优先级

```
Cookie (NEXT_LOCALE) > Accept-Language 请求头 > defaultLocale (en)
```

Cookie 和 Accept-Language 任一命中非默认语言，均会触发 307 重定向。

---

## 三、技术实现

### 3.1 Next.js i18n 动态路由

首页路由为 `/[locale]` 动态路由，由 Next.js i18n 中间件（middleware）处理：

```http
X-Matched-Path: /[locale]
```

支持的 locale（从 hreflang 标签推断）：

| 路径 | 语言 |
|------|------|
| `/` | 英语（默认 / x-default） |
| `/ko` | 韩语 |
| `/ja` | 日语 |
| `/zh` | 简体中文 |
| `/zh-tw` | 繁体中文 |
| `/de` | 德语 |
| `/es` | 西班牙语 |
| `/fr` | 法语 |
| `/it` | 意大利语 |
| `/pt` | 葡萄牙语 |

### 3.2 重定向逻辑推测（Next.js middleware）

```typescript
// middleware.ts 大致逻辑
import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;
  
  // 如果路径已包含 locale 前缀，跳过
  if (pathname.match(/^\/(ko|ja|zh|de|es|fr|it|pt|zh-tw)(\/|$)/)) {
    return NextResponse.next();
  }
  
  // 检查 Cookie
  const cookieLocale = request.cookies.get('NEXT_LOCALE')?.value;
  if (cookieLocale && cookieLocale !== 'en') {
    return NextResponse.redirect(new URL(`/${cookieLocale}`, request.url), 307);
  }
  
  // 检查 Accept-Language
  const acceptLang = request.headers.get('accept-language') || '';
  const detectedLocale = detectLocale(acceptLang);
  if (detectedLocale && detectedLocale !== 'en') {
    return NextResponse.redirect(new URL(`/${detectedLocale}`, request.url), 307);
  }
  
  return NextResponse.next();
}
```

### 3.3 hreflang 标签配置

网站配置了完善的 hreflang 标签：

```http
Link: <https://thetawave.ai/de>; rel="alternate"; hreflang="de"
Link: <https://thetawave.ai/>; rel="alternate"; hreflang="en"
Link: <https://thetawave.ai/es>; rel="alternate"; hreflang="es"
Link: <https://thetawave.ai/fr>; rel="alternate"; hreflang="fr"
Link: <https://thetawave.ai/it>; rel="alternate"; hreflang="it"
Link: <https://thetawave.ai/ja>; rel="alternate"; hreflang="ja"
Link: <https://thetawave.ai/ko>; rel="alternate"; hreflang="ko"
Link: <https://thetawave.ai/pt>; rel="alternate"; hreflang="pt"
Link: <https://thetawave.ai/zh>; rel="alternate"; hreflang="zh"
Link: <https://thetawave.ai/zh-tw>; rel="alternate"; hreflang="zh-tw"
Link: <https://thetawave.ai/>; rel="alternate"; hreflang="x-default"
```

---

## 四、其他页面不受影响的原因

### 4.1 /study 页面行为

对于 `/study` 等非首页路由，**三种触发条件下均不会发生重定向**：

| 测试条件 | /study 结果 |
|----------|-------------|
| `Cookie: NEXT_LOCALE=ko` | `200 OK`，无重定向 ✅ |
| 无 Cookie | `200 OK`，无重定向 ✅ |
| `Accept-Language: ko` | `200 OK`，无重定向 ✅ |

### 4.2 原因分析

`<https://thetawave.ai/study>` 的路由匹配为固定路径：

```http
X-Matched-Path: /study
```

而非 `/[locale]` 动态路由。这说明 `/study` 不在 i18n 中间件的处理范围内，它使用独立的静态路由，不参与语言检测和重定向逻辑。

### 4.3 路由架构推断

```
/                            → /[locale]        ← i18n 动态路由（有重定向）
/ko                          → /[locale]        ← i18n 动态路由
/ja                          → /[locale]        ← i18n 动态路由
...
/study                       → /study           ← 静态路由（无重定向）
/study/xxx                   → /study/xxx       ← 静态路由
/download                    → 静态路由          ← 独立页面
/pricing                     → 静态路由          ← 独立页面
/blog                        → 静态路由          ← 独立页面
...
```

也就是说，**只有首页使用了 `[locale]` 动态路由**，其他所有子页面（/study、/blog、/download 等）均为固定路径，不受语言自动重定向影响。

---

## 五、SEO 影响评估

### 5.1 积极方面

- **hreflang 标签完善**：所有语言版本都有对应的 `rel="alternate" hreflang="xx"` 标签，`x-default` 指向英文首页
- **独立 URL**：每个语言版本有独立可索引的 URL
- **/study 等子页面不受重定向影响**：Google 可以正常抓取和索引这些页面

### 5.2 风险方面

- **基于 Cookie/Accept-Language 的自动重定向是 Google 明确不推荐的做法**。Google 搜索中心文档指出：
  > "Avoid automatic redirection based on the user's perceived language. These redirections could prevent users (and search engines) from viewing all the versions of your site."

- `307 Temporary Redirect` 语义上为"临时重定向"。当 Googlebot 以美国 IP 抓取 `https://thetawave.ai/` 时不会触发重定向（Accept-Language 通常为 en），但当 Googlebot 使用其他地区 IP 时可能会被重定向
- 未设置 `Vary: Accept-Language` 响应头，搜索引擎缓存可能无法正确区分不同语言版本
- 被重定向后 `/ko` 页面不再写入 `NEXT_LOCALE` Cookie（仅首页 307 响应中有），可能导致后续行为不一致

### 5.3 总体评估

影响相对有限，因为：
1. 首页是唯一受影响的页面，/study、/blog 等 SEO 内容页面均不受影响
2. hreflang 标签配置完善，Google 能正确理解各语言版本关系
3. Googlebot 通常以 en-US Accept-Language 爬取，不触发重定向

但为了最佳实践，仍建议优化。

---

## 六、改进建议

### 6.1 短期方案

1. **添加 `Vary: Accept-Language` 响应头**：
   ```
   Vary: Accept-Language, Cookie
   ```
   告知 CDN 和搜索引擎，该页面响应内容因语言头和 Cookie 而异。

2. **将 307 改为 302**：语义更准确（302 Found 同样表示临时重定向，但对搜索引擎更友好）。

### 6.2 长期方案（推荐）

1. **关闭自动语言检测**，改为在页面上展示语言选择器 banner。用户首次访问始终看到默认英文页，由用户主动选择语言。

2. **如果需要保留语言检测**，至少区分对待搜索引擎爬虫：
   - 对 Googlebot（User-Agent 检测）返回英文首页 + 完整的 hreflang 标签
   - 对真实用户再做自动重定向

3. **统一重定向来源**：当前 Cookie 和 Accept-Language 两套机制并存，建议统一为单一的检测逻辑，减少不可预测的行为。

---

## 七、如何手动清除 Cookie 恢复正常

### Chrome / Edge

1. 按 `F12` 打开开发者工具
2. 切换到 **Application**（应用程序）标签
3. 左侧 **Cookies** → 找到 `thetawave.ai`
4. 选中 `NEXT_LOCALE` → 点击删除（或右键 → Delete）
5. 刷新页面

### 无痕模式

直接使用浏览器的无痕/隐私模式访问 `https://thetawave.ai/`，无痕模式不携带历史 Cookie，不会触发重定向。

---

## 八、总结

| 项目 | 详情 |
|------|------|
| **触发原因** | `NEXT_LOCALE=ko` Cookie + Accept-Language 双重检测 |
| **技术实现** | Next.js `/[locale]` 动态路由 + middleware 重定向 |
| **受影响页面** | 仅首页 `/`，其他页面（/study, /blog 等）不受影响 |
| **SEO 影响** | 有限，但 Google 不推荐此做法 |
| **解决方法** | 清除 `NEXT_LOCALE` Cookie 或使用无痕模式 |
| **最佳实践** | 关闭自动语言检测，让用户手动选择语言 |
