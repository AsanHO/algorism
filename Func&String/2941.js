const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const read = fs.readFileSync(filePath).toString().split("\n");

const source = read[0];
let count = 0;

const addCount = () => (count = count + 1);
for (let i = 0; i < source.length; i++) {
  const e = source[i];
  //č || ć
  if (e === "c") {
    if (source[i + 1] == "=") {
      addCount();
      i = i + 1;
    } else if (source[i + 1] == "-") {
      addCount();
      i = i + 1;
    } else {
      addCount();
    }
  }
  //dž || đ
  else if (e === "d") {
    if (source[i + 1] == "z") {
      if (source[i + 2] == "=") {
        addCount();
        i = i + 2;
      } else {
        addCount();
      }
    } else if (source[i + 1] == "-") {
      addCount();
      i = i + 1;
    } else {
      addCount();
    }
  }
  //lj
  else if (e === "l") {
    if (source[i + 1] == "j") {
      addCount();
      i = i + 1;
    } else {
      addCount();
    }
  }
  //nj
  else if (e === "n") {
    if (source[i + 1] == "j") {
      addCount();
      i = i + 1;
    } else {
      addCount();
    }
  }
  // š
  else if (e === "s") {
    if (source[i + 1] == "=") {
      addCount();
      i = i + 1;
    } else {
      addCount();
    }
  }
  // ž
  else if (e === "z") {
    if (source[i + 1] == "=") {
      addCount();
      i = i + 1;
    } else {
      addCount();
    }
  } else {
    addCount();
  }
}
console.log(count);
//dz=
