// The forecast today is 293 Kelvin
const kelvin = 0;

//Creating a celsius variable
let celsius = kelvin - 273;
console.log(celsius);

//Calculating Fahrenheit
let fahrenheit = celsius * (9 / 5) + 32;

//Using Math.floor to round down the fahrenheit temp
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

let newton = celsius * (33 / 100);

newton = Math.floor(newton);

console.log(`The temperature is ${newton} degrees Newton`);
