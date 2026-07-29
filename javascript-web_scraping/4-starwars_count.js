#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const results = JSON.parse(body).results;
  let count = 0;

  results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes('/18/')) {
        count++;
      }
    });
  });

  console.log(count);
});
