const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

array = read[1]
  .split(" ")
  .map(Number)
  .sort(function compare(a, b) {
    return a - b;
  });

console.log(array[0], array[array.length - 1]);
