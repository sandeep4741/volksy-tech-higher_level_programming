#!/usr/bin/node
if (process.argv < 3){
  console.log(0);
} else {
  let a = process.argv;
  let b = a.sort();
  console.log(b[b.length-2]);
}
