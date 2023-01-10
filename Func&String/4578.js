selfNums = [];
//1부터 10000이 되는 셀프넘버 리스트 작성
for (let i = 1; i < 10000; i++) {
  selfNums.push(i);
}
function d(num) {
  //입력된 생성자를 연산
  const one = parseInt(num[0]);
  let two = parseInt(num[1]);
  let three = parseInt(num[2]);
  let four = parseInt(num[3]);
  two = two || 0;
  three = three || 0;
  four = four || 0;
  const result = parseInt(num) + one + two + three + four;

  return result;
}
for (let i = 1; i < 10000; i = i + 1) {
  const num = String(i);
  const index = selfNums.indexOf(d(num)); //중복되는값이 있어도 밑의 조건문으로 인해 pass
  if (index !== -1) selfNums.splice(index, 1);
}
for (let index = 0; index < selfNums.length; index++) {
  const element = selfNums[index];
  console.log(element);
}
