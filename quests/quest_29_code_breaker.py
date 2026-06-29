#!/usr/bin/python3

secret_code = 42

for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}/3: Enter the secret code: "))

    if guess == secret_code:
        print("Correct! You unlocked the secret.")
        break
    else:
        print("Incorrect guess.")

if guess != secret_code:
    print("Game over. You've used all 3 attempts.")
