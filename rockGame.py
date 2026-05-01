import random

print("===== ROCK PAPER SCISSORS GAME =====")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user == "exit":
        print("Game Over 👋")
        print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You choose:", user)
    print("Computer choose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win! 🎉")
        user_score += 1

    else:
        print("Computer wins! 😢")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")