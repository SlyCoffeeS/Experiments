function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

const rolls = [];
let currentRoll;

do {
    currentRoll = rollDice();
    rolls.push(currentRoll);
} while (currentRoll !== 6);

document.getElementById("target").innerHTML="<ul><li>"+rolls.join("</li><li>")