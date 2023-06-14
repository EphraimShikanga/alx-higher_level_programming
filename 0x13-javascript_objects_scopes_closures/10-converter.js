#!/usr/bin/node

exports.converter = function (base) {
  return function myConvert (number) {
    if (number === 0) {
      return '';
    } else {
      return myConvert(Math.floor(number / base)) + (number % base);
    }
  };
};
