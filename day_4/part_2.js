const input = require("fs")
  .readFileSync("./input2.txt", { encoding: "utf-8", flag: "r" })
  .split("\n");

const copies = {};

const getCardId = (splittedCard) => splittedCard[0].split(" ")[1];

const solution = (card, index) => {
  const splittedCard = card.replaceAll(/\s+/g, " ").split(":");
  const cardId = getCardId(splittedCard);
  let cardValues = splittedCard[1].split("|");
  const winningCards = cardValues[1].split(" ").filter((c) => c !== "");
  const winnedCards = [];

  cardValues = cardValues[0]
    .replace(/\s+/g, " ")
    .split(" ")
    .filter((c) => c !== "");

  winningCards.forEach((winningCard) => {
    if (cardValues.includes(winningCard)) {
      winnedCards.push(winningCard);
    }
  });

  if (winnedCards.length > 0) {
    for (let i = 1; i <= winnedCards.length; i++) {
      const nextCard = input[index + i] ?? input.at(-1);
      copies[cardId] = nextCard ? [nextCard] : [...copies[cardId], nextCard];
      // input.splice(i, 0, nextCard);
      input.push(nextCard);
    }
  }

  return copies;
};

const main = () => {
  let i = 0;
  let copies = [];

  while (i < input.length) {
    const card = input[i];
    solution(card, i);
    i++;
  }

  return input.length;
};

const result = main();


console.log(input);

console.log(copies);

console.log(result);
console.log(input.length);
