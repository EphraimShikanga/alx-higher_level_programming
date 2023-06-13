#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let times of x) {
    theFunction();
  }
};