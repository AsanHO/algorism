const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split("\n");

const m = parseInt(read[0]);
const n = parseInt(read[1]);

let target = [];
for (let i = m; i < n + 1; i++) {
  let divisor = [];
  for (let j = 1; j < i + 1; j++) {
    if (i % j == 0) {
      divisor.push(j);
    }
  }
  if (divisor.length < 3) {
    if (i !== 1) {
      target.push(i);
    }
  }
}

let sum = 0;
target.map((cur) => (sum = sum + cur));
if (target.length === 0) {
  console.log(-1);
} else {
  console.log(sum);
  console.log(target[0]);
}
