# Dubbing AI OG — post-cover 单独流程

> **与 AI 拼贴流程完全分离** · 不使用 APINEED / fal  
> 引擎：[chainepic/post-cover](https://github.com/chainepic/post-cover)（vendored 于 `_vendor/post-cover`）

---

## 1. 两条独立流水线

| 流程 | 脚本 | 输出目录 | 标题渲染 | 背景来源 |
|------|------|----------|----------|----------|
| **AI editorial collage** | `generate-og-cover.py` | `blog/images/og/` | AI 画字 | APINEED GPT Image 2 |
| **post-cover dock** | `generate-og-dock.py` | `blog/images/og-dock/` | **PIL 本地叠字** | 本地 / DDG 搜图 / 程序化渐变 |

**禁止混用**：dock 流程不得调用 `generate-og-cover.py` 或任何 AI 生图 API。

---

## 2. post-cover 工作流

```
data/dock-copy-registry.json（标题/副标题/搜图 query）
        ↓
post-cover 背景（Tier 1 本地 → Tier 3 DDG → Tier 4 程序化渐变）
        ↓
render_dock_cover（1920×1080 毛玻璃底栏 + 动态字号）
        ↓
scale → 1200×630 WebP
        ↓
blog/images/og-dock/{slug}/{slug}-og-en.webp
```

---

## 3. 执行

```powershell
pip install -r E:\clients\dubbingai\_vendor\post-cover\requirements.txt

# 自动搜背景 + 合成
python E:\clients\dubbingai\scripts\ops\generate-og-dock.py `
  --slug spiderman-voice-changer-pubgm

# 指定本地背景（100% 离线）
python E:\clients\dubbingai\scripts\ops\generate-og-dock.py `
  --slug spiderman-voice-changer-pubgm `
  --image path\to\photo.jpg

python E:\clients\dubbingai\scripts\ops\generate-og-dock.py --list
```

---

## 4. 新增文章

编辑 `data/dock-copy-registry.json`：

```json
"your-slug": {
  "title": "Article H1 (short enough for dock)",
  "subtitle": "One line · keywords",
  "note": "Evidence or hook line",
  "tags": "Bullet tags for right column",
  "search_query": "stock photo search terms (no trademarks)",
  "theme": "sky_blue"
}
```

主题预设见 post-cover README：`sky_blue` · `cyber_purple` · `orange_esports` 等。  
Dubbing accent 默认 `#22D3EE`（`defaults.accent_rgb`）。

---

## 5. CMS 路径

`/blog/images/og-dock/{slug}/{slug}-og-en.webp`

---

## 6. 关联

- AI collage 流程：[og-covers.md](./og-covers.md)
- post-cover 上游：[github.com/chainepic/post-cover](https://github.com/chainepic/post-cover)
