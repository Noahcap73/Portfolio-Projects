console.log("hi");

const getUserChoice = (userInput) => {
  userInput = userInput.toLowerCase();
  if (userInput === "rock" || "paper" || "scissors") {
    return userInput;
  } else {
    console.log("ERROR! INPUT DID NOT MATCH: ROCK, PAPER, OR SCISSORS!");
  }
};

const getComputerChoice = () => {
  randomNumber = Math.floor(Math.random() * 3);
  if (randomNumber === 0) {
    return "rock";
  } else if (randomNumber === 1) {
    return "paper";
  } else if (randomNumber === 2) {
    return "scissors";
  }
};

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
    return "YOU FUCKIN TIED!";
  }
  if (userChoice === "rock") {
    if (computerChoice === "paper") {
      return "You lost to a bot...";
    } else {
      return "You won!";
    }
  }
  if (userChoice === "paper") {
    if (computerChoice === "scissors") {
      return "You lost to a bot...";
    } else {
      return "You won!";
    }
  }
  if (userChoice === "scissors") {
    if (computerChoice === "rock") {
      return "You lost to a bot...";
    } else {
      return "You won!";
    }
  }
};

const playGame = () => {
  const userChoice = getUserChoice("rock");
  const computerChoice = getComputerChoice();
  console.log(`You threw: ${userChoice}!`);
  console.log(`The bot threw: ${computerChoice}!`);
  console.log(determineWinner(userChoice, computerChoice));
};

playGame();
