#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    let numMovies = 0;
    const data = JSON.parse(body).results;
    const character = '/api/people/18/';
    for (let i = 0; i < data.length; i++) {
      if (data[i].characters.find(char => char.includes(character))) {
        numMovies++;
      }
    }
    console.log(numMovies);
  }
});
