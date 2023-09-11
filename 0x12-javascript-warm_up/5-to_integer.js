#!/usr/bin/node
// Prints two arguments passed to it, in the following format: “ is ”.
const args = process.argv;
const num = Number(args[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
