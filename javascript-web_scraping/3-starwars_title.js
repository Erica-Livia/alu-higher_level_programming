#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieID}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('An error has occurred');
  }
});
