const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let target = read[0];
let result = 0;
let count = parseInt(target / 5); //먼저 5개로 채운개수.
while (true) {
  let cur = target - count * 5; //현재 채워야하는 키로수
  if (cur % 3 == 0) {
    //5로 나누어떨어지거나 현재키로수가 3으로 나누어떨어진다면 통과
    result = count + cur / 3;
    break;
  }
  if (count === 0 && cur % 3 !== 0) {
    //5로도 3으로도 해결이 안되면 실패
    result = -1;
    break;
  }
  //아니면 5키로를 뺌
  count = count - 1;
}
console.log(result);
