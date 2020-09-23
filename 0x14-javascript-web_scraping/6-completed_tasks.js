#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const tasks = JSON.parse(body);
  const usersTasks = {};
  for (const task of tasks) {
    if (task.completed === true) {
      if (task.userId in usersTasks) {
        usersTasks[task.userId] += 1;
      } else {
        usersTasks[task.userId] = 1;
      }
    }
  }
  console.log(usersTasks);
});
