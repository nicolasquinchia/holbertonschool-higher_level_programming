#!/usr/bin/node
const request = require('request');
const toFind = '/18/';
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let movies = 0;
  for (const movie of JSON.parse(body).results) {
    for (const person of movie.characters) {
      if (person.slice(-4) === toFind) {
        movies += 1;
      }
    }
  }
  console.log(movies);
});
