const fs = require("fs");
const input = fs
  .readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" })
  .split("\n");

const inputAsGrid = input.map((item) => {
  return item.split("");
});

const isNumber = (char) => char !== "" && !isNaN(Number(char));
const isSymbol = (char) =>
  char !== "" && !!char && !isNumber(char) && char !== ".";

for (let i = 0; i < inputAsGrid.length; i++) {
  const row = inputAsGrid[i];

  let coords = [];
  for (let j = 0; j < inputAsGrid[i].length; j++) {
    const column = inputAsGrid[i][j];
    if (column !== "*") continue;

    for (let y of [i - 1, i, i + 1]) {
      for (let x of [j - 1, j, j + 1]) {
        if (
          y < 0 ||
          x < 0 ||
          y > inputAsGrid.length ||
          y > inputAsGrid[x].length ||
          !isNumber(inputAsGrid[x][y])
        )
          continue;

        while (x > 0 && isNumber(inputAsGrid[y][x - 1])) {
          x -= 1;
        }
        coords.push([y, x]);
      }
    }
  }

  if (coords.length !== 2) continue;

  const result = [];

  for (let i = 0; i < coords.length; i++) {
    let [y, x] = coords[i];
    let currentNumber = "";

    while (x < inputAsGrid[y].length && isNumber(inputAsGrid[y][x])) {
      currentNumber += inputAsGrid[y][x];
      x += 1;
    }

    result.push(Number(currentNumber));
  }

  console.log(result[0] * result[1]);
}


// console.log(JSON.stringify(subjacentNumbers, null, 2));
// console.log(subjacentNumbers.length);
// const answer = 509115
// console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0) === answer);
// console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0) - answer);
// console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0));
