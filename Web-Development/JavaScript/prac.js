const animals = ["panda", "turtle", "giraffe", "hippo", "sloth", "human"];

const convertToBaby = (array) => {
  let baby = [];
  for (let i = 0; i < array.length; i++) {
    baby.push(`baby ${array[i]}`);
  }
  return baby;
};

console.log(convertToBaby(animals));
