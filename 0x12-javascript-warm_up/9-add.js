#!/usr/bin/node

function add(a, b){
    return a + b;
}
let a = Number(process.argv[2]);
let b = Number(process.argv[3]);

if(!isNaN(a) && !isNaN(b)){
    let x = add(a, b)
    console.log(x);
}
else{
    console.log('isNaN')
}