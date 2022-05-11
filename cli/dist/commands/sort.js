'use strict';

var path = require('path');
var fs = require('fs');
var consts = require('./consts-dcdb998c.js');
var getTasks = require('./get-tasks-3cb42620.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);
var fs__default = /*#__PURE__*/_interopDefaultLegacy(fs);

/**
 * Sort tasks by difficulty.
 *
 * @usage {cliName} sort
 */
async function main() {
  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const taskToNumFails = {};

  for (let i = 0; i < Math.min(3, solutionsData.archived.length); i++) {
    const tasks = solutionsData.archived[i].tasks;
    for (let task of tasks) {
      if (task.status === consts.TASK_STATUS_FAILED) {
        taskToNumFails[task.id] = (taskToNumFails[task.id] || 0) + 1;
      } else {
        taskToNumFails[task.id] = 0;
      }
    }
  }

  const groups = {
    easy: new Set(),
    medium: new Set(),
    hard: new Set(),
    new: new Set(),
  };

  for (let [tid, fails] of Object.entries(taskToNumFails)) {
    if (fails === 0) {
      groups.easy.add(tid);
    } else if (fails < 3) {
      groups.medium.add(tid);
    } else {
      groups.hard.add(tid);
    }
  }

  const tasks = getTasks.getTasksFlat(path__default["default"].join(process.cwd(), consts.TASKS_DIR_NAME));

  for (let group of Object.keys(groups)) {
    for (let taskId of groups[group]) {
      const outDirPath = path__default["default"].join(process.cwd(), consts.TASKS_DIR_NAME, group);
      const oldPath = tasks[taskId];
      if (!oldPath) {
        continue;
      }
      const taskFileName = path__default["default"].basename(tasks[taskId]);
      const newPath = path__default["default"].join(outDirPath, taskFileName);
      try {
        if (oldPath !== newPath) {
          fs__default["default"].renameSync(oldPath, newPath);
          console.log(`Moved ${taskFileName} to ${group}`);
        }
      } catch (e) {}
    }
  }
}

module.exports = main;
