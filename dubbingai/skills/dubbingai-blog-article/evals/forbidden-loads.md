# Forbidden Loads — 不得触发 dubbingai-blog-article 的场景

## 1. title/description 专项优化

**输入**：「优化 /blog/best-ai-voice-changer 的 meta description」

**应触发**：未来 `dubbingai-meta-title-description` 或手动

---

## 2. 运行时读取 dubbingai-*.md

**输入**：Agent 打开 `dubbingai-keywords.md`

**应触发**：只读 `dubbingai/skills/dubbingai-blog-article/references/*.md`

---

## 3. HTML→MD CMS 迁移

**输入**：「运行 fetch_and_convert.py 迁移博客」

**应触发**：`blog/cms-export/scripts/` — 非本 skill

---

## 4. 韩国 Naver 韩文

**输入**：「写一篇 Naver 品牌长文」

**应触发**：`localization/` 独立 skill

---

## 5. 非 dubbingai.io 博客

**输入**：Medium guest post about voice changers

**应触发**：通用 blog skill

---

## 6. 加载整个 cms-export 目录

**输入**：Phase 0 批量 read cms-export/*.md

**应触发**：只读 content-graph §4.7 + 单行 manifest 查询

---

## 7. 301 源 slug 新稿

**输入**：创建 slug `top-5-voice-changers`

**应触发**：C4 STOP — 链 hub

---

## 8. Programmatic 页重写

**输入**：「重写 /voice-changer/gojo 落地页」

**应触发**：站点页面模板，非 blog skill
