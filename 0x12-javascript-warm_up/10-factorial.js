#!/usr/bin/node
const x = process.argv[2];
function getFact (x) {
  let a, b;
  for (let i = x; i > 1; i--) {
    const a = i * (i - 1);
    for (let j = x; j > 1; j--) {
      const b = +a;
    }
  }
  return b;
}
const y = getFact(x);

if (!x) {
  console.log('NaN');
} else {
  console.log();
}
