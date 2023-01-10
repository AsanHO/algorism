const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const repeat = parseInt(read[0]);
const arr = read[1].split(" ");
const target = parseInt(read[2]);
let count = 0;

for (let i = 0; i < repeat; i++) {
  if (parseInt(arr[i]) === target) {
    count = count + 1;
  }
}

console.log(count);
