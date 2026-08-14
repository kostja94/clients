# MeDo 索引通知实施指南：Google Indexing API + IndexNow

> **站点**：https://medo.dev  
> **适用对象**：工程负责人（人类）+ Cursor Agent  
> **范围**：仅 IndexNow 与 Google Indexing API 的配置、脚本、运行与排错  
> **Last updated**：2026-06-22 · **版本**：1.4

---

## 文档结构

| 部分 | 读者 | 用途 |
|------|------|------|
| **Part I — 人类实施指南** | 工程 / 运维 | 配置步骤、命令、验收 |
| **Part II — Agent 执行手册** | Cursor Agent | 常量、文件清单、决策树 |
| **附录 A–F** | 实施时复制 | 代码与配置模板 |

---

# Part I — 人类实施指南

## 1. 两套 API 的分工

| 维度 | IndexNow | Google Indexing API |
|------|----------|---------------------|
| 官方文档 | https://www.indexnow.org/documentation | https://developers.google.com/search/apis/indexing-api/v3/using-api |
| 覆盖引擎 | Bing、Yandex、Seznam、Naver 等 | **仅 Google** |
| 认证 | 根目录 `{key}.txt` 文件验证 | GCP 服务账号 JWT + GSC **Owner** 授权 |
| 配额 | 单次最多 10,000 URL，无日配额 | **200 URL/天**（免费层） |
| 通知类型 | URL 变更（新增/更新） | `URL_UPDATED` / `URL_DELETED` |

**推荐用法**：

| 场景 | 命令 |
|------|------|
| 单页/少量 URL（多引擎） | `npm run indexnow https://medo.dev/blog/{slug}/` |
| 配置列表内全量（多引擎） | `npm run indexnow:all` |
| 单页 Google 通知 | `npm run google-index /blog/{slug}/` |
| 配置列表内全量 Google | `npm run google-index:all` |
| 查 Google 通知历史 | `npm run google-index -- --status https://medo.dev/` |
| Google 删除通知 | `npm run google-index -- --type URL_DELETED /old-path/` |

国内环境调用 Google API 常超时，Google 侧建议用 **GitHub Actions**（附录 D）在海外 runner 执行。

---

## 2. 前置条件

| 项 | 说明 |
|----|------|
| medo 主工程仓库 | 脚本与 `public/` 验证文件部署于此 |
| Node.js 20+ | 运行 `tsx` 脚本 |
| Bing Webmaster | 添加并验证 `medo.dev`；**在此生成 IndexNow API Key** |
| Google Search Console | medo.dev 属性已验证 |
| GCP 项目 | 已启用 **Indexing API**，并已下载服务账号 JSON 密钥 |

---

## 3. IndexNow 实施

### 3.1 获取 API Key

**推荐方式：Bing Webmaster Tools 生成**（与 Bing 官方 IndexNow 接入流程一致）。

1. 打开 https://www.bing.com/webmasters/ 并登录
2. 添加并验证站点 `medo.dev`（若尚未验证）
3. 右上角 **Settings（设置）→ API Access**
4. 点击 **Generate Key**（若已有密钥则直接复制显示的值）
5. 将密钥写入 `.env` / GitHub Secret，变量名 **`INDEXNOW_KEY`**

说明：

- 该密钥按 **Bing 账号** 生成，同一账号下已验证的多个站点可共用
- 更换密钥后，系统生效可能需要最多约 30 分钟
- 官方说明：https://www.bing.com/indexnow/getstarted · Bing Webmaster API Access 文档

**备选方式**（IndexNow 协议同样认可，但 medo 建议优先用 Bing 后台密钥以便在 Webmaster 查看提交记录）：

| 方式 | 操作 |
|------|------|
| IndexNow 官网 | https://www.bing.com/indexnow/getstarted 页内 **Generate** 按钮 |
| 自行生成 | 32 位十六进制字符串（须满足 8–128 字符、`a-zA-Z0-9-`） |

勿将真实密钥提交 Git。

### 3.2 部署验证文件

1. 创建 `public/{INDEXNOW_KEY}.txt`
2. 内容**仅一行**：密钥字符串（UTF-8，无 BOM、无换行、无空格）
3. 部署后访问 `https://medo.dev/{INDEXNOW_KEY}.txt` → HTTP 200

**host 一致性**：若站点主域名为 `www.medo.dev`，则 IndexNow 请求中的 `host`、`keyLocation`、提交的 URL 须统一同一主机名。

### 3.3 工程文件

| 文件 | 职责 |
|------|------|
| `src/lib/indexnow.ts` | 提交逻辑（附录 A.1） |
| `src/lib/urls.ts` | 待通知 URL 列表（附录 C） |
| `scripts/permanent/submit-to-indexnow.ts` | 单页 CLI（附录 A.3） |
| `scripts/permanent/indexnow-submit.ts` | 列表全量（附录 A.2） |
| `.env.example` | 附录 E |

`package.json`：

```json
{
  "scripts": {
    "indexnow": "tsx scripts/permanent/submit-to-indexnow.ts",
    "indexnow:all": "tsx scripts/permanent/indexnow-submit.ts"
  }
}
```

```bash
npm install dotenv tsx
```

### 3.4 在 Bing Webmaster 验证提交

密钥文件部署并完成首次 `npm run indexnow` 后：

1. Bing Webmaster Tools → 选择 `medo.dev`
2. 打开 **IndexNow** 相关报告/历史（入口因界面版本可能为 IndexNow 或 URL Submission）
3. 确认提交的 URL 已被 Bing 接收

IndexNow 只保证搜索引擎**收到变更通知**，不保证一定收录。

### 3.5 验收

```bash
npm run indexnow https://medo.dev/
npm run indexnow:all
```

| HTTP | 含义 |
|------|------|
| 200 | 成功 |
| 202 | 已接受，密钥验证待完成 |
| 403 | 密钥文件不可达或内容不匹配 → 附录 F |
| 422 | URL 与 `host` 不匹配 |

---

## 4. Google Indexing API 实施

### 4.1 GCP

1. https://console.cloud.google.com/ 创建或选择项目
2. **APIs & Services → Library** → 启用 **Indexing API**
3. **IAM → Service Accounts → Create** → 下载 JSON 密钥
4. 密钥存 `.env.local` 或 GitHub Secret **`GCP_SA_KEY`**，勿 commit

### 4.2 GSC 授权（缺此步必 403）

1. https://search.google.com/search-console 打开 medo 属性
2. **设置 → 用户和权限 → 添加用户**
3. 填入 JSON 中 `client_email`
4. 权限选 **Owner**（Full 不够）
5. `GSC_SITE_URL` 与 GSC 属性 URL 前缀一致，例如 `https://medo.dev/`

### 4.3 工程文件

| 文件 | 职责 |
|------|------|
| `src/lib/google-indexing.ts` | JWT、publish、status、配额（附录 B.1） |
| `scripts/permanent/submit-to-google-index.ts` | 单页 CLI（附录 B.2） |
| `scripts/permanent/submit-all-to-google-index.ts` | 列表全量（附录 B.3） |
| `.github/workflows/google-indexing.yml` | 附录 D |

`.env.local`（勿提交）：

```bash
GOOGLE_INDEXING_KEY_FILE=/absolute/path/to/service-account-key.json
GSC_SITE_URL=https://medo.dev/
INDEXNOW_KEY=<your-indexnow-key>
```

`package.json` 追加：

```json
{
  "scripts": {
    "google-index": "tsx scripts/permanent/submit-to-google-index.ts",
    "google-index:all": "tsx scripts/permanent/submit-all-to-google-index.ts"
  }
}
```

```bash
npm install google-auth-library dotenv tsx
```

### 4.4 JWT 认证要点（避免 401）

- 使用 `google-auth-library` 的 `JWT`，**不传 `scopes`**
- 用 `auth.request()` 直调 API，**不用** `googleapis` 的 `google.indexing()` 包装器
- `auth.request()` 传入完整 API URL 即可生成正确 audience JWT，无需额外配置
- `transporterOptions.agent` 会传入 `AuthClient` 的 HTTP 客户端；**仅本机 Windows 出现 ETIMEDOUT 时需要 IPv4 agent**；GitHub Actions 在海外 runner 上通常不需要
- 国内本机仍超时 → 优先用 GitHub Actions（附录 D）或代理

### 4.5 GitHub Actions

1. Secrets → `GCP_SA_KEY` = JSON 全文
2. 部署附录 D workflow（需已提交 `package-lock.json`；否则 workflow 内将 `npm ci` 改为 `npm install`）
3. 手动触发：`check_status` → `submit_urls`（首页）→ `submit_all`
4. Cron 默认每周一 UTC 09:00 跑 `submit_all`

### 4.6 验收

```bash
npm run google-index -- --status https://medo.dev/
npm run google-index https://medo.dev/
npm run google-index:all
```

成功：`OK URL_UPDATED`，配额 `N/200`。

---

## 5. URL 列表维护

批量命令（`indexnow:all` / `google-index:all`）从 **`src/lib/urls.ts`** 读取 URL，不自动扫描全站。

新增或更新页面时，在 `urls.ts` 的 `PAGE_PATHS` 中追加路径，例如：

```typescript
'/',
'/blog/',
  '/blog/my-new-post/',
  '/pricing/',
```

Blog 新文发布后：先更新列表，再跑单页或全量命令。

---

## 6. 日常流程

**新页发布**：

```
更新 src/lib/urls.ts
  → npm run indexnow https://medo.dev/blog/{slug}/
  → npm run google-index /blog/{slug}/
```

**页面上线后批量补交通知**：

```bash
npm run indexnow:all
npm run google-index:all    # 超过 200 条时自动截断，可分日执行
```

**页面下线（Google）**：

```bash
npm run google-index -- --type URL_DELETED https://medo.dev/old-path/
```

---

## 7. 故障排查

### IndexNow

| 现象 | 处理 |
|------|------|
| 403 | 附录 F：检查 `{key}.txt` 可达性与内容 |
| 202 | 等待；确认验证文件已部署 |
| 422 | 统一 `host` 与 URL 域名 |

### Google Indexing API

| 现象 | 处理 |
|------|------|
| ETIMEDOUT | 改用 GitHub Actions 或代理 |
| 401 | 确认 `auth.request()` + 无 scopes JWT |
| 403 | GSC 添加服务账号为 Owner |
| 429 | 日配额 200 用尽，次日再跑 |
| `GOOGLE_INDEXING_KEY_FILE not set` | 检查 `.env.local` 或 CI Secret |

API 提交成功只表示 Google **收到通知**，不保证最终收录结果。

---

## 8. 验收清单

### IndexNow

- [ ] 已在 Bing Webmaster **API Access** 获取密钥
- [ ] `https://medo.dev/{KEY}.txt` 可访问
- [ ] `npm run indexnow https://medo.dev/` → 200
- [ ] `npm run indexnow:all` → 列表内 URL 全部提交成功

### Google Indexing API

- [ ] 服务账号为 medo.dev GSC **Owner**
- [ ] Actions 上 `--status` → exit 0
- [ ] `google-index` 首页 → `OK URL_UPDATED`
- [ ] workflow 可手动 / cron 触发

---

# Part II — Agent 执行手册

> 所有代码从**本文件附录**创建。勿引用 medo 文件夹外资源。勿 commit 密钥。

---

## A. 项目常量

```yaml
site:
  base_url: "https://medo.dev"
  host_indexnow: "medo.dev"
  gsc_site_url: "https://medo.dev/"

env:
  INDEXNOW_KEY: "IndexNow 密钥"
  INDEXNOW_KEY_LOCATION: "可选，默认 https://medo.dev/{KEY}.txt"
  GOOGLE_INDEXING_KEY_FILE: "服务账号 JSON 本地路径"
  GSC_SITE_URL: "https://medo.dev/"

github_secrets:
  GCP_SA_KEY: "服务账号 JSON 全文"
  INDEXNOW_KEY: "IndexNow 密钥（CI 跑 IndexNow 时需要）"

google_indexing:
  daily_quota: 200
  publish_endpoint: "https://indexing.googleapis.com/v3/urlNotifications:publish"
  metadata_endpoint: "https://indexing.googleapis.com/v3/urlNotifications/metadata"

indexnow:
  endpoint: "https://api.indexnow.org/indexnow"
  batch_max: 10000
  key_file: "public/{INDEXNOW_KEY}.txt"

npm_scripts:
  indexnow: "tsx scripts/permanent/submit-to-indexnow.ts"
  indexnow_all: "tsx scripts/permanent/indexnow-submit.ts"
  google_index: "tsx scripts/permanent/submit-to-google-index.ts"
  google_index_all: "tsx scripts/permanent/submit-all-to-google-index.ts"

url_list:
  source_file: "src/lib/urls.ts"
  field: "PAGE_PATHS"
```

---

## B. 待创建文件

| 优先级 | 路径 | 附录 |
|--------|------|------|
| P0 | `src/lib/urls.ts` | C |
| P0 | `src/lib/indexnow.ts` | A.1 |
| P0 | `src/lib/google-indexing.ts` | B.1 |
| P0 | `scripts/permanent/indexnow-submit.ts` | A.2 |
| P0 | `scripts/permanent/submit-to-indexnow.ts` | A.3 |
| P0 | `scripts/permanent/submit-to-google-index.ts` | B.2 |
| P0 | `scripts/permanent/submit-all-to-google-index.ts` | B.3 |
| P0 | `public/{INDEXNOW_KEY}.txt` | 内容与 KEY 相同 |
| P1 | `.github/workflows/google-indexing.yml` | D |
| P1 | `.env.example` | E |

依赖：`npm install google-auth-library dotenv tsx`

---

## C. 决策树

```
配置 IndexNow / Google Indexing API
│
├─ IndexNow
│   ├─ Bing Webmaster → Settings → API Access → Generate Key → INDEXNOW_KEY
│   ├─ public/{KEY}.txt → 部署验证文件
│   ├─ 创建附录 A + C
│   └─ npm run indexnow / indexnow:all → Bing Webmaster 查看接收记录
│
├─ Google Indexing API
│   ├─ 提醒：GCP 启用 API + GSC Owner + GCP_SA_KEY
│   ├─ 创建附录 B + D
│   └─ Actions: check_status → submit 首页
│
└─ 新 URL
    ├─ 更新 urls.ts PAGE_PATHS
    ├─ npm run indexnow <url>
    └─ npm run google-index <path>
```

---

## D. Agent 执行顺序

1. 确认 medo 部署仓库路径
2. 按附录 B 创建文件；`.env.example` 仅用占位符
3. 提醒人类：Bing Webmaster 生成 KEY、配置 GSC Owner、配置 Secrets
4. 验证：`curl https://medo.dev/{KEY}.txt` → `npm run indexnow` → Actions 跑 `google-index --status`

---

## E. 禁止项

| ID | 禁止 |
|----|------|
| F1 | commit GCP JSON 或 `INDEXNOW_KEY` |
| F2 | GSC 权限用 Full 而非 Owner |
| F3 | 使用 `google.indexing()` 包装器 |
| F4 | 文档/代码硬编码真实密钥路径或账号 |

---

## F. 错误码 → 动作

| 错误 | 动作 |
|------|------|
| IndexNow 403 | 附录 F |
| IndexNow 202 | 提示等待密钥验证 |
| Google ETIMEDOUT | 附录 D Actions |
| Google 401 | 检查附录 B JWT 实现 |
| Google 403 | Part I §4.2 GSC Owner |
| Google 429 | 停止批量，次日继续 |

---

## G. 命令速查

```bash
npm run indexnow https://medo.dev/blog/{slug}/
npm run indexnow:all
npm run google-index -- --status https://medo.dev/
npm run google-index /blog/{slug}/
npm run google-index:all
npm run google-index -- --type URL_DELETED /old-path/
```

---

# 附录 A — IndexNow

## A.1 `src/lib/indexnow.ts`

```typescript
const INDEXNOW_API_URL = 'https://api.indexnow.org/indexnow';
const SITE_HOST = 'medo.dev';
const BASE_URL = 'https://medo.dev';

function hostnameMatchesSite(hostname: string, host: string): boolean {
  const bare = hostname.replace(/^www\./, '');
  const site = host.replace(/^www\./, '');
  return bare === site;
}

export function getIndexNowConfig(): { key: string; keyLocation: string; host: string } {
  const key = process.env.INDEXNOW_KEY?.trim();
  if (!key) throw new Error('[IndexNow] INDEXNOW_KEY not set. See .env.example');
  const keyLocation =
    process.env.INDEXNOW_KEY_LOCATION?.trim() || `${BASE_URL}/${key}.txt`;
  return { key, keyLocation, host: SITE_HOST };
}

export async function submitUrlsToIndexNow(urls: string[]): Promise<boolean> {
  if (!urls.length) return false;
  const { key, keyLocation, host } = getIndexNowConfig();

  const validUrls = urls.filter((url) => {
    try {
      return hostnameMatchesSite(new URL(url).hostname, host);
    } catch {
      return false;
    }
  });
  if (!validUrls.length) return false;

  const res = await fetch(INDEXNOW_API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: JSON.stringify({ host, key, keyLocation, urlList: validUrls }),
  });

  if (res.ok) {
    console.log(`[IndexNow] Submitted ${validUrls.length} URL(s) — HTTP ${res.status}`);
    return true;
  }
  const text = await res.text().catch(() => '');
  console.error(`[IndexNow] Failed: ${res.status} ${res.statusText}`, text.slice(0, 200));
  return false;
}

export function buildFullUrl(path: string): string {
  return `${BASE_URL}${path.startsWith('/') ? path : `/${path}`}`;
}
```

## A.2 `scripts/permanent/indexnow-submit.ts`

```typescript
import 'dotenv/config';
import { getAllPageUrls } from '../../src/lib/urls';
import { getIndexNowConfig, submitUrlsToIndexNow } from '../../src/lib/indexnow';

const BATCH = 10_000;

async function main() {
  getIndexNowConfig();
  const urls = getAllPageUrls();
  console.log(`[IndexNow] ${urls.length} URL(s)`);

  for (let i = 0; i < urls.length; i += BATCH) {
    const ok = await submitUrlsToIndexNow(urls.slice(i, i + BATCH));
    if (!ok) process.exit(1);
  }
  console.log('[IndexNow] Done.');
}

main().catch((e) => { console.error(e); process.exit(1); });
```

## A.3 `scripts/permanent/submit-to-indexnow.ts`

```typescript
import 'dotenv/config';
import { buildFullUrl, submitUrlsToIndexNow } from '../../src/lib/indexnow';

async function main() {
  const args = process.argv.slice(2);
  const urls =
    args.length > 0
      ? args.map((a) => (a.startsWith('http') ? a : buildFullUrl(a)))
      : [buildFullUrl('/')];
  process.exit((await submitUrlsToIndexNow(urls)) ? 0 : 1);
}

main();
```

---

# 附录 B — Google Indexing API

## B.1 `src/lib/google-indexing.ts`

```typescript
import { JWT } from 'google-auth-library';
import path from 'path';
import fs from 'fs';
import os from 'os';
import https from 'https';
import dns from 'dns';

const IPV4_HTTPS_AGENT = new https.Agent({
  family: 4,
  keepAlive: true,
  lookup: (hostname, _opts, cb) => dns.lookup(hostname, { family: 4 }, cb),
});

function getEnv(key: string, fallback = ''): string {
  if (process.env[key]) return process.env[key];
  try {
    const envPath = path.resolve(process.cwd(), '.env.local');
    if (fs.existsSync(envPath)) {
      for (const line of fs.readFileSync(envPath, 'utf-8').split('\n')) {
        const t = line.trim();
        if (!t || t.startsWith('#')) continue;
        const i = t.indexOf('=');
        if (i === -1) continue;
        if (t.slice(0, i).trim() === key) return t.slice(i + 1).trim();
      }
    }
  } catch { /* ignore */ }
  return fallback;
}

const SITE_URL = getEnv('GSC_SITE_URL', 'https://medo.dev').replace(/\/$/, '');
const SITE_HOST = new URL(SITE_URL).hostname.replace(/^www\./, '');
const KEY_FILE_PATH = getEnv('GOOGLE_INDEXING_KEY_FILE', '');
const DAILY_QUOTA = 200;
let quotaUsed = 0;

export type NotificationType = 'URL_UPDATED' | 'URL_DELETED';
export interface PublishResult {
  url: string; type: NotificationType; success: boolean;
  notifiedAt: string; error?: string;
}

export function getRemainingQuota() { return Math.max(0, DAILY_QUOTA - quotaUsed); }
export function getQuotaUsed() { return quotaUsed; }

let _auth: JWT | null = null;

function resolveKeyPath(): string {
  if (!KEY_FILE_PATH) throw new Error('[GoogleIndexing] GOOGLE_INDEXING_KEY_FILE not set');
  const p = KEY_FILE_PATH.startsWith('~/')
    ? path.join(os.homedir(), KEY_FILE_PATH.slice(2))
    : KEY_FILE_PATH;
  if (!fs.existsSync(p)) throw new Error(`[GoogleIndexing] Key file not found: ${p}`);
  return p;
}

async function getAuth(): Promise<JWT> {
  if (_auth) return _auth;
  const creds = JSON.parse(fs.readFileSync(resolveKeyPath(), 'utf-8'));
  if (!creds.client_email || !creds.private_key) throw new Error('[GoogleIndexing] Invalid key JSON');
  _auth = new JWT({
    email: creds.client_email,
    key: creds.private_key,
    keyId: creds.private_key_id,
    transporterOptions: { agent: IPV4_HTTPS_AGENT },
  });
  return _auth;
}

export function buildFullUrl(p: string): string {
  return `${SITE_URL}${p.startsWith('/') ? p : `/${p}`}`;
}

export async function publishUrlNotification(
  url: string,
  type: NotificationType = 'URL_UPDATED'
): Promise<PublishResult> {
  const base: PublishResult = { url, type, success: false, notifiedAt: new Date().toISOString() };
  try {
    if (new URL(url).hostname.replace(/^www\./, '') !== SITE_HOST) {
      return { ...base, error: `Host mismatch: expected ${SITE_HOST}` };
    }
  } catch {
    return { ...base, error: `Invalid URL: ${url}` };
  }
  if (quotaUsed >= DAILY_QUOTA) return { ...base, error: 'Daily quota exhausted' };

  try {
    const auth = await getAuth();
    await auth.request({
      url: 'https://indexing.googleapis.com/v3/urlNotifications:publish',
      method: 'POST',
      data: { url, type },
    });
    quotaUsed++;
    console.log(`[GoogleIndexing] OK ${type} | ${url} | quota: ${quotaUsed}/${DAILY_QUOTA}`);
    return { ...base, success: true };
  } catch (e: any) {
    const msg = e?.message || String(e);
    if (msg.includes('403')) return { ...base, error: '403: Add service account as GSC Owner' };
    if (msg.includes('429')) return { ...base, error: '429: Daily quota exceeded' };
    if (msg.includes('401')) return { ...base, error: '401: Use auth.request() with audience-only JWT' };
    return { ...base, error: msg };
  }
}

export async function publishBatch(
  urls: string[],
  type: NotificationType = 'URL_UPDATED',
  delayMs = 500
): Promise<PublishResult[]> {
  const slice = urls.slice(0, getRemainingQuota());
  const results: PublishResult[] = [];
  for (let i = 0; i < slice.length; i++) {
    results.push(await publishUrlNotification(slice[i], type));
    if (i < slice.length - 1 && delayMs > 0) await new Promise((r) => setTimeout(r, delayMs));
  }
  for (const url of urls.slice(slice.length)) {
    results.push({ url, type, success: false, notifiedAt: new Date().toISOString(), error: 'Skipped: quota' });
  }
  return results;
}

export async function getIndexStatus(url: string) {
  try {
    const auth = await getAuth();
    const res = await auth.request({
      url: 'https://indexing.googleapis.com/v3/urlNotifications/metadata',
      method: 'GET',
      params: { url },
    });
    return { url, raw: res.data as Record<string, unknown> };
  } catch (e: any) {
    if (e?.code === 404 || e?.status === 404) return { url, raw: {} };
    console.error('[GoogleIndexing]', e?.message || e);
    return null;
  }
}
```

## B.2 `scripts/permanent/submit-to-google-index.ts`

```typescript
import {
  buildFullUrl, publishUrlNotification, publishBatch,
  getIndexStatus, getRemainingQuota, getQuotaUsed,
} from '../../src/lib/google-indexing';
import type { NotificationType } from '../../src/lib/google-indexing';

const DEFAULT = 'https://medo.dev';

async function main() {
  const args = process.argv.slice(2);
  let type: NotificationType = 'URL_UPDATED';
  let statusMode = false;
  const urls: string[] = [];

  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a === '--type' && args[i + 1]) { type = args[++i] as NotificationType; continue; }
    if (a === '--status') { statusMode = true; continue; }
    if (!a.startsWith('--')) urls.push(a.startsWith('http') ? a : buildFullUrl(a));
  }

  const resolved = urls.length ? urls : [DEFAULT];

  if (statusMode) {
    console.log((await getIndexStatus(resolved[0])) ?? 'No status (check permissions)');
    return;
  }

  if (resolved.length === 1) {
    const r = await publishUrlNotification(resolved[0], type);
    if (!r.success) { console.error(r.error); process.exit(1); }
  } else {
    const rs = await publishBatch(resolved, type);
    if (rs.some((r) => !r.success)) process.exit(1);
  }
  console.log(`Remaining quota: ${getRemainingQuota()}/200 (used ${getQuotaUsed()})`);
}

main().catch((e) => { console.error(e); process.exit(1); });
```

## B.3 `scripts/permanent/submit-all-to-google-index.ts`

```typescript
import 'dotenv/config';
import { publishBatch, getQuotaUsed } from '../../src/lib/google-indexing';
import { getAllPageUrls } from '../../src/lib/urls';

async function main() {
  const urls = getAllPageUrls();
  console.log(`[GoogleIndexing] ${urls.length} URL(s), quota 200/day`);
  await publishBatch(urls, 'URL_UPDATED', 500);
  console.log(`Used: ${getQuotaUsed()}/200`);
}

main().catch((e) => { console.error(e); process.exit(1); });
```

---

# 附录 C — `src/lib/urls.ts`

```typescript
const BASE = 'https://medo.dev';

/** 需要通知搜索引擎的页面路径；发布新页时在此追加 */
export const PAGE_PATHS: string[] = [
  '/',
  '/blog/',
  // '/blog/example-slug/',
  // '/pricing/',
];

export function getAllPageUrls(): string[] {
  return PAGE_PATHS.map((p) => `${BASE}${p.startsWith('/') ? p : `/${p}`}`);
}
```

---

# 附录 D — GitHub Actions

`.github/workflows/google-indexing.yml`：

```yaml
name: Google Indexing

on:
  workflow_dispatch:
    inputs:
      mode:
        type: choice
        options: [submit_all, submit_urls, check_status]
        default: submit_all
      urls:
        required: false
        type: string
  schedule:
    - cron: '0 9 * * 1'

jobs:
  indexing:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: npm
      - run: npm ci   # 需已提交 package-lock.json；首次搭建可改为 npm install
      - name: Write service account key
        env:
          SA_KEY_FILE: ${{ runner.temp }}/sa-key.json
        run: echo '${{ secrets.GCP_SA_KEY }}' > "$SA_KEY_FILE"
      - name: Run Google Indexing
        env:
          GOOGLE_INDEXING_KEY_FILE: ${{ runner.temp }}/sa-key.json
          GSC_SITE_URL: https://medo.dev/
        run: |
          MODE="${{ github.event.inputs.mode }}"
          URLS="${{ github.event.inputs.urls }}"
          if [ "${{ github.event_name }}" = "schedule" ]; then
            npx tsx scripts/permanent/submit-all-to-google-index.ts
            exit $?
          fi
          case "$MODE" in
            submit_all) npx tsx scripts/permanent/submit-all-to-google-index.ts ;;
            submit_urls)
              [ -z "$URLS" ] && URLS="https://medo.dev/"
              npx tsx scripts/permanent/submit-to-google-index.ts $URLS ;;
            check_status)
              [ -z "$URLS" ] && URLS="https://medo.dev/"
              npx tsx scripts/permanent/submit-to-google-index.ts --status $URLS ;;
          esac
```

---

# 附录 E — `.env.example`

```bash
INDEXNOW_KEY=
# INDEXNOW_KEY_LOCATION=https://medo.dev/{INDEXNOW_KEY}.txt

GOOGLE_INDEXING_KEY_FILE=/absolute/path/to/service-account-key.json
GSC_SITE_URL=https://medo.dev/
```

| GitHub Secret | 内容 |
|---------------|------|
| `GCP_SA_KEY` | 服务账号 JSON 全文 |
| `INDEXNOW_KEY` | IndexNow 密钥（CI 需要时） |

---

# 附录 F — IndexNow 密钥排查

| 项目 | 要求 |
|------|------|
| 路径 | `https://medo.dev/{key}.txt` |
| 内容 | 仅密钥字符串 |
| 编码 | UTF-8 |
| 格式 | 8–128 字符，`a-z` `A-Z` `0-9` `-` |

检查清单：

- [ ] 已在 Bing Webmaster **Settings → API Access** 生成（或复制）密钥
- [ ] `INDEXNOW_KEY` 已写入 `.env` / Secret
- [ ] `public/{INDEXNOW_KEY}.txt` 内容与密钥一致
- [ ] 生产环境可 HTTP 200 访问
- [ ] `host` 与 URL 使用同一域名（www / 非 www 一致）

| HTTP | 含义 |
|------|------|
| 200 | 成功 |
| 202 | 已接受，验证待完成 |
| 403 | 密钥无效或文件不可达 |
| 422 | URL 不属于 host |

---

*指南 v1.4 · 范围：IndexNow + Google Indexing API only*
