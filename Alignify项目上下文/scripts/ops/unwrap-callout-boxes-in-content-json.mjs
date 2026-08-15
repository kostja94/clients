/**
 * 去掉 content 目录下各 JSON 中 HTML 字符串里的彩色「左边条」callout 与红绿对比卡片外层 div，
 * 保留内层段落/列表；表格行 bg-primary/5 高亮改为默认行。
 * 运行：node scripts/permanent/unwrap-callout-boxes-in-content-json.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..", "..");
const contentDir = path.join(root, "content");

function collectJsonFiles(dir, out = []) {
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) collectJsonFiles(p, out);
    else if (name.name.endsWith(".json")) out.push(p);
  }
  return out;
}

function findNextDivOpen(html, start) {
  const i = html.indexOf("<div", start);
  if (i === -1) return null;
  const gt = html.indexOf(">", i);
  if (gt === -1) return null;
  const tag = html.slice(i, gt + 1);
  const cm = tag.match(/\bclass="([^"]*)"/);
  const classVal = cm ? cm[1] : "";
  const selfClosing = /\/\s*>$/.test(tag);
  return { i, tagEnd: gt + 1, classVal, selfClosing };
}

function isCalloutClass(c) {
  if (!c) return false;
  if (
    c.includes("border-l-4") &&
    (c.includes("border-accent") || c.includes("border-secondary"))
  ) {
    return true;
  }
  if (c.includes("border-l-4")) {
    if (c.includes("bg-primary/5")) return true;
    if (c.includes("bg-yellow-50")) return true;
    if (c.includes("bg-amber-50")) return true;
    if (c.includes("bg-red-50")) return true;
    if (c.includes("bg-green-50")) return true;
  }
  if (c.includes("bg-red-50") && c.includes("border-red-200")) return true;
  if (c.includes("bg-green-50") && c.includes("border-green-200")) return true;
  return false;
}

function unwrapAllCallouts(html) {
  let guard = 0;
  while (guard++ < 5000) {
    let changed = false;
    let pos = 0;
    while (pos < html.length) {
      const d = findNextDivOpen(html, pos);
      if (!d) break;
      if (d.selfClosing || !isCalloutClass(d.classVal)) {
        pos = d.i + 1;
        continue;
      }
      const innerStart = d.tagEnd;
      let depth = 1;
      let j = innerStart;
      while (j < html.length && depth > 0) {
        const nextDiv = html.indexOf("<div", j);
        const nextClose = html.indexOf("</div>", j);
        if (nextClose === -1) return html;
        if (nextDiv !== -1 && nextDiv < nextClose) {
          const gt = html.indexOf(">", nextDiv);
          if (gt === -1) return html;
          const openTag = html.slice(nextDiv, gt + 1);
          if (/\/\s*>$/.test(openTag)) {
            j = gt + 1;
            continue;
          }
          depth++;
          j = gt + 1;
        } else {
          depth--;
          if (depth === 0) {
            const inner = html.slice(innerStart, nextClose);
            html = html.slice(0, d.i) + inner + html.slice(nextClose + 6);
            changed = true;
            pos = d.i + inner.length;
            break;
          }
          j = nextClose + 6;
        }
      }
      if (!changed) pos = d.i + 1;
    }
    if (!changed) break;
  }
  return html;
}

function stripTableRowHighlight(html) {
  return html.replace(/<tr class="bg-primary\/5">/g, "<tr>");
}

function normalizeBlockClassName(c) {
  if (!c) return c;
  if (/bg-primary\/5/.test(c) && /border-l-4/.test(c)) return "";
  if (/bg-yellow-50/.test(c) && /border-l-4/.test(c)) return "";
  return c;
}

function shouldProcessHtmlString(s) {
  if (!s.includes("<div") && !s.includes("<tr")) return false;
  return (
    s.includes("border-l-4") ||
    s.includes("bg-primary/5") ||
    s.includes("bg-yellow-50") ||
    s.includes("bg-amber-50") ||
    (s.includes("bg-red-50") && (s.includes("border-red") || s.includes("border-l-4"))) ||
    (s.includes("bg-green-50") && (s.includes("border-green") || s.includes("border-l-4")))
  );
}

function walkAndTransform(obj) {
  if (Array.isArray(obj)) {
    obj.forEach(walkAndTransform);
    return;
  }
  if (!obj || typeof obj !== "object") return;
  for (const k of Object.keys(obj)) {
    if (k === "className" && typeof obj[k] === "string") {
      obj[k] = normalizeBlockClassName(obj[k]);
      continue;
    }
    if (typeof obj[k] === "string") {
      const s = obj[k];
      if (shouldProcessHtmlString(s)) {
        obj[k] = stripTableRowHighlight(unwrapAllCallouts(s));
      } else if (s.includes("bg-primary/5") && s.includes("<tr")) {
        obj[k] = stripTableRowHighlight(s);
      }
      continue;
    }
    walkAndTransform(obj[k]);
  }
}

function main() {
  const files = collectJsonFiles(contentDir);
  let nChanged = 0;
  for (const file of files) {
    const raw = fs.readFileSync(file, "utf8");
    let doc;
    try {
      doc = JSON.parse(raw);
    } catch (e) {
      console.error("Invalid JSON:", file, e.message);
      process.exit(1);
    }
    const before = JSON.stringify(doc);
    walkAndTransform(doc);
    const after = JSON.stringify(doc);
    if (before !== after) {
      fs.writeFileSync(file, `${JSON.stringify(doc, null, 2)}\n`, "utf8");
      nChanged++;
      console.log("updated", path.relative(root, file));
    }
  }
  console.log(`Done. ${nChanged} file(s) modified.`);
}

main();
