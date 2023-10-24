#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const args = process.argv.slice(2);
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(args[0], function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    let numMovies = 0;
    const data = JSON.parse(body).results;
    for (const char of data) {
      if (char.characters.includes(character)) {
        numMovies++;
      }
    }
    console.log(numMovies);
  }
});
