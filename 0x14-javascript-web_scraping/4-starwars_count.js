#!/usr/bin/node

/*
 *  a script that prints the number of movies where the
 */
const movieCharacterId = '18';
const request = require('request');
const url = process.argv[2];
let countMovies = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(movieCharacterId)) {
          countMovies = countMovies + 1;
        }
      });
    });
    console.log(countMovies);
  }
});
