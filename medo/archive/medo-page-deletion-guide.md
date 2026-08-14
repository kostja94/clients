
# MeDo 页面删除方案指南：noindex vs 410 vs 301

> **适用场景**：需要永久删除大量页面（如 `/apps/*`）且页面无替代页时的 SEO 与技术方案  
> **关联文档**：[medo-indexing-diagnosis.md](./medo-indexing-diagnosis.md)、[medo-dual-domain-seo-strategy.md](./medo-dual-domain-seo-strategy.md)

---

## 一、核心结论

**返回 410 Gone + 自定义说明页（最佳实践）**

当页面需要永久删除且无相关替代页时，不要用 301 重定向到首页或通用说明页，也不要用 robots.txt Disallow 作为主手段。

---

## 二、为什么不推荐 301 重定向到说明页

### 2.1 Google 官方立场

来自 [Google Search Console Help](https://support.google.com/webmasters/answer/2445990)：

> "If you have permanently deleted content without intending to replace it with newer, related content, let the old URL return a **404 or 410**. Returning a code other than 404 or 410 for a non-existent page (or redirecting users to another page, such as the homepage, instead of returning a 404) can be problematic. Such pages are called **soft 404s**, and can be confusing to both users and search engines."

### 2.2 Soft 404 机制

当你把大量页面 301 重定向到一个通用说明页时：

1. 原 URL 是具体 App 页面（如 `/apps/app-xxx`）
2. 目标 URL 是不相关的通用说明页（如 `/content-removed`）
3. Google 判断主题不匹配 → 判定为 **Soft 404**
4. 后果：原 URL 的链接权重 **全部作废**，排名清零，索引最终被清除 — 和直接删除效果一样，但耗时更长

来自 John Mueller（Google 高级搜索分析师）的原话：

> "Redirects to the homepage or non-relevant pages can be treated as **soft 404s**. Google will essentially view the original pages as 404s and eventually remove them from the index."

来自 [GSQi 案例验证](https://www.gsqi.com/marketing-blog/redirects-less-relevant-pages-soft-404s/)：

> "Your nifty redirect to save search equity will actually mean nothing. The new page will not retain the rankings and traffic of the old page."

### 2.3 301 vs 410 决策对比

| 手段 | 搜索引擎处理 | 索引导清除速度 | 用户体验 | 链接权重 | 适用场景 |
|------|------------|-------------|---------|---------|---------|
| **301 到相关替代页** | 正常重定向 | — | 自动跳转 | ✅ 传递 | 有1:1语义相近的替代页 |
| **301 到首页/通用页** | Soft 404 | 缓慢（同404） | ❌ 主题不匹配跳转 | ❌ 作废 | 永远不适用 |
| **noindex** | 从索引移除 | 慢（需等重抓） | ✅ 页面正常访问 | ✅ follow保留 | 页面需保留用户访问 |
| **410 Gone** | 永久删除信号 | **快（几天到2周）** | ✅ 自定义说明页 | ❌ 作废 | 永久删除，无替代页 |
| **404 Not Found** | 临时缺失信号 | 慢（数周到6月） | — | ❌ 作废 | 不确定是否永久 |

---

## 三、410 vs 404 速度对比数据

### 3.1 Reboot Online 对照实验

实验设计：119 个已索引页面，一半返回 404，一半返回 410，观察 Googlebot 重抓频率

结果：**404 URL 被 Google 重抓的频率比 410 URL 高 49.6%**

> "An analysis of the Google Search Console API data shows that 404's are, on average, crawled 49.6% more often than 410's."

### 3.2 Search Engine Zine 三域对照测试

在三个电商域名上进行对照测试：

| 状态码 | 平均索引清除时间 |
|--------|----------------|
| 410 Gone | **4 天** |
| 404 Not Found | **12 天** |

结论：**410 比 404 快 3 倍**。

### 3.3 10,000 条 URL 规模对比

来自 [Gautam Khorana](https://gautamkhorana.com/blog/410-vs-404-status-codes-for-seo/)：

> "A site with 10,000 retired URLs split 50/50 between 404 and 410 will see the **410 half drop from the Coverage report within two weeks**, and the **404 half drift in the Coverage report for three to six months**."

---

## 四、大规模删除操作指南

### 4.1 四类 URL 决策矩阵

| URL 类型 | 条件 | 处理 | 状态码 |
|---------|------|------|--------|
| 有替代页 | 高流量 / 有外链 / 有语义相近的替换页 | 301 重定向到替代页 | `301` |
| 永久删除（无替代） | 无流量、无外链、不需要恢复 | 返回 410 + 自定义说明页 | `410` |
| 不确定是否永久 | 可能恢复 | 返回 404 观察 | `404` |
| 敏感/违规内容 | 需紧急下架 | Removals 应急 + 410 永久处理 | `410` |

MeDo `/apps/*` 18,037 个页面属于第二类。

### 4.2 分批实施策略

大规模删除（10,000+ URL）必须分批进行：

| 参数 | 推荐值 |
|------|--------|
| 每批占比 | 索引总量的 5-10% |
| 批次间隔 | 2-4 周 |
| 继续条件 | 抓取速率稳定（≤ 基线 15%）、保留页排名不降 |

来源：[Vega SEO Talks](https://vegaseotalks.com/what-is-the-most-effective-phased-strategy-for-deindexing-200k-low-quality-pages-without-triggering-a-site-wide-crawl-rate-disruption/)

### 4.3 技术实现

**服务端返回 410（示例）**：

```nginx
# nginx — 返回 410 状态码
location ~ ^/apps/app- {
    return 410;
}

# 配合自定义 410 页面
error_page 410 /410.html;
```

```apache
# Apache .htaccess
RedirectMatch 410 ^/apps/app-.*
```

```json
// vercel.json
{
  "rewrites": [
    { "source": "/apps/app-:id", "statusCode": 410 }
  ]
}
```

### 4.4 同步清理操作

| 操作 | 说明 |
|------|------|
| 从 Sitemap 移除 | 停止提交所有 `/apps/*` URL |
| 移除站内链接 | 首页广场不再以 `<a>` 链接到 App 详情页，或改为 JS 渲染链接避免爬虫发现 |
| 监控 GSC Coverage | 确认 410 URL 的移除进度 |
| 自定义 410 页面 | 返回友好的用户说明，引导到首页/Blog |

---

## 五、自定义 410 页面示例

**关键点**：HTTP 状态码是 `410 Gone`，但返回的 HTML 是完整的用户引导页面。搜索引擎读状态码处理索引，用户看 HTML 得到引导。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>该 App 已被删除 | MeDo</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #e2e8f0;
        }
        .container {
            text-align: center;
            padding: 48px 32px;
            max-width: 520px;
        }
        .code {
            font-size: 96px;
            font-weight: 800;
            background: linear-gradient(135deg, #818cf8, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1;
            margin-bottom: 16px;
        }
        h1 {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 12px;
            color: #f1f5f9;
        }
        p {
            font-size: 16px;
            color: #94a3b8;
            line-height: 1.6;
            margin-bottom: 32px;
        }
        .actions {
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
        }
        .btn {
            display: inline-block;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.2s;
        }
        .btn-primary {
            background: #6366f1;
            color: #fff;
        }
        .btn-primary:hover {
            background: #818cf8;
        }
        .btn-secondary {
            background: rgba(255,255,255,0.08);
            color: #cbd5e1;
            border: 1px solid rgba(255,255,255,0.12);
        }
        .btn-secondary:hover {
            background: rgba(255,255,255,0.12);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="code">410</div>
        <h1>该 App 已被删除</h1>
        <p>此应用已从 MeDo 平台永久移除，不再可用。<br>你可以浏览其他优秀作品或前往文档了解更多。</p>
        <div class="actions">
            <a href="/" class="btn btn-primary">返回首页</a>
            <a href="/blog/" class="btn btn-secondary">浏览 Blog</a>
        </div>
    </div>
</body>
</html>
```

---

## 六、真实案例

### 案例一：WordPress 网络 10,500 条垃圾 URL → 12 天全部清除

- **来源**：MD Pabel，[DEV Community](https://dev.to/md_pabel_fe07e07449db7326/case-study-how-i-removed-10500-seo-spam-urls-from-google-search-in-12-days-2fcj)
- **问题**：客户 WordPress 网站被黑，10,500 条垃圾 SEO 页面被索引。404 处理需要 3-6 个月
- **方案**：对所有垃圾 URL 模式返回 HTTP 410 Gone，提交临时 Sitemap 触发 Google 重抓
- **结果**：48 小时索引开始暴跌，第 12 天全部 10,500 条 URL 清除完毕

### 案例二：日本关键词黑帽攻击 50,000+ URL → 72 小时见效

- **来源**：MD Pabel [个人博客](https://www.mdpabel.com/case-studies/how-i-removed-50000-spam-urls-from-google-after-a-japanese-keyword-hack/)
- **问题**：客户网站被注入 50,000+ 条日文垃圾页面，品牌搜索结果被日文标题淹没
- **方案**：对所有黑帽 URL 模式返回服务器端 410 Gone（WordPress 加载之前就返回）
- **结果**：Day 1 服务器负载急降、Day 2 GSC 开始反映清除、Day 3 品牌搜索结果恢复正常

### 案例三：全球旅游网站 120 万条过期页面 → 流量增长 22%

- **来源**：Search Engine Zine [企业级 SEO 指南](https://searchenginezine.com/seo/logic/404-vs-410-for-seo/)
- **问题**：60% 索引页面是已过期酒店列表（404），大量消耗 crawl budget
- **方案**：对永久关闭的酒店页面批量实施 410 Gone，清理 120 万条死链
- **结果**：有效页面的抓取速率翻倍，下一季度自然流量增长 **22%**

### 案例四：Fintech 企业 20 万条遗留 PDF → 72 小时合规关闭

- **来源**：Search Engine Zine
- **问题**：200,000 条客户财务报表 PDF 被意外索引到 Google（严重合规风险）
- **方案**：批量实施 410 Gone
- **结果**：72 小时内 GSC 抓取成功率从 100% 降至 0%，合规风险消除

### 反面案例五：301 重定向到不相关页面 → 排名流量双降

- **来源**：[GSQi 案例分析](https://www.gsqi.com/marketing-blog/redirects-less-relevant-pages-soft-404s/)（含 John Mueller 原话验证）
- **问题**：多个站点迁移时，将大量旧 URL 统一 301 重定向到首页或弱相关页面
- **结果**：GSC 出现 Soft 404 警告激增；Google 将这些 301 视为无效，按 404 处理；排名和流量全部丢失；"重定向保留权重"策略完全失败
- **Google 确认**：Moz 2016 年实验也证明，301 重定向本身平均就会造成 **15% 的自然流量损失**，链式重定向每跳再多损失 15%

### 反面案例六：跨国媒体域名迁移 → 90% 流量崩塌

- **来源**：[Search Engine Land 报道](https://technicalseonews.com/latest/silent-soft-404s-caused-90-traffic-loss-after-site-migration/)
- **问题**：某大型媒体 13 个国家域名迁移后，大量页面返回 200 但内容为通用空模板，被 Google 判定为 Soft 404
- **结果**：日点击从 15,000-25,000 暴跌至 2,000-4,000（**损失约 90%**），持续超过一年；约 **500,000** 个页面无法被索引
- **修复后**：对不存在页面返回 404/410，Soft 404 从 120,000 降至 20,000（减少 83%），Crawled-not-indexed 从 513,000 降至 220,000（减少 57%）

---

## 七、禁止事项清单

1. ❌ 不要用 301 重定向到首页或通用说明页（会被判定为 Soft 404）
2. ❌ 不要用 robots.txt Disallow 替代 noindex 或 410
3. ❌ 不要在 robots.txt 中写 `Noindex:`（2019 年起已废弃）
4. ❌ 不要 noindex 与 Sitemap 提交并存于同一 URL
5. ❌ 不要对同一 URL 同时使用 noindex 和 robots.txt Disallow
6. ❌ 不要用客户端 JS 注入 noindex（CSR 场景 Google 可能读不到）
7. ❌ 不要用 GSC Removals 替代永久方案（6 个月后 URL 会重新出现）

---

## 八、参考资料

| 来源 | 标题 |
|------|------|
| [Google Search Console Help](https://support.google.com/webmasters/answer/2445990) | 404 errors 官方文档 |
| [Google robots.txt 文档](https://developers.google.com/search/docs/crawling-indexing/robots/intro) | robots.txt 官方文档 |
| [Google noindex 文档](https://developers.google.com/search/docs/crawling-indexing/block-indexing) | noindex 官方文档 |
| [Reboot Online](https://www.rebootonline.com/blog/404-vs-410-the-technical-seo-experiment/) | 404 vs 410 对照实验 |
| [GSQi](https://www.gsqi.com/marketing-blog/redirects-less-relevant-pages-soft-404s/) | 301 重定向 Soft 404 案例 |
| [Gautam Khorana](https://gautamkhorana.com/blog/410-vs-404-status-codes-for-seo/) | 410 vs 404 状态码指南 |
| [MD Pabel](https://dev.to/md_pabel_fe07e07449db7326/case-study-how-i-removed-10500-seo-spam-urls-from-google-search-in-12-days-2fcj) | 10,500 条垃圾 URL 12 天清除案例 |
| [MD Pabel](https://www.mdpabel.com/case-studies/how-i-removed-50000-spam-urls-from-google-after-a-japanese-keyword-hack/) | 50,000+ 黑帽 URL 72 小时清除案例 |
| [Search Engine Zine](https://searchenginezine.com/seo/logic/404-vs-410-for-seo/) | 企业级 404 vs 410 决策指南 |
| [Vega SEO Talks](https://vegaseotalks.com/what-is-the-most-effective-phased-strategy-for-deindexing-200k-low-quality-pages-without-triggering-a-site-wide-crawl-rate-disruption/) | 20 万+ 页面分批删除策略 |
| [Technical SEO News](https://technicalseonews.com/latest/silent-soft-404s-caused-90-traffic-loss-after-site-migration/) | 媒体域名迁移 90% 流量崩塌案例 |
| [Intero Digital](https://www.interodigital.com/blog/the-complete-guide-to-redirecting-deleted-pages-301-404-or-410/) | 删除页面：301/404/410 完整指南 |
| [Shop Circle](https://shopcircle.co/blogs/news/redirecting-404-page-to-homepage-seo-danger) | 重定向到首页摧毁 SEO 的分析 |
