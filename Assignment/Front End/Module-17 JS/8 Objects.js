// Lab Assignment  
//  Task: 
// o Create a JavaScript object car with properties brand, model, and year. Use JavaScript to: 
//  Access and print the car’s brand and model. 
//  Update the year property. 
//  Add a new property color to the car object. 

// Create object
let car = {
  brand: "Toyota",
  model: "Camry",
  year: 2020
};
console.log("Old Car:", car);

// Access and print brand & model
console.log("Brand:", car.brand);
console.log("Model:", car.model);

// Update year
car.year = 2023;

// Add new property
car.color = "Black";
// car['color'] = "Black";

// Print updated object
console.log("Updated Car:", car);