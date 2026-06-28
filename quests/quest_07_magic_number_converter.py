#/bin/bash/env python3

# Ask the user for their birth year
birth_year_text = input("Enter your birth year: ")

# Convert the string input into an integer (number)
birth_year = int(birth_year_text)

# Calculate approximate age using the current year (2026)
current_year = 2026
age = current_year - birth_year

# Print the final result
print(f"You are approximately {age} years old!")
