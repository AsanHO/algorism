const fs = require("fs");

const read = fs.readFileSync("example.txt").toString().trim().split("\n");

let people = read[0].split(" ").map(Number);
let news = read[1].split(" ").map(Number);

const target = people[0] * people[1];
people = parseInt(people[0]);

let result = [];
for (let i = 0; i < 5; i++) {
  result.push(news[i] - target);
}

console.log(...result);
