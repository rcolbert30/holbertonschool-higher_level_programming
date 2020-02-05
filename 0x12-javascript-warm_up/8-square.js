#!/usr/bin/node
// prints a square, size of first arg

let x = process.argv[2];
let idx;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (idx = x; idx > 0; idx--) {
    console.log('X'.repeat(x));
  }
}
