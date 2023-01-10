const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

let input = parseInt(read[0]);

var i = 2;
var primes = [];
while (true) {
  if (input % i === 0) {
    input = input / i;
    primes.push(i);
  } else {
    i++; // 4로 나누어 떨어지면 애초에 2로 나누어떨여졌음
  }
  if (i > input) {
    break;
  }
}

console.log(primes.join("\n"));
