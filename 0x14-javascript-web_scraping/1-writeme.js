#!/usr/bin/node
// writes a string to a file
const fs = require('fs');
const data = process.argv[3];
const path = process.argv[2];

fs.writeFile(path, data, (error) => {
  error && console.log(error);
});
