// Lab Assignment  
//  Task 1: 
// o Write a JavaScript program to check if a number is positive, negative, or zero using 
// an if-else statement. 

const prompt = require("prompt-sync")();

let num = prompt("Enter your number: ");

num = Number(num)

if (!isNaN(num)){
    if (num > 0) {
        console.log(`${num} is positive number`);    
    }
    else if(num < 0) {
        console.log(`${num} is negative number`);    
    }
    else {
        console.log(`${num} is Zero`);    
    }
}
else {
    console.log(`${num} is Not A Number`);    
}

//  Task 2: 
// o Create a JavaScript program using a switch statement to display the day of the week 
// based on the user input (e.g., 1 for Monday, 2 for Tuesday, etc.). 

let dayNum = prompt("Enter a number (1-7) for the day of the week: ");
dayNum = Number(dayNum);

switch(dayNum) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    case 7:
        console.log("Sunday");
        break;
    default:
        console.log("Invalid input! Please enter a number between 1 and 7.");
        break;
}


