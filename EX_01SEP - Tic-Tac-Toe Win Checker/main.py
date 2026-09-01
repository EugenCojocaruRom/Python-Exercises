#Print header and separator
print("<-- Tic-Tac-Toe Win Checker -->")
print("-------------------------------")

def get_valid_input(prompt):
    #Keep asking until the user enters X, O, or blank (empty) for a cell
    while True:
        value = input(prompt).strip().upper()
        if value in ("X", "O", ""):
            return value
        print("Invalid entry. Please enter X, O, or leave blank for empty.")

def build_board():
    #Ask the user for all 16 cells and return them as a 4x4 list of lists
    board = []
    for row_num in range(4):
        row = []
        for col_num in range(4):
            cell = get_valid_input(f"Row {row_num + 1}, Col {col_num + 1} (X/O/blank): ")
            row.append(cell)
        board.append(row)
    return board

def print_board(board):
    #Print the board in a readable grid, using enumerate() for row numbers
    print("\nCurrent board:")
    for row_index, row in enumerate(board, start=1):
        #Replace empty strings with "." (for display purposes)
        display_row = [cell if cell != "" else "." for cell in row]
        print(f"Row {row_index}: {' | '.join(display_row)}")
    print()

def get_all_lines(board):
    #Collect every possible winning line: 4 rows, 4 columns, 2 diagonals
    rows = board  #the rows are already there as-is
    #Build columns using list comprehension: grab the i-th item from every row
    columns = [[board[row][col] for row in range(4)] for col in range(4)]
    #The two diagonals
    diagonal_1 = [board[i][i] for i in range(4)]        # top-left to bottom-right
    diagonal_2 = [board[i][3 - i] for i in range(4)]    # top-right to bottom-left
    return rows + columns + [diagonal_1, diagonal_2]

def check_winner(board):
    #Check all lines; return 'X', 'O', or None if nobody has won.
    all_lines = get_all_lines(board)
    for line in all_lines:
        #A line wins if all 4 cells match and aren't empty
        if line[0] != "" and line.count(line[0]) == 4:
            return line[0]
    return None

def is_board_full(board):
    #True if there are no empty cells left anywhere on the board
    #Flatten the board into one list and check for any leftover blanks
    all_cells = [cell for row in board for cell in row]
    return "" not in all_cells

#Execute the program by calling the functions
board = build_board()
print_board(board)
winner = check_winner(board)

if winner:
    print(f"{winner} wins!")
elif is_board_full(board):
    print("It's a draw!")
else:
    print("No winner yet")