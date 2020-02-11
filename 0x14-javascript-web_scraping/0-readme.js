#!/usr/bin/node
// reads a prints the content of a file

const path = process.argv[2];
const fs = require('fs');
fs.readFile(path, 'utf-8', (error, data) => {
  console.log(error || data);
});
