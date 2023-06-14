#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOfOccurences = 0;

  for (const target of list) {
    if (target === searchElement) {
      numOfOccurences++;
    }
  }

  return numOfOccurences;
};
