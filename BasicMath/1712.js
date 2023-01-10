const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const input = fs.readFileSync(filePath).toString().split(" ").map(Number);
const A = input[0];
const B = input[1];
const C = input[2];

let invest = A;
// 반복문대신 나눗셈으로 연산할것!!!!
const per = C - B;
if (per <= 0) {
  console.log(-1);
} else {
  const result = invest / per + 1;
  console.log(parseInt(result));
}
//infinity예외처리
