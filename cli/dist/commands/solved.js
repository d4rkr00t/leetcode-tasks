'use strict';

var path = require('path');
var fs = require('fs');
var consts = require('./consts-dcdb998c.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);
var fs__default = /*#__PURE__*/_interopDefaultLegacy(fs);

/**
 * Marks the most recent task as solved.
 *
 * @usage {cliName} solved
 */
async function main() {
  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);

  if (
    solutionsData.active.tasks.length === 0 ||
    solutionsData.active.tasks[0].status !== consts.TASK_STATUS_NEW
  ) {
    return;
  }

  solutionsData.active.tasks[0].status = consts.TASK_STATUS_SOLVED;
  solutionsData.active.solved += 1;
  solutionsData.active.successRate =
    Math.round(
      (solutionsData.active.solved /
        (solutionsData.active.failed + solutionsData.active.solved)) *
        100
    ) / 100;

  fs__default["default"].writeFileSync(solutionsPath, JSON.stringify(solutionsData, null, 2));

  console.log(`✅ Task: ${solutionsData.active.tasks[0].id} solved!`);
}

module.exports = main;
