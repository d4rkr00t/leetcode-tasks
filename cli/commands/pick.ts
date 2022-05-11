import path from "path";
import fs from "fs";
import { execSync } from "child_process";

import {
  SOLUTIONS_DIR_NAME,
  SOLUTIONS_FILE_NAME,
  TAKS_STATUS_NEW,
  TASKS_DIR_NAME,
} from "../lib/consts";
import { getGroupedTasksList } from "../lib/get-tasks";

/**
 * Pick next task to solve.
 *
 * @usage {cliName} pick
 */
export default async function main() {
  const tasks = getGroupedTasksList(path.join(process.cwd(), TASKS_DIR_NAME));
  const solutionsDirPath = path.join(process.cwd(), SOLUTIONS_DIR_NAME);
  const solutions = fs.readdirSync(solutionsDirPath);
  const solutionsCount = solutions.length;
  const totalTasksCount = Object.keys(tasks).reduce<number>((acc, key) => {
    acc += tasks[key].length;
    return acc;
  }, 0);

  if (solutionsCount === totalTasksCount) {
    console.log("🎉 Everything is solved!");
    return;
  }

  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);

  while (true) {
    const category = pickCategory();
    const item =
      tasks[category][Math.floor(Math.random() * tasks[category].length)];

    if (fs.existsSync(path.join(solutionsDirPath, item))) {
      continue;
    }

    const [id] = item.split("-");
    solutionsData.active.tasks.unshift({
      id,
      status: TAKS_STATUS_NEW,
    });
    const fileSrc = path.join(process.cwd(), TASKS_DIR_NAME, category, item);
    const fileDest = path.join(solutionsDirPath, item);
    fs.copyFileSync(fileSrc, fileDest);
    fs.writeFileSync(solutionsPath, JSON.stringify(solutionsData, null, 2));

    console.log("Next task: ", item);
    execSync(`code-insiders ${fileDest} -r`);

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
