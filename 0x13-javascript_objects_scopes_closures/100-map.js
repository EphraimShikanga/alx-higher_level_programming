#!/usr/bin/node

const arrList = require('./100-data').list;
const newList = arrList.map((index, value) => index * value);
console.log(arrList);
console.log(newList);
