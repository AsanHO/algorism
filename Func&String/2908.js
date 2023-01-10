const fs = require("fs");
const read = fs.readFileSync("example.txt").toString().trim().split("\n");

let source = read[0].split(" ");
let list = [];
for (let i = 0; i < 2; i++) {
  let target = "";
  fixedsource = source[i];
  for (let i = fixedsource.length - 1; i >= 0; i--) {
    const element = fixedsource[i];
    target = target + element;
  }
  list.push(target);
}
let WIN = 0;
list[0] > list[1] ? (WIN = list[0]) : (WIN = list[1]);
console.log(WIN);
