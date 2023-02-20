#!/usr/bin/node
if (process.argv <= 3) {
  console.log(0);
} else {
  const a = process.argv;
  a.sort((a, b) => a - b);
  console.log(a[a.length - 2]);
}
