#!/usr/bin/node
const request = require('request');
const path = process.argv[3];
const url = process.argv[2];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = body;
    fs.writeFile(path, data, function (error, file) {
      if (error) {
        console.log(error);
      }
    });
  }
});
