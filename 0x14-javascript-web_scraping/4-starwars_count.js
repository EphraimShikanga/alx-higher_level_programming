#!/usr/bin/node

const request = require('request');
const wedgeAntillesId = 18;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, body);
  } else {
    const movieData = JSON.parse(body);
    let count = 0;
    for (const character of movieData.characters) {
      if (character.includes(wedgeAntillesId)) {
        count++;
      }
    }
    console.log(count);
  }
});
