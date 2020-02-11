#!/usr/bin/node
// converts a number from base 10 to anoter base passed as a argument
exports.converter = function (base) {
  return function convertNum (num) {
    return num.toString(base);
  };
};
