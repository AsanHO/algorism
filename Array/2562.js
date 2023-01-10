const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let result = 0;
for (let i = 0; i < read.length; i++) {
  const element = read[i];
  if (element > result) {
    result = element;
  }
}

console.log(result);
console.log(read.indexOf(result) + 1);
