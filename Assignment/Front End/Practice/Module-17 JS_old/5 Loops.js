// Lab Assignment  
//  Task 1: 
// o Write a JavaScript program using a for loop to print numbers from 1 to 10. 

let num = 10

for (i=1; i<=num; i++){
    console.log(i)
}

//  Task 2: 
// o Create a JavaScript program that uses a while loop to sum all even numbers between 1 and 20. 

let n = 1;
let sum = 0;

while (n <= 20) {
    if (n % 2 === 0) {
        sum += n;  
    }
    n++;
}

console.log(`The sum of all even numbers between 1 and 20 is: ${sum}`);



//  Task 3: 
// o Write a do-while loop that continues to ask the user for input until they enter a number greater than 10. 