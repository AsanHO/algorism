//https://namu.wiki/w/%EC%86%8C%EC%88%98(%EC%88%98%EB%A1%A0)#s-6
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().split(" ").map(Number);
let start = read[0];
const end = read[1];
const target = parseInt(Math.sqrt(end));
let prime = [];
for (let i = 2; i < target + 1; i++) {
  const e = i;
  let divisor = [];
  for (let i = 1; i < e + 1; i++) {
    if (e % i == 0) {
      divisor.push(i);
    }
  }
  if (divisor.length < 3) {
    if (e !== 1) {
      prime.push(e);
    }
  }
}
// 에라토스테네스 체에 거를 숫자리스트 생성

esc: for (let i = start === 1 ? 2 : start; i < end + 1; i++) {
  for (let p = 0; p < prime.length; p++) {
    const cur = prime[p];
    if (i > cur && i % cur === 0) {
      continue esc;
    }
  }
  console.log(i);
}
