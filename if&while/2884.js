const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let a = read[0];
let b = read[1];

b = b - 45;
if (b < 0) {
  a = a - 1;
  b = b + 60;
}
if (a < 0) {
  a = 24 + a;
}
console.log(a, b);
