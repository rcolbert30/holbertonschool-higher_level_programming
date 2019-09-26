#!/usr/bin/node
exports.nbOccurences = function (list, element) {
  return list.filter(x => x == element).length;
};
