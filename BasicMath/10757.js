const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ")
  .map(BigInt);

result = read[0] + read[1];

console.log(result.toString());
