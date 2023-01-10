const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");
const repeat = parseInt(read[0]);
array = read[1].split(" ").map(Number);
array.sort(function (a, b) {
  return a - b;
});
let sum = 0;
let max = array[repeat - 1];
for (let i = 0; i < repeat; i++) {
  const element = array[i];
  sum = sum + (element / max) * 100;
}
console.log(sum / repeat);
