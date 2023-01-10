const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");
const N = parseInt(read[0].split(" ")[0]);
const M = parseInt(read[0].split(" ")[1]);

for (let i = 1; i <= N; i++) {
  const A = read[i].split(" ").map(Number);
  const B = read[i + N].split(" ").map(Number);
  let result = [];
  for (let i = 0; i < M; i++) {
    const sum = A[i] + B[i];
    result.push(sum);
  }
  console.log(...result);
}
