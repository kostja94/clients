# Dubbing AI scripts

## OG cover generation

生图管线已统一迁移到 `E:\clients\Image Generator`（见其 [README](../../Image%20Generator/README.md)）。
本目录只保留 LLM 页面分析助手。

| Script | 流程 | 位置 |
|--------|------|------|
| `generate-og-cover.py` / `batch-generate-og-covers.py` | AI editorial collage（fal / apineed / gitaigc → 裁切 → WebP） | `E:\clients\Image Generator\`（`--client dubbingai`） |
| `ops/analyze-og-page.py` | LLM brief → `data/og-briefs/` | 本目录 |

- AI collage SOP：[skills/ops/og-covers.md](../skills/ops/og-covers.md)
- ~~post-cover dock 流程~~（`generate-og-dock.py` / `og-docks.md` / `_vendor/post-cover`）已于 2026-09 移除（效果不佳，不再使用），代码与历史产出已删除；存档 OG 图统一在 `E:\clients\Image Generator\output\`。

```powershell
# AI collage
$env:APINEED_API_KEY = "..."
python "E:\clients\Image Generator\generate-og-cover.py" --client dubbingai --slug best-ai-voice-changer
```
