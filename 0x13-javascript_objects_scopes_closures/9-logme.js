#!/usr/bin/node
exports.logMe = function (item) {
  this.logsCounter = this.logsCounter || 0;
  console.log(`${this.logsCounter}: ${item}`);
  this.logsCounter += 1;
};
