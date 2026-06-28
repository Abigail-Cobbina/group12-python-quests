#/bin/bash/env python3
# Start the counter at 0
count = 0

# Use a while loop that stops when the count reaches 5
while count < 5:
    print(f"Climbing stair step: {count}")
    
    # Increase the counter by 1 so the loop doesn't run forever
    count = count + 1

print("You reached the top of the staircase!")
