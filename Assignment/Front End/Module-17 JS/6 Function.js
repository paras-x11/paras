// Lab Assignment  
//  Task 1: 
// o Write a function greetUser that accepts a user’s name as a parameter and displays a greeting message (e.g., "Hello, John!"). 

function greetUser(name){
    console.log(`Hello, ${name}!`)
}

// greetUser("ViVaN")



//  Task 2: 
// o Create a JavaScript function calculateSum that takes two numbers as parameters, adds them, and returns the result. 

function calculateSum(a, b){
    try{
        let x = Number(a)
        let y = Number(b)

        if(isNaN(x) || isNaN(y)){
            return `Enter valid Numbers!`
        }
        else{
            return x+y;
        }
    }
    catch (err){
        console.log("Error name:", err.name);
        console.log("Error message:", err.message);
        return `exception occured`
    }
}

res = calculateSum("34", "7a")
console.log(res)




// handlig specific exceptions
try {
    // Something that might fail
    notDefinedVariable + 1;  // ReferenceError
} catch (err) {
    console.log("Error name:", err.name);
    console.log("Error message:", err.message);
}
