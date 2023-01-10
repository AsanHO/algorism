const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

let maxValue = 0;
let maxX = 0;
let maxY = 0;

for (let i = 0; i < 9; i++) {
  const row = read[i].split(" ").map(Number);
  for (let j = 0; j < 9; j++) {
    const element = row[j];
    if (maxValue <= element) {
      maxValue = element;
      maxX = j + 1;
      maxY = i + 1;
    }
  }
}
console.log(maxValue);
console.log(maxY, maxX);
