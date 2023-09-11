#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.
const args = process.argv;
const len = args.length;
const arr = [];

if (len <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr.push(Number(args[i]));
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
