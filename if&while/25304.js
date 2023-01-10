const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const recipt = parseInt(read[0]);
const num = parseInt(read[1]) + 1;
let sum = 0;

for (let i = 1; i < num; i++) {
  const AB = read[i + 1].split(" ");
  const A = parseInt(AB[0]);
  const B = parseInt(AB[1]);
  sum = sum + A * B;
}
let result;
result = sum === recipt ? "Yes" : "No";

console.log(result);
