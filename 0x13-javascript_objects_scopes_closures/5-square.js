#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (_size) {
    super(_size, _size);
  }
}
module.exports = Square;
