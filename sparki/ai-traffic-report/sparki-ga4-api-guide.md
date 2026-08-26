# Sparki GA4 API 接入操作指南

> 目标：通过 GA4 Data API 自动拉取 **AI 助手来源流量** + **全站页面流量**，输出 `ai-traffic-bundle-YYYY-MM-DD.json`。
> 适用对象：有 GCP 控制台和 sparki.io GA4 属性访问权限的技术同事。

---

## 一、前置准备

| 系统 | 网址 | 需要权限 |
|------|------|----------|
| Google Cloud Console | https://console.cloud.google.com | 项目 Owner 或 Editor |
| Google Analytics | https://analytics.google.com | sparki.io GA4 属性 **Viewer** 及以上 |

确认 GA4 属性 ID（Admin → Property settings → **Property ID**，纯数字）。

---

## 二、GCP 与服务账号

1. 创建或复用 GCP 项目
2. 启用 **Google Analytics Data API**
3. 创建服务账号 → 下载 JSON 密钥
4. 将以下写入 `scripts/.env`：

```env
GA4_PROPERTY_ID=123456789
GA4_CLIENT_EMAIL=xxx@xxx.iam.gserviceaccount.com
GA4_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
```

5. GA4 Admin → Property access management → 添加服务账号邮箱 → 角色 **Viewer**

---

## 三、脚本使用

```bash
cd ai-traffic-report/scripts
npm install
npm run fetch-all
```

| 命令 | 输出 |
|------|------|
| `npm run fetch-traffic` | `data/ga4-traffic-weekly-YYYY-MM-DD.json` |
| `npm run merge-traffic` | `data/ai-traffic-bundle-YYYY-MM-DD.json` |
| `npm run fetch-all` | 以上两步 |

可选环境变量：

| 变量 | 说明 |
|------|------|
| `REPORT_WEEK_END` | 指定周期结束日（周日），如 `2026-08-17` |
| `AI_SOURCE_REGISTRY_PATH` | 自定义 registry 路径 |

---

## 四、拉取的 GA4 报告

| 报告 key | 维度 | 筛选 | 用途 |
|----------|------|------|------|
| `aiBySource` | sessionSource, medium, channel | sourceRegex | AI 来源汇总 |
| `aiByLanding` | sessionSource, landingPage | sourceRegex | AI × 落地页 |
| `aiByReferrer` | pageReferrer, landingPage | referrer regex | 精确归因 |
| `allPagesByPath` | pagePath | **无** | 全站页面流量 |
| `allPagesByLanding` | landingPage | **无** | 入口页流量 |
| `siteByChannel` | sessionDefaultChannelGroup | **无** | 渠道结构 |
| `aiEvents` | sessionSource, eventName | sourceRegex | AI 来源转化 |

周期默认：**上周一至上周日** vs **再上一周**（以最近完整周为准）。

---

## 五、GA4 UI 手动导出（降级）

无 API 权限时，在 GA4 Explore 创建 Free form：

### 5.1 AI 来源流量

- **Filter**：Session source matches regex（见 `ai-source-registry.yaml` → `sourceRegex`）
- **Rows**：Session source / medium / Default channel group
- **Values**：Sessions, Total users, Engaged sessions
- 导出 → `ga4-ai-source-medium.csv`

### 5.2 AI 来源 × 落地页

- 同上 Filter
- **Rows**：Landing page + Session source
- 导出 → `ga4-ai-landing-x-source.csv`

### 5.3 全站页面（全渠道）

- **无 Filter**
- **Rows**：Page path
- **Values**：Sessions, Views, Total users
- 导出 → `ga4-all-pages.csv`

### 5.4 全站渠道

- **Rows**：Session default channel group
- 导出 → `ga4-channel-breakdown.csv`

将 CSV 与 Skill 全文 + registry 一并提交，指令见 SKILL.md §0.3。

---

## 六、AI Referrer 正则维护

正则存放在 `ai-source-registry.yaml` → `sourceRegex`。覆盖常见 AI 助手域（ChatGPT、Claude、Perplexity、Copilot、Gemini、DeepSeek 等）；完整列表见该文件 `aiSources[]`。

发现 GA4 中出现新 AI 域但不在 `aiSources[]` 时：
1. 追加到 `aiSources` 列表
2. 更新 `sourceRegex`
3. 重新运行 `npm run fetch-all`

---

## 七、常见问题

**Q: AI 流量为 0 但 Prompt 抽样有 citation？**  
A: Citation ≠ click-through。部分助手不传递 referrer，流量会记为 Direct。报告须标注 dark traffic 限制（见 SKILL.md §6 三层测量）。

**Q: 本工具与「外链 Referral 周报」有何不同？**  
A: 本工具追踪 **AI 助手引荐** + **全站页面流量**，服务 GEO click-through 监测；guest post / listicle 外链归因属另一类专项。

**Q: 需要 GSC 吗？**  
A: 非必须。有 GSC 可补充搜索表现，但不影响本 bundle 生成。

*Last updated: 2026-08-24 · v1.0.1 self-contained*
