import path from "path";
import fs from "fs";
import {
  SOLUTIONS_FILE_NAME,
  TASK_STATUS_NEW,
  TASK_STATUS_SOLVED,
} from "../lib/consts";

/**
 * Marks the most recent task as solved.
 *
 * @usage {cliName} solved
 */
export default async function main() {
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);

  if (
    solutionsData.active.tasks.length === 0 ||
    solutionsData.active.tasks[0].status !== TASK_STATUS_NEW
  ) {
    return;
  }

  solutionsData.active.tasks[0].status = TASK_STATUS_SOLVED;
  solutionsData.active.solved += 1;
  solutionsData.active.successRate =
    Math.round(
      (solutionsData.active.solved /
        (solutionsData.active.failed + solutionsData.active.solved)) *
        100
    ) / 100;

  fs.writeFileSync(solutionsPath, JSON.stringify(solutionsData, null, 2));

  console.log(`✅ Task: ${solutionsData.active.tasks[0].id} solved!`);
}
