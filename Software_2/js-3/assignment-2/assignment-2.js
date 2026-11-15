const count = Number(prompt("Number of participants"));
const names = [];

for (let i = 0; i < count; i++) {
    names.push(prompt(`Enter name ${i + 1}:`));
}

names.sort();

const target = document.querySelector('#target');
for (const name of names) {
    target.innerHTML += `<li>${name}</li>`;
}