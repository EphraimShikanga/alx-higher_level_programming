#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBaseN (number) {
    if (number === 0) {
      return '0';
    }

    if (number < base) {
      return number < 10 ? number.toString() : String.fromCharCode(number + 55);
    }

    return convertToBaseN(Math.floor(number / base)) + convertToBaseN(number % base);
  };
};
