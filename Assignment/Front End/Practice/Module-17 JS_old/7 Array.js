// Lab Assignment  
//  Task 1: 
// o Declare an array of fruits (["apple", "banana", "cherry"]). Use JavaScript to: 
//  Add a fruit to the end of the array. 
//  Remove the first fruit from the array. 
//  Log the modified array to the console. 
//  Task 2: 
// o Write a program to find the sum of all elements in an array of numbers. 
 

fruits = ['apple', 'banana', 'cherry']
console.log(fruits)

fruits.push('watermelon')
console.log(fruits)

fruits.shift()
console.log(fruits)


numbers = [12, 54, 78, 92, 23, 45]

let sum = 0

for (i=0 ; i<(numbers.length); i++){
    sum += numbers[i]
}

console.log(sum)


numbers = [12, 54, 78, 92, 23, 45]
let sum1 = 0
numbers.forEach(element => {
    sum1 += element
});
console.log(sum1)
