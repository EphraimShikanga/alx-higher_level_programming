#!/usr/bin/node

const args = process.argv[2];
const argAsInt = parseInt(args);
if (isNaN(args)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argAsInt);
}
