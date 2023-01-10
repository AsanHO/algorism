const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const repeat = parseInt(read[0]) + 1;
let sum = 0;
for (let i = 1; i < repeat; i++) {
  sum = sum + i;
}
console.log(sum);
