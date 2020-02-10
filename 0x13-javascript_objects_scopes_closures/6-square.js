#!/usr/bin/node
// square that inherits from a rectangle

const Sq = require('./5-square');
class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
