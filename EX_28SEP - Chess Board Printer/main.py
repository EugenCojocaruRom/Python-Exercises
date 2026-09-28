#Print header and separator
print("<-- Chess Board Printer -->")
print("---------------------------")

#Prompt the user to enter squares, and keep asking until at least one is valid
while True:
    user_input = input("Enter squares (like b2 d4 g7): ") #Example: a1 a1 c3 h7 f9 e5 e5 f3 b6 i10 hello a
    #Normalize: lowercase, then split into a list of words
    squares = user_input.lower().split()
    #Valid = exactly 2 characters, letter a-h, number 1-8
    marked = [sq for sq in squares
              if len(sq) == 2 and sq[0] in "abcdefgh" and sq[1] in "12345678"]
    #Invalid = everything that is not in the valid list
    invalid = [sq for sq in squares if sq not in marked]
    if invalid:
        print(f"Ignored invalid squares: {invalid}")
    if marked:
        break
    print("No valid squares entered. Please try again.")

#Remove duplicate squares (keeping the original order)
marked = list(dict.fromkeys(marked))
#Convert each square (e.g. c3) into a (col, row) pair
marked_positions = []
for sq in marked:
    col = "abcdefgh".index(sq[0])
    row = 8 - int(sq[1])
    marked_positions.append((col, row))

# marked_positions = [("abcdefgh".index(sq[0]), 8 - int(sq[1])) for sq in marked] --> using list comprehension

#Declare variable for dark squares and initialize it to 0
dark_count = 0
#Declare variable for light squares and initialize it to 0
light_count = 0
#Loop for each row in range 8
for row in range(8):
    #Create empty list to hold the board lines
    line = []
    #Loop for each column in range 8
    for col in range(8):
        #Store the color check once to reuse it
        is_dark = (row + col) % 2 == 1
        #Set conditions for checking if a square is dark or light
        if is_dark:
            #Increment the dark squares count if dark
            dark_count += 1
        else:
            #Increment the light squares count if light
            light_count += 1
        #Set condition for checking if a selected square is in the marked positions list
        if (col, row) in marked_positions:
            line.append("X")
        #Set conditions for setting a square as dark (#) or light (.)
        elif is_dark:
            line.append("#")
        else:
            line.append(".")
    print(" ".join(line))

print()
#Create empty list to store the marked dark squares
marked_dark = []
#Create empty list to store the marked light squares
marked_light = []
#Loop through the marked list with enumerate
for i, sq in enumerate(marked):
    col, row = marked_positions[i]
    #Set conditions for checking if a square is dark or light
    if (row + col) % 2 == 1:
        #Add the marked square to the marked on dark list
        marked_dark.append(sq)
    else:
        #Add the marked square to the marked on light list
        marked_light.append(sq)

#Print the lists
print(f"Dark squares: {dark_count}")
print(f"Light squares: {light_count}")
if marked_dark:
    print(f"Marked on dark squares: {', '.join(marked_dark)}")
else:
    print("Marked on dark squares: none")
if marked_light:
    print(f"Marked on light squares: {', '.join(marked_light)}")
else:
    print("Marked on light squares: none")