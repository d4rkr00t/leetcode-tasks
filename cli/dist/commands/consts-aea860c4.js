'use strict';

const SOLUTIONS_DIR_NAME = "solutions";
const SOLUTIONS_FILE_NAME = "solutions.json";
const BREAKDOWN_FILE_NAME = "breakdown.json";

const TASK_STATUS_NEW = 0;
const TASK_STATUS_SOLVED = 1;
const TASK_STATUS_FAILED = 2;

const TASKS_DIR_NAME = "tasks";
const TASKS_GROUPS_NAMES = ["easy", "medium", "hard", "new"];

exports.BREAKDOWN_FILE_NAME = BREAKDOWN_FILE_NAME;
exports.SOLUTIONS_DIR_NAME = SOLUTIONS_DIR_NAME;
exports.SOLUTIONS_FILE_NAME = SOLUTIONS_FILE_NAME;
exports.TASKS_DIR_NAME = TASKS_DIR_NAME;
exports.TASKS_GROUPS_NAMES = TASKS_GROUPS_NAMES;
exports.TASK_STATUS_FAILED = TASK_STATUS_FAILED;
exports.TASK_STATUS_NEW = TASK_STATUS_NEW;
exports.TASK_STATUS_SOLVED = TASK_STATUS_SOLVED;