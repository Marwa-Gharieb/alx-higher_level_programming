#!/usr/bin/node

const args = process.argv.slice(2);

function calc (...args) {
  const result = Math.max(...args);
  console.log(result);
}
if (args.length == 0 || args.length == 1) {
  console.log(0);
} else {
  calc(...args);
}
