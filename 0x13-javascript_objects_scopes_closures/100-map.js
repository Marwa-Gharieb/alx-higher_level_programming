#!/usr/bin/node
const list = require('./100-data.js').list;
const multipledList = [];
for (let i = 0; i < list.length; i++) {
  multipledList.push(list[i] * i);
}
console.log(list);
console.log(multipledList);
