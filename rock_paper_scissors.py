import tkinter as tk
import random

# Class to manage Rock, Paper, Scissors Game
class RockPaperScissorsGame:
    # Initialize the game
    def __init__(self, root):
        # Set up the user interface
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.configure(bg='#e6e6e6')  # Set background color

        # Set initial user and computer scores
        self.user_score = 0
        self.comp_score = 0

        # Label to prompt user for their choice
        self.user_choice_label = tk.Label(root, text="Choose: Rock, Paper, or Scissors", bg='#e6e6e6')
        self.user_choice_label.pack()

        # Buttons for user choices
        self.rock_button = tk.Button(root, text="Rock", command=self.choose_rock, bg='#66c2ff')  # Set button color
        self.rock_button.pack()

        self.paper_button = tk.Button(root, text="Paper", command=self.choose_paper, bg='#99ff99')  # Set button color
        self.paper_button.pack()

        self.scissors_button = tk.Button(root, text="Scissors", command=self.choose_scissors, bg='#ffcc99')  # Set button color
        self.scissors_button.pack()

        # Labels for game result and score
        self.result_label = tk.Label(root, text="", bg='#e6e6e6')
        self.result_label.pack()

        self.score_label = tk.Label(root, text=f"User: {self.user_score} | Computer: {self.comp_score}", bg='#e6e6e6')
        self.score_label.pack()

    # Handle user choice "Rock" button click
    def choose_rock(self):
        self.play("rock")

    # Handle user choice "Paper" button click
    def choose_paper(self):
        self.play("paper")

    # Handle user choice "Scissors" button click
    def choose_scissors(self):
        self.play("scissors")

    # Simulate the game based on user choice
    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)
        result = self.determine_winner(user_choice, comp_choice)
        self.result_label.config(text=result)

        # Update scores
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.comp_score += 1
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.comp_score}")

    # Determine game winner
    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            return "You win!"
        else:
            return "Computer wins!"

# Create and run the game
root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()

