const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

let a = read[0].split(" ");
hour = parseInt(a[0]);
minute = parseInt(a[1]);
let time = parseInt(read[1]);

minute = minute + time;
if (minute > 59) {
  hour = parseInt(hour + minute / 60);
  minute = minute % 60;
}
if (hour > 23) {
  hour = hour - 24;
}
console.log(hour, minute);
