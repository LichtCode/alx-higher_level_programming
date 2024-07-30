#!/usr/bin/node
/**
 *  script that prints all characters of a Star Wars movie:
 **/
const movieId = process.argv[2];
const request = require('request'); /* import the request module */
const url = `https://swapi.dev/api/films/${movieId}/`; /* star wars api url */

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const charactersUrl = body.characters;
  charactersUrl.forEach(url => {
    request(url, { json: true }, (error, res, content) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(content.name);
    });
  });
});
