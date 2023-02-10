#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  const result = {};
  JSON.parse(body).filter(el => el.completed).forEach(el => {
    if (result[el.userId] === undefined) {
      result[el.userId] = 1;
    } else {
      result[el.userId] += 1;
    }
  });
  console.log(result);
});
