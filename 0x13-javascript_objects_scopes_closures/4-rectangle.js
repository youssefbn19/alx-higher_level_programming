#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let symbol = '';
    for (let j = 0; j < this.width; j++) {
      symbol += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(symbol);
    }
  }

  rotate () {
    let symbol = '';
    for (let j = 0; j < this.height; j++) {
      symbol += 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(symbol);
    }
  }

  double () {
    let symbol = '';
    this.height *= 2;
    this.width *= 2; 
    for (let j = 0; j < this.width; j++) {
      symbol += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(symbol);
    }
  }
}
module.exports = Rectangle;
