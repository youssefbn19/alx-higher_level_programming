#!/usr/bin/node
// Prints a square.
const args = process.argv;
const num = Number(args[2]);
let character;

if (isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    character = '';
    for (let i = 0; i < num; i++) {
      character += 'X';
    }
    console.log(character);
  }
}
