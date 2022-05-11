const fs = require("fs");
const path = require("path");
const solutionsFilePath = path.join(__dirname, "solutions.md");
const faildTaskPrefix = "❌ ";
const solvedTaskPrefix = "✅ ";
const newTaskPrefix = "✅❌ ";
const solutionsRawData = fs
  .readFileSync(solutionsFilePath, "utf-8")
  .split("Solved:");

const solutions = [];

const NEW_TASK = 0;
const SOLVED_TASK = 1;
const FAILD_TASK = 2;

for (let group of solutionsRawData) {
  let groupSolutions = { solved: 0, failed: 0, successRate: 0, tasks: [] };
  for (let line of group.split("\n")) {
    line = line.trim();
    if (
      !line ||
      line.startsWith(newTaskPrefix) ||
      (!line.startsWith(faildTaskPrefix) && !line.startsWith(solvedTaskPrefix))
    ) {
      continue;
    }
    const taskId = line
      .replace(faildTaskPrefix, "")
      .replace(solvedTaskPrefix, "")
      .trim();

    if (line.startsWith(faildTaskPrefix)) {
      groupSolutions.tasks.push({
        id: taskId,
        status: FAILD_TASK,
      });
      groupSolutions.failed += 1;
    } else {
      groupSolutions.tasks.push({
        id: taskId,
        status: SOLVED_TASK,
      });
      groupSolutions.solved += 1;
    }
  }
  groupSolutions.successRate =
    Math.round(
      (groupSolutions.solved /
        (groupSolutions.failed + groupSolutions.solved)) *
        100
    ) / 100;

  solutions.push(groupSolutions);
}

fs.writeFileSync(
  path.join(__dirname, "solutions.json"),
  JSON.stringify(
    {
      active: {
        solved: 0,
        failed: 0,
        successRate: 1,
        tasks: [],
      },
      archived: solutions,
    },
    null,
    2
  )
);

console.log(solutions);
