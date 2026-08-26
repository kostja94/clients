# robots.txt 配置说明

本文档说明 Alignify 站点的 robots.txt 实现与最佳实践。

**实现位置**：`public/robots.txt`（静态文件）

---

## 一、robots.txt 最佳实践

### 1.1 定位与作用

| 要点 | 说明 |
|------|------|
| **作用** | 控制爬虫抓取，不是阻止索引的手段（被禁止的 URL 仍可能出现在搜索结果中，仅无摘要） |
| **不索引** | 用 noindex 或认证；敏感内容勿依赖 robots.txt（文件公开可读） |
| **建议性** | 规则对爬虫是建议性的，恶意爬虫可能无视 |

### 1.2 位置与格式

| 项 | 要求 |
|----|------|
| 路径 | 站点根：`https://example.com/robots.txt` |
| 编码 | UTF-8 纯文本 |
| 范围 | 每个 host/协议/端口一个文件；子域名需单独配置 |
| 规范 | 遵循 RFC 9309（Robots Exclusion Protocol） |

### 1.3 核心指令

| 指令 | 用途 | 示例 |
|------|------|------|
| `User-agent:` | 指定爬虫 | `User-agent: Googlebot`、`User-agent: *` |
| `Disallow:` | 禁止抓取路径前缀 | `Disallow: /private/` |
| `Allow:` | 允许抓取（可覆盖 Disallow） | `Allow: /public/` |
| `Sitemap:` | 声明 sitemap 绝对 URL | `Sitemap: https://example.com/sitemap.xml` |
| `Clean-param:` | 清理查询参数（Yandex 扩展） | 见下节 |

### 1.4 语法与模式

- 路径为前缀匹配；`Disallow: /dir/` 禁止该目录及子路径
- 通配符：`*`（任意字符）、`$`（URL 结尾），如 `Disallow: /*.json$`
- 同一 User-agent 下多条规则按最长匹配优先；Allow 可与 Disallow 配合使用

### 1.5 禁止规则注意

- **勿禁止渲染所需资源**：CSS、JS、图片等被禁止会导致 Google 无法正确渲染，损害索引（见 [technical-indexing](./seo-fundamentals.md#51-nextjs--vercel_nextstaticcsscssdpl)）
- 仅禁止不需要抓取的路径：后台、API、临时文件等

### 1.6 常见模式

```
# 禁止整个站点
User-agent: *
Disallow: /

# 禁止某目录
User-agent: *
Disallow: /admin/

# 禁止某目录但允许子路径
User-agent: *
Disallow: /
Allow: /blog/

# 多 sitemap
Sitemap: https://example.com/sitemap.xml
Sitemap: https://example.com/sitemap-zh.xml
```

### 1.7 AI 爬虫最佳实践

AI 爬虫分两类：**查找/检索**（用于搜索、引用，可带来流量）与**训练数据**（抓取内容用于模型训练，通常无直接流量）。

| 策略 | 说明 |
|------|------|
| **允许查找类** | 让内容出现在 ChatGPT、Perplexity、Claude 等 AI 搜索/回答中，可获取引用与流量 |
| **禁止训练类** | 若不想内容被用于模型训练，可禁止对应爬虫 |

**常见 AI 爬虫与推荐策略**：

| User-agent | 用途 | 推荐 | 说明 |
|------------|------|------|------|
| **OAI-SearchBot** | ChatGPT 搜索索引 | Allow | 允许则内容可出现在 ChatGPT 搜索结果 |
| **GPTBot** | OpenAI 模型训练 | Disallow | 禁止则内容不用于训练 GPT 等模型 |
| **ClaudeBot** | Anthropic 模型训练 | Disallow | 禁止则内容不用于训练 Claude |
| **Claude-SearchBot** | Claude 搜索索引 | Allow | 允许则内容可出现在 Claude 搜索 |
| **Google-Extended** | Gemini 训练与 grounding | Allow | 允许 Google 在 AI 搜索中引用（Alignify 实际策略为 Allow） |
| **PerplexityBot** | Perplexity 搜索 | Allow | 允许则内容可被引用，可能带来流量 |
| **CCBot** | Common Crawl 公开数据集 | — | 未在 robots.txt 中单独配置（由 User-agent: * 默认 Allow） |

**ChatGPT-User**、**Claude-User**、**Applebot-Extended**：已在 robots.txt 中配置 Allow，用于用户主动请求时的即时回答和 AI 搜索引用。

**示例配置**：

```
# 允许 AI 查找/搜索（出现在 AI 回答中）
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

# 禁止 AI 训练数据抓取
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /
```

**参考**：

- [OpenAI Crawlers](https://platform.openai.com/docs/gptbot)（OAI-SearchBot、GPTBot）
- [Anthropic - Block the crawler](https://support.anthropic.com/en/articles/8896518)
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/perplexitybot)
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot)

### 1.8 参考

- [Create a robots.txt - Google](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt)
- [Useful robots.txt rules - Google](https://developers.google.com/crawling/docs/robots-txt/useful-robots-txt-rules)
- [Clean-param - Yandex](https://yandex.com/support/webmaster/robot-workings/clean-param.html)

---

## 二、当前配置

```
# Allow traditional search engines
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Yandex
Allow: /
Clean-param: utm_source&utm_medium&utm_campaign&utm_term&utm_content&ref&fbclid&gclid&share&nb

# Allow social media crawlers
User-agent: Twitterbot
Allow: /

User-agent: facebookexternalhit
Allow: /

# Allow AI search / citation bots (bring visibility and traffic)
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

# Disallow AI training bots (scrape without citing; no referral value)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

# AI content usage signals
Content-Signal: ai-train=no, search=yes, ai-input=yes

# Default: allow everything else
User-agent: *
Allow: /

# Sitemap
Sitemap: https://alignify.co/sitemap.xml
```

> **更新日期**：2026-06-09。与 deploy repo 的 public/robots.txt 完全同步。

---

## 三、符合性评估

| 最佳实践 | 状态 | 说明 |
|----------|------|------|
| 文件位于站点根 | ✅ | `public/robots.txt` 发布为 `/robots.txt` |
| UTF-8 纯文本 | ✅ | 无 BOM、无隐藏字符 |
| 包含 Sitemap | ✅ | 使用绝对 URL |
| 勿禁止 CSS/JS | ✅ | 未禁止 `/_next/`（并通过 X-Robots-Tag 控制静态资源索引） |
| 主流爬虫已配置 | ✅ | Googlebot、Bingbot、Yandex、Twitterbot、facebookexternalhit |
| 默认规则 User-agent: * | ✅ | 覆盖其他爬虫 |
| Clean-param（Yandex） | ✅ | 清理 UTM、ref、fbclid、gclid、share、nb 等，避免重复 URL |
| 无多余 Disallow | ✅ | 全站允许抓取，符合内容站需求 |
| AI 爬虫配置 | ✅ | Allow 查找类（OAI-SearchBot、Claude-SearchBot、PerplexityBot），Disallow 训练类（GPTBot、ClaudeBot、Google-Extended、CCBot） |

**结论**：当前 robots.txt 符合最佳实践，含 AI 爬虫区分策略。

---

## 四、X-Robots-Tag（next.config.js）

`_next/static` 下的静态资源已设置 `noindex, nofollow`，防止被搜索引擎索引：

```js
async headers() {
  return [
    {
      source: '/_next/static/:path*',
      headers: [{ key: 'X-Robots-Tag', value: 'noindex, nofollow' }],
    },
  ];
}
```

---

## 五、中间件排除

`middleware.ts` 中 `robots.txt` 请求由 `.*\\..*` 模式排除，不会经过 i18n 重定向，直接返回 `public/robots.txt`。

---

## 六、相关文档

- **SEO 指南**：`/seo/robots-txt` 页面提供 robots.txt 语法与最佳实践
- **Sitemap**：参见 [technical-sitemap](./sitemap.md)
- **索引（含 _next 静态资源说明）**：参见 [technical-indexing](./seo-fundamentals.md#51-nextjs--vercel_nextstaticcsscssdpl)
