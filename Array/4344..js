const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

const count = parseInt(read[0]);

for (let i = 1; i < count + 1; i++) {
  let sum = 0;
  let avg = 0;
  const arr = read[i].split(" ").map(Number);
  for (let i = 1; i < arr[0] + 1; i++) {
    sum = sum + arr[i];
  }
  avg = sum / arr[0];
  let winAvgMan = 0;
  for (let i = 1; i < arr[0] + 1; i++) {
    const element = arr[i];
    if (element > avg) {
      winAvgMan = winAvgMan + 1;
    }
  }
  let per = (winAvgMan / arr[0]) * 100;
  console.log(per.toFixed(3) + "%");
}
