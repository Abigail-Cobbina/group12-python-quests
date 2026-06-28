#!/usr/bin/env python3
#Quest 13: The Maze Of Many Choices - conditional statements

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
else: 
    print("You need to improve your score.")