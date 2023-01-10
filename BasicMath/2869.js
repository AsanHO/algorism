const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const a = read[0];
const b = read[1];
const v = read[2];
// 올라야 하는 건 결국 v에서 -b를 뺀값이다.
const result = Math.ceil((v - b) / (a - b));
console.log(result);
