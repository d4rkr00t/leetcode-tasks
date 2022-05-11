'use strict';

var path = require('path');
var fs = require('fs');
var child_process = require('child_process');
var getTasks = require('./get-tasks-3b538152.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);
var fs__default = /*#__PURE__*/_interopDefaultLegacy(fs);

/**
 * Pick next task to solve.
 *
 * @usage {cliName} pick
 */
async function main() {
  const tasks = getTasks.getGroupedTasksList(path__default["default"].join(process.cwd(), getTasks.TASKS_DIR_NAME));
  const solutionsDirPath = path__default["default"].join(process.cwd(), getTasks.SOLUTIONS_DIR_NAME);
  const solutions = fs__default["default"].readdirSync(solutionsDirPath);
  const solutionsCount = solutions.length;
  const totalTasksCount = Object.keys(tasks).reduce((acc, key) => {
    acc += tasks[key].length;
    return acc;
  }, 0);

  if (solutionsCount === totalTasksCount) {
    console.log("🎉 Everything is solved!");
    return;
  }

  const solutionsPath = path__default["default"].join(process.cwd(), getTasks.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);

  while (true) {
    const category = pickCategory();
    const item =
      tasks[category][Math.floor(Math.random() * tasks[category].length)];

    if (fs__default["default"].existsSync(path__default["default"].join(solutionsDirPath, item))) {
      continue;
    }

    const [id] = item.split("-");
    solutionsData.active.tasks.unshift({
      id,
      status: getTasks.TAKS_STATUS_NEW,
    });
    const fileSrc = path__default["default"].join(process.cwd(), getTasks.TASKS_DIR_NAME, category, item);
    const fileDest = path__default["default"].join(solutionsDirPath, item);
    fs__default["default"].copyFileSync(fileSrc, fileDest);
    fs__default["default"].writeFileSync(solutionsPath, JSON.stringify(solutionsData, null, 2));

    console.log("Next task: ", item);
    child_process.execSync(`code-insiders ${fileDest} -r`);

    break;
  }
}

function pickCategory() {
  const rnd = Math.floor(Math.random() * (100 - 2)) + 1;
  if (rnd <= 25) {
    return "easy";
  } else if (rnd <= 50) {
    return "medium";
  } else if (rnd <= 75) {
    return "new";
  } else {
    return "hard";
  }
}

module.exports = main;
