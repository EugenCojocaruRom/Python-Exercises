#Print header and separator
print("<-- Bingo Card Validator -->")
print("----------------------------")

#Set up the Bingo card (5x5 grid)
card = [
    [ 3, 17, 32, 48, 61],
    [ 8, 22, 39, 51, 67],
    [12, 27, 45, 55, 72],  # middle row/column intersect at 45
    [ 5, 19, 34, 49, 63],
    [14, 25, 41, 58, 70]
]

#Create empty list to hold the user's input
player_input = []
#Outer loop keeps collecting numbers until the user types "done"
while True:
    #Create loop to validate the user's input
    while True:
        try:
            #Prompt user to enter a number from 1 to 75
            number = input("Please enter a number (1 - 75): ")
            #Check for the sentinel value first, before checking emptiness
            if number == "done":
                break
            if number == "":
                print("The value cannot be empty. Please try again.")
                continue
            #Check that the number entered is in the 1-75 range
            if int(number) not in range(1, 76):
                print("The number must be between 1 and 75.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #If the sentinel was entered, stop the outer loop too — before appending
    if number == "done":
        break
    #Warn if this number was already entered before adding it
    if int(number) in player_input:
        print(f"You've already entered {number} — it won't be counted again.")
        continue
    #Add the validated number to the player input list
    player_input.append(int(number))

#Build the "marked" version of the card -> replace the number with "X" if it was called, otherwise keep the number as is
marked_card = [["X" if value in player_input else value for value in row] for row in card]

#Print the card, row by row, with row numbers
print("\nCurrent card:")
for row_number, row in enumerate(marked_card, start=1):
    print(f"Row {row_number}: {row}")

    #Check if the user has BINGO
#Declare variable for 'bingo' and set it to false
bingo = False
#Declare variable for the winning line and initialize it as 'none'
winning_line = None
#Check the rows -> a row wins if every value in it is "X"
for row_number, row in enumerate(marked_card, start=1):
    if all(value == "X" for value in row):
        bingo = True
        winning_line = f"Row {row_number}"
        break

#Check the columns -> each column is built by retrieving the same index from every row
if not bingo:
    for col_number in range(5):
        column = [marked_card[row_number][col_number] for row_number in range(5)]
        if all(value == "X" for value in column):
            bingo = True
            winning_line = f"Column {col_number + 1}"
            break

#Check the 2 diagonals
if not bingo:
    diagonal_1 = [marked_card[i][i] for i in range(5)]
    diagonal_2 = [marked_card[i][4 - i] for i in range(5)]
    if all(value == "X" for value in diagonal_1):
        bingo = True
        winning_line = "Diagonal (top-left to bottom-right)"
    elif all(value == "X" for value in diagonal_2):
        bingo = True
        winning_line = "Diagonal (top-right to bottom-left)"

#Check for BLACKOUT (every cell marked)
blackout = all(value == "X" for row in marked_card for value in row)

#Print the summary of the card
marked_count = sum(value == "X" for row in marked_card for value in row)
print(f"\n{marked_count} out of 25 numbers marked.")
if blackout:
    print("BLACKOUT! Every square on the card is marked!")
elif bingo:
    print(f"BINGO! Winning line: {winning_line}")
else:
    print("No BINGO yet — keep playing.")