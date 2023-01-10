const fs = require("fs");
const { syncBuiltinESMExports } = require("module");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let arr = [];
for (let i = 0; i < read.length; i++) {
  arr.push(read[i]);
}
for (let i = 0; i < arr.length; i++) {
  for (let j = i + 1; j < arr.length; j++) {
    if (arr[i] > arr[j]) {
      temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
  }
}
let sum = 0;
arr.map((cur) => (sum = sum + cur));
console.log(sum / arr.length);
console.log(arr[2]);
