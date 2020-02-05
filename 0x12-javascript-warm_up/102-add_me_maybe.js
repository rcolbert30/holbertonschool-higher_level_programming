#!/usr/bin/node
// increments a function

exports.addMeMaybe = (number, theFunction) => {
  number = number + 1;
  theFunction(number);
};
