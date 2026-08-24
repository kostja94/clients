/**
 * Resolve Nova Scientia deployment repo root from context scripts.
 * Override: NOVA_SCIENTIA_DEPLOY_ROOT=D:\部署项目\nova-scientia
 */
const path = require("path");

const CONTEXT_ROOT = path.resolve(__dirname, "..", "..");

function getDeployRoot() {
  if (process.env.NOVA_SCIENTIA_DEPLOY_ROOT) {
    return path.resolve(process.env.NOVA_SCIENTIA_DEPLOY_ROOT);
  }
  return path.resolve(CONTEXT_ROOT, "..", "..", "部署项目", "nova-scientia");
}

module.exports = { getDeployRoot, CONTEXT_ROOT };
