# IndexNow 集成指南

> **部署仓库**：脚本位于 `alignify-by-kostja/scripts/permanent/*.ts`；npm 命令 `indexnow` / `indexnow:all` 仅在部署仓 `package.json` 中注册。

---

# IndexNow 集成方案

为内容网站提供即时搜索引擎通知方案：发布/更新页面后，主动 ping IndexNow API，让 Bing/Yandex/Seznam 几小时内收录，无需等待自然抓取。

---

## 1. 什么是 IndexNow

IndexNow 是一个由 Bing 和 Yandex 联合发起的协议。网站主动向搜索引擎通知 URL 变更（新增、更新、删除），搜索引擎在收到通知后立即安排抓取。相比传统 sitemap 被动等待（可能数天到数周），IndexNow 将收录延迟压缩到数小时内。

**支持的搜索引擎**：Bing、Yandex、Seznam、Naver（部分）。

**协议核心**：HTTP POST 一个 JSON 到 `https://api.indexnow.org/IndexNow`，包含站点 host、API key、key 文件位置、要提交的 URL 列表。

**限制**：单次最多 10,000 个 URL，无每日配额。

---

## 2. 前置准备：获取 API Key

### 2.1 生成 Key

API Key 是一个任意字符串（建议 32 位十六进制）。可以在线生成或在终端生成：

```bash
# PowerShell
-join ((48..57) + (97..102) | Get-Random -Count 32 | ForEach-Object { [char]$_ })

# Bash
openssl rand -hex 16
```

### 2.2 部署 Key 验证文件

将 Key 文件放到网站根目录，命名为 `{key}.txt`，路径必须可公开访问。文件内容只需包含 Key 本身。

**示例**：
- Key：`5ede514145b049168e29ed7a00f52bee`
- 文件：`https://yourdomain.com/5ede514145b049168e29ed7a00f52bee.txt`
- 文件内容：`5ede514145b049168e29ed7a00f52bee`

**Next.js 做法**：将 `{key}.txt` 放到 `public/` 目录即可。

### 2.3 注册到搜索引擎

访问 Bing Webmaster Tools：https://www.bing.com/webmasters/

在站点设置中开启 IndexNow，填入 API Key。Bing 会自动拉取并验证 `{key}.txt` 文件。Yandex 和 Seznam 会自动通过 IndexNow 协议读取 Key 文件完成认证，无需额外注册。

---

## 3. 代码实现

### 3.1 核心 API 模块（`src/lib/indexnow.ts`）

这是可复用的核心，直接复制到新项目即可。需要改的只有三个常量：

```typescript
/**
 * IndexNow API integration
 *
 * Reference: https://www.bing.com/indexnow/getstarted
 */

const INDEXNOW_API_KEY = '你的API-KEY';           // ← 改成你的 Key
const INDEXNOW_KEY_LOCATION = 'https://你的域名/你的API-KEY.txt';  // ← 改成你的 Key 文件地址
const INDEXNOW_API_URL = 'https://api.indexnow.org/IndexNow';
const SITE_HOST = '你的域名';                     // ← 改成你的域名（不含协议）

/**
 * 提交单个 URL
 */
export async function submitUrlToIndexNow(url: string): Promise<boolean> {
  try {
    const urlObj = new URL(url);
    if (urlObj.hostname !== SITE_HOST && urlObj.hostname !== `www.${SITE_HOST}`) {
      console.warn(`[IndexNow] URL hostname mismatch: ${urlObj.hostname}`);
      return false;
    }

    const response = await fetch(INDEXNOW_API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({
        host: SITE_HOST,
        key: INDEXNOW_API_KEY,
        keyLocation: INDEXNOW_KEY_LOCATION,
        urlList: [url],
      }),
    });

    if (response.status === 200) {
      console.log(`[IndexNow] Submitted: ${url}`);
      return true;
    }
    console.error(`[IndexNow] Failed:`, response.status, response.statusText);
    return false;
  } catch (error) {
    console.error(`[IndexNow] Error:`, error);
    return false;
  }
}

/**
 * 批量提交多个 URL（最多 10,000 个）
 */
export async function submitUrlsToIndexNow(urls: string[]): Promise<boolean> {
  if (!urls || urls.length === 0) {
    console.warn('[IndexNow] No URLs to submit');
    return false;
  }

  try {
    const validUrls = urls.filter(url => {
      try {
        const urlObj = new URL(url);
        return urlObj.hostname === SITE_HOST || urlObj.hostname === `www.${SITE_HOST}`;
      } catch { return false; }
    });

    if (validUrls.length === 0) {
      console.warn('[IndexNow] No valid URLs');
      return false;
    }

    const response = await fetch(INDEXNOW_API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({
        host: SITE_HOST,
        key: INDEXNOW_API_KEY,
        keyLocation: INDEXNOW_KEY_LOCATION,
        urlList: validUrls,
      }),
    });

    if (response.status === 200) {
      console.log(`[IndexNow] Submitted ${validUrls.length} URLs`);
      return true;
    }
    const errorText = await response.text().catch(() => '');
    console.error(`[IndexNow] Failed:`, response.status, response.statusText, errorText);
    return false;
  } catch (error) {
    console.error('[IndexNow] Error:', error);
    return false;
  }
}

/**
 * 相对路径 → 完整 URL
 */
export function buildFullUrl(path: string): string {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return `https://${SITE_HOST}${normalizedPath}`;
}

/**
 * 批量提交相对路径
 */
export async function submitPathsToIndexNow(paths: string[]): Promise<boolean> {
  const urls = paths.map(buildFullUrl);
  return submitUrlsToIndexNow(urls);
}
```

### 3.2 单页提交脚本（`scripts/permanent/submit-to-indexnow.ts`）

用于 CI/CD 中按需提交少量 URL，或手动提交单个页面。零依赖，纯 Node.js：

```javascript
#!/usr/bin/env node
const INDEXNOW_API_KEY = '你的API-KEY';
const INDEXNOW_KEY_LOCATION = 'https://你的域名/你的API-KEY.txt';
const INDEXNOW_API_URL = 'https://api.indexnow.org/IndexNow';
const SITE_HOST = '你的域名';
const DEFAULT_URL = 'https://你的域名';

function buildFullUrl(path) {
  return `https://${SITE_HOST}${path.startsWith('/') ? path : '/' + path}`;
}

async function submitUrls(urls) {
  // ... 同上批量提交逻辑
}

async function main() {
  const args = process.argv.slice(2);
  const urls = args.length > 0
    ? args.map(a => a.startsWith('http') ? a : buildFullUrl(a))
    : [DEFAULT_URL];
  await submitUrls(urls);
}

main();
```

**用法**：
```powershell
# 提交首页
npm run indexnow

# 提交指定页面（完整 URL）
npm run indexnow https://yourdomain.com/new-page

# 提交指定页面（相对路径）
npm run indexnow /new-page /another-page
```

### 3.3 全站页面 URL 配置（`src/data/site-pages-config.ts`）

这是最关键的一步：把所有页面路径集中维护在一个地方。新页面添加时，同时更新这个配置，IndexNow 批量提交就能自动覆盖。

```typescript
const baseUrl = 'https://yourdomain.com';

/**
 * 所有页面路径的集中注册表
 * 添加新页面时在此处追加路径
 */
const EN_PATHS: string[] = [
  '/',
  '/about',
  '/blog',
  '/blog/post-1',
  // ...
];

const ZH_PATHS: string[] = [
  '/zh',
  '/zh/about',
  '/zh/blog',
  '/zh/blog/post-1',
  // ...
];

/**
 * 如果你的页面由数据驱动（如从 CMS 或配置文件生成），
 * 可以像这样动态生成路径：
 */
function getDynamicPagePaths(): string[] {
  // 例如：从 tools-pages-config 或 CMS 中读取
  return YOUR_PAGE_REGISTRY.map(p => `/tools/${p.slug}`);
}

/**
 * 返回全站完整 URL 列表
 */
export function getAllPageUrls(siteBaseUrl: string = baseUrl): string[] {
  const enTools = getDynamicPagePaths().map(p => `${siteBaseUrl}${p}`);
  const zhTools = getDynamicPagePaths().map(p => `${siteBaseUrl}/zh${p}`);
  const enOther = EN_PATHS.map(p => `${siteBaseUrl}${p}`);
  const zhOther = ZH_PATHS.map(p => `${siteBaseUrl}${p}`);
  return [...enTools, ...zhTools, ...enOther, ...zhOther];
}
```

**设计原则**：
- 单一数据源：页面注册表（如 `TOOLS_PAGES`、`SEO_PAGES`）是唯一权威
- 新页面添加后，IndexNow 脚本自动感知
- 避免手动维护两套路径列表

### 3.4 批量提交脚本（`scripts/permanent/submit-all-pages-to-indexnow.ts`）

从 `getAllPageUrls()` 获取全站 URL，分批提交到 IndexNow：

```typescript
import { submitUrlsToIndexNow } from '../../src/lib/indexnow';
import { getAllPageUrls } from '../../src/data/site-pages-config';

const baseUrl = 'https://yourdomain.com';

async function main() {
  console.log('[IndexNow] Starting batch submit...');

  const urls = getAllPageUrls(baseUrl);
  console.log(`[IndexNow] Found ${urls.length} pages`);

  // IndexNow 单次上限 10,000 URL
  const batchSize = 10000;
  const batches: string[][] = [];
  for (let i = 0; i < urls.length; i += batchSize) {
    batches.push(urls.slice(i, i + batchSize));
  }

  console.log(`[IndexNow] ${batches.length} batch(es)`);

  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < batches.length; i++) {
    const batch = batches[i];
    console.log(`[IndexNow] Batch ${i + 1}/${batches.length} (${batch.length} URLs)...`);

    const success = await submitUrlsToIndexNow(batch);
    if (success) {
      successCount += batch.length;
      console.log(`[IndexNow] Batch ${i + 1} OK`);
    } else {
      failCount += batch.length;
      console.error(`[IndexNow] Batch ${i + 1} FAILED`);
    }

    // 批次间延迟 1 秒
    if (i < batches.length - 1) {
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
  }

  console.log(`\n[IndexNow] Done! OK: ${successCount}, Failed: ${failCount}, Total: ${urls.length}`);
}

main().catch(error => {
  console.error('[IndexNow] Error:', error);
  process.exit(1);
});
```

### 3.5 npm scripts 配置（`package.json`）

```json
{
  "scripts": {
    "indexnow": "tsx scripts/permanent/submit-to-indexnow.ts",
    "indexnow:all": "tsx scripts/permanent/submit-all-pages-to-indexnow.ts"
  }
}
```

- `indexnow`：提交单个/少量 URL（传参或默认首页）
- `indexnow:all`：批量提交全站所有页面

**依赖**：`indexnow` 与 `indexnow:all` 均需要 `tsx` 来运行 TypeScript 脚本（import 项目内 TS 模块）。

---

## 4. 文件结构

```
项目根目录/
├── public/
│   └── {api-key}.txt                # IndexNow Key 验证文件
├── src/
│   ├── lib/
│   │   └── indexnow.ts              # 核心 API 模块（可复用）
│   └── data/
│       └── site-pages-config.ts     # 全站 URL 注册表（含 getAllPageUrls）
├── scripts/
│   └── permanent/
│       ├── submit-to-indexnow.ts    # 单页/少量 URL 提交
│       └── submit-all-pages-to-indexnow.ts  # 批量全站提交
└── package.json                     # npm scripts
```

---

## 5. 使用场景

### 5.1 首次部署：提交全站

```powershell
npm run indexnow:all
```

一次性将现有全部页面通知搜索引擎。适用于上线、大改版后。

### 5.2 发布新页面：提交单个 URL

```powershell
npm run indexnow https://yourdomain.com/new-page
```

### 5.3 CI/CD 集成：构建后自动提交

在部署脚本末尾添加：

```json
{
  "scripts": {
    "build": "next build && npm run indexnow:all"
  }
}
```

或更精细地，只提交变更的页面（通过 git diff 获取变更文件列表，映射到对应 URL）。

### 5.4 定时任务：周期性刷新

用 cron job 或 Vercel Cron Jobs 定期提交。例如每天一次，确保搜索引擎索引保持最新：

```typescript
// app/api/cron/indexnow/route.ts
export async function GET() {
  const urls = getAllPageUrls('https://yourdomain.com');
  await submitUrlsToIndexNow(urls);
  return Response.json({ ok: true });
}
```

---

## 6. 验证

### 6.1 检查 Key 文件可访问

浏览器打开 `https://yourdomain.com/{api-key}.txt`，应返回 Key 值。

### 6.2 手动测试单页提交

```powershell
npm run indexnow https://yourdomain.com
```

应输出 `[IndexNow] Submitted: https://yourdomain.com`，状态码 200。

### 6.3 Bing Webmaster Tools 确认

登录 Bing Webmaster Tools → 站点 → IndexNow，查看提交历史和状态。

### 6.4 常见问题

| 问题 | 原因 | 解决 |
|---|---|---|
| 403 Forbidden | Key 不匹配或 Key 文件不可访问 | 确认 Key 文件路径和内容一致 |
| 422 Unprocessable | URL 格式错误或不属于该 host | 检查 URL 域名和格式 |
| 200 但 Bing 仍未索引 | 正常延迟，Bing 需要数小时处理 | 等待 1-4 小时后在 Bing 搜索 `site:yourdomain.com` 验证 |
| npm script 路径错误 | Windows 下 `../` 路径解析问题 | 使用项目内相对路径或绝对路径 |

---

## 7. 适配新项目的检查清单

- [ ] 生成 API Key（32 位十六进制字符串）
- [ ] 将 `{key}.txt` 放到 `public/` 目录
- [ ] 复制 `src/lib/indexnow.ts`，修改 3 个常量（KEY、KEY_LOCATION、SITE_HOST）
- [ ] 创建或更新 `src/data/site-pages-config.ts`，注册全站路径
- [ ] 导出 `getAllPageUrls(siteBaseUrl)` 函数
- [ ] 复制 `scripts/permanent/submit-all-pages-to-indexnow.ts`
- [ ] 复制 `scripts/permanent/submit-to-indexnow.ts`
- [ ] 在 `package.json` 中添加 `indexnow` 和 `indexnow:all` scripts
- [ ] 部署后运行 `npm run indexnow:all` 首次提交
- [ ] 在 Bing Webmaster Tools 中注册 API Key
- [ ] 验证 Key 文件在线上可访问
