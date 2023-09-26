const getSleepHours = (day) => {
  switch (day) {
    case "monday":
      return 7;
    case "tuesday":
      return 6;
    case "wednesday":
      return 7;
    case "thursday":
      return 8;
    case "friday":
      return 9;
    case "saturday":
      return 10;
    case "sunday":
      return 9;
  }
};

//Using an implicit return. No curly brackets
const getActualSleepHours = () =>
  getSleepHours("monday") +
  getSleepHours("tuesday") +
  getSleepHours("wednesday") +
  getSleepHours("thursday") +
  getSleepHours("friday") +
  getSleepHours("saturday") +
  getSleepHours("sunday");

const getIdealSleepHours = () => {
  let idealHours = 9; //enter your ideal hours of sleep per night here
  return idealHours * 7;
};

const calculateSleepDebt = () => {
  let actualSleepHours = getActualSleepHours();
  let idealSleepHours = getIdealSleepHours();
  if (actualSleepHours === idealSleepHours) {
    console.log("You got the perfect amount of sleep");
  } else if (actualSleepHours > idealSleepHours) {
    let overSleepHours = actualSleepHours - idealSleepHours;
    console.log(`You got ${overSleepHours} more hours of sleep than needed!`);
  } else if (actualSleepHours < idealSleepHours) {
    let lessSleepHours = idealSleepHours - actualSleepHours;
    console.log(`You should sleep ${lessSleepHours} more hours!`);
  }
};

calculateSleepDebt();
