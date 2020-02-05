#!/usr/bin/node
// computes and prints a factorial

function factorial (x) {
  if (x <= 1 || isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
