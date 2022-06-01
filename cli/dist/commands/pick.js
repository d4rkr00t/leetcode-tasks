'use strict';

var path = require('path');
var fs = require('fs');
var child_process = require('child_process');
var consts = require('./consts-aea860c4.js');
var getTasks = require('./get-tasks-353b8748.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);
var fs__default = /*#__PURE__*/_interopDefaultLegacy(fs);

/**
 * Pick next task to solve.
 *
 * @usage {cliName} pick
 */
async function main() {
  const tasks = getTasks.getGroupedTasksList(path__default["default"].join(process.cwd(), consts.TASKS_DIR_NAME));
  const tasksFlat = getTasks.getTasksFlat(path__default["default"].join(process.cwd(), consts.TASKS_DIR_NAME));
  const solutionsDirPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_DIR_NAME);
  const solutions = fs__default["default"].readdirSync(solutionsDirPath);
  const solutionsCount = solutions.length;
  const totalTasksCount = Object.keys(tasks).reduce((acc, key) => {
    acc += tasks[key].length;
    return acc;
  }, 0);
  const breakdownPath = path__default["default"].join(process.cwd(), consts.BREAKDOWN_FILE_NAME);
  const breakdownData = require(breakdownPath);

  if (solutionsCount === totalTasksCount) {
    console.log("🎉 Everything is solved!");
    return;
  }

  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);

  if (
    solutionsData.active.tasks.length &&
    solutionsData.active.tasks[0].status === consts.TASK_STATUS_NEW
  ) {
    console.log(
      `⚠️ Task: ${path__default["default"].basename(
        tasksFlat[solutionsData.active.tasks[0].id]
      )} already in progress!`
    );
    return;
  }

  let attemptsCount = 20;
  let selected = false;

  while (attemptsCount) {
    attemptsCount -= 1;

    const category = pickCategory();
    const item =
      tasks[category][Math.floor(Math.random() * tasks[category].length)];

    const [id] = item.split("-");

    if (fs__default["default"].existsSync(path__default["default"].join(solutionsDirPath, item))) {
      continue;
    }
    if (breakdownData[id]) {
      continue;
    }

    solutionsData.active.tasks.unshift({
      id,
      status: consts.TASK_STATUS_NEW,
    });
    const fileSrc = path__default["default"].join(process.cwd(), consts.TASKS_DIR_NAME, category, item);
    const fileDest = path__default["default"].join(solutionsDirPath, item);
    fs__default["default"].copyFileSync(fileSrc, fileDest);
    fs__default["default"].writeFileSync(solutionsPath, JSON.stringify(solutionsData, null, 2));

    console.log("Next task: ", item);
    child_process.execSync(`code-insiders ${fileDest} -r`);
    selected = true;

    break;
  }

  if (attemptsCount === 0 && !selected) {
    console.log(
      `No task was selected. Check breakdown tasks list to unblock task selection.`
    );
  }
}

function pickCategory() {
  const rnd = Math.floor(Math.random() * (100 - 2)) + 1;
  if (rnd <= 30) {
    return "easy";
  } else if (rnd <= 60) {
    return "medium";
  } else {
    return "hard";
  }
}

module.exports = main;
