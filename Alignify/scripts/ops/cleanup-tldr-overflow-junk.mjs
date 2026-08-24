/**
 * 移除 fix-tldr-compliance 在 section/html 前部误插入的双段「要点补充」碎片（… + 残句）。
 * 用法：node scripts/permanent/cleanup-tldr-overflow-junk.mjs
 */
import fs from "fs";
import path from "path";

function walk(dir, acc = []) {
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) walk(p, acc);
    else if (name.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

const junkDoubleRe =
  /<p class="text-base md:text-lg leading-relaxed"><strong>要点补充：<\/strong>[\s\S]*?<\/p><p class="text-base md:text-lg leading-relaxed"><strong>要点补充：<\/strong>[\s\S]*?<\/p>/g;

const junkSingleEllipsisRe =
  /<p class="text-base md:text-lg leading-relaxed"><strong>要点补充：<\/strong>(?:\s|…|\u2026|\.|<br\s*\/?>)*<\/p>\s*/g;

function cleanString(s) {
  if (typeof s !== "string" || !s.includes("要点补充：")) return s;
  let out = s.replace(junkDoubleRe, "");
  out = out.replace(junkSingleEllipsisRe, "");
  out = out.replace(
    /<p class="text-base md:text-lg leading-relaxed"><strong>要点补充：<\/strong>/g,
    '<p class="text-base md:text-lg leading-relaxed">',
  );
  return out.trim();
}

function walkValue(v) {
  if (typeof v === "string") return cleanString(v);
  if (Array.isArray(v)) return v.map(walkValue);
  if (v && typeof v === "object") {
    for (const k of Object.keys(v)) {
      v[k] = walkValue(v[k]);
    }
  }
  return v;
}

const roots = ["content/tools", "content/seo", "content/marketing", "content/insights"];
const files = roots.flatMap((r) => {
  const full = path.join(process.cwd(), r);
  return fs.existsSync(full) ? walk(full) : [];
});

let n = 0;
for (const f of files) {
  let data;
  try {
    data = JSON.parse(fs.readFileSync(f, "utf8"));
  } catch {
    continue;
  }
  const before = JSON.stringify(data);
  walkValue(data);
  const after = JSON.stringify(data);
  if (before !== after) {
    fs.writeFileSync(f, JSON.stringify(data, null, 2) + "\n", "utf8");
    n++;
  }
}
console.log("Cleaned files:", n);
