/**
 * Load project-config.yaml from package root config/
 */

import { readFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { parse as parseYaml } from 'yaml';

const __dirname = dirname(fileURLToPath(import.meta.url));
export const PACKAGE_ROOT = join(__dirname, '..', '..');

export function loadProjectConfig() {
  const path = join(PACKAGE_ROOT, 'config', 'project-config.yaml');
  if (!existsSync(path)) {
    return {
      project: { id: 'default', displayName: 'Site', siteUrl: process.env.GSC_SITE_URL || '' },
      health: { gscWeeklyClicksMin: 0, gscWeeklyClicksMax: 500000, pageOverlapRateWarnBelow: 0.2 },
      conversionEvents: [],
      paths: {},
    };
  }
  return parseYaml(readFileSync(path, 'utf8'));
}

export function configPath(name) {
  return join(PACKAGE_ROOT, 'config', name);
}
