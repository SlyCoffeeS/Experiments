const sides = Number(prompt("Enter number of sides"));
function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

const rolls = [];
let currentRoll;

do {
    currentRoll = rollDice(sides);
    rolls.push(currentRoll);
} while (currentRoll !== sides);

document.getElementById("target").innerHTML="<ul><li>"+rolls.join("</li><li>")