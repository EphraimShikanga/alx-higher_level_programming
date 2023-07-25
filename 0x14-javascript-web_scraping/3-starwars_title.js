#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request({ url: apiUrl, json: true }, (error, response, body) => {
  if (error) {
    return console.error('Unable to connect to API: ', error);
  } else if (response.statusCode !== 200) {
    return console.error('Status Code: ', response.statusCode);
  }

  const title = body.title;

  console.log(title);
});
