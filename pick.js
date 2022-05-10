#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const solutionsMDFilePath = path.join(__dirname, "solutions.md");
const solutionsDirPath = path.join(__dirname, "solutions");
const solutions = fs.readdirSync(solutionsDirPath);
const solutionsCount = solutions.length;
const tasks = {
  easy: fs.readdirSync(path.join(__dirname, "tasks", "easy")),
  medium: fs.readdirSync(path.join(__dirname, "tasks", "medium")),
  hard: fs.readdirSync(path.join(__dirname, "tasks", "hard")),
  new: fs.readdirSync(path.join(__dirname, "tasks", "new")),
};
const totalTasksCount = Object.keys(tasks).reduce((acc, key) => {
  acc += tasks[key].length;
  return acc;
}, 0);

if (solutionsCount === totalTasksCount) {
  console.log("🎉 Everything is solved!");
  process.exit(0);
}

while (true) {
  const category = pickCategory();
  const item =
    tasks[category][Math.floor(Math.random() * tasks[category].length)];

  if (fs.existsSync(path.join(solutionsDirPath, item))) {
    continue;
  }

  const num = item.split("-")[0];
  const newContent =
    `✅❌ ${num}\n` + fs.readFileSync(solutionsMDFilePath, "utf-8");
  fs.writeFileSync(solutionsMDFilePath, newContent, "utf-8");
  const fileSrc = path.join(__dirname, "tasks", category, item);
  const fileDest = path.join(solutionsDirPath, item);
  fs.copyFileSync(fileSrc, fileDest);

  console.log("Next task: ", item);
  execSync(`code-insiders ${fileDest} -r`);

  break;
}

function pickCategory() {
  const rnd = Math.floor(Math.random() * (100 - 2)) + 1;
  if (rnd <= 20) {
    return "easy";
  } else if (rnd <= 40) {
    return "medium";
  } else if (rnd <= 60) {
    return "new";
  } else {
    return "hard";
  }
}
