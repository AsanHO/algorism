const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const count = parseInt(read[0]);

let a = "";

for (let i = 1; i < count; i++) {
  b = " ".repeat(count - i - 1);
  a = a + "*";
  console.log(b, a);
}
console.log("*".repeat(count));
