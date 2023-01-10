const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const count = parseInt(read[0]);

let a = "";
for (let i = 1; i < count + 1; i++) {
  a = a + "*";
  console.log(a);
}
