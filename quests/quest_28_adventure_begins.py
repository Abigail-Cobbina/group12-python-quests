#!/usr/bin/env python3
# Quest 28: The Adventure Begins - functions

def cave():
    print("You step into a dark cave. Something glints on the ground.")
    choice = input("Do you pick it up or leave it? (Pick/Leave): ").lower()
    if choice == "pick":
        print("It's a magic sword! You are now a legendary hero. You win!")
    else:
        print("You leave it behind and walk away safely. Game over.")

def forest():
    print("You enter a dark forest. The path splits into two.")
    choice = input("Do you go left or right? (Left/Right): ").lower()
    if choice == "left":
        print("You hesitated and fall into a pit. Game over.")
    elif choice == "right":
        print("You find a treasure chest filled with gold! You win!")

def main():
    print("Welcome to the adventure!")
    location = input("Do you go to the cave or the forest? (Cave/Forest): ").lower()
    if location == "cave":
        cave()
    else:
        forest()

if __name__ == "__main__":
    main()
    