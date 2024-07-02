#!/usr/bin/node

const n = parseInt(process.argv[2])

function factorial(n){
    if(n == 1 || !n){
      return 1
    }
    else{
      return n * factorial(n-1)
    }
}

const num = factorial(n)
console.log(num)