const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const line1 = read[0].split(" ");
const line2 = read[1].split(" ");

const repeat = parseInt(line1[0]);
const target = parseInt(line1[1]);

let nest = [];
for (let i = 0; i < repeat; i++) {
  const curNum = parseInt(line2[i]);
  curNum < target && nest.push(curNum);
}
console.log(...nest);
