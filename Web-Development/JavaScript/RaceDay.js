//Writing a program that will register runners for a race and give them instructions

//Creating a raceNumber variable
let raceNumber = Math.floor(Math.random() * 1000);

//Creating a register time variable
const registerTimeEarly = true;

//Creating a runner's age variable
let runnerAge = 22;

//If runner registered early and is over 18, add 1000 to their raceNumber
if (registerTimeEarly && runnerAge > 18) {
  raceNumber += 1000;
}

//Control flow to assign Runners a time to race and telling them their raceNumber
if (runnerAge > 18 && registerTimeEarly) {
  console.log(`Runner: ${raceNumber}, your race will begin at 9:30 am!`);
} else if (runnerAge > 18 && !registerTimeEarly) {
  console.log(`Runner: ${raceNumber}, your race will begin at 11:00 am!`);
} else if (runnerAge < 18) {
  console.log(`Runner: ${raceNumber}, your race will begin at 12:30 pm!`);
} else if (runnerAge === 18) {
  console.log("Please see the registration desk");
}
