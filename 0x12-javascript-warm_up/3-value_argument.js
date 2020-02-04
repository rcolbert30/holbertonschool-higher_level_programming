#!/usr/bin/node
// prints first argument passed to it

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
