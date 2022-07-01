import path from "path";
import {
  SOLUTIONS_FILE_NAME,
  TASK_STATUS_FAILED,
  TASK_STATUS_SOLVED,
} from "../lib/consts";

/**
 * Show success rate of previous solves.
 *
 * @usage {cliName} history
 * @usage {cliName} history <task_id>
 * @param {Array<string>} $inputs Any non-flag arguments are passed here
 */
export default async function main($inputs: number[]) {
  if ($inputs.length) {
    const [taskId] = $inputs;
    taskHistory(taskId);
    return;
  } else {
    console.log("Task id is required!");
  }
}

function taskHistory(taskId: number) {
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const history = [];

  for (let solve of solutionsData.archived) {
    let taskData = solve.tasks.find((t: any) => t.id === "" + taskId);
    if (taskData) {
      history.push(taskStatusToIcon(taskData.status));
    }
  }

  let taskData = solutionsData.active.tasks.find(
    (t: any) => t.id === "" + taskId
  );
  if (taskData) {
    history.push(taskStatusToIcon(taskData.status));
  }

  console.log(history.join(" "));
}

function taskStatusToIcon(status: number): string {
  if (status === TASK_STATUS_SOLVED) {
    return "✅";
  } else if (status === TASK_STATUS_FAILED) {
    return "❌";
  } else {
    return "🤷‍♂️";
  }
}
