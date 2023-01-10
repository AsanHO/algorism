/* 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면,
그 수를 한수라고 한다. 99까지는 한수 111 123 135 147 159 210
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
*/
const fs = require("fs");

const read = fs
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const countlist = [];
function func(num) {
  const nnum = parseInt(num);
  if (parseInt(nnum) < 100) {
    countlist.push(num);
    return;
  }
  const one = parseInt(num[0]);
  let two = parseInt(num[1]);
  let three = parseInt(num[2]);
  let four = parseInt(num[3]);
  two = two || 0;
  three = three || 0;
  four = four || 0;
  if (three - two === two - one) {
    countlist.push(num);
  }
}
for (let index = read[0]; index > 0; index = index - 1) {
  func(String(index));
}
console.log(countlist.length);
