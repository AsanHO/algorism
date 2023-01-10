const fs = require("fs");
const read = fs.readFileSync("example.txt").toString().trim().split("\n");
const repeat = parseInt(read[0]);
//단어 순회
count = 0;
for (let i = 1; i < repeat + 1; i++) {
  let group = [];
  const word = read[i];
  let isTrue = true;
  label: for (let j = 0; j < word.length; j++) {
    // 단어 전개
    if (!group.includes(word[j])) {
      group.push(word[j]);
    } else {
      if (word[j] !== word[j - 1]) {
        //연속된 단어가 아니면 탈락
        isTrue = false;
        break label;
      }
    }
  }
  isTrue && (count = count + 1);
}
console.log(count);
