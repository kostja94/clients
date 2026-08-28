# Datus GSC + GA4 API 接入指南

> 目标：每周自动拉取 GSC + GA4，合并 `datus/blog` 目录，生成 `seo-report-bundle-YYYY-MM-DD.json`。
> 适用：有 GCP 与 GSC 权限的同事。
> 预计首次配置：2–3 小时。

---

## 一、前置权限

| 系统 | 需要 |
|------|------|
| [Google Cloud Console](https://console.cloud.google.com) | Editor 或 Owner |
| [Google Search Console](https://search.google.com/search-console) | `https://datus.ai/` Full 权限 |
| [Google Analytics](https://analytics.google.com) | datus.ai GA4 属性 Viewer |

---

## 二、GCP 服务账号（GSC + GA4 共用）

1. 新建 GCP 项目（如 `datus-analytics`）
2. 启用 API：
   - **Google Search Console API**
   - **Google Analytics Data API**
3. 创建服务账号 → 下载 JSON 密钥
4. GSC → 设置 → 用户和权限 → 添加服务账号邮箱（**Full**）
5. GA4 → Admin → Property Access Management → 添加 Viewer

---

## 三、配置 `.env`

```bash
cd seo-weekly-report/scripts
cp .env.example .env
```

填入：

| 变量 | 值 |
|------|-----|
| `GSC_SITE_URL` | `https://datus.ai/` |
| `GSC_CLIENT_EMAIL` | 服务账号 email |
| `GSC_PRIVATE_KEY` | JSON 中 private_key（保留 `\n`） |
| `GA4_PROPERTY_ID` | 数字 Property ID |
| `GA4_CLIENT_EMAIL` | 可与 GSC 相同 |
| `GA4_PRIVATE_KEY` | 可与 GSC 相同 |

**Blog 目录**（单独打包本文件夹给同事时）：

```env
BLOG_DIR=/path/to/datus/blog
```

---

## 四、每周命令

```bash
cd seo-weekly-report/scripts
npm install          # 首次
npm run fetch-all    # sync-blog → fetch-gsc → fetch-ga4 → merge
```

输出：

| 文件 | 内容 |
|------|------|
| `../blog-catalog.yaml` | 从 blog frontmatter 同步 |
| `../data/gsc-weekly-YYYY-MM-DD.json` | GSC 原始数据 |
| `../data/ga4-weekly-YYYY-MM-DD.json` | GA4 原始数据 |
| `../data/seo-report-bundle-YYYY-MM-DD.json` | **提交给 AI 的主文件** |

指定报告周（周日日期）：

```bash
REPORT_WEEK_END=2026-08-24 npm run fetch-all
```

---

## 五、手动降级（无 API）

1. GSC → 效果 → 搜索结果 → Compare 本周 vs 上周 → 导出 Queries/Pages/Countries/Devices xlsx
2. GA4 → Traffic acquisition → Compare → 导出 CSV
3. 运行 `npm run sync-blog` 更新 catalog
4. 将 xlsx/CSV + SKILL.md + 上周报告 + `===CONTENT===` 提交 AI（见 SKILL.md §0.3）

---

## 六、常见问题

**Q: GSC 403 / insufficient permission**  
A: 确认服务账号在 GSC 有 Full 权限；`GSC_SITE_URL` 与 GSC 属性 URL 完全一致（含尾部 `/`）。

**Q: GA4 无数据**  
A: 确认 Property ID 是 datus.ai 主站属性，非 studio/docs 子域。

**Q: blog-catalog 为空**  
A: 设置 `BLOG_DIR` 指向含 `*.md` 文章的 blog 目录。

**Q: 国内网络**  
A: Google API 需 VPN。

---

*Last updated: 2026-08-24*
