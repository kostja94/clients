# Clients 任务看板

> 跨客户任务总览 · **Last updated**: 2026-08-21

**用法**：新任务进「待办」→ 执行中移「进行中」→ 完成移「已完成」。ID 格式 `{client}-{序号}`。

---

## 看板

### 待办

| ID | 客户 | 任务 | 优先级 | 备注 |
|----|------|------|:------:|------|
| datus-001 | datus | 调研 Dosi | P1 | 调研文档已建，待确认主张 |

### 进行中

| ID | 客户 | 任务 | 优先级 | 开始 | 备注 |
|----|------|------|:------:|------|------|
| | | | | | |

### 已完成

| ID | 客户 | 任务 | 完成 | 交付物 |
|----|------|------|------|--------|
| floatboat-001 | floatboat | 构建全站 SEO/GEO 审计 Skill 包（内部团队执行） | 2026-08-21 | [site-seo-geo-audit/](./floatboat/site-seo-geo-audit/) |

### 已阻塞

| ID | 客户 | 任务 | 原因 |
|----|------|------|------|
| | | | |

---

## 详情

### datus-001

- **目标**：调研 Dosi 新产品推广大方向（关键词 + 候选文章）
- **范围**：仅调研，不写文章、不改站
- **交付**：[datus-dosi.md](./datus/datus-dosi.md)
- **待确认**：「only Ossie implementation」等对外主张需产品/法务

### floatboat-001

- **目标**：交付自包含审计 Skill 包，供内部团队对 floatboat.ai 跑 full / delta / pre-launch 审计
- **范围**：Skill + checklist + references + tools + README；不含代跑审计、不改现网
- **入口**：[site-seo-geo-audit/README.md](./floatboat/site-seo-geo-audit/README.md)
- **下一步**（内部团队）：跑 tools → Agent full 审计 → 按 checklist 填 P0/P1/P2 → 工程修复

---

## 客户索引

| 客户 | 文件夹 | 已完成 |
|------|--------|:------:|
| datus | [datus/](./datus/) | 0 |
| floatboat | [floatboat/](./floatboat/) | 1 |
