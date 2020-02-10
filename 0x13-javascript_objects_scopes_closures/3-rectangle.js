#!/usr/bin/node
// rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let rows = 0; rows < this.height; rows++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
