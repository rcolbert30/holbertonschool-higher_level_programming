#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        const id = task.userId;

        if (dict[id] === undefined) {
          dict[id] = 1;
        } else {
          dict[id] += 1;
        }
      }
    }
    console.log(dict);
  }
});
