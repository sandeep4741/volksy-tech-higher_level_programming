#!/usr/bin/node

if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('x'.repeat(process.argv[2]);
}
