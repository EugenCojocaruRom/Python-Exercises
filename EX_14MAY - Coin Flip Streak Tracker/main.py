import random
#Prompt user for number of flips
num_flips = int(input("Enter number of flips: "))
#Create list of random flips
flips = [random.choice(["H", "T"]) for _ in range(num_flips)]
#Print the list
print(f"Flips: {' '.join(flips)}")
#Declare variable (counter) for heads
heads = 0
#Declare variable (counter) for tails
tails = 0
#Loop through the flips list
for flip in flips:
    #Set condition for heads
    if flip == "H":
        #Increment heads counter
        heads += 1
    #Set condition for tails
    else:
        #Increment tails counter
        tails += 1
print(f"Heads: {heads}  |  Tails: {tails}")

#Declare variable (counter) for current streak
current_streak = 0
#Declare variable (counter) for best streak
best_streak = 0
#Declare variables for H and T streaks
best_H_streak = 0
best_T_streak = 0
#Declare variable for previous flip (for comparison)
prev_flip = None
#Loop through the flips list
for flip in flips:
    #Set condition for comparing the current flip to the previous flip
    if flip == prev_flip:
        #Increment current streak
        current_streak += 1
    #Set condition for current flip different from previous flip
    else:
        #Reset the current streak counter
        current_streak = 1
    # Set condition for comparing the current streak to the best streak
    if current_streak > best_streak:
        # Update the best streak
        best_streak = current_streak
        # Save which flip the streak belongs to (heads or tails)
        best_flip = flip
    #Set condition for comparing the current streak to the best heads streak
    if current_streak > best_H_streak and flip == "H":
        #Update the best streak
        best_H_streak = current_streak
    # Set condition for comparing the current streak to the best tails streak
    if current_streak > best_T_streak and flip == "T":
       # Update the best streak
       best_T_streak = current_streak
    #Update the previous flip (so that comparison is possible at the next iteration)
    prev_flip = flip
#Print the best streak
print(f"Best streak: {best_streak} ({best_flip})")
#Print the longest H and T streaks
print(f"Longest heads streak: {best_H_streak}")
print(f"Longest tails streak: {best_T_streak}")