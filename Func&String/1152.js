const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split("\n");

const source = read[0];

let result = source.split(" ");
if (result[0] === "") {
  result = 0;
} else {
  result = result.length;
}
console.log(result);
//입력에 공백만 있다면 문제가 생김
