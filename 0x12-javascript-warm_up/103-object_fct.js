#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject = {
  type: 'object',
  value: 12,
  incr () {
    this.value += 1;
    return (this.value);
  }
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
