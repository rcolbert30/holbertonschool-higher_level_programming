#!/usr/bin/node

const dict = require('./101-data').dict;

console.log(Object.entries(dict).reduce(function (x, y) {
  x[y[1]] = (x[y[1]] || []).concat(y[0]);
  return x;
}, {}));
