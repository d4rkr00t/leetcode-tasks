'use strict';

var path = require('path');
var consts = require('./consts-dcdb998c.js');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var path__default = /*#__PURE__*/_interopDefaultLegacy(path);

/**
 * Show success rate of previous solves.
 *
 * @usage {cliName} history
 */
async function main() {
  const asciichart = require("asciichart");
  const solutionsPath = path__default["default"].join(process.cwd(), consts.SOLUTIONS_FILE_NAME);
  const solutionsData = require(solutionsPath);
  const data = solutionsData.archived
    .reverse()
    .map((solve) => solve.successRate * 100);
  data.push(solutionsData.active.successRate * 100);

  console.log(asciichart.plot(data, { height: 20 }));
}

module.exports = main;
