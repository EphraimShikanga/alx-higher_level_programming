exports.converter = function (base) {
    return function convertToBaseN(number) {
      if (number === 0) {
        return '0';
      }
  
      let result = '';
  
      while (number > 0) {
        const remainder = number % base;
        const digit = remainder < 10 ? remainder : String.fromCharCode(remainder + 55);
        result = digit + result;
        number = Math.floor(number / base);
      }
  
      return result;
    };
  };