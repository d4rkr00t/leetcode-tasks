'use strict';

var path = require('path');
var consts = require('./consts-aea860c4.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);

/**
 * Show success rate of previous solves.
 *
 * @usage {cliName} history
 * @usage {cliName} history <task_id>
 * @param {Array<string>} $inputs Any non-flag arguments are passed here
 */
async function main($inputs) {
  if ($inputs.length) {
    const [taskId] = $inputs;
    taskHistory(taskId);
    return;
  }

  highLevelHistory();
}

function highLevelHistory() {
  const asciichart = require("asciichart");
  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const data = solutionsData.archived
    .reverse()
    .map((solve) => solve.successRate * 100);
  data.push(solutionsData.active.successRate * 100);

  console.log(asciichart.plot(data, { height: 20 }));
}

function taskHistory(taskId) {
  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const history = [];

  for (let solve of solutionsData.archived) {
    let taskData = solve.tasks.find((t) => t.id === "" + taskId);
    if (taskData) {
      history.push(taskData.status === consts.TASK_STATUS_SOLVED ? "✅" : "❌");
    }
  }

  let taskData = solutionsData.active.tasks.find(
    (t) => t.id === "" + taskId
  );
  if (taskData) {
    history.push(taskData.status === consts.TASK_STATUS_SOLVED ? "✅" : "❌");
  }

  console.log(history.join(" "));
}

module.exports = main;
