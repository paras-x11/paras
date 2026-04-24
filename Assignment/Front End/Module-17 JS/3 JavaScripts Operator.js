// Lab Assignment  
//  Task: 
// o Create a JavaScript program to perform the following: 
//  Add, subtract, multiply, and divide two numbers using arithmetic operators. 
//  Use comparison operators to check if two numbers are equal and if one 
// number is greater than the other. 
//  Use logical operators to check if both conditions (e.g., a > 10 and b < 5) are true. 

// Two numbers
let a = 20;
let b = 5;

console.log("Numbers: a =", a, ", b =", b);

// ✅ Arithmetic operators
console.log("Addition (a + b) =", a + b);
console.log("Subtraction (a - b) =", a - b);
console.log("Multiplication (a * b) =", a * b);
console.log("Division (a / b) =", a / b);

// ✅ Comparison operators
console.log("Are a and b equal? (a == b):", a == b);
console.log("Is a greater than b? (a > b):", a > b);
console.log("Is a less than or equal to b? (a <= b):", a <= b);

// ✅ Logical operators
console.log("Both conditions true? (a > 10 && b < 5):", a > 10 && b < 5);
console.log("At least one condition true? (a > 10 || b < 5):", a > 10 || b < 5);
console.log("Negation of (a == b):", !(a == b));

// ✅ Equality Operators
a = 10, b = "10"
console.log("Loose Equality (a == b):", a == b, "→ compares values only (ignores type)");
console.log("Strict Equality (a === b):", a === b, "→ compares both value AND type");