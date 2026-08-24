/**
 * FAQ 答案长度审计：检测 answer 是否符合 40-60 词(EN)/70-100 字(ZH)
 * 依据：content/sections/section-faq.md
 *
 * 运行：node scripts/permanent/audit-faq-length.mjs
 */

import fs from "fs";
import path from "path";

const SRC_DIRS = [
  path.join(process.cwd(), "src/tools"),
  path.join(process.cwd(), "src/seo"),
  path.join(process.cwd(), "src/marketing"),
  path.join(process.cwd(), "src/insights"),
];

const ZH_MIN = 70;
const ZH_MAX = 100;
const EN_MIN = 40;
const EN_MAX = 60;

function countWords(str) {
  return str.trim().split(/\s+/).filter(Boolean).length;
}

function countChars(str) {
  return str.replace(/\s+/g, " ").trim().length;
}

function isChinese(str) {
  const cjk = (str.match(/[\u4e00-\u9fff]/g) || []).length;
  return cjk / str.length > 0.3;
}

function walkDir(dir, files = []) {
  if (!fs.existsSync(dir)) return files;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walkDir(full, files);
    else if (e.name.endsWith(".mdx")) files.push(full);
  }
  return files;
}

function extractFaqItems(content) {
  const items = [];
  const answerRe = /answer:\s*"((?:[^"\\]|\\.)*)"/g;
  const questionRe = /question:\s*"((?:[^"\\]|\\.)*)"/g;
  const faqStart = content.indexOf("<FAQ");
  if (faqStart < 0) return items;
  const faqEnd = content.indexOf("/>", faqStart);
  if (faqEnd < 0) return items;
  const faqBlock = content.slice(faqStart, faqEnd + 2);
  const questions = [...faqBlock.matchAll(questionRe)].map((m) => m[1]);
  const answers = [...faqBlock.matchAll(answerRe)].map((m) => m[1]);
  for (let i = 0; i < Math.min(questions.length, answers.length); i++) {
    items.push({ question: questions[i], answer: answers[i] });
  }
  return items;
}

const allFiles = SRC_DIRS.flatMap((d) => walkDir(d));
const results = [];

for (const filePath of allFiles) {
  const content = fs.readFileSync(filePath, "utf-8");
  const items = extractFaqItems(content);
  if (items.length === 0) continue;

  const relPath = filePath.replace(process.cwd(), "").replace(/\\/g, "/");
  const sampleAnswer = items[0].answer;
  const isZh = isChinese(sampleAnswer);

  for (let i = 0; i < items.length; i++) {
    const a = items[i].answer;
    const stripped = a.replace(/<[^>]*>/g, "").replace(/&nbsp;/g, " ").trim();
    const charCount = countChars(stripped);
    const wordCount = countWords(stripped);
    const zh = isChinese(a);
    let status = "ok";
    if (zh) {
      if (charCount < ZH_MIN) status = "short";
      else if (charCount > ZH_MAX) status = "long";
    } else {
      if (wordCount < EN_MIN) status = "short";
      else if (wordCount > EN_MAX) status = "long";
    }
    results.push({
      file: path.basename(filePath),
      path: relPath,
      index: i + 1,
      question: items[i].question.slice(0, 30) + "...",
      chars: charCount,
      words: wordCount,
      lang: zh ? "zh" : "en",
      status,
    });
  }
}

const short = results.filter((r) => r.status === "short");
const long = results.filter((r) => r.status === "long");
const ok = results.filter((r) => r.status === "ok");

console.log("=== FAQ Answer Length Audit ===\n");
console.log("Total FAQ answers:", results.length);
console.log("OK:", ok.length, "| Short:", short.length, "| Long:", long.length);
console.log("\nTarget: ZH 70-100 字, EN 40-60 词\n");

if (short.length > 0) {
  console.log("--- Short (需补充) ---");
  short.forEach((r) => {
    const val = r.lang === "zh" ? `${r.chars}字` : `${r.words}词`;
    console.log(`${r.path} #${r.index}: ${val} - ${r.question}`);
  });
}

if (long.length > 0) {
  console.log("\n--- Long (需精简) ---");
  long.forEach((r) => {
    const val = r.lang === "zh" ? `${r.chars}字` : `${r.words}词`;
    console.log(`${r.path} #${r.index}: ${val} - ${r.question}`);
  });
}

if (short.length === 0 && long.length === 0) {
  console.log("✓ All FAQ answers within target range.");
}
