#!/usr/bin/node
// prints if 1st arg can be converted into integer

const arg = process.argv[2];
if (parseInt(arg)) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
