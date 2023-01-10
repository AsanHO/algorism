const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

for (let i = 1; i < 31; i++) {
  const cur = i;
  let isExist = false;
  for (let i = 0; i < read.length; i++) {
    const element = read[i];
    if (element === cur) {
      isExist = true;
      break;
    }
  }
  if (isExist === false) {
    console.log(cur);
  }
}
