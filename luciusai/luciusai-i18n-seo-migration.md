# Lucius AI 多语种 SEO 方案

> **来源**：luciusai.com 实站分析  
> **创建日期**：2026-07-31  
> **状态**：草案

**Last updated**: 2026-07-31 | 模式：国际版

---

## 一、问题

Lucius 当前通过 Cookie/LocalStorage 切换中英文，URL 不变（`luciusai.com/pricing` 通用于所有语言）。

**对 SEO 的影响**：Google 爬虫不携带 Cookie、不保持 localStorage 状态，每次抓取只能看到服务端默认返回的一种语言。中文内容对搜索引擎完全不可见。

| 当前 | 推荐 |
|------|------|
| `luciusai.com/pricing`（所有语言） | 英文：`luciusai.com/pricing` |
| | 中文：`luciusai.com/pricing/zh` |

---

## 二、方案

**英文（默认语言）使用根路径，其他语言使用子目录后缀。**

### URL 结构

| 页面 | 英文（不改动） | 中文（新增） |
|------|--------------|-------------|
| 定价 | `/pricing` | `/pricing/zh` |
| 案例 | `/case-studies` | `/case-studies/zh` |
| 对比 | `/compare` | `/compare/zh` |

### hreflang

每个页面声明语言版本关系：

```html
<!-- /pricing（英文） -->
<link rel="alternate" hreflang="en" href="https://luciusai.com/pricing" />
<link rel="alternate" hreflang="zh" href="https://luciusai.com/pricing/zh" />
<link rel="alternate" hreflang="x-default" href="https://luciusai.com/pricing" />

<!-- /pricing/zh（中文） -->
<link rel="alternate" hreflang="en" href="https://luciusai.com/pricing" />
<link rel="alternate" hreflang="zh" href="https://luciusai.com/pricing/zh" />
<link rel="alternate" hreflang="x-default" href="https://luciusai.com/pricing" />
```

### 跳转逻辑

- 无 `/zh` 后缀时，根据 Accept-Language 头判断是否需要跳转
- 中文用户访问 `/pricing` → 302 跳转到 `/pricing/zh`
- 英文用户访问 `/pricing` → 直接渲染，无需跳转
- 中文页面内切换为英文 → 跳转到根路径（去 `/zh` 后缀）

### Sitemap

两种语言版本都出现在 Sitemap 中，并附带 hreflang 声明。

---

## 三、迁移要点

### 工作量

英文 URL 保持不变，只需：

1. **新增路由**：为每页增加 `/:path/zh` 后缀路由
2. **添加 hreflang 标签**：在所有页面的 `<head>` 中声明语言关系
3. **改造语言切换器**：从 Cookie 驱动改为 URL 跳转
4. **服务端重定向**：根据 Accept-Language 302 跳转中文用户到 `/zh` 后缀
5. **更新 Sitemap**：加入 `*/zh` 版本及 hreflang

### 注意事项

- 英文 URL 完全不改动，已有的 Google 收录不受影响
- 中文 URL 是从零新增，无需处理 301（英文页面本来也没有中文内容被索引）
- 上线后在 GSC 提交新 Sitemap，监控 `/zh` 后缀页面的索引进度

---

## 四、风险

| 风险 | 缓解 |
|------|------|
| hreflang 配置错误 | 上线前用 Screaming Frog 或 GSC International Targeting 验证 |
| 中英文内容混合 | 确保 `/pricing/zh` 完全为中文，不能混入英文段落 |
| 频繁改动 URL 结构 | 本次为一次性迁移，之后保持稳定 |
