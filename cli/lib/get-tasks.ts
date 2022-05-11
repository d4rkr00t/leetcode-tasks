import fs from "fs";
import path from "path";
import { TASKS_GROUPS_NAMES } from "./consts";

export function getGroupedTasksList(dir: string) {
  const tasks: Record<string, Array<string>> = {};
  for (let taskGroupName of TASKS_GROUPS_NAMES) {
    const taskDir = path.join(dir, taskGroupName);
    tasks[taskGroupName] = fs.readdirSync(taskDir);
  }
  return tasks;
}

export function getTasksFlat(dir: string) {
  let tasks: Record<string, string> = {};
  for (let taskGroupName of TASKS_GROUPS_NAMES) {
    const taskDir = path.join(dir, taskGroupName);
    tasks = { ...tasks, ...processTasksList(fs.readdirSync(taskDir), taskDir) };
  }
  return tasks;
}

function processTasksList(tasks: Array<string>, dir: string) {
  return tasks.reduce<Record<string, string>>((acc, task) => {
    const [id] = task.split("-");
    acc[id] = path.join(dir, task);
    return acc;
  }, {});
}
