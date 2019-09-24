#!/usr/bin/node
// returns factorial of number

function factorialize (num) {
  if (num <= 1 || isNaN(num)) {
    return 1;
  } else {
    return num * factorialize(num - 1);
  }
}
console.log(factorialize(parseInt(process.argv[2])));
