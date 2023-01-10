const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const repeat = parseInt(read[0]);

let sum = 0;

for (let i = 0; i < repeat; i++) {
  const element = parseInt(read[1][i]);
  sum = sum + element;
}

console.log(sum);
