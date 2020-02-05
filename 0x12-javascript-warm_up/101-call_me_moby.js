#!/usr/bin/node
// execute function x times

exports.callMeMoby = (x, theFunction) => {
  let y = x;
  while (y > 0) {
    theFunction();
    --y;
  }
};
