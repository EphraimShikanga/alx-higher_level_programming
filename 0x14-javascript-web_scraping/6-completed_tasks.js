#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request({ url: apiUrl, json: true }, (error, response, body) => {
  if (error) {
    return console.error('Unable to connect to API:', error);
  } else if (response.statusCode !== 200) {
    return console.error('Status Code:', response.statusCode);
  }

  const users = {};

  body.forEach(task => {
    if (task.completed) {
      const userId = task.userId;
      if (users[userId]) {
        users[userId]++;
      } else {
        users[userId] = 1;
      }
    }
  });

  console.log(users);
});
