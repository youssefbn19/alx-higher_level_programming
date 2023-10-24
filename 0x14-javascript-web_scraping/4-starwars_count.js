#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const args = process.argv.slice(2);
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
let numMovies = 0;
request.get(args[0], function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    for (const char of data.results) {
      if (char.characters.includes(character)) {
        numMovies++;
      }
    }
    console.log(numMovies);
  }
});
