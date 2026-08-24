# TLDR 底部 Star/Fork CTA 优化方案

在 TLDR 的 skillCta 区域增加对 [marketing-skills](https://github.com/kostja94/marketing-skills) 的 Star/Fork 呼吁，引导用户到 GitHub 获取 160+ 全套技能。

**参考**：[template-tldr-skill-cta](./template-tldr-skill-cta.md)

---

## 一、目标

| 目标 | 说明 |
|------|------|
| **转化 Star** | 引导用户 Star 项目，提升 marketing-skills 曝光与 discoverability |
| **转化 Fork** | 引导用户 Fork 获取完整 skills 结构（含 templates、docs） |
| **无缝衔接** | 与现有 skillCta（单技能安装）自然衔接，不割裂 |

---

## 二、技术方案

### 2.1 修改 Tldr 组件

在 `skillCta` 渲染块内、复制按钮之后，新增一行：

- **中文**：Star 或 Fork 获取 160+ 全套技能 →
- **英文**：Star or fork on GitHub for 160+ skills →
- **链接**：`https://github.com/kostja94/marketing-skills`，`target="_blank"`，`rel="noopener noreferrer"`

### 2.2 设计要点

- **同字号/色**：`text-[15px] text-muted-foreground`，与 description 一致
- **无分隔线**：不加 `border-t`，与上方命令块自然衔接
- **链接样式**：`hover:text-primary`，与站点链接风格一致

### 2.3 文案

| 语言 | 文案 |
|------|------|
| 中文 | Star 或 Fork 获取 160+ 全套技能 |
| 英文 | Star or fork on GitHub for 160+ skills |

---

## 三、实施范围

- 所有带 `skillCta` 的 Tldr 页面（约 50+ 页）自动生效
- 无需修改各 JSON 文件，仅改 Tldr 组件
