const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().split(" ");
const target = parseInt(read[0]);
let depth = 1;
let loc = 1;
let inc = 2; //이 방에 도달하면 깊이 추가
while (true) {
  if (loc === target) {
    break;
  }
  loc = loc + 1;
  //증가점에 존재한다면 depth추가
  if (loc === inc) {
    depth = depth + 1;
    const x = depth - 1; //증가 비
    inc = inc + 6 * x;
  }
}
console.log(depth);

let range = 1,
  block = 1;

while (block < target) {
  block = block + 6 * range;
  range = range + 1;
}

console.log(range);
