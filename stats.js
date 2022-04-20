const fs = require("fs");
const path = require("path");
const tagsData = require("./tags.json");
const solutionsFilePath = path.join(__dirname, "solutions.md");
const solutionsRawData = fs.readFileSync(solutionsFilePath, "utf-8");
const faildTaskPrefix = "❌ ";
const solvedTaskPrefix = "✅ ";
const newTaskPrefix = "✅❌ ";
const taskToNumFails = {};

for (let line of solutionsRawData.split("\n")) {
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

  if (!taskToNumFails[taskId]) {
    taskToNumFails[taskId] = 0;
  }

  if (line.startsWith(faildTaskPrefix)) {
    taskToNumFails[taskId] += 1;
  }
}

const groups = {
  easy: [],
  medium: [],
  hard: [],
};

const tags = {};

for (let [tid, fails] of Object.entries(taskToNumFails)) {
  if (fails === 0) {
    groups.easy.push(tid);
  } else if (fails < 3) {
    groups.medium.push(tid);
  } else {
    groups.hard.push(tid);
  }
  if (fails > 0) {
    for (let tag of tagsData[tid] || []) {
      tags[tag] = (tags[tag] || 0) + fails;
    }
  }
}

console.log(JSON.stringify(groups, null, 2));
console.log();
console.log("--------------");
console.log();
console.log(JSON.stringify(tags, null, 2));
