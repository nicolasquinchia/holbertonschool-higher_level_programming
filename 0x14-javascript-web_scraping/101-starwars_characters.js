#!/usr/bin/node
const request = require('request');
const requestUrl = 'https://swapi-api.hbtn.io/api/films/';
const filmId = parseInt(process.argv[2]);
request(requestUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const allFilms = JSON.parse(body).results;
  for (const film of allFilms) {
    if (film.episode_id === filmId) {
      for (const charact of film.characters) {
        request(charact, function (error, response, body) {
          if (error) {
            console.log(error);
          }
          console.log(JSON.parse(body).name);
        });
      }
    }
  }
});
