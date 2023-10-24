#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
request.get(args[0], function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    fs.writeFile(args[1], body, 'utf-8', function (err) {
      if (err) { console.log(err); }
    });
  }
});
