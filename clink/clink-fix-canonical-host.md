# Clink 任务单 — 统一 www / 裸域 301 重定向

> **任务类型**：Technical SEO（域名规范化 / Host Consolidation）
> **目标域名**：clinkbill.com
> **状态**：待处理
> **优先级**：P0（全站 www 与裸域并存可访问；主站与 Blog 两仓库 host 信号不一致，直接影响索引合并与链接权重）
> **提交**：2026-08-26
> **关联任务**：[clink-fix-canonical-tag.md](./clink-fix-canonical-tag.md)（页面级 canonical tag，独立问题）

---

## 问题概述

### 问题是什么

Clink 当前在 **两个独立仓库 / 部署** 上对外服务同一域名 `clinkbill.com`：

| 属性 | 主站仓库 | Blog 仓库 |
|------|----------|-----------|
| 示例 URL | [https://www.clinkbill.com/](https://www.clinkbill.com/) | [https://clinkbill.com/blog/monthly-recurring-revenue](https://clinkbill.com/blog/monthly-recurring-revenue) |
| 部署 | Next.js + CloudFront | Next.js + Vercel（经 CloudFront 回源） |
| 当前倾向的 host | sitemap / robots 使用 `www` | 正文内链、项目配置使用裸域 `clinkbill.com` |

**核心缺陷**：`https://www.clinkbill.com/*` 与 `https://clinkbill.com/*` **均可直接 200 访问**，两者之间 **没有 301 互跳**。Google 会把 www 与裸域视为两个可索引副本，无法判定「唯一官方 host」。

### 会造成什么影响

1. **重复内容（Duplicate Content）**  
   同一页面存在 `www` 与裸域两个可抓取 URL，爬虫预算被分散，Google 需在两者间自行选择索引副本，索引状态不可控。

2. **链接权重（Link Equity）被稀释**  
   外链、社媒分享、内链若混用两种 host，PageRank / 权重无法汇聚到单一 URL，削弱排名与品牌 SERP 稳定性。

3. **GSC 数据分裂**  
   Google Search Console 中 www 与裸域可能被当作不同资源；若未做 Domain property 或未统一重定向，展示、点击、覆盖率报表会失真，难以评估 SEO 成效。

4. **主站与 Blog 信号冲突**  
   主站 sitemap 提交 `https://www.clinkbill.com/...`，Blog 正文链到 `https://clinkbill.com/contact` 等裸域 URL，向搜索引擎发送矛盾的「首选 host」信号，Blog 内容更难与主站形成统一的站点权威。

5. **分析与分享口径混乱**  
   同一篇文章可能以两种 URL 被访问、被分享；Referrer、UTM 无法保证一致，运营与增长数据难以对齐。

---

## 1. 任务目标

为 clinkbill.com **选定唯一首选 host**，并在 **主站仓库 + Blog 仓库 + CDN/DNS 层** 完成：

1. 非首选 host → 首选 host 的 **301 Permanent Redirect**（全路径保留，含 query string）；
2. sitemap、robots.txt、站内绝对内链中的 URL **全部统一为首选 host**；
3. HTTP → HTTPS 跳转链最终落在首选 host 上（例如 `http://clinkbill.com/` → `https://www.clinkbill.com/`）。

**建议首选 host**：`https://www.clinkbill.com`（与现有 [sitemap](https://www.clinkbill.com/sitemap.xml) 及 robots.txt `Host` 声明一致）。若产品方决定改用裸域，两仓库须 **同时** 改 redirect + sitemap + 内链常量，禁止只改一侧。

> 页面级 `<link rel="canonical">` 与 `og:url` 见独立任务单 [clink-fix-canonical-tag.md](./clink-fix-canonical-tag.md)。

---

## 2. 问题证据（2026-08-26 实测）

### 2.1 HTTPS：www 与裸域均 200，无互跳

```http
# https://www.clinkbill.com/
HTTP/1.1 200 OK
X-Powered-By: Next.js
Via: ...cloudfront.net (CloudFront)

# https://clinkbill.com/
HTTP/1.1 200 OK
X-Powered-By: Next.js
Via: ...cloudfront.net (CloudFront)
ETag: "15f7u0pjl1q1wdh"   ← 与 www 版本相同，确认为同一 HTML 副本
```

Blog 文章 `/blog/monthly-recurring-revenue` 在 www 与裸域下同样均为 **200 OK**，`Content-Length: 71252`、`etag` 一致，`server: Vercel`。

### 2.2 HTTP → HTTPS 保留 host 变体（未收敛到单一 host）

```http
# http://www.clinkbill.com/
HTTP/1.1 301 Moved Permanently
Location: https://www.clinkbill.com/

# http://clinkbill.com/
HTTP/1.1 301 Moved Permanently
Location: https://clinkbill.com/
```

HTTPS 层未再合并 www / 裸域。

### 2.3 sitemap / robots 与 Blog 内链 host 不一致

**robots.txt**（www 与裸域返回内容相同）：

```text
Host: https://www.clinkbill.com
Sitemap: https://www.clinkbill.com/sitemap.xml
```

> 注：`Host` 指令仅 Yandex 使用；Google **不** 据此选首选 host，**不能替代 301**。

**sitemap.xml** 中 URL 均为 `www` 前缀，且 **未包含任何 `/blog/*` 路径**（Blog sitemap 另项跟进）。

**Blog 正文内链**（`/blog/monthly-recurring-revenue` 页面源码）使用裸域：

```html
<a href="https://clinkbill.com/contact" ...>Contact Sales</a>
```

Blog 仓库项目配置（`skills/clink-blog-article/references/project-config.md`）亦声明 **主域名 `clinkbill.com`**（无 `www`），与主站 sitemap 冲突。

---

## 3. 根因分析

1. **CDN / 边缘层未配置 apex ↔ www 301**  
   CloudFront（或上游 DNS）同时接受 `www.clinkbill.com` 与 `clinkbill.com` 的 HTTPS 请求并回源，未将非首选 host 301 到首选 host。这是 duplicate URL 的直接原因。

2. **两仓库独立维护 SITE_URL，未统一**  
   主站 sitemap 生成逻辑使用 `https://www.clinkbill.com`；Blog 仓库的 `SITE_URL`、内链模板、分享 URL 使用 `https://clinkbill.com`。缺少跨仓库的 host 常量与 CI 校验。

3. **robots.txt `Host` 被误当作 Google 规范化信号**  
   `Host: https://www.clinkbill.com` 对 Google 无效，造成「看似已配置、实际未生效」的假象。

因果链：**双 host 可访问** + **无 301** + **跨仓库 URL 常量不一致** → 重复 URL 被索引 → 权重分散、GSC 分裂、Blog SEO 与主站无法形成合力。

---

## 4. 影响范围

| 范围 | 说明 |
|------|------|
| **全站所有路径** | 任意 `https://clinkbill.com{path}` 与 `https://www.clinkbill.com{path}` 均可能形成重复副本 |
| **主站仓库** | 首页、产品页、`/agentic-payment`、`/skills`、`/contact`、法务页等；sitemap / robots 生成 |
| **Blog 仓库** | `/blog`、`/blog/{slug}` 全部文章；内链、分享按钮 |
| **边缘 / 基础设施** | CloudFront、Vercel 自定义域、DNS（A/AAAA/CNAME） |

已抽验页面：

| 页面 | www 200 | 裸域 200 |
|------|---------|----------|
| `/` | ✅ | ✅ |
| `/products/billing` | ✅ | ✅ |
| `/blog/monthly-recurring-revenue` | ✅ | ✅ |

---

## 5. 修复要求

### 5.1 修复位置

**基础设施层（优先）**

- CloudFront Distribution / ALB / Nginx：配置 **非首选 host → 首选 host** 的 301
- Vercel 项目（Blog）：Domains 设置中指定 Primary Domain，启用 redirect
- DNS：确认 apex 与 www 均指向正确入口，且 redirect 在 HTTPS 层生效

**主站仓库**

- 全局 `SITE_URL` / `NEXT_PUBLIC_SITE_URL` 环境变量
- sitemap 生成器、robots.txt 生成器
- 站内绝对内链模板

**Blog 仓库**

- `SITE_URL` 环境变量与内链 / CTA / 分享 URL 模板
- Blog 专用 sitemap（若存在）及向主 robots 的 `Sitemap:` 声明

**跨仓库**

- 统一常量或 env：`SITE_URL=https://www.clinkbill.com`（若改用裸域则同步改两处）
- 禁止硬编码另一种 host 的绝对 URL

### 5.2 规则（必须满足）

1. **单一首选 host**：全站只承认一个 host（建议 `https://www.clinkbill.com`）。
2. **301 永久重定向**：非首选 host 的任意路径（含 `/blog/*`）必须 301 到首选 host 等价路径；禁止 302/307（除非临时维护）。
3. **保留 path 与 query**：`https://clinkbill.com/blog/foo?utm=1` → `https://www.clinkbill.com/blog/foo?utm=1`。
4. **HTTP 链收敛**：`http://clinkbill.com/*` 与 `http://www.clinkbill.com/*` 最终均到 `https://www.clinkbill.com/*`（一步或两步跳转均可，但最终 URL 必须唯一）。
5. **不引入 mixed host 内链**：修复后站内新产生的绝对链接不得再混用 `www` / 裸域。
6. **sitemap / robots 与 redirect 一致**：sitemap 中 `<loc>` 与 robots `Sitemap:` 均使用首选 host。

### 5.3 修复后的期望输出

**边缘 301（以首选 host = www 为例）**

```http
GET https://clinkbill.com/blog/monthly-recurring-revenue HTTP/1.1

HTTP/1.1 301 Moved Permanently
Location: https://www.clinkbill.com/blog/monthly-recurring-revenue
```

**Blog 正文内链（修复后）**

```html
<a href="https://www.clinkbill.com/contact">Contact Sales</a>
```

**robots.txt**

```text
User-agent: *
Allow: /

Sitemap: https://www.clinkbill.com/sitemap.xml
Sitemap: https://www.clinkbill.com/blog/sitemap.xml
```

> 若保留 Yandex `Host` 指令，须与首选 host 一致。

### 5.4 代码级参考（示意，按项目实际实现调整）

**CloudFront Function / Lambda@Edge（伪代码）**

```javascript
function handler(event) {
  var request = event.request;
  var host = request.headers.host.value;
  if (host === "clinkbill.com") {
    var uri = request.uri;
    var qs = request.querystring ? "?" + request.querystring : "";
    return {
      statusCode: 301,
      statusDescription: "Moved Permanently",
      headers: {
        location: { value: "https://www.clinkbill.com" + uri + qs },
      },
    };
  }
  return request;
}
```

**环境变量（两仓库对齐）**

```env
NEXT_PUBLIC_SITE_URL=https://www.clinkbill.com
```

---

## 6. 验收标准

- [ ] `curl -I https://clinkbill.com/` 返回 **301**，`Location: https://www.clinkbill.com/`
- [ ] `curl -I https://clinkbill.com/blog/monthly-recurring-revenue` 返回 **301** 到 `https://www.clinkbill.com/blog/monthly-recurring-revenue`
- [ ] `curl -I https://www.clinkbill.com/` 返回 **200**（首选 host 可直接访问）
- [ ] `curl -I http://clinkbill.com/` 经跳转链最终到达 `https://www.clinkbill.com/`
- [ ] Blog 正文抽样 3 篇文章，绝对内链不再出现 `https://clinkbill.com/`（无 www 的裸域形式）
- [ ] `https://www.clinkbill.com/sitemap.xml` 中所有 `<loc>` 使用首选 host
- [ ] Blog sitemap（若有）中所有 `<loc>` 使用首选 host
- [ ] [Google URL Inspection](https://search.google.com/search-console) 对裸域 URL 显示「重定向到首选 host」或不再作为独立索引 URL
- [ ] 部署后 2 周内 GSC 中 duplicate URL 相关警告趋势下降（需等待重新抓取）

---

*本任务单由外部 SEO 审计/协作方提交，供 Clink 方 agent 直接执行。完成后请将本文档移入 `clink/archive/`。*
