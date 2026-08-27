/**
 * FAQ 答案长度审计：扫描 md 内 `## 常见问题 {#faq}` / `## FAQ {#faq}`
 * 依据：skills/create-article/rules/sections.md Part 2.2
 *
 * 用法（部署仓根目录）：
 *   node ../../clients/Alignify/scripts/ops/audit-faq-length.mjs
 */
import fs from "fs";
import path from "path";

const DEPLOY_CANDIDATES = [
  process.env.ALIGNIFY_DEPLOY_ROOT,
  process.cwd(),
  "E:/自有部署项目/alignify production",
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

const ZH_MIN = 60;
const ZH_MAX = 120;
const EN_MIN = 40;
const EN_MAX = 80;

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
  return s.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
}

function countWords(str) {
  return stripHtml(str).split(/\s+/).filter(Boolean).length;
}

function countChars(str) {
  return stripHtml(str).replace(/\s/g, "").length;
}

function isChinese(str) {
  const cjk = (str.match(/[\u4e00-\u9fff]/g) || []).length;
  return cjk / Math.max(stripHtml(str).length, 1) > 0.3;
}

const FAQ_HEADING = /^##\s+(常见问题|FAQ|Frequently Asked Questions)\s+\{#faq\}/m;

function extractFaqItems(text) {
  const m = text.match(FAQ_HEADING);
  if (!m || m.index === undefined) return [];
  const start = m.index + m[0].length;
  const rest = text.slice(start);
  const next = rest.search(/^##\s+/m);
  const body = next >= 0 ? rest.slice(0, next) : rest;
  const parts = body.split(/^###\s+/m).slice(1);
  return parts.map((chunk) => {
    const lines = chunk.split(/\r?\n/);
    const question = lines[0]?.replace(/\s*\{#faq-\d+\}\s*$/, "").trim() || "";
    const answer = lines.slice(1).join("\n").trim();
    return { question, answer };
  });
}

const roots = ["content/tools", "content/seo", "content/blog", "content/marketing", "content/insights"];
const files = roots.flatMap((r) => walk(path.join(deployRoot, r)));

const results = [];

for (const filePath of files) {
  const content = fs.readFileSync(filePath, "utf8");
  const items = extractFaqItems(content);
  if (items.length === 0) continue;

  const relPath = path.relative(deployRoot, filePath).replace(/\\/g, "/");

  for (let i = 0; i < items.length; i++) {
    const a = items[i].answer;
    if (!a) continue;
    const stripped = stripHtml(a);
    const charCount = countChars(stripped);
    const wordCount = countWords(stripped);
    const zh = isChinese(stripped);
    let status = "ok";
    if (zh) {
      if (charCount < ZH_MIN) status = "short";
      else if (charCount > ZH_MAX) status = "long";
    } else {
      if (wordCount < EN_MIN) status = "short";
      else if (wordCount > EN_MAX) status = "long";
    }
    if (/\]\(|<a\s/i.test(a)) status = "has-link";
    results.push({
      path: relPath,
      index: i + 1,
      question: items[i].question.slice(0, 40),
      chars: charCount,
      words: wordCount,
      lang: zh ? "zh" : "en",
      status,
    });
  }
}

const short = results.filter((r) => r.status === "short");
const long = results.filter((r) => r.status === "long");
const links = results.filter((r) => r.status === "has-link");
const ok = results.filter((r) => r.status === "ok");

console.log("=== FAQ Answer Length Audit (inline md) ===\n");
console.log("Deploy:", deployRoot);
console.log("Total FAQ answers:", results.length);
console.log("OK:", ok.length, "| Short:", short.length, "| Long:", long.length, "| Has link:", links.length);
console.log("\nTarget: ZH 60-120 字, EN 40-80 词, no internal links\n");

for (const group of [
  ["Short", short],
  ["Long", long],
  ["Has link (P0 violation)", links],
]) {
  if (group[1].length === 0) continue;
  console.log(`--- ${group[0]} ---`);
  group[1].slice(0, 30).forEach((r) => {
    const val = r.lang === "zh" ? `${r.chars}字` : `${r.words}词`;
    console.log(`${r.path} #${r.index}: ${val} - ${r.question}`);
  });
}

process.exit(short.length + long.length + links.length ? 1 : 0);
