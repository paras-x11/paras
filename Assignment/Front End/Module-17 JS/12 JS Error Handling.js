// 12. JavaScript Error Handling  
// Lab Assignment  
//  Task: 
// o Write a JavaScript program that attempts to divide a number by zero. Use try-
// catch to handle the error and display an appropriate error message.  

try {
  let num1 = 10;
  let num2 = 0;

  if (num2 === 0) {
    throw new Error("Cannot divide by zero!");
  }

  let result = num1 / num2;
  console.log(result);

} catch (error) {
  console.log(error.message);

} finally {
  console.log("Program executed");
}