# DubbingAI 外链 Referral 效果周报

本目录存放 **外链 Referral 追踪 Skill**、**外链注册表**、**GA4 API 脚本** 与 **历史报告**。

> 范围：仅 GA4 Referral 渠道，按已追踪外链 URL 归因，统计落地页与转化。不含 GSC/Bing 全站 SEO 周报。

---

## 文件清单

| 文件 | 用途 |
|------|------|
| [dubbingai-referral-backlink-report-skill.md](./dubbingai-referral-backlink-report-skill.md) | **唯一 Skill 文件**（v1.0.0）— 分析规则、输出模板、数据规范 |
| [dubbingai-ga4-referral-api-guide.md](./dubbingai-ga4-referral-api-guide.md) | GA4 Data API 接入与脚本使用 |
| [backlink-registry.yaml](./backlink-registry.yaml) | 外链主数据（持续维护） |
| `scripts/` | 自动拉数 + 合并脚本 |
| `data/` | JSON 输出（不入库，见 `.gitignore`） |
| `reports/` | 历史周报样例 |

---

## 每周最小数据包

按 Skill §0 准备：

1. **backlink-registry.yaml**（P0 必填 — 当周活跃外链）
2. **GA4 Referral 数据**（P0 必填 — API bundle 或 UI 导出 CSV）
3. **上周报告** md（P1 推荐）
4. **===BACKLINKS=== / ===OBSERVATIONS===** 文本块（P1 推荐）

---

## 快速开始

### 自动模式（推荐）

```bash
cd dubbingai/referral-backlink-report/scripts
cp .env.example .env
# 编辑 .env 填入 GA4 凭据
npm install
npm run fetch-all
```

将 Skill 全文 + `backlink-registry.yaml` + `data/referral-bundle-YYYY-MM-DD.json` + 上周报告 + 执行块提交给 AI：

> **指令**：请按本 Skill（识别 referral-bundle.json 自动化模式）生成本周 DubbingAI 外链 Referral 效果周报

### 手动模式（降级）

从 GA4 UI 导出 Referral 相关 CSV（见 [接入指南](./dubbingai-ga4-referral-api-guide.md) §5.4），连同 Skill + registry + 上周报告提交。

> **指令**：请按本 Skill 生成本周 DubbingAI 外链 Referral 效果周报

---

## 每周 SOP

1. 更新 `backlink-registry.yaml`（新上线 / 状态变更）
2. 填写 `===BACKLINKS===` / `===OBSERVATIONS===`
3. 运行 `npm run fetch-all`（或 GA4 UI 手动导出）
4. 提交数据包给 AI 生成报告
5. 保存至 `reports/dubbingai-referral-backlink-report-YYYY-MM-DD.md`
6. 处理零流量告警、补录未匹配新源

---

## 给 AI Agent 的用法

生成外链 Referral 周报时使用 [dubbingai-referral-backlink-report-skill.md](./dubbingai-referral-backlink-report-skill.md)；历史样例见 `reports/`。

*Last updated: 2026-08-20*
