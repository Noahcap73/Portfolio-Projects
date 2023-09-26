const team = {
  _players: [
    { firstName: "Crizia", lastName: "Samiano", age: 22 },
    { firstName: "Noah", lastName: "Capil", age: 21 },
    { firstName: "Collin", lastName: "Capil", age: 19 },
  ],

  _games: [
    { opponent: "Raiders", teamPoints: 56, opponentPoints: 32 },
    { opponent: "49ers", teamPoints: 12, opponentPoints: 17 },
    { opponent: "Golden Knights", teamPoints: 22, opponentPoints: 22 },
  ],

  get players() {
    return this._players;
  },

  get games() {
    return this._games;
  },

  addPlayer(newFirstName, newLastName, newAge) {
    let player = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge,
    };
    this.players.push(player);
  },

  addGame(newOpponent, newTeamPoints, newOpponentPoints) {
    let game = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints,
    };
    this.games.push(game);
  },
};

team.addPlayer("Bugs", "Bunny", 76);
team.addGame("Titans", 100, 98);

console.log(team.players);
console.log(team.games);
