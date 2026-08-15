/**
 * 检查 EN Tools 页面 What Are / HowItWorks 内容合规性
 * 依据：content/sections/section-what-is.md、section-how-it-works.md
 * 防止：mid-word 截断、字数不足、内容缺失
 * 字数：±10% 容差可接受
 *
 * 运行：node scripts/permanent/check-tools-en-content.mjs 或 npm run check:tools-en
 */

import fs from "fs";
import path from "path";

const TOOLS_DIR = path.join(process.cwd(), "src/tools");

// 字数 ±10% 容差
const TECH_BASE_MIN = Math.floor(165 * 0.9); // 148
const TECH_BASE_MAX = Math.ceil(200 * 1.1); // 220
const ARCH_MIN = Math.floor(100 * 0.9); // 90
const ARCH_MAX = Math.ceil(135 * 1.1); // 149
const WHAT_ARE_MIN = Math.floor(220 * 0.9); // 198
const WHAT_ARE_MAX = Math.ceil(230 * 1.1); // 253

// 常见 mid-word 截断模式（禁止以这些结尾）
// 依据：section-how-it-works.md 禁止 mid-word 截断
const MID_WORD_TRUNCATION_PATTERNS = [
  /generatin$/i,
  /high-quali$/i,
  /generating natu$/i,
  /generating hig$/i,
  /, usin$/i,
  /, gen$/i,
  /compr$/i,
  /proces$/i,
  /analy$/i,
  /unders$/i,
  /cros$/i,
  /positiona$/i,
  /characteristic$/i,
  /, provid$/i,
  /, gener$/i,
  /autom$/i,
  /, an$/i,
  /intellig$/i,
  /object$/i,
  /, pro$/i,
  /, rec$/i,
  /, au$/i,
  /struc$/i,
  /into s$/i,
  /pronun$/i,
  /deep lea$/i,
];

function countChars(str) {
  if (!str || typeof str !== "string") return 0;
  return str.replace(/\s+/g, " ").trim().length;
}

function hasMidWordTruncation(str) {
  const trimmed = str.trim();
  for (const pattern of MID_WORD_TRUNCATION_PATTERNS) {
    if (pattern.test(trimmed)) return true;
  }
  return false;
}

function analyzeFile(filePath) {
  const content = fs.readFileSync(filePath, "utf-8");
  const basename = path.basename(filePath);
  const issues = [];

  const introIdx = content.indexOf('id="article-intro"');
  const whatAreIdx = content.indexOf('id="what-are-');
  const howItWorksIdx = content.indexOf("<HowItWorks");

  if (howItWorksIdx < 0) return { file: basename, issues };

  const rest = content.slice(howItWorksIdx);
  const techMatch = rest.match(
    /technologyBase="([^"]*)"\s*advantages/
  );
  const archMatch = rest.match(
    /architectureDifferences="([^"]*)"/
  );

  if (techMatch) {
    const tech = techMatch[1];
    const techLen = countChars(tech);
    if (hasMidWordTruncation(tech)) {
      issues.push(`[mid-word] technologyBase ends with truncated word`);
    }
    if (techLen < TECH_BASE_MIN) {
      issues.push(`[short] technologyBase ${techLen} chars (target 165-200, ±10% ${TECH_BASE_MIN}-${TECH_BASE_MAX})`);
    }
    if (techLen > TECH_BASE_MAX) {
      issues.push(`[long] technologyBase ${techLen} chars (target 165-200, ±10% ${TECH_BASE_MIN}-${TECH_BASE_MAX})`);
    }
  }

  if (archMatch) {
    const arch = archMatch[1];
    const archLen = countChars(arch);
    if (archLen < ARCH_MIN && archLen > 0) {
      issues.push(`[short] architectureDifferences ${archLen} chars (target 100-135, ±10% ${ARCH_MIN}-${ARCH_MAX})`);
    }
    if (archLen > ARCH_MAX) {
      issues.push(`[long] architectureDifferences ${archLen} chars (target 100-135, ±10% ${ARCH_MIN}-${ARCH_MAX})`);
    }
  }

  if (whatAreIdx >= 0) {
    const whatRest = content.slice(whatAreIdx);
    const pMatch = whatRest.match(/paragraphs=\{\[([\s\S]*?)\]\s*\}/);
    if (pMatch) {
      const inner = pMatch[1];
      const textMatch = inner.match(/"([^"]*)"(?:\s*,|\s*$)/);
      const firstPara = textMatch ? textMatch[1].trim() : "";
      const paraLen = countChars(firstPara);
      if (paraLen > 0 && paraLen < WHAT_ARE_MIN) {
        issues.push(`[short] What Are first para ${paraLen} chars (target 220-230, ±10% ${WHAT_ARE_MIN}-${WHAT_ARE_MAX})`);
      }
      if (paraLen > WHAT_ARE_MAX) {
        issues.push(`[long] What Are first para ${paraLen} chars (target 220-230, ±10% ${WHAT_ARE_MIN}-${WHAT_ARE_MAX})`);
      }
    }
  }

  return { file: basename, issues };
}

const files = fs
  .readdirSync(TOOLS_DIR)
  .filter((f) => f.endsWith("EN.mdx"));

const results = [];
for (const f of files) {
  try {
    const r = analyzeFile(path.join(TOOLS_DIR, f));
    if (r.issues && r.issues.length > 0) {
      results.push(r);
    }
  } catch (e) {
    results.push({ file: f, issues: [`Parse error: ${e.message}`] });
  }
}

if (results.length > 0) {
  console.error("\n❌ EN Tools content issues found:\n");
  results.forEach((r) => {
    console.error(`${r.file}:`);
    r.issues.forEach((i) => console.error(`  - ${i}`));
    console.error("");
  });
  process.exit(1);
} else {
  console.log("✓ All EN Tools content checks passed.");
  process.exit(0);
}
