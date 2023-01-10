const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const a = read[0];
const b = read[1];
const c = read[2];
let result;
//jackpot
if (a === b && b === c) {
  result = 10000 + a * 1000;
} else if (a === b || a === c) {
  result = 1000 + a * 100;
} else if (b === c) {
  result = 1000 + b * 100;
} else {
  if (a > b && a > c) {
    //a가 가장 크면
    result = a * 100;
  } else if (b > c) {
    result = b * 100;
  } else {
    result = c * 100;
  }
}
console.log(result);
