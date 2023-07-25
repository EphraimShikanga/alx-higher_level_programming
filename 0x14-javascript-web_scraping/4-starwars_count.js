#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    return console.error('API request failed: ', error);
  }

  if (response.statusCode !== 200) {
    return console.error('Invalid API response: ', response.statusCode);
  }

  const data = JSON.parse(body);

  let count = 0;

  data.results.forEach(film => {
    film.characters.forEach(url => {
      if (url.match(new RegExp(`people/${characterId}/`))) {
        count++;
      }
    });
  });

  console.log(count);
});
