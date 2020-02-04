#!/usr/bin/node
// prints x amount of times

let x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (x; x > 0; --x) {
    console.log('C is fun');
  }
}
