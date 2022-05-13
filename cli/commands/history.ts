import path from "path";
import { SOLUTIONS_FILE_NAME } from "../lib/consts";

/**
 * Show success rate of previous solves.
 *
 * @usage {cliName} history
 */
export default async function main() {
  const asciichart = require("asciichart");
  const solutionsPath = path.join(process.cwd(), SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const data = solutionsData.archived
    .reverse()
    .map((solve: any) => solve.successRate * 100);
  data.push(solutionsData.active.successRate * 100);

  console.log(asciichart.plot(data, { height: 20 }));
}
