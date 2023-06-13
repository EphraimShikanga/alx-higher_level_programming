#!/usr/bin/node

const argsAsList = Array.from(process.argv);
function secondBiggest (argsAsList) {
  let biggest = 0;
  let secondBiggest = 0;
  for (let args of argsAsList) {
    if (parseInt(args) > biggest) {
      secondBiggest = biggest;
      biggest = parseInt(args);
    } else if (parseInt(args) > secondBiggest) {
      secondBiggest = parseInt(args);
    }
  }
  return secondBiggest;
}
if (argsAsList.length === 2 || argsAsList.length === 3) {
  console.log(0);
} else {
  console.log(secondBiggest(argsAsList));
}