#!/usr/bin/node
// prints a string x times

let a = parseInt(process.argv[2]);
if (isNaN(a)) {
  console.log('Missing number of occurences');
} else {
  for (a; a > 0; --a) {
    console.log('C is fun');
  }
}
