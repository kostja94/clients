/**
 * TL;DR 字数审计：扫描 md 内 `## 核心要点 {#article-intro}` / `## Key Takeaways {#article-intro}`
 * 依据：skills/create-article/rules/sections/tldr.md §2.2
 *
 * 用法（部署仓根目录）：
 *   node ../../clients/Alignify/scripts/ops/audit-tldr-length.mjs
 *   node ../../clients/Alignify/scripts/ops/audit-tldr-length.mjs --json report.json
 *
 * 环境：ALIGNIFY_DEPLOY_ROOT 或自动探测常见路径
 */
import fs from "fs";
import path from "path";

const jsonOut = process.argv.includes("--json")
  ? process.argv[process.argv.indexOf("--json") + 1]
  : null;

const DEPLOY_CANDIDATES = [
  process.env.ALIGNIFY_DEPLOY_ROOT,
  path.join(process.cwd()),
  "E:/自有部署项目/alignify production",
  path.resolve(process.cwd(), "../../部署项目/alignify-by-kostja"),
].filter(Boolean);

function findDeployRoot() {
  for (const root of DEPLOY_CANDIDATES) {
    const full = path.resolve(root);
    if (fs.existsSync(path.join(full, "content"))) return full;
  }
  console.error("Deploy repo not found. Set ALIGNIFY_DEPLOY_ROOT.");
  process.exit(1);
}

const deployRoot = findDeployRoot();

function walk(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) walk(p, acc);
    else if (name.name.endsWith(".md")) acc.push(p);
  }
  return acc;
}

function stripHtml(s) {
  return s
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z]+;/gi, " ")
    .replace(/\*\*/g, "")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
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

const TLDR_HEADING =
  /^##\s+(核心要点|Key Takeaways)\s+\{#article-intro\}/m;

function extractTldrSection(text) {
  const m = text.match(TLDR_HEADING);
  if (!m || m.index === undefined) return null;
  const start = m.index + m[0].length;
  const rest = text.slice(start);
  const next = rest.search(/^##\s+/m);
  const body = next >= 0 ? rest.slice(0, next) : rest;
  const lines = body.split(/\r?\n/).map((l) => l.trim());
  const bullets = [];
  const introLines = [];
  for (const line of lines) {
    if (!line || line.startsWith("<!--")) continue;
    const bullet = line.match(/^[-*]\s+(.+)/);
    if (bullet) bullets.push(bullet[1]);
    else if (!line.startsWith("#")) introLines.push(line);
  }
  return {
    introduction: introLines.join(" "),
    items: bullets,
  };
}

const roots = ["content/tools", "content/seo", "content/blog", "content/marketing", "content/insights"];
const files = roots.flatMap((r) => walk(path.join(deployRoot, r)));

const issues = [];

for (const file of files) {
  const text = fs.readFileSync(file, "utf8");
  const tldr = extractTldrSection(text);
  if (!tldr) continue;

  const isZh = file.includes(`${path.sep}zh${path.sep}`) || /\\zh\\/.test(file);
  const intro = tldr.introduction || "";
  const items = tldr.items || [];

  const introLen = isZh ? countZhChars(intro) : countEnWords(intro);
  const introLimit = isZh ? [30, 100] : [25, 70];

  const problems = [];
  if (introLen < introLimit[0] || introLen > introLimit[1]) {
    problems.push(
      `intro ${introLen} (want ${introLimit[0]}-${introLimit[1]} ${isZh ? "chars" : "words"})`,
    );
  }
  const itemMax = isZh ? 80 : 40;
  items.forEach((it, i) => {
    const len = isZh ? countZhChars(it) : countEnWords(it);
    if (len > itemMax) problems.push(`item[${i}] ${len} (max ${itemMax})`);
  });
  if (items.length < 3 || items.length > 6) {
    problems.push(`items count ${items.length} (want 3-6)`);
  }

  if (problems.length) {
    issues.push({ file: path.relative(deployRoot, file), problems });
  }
}

console.log(`Scanned ${files.length} md files under ${deployRoot}`);
console.log(`TL;DR sections found with issues: ${issues.length}\n`);
for (const row of issues.slice(0, 50)) {
  console.log(row.file);
  row.problems.forEach((p) => console.log(`  - ${p}`));
}
if (issues.length > 50) console.log(`... and ${issues.length - 50} more`);

if (jsonOut) {
  fs.writeFileSync(jsonOut, JSON.stringify({ issues }, null, 2), "utf8");
}

process.exit(issues.length ? 1 : 0);
