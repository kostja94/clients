# DubbingAI GA4 Referral 数据 API 接入操作指南

> 目标：通过 GA4 Data API 自动拉取 Referral 渠道数据，按外链注册表匹配归因，输出 `referral-bundle-YYYY-MM-DD.json`。
> 适用对象：有 GCP 控制台和 dubbingai.io GA4 属性访问权限的技术同事。
> 预计耗时：首次配置约 1–2 小时。

---

## 目录

1. [前置准备](#一前置准备)
2. [GCP 与服务账号](#二gcp-与服务账号)
3. [GA4 属性授权](#三ga4-属性授权)
4. [本地环境搭建](#四本地环境搭建)
5. [脚本使用](#五脚本使用)
6. [GA4 UI 手动导出（降级）](#六ga4-ui-手动导出降级)
7. [Secrets 汇总](#七secrets-汇总)
8. [常见问题](#八常见问题)

---

## 一、前置准备

| 系统 | 网址 | 需要权限 |
|------|------|----------|
| Google Cloud Console | https://console.cloud.google.com | 项目 Owner 或 Editor |
| Google Analytics | https://analytics.google.com | dubbingai.io GA4 属性 **Viewer** 及以上 |

确认 GA4 属性 ID（Admin → Property settings → **Property ID**，纯数字）。

> **跨属性**：`shop.dubbingai.io` 若为独立 GA4 属性，本脚本 v1 仅拉主站属性；硬件 Referral 需 Phase 2 扩展。

---

## 二、GCP 与服务账号

### 2.1 创建或复用 GCP 项目

1. [Google Cloud Console](https://console.cloud.google.com) → 新建项目（如 `dubbingai-analytics`）
2. 记下 **项目 ID**

### 2.2 启用 Analytics Data API

1. **API 和服务** → **库**
2. 搜索 `Google Analytics Data API` → **启用**

### 2.3 创建服务账号

1. **API 和服务** → **凭据** → **创建凭据** → **服务账号**
2. 名称：`ga4-referral-reader`
3. 角色：无需 GCP 项目级角色（GA4 侧授权即可）
4. 创建密钥 → **JSON** → 下载保存（勿提交 Git）

从 JSON 提取：

| 字段 | 环境变量 |
|------|----------|
| `client_email` | `GA4_CLIENT_EMAIL` |
| `private_key` | `GA4_PRIVATE_KEY` |

---

## 三、GA4 属性授权

1. GA4 → **Admin** → **Property access management**
2. **+** → **Add users**
3. 填入服务账号邮箱（`ga4-referral-reader@...iam.gserviceaccount.com`）
4. 角色：**Viewer**
5. Save

---

## 四、本地环境搭建

```bash
cd dubbingai/referral-backlink-report/scripts
cp .env.example .env
npm install
```

编辑 `.env`：

```bash
GA4_PROPERTY_ID=123456789
GA4_CLIENT_EMAIL=ga4-referral-reader@dubbingai-analytics-xxxx.iam.gserviceaccount.com
GA4_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
BACKLINK_REGISTRY_PATH=../backlink-registry.yaml
# REPORT_WEEK_END=2026-08-17   # 可选，默认上周日
```

> `.env` 已在仓库根 `.gitignore` 中排除，勿提交。

---

## 五、脚本使用

### 5.1 脚本概览

| 脚本 | 功能 | 输出 |
|------|------|------|
| `fetch-ga4-referral.mjs` | 拉取 GA4 Referral 四表（本周+上周） | `data/ga4-referral-weekly-YYYY-MM-DD.json` |
| `merge-referral-weekly.mjs` | 匹配注册表 + 环比 + 告警 | `data/referral-bundle-YYYY-MM-DD.json` |

### 5.2 一键运行

```bash
npm run fetch-all
```

等效于：

```bash
node fetch-ga4-referral.mjs
node merge-referral-weekly.mjs
```

> **VPN**：需访问 `oauth2.googleapis.com` 与 `analyticsdata.googleapis.com`；国内网络通常需 VPN。

### 5.3 运行成功标志

```
═══ GA4 Referral 数据拉取 ═══
  周期: 2026-08-11 ~ 2026-08-17 (对比 2026-08-04 ~ 2026-08-10)
  [1/4] referral-by-source... ✓ 42 行
  [2/4] referral-by-landing... ✓ 128 行
  [3/4] referral-by-referrer... ✓ 86 行
  [4/4] referral-events... ✓ 15 行
  保存 → ../data/ga4-referral-weekly-2026-08-17.json ✓

═══ Referral 数据合并 ═══
  注册表: 5 条 live 外链
  匹配: 4/5 有流量
  保存 → ../data/referral-bundle-2026-08-17.json ✓
```

### 5.4 提交给 AI

```
附件：
  - dubbingai-referral-backlink-report-skill.md
  - backlink-registry.yaml
  - data/referral-bundle-2026-08-17.json
  - reports/dubbingai-referral-backlink-report-2026-08-10.md（上周）
  - ===BACKLINKS=== / ===OBSERVATIONS=== 文本

指令：按本 Skill（自动化模式）生成本周 DubbingAI 外链 Referral 效果周报
```

---

## 六、GA4 UI 手动导出（降级）

API 不可用时，从 GA4 UI 导出以下 CSV，连同 Skill + registry 提交：

| 报告 | 路径 | 文件名 |
|------|------|--------|
| Traffic acquisition | Reports → Acquisition → Traffic acquisition；Filter: Referral | `ga4-referral-source-medium.csv` |
| Landing × Source | Explore → Free form；Rows: Landing page + Session source | `ga4-referral-landing-x-source.csv` |
| Page referrer | Explore；Rows: Page referrer + Landing page | `ga4-referral-pageReferrer.csv` |
| Events | Reports → Engagement → Events；Filter: Referral | `ga4-referral-events.csv` |

日期：**必须** 本周 Mon–Sun vs 上周 Mon–Sun（Compare 模式）。

---

## 七、Secrets 汇总

| 环境变量 | 说明 | 获取方式 |
|----------|------|----------|
| `GA4_PROPERTY_ID` | GA4 属性 ID | GA4 Admin → Property settings |
| `GA4_CLIENT_EMAIL` | 服务账号邮箱 | GCP 服务账号 JSON |
| `GA4_PRIVATE_KEY` | 服务账号私钥 | GCP 服务账号 JSON |
| `BACKLINK_REGISTRY_PATH` | 注册表路径 | 默认 `../backlink-registry.yaml` |
| `REPORT_WEEK_END` | 报告周结束日（YYYY-MM-DD，通常为周日） | 可选，默认自动计算上周日 |

---

## 八、常见问题

**Q: 403 User does not have sufficient permissions**
A: 确认服务账号已在 GA4 Property access management 中添加为 Viewer。

**Q: 拉到的 Referral sessions 为 0**
A: 检查属性 ID 是否为主站；周期是否正确；Admin 中 Referral exclusions 是否过度排除。

**Q: pageReferrer 大量 (not set)**
A: 正常；merge 脚本会计算 `pageReferrerCoverage` 并在 bundle 中标注；报告降级 L1 域名归因。

**Q: 与 GA4 UI 数字差 5–10%**
A: API 与 UI 聚合口径可能略有差异；趋势对比保持同一数据源即可。

**Q: 如何追加 shop.dubbingai.io？**
A: Phase 2：第二套 `GA4_PROPERTY_ID_SHOP` 环境变量 + 合并脚本扩展。

---

*Last updated: 2026-08-20*
