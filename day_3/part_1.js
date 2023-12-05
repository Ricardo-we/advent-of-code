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
    let currentNumber = "";

    for (let j = 0; j < row.length; j++) {
        const char = row[j];

        if (isNumber(char)) {
            currentNumber += char;
            continue;
        } 
        
        if (currentNumber.length > 0 && !isNumber(row[j])) {
            const previousRowIndex = inputAsGrid.indexOf(row) - 1;
            const nextRowIndex = inputAsGrid.indexOf(row) + 1;
            const previousRow = inputAsGrid[previousRowIndex];
            const nextRow = inputAsGrid[nextRowIndex];
            const rightCharToNumber = row[j];
            const leftCharToNumber = row[j - currentNumber.length - 1];
            
            if (isSymbol(rightCharToNumber) || isSymbol(leftCharToNumber)) {
                subjacentNumbers.push(Number(currentNumber));
                currentNumber = ""
                continue;
            }


            for (let k = j - currentNumber.length - 1; k <= j + 1; k++) {
                const prevRowChar = previousRow ? previousRow[k] : ".";
                const nextRowChar = nextRow ? nextRow[k] : ".";
    
                if (isSymbol(prevRowChar) || isSymbol(nextRowChar)) {
                    subjacentNumbers.push(Number(currentNumber));
                    currentNumber = ""
                    break;
                }
            }
        }
        currentNumber = "";
    }
}

// console.log(JSON.stringify(subjacentNumbers, null, 2));
// console.log(subjacentNumbers.length);
const answer = 509115
console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0) === answer);
console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0) - answer);
console.log(subjacentNumbers.reduce((acc, curr) => acc + curr, 0));


