#!/usr/bin/node

const args = process.argv[3];
if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}