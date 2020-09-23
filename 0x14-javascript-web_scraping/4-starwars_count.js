#!/usr/bin/node
const request = require('request');
const toFind = 'https://swapi-api.hbtn.io/api/people/18/';
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let movies = 0;
  for (const movie of JSON.parse(body).results) {
    if (movie.characters.includes(toFind)) {
      movies += 1;
    }
  }
  console.log(movies);
});
