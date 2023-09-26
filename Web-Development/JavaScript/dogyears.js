// Variable for my age
let myAge = 21;

//Variable with the value of 2
let earlyYears = 2;

earlyYears *= 10.5;

//Subracting 2 from myAge to get laterYears
let laterYears = myAge - 2;

//Multiplying laterYears by 4 to get number of dog years
laterYears *= 4;

console.log(laterYears);
console.log(earlyYears);

//adding earlyYears and laterYears to get myAgeInDogYears
let myAgeInDogYears = earlyYears + laterYears;

//Writing my name as a string and using the built-in method ".toLocaleLowerCase" on it.
myName = "Noah Capil".toLocaleLowerCase();

console.log(
  `My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`
);
