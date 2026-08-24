/**
 * 压缩 content 目录下各 JSON 中 HTML 片段的多余换行与缩进，减少纯文本抽取时的断行/缺空格问题。
 * 跳过含 pre、script 标签的字符串（整段不处理，以免破坏代码块）。
 * 仅处理同时含 "<" 与换行的字符串，不合并无 HTML 的纯文本字段。
 *
 * 运行: npx tsx scripts/permanent/normalize-content-html-whitespace.mts
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "../..");

function shouldSkipHtmlString(s: string): boolean {
  return /<pre\s|<script\b/i.test(s);
}

function normalizeHtmlWhitespace(s: string): string {
  if (!s.includes("\n") || !s.includes("<")) return s;
  if (shouldSkipHtmlString(s)) return s;

  let t = s;
  t = t.replace(/<\/a>\s*\r?\n\s*([\u3002\uff0c\uff0e.,。．;:])/g, "</a>$1");
  t = t.replace(/<\/a>\s*\r?\n\s*(or|and|或)(?=\s|<)/gi, "</a> $1");
  t = t.replace(/>\s*\r?\n\s*</g, "><");

  t = t.replace(
    /<(p|div|li|td|th|h[1-6]|span|strong|em|section|ul|ol|blockquote)(\s[^>]*)?>\s*\r?\n\s+/gi,
    "<$1$2>",
  );
  t = t.replace(
    /\s*\r?\n\s*<\/(p|div|li|td|th|h[1-6]|span|strong|em|section|ul|ol|blockquote)>/gi,
    "</$1>",
  );

  t = t.replace(/\r?\n[\s\u00a0]*/g, " ");
  t = t.replace(/[\s\u00a0]{2,}/g, " ");
  return t.trim();
}

function deepNormalizeStrings(obj: unknown): { out: unknown; changed: number } {
  let changed = 0;

  const walk = (x: unknown): unknown => {
    if (typeof x === "string") {
      if (!x.includes("\n") || !x.includes("<")) return x;
      const next = normalizeHtmlWhitespace(x);
      if (next !== x) changed++;
      return next;
    }
    if (Array.isArray(x)) return x.map(walk);
    if (x && typeof x === "object") {
      const o = x as Record<string, unknown>;
      const out: Record<string, unknown> = {};
      for (const k of Object.keys(o)) {
        out[k] = walk(o[k]);
      }
      return out;
    }
    return x;
  };

  return { out: walk(obj), changed };
}

function walkContentJson(callback: (absPath: string) => void): void {
  const base = path.join(ROOT, "content");
  for (const area of ["tools", "seo", "marketing"] as const) {
    for (const locale of ["en", "zh"] as const) {
      const dir = path.join(base, area, locale);
      if (!fs.existsSync(dir)) continue;
      for (const name of fs.readdirSync(dir)) {
        if (!name.endsWith(".json")) continue;
        callback(path.join(dir, name));
      }
    }
  }
}

function main(): void {
  let filesTouched = 0;
  let stringsNormalized = 0;

  walkContentJson((absPath) => {
    const raw = fs.readFileSync(absPath, "utf8");
    let doc: unknown;
    try {
      doc = JSON.parse(raw);
    } catch {
      console.error("JSON parse error:", absPath);
      return;
    }
    const { out, changed } = deepNormalizeStrings(doc);
    if (changed === 0) return;
    stringsNormalized += changed;
    filesTouched++;
    fs.writeFileSync(absPath, JSON.stringify(out, null, 2) + "\n", "utf8");
  });

  console.log("Files updated:", filesTouched);
  console.log("Strings normalized (count of changed string nodes):", stringsNormalized);
}

main();
