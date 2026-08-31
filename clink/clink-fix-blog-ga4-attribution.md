# Clink 任务单 — Blog 与主站 GA4 归因统一

> **任务类型**：Analytics / 站内归因（Measurement）
> **目标域名**：clinkbill.com
> **状态**：待处理
> **优先级**：P2（Blog 流量无法进入主站 GA4 属性，增长/渠道/转化归因断裂；不影响 GSC/Bing 搜索侧数据）
> **提交**：2026-08-31
> **关联文档**：[clink-site-structure.md](./clink-site-structure.md) · [clink-fix-canonical-host.md](./clink-fix-canonical-host.md)

---

## 1. 任务目标

在 **Blog 仓库**（经 CloudFront 反向代理至 `clinkbill.com/blog` 的 Vercel Next.js App Router 应用）部署与 **主站相同的 GA4 Measurement ID**，使 Blog 页面产生可计入同一 GA4 属性的 `page_view` / session 数据。

**完成判定标准**：

1. Blog 列表页与文章页 HTML 或 JS bundle 中可检出 GA4 ID `G-0YGZ90TPXH`（或与主站一致的 gtag 实现）；
2. GA4 DebugView / Realtime 中，直接访问 `https://clinkbill.com/blog` 及任意文章 URL 可看到 page_view；
3. 主站与 Blog 会话在 **同一 GA4 属性** 内可按 `page_path`（如 `/blog/*`）区分，无需新建 property。

**不在本任务范围**（可另开任务单）：

- GSC / Bing 站长工具配置（已可不依赖页面埋点覆盖 Blog SEO 数据，见 §3.2）；
- GTM 迁移或 CloudFront 边缘统一注入；
- www / 裸域 host 统一（见 [clink-fix-canonical-host.md](./clink-fix-canonical-host.md)）。

---

## 2. 问题证据（2026-08-31 实测）

### 2.1 架构：主站与 Blog 为两套独立 Next.js 构建

| 属性 | 主站 `/` | Blog `/blog` |
|------|----------|--------------|
| 示例 URL | https://clinkbill.com/ | https://clinkbill.com/blog |
| Router | Pages Router（`pages/_app-*.js`） | App Router（`main-app-*.js`、`app/blog/*`） |
| 响应头 | `X-Powered-By: Next.js` | `server: Vercel` |
| CDN | CloudFront | CloudFront → Vercel 回源 |
| build 指纹 | `buildId: 1b0445e383329ee54cb98940c5b97a602955d1dd` | 独立 webpack chunk（如 `webpack-f49ab86a249e0a1f.js`） |

反向代理仅统一 **URL 路径**，**不会**自动继承主站前端资源或统计代码。

### 2.2 主站：已部署 GA4（direct gtag，非 GTM）

主站共享 bundle `/_next/static/chunks/pages/_app-40f74f9cd1f842ed.js` 中含：

```javascript
// next/script, strategy: afterInteractive
src: "https://www.googletagmanager.com/gtag/js?id=G-0YGZ90TPXH"
// ...
gtag('config', 'G-0YGZ90TPXH')
```

对 `https://clinkbill.com/` 及 `/_next/static/chunks/pages/_app-*.js` 扫描结果：

- GA4 ID：`G-0YGZ90TPXH` ✅
- GTM 容器 ID：无
- `googletagmanager.com/gtag/js` 引用：有

### 2.3 Blog：无任何 GA / GTM 实现

对 `https://clinkbill.com/blog`、`https://clinkbill.com/blog/what-is-clink` 的 **初始 HTML** 及 **全部引用的 JS chunk**（11–12 个）扫描结果：

- GA4 ID：无
- GTM ID：无
- `gtag()` / `googletagmanager.com`：无
- 是否包含主站 ID `G-0YGZ90TPXH`：否

Blog 面包屑 JSON-LD 仍引用 origin 域名（佐证为独立部署）：

```json
"item": "https://clink-ai.lovable.app/"
```

（`/blog/monthly-recurring-revenue` 页面源码，2026-08-31 抽验。）

### 2.4 数据断裂示例

| 用户路径 | GSC（搜索侧） | GA4（站内行为） |
|----------|---------------|-----------------|
| Google → `clinkbill.com/blog/xxx` | ✅ 可有点击/query（无需 Blog 埋点） | ❌ 无 session |
| Google → 首页 → 点击进入 Blog | ✅ 各 URL 可有搜索数据 | ⚠️ 仅首页有 session；进入 Blog 后 pageview 丢失 |
| 广告/邮件/社交 → Blog | ❌ 不涉及 | ❌ 完全不可见 |

---

## 3. 根因分析

### 3.1 为什么 Blog 没有 GA4？

1. **两套代码库、两套 `_app` / `layout`**：主站在 Pages Router 的 `_app` 中注入了 GA4；Blog 为 App Router 独立项目，root layout 未接入相同 snippet。
2. **反向代理不传递统计逻辑**：CloudFront 将 `/blog/*` 转发至 Vercel origin，返回的是 Blog 应用的 HTML/JS，与主站 `_app.js` 无关。
3. **同域名 ≠ 同 GA 配置**：GA4 依赖页面加载 gtag/GTM；域名一致不能替代客户端实现。

参考：[GA4 设置文档](https://support.google.com/analytics/answer/9304153) — 须在页面或 GTM 容器中部署 Measurement ID 才会收集事件。

### 3.2 哪些平台「无 Blog 埋点」仍能看到 Blog 数据？

以下结论供产品/增长侧理解「缺 GA 仍能看到什么」；**不能替代** Blog GA4 部署。

| 平台 | 无 Blog 埋点能否看到 Blog | 数据来源 | 典型指标 |
|------|---------------------------|----------|----------|
| **Google Search Console** | ✅ 可以 | Google 爬虫 + 搜索结果 | 展示、点击、query、索引、抓取错误 |
| **Bing Webmaster Tools** | ✅ 可以 | Bing 爬虫 + Site Explorer | `/blog/` 文件夹点击、展示、索引状态 |
| **GA4（Blog 页面本身）** | ❌ 不可以 | 需 gtag/GTM/MP | sessions、events、转化、渠道归因 |
| **GA4 ↔ GSC 关联报告** | ⚠️ 部分 | GSC 侧着陆页 + 有限 GA 指标 | 可见 `/blog/*` 的 **搜索** 点击/impression；**无** Blog 上完整行为链 |
| **GTM** | ❌ 不可以 | 需容器 snippet | 依赖 GTM 的所有标签 |
| **广告像素 / Clarity 等** | ❌ 不可以 | 需各自 script | 转化、录屏、热力图 |
| **CloudFront / Vercel 访问日志** | ✅ 若已开启 | 服务器/边缘日志 | 请求量、URL、Referer（非搜索词） |

**GSC** 通过 [DNS 域属性验证](https://support.google.com/webmasters/answer/9008080) 覆盖 `clinkbill.com` 下全部路径，**不需要**页面 Analytics 代码。见 [Add a Search Console property](https://support.google.com/webmasters/answer/34592)。

**Bing Webmaster Tools** 通过 meta / `BingSiteAuth.xml` 验证站点，**不部署** visitor-facing tracking script；[Site Explorer](https://blogs.bing.com/webmaster/January-2024/Mastering-Website-Management-with-Site-Explorer) 可按 `/blog/` 目录查看 SEO 指标。

**GA4 关联 GSC** 后可在 Admin → [Search Console Links](https://support.google.com/analytics/answer/10737381) 查看 Organic Search Queries / Traffic 报告，但 Blog 无埋点时 **GSC 显示「有人从 Google 点进 blog」≠ GA 记录了完整访问行为**。

---

## 4. 影响范围

| 范围 | 是否有 GA4 | 说明 |
|------|------------|------|
| 主站 `/` | ✅ `G-0YGZ90TPXH` | Pages Router `_app` |
| 主站 `/products/*`、`/contact` 等 Pages Router 页 | ✅ 预期同 `_app` | 与首页共用 bundle |
| Blog `/blog` 列表 | ❌ | App Router，Vercel |
| Blog `/blog/{slug}` 全部文章 | ❌ | 已抽验 `what-is-clink`、`monthly-recurring-revenue` |
| GSC / Bing 中 Blog SEO 报表 | ✅ 独立可用 | 与 GA 埋点无关 |

**抽验记录（2026-08-31）**：`/`、`/blog`、`/blog/what-is-clink`、`/products/billing`（billing 因 SSL 偶发中断，主站 `_app` 与首页结论一致）。

---

## 5. 修复要求

### 5.1 修复位置

**Blog 仓库**（Vercel 部署、App Router）：

1. 定位 root layout：通常为 `app/layout.tsx`（或等价的 `app/(marketing)/layout.tsx`）。
2. 搜索关键词：`layout.tsx`、`GoogleAnalytics`、`gtag`、`next/script`、`NEXT_PUBLIC_GA`。
3. **不要**在主站 Pages Router 仓库重复添加（主站已有）；**仅 Blog 仓库**缺失。

可选替代方案（若团队希望两站统一由标签管理）：

- 在 **CloudFront** 对 `clinkbill.com/*` 统一注入 GTM 容器（需另定 GTM ID，超出本任务最小范围）。

### 5.2 规则（必须满足）

1. **Measurement ID 与主站一致**：使用 `G-0YGZ90TPXH`，禁止为 Blog 单独新建 GA4 property（除非产品明确要求拆分报表）。
2. **覆盖全部 Blog 路由**：`/blog` 列表 + `/blog/[slug]` 及未来子路径均通过 root layout 继承。
3. **加载策略**：与主站一致，推荐 `next/script` + `strategy="afterInteractive"`，避免阻塞 LCP。
4. **不要用 GSC 关联代替埋点**：GSC 链接不能产生 page_view。
5. **部署环境**：Production（经 CloudFront 反代的 `clinkbill.com/blog`）必须生效；Preview 可用同一 ID 或环境变量区分（若区分须在验收中说明）。
6. **Consent（若站点有 CMP）**：若主站有同意模式（Consent Mode），Blog 须对齐同一逻辑，避免欧盟流量统计偏差。

### 5.3 修复后的期望输出

Blog 任意页面（如 `/blog`）源码或 hydration 后应等价于主站实现。期望在 layout 中呈现：

```tsx
import Script from "next/script";

const GA_MEASUREMENT_ID = "G-0YGZ90TPXH";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Script
          src={`https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`}
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '${GA_MEASUREMENT_ID}');
          `}
        </Script>
      </body>
    </html>
  );
}
```

**验收时在页面中应能检出**：

```html
<script src="https://www.googletagmanager.com/gtag/js?id=G-0YGZ90TPXH" ...></script>
```

且 `gtag('config', 'G-0YGZ90TPXH')` 被执行。

> 以上为示意；App Router 现有 `<html>` / `<body>` 结构、字体、metadata 等按项目实际合并，勿破坏现有 layout。

### 5.4 代码级参考（环境变量，可选）

若 Blog 项目已使用 `NEXT_PUBLIC_*` 常量：

```env
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-0YGZ90TPXH
```

```tsx
const GA_ID = process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID;
// 仅当 GA_ID 存在时注入 script，避免 preview 环境误报
```

主站 `_app` 当前为硬编码 ID；Blog 可用 env，但 **Production 值必须与主站一致**。

### 5.5 建议同步修复（同 PR 可选，不阻断本任务验收）

Blog 面包屑 schema 中 `clink-ai.lovable.app` → `https://clinkbill.com`（见 [archive/clink-fix-breadcrumb-schema.md](./archive/clink-fix-breadcrumb-schema.md)）。

---

## 6. 验收标准

### 6.1 代码与页面

- [ ] `https://clinkbill.com/blog` 页面可检出 `G-0YGZ90TPXH` 或 `gtag/js?id=G-0YGZ90TPXH`
- [ ] 抽查 ≥3 篇文章 URL（如 `/blog/what-is-clink`、`/blog/monthly-recurring-revenue`、`/blog/smart-routing`）均有相同 GA 实现
- [ ] Blog JS bundle 扫描：`G-0YGZ90TPXH` 或内联 gtag config 存在；无第二套冲突 GA ID

### 6.2 GA4 实时验证

- [ ] GA4 属性 `G-0YGZ90TPXH` → **Realtime** 或 **DebugView**（`debug_mode: true` 或 [Tag Assistant](https://tagassistant.google.com/)）中，访问 Blog URL 可见 `page_view`
- [ ] `page_location` / `page_path` 为 `https://clinkbill.com/blog...`（非 `clink-ai.lovable.app`）
- [ ] 从首页点击进入 Blog 后，同一 session 内可见连续 page_view（非仅首页一条）

### 6.3 回归

- [ ] 主站 `https://clinkbill.com/` 仍正常加载 GA，ID 未变
- [ ] Blog 页面 LCP / 控制台无 Script 相关报错（目视即可）

### 6.4 平台预期（确认「该有仍有、该无仍无」）

- [ ] GSC 中 `/blog/*` 搜索数据 **不受本修复影响**（修复前后均应存在，若已验证域属性）
- [ ] 修复前 GA4 报表中 Blog 直接流量为 0 或显著偏低；修复后 24–48h 内 Explore 按 `page_path begins with /blog` 可看到 sessions

---

## 附录 A — 自检命令（审计方 / 对方 agent 可用）

```bash
# 1. 主站 _app 是否仍含 GA4
curl -sL "https://clinkbill.com/_next/static/chunks/pages/_app-40f74f9cd1f842ed.js" | grep -o "G-0YGZ90TPXH"

# 2. Blog 列表页 HTML 是否含 GA（修复后应有多行输出）
curl -sL "https://clinkbill.com/blog" | grep -o "G-0YGZ90TPXH"

# 3. 响应头确认 Blog 仍走 Vercel 回源
curl -sI "https://clinkbill.com/blog" | grep -i server
```

---

## 附录 B — 决策记录（2026-08-31 审计结论）

| 问题 | 结论 |
|------|------|
| Blog 与首页是否同一 GA 代码？ | **否**。主站 `G-0YGZ90TPXH`；Blog 无实现。 |
| 反向代理能否自动统一 GA？ | **否**。需 Blog 代码库或边缘注入。 |
| 无埋点时 GSC/Bing 能否看 Blog？ | **能**。搜索/索引数据不依赖 GA。 |
| 无埋点时 GA 能否看 Blog 站内行为？ | **不能**。GSC 关联仅补充有限搜索着陆页指标。 |

---

*本任务单由外部 SEO / 增长审计提交，供 Clink Blog 仓库维护方 agent 直接执行。完成后可归档至 `clink/archive/`。*
