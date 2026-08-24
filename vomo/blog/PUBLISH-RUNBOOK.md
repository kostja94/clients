# VOMO 文章发布流程（Runbook）

## 0. 快速结论（当前状态）

- ✅ Preview 环境 API 已恢复（8/9 曾部分故障，8/11 复测 validate 可用）
- ✅ 文章 `how-to-convert-podcast-to-blog-post` 已于 8/9 创建草稿（Article ID `989`，封面 `mediaId=2894`）
- ❌ **publish 被卡**：8/11 复测 token 对 validate / publish 全部返回 **401 Unauthorized**，Preview 草稿链接也已 404（签名过期）
  → 判定：**对方已更换/撤销 Preview token**。需向对方索取新 token（或新发布包）后才能继续 publish。
- ⚠️ 注意：本文档保存的 token 为**旧 token（已失效）**，仅作留档，勿外传。

---

## 1. 前置条件

| 项 | 说明 |
|---|---|
| 客户端 | **不需要 Node.js**。本机方案 = Windows 自带 `curl.exe` + PowerShell 脚本 `vomo/blog/publish-article.ps1` |
| 环境变量 | `VOMO_CONTENT_API_URL` + `VOMO_CONTENT_API_TOKEN`（见 §6） |
| 网络代理 | 本机外网需走本地代理（Veee，`http://localhost:15236`）；脚本已自动处理 |
| 必需文件 | ① 规范格式稿 `NN-{slug}.publish.md` ② 封面图 `images/cover.png`（相对稿件路径） |

发布包原说明（START-HERE.md）要点：
- 仅连接 **Preview 环境**，不连生产
- Token 具写权限 → **禁止**提交 Git / 公开传播 / 上传云盘公共链接
- 未获明确"确认发布"前，**禁止**执行 `publish`

---

## 2. 文章格式规范（必需，改动会 422）

frontmatter 必须**恰好**包含以下字段（多余字段会被 API 拒绝）：

```yaml
title: string
slug: lowercase-kebab-case
excerpt: string
category: use-cases | ai-transcription | ai-insights
publishedAt: 2026-08-05T10:00:00Z        # ISO 8601
seoTitle: string
seoDescription: string
featuredImage: relative/path/image.webp   # 相对稿件文件
featuredImageAlt: string
```

正文允许：H2-H4、段落、粗体/斜体/删除线、链接、有序/无序列表、引用、围栏代码、行内代码、GFM 表格、分隔线、本地图片。

**禁止**：H1、HTML、MDX、脚本、任务列表、嵌套列表、远程图片、SVG、绝对路径图片、父目录路径。
内链以 `/` 开头（如 `/guide/how-to-convert-audio-to-text`）；外链用 `https://` / `http://` / `mailto:`。
图片单独成行并给 alt；格式限 JPEG/PNG/WebP/AVIF，单张 ≤10MB，含封面 ≤20 张。

> 原稿 `NN-{slug}.md` 是本地稿格式（`description`/`date`/`author` 等字段），**不能直接发布**。需转换字段：
> `description→excerpt`，`date: 2026-08-05→publishedAt: 2026-08-05T00:00:00Z`，删除 `author`，补齐 `seoTitle` / `seoDescription` / `featuredImage` / `featuredImageAlt`。
> 转换稿统一命名 `NN-{slug}.publish.md`。

---

## 3. 完整命令流程

> 以下命令在 PowerShell 中执行。`<token>` 从 §6 获取；代理默认 `localhost:15236`。

### 3.0 设置环境变量（每次新开终端都要执行）

```powershell
$env:VOMO_CONTENT_API_URL = "https://vomo-web-preview.truant-wz.workers.dev"
$env:VOMO_CONTENT_API_TOKEN = "<token>"
```

### 3.1 校验（必须通过再下一步）

```powershell
& "d:\项目文档\clients\vomo\blog\publish-article.ps1" validate `
  "d:\项目文档\clients\vomo\blog\01-how-to-convert-podcast-to-blog-post.publish.md"
```

预期输出：`Valid: <slug>` / `Assets: N`。任何报错先修稿再重试。

### 3.2 创建草稿（上传封面 + 建草稿，返回 Preview URL）

```powershell
& "d:\项目文档\clients\vomo\blog\publish-article.ps1" draft `
  "d:\项目文档\clients\vomo\blog\01-how-to-convert-podcast-to-blog-post.publish.md"
```

预期输出：`Article ID` / `updatedAt` / `contentHash` / `Preview:` URL。

**保存 `Article ID` 和 `updatedAt`（publish 必须用草稿返回的原始值）。**
把 Preview URL 发给审核人；**审核人明确说"确认发布"前，不执行 publish。**

### 3.3 发布（审核确认后）

```powershell
& "d:\项目文档\clients\vomo\blog\publish-article.ps1" publish `
  --article-id <ID> --updated-at <updatedAt>
```

预期输出：`English published: <url>` / `Translation job: <jobId>`。

### 3.4 查看翻译进度

```powershell
& "d:\项目文档\clients\vomo\blog\publish-article.ps1" status --job-id <jobId>
```

### 3.5 重试失败的语种 / sitemap

原发布包提供 `retry --job-id <jobId> --locale <locale>` 与 `retry --job-id <jobId> --sitemap`，本地 PS1 尚未实现，需要时按原包接口补（或直接用 curl，见 §7.3）。

### 3.6 完成判定（原包标准）

- 英文 URL 已发布
- 15 个本地化 URL 全部 `published`
- 无 `queued` / `translating` / `failed`
- Sitemap `completed`
- 汇报：article ID、翻译 job ID、英文 URL、各失败语种及精确重试命令

---

## 4. 本地脚本 `publish-article.ps1` 说明

位置：`vomo/blog/publish-article.ps1`（本仓库内，已随项目保存，不依赖下载包）。

功能：`validate | draft | publish | status`。纯 PowerShell + `curl.exe`，无 Node.js。

要点：
- 代理默认 `http://localhost:15236`，可用 `HTTPS_PROXY` 环境变量覆盖
- JSON 请求体先写入临时文件再用 `curl --data-binary` 发送，避免编码问题
- 图片上传用 `curl -F` 构造 multipart（PowerShell 5.1 的 `Invoke-RestMethod` 不支持 `-Form`）
- HTTP 2xx 视为成功（create 草稿返回 201，不是 200）
- `publish` 命令不带 `--wait`，发布后需手动 `status` 轮询

---

## 5. 已知坑与解决方案（务必先看）

| # | 坑 | 现象 | 解决 |
|---|---|---|---|
| 1 | PowerShell 5.1 把无 BOM 的 UTF-8 脚本按 GBK 解析 | 中文注释/字符串导致语法错误 | 脚本全部用 ASCII（本脚本已处理） |
| 2 | `ConvertTo-Json -Depth 5` 膨胀 bug | 15KB 文章被序列化成 2.25MB，`-Depth 10` 直接卡死 | 一律用默认深度（脚本已处理） |
| 3 | `Get-Content` 返回"带附加属性的字符串" | `ConvertTo-Json` 把 markdown 变成 `{value, PSPath, ...}` 对象 → 服务端 422 | 用 `[System.IO.File]::ReadAllText(...)` 读文件（脚本已处理） |
| 4 | Node `fetch` / PowerShell 不走系统代理 | 超时 `UND_ERR_CONNECT_TIMEOUT` 或挂起 | 显式走本地代理（脚本已处理） |
| 5 | 原稿字段与 API 不符 | validate 422 | 用 `.publish.md` 转换稿（§2 字段对照） |
| 6 | HTTP 201 被误判为失败 | create 返回 201 却报错 | 2xx 均视为成功（脚本已修复） |
| 7 | **token 被对方轮换** | 所有端点返回 401 | 向对方索取新 token / 新发布包 |

---

## 6. 凭据留档

> ⚠️ **敏感信息，仅限本机使用，禁止外传 / 提交 Git / 上传任何公共位置。**

- Preview API URL：`https://vomo-web-preview.truant-wz.workers.dev`
- **旧 Preview token（2026-08-11 已确认失效，401）**：`08e195d658f2b593e82486a15646366a3edf6f5f60d47b05358d1efa54446f8d`
- 原 `.env.preview` 文件路径（发布包内，将随发布包删除）：`...\vomo-article-publisher-handoff\.env.preview`

**下一步**：向对方索取**新的** Preview token（或新发布包），替换 §3.0 后重跑 `validate → draft → publish`。

---

## 7. 原始发布包参考信息（存档，便于恢复）

原包结构：
```
vomo-article-publisher-handoff/
├── .env.preview            # VOMO_CONTENT_API_URL / VOMO_CONTENT_API_TOKEN
├── START-HERE.md           # 使用说明（步骤 0-5 + 完成检查清单）
├── AGENT-PROMPT.txt        # 给 Agent 的提示词
└── vomo-article-publisher/
    ├── SKILL.md            # 工作流定义（validate→draft→publish→status→retry）
    ├── references/article-format.md   # 格式规范（= §2）
    ├── assets/article-template.md     # 文章模板
    └── scripts/vomo-article.mjs       # Node 版 API 客户端（validate/draft/publish/status/retry）
```

### 7.1 Node 版原命令（若改用 Node.js 20+）

```bash
set -a && source .env.preview && set +a
node vomo-article-publisher/scripts/vomo-article.mjs validate /path/article.md
node vomo-article-publisher/scripts/vomo-article.mjs draft /path/article.md
node vomo-article-publisher/scripts/vomo-article.mjs publish --article-id ID --updated-at VALUE --wait
node vomo-article-publisher/scripts/vomo-article.mjs status --job-id ID
node vomo-article-publisher/scripts/vomo-article.mjs retry --job-id ID --locale ja
node vomo-article-publisher/scripts/vomo-article.mjs retry --job-id ID --sitemap
```

### 7.2 API 端点

| 步骤 | 端点 | 说明 |
|---|---|---|
| 校验 | `POST /api/internal/content/articles/validate` | body: `{schemaVersion:1, markdown}`，返回 metadata + requiredAssets |
| 传图 | `POST /api/internal/content/media` | multipart：`schemaVersion` `file` `alt` `sourcePath` `sha256` |
| 建稿 | `POST /api/internal/content/articles` | body: `{schemaVersion:1, markdown, mediaByPath}` → 返回 `articleId/updatedAt/contentHash/previewUrl/url` |
| 发布 | `POST /api/internal/content/articles/{id}/publish` | body: `{schemaVersion:1, expectedUpdatedAt}` → `url/translationJobId` |
| 状态 | `GET /api/internal/content/translation-jobs/{jobId}` | → `english/progress/locales[]/sitemap` |
| 重试 | `POST /api/internal/content/translation-jobs/{jobId}/locales/{locale}/retry` | 单语种重试 |
| 重试 | `POST /api/internal/content/translation-jobs/{jobId}/sitemap/retry` | sitemap 重试 |

请求头一律带 `Authorization: Bearer <token>`。

### 7.3 纯 curl 最小示例（不依赖脚本）

```powershell
# validate
curl.exe -x http://localhost:15236 -s -X POST "$env:VOMO_CONTENT_API_URL/api/internal/content/articles/validate" `
  -H "Authorization: Bearer $env:VOMO_CONTENT_API_TOKEN" -H "Content-Type: application/json" `
  -d '{"schemaVersion":1,"markdown":"# probe"}'

# 上传封面（multipart）
curl.exe -x http://localhost:15236 -s -X POST "$env:VOMO_CONTENT_API_URL/api/internal/content/media" `
  -H "Authorization: Bearer $env:VOMO_CONTENT_API_TOKEN" `
  -F "schemaVersion=1" -F "file=@d:/项目文档/clients/vomo/blog/images/cover.png;type=image/png" `
  -F "alt=cover" -F "sourcePath=images/cover.png" -F "sha256=<file sha256>"

# 发布
curl.exe -x http://localhost:15236 -s -X POST "$env:VOMO_CONTENT_API_URL/api/internal/content/articles/989/publish" `
  -H "Authorization: Bearer $env:VOMO_CONTENT_API_TOKEN" -H "Content-Type: application/json" `
  -d '{"schemaVersion":1,"expectedUpdatedAt":"2026-08-09T10:11:46.034Z"}'
```

---

## 8. 执行日志（本次）

| 日期 | 事件 | 结果 |
|---|---|---|
| 2026-08-07 | 排障：validate 200、media 200、create 400 | 记录于 `PUBLISH-TROUBLESHOOTING.md` |
| 2026-08-09 | Preview 部分恢复：validate 曾全挂（422 Internal server error）；修复脚本序列化后 validate 通过 | — |
| 2026-08-09 | `draft` 成功：Article ID `989`，updatedAt `2026-08-09T10:11:46.034Z`，封面 `mediaId=2894` | ✅ |
| 2026-08-09 | Preview URL（已过期）：`https://vomo-web-preview.truant-wz.workers.dev/guide/how-to-convert-podcast-to-blog-post?previewArticle=989&expires=1786272107&signature=...` | — |
| 2026-08-11 | 用户确认发布；执行 publish 被 **401 Unauthorized** 拦截 | ❌ 待新 token |

---

*记录日期：2026-08-11*
*目的：完整固化 VOMO 文章发布流程，即使原发布包 `vomo-article-publisher-preview-handoff` 被删除，也能凭本文档 + 本地脚本独立完成发布。*
*关联：[发布排障记录](./PUBLISH-TROUBLESHOOTING.md) · [README](./README.md)*
*Runbook v1.0 · AI agent 应 @vomo/blog 要求记录*
