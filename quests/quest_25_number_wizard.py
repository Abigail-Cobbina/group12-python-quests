#!/usr/bin/python3
# Quest 25: The Number Wizard - guessing game with hints

secret = 7

while True:
    guess = int(input("Guess the secret number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You win!")
        break
