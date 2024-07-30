#!/usr/bin/node

/*
 *  a script that display the status code of a GET request.
 */
const url = process.argv[2];
const request = require('request');
const filename = process.argv[3];
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filename, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
