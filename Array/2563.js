const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split("\n");
const repeat = parseInt(read[0]);

const board = [];
for (let i = 0; i < 100; i++) {
  board[i] = [];
  for (let j = 0; j < 100; j++) {
    board[i].push(0);
  }
}

for (let i = 1; i < repeat + 1; i++) {
  const target = read[i].split(" ");
  const targetX = parseInt(target[0]);
  const targetY = parseInt(target[1]);
  console.log(targetX, targetY);
  for (let i = targetY; i < targetY + 10; i++) {
    for (let j = targetX; j < targetX + 10; j++) {
      board[i][j] = 1;
    }
  }
}

let count = 0;
for (let i = 0; i < board.length; i++) {
  for (let j = 0; j < board.length; j++) {
    if (board[i][j] === 1) {
      count = count + 1;
    }
  }
}

console.log(count);
