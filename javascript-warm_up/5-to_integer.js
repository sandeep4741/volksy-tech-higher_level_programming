#!/usr/bin/node

let Num = parseInt(process.argv[2]);
if (isNaN(Num)) console.log('Not a number');
else console.log(`My number: ${Num}`);
