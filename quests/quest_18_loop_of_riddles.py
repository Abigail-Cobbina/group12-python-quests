#!/usr/bin/env python3
# Quest 18: The Loop Of Riddles - loops

secret_number = 7
guess = int(input("Guess the secret number (between 1 and 10): "))
while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the secret number (between 1 and 10): "))

print("Congratulations! You've guessed the secret number!")