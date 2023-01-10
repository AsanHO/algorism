const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const a = read[0];

for (let i = 1; i < 10; i++) {
  console.log(`${a} * ${i} = ${a * i}`);
}
