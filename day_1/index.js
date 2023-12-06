const data = require('fs').readFileSync("./input.txt", 'utf-8').split("\n");

const numberValueByName = {
  zero: 0,
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
};

const solution = (data) => {
  let numberValues = Array.from(
    data.matchAll(/(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))/g)
    // data.matchAll(/(?=(\d))/g)
  ).map((value) => {
    console.log(value);
    return value[1].length > 1 ? numberValueByName[value[1]] : value[1];
  });
  let firstDigit = String(numberValues[0]);
  let lastDigit = String(numberValues?.at(-1));

  return Number(firstDigit + lastDigit);
};

// console.log(solution("1oneightfs"));
// console.log(solution("eightwothree"));
// console.log(solution("abcone2threexyz"));
// console.log(solution("xtwone3four"));
// console.log(solution("4nineeightseven2"));
// console.log(solution("zoneight234"));
// console.log(solution("7pqrstsixteen"));

let result = data.map((item) => solution(item));
console.log(JSON.stringify(result));
result = result.reduce((a, b) => a + b);
console.log(result);
