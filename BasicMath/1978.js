const fs = require("fs");
const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const repeat = parseInt(read[0]);
const arr = read[1].split(" ").map(Number);
let target = [];
for (let i = 0; i < repeat; i++) {
  const e = arr[i];
  let divisor = [];
  for (let i = 1; i < e + 1; i++) {
    if (e % i == 0) {
      divisor.push(i);
    }
  }
  if (divisor.length < 3) {
    if (e !== 1) {
      target.push(e);
    }
  }
}

console.log(target.length);
