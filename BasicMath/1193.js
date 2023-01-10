const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split(" ");
const target = parseInt(read[0]);
let count = 1;
let main = 1;
let p = 1;
let c = 1;
// 타겟과 카운트값이 같아질때까지 반복
while (target != count) {
  main = main + 1; //분모증가
  //라인이 짝수일 경우 1까지 -1반복
  if (main % 2 == 0) {
    p = main;
    c = 1;
    count = count + 1;
    if (target === count) {
      break;
    }
    for (let i = c; i < main; i++) {
      p = p - 1;
      c = c + 1;
      count = count + 1;
      if (target === count) {
        break;
      }
    }
    //홀수일경우 1부터 +1 반복
  } else {
    c = main;
    p = 1;
    count = count + 1;
    if (target === count) {
      break;
    }
    for (let i = p; i < main; i++) {
      p = p + 1;
      c = c - 1;
      count = count + 1;

      if (target === count) {
        break;
      }
    }
  }
}
console.log(c + "/" + p);
