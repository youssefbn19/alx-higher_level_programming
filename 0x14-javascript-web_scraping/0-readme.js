#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) { return console.log(err); }
  console.log(data.toString());
});
