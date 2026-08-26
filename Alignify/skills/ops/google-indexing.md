# Google Indexing API 集成指南（完整实施文档）

> **部署仓库**：脚本位于 `alignify-by-kostja/scripts/permanent/submit-to-google-index.ts` 与 `submit-all-to-google-index.ts`；核心库位于 `src/lib/google-indexing.ts`；GitHub Actions workflow 位于 `.github/workflows/google-indexing.yml`；npm 命令 `google-index` / `google-index:all` 在 `package.json` 中注册。

---

## 1. 概述

Google Indexing API 允许网站通过服务账号认证，主动通知 Google 页面变更（URL_UPDATED）或删除（URL_DELETED），并查询指定 URL 的通知历史。与被动等待 Googlebot 抓取（数天至数周）相比，Indexing API 可在几分钟内触发 Google 对指定 URL 的重新处理。

**核心数据**：

| 项目 | 值 |
|------|-----|
| API 端点 | `https://indexing.googleapis.com/v3/urlNotifications` |
| 认证方式 | 服务账号自签名 JWT（audience-only，无 OAuth token 交换） |
| 每日配额 | 200 URL（免费层级） |
| 权限要求 | 服务账号在 Google Search Console 中为 **Owner** |
| Google Cloud 项目 | `crypto-reality-485804-j5` |
| 服务账号 | `zyjstc@crypto-reality-485804-j5.iam.gserviceaccount.com` |
| 密钥文件 | `D:\项目文档\数据类\crypto-reality-485804-j5-c20f817c7dd2.json` |

**与 IndexNow 的关系**：

| 维度 | IndexNow | Google Indexing API |
|------|----------|---------------------|
| 覆盖引擎 | Bing, Yandex, Seznam, Naver | Google 专用 |
| 认证 | API Key（文件验证） | 自签名 JWT |
| 配额 | 无限制 | 200 URL/天 |
| 批量提交 | 单次 10,000 URL | 每次 1 URL（逐个调用） |
| 适用场景 | 全站定期批量 | 新页面/重要页面即时通知 |

推荐策略：全量用 IndexNow（`npm run indexnow:all`），Google API 用于即时通知和增量提交。

---

## 2. 前置准备

### 2.1 创建 Google Cloud 项目 & 服务账号

1. 访问 [Google Cloud Console](https://console.google.com/)
2. 创建项目（名称如 `alignify-indexing`）
3. **APIs & Services → Library** → 搜索启用 **Indexing API**
4. **IAM & Admin → Service Accounts → Create Service Account**
   - 名称：`alignify-indexing`
   - 创建后进入该账号 → **Keys → Add Key → Create New Key → JSON**
   - 下载 JSON 密钥文件，妥善保存（**勿提交 Git**）

### 2.2 授权服务账号访问 Search Console（⭐ 关键步骤）

这是最容易遗漏的一步。即使 GCP 项目配置正确，**缺此步骤必然返回 403**。

1. 访问 [Google Search Console](https://search.google.com/search-console)
2. 选择目标站点（如 `alignify.co`）
3. **Settings**（左下齿轮图标）→ **Users and permissions**
4. 点 **Add user**
5. 填入服务账号 email（在 JSON 密钥文件中 `client_email` 字段）
6. 权限选择 **Owner**（Indexing API 必须 Owner，不能是 Full）
7. 点 **Add**

### 2.3 配置环境变量

将密钥文件路径写入 `.env.local`（本地）或设为 GitHub Secret（CI）：

```bash
# 本地 .env.local
GOOGLE_INDEXING_KEY_FILE=d:/项目文档/数据类/crypto-reality-485804-j5-c20f817c7dd2.json
GSC_SITE_URL=https://alignify.co/

# GitHub Actions: Settings → Secrets → Actions → New repository secret
# Name: GCP_SA_KEY
# Value: <完整 JSON 文件内容>
```

---

## 3. 代码架构

### 3.1 文件结构

```
alignify-by-kostja/
├── .env.example                              # GOOGLE_INDEXING_KEY_FILE + GSC_SITE_URL 模板
├── .github/workflows/google-indexing.yml     # GitHub Actions 自动/手动触发
├── src/lib/
│   ├── indexnow.ts                           # IndexNow 核心模块（API Key 认证）
│   └── google-indexing.ts                    # Google Indexing 核心模块（JWT 认证）
├── scripts/permanent/
│   ├── submit-to-indexnow.ts                 # IndexNow 单页提交
│   ├── submit-all-pages-to-indexnow.ts       # IndexNow 全站提交
│   ├── submit-to-google-index.ts             # Google 单页/状态查询
│   └── submit-all-to-google-index.ts         # Google 全站提交
└── package.json                              # npm scripts 注册
```

### 3.2 核心认证方式：audience-only 自签名 JWT

**为什么不用标准 OAuth 2.0？**

标准 OAuth 流程需要 JWT 签名后 POST 到 `https://oauth2.googleapis.com/token` 换取 access token，再拿 token 调 API。这条路有两个问题：

1. **网络依赖**：国内/某些网络环境无法直连 `oauth2.googleapis.com`（ETIMEDOUT）
2. **额外延迟**：每次认证多一次 HTTP 往返

**解决方案：audience-only 自签名 JWT**

Google 部分 API 支持直接将签名后的 JWT 用作 Bearer token，跳过 OAuth token 交换。JWT 的 `aud`（audience）设为 API 端点域名 `https://indexing.googleapis.com/`，而非 token 端点。

关键代码（`src/lib/google-indexing.ts`）：

```typescript
import { JWT } from 'google-auth-library';

// 注意：不传 scopes 参数 — 传了会触发 OAuth 流程
_authClient = new JWT({
  email: creds.client_email,       // 从 JSON 密钥文件读取
  key: creds.private_key,          // RSA 私钥
  keyId: creds.private_key_id,     // 私钥 ID（可选但推荐）
  defaultServicePath: 'indexing.googleapis.com',  // 用于推断 aud
  transporterOptions: { agent: IPV4_HTTPS_AGENT }, // IPv4 强制
});
```

**注意**：不要传 `scopes` 参数。即使加上 `useJWTAccessWithScope: true`，google-auth-library 对 Indexing API 仍会回退到 `oauth2.googleapis.com/token`。audience-only（无 scopes）是经过验证的可行方式。

### 3.3 为什么用 `auth.request()` 而非 `google.indexing()`

**这是一个踩过的坑。**

`googleapis` 的 `google.indexing({ version: 'v3', auth })` 包装器不兼容 audience-only JWT。它内部期望 OAuth scoped 凭据，导致认证头不传，返回 `401 missing required authentication credential`。

修复方式是直接使用 JWT 客户端原生的 `auth.request()` 方法：

```typescript
// ✗ 错误（会 401）
const indexing = google.indexing({ version: 'v3', auth });
const response = await indexing.urlNotifications.publish({
  requestBody: { url, type },
});

// ✓ 正确
const response = await auth.request({
  url: 'https://indexing.googleapis.com/v3/urlNotifications:publish',
  method: 'POST',
  data: { url, type },
});
```

`auth.request()` 底层走 gaxios，会自动挂载自签名 JWT 到 `Authorization: Bearer <jwt>` 头。

### 3.4 IPv4 Agent（解决 Windows Node.js 网络问题）

**问题**：Windows 上 Node.js 的 Happy Eyeballs（RFC 8305）算法可能优先尝试 IPv6，若 IPv6 路由不通则超时。即使使用 `--dns-result-order=ipv4first` 也不一定生效。

**解决**：给 gaxios 注入 `https.Agent({ family: 4 })`，强制所有 Google API 请求走 IPv4：

```typescript
import https from 'https';
import dns from 'dns';

const IPV4_HTTPS_AGENT = new https.Agent({
  family: 4,
  keepAlive: true,
  lookup: (hostname, _options, callback) => {
    dns.lookup(hostname, { family: 4 }, callback);
  },
});

// 注入到 JWT 客户端的 transporterOptions 中
_authClient = new JWT({
  // ...其他配置
  transporterOptions: { agent: IPV4_HTTPS_AGENT },
});
```

### 3.5 配额管理

Google 每日免费配额为 200 URL。库内置进程级追踪：

- `publishBatch()` 自动截断超过 200 的 URL，输出跳过列表
- `resetQuota()` 可手动重置（跨批提交时调用）
- 每个请求后打印 `quota: N/200` 进度

---

## 4. npm 命令

| 命令 | 用途 |
|------|------|
| `npm run google-index` | 提交单个/少量 URL（默认首页） |
| `npm run google-index /tools/chatgpt` | 提交指定相对路径 |
| `npm run google-index -- --status https://alignify.co/` | 检查索引通知状态 |
| `npm run google-index -- --type URL_DELETED /old-page` | 提交删除通知 |
| `npm run google-index:all` | 全站批量提交（受 200/天配额限制） |

---

## 5. GitHub Actions 部署

### 5.1 为什么用 GitHub Actions

本机网络（国内环境）对 Google API 域名不可达（curl -4 也超时）。GitHub Actions 的 `ubuntu-latest` runner 部署在海外，天然可达所有 Google 端点，无需代理/VPN。同时避免密钥泄漏风险（密钥只存 GitHub Secret，不出本机）。

### 5.2 Workflow 设计

`.github/workflows/google-indexing.yml`：

- **trigger**：`workflow_dispatch`（手动触发，可选模式 + URL 参数）+ `schedule`（每周一 UTC 9:00 自动全站提交）
- **步骤**：checkout → setup Node.js 20 → `npm ci` → 写密钥文件到 `$RUNNER_TEMP` → 运行 tsx 脚本
- **密钥注入**：GitHub Secret `GCP_SA_KEY` → 运行时写入 `$RUNNER_TEMP/sa-key.json` → 通过 `GOOGLE_INDEXING_KEY_FILE` 环境变量传给脚本

Workflow 完整内容见 `alignify-by-kostja/.github/workflows/google-indexing.yml`。

### 5.3 设置步骤

**第 1 步：添加 Secret**

仓库 Settings → Secrets and variables → Actions → New repository secret：
- Name: `GCP_SA_KEY`
- Value: 完整的服务账号 JSON 密钥文件内容

**第 2 步：推送代码**

```bash
git add .github/workflows/google-indexing.yml scripts/permanent/submit-to-google-index.ts scripts/permanent/submit-all-to-google-index.ts src/lib/google-indexing.ts
git commit -m "Add Google Indexing API integration"
git push
```

**第 3 步：验证连通性**

Actions 标签页 → 左侧 Google Indexing → Run workflow：
- Mode: `check_status`, URLs: `https://alignify.co/`
- 成功：exit 0，日志显示正常
- 失败：见下方诊断流程

**第 4 步：验证提交权限**

同上，Mode: `submit_urls`, URLs: `https://alignify.co/`
- 成功：日志显示 `OK URL_UPDATED`
- 403：检查 Search Console 权限

**第 5 步：首次全站提交**

Mode: `submit_all`
- 注意：Google 每日 200 URL 配额。全站超过 200 时自动截断，需分多天提交

### 5.4 踩过的坑（⚠️ 务必注意）

| 坑 | 表现 | 原因 | 解决 |
|----|------|------|------|
| `--` 分隔符 | `Unknown option: --` | workflow YAML 中 `npx tsx ... -- --status` 的 `--` 被当成脚本参数传入 | 去掉多余 `--`：`npx tsx ... --status` |
| 新文件未推送 | `ERR_MODULE_NOT_FOUND` | Re-run 用的是旧 commit，不包含新文件 | push 后点 **Run workflow**（全新触发）而非 Re-run |
| `google.indexing()` | `401 missing required authentication` | googleapis 包装器不兼容 audience-only JWT | 改用 `auth.request()` 直调 API |
| OAuth 超时 | `ETIMEDOUT oauth2.googleapis.com` | 国内网络屏蔽 Google OAuth | 用 GitHub Actions 海外 runner，或本机配 HTTPS_PROXY |
| `useJWTAccessWithScope` 无效 | 仍走 OAuth 流程 | Indexing API 不支持此模式 | audience-only（不传 scopes）是唯一可行方式 |

---

## 6. 完整的错误诊断流程

当 `google-index` 失败时，按以下顺序排查：

1. **网络层**：错误含 `ETIMEDOUT` → 网络不可达
   - 本机：开 VPN/代理或改用 GitHub Actions
   - CI：检查 runner 网络
2. **认证层**：错误含 `401 missing required authentication` → JWT 没挂上
   - 检查是否用了 `auth.request()` 而非 `google.indexing()`
   - 检查 JWT 创建时是否**没有传 scopes**（audience-only 模式）
3. **权限层**：错误含 `403` → 服务账号未加到 Search Console Owner
   - 检查 Search Console → Settings → Users 是否有该 email
   - 权限必须是 Owner，不能是 Full
4. **配额层**：错误含 `429` → 当日配额耗尽
   - 等明天刷新，或检查进程内配额计数是否重复
5. **密钥层**：错误含 `GOOGLE_INDEXING_KEY_FILE not set`
   - 本地：检查 `.env.local` 是否存在且路径正确
   - CI：检查 GitHub Secret `GCP_SA_KEY` 是否已设置

---

## 7. 与 IndexNow 的联合使用策略

| 场景 | 工具 | 命令 |
|------|------|------|
| 全站首次通知所有引擎 | IndexNow | `npm run indexnow:all` |
| 定期全站刷新 | IndexNow（cron） | GitHub Actions 或 Vercel Cron |
| 新页面即时通知 Google | Google Indexing | `npm run google-index /new-page` |
| 删除页面通知 Google | Google Indexing | `npm run google-index -- --type URL_DELETED /old-page` |
| 检查 Google 通知状态 | Google Indexing | `npm run google-index -- --status /page` |
| 全站 Google 通知 | Google Indexing（限 200/天） | `npm run google-index:all`（GitHub Actions 每周自动） |

---

## 8. 新项目适配检查清单（可直接复制执行）

- [ ] 创建 Google Cloud 项目，启用 Indexing API
- [ ] 创建服务账号，下载 JSON 密钥文件
- [ ] 密钥文件安全存储（不提交 Git，用 `.env.local` 或 GitHub Secret）
- [ ] **服务账号 email 添加到 Search Console → Owner（⭐ 最易遗漏，缺此步必 403）**
- [ ] `npm install googleapis google-auth-library`（google-auth-library 已含在 googleapis 依赖中）
- [ ] 复制 `src/lib/google-indexing.ts`（核心库，约 300 行，可直接复用）
- [ ] 复制 `scripts/permanent/submit-to-google-index.ts`（单页 CLI 脚本）
- [ ] 复制 `scripts/permanent/submit-all-to-google-index.ts`（全站批量脚本）
- [ ] 确认 `src/data/site-pages-config.ts` 已导出 `getAllPageUrls(baseUrl)` 函数
- [ ] `package.json` 添加 `"google-index"` 和 `"google-index:all"` 脚本（用 `tsx` 运行）
- [ ] `.env.local` 配置 `GOOGLE_INDEXING_KEY_FILE` + `GSC_SITE_URL`
- [ ] 创建 `.github/workflows/google-indexing.yml`（推荐，用于 CI 环境）
- [ ] GitHub 仓库添加 Secret `GCP_SA_KEY`（如用 Actions）
- [ ] 验证认证：`npm run google-index -- --status https://yoursite.com/`
- [ ] 首次提交：`npm run google-index https://yoursite.com/`（先用单页测试）
- [ ] 确认成功后：`npm run google-index:all`（全站，GitHub Actions 上执行）

---

## 9. 产出物清单

| 文件 | 位置 | 说明 |
|------|------|------|
| 核心库 | `alignify-by-kostja/src/lib/google-indexing.ts` | JWT 认证、publish、getStatus、配额管理 |
| 单页脚本 | `alignify-by-kostja/scripts/permanent/submit-to-google-index.ts` | CLI 入口，支持 --status/--type/--delay |
| 全站脚本 | `alignify-by-kostja/scripts/permanent/submit-all-to-google-index.ts` | 从 site-pages-config 读取全站 URL 批量提交 |
| GitHub Actions | `alignify-by-kostja/.github/workflows/google-indexing.yml` | 手动触发 + 每周自动 cron |
| npm scripts | `alignify-by-kostja/package.json` | `google-index` / `google-index:all` 两条命令 |
| CLAUDE.md | `alignify-by-kostja/CLAUDE.md` | 已新增 google-index 命令说明 |
| .env.example | `alignify-by-kostja/.env.example` | 已新增 GOOGLE_INDEXING_KEY_FILE 模板 |
| 本文档 | `Alignify项目上下文/technical/technical-google-indexing.md` | 完整实施记录 |
| INDEX | `Alignify项目上下文/README.md` | 已合并入 README.md |
