# IndexNow 故障排查

## 问题现象

- 提交返回 **202 Accepted**：请求已接受，但密钥验证待完成
- 提交返回 **403 Forbidden**：密钥验证失败
- Bing Webmaster 中 URL 未显示已接收

## 根本原因（常见）

**密钥文件无法访问**：`https://novascientia.com.br/{INDEXNOW_KEY}.txt` 若返回 404，搜索引擎无法验证所有权。

IndexNow 要求搜索引擎能抓取密钥文件以验证站点所有权。若密钥文件 404，验证会失败，导致 403 或 202 后无法完成索引。

本地与 CI 需在 `.env` 中配置 `INDEXNOW_KEY`，并在 `public/` 下放置同名 `.txt` 文件（内容仅为密钥字符串），与 [Bing IndexNow 说明](https://www.bing.com/indexnow/getstarted) 一致。

## 排查清单

### 1. 确认密钥文件已部署

- [ ] `.env` 中已设置 `INDEXNOW_KEY`（勿提交仓库）
- [ ] `public/{INDEXNOW_KEY}.txt` 存在且内容为纯密钥
- [ ] 最新代码已推送到 GitHub并完成部署
- [ ] 在浏览器中访问 `https://novascientia.com.br/{INDEXNOW_KEY}.txt` 无 404，正文与密钥一致

### 2. 密钥文件要求（IndexNow 规范）

| 项目 | 要求 |
|------|------|
| 路径 | 站点根目录：`https://novascientia.com.br/{key}.txt` |
| 内容 | 仅密钥字符串，无空格、换行或额外字符 |
| 编码 | UTF-8 |
| 密钥格式 | 8–128 字符，仅 a-z、A-Z、0-9、连字符 |

### 3. Bing Webmaster 验证

- [ ] 站点已添加到 [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [ ] 使用「通过放置 TXT 文件验证」时，文件名与 IndexNow 密钥一致
- [ ] 或使用 IndexNow 密钥文件作为验证文件（二者可共用）

### 4. host 参数一致性

- `host` 必须与密钥文件所在域名一致
- 当前脚本中：`novascientia.com.br`（无 www）
- 若站点强制跳转到 `www.novascientia.com.br`，需将 `host` 和 `INDEXNOW_KEY_LOCATION` 改为带 www 的完整 URL

### 5. robots.txt

- 确认未 Disallow 根路径或 `.txt` 文件
- 当前 `public/robots.txt` 已 Allow `/`，无问题

## 响应码说明（IndexNow 文档）

| 状态码 | 含义 |
|--------|------|
| 200 | 提交成功，密钥已验证 |
| 202 | 已接受，密钥验证待完成（需确保密钥文件可访问） |
| 403 | 密钥无效：文件不存在、无法访问或内容不匹配 |
| 422 | URL 不属于该 host，或密钥与协议不匹配 |

## 参考

- [Bing IndexNow 入门](https://www.bing.com/indexnow/getstarted)
- [IndexNow 协议文档](https://www.indexnow.org/documentation)
- [Rank Math: 403 错误修复](https://rankmath.com/kb/fix-403-forbidden-error-indexnow/)
