#Import the random function
import random

#Create dice rolls list - generate 10 rolls in the range 1-6
dice_rolls = [random.randint(1, 6) for i in range(10)]
#Print the dice rolls list
print(f"Dice rolls: {dice_rolls}")
#Loop over each possible dice face (1 to 6)
for number in range(1, 7):
    #Count how many times a number appears in the rolls list
    number_count = dice_rolls.count(number)
    #Print the counter for each number
    print(f"{number} appeared {number_count} times")
#Declare variables for highest and lowest dice value and initialize them as the first value in the rolls list
highest_number = dice_rolls[0]
lowest_number = dice_rolls[0]
#Loop through the rolls and update the highest/lowest value
for roll in dice_rolls:
    #Set condition for the highest value
    if roll > highest_number:
        highest_number = roll
    #Set condition for the lowest value
    if roll < lowest_number:
        lowest_number = roll
#Print the values
print("Highest roll:", highest_number)
print("Lowest roll:", lowest_number)