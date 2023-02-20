#!/usr/bin/node

let a = parseInt(process.argv[2])
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    console.log('x'.repeat(a);
}
