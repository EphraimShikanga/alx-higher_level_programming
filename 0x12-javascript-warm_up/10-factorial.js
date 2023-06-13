#!/usr/bin/node

const args = process.argv[2];
const argAsInt = Number(args);
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(argAsInt));