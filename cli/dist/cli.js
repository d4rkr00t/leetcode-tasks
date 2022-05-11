#!/usr/bin/env node

let cli = require("@opaline/core").default;
let pkg = require("../package.json");
let config = {
  cliName: "riprep",
  cliVersion: pkg.version,
  cliDescription: "" || pkg.description,
  isSingleCommand: false,
  commands: {
    "failed": {
      commandName: "failed",
      meta: {"title":"Marks the most recent task as failed.","description":"","usage":"riprep failed","examples":[],"shouldPassInputs":false,"options":{}},
      load: () => {
        let command = require("./commands/failed");

        if (typeof command !== "function") {
          throw new Error(`Command "failed" doesn't export a function...`)
        }

        return command;
      }
    }, "pick": {
      commandName: "pick",
      meta: {"title":"Pick next task to solve.","description":"","usage":"riprep pick","examples":[],"shouldPassInputs":false,"options":{}},
      load: () => {
        let command = require("./commands/pick");

        if (typeof command !== "function") {
          throw new Error(`Command "pick" doesn't export a function...`)
        }

        return command;
      }
    }, "progress": {
      commandName: "progress",
      meta: {"title":"Showes the progress.","description":"","usage":"riprep progress","examples":[],"shouldPassInputs":false,"options":{}},
      load: () => {
        let command = require("./commands/progress");

        if (typeof command !== "function") {
          throw new Error(`Command "progress" doesn't export a function...`)
        }

        return command;
      }
    }, "solved": {
      commandName: "solved",
      meta: {"title":"Marks the most recent task as solved.","description":"","usage":"riprep solved","examples":[],"shouldPassInputs":false,"options":{}},
      load: () => {
        let command = require("./commands/solved");

        if (typeof command !== "function") {
          throw new Error(`Command "solved" doesn't export a function...`)
        }

        return command;
      }
    }, "sort": {
      commandName: "sort",
      meta: {"title":"Sort tasks by difficulty.","description":"","usage":"riprep sort","examples":[],"shouldPassInputs":false,"options":{}},
      load: () => {
        let command = require("./commands/sort");

        if (typeof command !== "function") {
          throw new Error(`Command "sort" doesn't export a function...`)
        }

        return command;
      }
    }
  }
};

cli(process.argv, config);
