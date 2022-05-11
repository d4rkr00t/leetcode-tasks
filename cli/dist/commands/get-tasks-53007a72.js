'use strict';

var fs = require('fs');
var path = require('path');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var fs__default = /*#__PURE__*/_interopDefaultLegacy(fs);
var path__default = /*#__PURE__*/_interopDefaultLegacy(path);

const SOLUTIONS_FILE_NAME = "solutions.json";
const TAKS_STATUS_FAILED = 2;

const TASKS_DIR_NAME = "tasks";
const TASKS_GROUPS_NAMES = ["easy", "medium", "hard", "new"];

function getTasks(dir) {
  const tasks = {};
  for (let taskGroupName of TASKS_GROUPS_NAMES) {
    const taskDir = path__default["default"].join(dir, taskGroupName);
    tasks[taskGroupName] = processTasksList(fs__default["default"].readdirSync(taskDir), taskDir);
  }
  return tasks;
}

function getTasksFlat(dir) {
  let tasks = {};
  for (let taskGroupName of TASKS_GROUPS_NAMES) {
    const taskDir = path__default["default"].join(dir, taskGroupName);
    tasks = { ...tasks, ...processTasksList(fs__default["default"].readdirSync(taskDir), taskDir) };
  }
  return tasks;
}

function processTasksList(tasks, dir) {
  return tasks.reduce((acc, task) => {
    const [id] = task.split("-");
    acc[id] = path__default["default"].join(dir, task);
    return acc;
  }, {});
}

exports.SOLUTIONS_FILE_NAME = SOLUTIONS_FILE_NAME;
exports.TAKS_STATUS_FAILED = TAKS_STATUS_FAILED;
exports.TASKS_DIR_NAME = TASKS_DIR_NAME;
exports.getTasks = getTasks;
exports.getTasksFlat = getTasksFlat;
