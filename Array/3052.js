const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const set = new Set();

read.map((cur) => set.add(cur % 42));
console.log(set.size);
