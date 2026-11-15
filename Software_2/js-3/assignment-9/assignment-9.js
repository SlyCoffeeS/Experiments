function even(array){
    const evenArray = [];

    for (const num of array){
        if (num % 2 === 0){
            evenArray.push(num)
        }
    }
    return evenArray;
}
array=[2,3,4,5,6]
const evenNumberArray = even(array)
console.log(array, evenNumberArray)