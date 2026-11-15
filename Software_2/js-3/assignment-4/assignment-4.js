const number = [];
let input;

do {
    input = Number(prompt("Enter number (0 to stop)"));
    if (input !== 0) {
        number.push(input);
    }
}
while (input !== 0);
number.sort((a, b) => b - a);
console.log(number);