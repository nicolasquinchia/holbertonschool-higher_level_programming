#!/usr/bin/node
const request = require('request');
const requestUrl = process.argv[2];
const characUrl = 'https://swapi-api.hbtn.io/api/people/18/';
let movies = 0;
request(requestUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const toObj = JSON.parse(body);
  for (let i = 0; toObj.results[i]; i++) {
    if (toObj.results[i].characters.includes(characUrl)) {
      movies++;
    }
  }
  console.log(movies);
});
