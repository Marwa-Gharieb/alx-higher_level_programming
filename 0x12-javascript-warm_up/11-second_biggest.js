#!/usr/bin/node

const inputArgs = process.argv.slice(2).map(arg => parseInt(arg));

function SMax (...args) {
  if (args.length === 0 || args.length === 1) {
    console.log(1);
  } else {
    args.sort((a, b) => a - b);
    console.log(args[args.length - 2]);
  }
}

SMax(...inputArgs);
