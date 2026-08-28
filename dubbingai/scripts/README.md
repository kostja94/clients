# Dubbing AI scripts

## OG cover generation (`ops/`)

两条**独立**流程，输出目录不同，禁止混用。

| Script | 流程 | 输出目录 |
|--------|------|----------|
| `generate-og-cover.py` | AI editorial collage（APINEED → 裁切 → WebP） | `blog/images/og/` |
| `analyze-og-page.py` | LLM brief → `data/og-briefs/` | — |
| `batch-generate-og-covers.py` | 批量 AI collage | `blog/images/og/` |
| `generate-og-dock.py` | **post-cover 单独流程**（PIL 叠字，无 AI 生图 API） | `blog/images/og-dock/` |
| `og_brief_lib.py` | AI collage brief / registry | — |
| `generate_og_cover_paths.py` | 路径 helper | — |

- AI collage SOP：[skills/ops/og-covers.md](../skills/ops/og-covers.md)
- post-cover dock SOP：[skills/ops/og-docks.md](../skills/ops/og-docks.md)

```powershell
# AI collage
$env:APINEED_API_KEY = "..."
python ops/generate-og-cover.py --slug best-ai-voice-changer

# post-cover dock（无需 API key）
python ops/generate-og-dock.py --slug spiderman-voice-changer-pubgm
```
