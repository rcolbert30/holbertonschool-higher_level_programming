#!/usr/bin/node
// prints a square

const square = parseInt(process.argv[2]);
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let s = square; s > 0; s--) {
    console.log('X'.repeat(square));
  }
}
