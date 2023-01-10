const fs = require("fs");
const read = fs.readFileSync("example.txt").toString().trim().split("\n");
const repeat = parseInt(read[0]);
for (let i = 1; i < repeat + 1; i++) {
  let result = "";
  let e = read[i];
  e = e.split(" ");
  for (let i = 0; i < e[1].length; i++) {
    for (let j = 0; j < e[0]; j++) {
      result = result + e[1][i];
    }
  }
  console.log(result);
}
