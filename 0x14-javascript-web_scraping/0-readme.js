#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    process.stdout.write(data);
  }
});
