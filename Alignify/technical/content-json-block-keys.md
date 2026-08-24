# Content JSON Block Key Reference

## Critical Rule: JSON keys MUST match ArticleFromJson expectations

Every block type in `src/content/render/ArticleFromJson.tsx` reads specific keys from the JSON. Using wrong key names causes the React component to receive `undefined` for arrays, which triggers `TypeError: Cannot read properties of undefined (reading 'map')` — resulting in a **blank page** (client-side exception caught by Next.js error boundary).

## Block type → expected array/data key

| Block type | Expected key | Component | What happens if wrong |
|---|---|---|---|
| `tldr` | `items` | `<Tldr>` | Blank page |
| `section` | `paragraphs` | `<Section>` | Empty section (safe — defaults to `[]`) |
| `howItWorks` | `advantages` | `<HowItWorks>` | Blank page |
| `bestTools` | `tools` | `<BestTools>` | Blank page |
| `useCases` | `useCases` | `<UseCases>` | Blank page |
| `howToChoose` | `steps` | `<HowToChoose>` | Blank page |
| `faq` | `items` | `<FAQ>` | Blank page |
| `references` | `items` | `<References>` | Blank page |
| `comparisonSection` | `table` (with `table.items`) | `<Table>` | No table rendered (safe — guarded) |
| `html` | `html` | Raw HTML | Empty div (safe) |

## Common mistakes (DO NOT DO)

| Wrong | Correct | Why it's wrong |
|---|---|---|
| `"references": [...]` in references block | `"items": [...]` | Key named after block type, not the expected field |
| `"questions": [...]` in faq block | `"items": [...]` | Alternative naming instead of standard `items` |
| `"cases": [...]` in useCases block | `"useCases": [...]` | Abbreviated name instead of full key |
| `"items": [...]` in useCases block | `"useCases": [...]` | Generic `items` instead of type-specific key |

## Verification script

Run this to check all content JSONs for key mismatches:

```bash
python3 << 'PYEOF'
import json, glob

BLOCK_ARRAY_FIELDS = {
    'tldr': 'items', 'section': 'paragraphs', 'howItWorks': 'advantages',
    'bestTools': 'tools', 'useCases': 'useCases', 'howToChoose': 'steps',
    'faq': 'items', 'references': 'items',
}

for pattern in ['content/tools/en/*.json', 'content/tools/zh/*.json', 'content/seo/en/*.json', 'content/seo/zh/*.json', 'content/marketing/en/*.json', 'content/marketing/zh/*.json', 'content/insights/en/*.json', 'content/insights/zh/*.json']:
    for f in sorted(glob.glob(pattern)):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                doc = json.load(fh)
        except Exception as e:
            print(f'CORRUPTED: {f}')
            continue
        for i, b in enumerate(doc.get('blocks', [])):
            bt = b.get('type', '')
            expected = BLOCK_ARRAY_FIELDS.get(bt)
            if expected and expected not in b:
                array_keys = [k for k, v in b.items() if isinstance(v, list) and k != 'subSections']
                if array_keys:
                    print(f'{f} block {i} ({bt}): has "{array_keys[0]}", expected "{expected}"')
PYEOF
```

## Locale field requirement

Blocks that display language-dependent text MUST have `"locale"` set correctly. Missing or wrong locale causes **cross-language display** (e.g., English page showing Chinese "参考文献" instead of "References").

### Components with visible locale-dependent text

| Component | Locale effect | Default if missing |
|---|---|---|
| `<References>` | Heading: "参考文献" (zh) vs "References" (en) | `"en"` (changed from `"zh"` on 2026-05-10) |
| `<BestTools>` | Button: "试试" (zh) vs "Try" (en) | `"en"` (from ArticleFromJson `?? "en"`) |
| `<HowItWorks>` | No visible effect (locale prop unused) | — |
| `<UseCases>` | No visible effect (locale prop unused) | — |
| `<Table>` | Column headers language | Derived from `usePathname()`, not from locale prop |

### Required locale per block type

| Block type | Requires locale? | Rule |
|---|---|---|
| `references` | **YES** | `"en"` for EN pages, `"zh"` for ZH pages |
| `bestTools` | **YES** | `"en"` for EN pages, `"zh"` for ZH pages |
| `howItWorks` | Defensive | Set matching page language |
| `useCases` | Defensive | Set matching page language |
| All others | No | — |

### Verification script (locale)

```bash
python3 << 'PYEOF'
import json, glob
for pattern in ['content/tools/en/*.json', 'content/tools/zh/*.json', 'content/seo/en/*.json', 'content/seo/zh/*.json', 'content/marketing/en/*.json', 'content/marketing/zh/*.json', 'content/insights/en/*.json', 'content/insights/zh/*.json']:
    for f in sorted(glob.glob(pattern)):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                doc = json.load(fh)
        except:
            print(f'CORRUPTED: {f}')
            continue
        expected = 'en' if '/en/' in f else 'zh'
        for i, b in enumerate(doc.get('blocks', [])):
            if b.get('type') in ('bestTools', 'howItWorks', 'useCases', 'references'):
                if b.get('locale') != expected:
                    print(f'{f} block {i} ({b["type"]}): locale={b.get("locale")} expected={expected}')
PYEOF
```

## Also check for Edit tool file corruption

The Edit tool truncates files after editing. After any Edit operation, verify:

```bash
# Check file sizes match git
git diff --stat HEAD -- path/to/file

# If file was edited but git shows no diff, the file may be corrupted
# Restore with: git checkout -- path/to/file
# Then re-apply edits using Python instead of the Edit tool
```

### Prevention rules

1. **Never use the Edit tool for JSON, TSX, or TS files** — always use Python scripts via Bash instead.
2. **After any Edit operation**, immediately verify the file is structurally complete (closing braces match, no mid-string truncation).
3. **Run a truncation scan** after any session that used the Edit tool:
```bash
python3 -c "
import glob
for f in glob.glob('src/**/*.tsx', recursive=True) + glob.glob('app/**/*.tsx', recursive=True):
    c = open(f).read().rstrip()
    if not c.endswith('}') and not c.endswith(';') and len(c) > 200:
        print(f'TRUNCATED: {f}')
"
```
4. Know the Edit tool failure modes:
   - Files can lose closing lines (truncation mid-content)
   - Files can lose trailing newlines
   - Files can be overwritten with empty/blank content
   - The problem is worst with large files and long sessions
5. `formatOnSave` in VS Code can interfere — consider disabling during AI editing sessions.
6. When in doubt about file integrity, restore from git and re-apply changes via Python.

## Incident history

- **2026-05-10**: `music-generator.json` had `"references": [...]` instead of `"items": [...]` — caused blank page on `/tools/music-generator`. Same bug found in `cli.json` and `image-generator.json` (both EN+ZH).
- **2026-05-10**: `ai-scheduling.json` (EN+ZH) had `"cases": [...]` instead of `"useCases": [...]` and `"questions": [...]` instead of `"items": [...]` for FAQ.
- **2026-05-10**: `ai-homework-helper.json` (ZH) had `"items": [...]` instead of `"useCases": [...]` in useCases block.
- **2026-05-10**: Four JSON files corrupted (truncated) by Edit tool: `interview-assistant.json`, `music-video-generator.json` (both EN+ZH). Restored from git.
- **2026-05-10**: Comprehensive language audit — found and fixed:
  - **GlossaryViewer.tsx hardcoded Chinese**: Footer text ("这个词汇表涵盖了...", "持续更新中") was hardcoded in the component, showing on all EN glossary pages (`/glossary/ai`, `/glossary/marketing`, `/glossary/seo`). Fixed by adding `bottomNoteText`/`bottomNoteBadge` props to GlossaryViewer, GlossaryPageContent, and all 6 glossary JSON i18n sections.
  - **Table.tsx usePathname() null safety**: `pathname.startsWith("/zh")` at line 99 could crash during SSR if `usePathname()` returned `null`. Added null guard: `(pathname || '').startsWith("/zh")`.
  - **12 ZH tools pages wrong OG locale values**:
    - 4 pages had `locale: 'en_US'` instead of `'zh_CN'`: headshot-generator, image-enhancer, productivity, image-relighting
    - 9 pages had `alternateLocale: 'zh_CN'` instead of `'en_US'`: code-review, directory, fashion, headshot-generator, image-enhancer, image-relighting, knowledge-base, productivity, spreadsheet, text-generator, user-research
    - 4 pages had `alternateLocale` as array `['en_US']` instead of string: fundraising, geo, interview-assistant, recruiting
  - **98+ SEO/marketing/insights/listing pages**: Missing `locale` and `alternateLocale` from `openGraph` metadata block. **Fixed 2026-05-10**: 96 page.tsx files updated with correct locale/alternateLocale values. All 368 page.tsx files now verified correct.
