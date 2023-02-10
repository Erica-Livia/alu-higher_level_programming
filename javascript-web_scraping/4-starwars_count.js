#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];
const characterId = 18;

request(API_URL, function (error, response, body) {
  if (error) {
    console.error('Error: ', error);
    return;
  }

  let count = 0;
  const films = JSON.parse(body).results;
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes(`/${characterId}/`)) {
        count++;
      }
    });
  });
  console.log(count);
});
