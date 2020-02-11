#!/usr/bin/node
/* imports array and computes a new array
   creates a new list, new value is multipled by its index in the list */

const list = require('./100-data').list;

console.log(list);
console.log(list.map((item, index) => item * index));
