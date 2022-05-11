import path from "path";
import fs from "fs";
import {
  SOLUTIONS_FILE_NAME,
  TASK_STATUS_FAILED,
  TASK_STATUS_NEW,
} from "../lib/consts";

/**
 * Marks the most recent task as failed.
 *
 * @usage {cliName} failed
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

  solutionsData.active.tasks[0].status = TASK_STATUS_FAILED;
  solutionsData.active.failed += 1;
  solutionsData.active.successRate =
    Math.round(
      (solutionsData.active.solved /
        (solutionsData.active.failed + solutionsData.active.solved)) *
        100
    ) / 100;

  fs.writeFileSync(solutionsPath, JSON.stringify(solutionsData, null, 2));

  console.log(`❌ Tasks: ${solutionsData.active.tasks[0].id} is failed!`);
}
