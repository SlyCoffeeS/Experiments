const n1 = parseInt(prompt("number"));
const n2 = parseInt(prompt("number"));
const n3 = parseInt(prompt("number"));

document.querySelector("#target").innerHTML = `
sum: ${n1 + n2 + n3}
product: ${n1 * n2 * n3}
Average: ${(n1 + n2 + n3) / 3}
`;