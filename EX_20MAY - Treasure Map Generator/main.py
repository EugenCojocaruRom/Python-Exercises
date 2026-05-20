import random

#Prompt user for size of grid
n = int(input("Enter the size of the grid: "))
#Create the grid based on the user input
grid = [['.'] * n for _ in range(n)]

#Place @ in the grid
grid[0][0] = '@'

#Filter the positions in the grid that are different from the one occupied by @
available_spots = [(row, col) for row in range(n) for col in range(n) if not (row == 0 and col == 0)]
#Prompt user for number of hidden treasures
treasures = int(input("Enter the number of treasures: "))
#Set condition for checking that the number of treasures does not exceed the number of cells
if treasures > len(available_spots):
    #Print warning message
    print("Too many treasures for this grid size!")
else:
    #Pick the spots in the grid where the treasures will be placed
    treasure_spots = random.sample(available_spots, treasures)
    #Place the treasures ($) in the grid in random places
    for (row, col) in treasure_spots:
        grid[row][col] = '$'
    #Print the grid
    for i in grid:
        print("   ".join(i))

    #Print section separator
    print("<------------------------------------>")
    #Loop through the treasure spots to find the treasure coordinates
    for i, (row, col) in enumerate(treasure_spots):
        #Print the coordinates
        print(f"Treasure {i + 1} is at row {row} and column {col}.")

    #Count the treasures in the top half of the grid
    top_half = [(row, col) for row, col in treasure_spots if row < n // 2]
    #Count the treasures in the bottom half of the grid
    bottom_half = [(row, col) for row, col in treasure_spots if row >= n // 2]
    #Print section separator
    print("<------------------------------------->")
    #Print the 2 counters
    print(f"Treasures in the top half: {len(top_half)} | Treasures in the bottom half: {len(bottom_half)}")