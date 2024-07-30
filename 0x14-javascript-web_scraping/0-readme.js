#!/usr/bin/node

/*
 *  a script that reads and prints the content of a file.
 */
const fs = require('fs'); /* load the fs modole */
const filename = process.argv[2]; /* loads the process to access argv */

fs.readFile(filename, 'utf-8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
