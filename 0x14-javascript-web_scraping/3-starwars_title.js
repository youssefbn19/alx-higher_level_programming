#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const args = process.argv.slice(2);
const uri = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
request.get(uri, function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
