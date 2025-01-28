import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").lower()

random = random.choice(choices)

print(f"You chose: {user}")
print(f"Computer chose: {random}")

if user == random:
    print("It's a tie!")
elif (user == "rock" and random == "scissors") or \
     (user == "scissors" and random == "paper") or \
     (user == "paper" and random == "rock"):
    print("You win!")
else:
    print("You lose!")
