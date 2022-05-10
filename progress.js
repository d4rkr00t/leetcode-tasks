const fs = require("fs");
const path = require("path");

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

const solutions = fs.readdirSync(path.join(__dirname, "solutions"));
const solutionsSet = new Set(solutions);

tasks.easy.forEach((task) => {
  if (!solutionsSet.has(task)) {
    console.log("Not solved: " + task);
  }
});

tasks.medium.forEach((task) => {
  if (!solutionsSet.has(task)) {
    console.log("Not solved: " + task);
  }
});

tasks.hard.forEach((task) => {
  if (!solutionsSet.has(task)) {
    console.log("Not solved: " + task);
  }
});

tasks.new.forEach((task) => {
  if (!solutionsSet.has(task)) {
    console.log("Not solved: " + task);
  }
});

console.log();
console.log(
  `${solutions.length}/${totalTasksCount} | ${(
    (solutions.length / totalTasksCount) *
    100
  ).toFixed(0)}% | ${totalTasksCount - solutions.length} task(s) left`
);
