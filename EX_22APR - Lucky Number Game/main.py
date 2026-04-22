#Have a list of predefined numbers
winning_numbers = [4, 17, 23, 8, 42, 15]
#Display message for user
print("You must guess all 5 numbers to win! Good luck!")
#Declare empty list to collect the numbers entered by the user
user_numbers = []
#Loop through the range of 5
for i in range(5):
    #Prompt user to enter each number
    number = int(input(f"Enter number {i + 1}: "))
    #Add the entered number to the list
    user_numbers.append(number)
#Display the numbers entered by the user
print(f"You have entered the following numbers: {user_numbers}")
#Declare variable (counter) for number of matching guesses
matches = 0
#Loop through the user numbers
for number in user_numbers:
    #Set condition to check if the user number is among the winning numbers
    if number in winning_numbers:
        #Increment the counter
        matches += 1
#Print the result
if matches == 0:
    print(f"No matched numbers! Better luck next time!")
elif matches <= 2:
    print(f"Not bad, you matched {matches} numbers!")
elif matches <= 4:
    print(f"Nice job! You got {matches} matches — so close!")
else:
    print("JACKPOT! You got them all!")