#!/usr/bin/node
// Prints the addition of 2 integers.
const args = process.argv;

function add (a, b) {
  const num1 = Number(a);
  const num2 = Number(b);
  console.log(num1 + num2);
}

add(args[2], args[3]);
