#!/usr/bin/node
const list = require('./100-data.js').list;
const indexList = list.map((x) => x * list.indexOf(x));
console.log(list);
console.log(indexList);
