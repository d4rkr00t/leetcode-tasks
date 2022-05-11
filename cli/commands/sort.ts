import path from "path";
import fs from "fs";
import {
  SOLUTIONS_FILE_NAME,
  TASK_STATUS_FAILED,
  TASKS_DIR_NAME,
} from "../lib/consts";
import { getTasksFlat } from "../lib/get-tasks";

/**
 * Sort tasks by difficulty.
 *
 * @usage {cliName} sort
 */
export default async function main() {
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const taskToNumFails: Record<string, number> = {};

  for (let i = 0; i < Math.min(3, solutionsData.archived.length); i++) {
    const tasks = solutionsData.archived[i].tasks;
    for (let task of tasks) {
      if (task.status === TASK_STATUS_FAILED) {
        taskToNumFails[task.id] = (taskToNumFails[task.id] || 0) + 1;
      } else {
        taskToNumFails[task.id] = 0;
      }
    }
  }

  const groups: Record<string, Set<string>> = {
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

  const tasks = getTasksFlat(path.join(process.cwd(), TASKS_DIR_NAME));

  for (let group of Object.keys(groups)) {
    for (let taskId of groups[group]) {
      const outDirPath = path.join(process.cwd(), TASKS_DIR_NAME, group);
      const oldPath = tasks[taskId];
      if (!oldPath) {
        continue;
      }
      const taskFileName = path.basename(tasks[taskId]);
      const newPath = path.join(outDirPath, taskFileName);
      try {
        if (oldPath !== newPath) {
          fs.renameSync(oldPath, newPath);
          console.log(`Moved ${taskFileName} to ${group}`);
        }
      } catch {}
    }
  }
}
