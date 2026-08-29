/**
 * Resolve Nova Scientia deployment repo root from context scripts.
 * Override: NOVA_SCIENTIA_DEPLOY_ROOT=E:\自有部署项目\nova-scientia-main
 */
const path = require("path");

const CONTEXT_ROOT = path.resolve(__dirname, "..", "..");

function getDeployRoot() {
  if (process.env.NOVA_SCIENTIA_DEPLOY_ROOT) {
    return path.resolve(process.env.NOVA_SCIENTIA_DEPLOY_ROOT);
  }
  return path.resolve(CONTEXT_ROOT, "..", "..", "自有部署项目", "nova-scientia-main");
}

module.exports = { getDeployRoot, CONTEXT_ROOT };
