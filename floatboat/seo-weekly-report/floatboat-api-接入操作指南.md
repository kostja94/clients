# FloatBoat SEO 数据 API 接入操作指南

> 目标：通过 API 自动拉取 GSC、Bing Webmaster、GA4 三源数据，替代每周手动导出 xlsx/CSV 的重复操作。
> 适用对象：有 GCP 控制台和域名验证权限的技术同事。
> 预计耗时：首次配置约 2-3 小时。

---

## 目录

1. [前置准备：申请权限](#一前置准备申请权限)
2. [GSC API 接入](#二gsc-api-接入)
3. [Bing Webmaster API 接入](#三bing-webmaster-api-接入)
4. [GA4 API 接入](#四ga4-api-接入)
5. [数据拉取脚本使用](#五数据拉取脚本使用)
6. [Secrets 汇总表](#六secrets-汇总表)
7. [常见问题排查](#七常见问题排查)

---

## 一、前置准备：申请权限

### 你需要确保能访问以下系统：

| 系统 | 网址 | 需要权限 |
|------|------|----------|
| Google Cloud Console | `https://console.cloud.google.com` | 项目 Owner 或 Editor |
| Google Search Console | `https://search.google.com/search-console` | floatboat.ai 的 Full 权限 |
| Google Analytics | `https://analytics.google.com` | floatboat.ai GA4 属性的 Viewer 权限 |
| Bing Webmaster Tools | `https://www.bing.com/webmasters/` | floatboat.ai 的网站所有者 |

如果某个系统还没有权限，先找对应负责人添加。

---

## 二、GSC API 接入

Google Search Console API 用于拉取搜索绩效数据（点击、曝光、CTR、排名），按页面/关键词/国家/设备维度拆分，这是**周报的核心数据源**。

### 2.1 创建 GCP 项目

1. 打开 [Google Cloud Console](https://console.cloud.google.com)
2. 如果还没有项目，点击顶部项目下拉 → **新建项目**
   - 项目名称建议：`floatboat-analytics` 或 `floatboat-seo`
   - 记下 **项目 ID**（例如 `floatboat-analytics-1234`），后面会用到
3. 等待项目创建完成（通常几秒钟）

### 2.2 启用 Search Console API

1. 在 GCP 控制台左侧菜单 → **API 和服务** → **库**
2. 搜索框输入 `Google Search Console API`
3. 点击该 API → 点击 **启用**
4. 成功后页面会跳转到 API 概览页

### 2.3 创建服务账号

1. 左侧菜单 → **API 和服务** → **凭据**
2. 点击顶部 **+ 创建凭据** → **服务账号**
3. 填写信息：
   - 服务账号名称：`gsc-api-reader`
   - 服务账号 ID：自动生成，保持默认即可
   - 描述：`用于读取 GSC 搜索绩效数据`
4. 点击 **创建并继续**
5. 角色选择：**基本 → Viewer**（只读权限足够）
6. 点击 **完成**

### 2.4 下载服务账号密钥

1. 在凭据页面，找到刚创建的服务账号，点击其邮箱地址进入详情
2. 切换到 **密钥** 标签页
3. 点击 **添加密钥** → **创建新密钥**
4. 密钥类型选择 **JSON**
5. 浏览器会自动下载一个 `.json` 文件，**妥善保存**，文件名类似 `floatboat-analytics-xxxx-xxxxxxxxxxxx.json`

### 2.5 在 GSC 中授权服务账号

1. 打开 [Google Search Console](https://search.google.com/search-console)
2. 确保已选择 `https://floatboat.ai/` 属性（左上角下拉切换）
3. 左侧菜单 → **设置** → **用户和权限**
4. 点击 **添加用户**
5. 输入刚创建的服务账号邮箱（在密钥文件的 `client_email` 字段中，格式类似 `gsc-api-reader@floatboat-analytics-xxxx.iam.gserviceaccount.com`）
6. 权限选 **拥有者**（Full），否则无法读取 search analytics 数据
7. 点击 **添加**

### 2.6 验证配置

GSC API 配置完成。你需要保存以下信息供后续使用：

| 信息 | 位置 | 环境变量名 |
|------|------|------------|
| 服务账号邮箱 | JSON 文件中 `client_email` 字段 | `GSC_CLIENT_EMAIL` |
| 服务账号私钥 | JSON 文件中 `private_key` 字段（完整字符串，含 `\n`） | `GSC_PRIVATE_KEY` |
| 网站 URL | GSC 中已验证的属性 URL | `GSC_SITE_URL` = `https://floatboat.ai/` |

> **注意**：
> - 私钥是一段很长的字符串，以 `-----BEGIN PRIVATE KEY-----` 开头、`-----END PRIVATE KEY-----` 结尾。
> - 将密钥 JSON 文件保存到项目目录下的 `config/gsc-key.json`（脚本会自动读取），或通过 `.env` 文件配置环境变量。

---

## 三、Bing Webmaster API 接入

Bing 的接入比 GSC 简单得多——只需要一个 API Key，不需要任何 OAuth 或服务账号。

### 3.1 验证网站

1. 打开 [Bing Webmaster Tools](https://www.bing.com/webmasters/)
2. 如果 `floatboat.ai` 还没有添加，点击 **添加网站**
   - 输入 `https://floatboat.ai`
   - 选择验证方式（推荐：HTML meta 标签 或 DNS TXT 记录）
   - 按照提示完成验证
3. 验证成功后，该站点会出现在网站列表中

### 3.2 生成 API Key

1. 在 Bing Webmaster Tools 中，点击进入 `floatboat.ai` 站点
2. 左侧菜单 → **设置**（或右上角齿轮图标）→ **API 访问**
3. 点击 **生成 API Key**（Generate API Key）
4. **立即复制** API Key——这个值只显示一次，离开页面后无法再查看
5. 如果丢失，只能重新生成一个新的 Key

### 3.3 验证 API Key

用浏览器或 curl 测试 API Key 是否有效：

```
https://ssl.bing.com/webmaster/api.svc/json/GetPageStats?siteUrl=https://floatboat.ai&apikey=你的API_KEY
```

如果返回 JSON 数据（而不是错误信息），说明配置成功。

### 3.4 你需要保存的信息

| 信息 | 环境变量名 | 示例值 |
|------|------------|--------|
| API Key | `BING_API_KEY` | 一串字母数字字符串 |
| 网站 URL | `BING_SITE_URL` | `https://floatboat.ai` |

### 3.5 Bing API 能拉取的数据

| API 端点 | 返回数据 | GSC 是否有对应 |
|----------|----------|:---:|
| `GetPageStats` | 每个页面的点击、曝光、CTR、平均排名 | ✅ |
| `GetQueryStats` | 每个搜索词的点击、曝光、排名 + 关联页面 | ✅ |
| `GetCrawlIssues` | Bing 抓取 bot 发现的错误 URL | ❌ 独有 |
| `GetBacklinks` | 外链数据 | ❌ 独有 |

---

## 四、GA4 API 接入

Google Analytics Data API 用于拉取用户行为数据（UV、PV、会话时长、跳出率、事件转化），这是**补充搜索数据的关键**——GSC 只告诉你"搜到了、点了"，GA4 告诉你"点了之后做了什么"。

### 4.1 前提确认

FloatBoat 应该已经接入了 GA4。确认方式：
- 打开 [Google Analytics](https://analytics.google.com)
- 查看是否有 `floatboat.ai` 对应的 GA4 属性
- 记下 **GA4 属性 ID**（格式：`123456789`，不含 `G-` 前缀的纯数字）

如果没有 GA4，需要先通过 Google Tag Manager 接入，在 GTM 中创建 GA4 Configuration 标签，输入 Measurement ID（`G-XXXXXXXXXX`），触发器选 All Pages。

### 4.2 启用 Analytics Data API

1. 回到之前在 **2.1** 创建的 GCP 项目
2. 左侧菜单 → **API 和服务** → **库**
3. 搜索 `Google Analytics Data API`
4. 点击该 API → 点击 **启用**

### 4.3 授权服务账号访问 GA4

1. 打开 [Google Analytics](https://analytics.google.com)
2. 选择 floatboat.ai 对应的 GA4 属性
3. 左下角 **管理**（齿轮图标）
4. **属性** 列 → **属性访问管理**
5. 点击右上角 **+** → **添加用户**
6. 输入在 2.3 创建的服务账号邮箱（与 GSC 用的同一个）
7. 角色选 **查看者**（Viewer，只读即可）
8. 点击 **添加**

### 4.4 你需要保存的信息

| 信息 | 位置 | 环境变量名 |
|------|------|------------|
| GA4 属性 ID | GA4 管理 → 属性设置 → 属性 ID（纯数字） | `GA4_PROPERTY_ID` |
| 服务账号邮箱 | 同 GSC 的服务账号 | `GA4_CLIENT_EMAIL` |
| 服务账号私钥 | 同 GSC 的服务账号 | `GA4_PRIVATE_KEY` |

> **GA4 和 GSC 可以共用同一个 GCP 项目和服务账号**——只需额外启用 Analytics Data API 并在 GA4 中添加服务账号权限即可。

---

## 五、本地环境搭建与脚本使用

### 5.1 脚本概览

| 脚本 | 功能 | 输出文件 |
|------|------|----------|
| `fetch-gsc.mjs` | 拉取 GSC 本周+上周 7 天数据（page/query/country/device） | `data/gsc-weekly-YYYY-MM-DD.json` |
| `fetch-bing.mjs` | 拉取 Bing 页面+搜索词+抓取问题数据 | `data/bing-weekly-YYYY-MM-DD.json` |
| `fetch-ga4.mjs` | 拉取 GA4 概览+渠道+事件+Top页数据 | `data/ga4-weekly-YYYY-MM-DD.json` |
| `merge-weekly.mjs` | 合并三源 → 统一 bundle（含环比计算、品牌词拆分、数据校验） | `data/report-bundle-YYYY-MM-DD.json` |

### 5.2 配置本地 `.env` 文件

在项目根目录创建 `.env` 文件（此文件不应提交到 Git，已在 `.gitignore` 中配置），填入以下内容：

```bash
# ── GSC ──
GSC_SITE_URL=https://floatboat.ai/
GSC_CLIENT_EMAIL=gsc-api-reader@floatboat-analytics-xxxx.iam.gserviceaccount.com
GSC_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n你的私钥内容\n-----END PRIVATE KEY-----\n"

# ── Bing Webmaster ──
BING_API_KEY=你在BingWebmaster生成的APIKey
BING_SITE_URL=https://floatboat.ai

# ── GA4 ──
GA4_PROPERTY_ID=519618432
GA4_CLIENT_EMAIL=gsc-api-reader@floatboat-analytics-xxxx.iam.gserviceaccount.com
GA4_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n你的私钥内容\n-----END PRIVATE KEY-----\n"
```

> **填充说明**：
> - `GSC_CLIENT_EMAIL`、`GSC_PRIVATE_KEY`、`GA4_CLIENT_EMAIL`、`GA4_PRIVATE_KEY` 的值从第二章下载的 JSON 密钥文件中提取
> - GA4 和 GSC 共用同一个服务账号，所以 `GA4_CLIENT_EMAIL` 和 `GA4_PRIVATE_KEY` 与 GSC 的完全相同
> - `BING_API_KEY` 从第三章获取
> - `GA4_PROPERTY_ID` 从第四章获取
> - `.env` 文件不要提交到 Git——如果 team 内多人使用，各自维护自己的 `.env`

### 5.3 一键运行

配置好 `.env` 后，终端执行：

```bash
# 一次性拉取全部数据并合并
npm run fetch-all
```

等效于依次执行：

```bash
node scripts/fetch-gsc.mjs      # 先拉 GSC
node scripts/fetch-bing.mjs     # 再拉 Bing
node scripts/fetch-ga4.mjs      # 再拉 GA4
node scripts/merge-weekly.mjs   # 最后合并
```

> **VPN 提示**：GSC 和 GA4 脚本需要访问 `oauth2.googleapis.com`，国内网络无法直连，运行前请确保已开启 VPN。Bing 脚本不受此限制。

### 5.4 运行成功的标志

终端中会依次输出：

```
═══ GSC 数据拉取 ═══
  [1/3] 检查连通性... ✓
  [2/3] 拉取本周数据 (2026-07-06 ~ 2026-07-12)... 已获取: 283 行
  [3/3] 保存 → data/gsc-weekly-2026-07-13.json  ✓

═══ Bing 数据拉取 ═══
  [1/4] GetPageStats... ✓ 150 条
  [2/4] GetQueryStats... ✓ 320 条
  [3/4] GetCrawlIssues... ✓ 0 个问题
  [4/4] 保存 → data/bing-weekly-2026-07-13.json  ✓

═══ GA4 数据拉取 ═══
  [1/2] 拉取概览... ✓
  [2/2] 保存 → data/ga4-weekly-2026-07-13.json  ✓

═══ 数据合并 ═══
  数据源: GSC(283 pages) + Bing(150 pages) + GA4(80 pages)
  合并完成 → data/report-bundle-2026-07-13.json  ✓
```

### 5.5 数据使用方式

拉取完成后，`data/report-bundle-YYYY-MM-DD.json` 包含了周报 Skill 所需的全部结构化数据（格式与 Skill §2 的数据输入格式完全对应）。

提交给 AI 生成周报时，无需再手动导出 xlsx/CSV，直接附上 bundle 文件即可：

```
附件：
  - floatboat-seo-weekly-report-skill.md（Skill 全文）
  - data/report-bundle-2026-07-12.json（自动拉取的数据）
  - floatboat-seo-weekly-report-2026-07-05.md（上周报告）

指令：按 Skill 生成本周 FloatBoat SEO 周报
```

> **降级方案**：如果某周 API 出问题，仍可从 GSC/Bing 手动导出 xlsx/CSV，Skill 的 §0-a 保留了手动模式的说明。

---

## 六、Secrets 汇总表

以下是配置本地 `.env` 文件需要用到的所有环境变量。

### 6.1 全部变量清单

| 变量名 | 示例值 | 获取方式 |
|--------|--------|----------|
| `GSC_SITE_URL` | `https://floatboat.ai` | GSC 中已验证的属性 URL |
| `GSC_CLIENT_EMAIL` | `gsc-api-reader@floatboat-analytics.iam.gserviceaccount.com` | GCP 服务账号密钥 JSON → `client_email` |
| `GSC_PRIVATE_KEY` | `-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n` | GCP 服务账号密钥 JSON → `private_key` |
| `BING_API_KEY` | `abc123def456...` | Bing Webmaster → API Access → 生成 |
| `BING_SITE_URL` | `https://floatboat.ai` | Bing Webmaster 中已验证的站点 |
| `GA4_PROPERTY_ID` | `519618432` | GA4 管理 → 属性设置 → 属性 ID |
| `GA4_CLIENT_EMAIL` | 同 `GSC_CLIENT_EMAIL` | 与 GSC 共用服务账号 |
| `GA4_PRIVATE_KEY` | 同 `GSC_PRIVATE_KEY` | 与 GSC 共用服务账号 |

### 6.2 `.env` 文件配置步骤

1. 在项目根目录创建 `.env` 文件（如果已存在则编辑）
2. 按 6.1 表中的变量名填入对应值，格式参考 5.2 节的模板
3. 保存文件

> **`GSC_PRIVATE_KEY` 特别注意**：
> - JSON 密钥文件中的 `private_key` 本身就带 `\n` 换行符，直接复制全部内容（含引号）即可
> - `.env` 文件中值可以用双引号包裹：`GSC_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n..." `
> - 确保首尾没有多余空格

### 6.3 验证配置

配置完成后，在终端中运行一次验证脚本，确认所有 API 均可正常连接：

```bash
node scripts/check-api-access.mjs
```

预期输出：

```
检查 API 连通性...
  GSC API  : ✓ OK (test query returned 1 row)
  Bing API : ✓ OK (GetPageStats returned 150 records)
  GA4 API  : ✓ OK (overview fetched)
全部 API 连接正常。
```

如果某个 API 报错，参照第七章对应的故障排查条目解决。

---

## 七、常见问题排查

### Q1：GSC API 返回 403 或 "user does not have permission"

**原因**：服务账号在 GSC 中没有 Full 权限。
**解决**：GSC → 设置 → 用户和权限 → 确认服务账号邮箱已添加且权限为"拥有者"。

### Q2：运行脚本时报 "fetch failed" 或无法连接

**原因**：国内网络限制，`oauth2.googleapis.com` 无法直连。
**解决**：开启 VPN 后再运行脚本。Bing API 脚本不受此影响。

### Q3：GSC 返回 0 行数据

**可能原因**：
1. 时间范围太短（GSC 数据有 2-3 天延迟，endDate 需要设为 3 天前）
2. 站点是新站，暂无搜索流量
3. `GSC_SITE_URL` 格式不对（必须是 `https://floatboat.ai/` 末尾带 `/`）

### Q4：GA4 API 返回 "Analytics Data API has not been used in project"

**原因**：GA4 API 未在 GCP 项目中启用。
**解决**：回到 GCP → API 和服务 → 库 → 搜索 `Google Analytics Data API` → 启用。

### Q5：GA4 API 返回 403 但 GSC API 正常

**原因**：服务账号有 GSC 权限但没有 GA4 权限。
**解决**：GA4 管理 → 属性访问管理 → 添加服务账号邮箱（Viewer 即可）。

### Q6：Bing API 返回空数组 `[]`

**可能原因**：
1. API Key 已过期或未正确生成
2. 网站在 Bing 中还没有搜索数据（需先验证网站并在 Bing 中产生搜索流量）
**解决**：先用浏览器访问 `https://ssl.bing.com/webmaster/api.svc/json/GetPageStats?siteUrl=...&apikey=...` 看返回什么。

### Q7：Bing GetPageStats 的 `Query` 字段不是搜索词

**原因**：Bing API 的命名有历史遗留问题——`GetPageStats` 中的 `Query` 字段实际存储的是页面 URL，不是搜索词。真正的搜索词在 `GetQueryStats` 中。
**解决**：脚本已处理此问题。页面级数据使用 `Query` 字段作为 URL。

### Q8：GA4 和 GSC 的数据对不上（点击 vs 会话差很多）

**原因**：正常现象。GA4 统计的是"用户到达网站后会话开始"，GSC 统计的是"用户在 SERP 中点击"。差距通常 5-15%，原因包括：
- 用户点击后页面未完全加载就关闭
- JS 拦截/Cookie consent 阻挡 GA4 追踪
- GA4 的 `(not set)` 渠道会吞掉部分自然搜索
**解决**：周报 Skill 的 §3.5 已定义了正常偏差范围（5-15%），超过 20% 才需排查追踪代码。

---

---

*文档版本：v1.0 · 2026-07-13*
