#!/usr/bin/node

const SQUARE = require('./5-square');

class Square extends SQUARE {
  charPrint (c) {
    let symbol = '';
    if (c === undefined) c = 'X';
    for (let j = 0; j < this.width; j++) {
      symbol += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(symbol);
    }
  }
}
module.exports = Square;
