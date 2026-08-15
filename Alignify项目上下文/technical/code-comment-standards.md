# Code Comment Standards

All code comments must be in English. The only exception: native-language example strings within JSDoc that document API input/output formats.

## Exception: Format example strings in JSDoc

When a function's JSDoc documents a format that is inherently language-specific (Chinese date strings, Japanese text, etc.), the example string stays in its native language. These are API documentation, not code comments.

### Current instances (intentionally kept as-is)

| File | Line | Content | Why kept |
|---|---|---|---|
| `src/lib/utils.ts` | L28 | `@returns Format: YYYY年M月D日 (e.g. 2025年2月12日)` | Documents `getCurrentDateCN()` output format |
| `src/lib/utils.ts` | L40 | `@param dateStr - Chinese date string, format: YYYY年M月D日` | Documents `convertCNDateToISO()` input format |
| `src/lib/utils.ts` | L117 | `@param readTime - e.g. "8 分钟阅读", "20 min read"` | Documents `convertReadTimeToISO8601()` bilingual input |
| `src/components/References.tsx` | L27 | `Supports Chinese: "2026年1月15日" → ...` | Documents `parseDate()` supported date format |
| `src/components/References.tsx` | L37 | `Chinese date: "2026年1月15日" or "2026年"` | Labels Chinese date parsing branch |
| `src/components/References.tsx` | L58 | `Year-only: "2026" or "2026年"` | Labels year-only parsing branch |

## Audit checklist

When auditing comments for Chinese content, check whether the Chinese characters are:
1. Format example strings within JSDoc → **keep**
2. Inline comment text that could be English → **translate**
3. JSX structural markers → **delete** (redundant)
