import path from "path";
import { SOLUTIONS_FILE_NAME, TASKS_DIR_NAME } from "../lib/consts";
import { getTasksFlat } from "../lib/get-tasks";

/**
 * Showes the progress.
 *
 * @usage {cliName} progress
 */
export default async function main() {
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const attemptedCount =
    solutionsData.active.failed + solutionsData.active.solved;
  const totalTasksCount = Object.keys(
    getTasksFlat(path.join(process.cwd(), TASKS_DIR_NAME))
  ).length;

  console.log(
    `Solved/Failed:  ${solutionsData.active.solved}/${solutionsData.active.failed}`
  );
  console.log(`Success Rate:   ${solutionsData.active.successRate}`);

  console.log(
    `Progress:       ${attemptedCount}/${totalTasksCount} | ${(
      (attemptedCount / totalTasksCount) *
      100
    ).toFixed(0)}% | ${totalTasksCount - attemptedCount} tasks(s) left`
  );
  console.log();
  highLevelHistory();
}

function highLevelHistory() {
  const asciichart = require("asciichart");
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const data = solutionsData.archived
    .reverse()
    .map((solve: any) => solve.successRate * 100);
  data.push(solutionsData.active.successRate * 100);

  console.log(asciichart.plot(data, { height: 20 }));
}
