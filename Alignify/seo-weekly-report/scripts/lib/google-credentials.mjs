/**
 * Shared Google service account credentials for GSC / GA4.
 *
 * Priority:
 *   1. GSC_CLIENT_EMAIL + GSC_PRIVATE_KEY (or GA4_*)
 *   2. GSC_KEY_FILE / GOOGLE_SERVICE_ACCOUNT_KEY_FILE / GOOGLE_INDEXING_KEY_FILE
 *   3. Legacy deploy paths: {ALIGNIFY_DEPLOY_ROOT}/config/gsc-key.json
 */

import { readFileSync, existsSync } from 'fs';
import { resolve, dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

function normalizePrivateKey(rawKey) {
  if (!rawKey) return rawKey;
  return rawKey.includes('\\n') ? rawKey.replace(/\\n/g, '\n') : rawKey;
}

function readKeyFile(keyFile) {
  const abs = resolve(keyFile);
  if (!existsSync(abs)) return null;
  const parsed = JSON.parse(readFileSync(abs, 'utf-8'));
  if (!parsed.client_email || !parsed.private_key) {
    throw new Error(`Invalid service account JSON (missing client_email/private_key): ${abs}`);
  }
  return {
    client_email: parsed.client_email,
    private_key: parsed.private_key,
  };
}

function legacyKeyPaths() {
  const paths = [];
  const deployRoot = process.env.ALIGNIFY_DEPLOY_ROOT;
  if (deployRoot) {
    paths.push(join(deployRoot, 'config', 'gsc-key.json'));
  }
  paths.push(
    'E:/自有部署项目/alignify production/config/gsc-key.json',
    join(__dirname, '..', '..', '..', 'config', 'gsc-key.json'),
  );
  return paths;
}

export function loadGoogleServiceAccountCredentials() {
  const email = process.env.GSC_CLIENT_EMAIL || process.env.GA4_CLIENT_EMAIL;
  const rawKey = process.env.GSC_PRIVATE_KEY || process.env.GA4_PRIVATE_KEY;
  if (email && rawKey) {
    return {
      client_email: email,
      private_key: normalizePrivateKey(rawKey),
    };
  }

  const keyFiles = [
    process.env.GSC_KEY_FILE,
    process.env.GOOGLE_SERVICE_ACCOUNT_KEY_FILE,
    process.env.GOOGLE_INDEXING_KEY_FILE,
    ...legacyKeyPaths(),
  ].filter(Boolean);

  for (const keyFile of keyFiles) {
    const creds = readKeyFile(keyFile);
    if (creds) return creds;
  }

  throw new Error(
    'Missing Google service account credentials. Set GSC_CLIENT_EMAIL + GSC_PRIVATE_KEY in scripts/.env, ' +
      'or set GSC_KEY_FILE / GOOGLE_SERVICE_ACCOUNT_KEY_FILE to a GCP JSON key file ' +
      '(same file as Indexing API / former config/gsc-key.json).'
  );
}
