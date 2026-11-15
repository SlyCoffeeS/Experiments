const numbers = [];

while (true) {
    const num = Number(prompt("Enter number"));
    if (numbers.includes(num)) {
        alert("the number has already been given")
        break;
    }
    numbers.push(num);
}
numbers.sort((a, b) => a - b);
console.log(numbers);