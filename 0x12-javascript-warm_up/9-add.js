#!/usr/bin/node

const args1 = process.argv[2];
const args2 = process.argv[3];
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(args1), parseInt(args2)));