#!/usr/bin/node
// prints number of args w value
let arg = 0;

exports.logMe = function (item) {
  console.log(`${arg}: ${item}`);
  arg++;
};
