const fs = require("fs");

const data = fs.readFileSync("./test_1.txt",
    { encoding: 'utf8', flag: 'r' }).split("\n");

const maxOfEachColor = {
    red: 12,
    green: 13,
    blue: 14,
};

const solution = (str) => {
    const gameRound = str.split(":")[1].split(";");
    const gameId = str.split(":")[0].trim().split(" ")[1];

    let usedValues = {
        red: 0,
        blue: 0,
        green: 0,
    };

    gameRound.forEach((round) => {
        round.trim().split(",").forEach((roundValue) => {
            const [value, key] = roundValue.trim().split(" ");
            usedValues[key] = Math.max(usedValues[key], Number(value));
        })
    });

    const gameIsPossble = usedValues.red <= maxOfEachColor.red && usedValues.blue <= maxOfEachColor.blue && usedValues.green <= maxOfEachColor.green;

    if (gameIsPossble) {
        return Number(gameId);
    }

    console.log(usedValues);

    return false;
}

const result = data.map((str) => solution(str))
    .filter(item => item)
    .reduce((a, b) => a + b, 0);
    // .reduce((a, b) => a + b, 0);

console.log(result);
