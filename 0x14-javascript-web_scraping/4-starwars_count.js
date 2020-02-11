#!/usr/bin/node
// prints the number of movies where the wedge antiles is present

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const movie = (data.results);
    const wedge = /18/;

    for (const m of movie) {
      const c = m.characters;
      for (const x of c) {
        if (wedge.test(x) === true) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
