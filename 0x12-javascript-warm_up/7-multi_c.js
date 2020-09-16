#!/usr/bin/node
const args = process.argv;
const myInt = parseInt(args[2]);
let i;
if (isNaN(myInt)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < myInt; i++) {
    console.log('C is fun');
  }
}
