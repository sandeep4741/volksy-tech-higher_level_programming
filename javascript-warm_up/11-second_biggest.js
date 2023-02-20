#!/usr/bin/node
if (process.argv < 3){
  console.log(0);
} else {
  let a = process.argv;
  a.sort()
  console.log(a[a.length - 2]);
}
