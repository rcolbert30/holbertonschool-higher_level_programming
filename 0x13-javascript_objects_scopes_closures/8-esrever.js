#!/usr/bin/node
// return reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 2; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
