#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(url, function (error, response, body) {
  if (error) console.log(error);
  const chars = JSON.parse(body).characters;
  logChars(chars, 0);
});

const logChars = (chars, a) => {
  if (a === chars.length) return;
  request(chars[a], function (error, response, body) {
    if (error) console.log(error);
    console.log(JSON.parse(body).name);
    logChars(chars, a + 1);
  });
}
