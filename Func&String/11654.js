const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");
console.log(read[0].charCodeAt(0));
