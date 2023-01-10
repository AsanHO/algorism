const fs = require("fs");
const read = fs.readFileSync("example.txt").toString().trim().split("");

const source = read.map((cur) => cur.toUpperCase()).sort();
let oldcount = 0;
let target = "";
for (let i = 0; i < source.length; ) {
  const element = source[i];
  let newcount = 0;
  let jumpnumber = 0;
  for (let j = i; j < source.length; j++) {
    if (element == source[j]) {
      newcount = newcount + 1;
      jumpnumber = jumpnumber + 1;
    } else {
      break;
    }
  }
  if (newcount == oldcount) {
    target = "?";
  }
  if (newcount > oldcount) {
    oldcount = newcount;
    target = element;
  }
  i = i + jumpnumber;
}
console.log(target);

/* let oldcount = 0;
let target = "";
for (let i = 0; i < source.length; i++) {
  const element = source[i].toUpperCase();
  let newcount = 0;
  for (let j = i; j < source.length; j++) {
    if (element == source[j].toUpperCase()) {
      newcount = newcount + 1;
    }
  }
  if (newcount == oldcount) {
    target = "?";
  }
  if (newcount > oldcount) {
    oldcount = newcount;
    target = element;
  }
}console.log(target); */
