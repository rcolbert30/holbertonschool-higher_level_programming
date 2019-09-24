#!/usr/bin/node
// adds 2 numbers

function add (a, b) {
  console.log(a + b);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
