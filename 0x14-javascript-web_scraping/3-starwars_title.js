#!/usr/bin/node
const request = require('request');
const requestUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(requestUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const toObj = JSON.parse(body);
    console.log(toObj.title);
  }
});
