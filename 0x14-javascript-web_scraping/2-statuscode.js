#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], function (error, response) {
  if (error) { console.log(error); }
  console.log(`code: ${response.statusCode}`);
});
