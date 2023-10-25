#!/usr/bin/node
// Prints all characters of a Star Wars movie which its ID passed as an argument.
const request = require('request');
const args = process.argv.slice(2);
const uri = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
request.get(uri, function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const char of characters) {
      request.get(char, function (error, result, content) {
        if (error) { return console.log(error); }
        if (result.statusCode === 200) {
          const name = JSON.parse(content).name;
          console.log(name);
        }
      });
    }
  }
});
