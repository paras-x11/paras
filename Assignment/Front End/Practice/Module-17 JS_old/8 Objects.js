// Lab Assignment  
//  Task: 
// o Create a JavaScript object car with properties brand, model, and year. Use JavaScript 
// to: 
//  Access and print the car’s brand and model. 
//  Update the year property. 
//  Add a new property color to the car object. 


car = {
    brand: 'Audi',
    model: 'A6',
    year: '2004'
}

console.log(car.brand, car.model, car.year);

car.year = '2006'
console.log(car.brand, car.model, car.year);

car.color = 'Red'
console.log(car);


// Create a JavaScript object
let car = {
  brand: "Toyota",
  model: "Corolla",
  year: 2020
};

// 1. Access and print brand and model
console.log("Brand:", car.brand);   // Toyota
console.log("Model:", car.model);   // Corolla

// 2. Update the year property
car.year = 2023;
console.log("Updated Year:", car.year); // 2023

// 3. Add a new property 'color'
car.color = "Red";
console.log("Color:", car.color);   // Red

// Print the whole object to see changes
console.log("Car Object:", car);
