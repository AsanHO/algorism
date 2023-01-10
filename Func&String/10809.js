const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");
const list = read[0];
console.log(list);
for (let i = 97; i < 123; i++) {
  const element = String.fromCharCode(i);
  let fix = -1;
  for (let i = 0; i < list.length; i++) {
    if (list[i] == element) {
      fix = i;
      break;
    }
  }
  console.log(fix);
}
