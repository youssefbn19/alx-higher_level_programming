#!/usr/bin/node
// Prints the addition of 2 integers.
const args = process.argv;

function factorial (a) {
  let num = Number(a);
  if (isNaN(num)) {
    return 1;
  } else if (num > 1) {
    num *= factorial(num - 1);
  }
  return num;
}

const result = factorial(args[2]);
console.log(result);
