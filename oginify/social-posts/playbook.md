# Oginify 社媒发帖 Playbook

> **本文档职责**：跨平台生成 SOP、发布检查清单。Repurpose 角度见 [templates/repurpose-matrix.md](./templates/repurpose-matrix.md)；口径见 [voice-and-messaging.md](./voice-and-messaging.md)。  
> **引用**：[index.md](./index.md) | [agent-prompt.md](./agent-prompt.md)

---

## 总流程

```
Phase A 准备输入
    → Phase B 按平台生成草稿
    → Phase C Repurpose（角度差异化，非复制粘贴）
    → Phase D 发布 + 首小时互动 + 归档
```

---

## Phase A — 准备输入

- [ ] 确定 **Milestone ID**（如 `M2`）与 **slug**（如 `first-user-feedback`）
- [ ] 从 [oginify-build-in-public.md](../oginify-build-in-public.md) 提取 **new_facts**（本次新进展）
- [ ] 阅读 [voice-and-messaging.md](./voice-and-messaging.md)
- [ ] 阅读目标平台：[platforms/linkedin.md](./platforms/linkedin.md) · [platforms/x.md](./platforms/x.md) · [platforms/jike.md](./platforms/jike.md)
- [ ] 准备素材：`demo_url`、carousel 张数、截图/生成图

---

## Phase B — 按平台生成（建议顺序）

| 顺序 | 平台 | 形态 | 语言 |
|------|------|------|------|
| 1 | LinkedIn | Carousel 文字帖 | EN |
| 2 | X | Article + 自动 Feed Post | ZH |
| 3 | 即刻 | 短帖或深度长文 | ZH |

各平台链接策略见 [platforms/](./platforms/) 专文，此处不重复。

---

## Phase C — Repurpose 规则

**同一 Milestone，三端讲同一个故事，但角度不同：**

| 元素 | LinkedIn | X Article | 即刻 |
|------|----------|-----------|------|
| 主轴 | Milestone + vulnerable | Milestone 起点 + 系列承诺 | 口语 BiP |
| 深度 | 中（图演示） | 深（长文） | 短 |
| OG/pSEO 洞察 | 支撑论点 | 独立章节 | 1–2 句 |

详见 [templates/repurpose-matrix.md](./templates/repurpose-matrix.md)。

---

## Phase D — 发布与归档

### 发布前检查

- [ ] 口径与 [voice-and-messaging.md](./voice-and-messaging.md) 一致
- [ ] LinkedIn：carousel 已上传；链接在**第一条评论**（若正文无链）
- [ ] X：Article 标题栏已填；正文小标题用 **Heading**（非 Subheading）
- [ ] X：Premium 已开通（Article 必需）
- [ ] 即刻：纯文本、无 Markdown 符号（见 [platforms/jike.md](./platforms/jike.md)）

### 发布后（首 60 分钟）

- [ ] 回复所有 early 评论（X 算法首小时窗口关键）
- [ ] LinkedIn / X teaser 下发布链接回复（若尚未发）
- [ ] 即刻可转发 LinkedIn/X 做二次触达（可选）

### 归档

- [ ] 新建 `published/Mx-{slug}/`
- [ ] 写入各平台 `.md` 全文 + `post.meta.yaml`（`status: published`，填 URL、`published_at`）
- [ ] 更新 [index.md](./index.md) Milestone 日历

---

## 推荐发布时间（参考）

| 平台 | 建议窗口 |
|------|----------|
| LinkedIn | 周二–周四，美东 8:00–10:00 |
| X | 与 LinkedIn 错开 2–4 小时 |
| 即刻 | 21:00–23:00 或工作日上午 9:00–10:00 |

---

## 指标回填（可选，每周）

在 `published/Mx-*/post.meta.yaml` 的 `metrics` 段填写 impressions / reactions / comments 等，便于对比哪条角度有效。

---

*Last updated: 2026-05-31*
