#!/usr/bin/python3
# Quest 15: The Nested Riddle - nested if statements

direction = input("Do you go left or right? ").lower()

if direction == "left":
    action = input("Do you swim or wait? ").lower()
    if action == "swim":
        print("You swim across and find a hidden treasure!")
    else:
        print("You wait too long and the cave floods. Game over.")
else:
    print("You go right and hit a dead end.")
