#!/usr/bin/node
// makes a request based on id

const request = require('request');
const id = process.argv[2];
const url = `http://swapi.co/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
