#!/usr/bin/node
// Prints all characters of a Star Wars movie which its ID passed as an argument,
// in the same order of the list “characters” in the /films/ response.
const request = require('request');
const args = process.argv.slice(2);
const uri = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
request.get(uri, function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characterName(characters, 0);
  }
});
function characterName (arr, indx) {
  if (indx >= arr.length) return;
  request.get(arr[indx], function (error, result, content) {
    if (error) { return console.log(error); }
    if (result.statusCode === 200) {
      const name = JSON.parse(content).name;
      console.log(name);
      characterName(arr, indx + 1);
    }
  });
}
