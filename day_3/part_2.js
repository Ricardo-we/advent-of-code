const fs = require("fs");
const input = fs
	.readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" })
	.split("\n");

const inputAsGrid = input.map((item) => {
	return item.split("");
});

const isNumber = (char) => char !== "" && !isNaN(Number(char));
let total = 0;

for (let i = 0; i < inputAsGrid.length; i++) {
	const coords = [];

	for (let j = 0; j < inputAsGrid[i].length; j++) {
		const column = inputAsGrid[i][j];
		if (column !== "*") continue;

		for (let y of [i - 1, i, i + 1]) {
			for (let x of [j - 1, j, j + 1]) {
				if (
					y < 0 ||
					x < 0 ||
					y > inputAsGrid.length ||
					x > inputAsGrid[x].length ||
					!isNumber(inputAsGrid[y][x]) //||
					// !isNumber(inputAsGrid[y][x - 1])
				) {
					continue;
				}

				while (x > 0 && isNumber(inputAsGrid[y][x - 1])) {
					x -= 1;
				}

				if (
					!coords.find(
						(coord) => JSON.stringify(coord) === JSON.stringify([y, x])
					)
				) {
					coords.push([y, x]);
				}
			}
		}
	}

	if (coords.length !== 2) continue;

	let result = [];

	for (let i = 0; i < coords.length; i++) {
		let [y, x] = coords[i];
		let currentNumber = "";

		while (x < inputAsGrid[y].length && isNumber(inputAsGrid[y][x])) {
			currentNumber += inputAsGrid[y][x];
			x += 1;
		}

		result.push(Number(currentNumber));
	}

	total += result[0] * result[1];
}

console.log(total);
