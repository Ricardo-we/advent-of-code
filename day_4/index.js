const input = require("fs").readFileSync("./input1.txt", { encoding: "utf-8",flag: 'r' }).split("\n");

const solution = (card) => {
    const splittedCard =  card.replaceAll(/\s+/g, " ").split(":");
    let cardValues = splittedCard[1].split("|");
    const winningCards = cardValues[1].split(" ").filter((c) => c !== "");
    const winnedCards = [];
    cardValues = cardValues[0].replace(/\s+/g, " ").split(" ").filter((c) => c !== "");
    
    winningCards.forEach((winningCard) => {
        if(cardValues.includes(winningCard)) winnedCards.push(winningCard);
    })

    return winnedCards;
};


const result = input.map((card) => {
    let result = solution(card).map(c => 1)
    let points = 0;

    result.forEach(r => {
        if(points <= 0) points = 1;
        points += points;
    });

    return points / 2;
}) 

console.log(JSON.stringify(result));
console.log(result.reduce((a,b) => a + b, 0));