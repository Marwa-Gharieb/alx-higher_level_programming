#!/usr/bin/node
const list = require('./100-data.js').list;
const multipliedList = list.map((value, index) => (value * index));

console.log(list);
console.log(multipliedList);
