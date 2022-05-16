import path from "path";
import { SOLUTIONS_FILE_NAME, TASK_STATUS_SOLVED } from "../lib/consts";

/**
 * Show success rate of previous solves.
 *
 * @usage {cliName} history
 * @usage {cliName} history <task_id>
 * @param {Array<number>} $inputs Any non-flag arguments are passed here
 */
export default async function main($inputs: number[]) {
  if ($inputs.length) {
    const [taskId] = $inputs;
    taskHistory(taskId);
    return;
  }

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

function taskHistory(taskId: number) {
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const history = [];

  for (let solve of solutionsData.archived) {
    let taskData = solve.tasks.find((t: any) => t.id === "" + taskId);
    if (taskData) {
      history.push(taskData.status === TASK_STATUS_SOLVED ? "✅" : "❌");
    }
  }

  let taskData = solutionsData.active.tasks.find(
    (t: any) => t.id === "" + taskId
  );
  if (taskData) {
    history.push(taskData.status === TASK_STATUS_SOLVED ? "✅" : "❌");
  }

  console.log(history.join(" "));
}
