#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
