'use strict';

var path = require('path');
var consts = require('./consts-dcdb998c.js');
var getTasks = require('./get-tasks-3cb42620.js');
require('fs');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);

/**
 * Showes the progress.
 *
 * @usage {cliName} progress
 */
async function main() {
  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const attemptedCount =
    solutionsData.active.failed + solutionsData.active.solved;
  const totalTasksCount = Object.keys(
    getTasks.getTasksFlat(path__default["default"].join(process.cwd(), consts.TASKS_DIR_NAME))
  ).length;

  console.log(
    `Solved/Failed:  ${solutionsData.active.solved}/${solutionsData.active.failed}`
  );
  console.log(`Success Rate:   ${solutionsData.active.successRate}`);

  console.log(
    `Progress:       ${attemptedCount}/${totalTasksCount} | ${(
      (attemptedCount / totalTasksCount) *
      100
    ).toFixed(0)}% | ${totalTasksCount - attemptedCount} tasks(s) left`
  );
}

module.exports = main;
