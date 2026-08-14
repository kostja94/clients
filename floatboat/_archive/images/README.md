# 博客 OG 图片

本目录**有意不含**图片文件。各博客 Markdown 的 frontmatter 中：

```yaml
image: "/blog/images/{slug}-og.jpg"
```

指向 **floatboat.ai 现网** 的绝对路径（1200×630 OG 图）。

## 本地包内的对应关系

| 文章 slug | frontmatter `image` 路径 |
|-----------|-------------------------|
| introducing-floatim | `/blog/images/introducing-floatim-2026.jpg` |
| ai-scheduling-agent | `/blog/images/ai-scheduling-agent.jpg` |
| what-is-agentic-calendar | `/blog/images/agentic-calendar-definition-og.jpg` |
| calendar-driven-ai-vs-chat-ai | `/blog/images/calendar-driven-vs-chat-og.jpg` |
| best-ai-scheduling-assistants | `/blog/images/scheduling-assistants-comparison-og.jpg` |
| ai-meeting-preparation | `/blog/images/ai-meeting-prep-og.jpg` |
| ai-follow-up-automation | `/blog/images/ai-follow-up-automation-og.jpg` |
| claude-cowork-alternative | `/blog/images/claude-cowork-alternative-og.jpg` |

## 生成新图

按 [skills/floatboat-blog-article/floatboat-og-image-prompts.md](../skills/floatboat-blog-article/floatboat-og-image-prompts.md) 的 prompt 模板生成后，上传至现网 CMS 或静态资源目录。
