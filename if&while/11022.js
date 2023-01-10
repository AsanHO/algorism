const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const count = parseInt(read[0]);

for (let i = 1; i < count + 1; i++) {
  const AB = read[i].split(" ");
  const A = parseInt(AB[0]);
  const B = parseInt(AB[1]);
  console.log(`Case #${i}: ${A} + ${B} = ${A + B}`);
}
