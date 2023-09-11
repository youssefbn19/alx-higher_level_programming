#!/usr/bin/node
// Prints x times “C is fun”. Where x is the first argument of the script.
const args = process.argv;
const num = Number(args[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
