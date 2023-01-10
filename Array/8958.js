const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

for (let i = 1; i < parseInt(read[0]) + 1; i++) {
  array = read[i].split("");
  let sum = 0;
  let conti = 0;

  for (const e of array) {
    if (e === "O") {
      conti = conti + 1;
      sum = sum + conti;
    } else {
      conti = 0;
    }
  }
  console.log(sum);
}
