const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

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

for (let i = 0; i < read.length - 1; i++) {
  n = read[i];
  end = 2 * n;
  //에라토스테네스 체 생성
  const result = eratosthenes(n, end);
  console.log(result.count);
}
