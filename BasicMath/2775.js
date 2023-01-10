const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().trim().split("\n");

const repeat = parseInt(read[0]);

for (let i = 1; i < repeat * 2; i = i + 2) {
  const k = parseInt(read[i]);
  const n = parseInt(read[i + 1]);

  let count = [];
  //0층 인원구하기
  for (let i = 1; i < n + 1; i++) {
    count.push(i);
  }
  //2층이상이면 계산
  if (k > 1) {
    //1층부터 k층까지
    for (let i = 0; i < k - 1; i++) {
      //n호까지
      let curRooms = [];
      let curCount = 0;
      for (let j = 0; j < n; j++) {
        curCount = curCount + count[j];
        curRooms.push(curCount);
      }

      count = curRooms;
    }
  }
  let finalCount = 0;
  count.map((cur) => (finalCount = finalCount + cur));
  console.log(finalCount);
}
/* 
1,7,28
1,6,21 7
1,5,15 6
1,4,10 5
1,3,6 4
1,2,3 3*/
