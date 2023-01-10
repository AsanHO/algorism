const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

let target = parseInt(read[0]);
let num = target;
let cycle = 1;
while (true) {
  sum = parseInt(num / 10) + (num % 10);
  num = (num % 10) * 10 + (sum % 10);
  if (target === num) {
    break;
  }
  cycle = cycle + 1;
}
console.log(cycle);
