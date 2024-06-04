#!/usr/bin/node
let args = process.argv
let x =args.slice(2)

if (!args[2]){
    console.log('No argument')
}
else {
    console.log(x)
}