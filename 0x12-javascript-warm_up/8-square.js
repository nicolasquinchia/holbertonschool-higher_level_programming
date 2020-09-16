#!/usr/bin/node
const args = process.argv;
const myInt = parseInt(args[2]);
let i;
if (isNaN(myInt)) {
  console.log('Missing size');
} else {
  for (i = 0; i < myInt; i++) {
    console.log('X'.repeat(myInt));
  }
}
