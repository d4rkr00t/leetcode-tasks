'use strict';

var fs = require('fs');
var path = require('path');
var consts = require('./consts-a90bc138.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var fs__default = /*#__PURE__*/_interopDefaultLegacy(fs);
var path__default = /*#__PURE__*/_interopDefaultLegacy(path);

function getGroupedTasksList(dir) {
  const tasks = {};
  for (let taskGroupName of consts.TASKS_GROUPS_NAMES) {
    const taskDir = path__default["default"].join(dir, taskGroupName);
    tasks[taskGroupName] = fs__default["default"].readdirSync(taskDir);
  }
  return tasks;
}

function getTasksFlat(dir) {
  let tasks = {};
  for (let taskGroupName of consts.TASKS_GROUPS_NAMES) {
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

exports.getGroupedTasksList = getGroupedTasksList;
exports.getTasksFlat = getTasksFlat;
