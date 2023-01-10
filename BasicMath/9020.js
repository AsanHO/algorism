//골드바흐의 추측
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const repeat = read[0];

function eratosthenes(start, end) {
  arr = [];
  for (let i = 0; i <= end; i++) {
    arr.push(true);
  }
  arr[0] = false;
  arr[1] = false;
  for (let m = 2; m <= parseInt(Math.sqrt(end)); m++) {
    if (arr[m]) {
      for (let n = 2; n <= end / m; n++) {
        arr[m * n] = false;
      }
    }
  }
  let info = {
    base: [start, end],
    prime: [],
    count: 0,
  };
  for (var j = start + 1; j <= end; j++) {
    if (arr[j]) {
      info.prime.push(j);
      info.count = info.count + 1;
    }
  }
  return info;
}

for (let i = 1; i < repeat + 1; i++) {
  const element = read[i];
  const info = eratosthenes(1, element);
  let diff = info.base[1];
  let a = 0;
  let b = 0;
  let result = 0;
  done: for (let i = 0; i < info.prime.length; i++) {
    a = info.prime[i];
    for (let j = 0; j < info.prime.length; j++) {
      b = info.prime[j];
      if (a + b === element) {
        if (diff > Math.abs(a - b)) {
          //차가 작으면
          if (a > b) {
            console.log("!");
            break done;
          }
          diff = Math.abs(a - b);
          result = [a, b];
        }
      }
    }
  }
  console.log(result[0], result[1]);
}
