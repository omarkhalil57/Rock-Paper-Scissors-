import tkinter as tk
import random

player_score = 0
computer_score = 0


def play(choice):
    global player_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)

    computer_label.config(
        text=f"Computer's Choice: {computer}"
    )

    if choice == computer:
        result.config(text="Draw!", fg="yellow")

    elif (
        (choice == "Rock" and computer == "Scissors")
        or
        (choice == "Paper" and computer == "Rock")
        or
        (choice == "Scissors" and computer == "Paper")
    ):
        result.config(text="You won!", fg="lightgreen")
        player_score += 1

    else:
        result.config(text="Computer won!", fg="red")
        computer_score += 1

    score.config(
        text=f"You: {player_score}     Computer: {computer_score}"
    )

def new_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    result.config(text="Choose!", fg="yellow")
    computer_label.config(text="Computer Choice: -")
    score.config(text="You: 0     Computer: 0")

# Window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x300")
window.config(bg="navy")


# Title
title = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="navy",
    fg="white"
)
title.pack(pady=20)


# Result
result = tk.Label(
    window,
    text="Choose!",
    font=("Arial", 20, "bold"),
    bg="navy",
    fg="yellow"
)
result.pack(pady=10)


# Computer choice
computer_label = tk.Label(
    window,
    text="Computer Choice: -",
    font=("Arial", 14),
    bg="navy",
    fg="white"
)
computer_label.pack(pady=10)


# Buttons
rock_button = tk.Button(
    window,
    text="Rock",
    font=("Arial", 14),
    bg="lightblue",
    fg="black",
    command=lambda: play("Rock")
)
rock_button.pack(pady=5)


paper_button = tk.Button(
    window,
    text="Paper",
    font=("Arial", 14),
    bg="lightblue",
    fg="black",
    command=lambda: play("Paper")
)
paper_button.pack(pady=5)


scissors_button = tk.Button(
    window,
    text="Scissors",
    font=("Arial", 14),
    bg="lightblue",
    fg="black",
    command=lambda: play("Scissors")
)
scissors_button.pack(pady=5)


# Score
score = tk.Label(
    window,
    text="You: 0     Computer: 0",
    font=("Arial", 14, "bold"),
    bg="navy",
    fg="white"
)
score.pack(pady=15)


# New game
new_game_button = tk.Button(
    window,
    text="New Game",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="navy",
    command=new_game
)
new_game_button.pack()


window.mainloop()