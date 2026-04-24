// Lab Assignment  
//  Task: 
// o Write a JavaScript program to declare variables for different data types (string, 
// number, boolean, null, and undefined). 
// o Log the values of the variables and their types to the console using console.log(). 

 let number_var = 25
 let string_var = "Paras"
 let boolean_var = true
 let null_var = null
 let undefined_var = undefined


console.table(
    [
        {Value:number_var, DataType: typeof(number_var)},
        {Value:string_var, DataType: typeof(string_var)},
        {Value:boolean_var, DataType: typeof(boolean_var)},
        {Value:null_var, DataType: typeof(null_var)},
        {Value:undefined_var, DataType: typeof(undefined_var)},
    ]
)