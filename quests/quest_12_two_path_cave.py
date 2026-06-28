#!/usr/bin/env python3

# Set the correct password
correct_password = "python123"

# Ask the user to enter a password
password = input("Enter the password: ")

# Check if the password is correct
if password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")
