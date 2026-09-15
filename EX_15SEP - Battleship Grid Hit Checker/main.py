#Print header and separator
print("<-- Battleship Grid Hit Checker -->")
print("-----------------------------------")

import random

#Build the grid
GRID_SIZE = 5

#Start with an empty grid of "." (water)
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

#Get all possible (row, col) coordinates as a flat list
all_coords = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)]

#Randomly choose 3 unique coordinates to place ships on
ship_coords = random.sample(all_coords, 3)

#Place the ships on the grid
for row, col in ship_coords:
    grid[row][col] = "S"

#DISPLAY FUNCTION
def display_grid(grid):
    #Print column headers (0 to GRID_SIZE - 1)
    header = "   " + " ".join(str(c) for c in range(GRID_SIZE))
    print(header)

    #Use enumerate() to get the row index alongside each row
    for row_index, row in enumerate(grid):
        #Hide ships that haven't been hit yet ("S" shows as ".")
        display_row = [cell if cell != "S" else "." for cell in row]
        print(f"{row_index}  " + " ".join(display_row))
    print()

#GAME LOOP
shots_taken = 0
hits = 0

print("Welcome to Battleship! Try to sink all 3 ships.\n")
display_grid(grid)

while True:
    #Count remaining ship cells using a flattened list comprehension
    remaining_ships = len([cell for row in grid for cell in row if cell == "S"])

    if remaining_ships == 0:
        print(f"You sank all the ships in {shots_taken} shots!")
        print(f"Hit ratio: {hits}/{shots_taken} ({hits / shots_taken:.1%})")
        break

    #Validate row input
    while True:
        row_input = input(f"Enter row (0-{GRID_SIZE - 1}): ").strip()
        try:
            row = int(row_input)
            if 0 <= row < GRID_SIZE:
                break
            else:
                print(f"Row must be between 0 and {GRID_SIZE - 1}.")
        except ValueError:
            print("Please enter a valid number.")

    #Validate column input
    while True:
        col_input = input(f"Enter column (0-{GRID_SIZE - 1}): ").strip()
        try:
            col = int(col_input)
            if 0 <= col < GRID_SIZE:
                break
            else:
                print(f"Column must be between 0 and {GRID_SIZE - 1}.")
        except ValueError:
            print("Please enter a valid number.")

    cell = grid[row][col]

    #Handle the shot
    if cell in ("X", "O"):
        print("You already fired there! Try a different cell.\n")
        continue  #Doesn't count as a shot, loop back without incrementing

    shots_taken += 1

    if cell == "S":
        grid[row][col] = "X"
        hits += 1
        print("Hit!\n")
    else:
        grid[row][col] = "O"
        print("Miss!\n")

    display_grid(grid)
