#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  console.log(args.sort((x, y) => y - x).slice(3)[0]);
}
