#!/usr/bin/node

const list = require('./100-data.js').list;

const mapList = list.map((element, idx) => element * idx);
console.log(list);
console.log(mapList);
