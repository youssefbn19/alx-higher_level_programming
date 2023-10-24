#!/usr/bin/node
// Computes the number of tasks completed by user id.
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], function (err, res, body) {
  if (err) { return console.log(err); }
  if (res.statusCode === 200) {
    const tasks = JSON.parse(body);
    const res = {};
    for (const task of tasks) {
      if (task.userId in res && task.completed) {
        res[task.userId] += 1;
      } else if (task.completed) {
        res[task.userId] = 1;
      }
    }
    console.log(res);
  }
});
