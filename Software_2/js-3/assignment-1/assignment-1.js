const numbers = [];

for (let i = 1; i <= 5; i++) {
    const input = prompt(`Enter number {i}`)
    numbers.push(Number(input));
}
for (let i = numbers.length -1; i >= 0; i--) {
    console.log(numbers[i]);
}