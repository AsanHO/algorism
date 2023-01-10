const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split("\n");

const repeat = parseInt(read[0]);
for (let i = 1; i < repeat + 1; i++) {
  const element = read[i].split(" ").map(Number);
  const floor = element[0];
  const roomCount = element[1];
  const customer = element[2];
  let rooms = [];
  for (let i = 1; i < roomCount + 1; i++) {
    for (let j = 1; j < floor + 1; j++) {
      const roomNumber = j * 100 + i;
      rooms.push(roomNumber);
    }
  }
  console.log(rooms[customer - 1]);
}
