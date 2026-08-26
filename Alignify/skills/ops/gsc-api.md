# Google Search Console API 集成

## 概述

通过 GCP 服务账号连接 Google Search Console API，在 Alignify 站内以 API Route 形式暴露三个接口：搜索绩效查询、URL 索引状态检查、站点地图管理。所有接口部署在 Vercel 生产环境，`/api/gsc/*` 路径下。

**上线日期**：2026-05-09  
**状态**：✅ 已部署，三个接口均可正常调用

---

## 架构

```
GCP 服务账号 (crypto-reality-485804-j5)
  └── Search Console API 已启用
  └── 已添加到 https://alignify.co/ 属性 (Full 权限)
        │
        ▼
  src/lib/gsc.ts          ← 认证层，初始化 googleapis 客户端
        │
        ├── app/api/gsc/search-analytics/route.ts   POST  搜索绩效
        ├── app/api/gsc/url-inspection/route.ts     POST  URL 索引状态
        └── app/api/gsc/sitemaps/route.ts           GET/POST  站点地图
```

### 认证方式

| 环境 | 方式 | 说明 |
|------|------|------|
| 本地开发 | `config/gsc-key.json`（项目内，gitignored） | `gsc.ts` 自动读取 `process.cwd()/config/gsc-key.json` |
| Vercel 生产 | `GSC_CLIENT_EMAIL` + `GSC_PRIVATE_KEY` 环境变量 | Vercel Dashboard 中配置 |

---

## 环境变量

| Key | 用途 | 环境 |
|-----|------|------|
| `GSC_SITE_URL` | Search Console 中已验证的属性 URL | 本地 + Vercel |
| `GSC_CLIENT_EMAIL` | 服务账号邮箱 | Vercel 生产 |
| `GSC_PRIVATE_KEY` | 服务账号私钥（含 BEGIN/END 行，多行） | Vercel 生产 |

本地 `.env.local` 只需 `GSC_SITE_URL`，认证走 `config/gsc-key.json`。

---

## API 接口

### 1. 搜索绩效查询

```
POST /api/gsc/search-analytics
```

**请求体**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `startDate` | string | ✅ | YYYY-MM-DD，太平洋时间 |
| `endDate` | string | ✅ | YYYY-MM-DD |
| `dimensions` | string[] | | query / page / country / device / date |
| `rowLimit` | number | | 1–25000，默认 1000 |
| `startRow` | number | | 分页偏移，从 0 起 |
| `type` | string | | web / discover / googleNews / news / image / video |
| `dataState` | string | | final / all / hourly_all |
| `filters` | object | | dimensionFilterGroups 数组 |

**返回**：`{ rows: [...], totalRows, metadata? }`

**示例**：
```bash
curl -X POST https://alignify.co/api/gsc/search-analytics \
  -H "Content-Type: application/json" \
  -d '{"startDate":"2026-05-02","endDate":"2026-05-09","dimensions":["query"],"rowLimit":10}'
```

### 2. URL 索引状态检查

```
POST /api/gsc/url-inspection
```

**请求体**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `inspectionUrl` | string | ✅ | 完整 URL |
| `languageCode` | string | | en-US / zh-CN，默认 en-US |

**返回**：`{ inspectionResult: {...} }` — 包含索引状态、抓取错误等

**示例**：
```bash
curl -X POST https://alignify.co/api/gsc/url-inspection \
  -H "Content-Type: application/json" \
  -d '{"inspectionUrl":"https://alignify.co/tools/documentation","languageCode":"en-US"}'
```

### 3. 站点地图管理

```
GET  /api/gsc/sitemaps     → 列出已提交的 sitemap
POST /api/gsc/sitemaps     → 提交 sitemap
```

**POST 请求体**：`{ "feedpath": "sitemap.xml" }`

**示例**：
```bash
# 列表
curl https://alignify.co/api/gsc/sitemaps

# 提交
curl -X POST https://alignify.co/api/gsc/sitemaps \
  -H "Content-Type: application/json" \
  -d '{"feedpath":"sitemap.xml"}'
```

---

## 代码位置

| 文件 | 说明 |
|------|------|
| `src/lib/gsc.ts` | 认证层：读取 key 文件 / env vars，初始化 `webmasters`(v3) 和 `searchconsole`(v1) 客户端 |
| `app/api/gsc/search-analytics/route.ts` | 搜索绩效 POST 接口 |
| `app/api/gsc/url-inspection/route.ts` | URL 索引状态 POST 接口 |
| `app/api/gsc/sitemaps/route.ts` | 站点地图 GET/POST 接口 |
| `config/gsc-key.json` | 服务账号密钥文件（gitignored，仅本地） |

---

## GCP 配置快照

| 项目 | 值 |
|------|----|
| GCP 项目 ID | `crypto-reality-485804-j5` |
| 服务账号 | `zyjstc@crypto-reality-485804-j5.iam.gserviceaccount.com` |
| 已启用 API | Google Search Console API |
| Search Console 属性 | `https://alignify.co/`（URL 前缀） |
| 权限 | Full |

---

## 已知限制

- **本地测试需要 VPN**：`oauth2.googleapis.com` 在国内无法直连。本地 `npm run dev` 调用 `/api/gsc/*` 时需要 VPN，否则 OAuth 令牌请求超时。
- **Search Analytics 不返回所有行**：API 与 GSC UI 一样存在匿名查询过滤，按 `query` 分组时的合计会低于无维度汇总。详见 `knowledge/tools/../分析-GSC-Search-Console-API-程序化指南-zh.md` 第七章。
- **`rowLimit` 上限 25,000**：超过需用 `startRow` 分页。

---

## 后续计划

- [ ] 搭建内部 SEO 看板页面，可视化 GSC 绩效数据
- [ ] 编写定时任务（npm script），定期拉取数据存档
- [ ] URL Inspection 批量检查新发布/更新的页面
- [ ] 过滤率对账脚本：对比无维度汇总 vs 按 query 分组

---

## 变更记录

| 日期 | 内容 |
|------|------|
| 2026-05-09 | 初始搭建：GCP 服务账号、三个 API Route、Vercel 环境变量、本地 key 文件配置 |
