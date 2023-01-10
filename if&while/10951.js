const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");
let i = 0;
while (true) {
  if (read[i] === undefined) {
    break;
  }
  const line = read[i].split(" ");
  a = parseInt(line[0]);
  b = parseInt(line[1]);
  console.log(a + b);
  i++;
}
