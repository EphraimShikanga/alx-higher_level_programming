#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    return console.error('Error requesting URL: ', error);
  }

  if (response.statusCode !== 200) {
    return console.error('Invalid status code: ', response.statusCode);
  }

  const content = body;

  fs.writeFile(path, content, 'utf8', (err) => {
    if (err) {
      return console.error('Error writing to file: ', err);
    }
  });
});
