# VOMO 文章发布排障记录 — Preview API 创建草稿失败

> 记录日期：2026-08-07
> 环境：Windows 11 · Node.js v22.21.0 · 发布包 `vomo-article-publisher-preview-handoff`
> 状态：**阻塞中**（对方 Preview API 服务端 bug，非客户端问题）

---

## 1. 背景与目标

- 稿件：`01-how-to-convert-podcast-to-blog-post.md`（本地新建稿 01，HowTo / use-cases）
- 发布方式：通过 `vomo-article-publisher-preview-handoff` 发布包调用 VOMO **Preview 环境** API
- 发布包路径：`C:\Users\zyjst\Downloads\vomo-article-publisher-preview-handoff\vomo-article-publisher-handoff`
- 目标：创建草稿 → 获得 Preview URL → 把文章交付给对方审核（**非生产发布**）

## 2. 网络前置问题（已解决）

Node.js 内置 `fetch` 默认**不走系统代理**，本机外网需经本地代理（Veee，`localhost:15236`），导致发布脚本报 `UND_ERR_CONNECT_TIMEOUT`。

**解决**：用 `undici` 的 `ProxyAgent` 显式指定代理，再以 `--import` 预加载：

```bash
node --import "file:///path/to/proxy-agent.mjs" \
  scripts/vomo-article.mjs draft article.md
```

```js
// proxy-agent.mjs
import { ProxyAgent, setGlobalDispatcher } from "undici";
setGlobalDispatcher(new ProxyAgent({ uri: "http://localhost:15236" }));
```

## 3. 稿件字段问题（已修复）

原稿 frontmatter 为本地稿件格式，与发布 API 要求的字段**不一致**，validate 直接 422。

| 原稿字段 | API 要求字段 | 差异 |
|---|---|---|
| `title` | `title` | 一致 |
| `slug` | `slug` | 一致 |
| `category` | `category` | 一致 |
| `description` | `excerpt` | 字段名不同 |
| `date: 2026-08-05` | `publishedAt: 2026-08-05T00:00:00Z` | 字段名 + 格式不同 |
| `author: "VOMO Team"` | —（多余字段） | API 拒绝未知字段 |
| — | `seoTitle` | 缺失 |
| — | `seoDescription` | 缺失 |
| — | `featuredImage`（**必填**） | 缺失 |
| — | `featuredImageAlt` | 缺失 |

**修复方式**：生成规范格式转换稿 `01-how-to-convert-podcast-to-blog-post.publish.md`，并生成占位封面图 `images/cover.png`。转换后 validate 通过（HTTP 200）。

## 4. 核心 bug：create 草稿接口返回 400

### 4.1 复现过程（发布脚本完整追踪）

| 步骤 | 端点 | 结果 |
|---|---|---|
| 1. 校验 | `POST /api/internal/content/articles/validate` | ✅ 200 |
| 2. 上传封面图 | `POST /api/internal/content/media` | ✅ 200（`mediaId: 2894`，`reused: true`） |
| 3. 创建草稿 | `POST /api/internal/content/articles` | ❌ **400** `{"error":"Internal server error"}` |

### 4.2 排除性证据（已穷举）

| 变量 | 测试内容 | 结果 |
|---|---|---|
| 文章内容 | 本稿件 / 发布包自带模板 / 最小测试文章 | create 全部 400 |
| slug 唯一性 | 含随机唯一 slug（如 `zzz-probe-t8v916fuch`） | create 照样 400 |
| 客户端 | Node 内置 fetch（发布脚本本身）/ npm undici v7 / curl | 全部 400 |
| 请求体 | 带 `mediaByPath` / 空 `{}` / 不带该字段 / `null` | 全部 400 |

### 4.3 结论

- validate 与 media 上传正常，唯独 **create 端点抛未捕获异常**，被统一包装成 `{"error":"Internal server error"}`。
- 最可能是该端点**写入数据库环节**在 Preview 环境不可用（数据库未开通 / 连接失败 / 构建版本 bug）。
- **属对方服务器（Lovable 上 `vomo-article-publisher` 项目 Preview 环境）问题，非客户端或稿件问题。**

## 5. 待办 / 移交信息

发对方排查时建议附上：

1. 发布包 `vomo-article-publisher-preview-handoff`
2. 转换稿 `vomo/blog/01-how-to-convert-podcast-to-blog-post.publish.md`
3. 封面图 `vomo/blog/images/cover.png`
4. 复现命令与完整追踪输出（见 §4.1）
5. 端点：`POST {VOMO_CONTENT_API_URL}/api/internal/content/articles`（Preview 域名：`vomo-web-preview.truant-wz.workers.dev`）

---

*记录人：AI agent（应 @vomo/blog 要求记录）*
