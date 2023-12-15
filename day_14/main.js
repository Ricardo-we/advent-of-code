let data = require("fs").readFileSync("./input.txt", { encoding: "utf-8" }).split("\n");
console.log(data);
data = data.map(line => (line.endsWith("\r") ? line.slice(0, line.length - 1) : line).split(""));

let moves = 0;

for(let i = 0; i < data.length; i++){
    const row = data[i];

    if (i <= 0) continue;

    for (let j = 0; j < row.length; j++){
        let i_ = i;
        let col = row[j];
        let prevRowCol = data[i - 1][j];

        while (col === "O" && prevRowCol === "."){
            data[i_ - 1][j] = col;
            data[i_][j] = prevRowCol;
            i_--;

            if(i_ <= 0) break;
            
            col = data[i_][j];
            prevRowCol = data[i_ - 1][j];
        }
        
    }
}

let load = data.length;
for(const row of data){
    moves += row.filter(col => col === "O").length * load;
    load--;
}

console.log(data.map(item => item.join("")).join("\n"));
console.log(moves);