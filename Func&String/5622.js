const fs = require("fs");
const read = fs.readFileSync("example.txt").toString().trim().split("\n");
const source = read[0];
let phone = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"];

let sum = 0;
for (let i = 0; i < source.length; i++) {
  const target = source[i];
  for (let i = 0; i < phone.length; i++) {
    const source = phone[i];
    for (let j = 0; j < source.length; j++) {
      if (target == source[j]) {
        sum = sum + i + 3;
      }
    }
  }
}
console.log(sum);
