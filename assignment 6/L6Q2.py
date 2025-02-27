import random

class RockPaperScissors:
    def __init__(self, rounds=1):
        self.rounds = rounds
        self.wins = 0
        self.round_number = 1
        self.res = []
        self.choice = ["rock", "paper", "scissor"]
        
    def play(self):
        a = random.choice(self.choice)
        b = input("Enter your choice (rock, paper, or scissor): ").lower()

        # Handle invalid input
        if b not in self.choice:
            print("Invalid choice, choose again:")
            return self.play()  # Recurse if invalid choice
        
        print(f"Computer's choice = {a}\nYour choice = {b}")

        # Check for win, loss, or tie
        if b == a:
            return (f"Round {self.round_number}", "It's a tie!")
        elif (b == 'rock' and a == 'scissor') or (b == 'scissor' and a == 'paper') or (b == 'paper' and a == 'rock'):
            self.wins += 1
            return (f"Round {self.round_number}", "You win!")
        else:
            return (f"Round {self.round_number}", "Computer wins!")

    def start(self):
        for i in range(self.rounds):
            print(f"Round {self.round_number}:")
            self.res.append(self.play())
            self.round_number += 1  # Update round number after each round
        return self.res

# Starting the game
player1 = RockPaperScissors(int(input("Number of rounds to play: ")))
results = player1.start()

# Output the results
for result in results:
    print(result[0], "->", result[1])

print(f"Number of wins: {player1.wins}")
