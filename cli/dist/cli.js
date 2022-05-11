#!/usr/bin/env node

let cli = require("@opaline/core").default;
let pkg = require("../package.json");
let config = {
  cliName: "riprep",
  cliVersion: pkg.version,
  cliDescription: "" || pkg.description,
  isSingleCommand: false,
  commands: {
    "pick": {
      commandName: "pick",
      meta: {"title":"Pick next task to solve.","description":"","usage":"riprep pick","examples":[],"shouldPassInputs":false,"options":{}},
      load: () => {
        let command = require("./commands/pick");

        if (typeof command !== "function") {
          throw new Error(`Command "pick" doesn't export a function...`)
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
