// 对照 content/sections/section-tldr.md §2.2，扫描 content 下 tools/seo/marketing/insights 中 zh 与 en 的 JSON tldr 字数。
// 用法：node scripts/permanent/audit-tldr-length.mjs
//       node scripts/permanent/audit-tldr-length.mjs --json report.json
import fs from "fs";
import path from "path";

const jsonOut = process.argv.includes("--json")
  ? process.argv[process.argv.indexOf("--json") + 1]
  : null;

function walk(dir, acc = []) {
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) walk(p, acc);
    else if (name.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

function stripHtml(s) {
  return s
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z]+;/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function countZhChars(s) {
  return stripHtml(s).replace(/\s/g, "").length;
}

function countEnWords(s) {
  const t = stripHtml(s);
  if (!t) return 0;
  return t.split(/\s+/).filter(Boolean).length;
}

const roots = ["content/tools", "content/seo", "content/marketing", "content/insights"];
const files = roots.flatMap((r) => {
  const full = path.join(process.cwd(), r);
  return fs.existsSync(full) ? walk(full) : [];
});

const issues = [];

for (const file of files) {
  let j;
  try {
    j = JSON.parse(fs.readFileSync(file, "utf8"));
  } catch {
    continue;
  }
  if (!j.blocks) continue;
  const tldr = j.blocks.find((b) => b.type === "tldr");
  if (!tldr) continue;

  const isZh = file.includes(`${path.sep}zh${path.sep}`);
  const intro = tldr.introduction || "";
  const items = tldr.items || [];

  const introLen = isZh ? countZhChars(intro) : countEnWords(intro);
  const introLimit = isZh ? [40, 80] : [40, 70];

  const itemLens = items.map((it, i) => ({
    i,
    len: isZh ? countZhChars(it) : countEnWords(it),
  }));

  const problems = [];
  if (introLen < introLimit[0] || introLen > introLimit[1]) {
    problems.push(
      `intro ${introLen} (want ${introLimit[0]}-${introLimit[1]} ${isZh ? "chars" : "words"})`,
    );
  }
  // 与 content/sections/section-tldr.md §2.2「单条上限」一致：≤50 字 / ≤30 词（目标 25–40 / 18–28 不记为违规）
  const itemMax = isZh ? 50 : 30;
  for (const it of itemLens) {
    if (it.len > itemMax) problems.push(`item[${it.i}] ${it.len} (max ${itemMax})`);
  }
  if (items.length < 3 || items.length > 6) problems.push(`items count ${items.length} (want 3-6)`);

  if (problems.length) {
    issues.push({ file: path.relative(process.cwd(), file), problems });
  }
}

issues.sort((a, b) => b.problems.length - a.problems.length);

let tldrCount = 0;
for (const f of files) {
  try {
    const j = JSON.parse(fs.readFileSync(f, "utf8"));
    if (j.blocks?.some((b) => b.type === "tldr")) tldrCount++;
  } catch {
    /* skip */
  }
}

console.log("Total files with tldr:", tldrCount);
console.log("Files with violations:", issues.length);
for (const x of issues) {
  console.log("\n" + x.file);
  for (const p of x.problems) console.log("  - " + p);
}

if (jsonOut) {
  fs.writeFileSync(
    jsonOut,
    JSON.stringify({ tldrCount, violationCount: issues.length, issues }, null, 2),
    "utf8",
  );
  console.log("\nWrote JSON report:", jsonOut);
}
