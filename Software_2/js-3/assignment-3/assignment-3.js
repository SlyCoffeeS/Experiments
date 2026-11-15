const dogs=[]
for (let i = 0; i < 6; i++) {
    dogs[i] = prompt("Enter a dog's name:");
}
dogs.sort()
.reverse()
document.getElementById("target").innerHTML= "<ul><li>"+dogs.join("</li><li>")