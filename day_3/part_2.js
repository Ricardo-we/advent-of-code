const fs = require('fs');
const input = fs.readFileSync('./input_1.txt', { encoding: 'utf8', flag: 'r' }).split('\n');

const inputAsGrid = input.map(item => {
    return item.split('');
});

const isNumber = (char) => char !== "" && !isNaN(Number(char));
const isSymbol = (char) => char !== "" && !!char && !isNumber(char) && char !== ".";

const subjacentNumbers = [];

for (let i = 0; i < inputAsGrid.length; i++) {
    const row = inputAsGrid[i];
    for (let j = 0; j < row.length; j++) {
        const char = row[j];

        if (char !== "*") continue;
        
        let numbersAround = 0;
        const previousRowIndex = inputAsGrid.indexOf(row) - 1;
        const nextRowIndex = inputAsGrid.indexOf(row) + 1;
        const previousRow = inputAsGrid[previousRowIndex];
        const nextRow = inputAsGrid[nextRowIndex];
        const rightCharToNumber = row[j + 1];
        const leftCharToNumber = row[j - 1];

        // console.log(previousRow.slice(j - 1, j + 2).join(""));
        // console.log(`${leftCharToNumber}${char}${rightCharToNumber}`);
        // console.log(nextRow.slice(j - 1, j + 2).join(""));
        // console.log("-------------------------========-------------------------");

        if (isNumber(rightCharToNumber) || isNumber(leftCharToNumber)) {
            numbersAround++;
        }

        for (let k = j - 1; k <= j + 2; k++) {
            const prevRowChar = previousRow ? previousRow[k] : ".";
            const nextRowChar = nextRow ? nextRow[k] : ".";

            
            if (isNumber(prevRowChar) || isNumber(nextRowChar)) {
                numbersAround++;
                // break;
            }
        }
        console.log(numbersAround);
        if(numbersAround === 2) 
            subjacentNumbers.push(Number(numbersAround));

    }
}

// console.log(JSON.stringify(subjacentNumbers, null, 2));
// console.log(subjacentNumbers.length);
// const answer = 509115
// console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0) === answer);
// console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0) - answer);
console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0));


