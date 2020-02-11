#!/usr/bin/node
// returns number of occurnces in a list

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
