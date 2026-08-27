/**
 * Landing page path normalization and classification (rules from YAML)
 */

import { readFileSync, existsSync } from 'fs';
import { parse as parseYaml } from 'yaml';
import { configPath } from './config.mjs';

let cachedRules = null;

export function getRules() {
  if (cachedRules) return cachedRules;
  const path = configPath('landing-page-rules.yaml');
  if (!existsSync(path)) {
    cachedRules = { rules: [], defaultType: 'other' };
  } else {
    cachedRules = parseYaml(readFileSync(path, 'utf8'));
  }
  return cachedRules;
}

export function normalizePath(raw) {
  if (!raw || raw === '(not set)') return '';
  let p = raw.split('?')[0].trim();
  if (!p.startsWith('/')) p = `/${p}`;
  p = p.replace(/\/+$/, '') || '/';
  return p;
}

export function stripDomain(url) {
  if (!url) return '';
  try {
    if (url.startsWith('http')) {
      return normalizePath(new URL(url).pathname);
    }
  } catch {
    /* fall through */
  }
  return normalizePath(url);
}

function matchRule(path, rule) {
  if (rule.exact !== undefined && path === rule.exact) return true;
  if (rule.prefix && path.startsWith(rule.prefix)) return true;
  if (rule.prefixes) {
    for (const p of rule.prefixes) {
      if (path === p || path.startsWith(`${p}/`)) return true;
    }
  }
  return false;
}

export function classifyLandingPage(rawPath) {
  const path = normalizePath(rawPath);
  if (!path) return { path: '', pageType: 'other' };

  const { rules = [], defaultType = 'other' } = getRules();
  for (const rule of rules) {
    if (matchRule(path, rule)) return { path, pageType: rule.type };
  }
  return { path, pageType: defaultType };
}
