#!/usr/bin/python3
# Quest 30: The Reflective Scribe - commented versions of 3 previous quests


# --- Quest 5: The Echoing Cave ---
player_health = 100               # set starting health
player_health = player_health - 25  # monster attack reduces health by 25
player_health = player_health + 10  # potion restores 10 health
print(f"Final health: {player_health}")  # show the updated value


# --- Quest 20: The Even Number Forager ---
for number in range(1, 21):       # loop through numbers 1 to 20
    if number % 2 == 0:           # % 2 == 0 means the number is even
        print(number)             # only print even numbers


# --- Quest 25: The Number Wizard ---
secret = 7                        # the number the user must guess
while True:                       # loop until they guess right
    guess = int(input("Guess the secret number (1-10): "))  # convert input to int
    if guess < secret:            # guess is below the target
        print("Too low!")
    elif guess > secret:          # guess is above the target
        print("Too high!")
    else:                         # guess matches the secret
        print("Correct! You win!")
        break                     # exit the loop
