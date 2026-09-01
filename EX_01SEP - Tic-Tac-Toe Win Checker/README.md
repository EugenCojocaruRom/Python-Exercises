EX\_01SEP - Tic-Tac-Toe Win Checker

You're given a 3x3 board like this:



board = \[

&#x20;   \["X", "O", "X"],

&#x20;   \["O", "X", "O"],

&#x20;   \["X", "O", "X"]

]



Empty cells are represented by an empty string "".



Requirements:

&#x20;- Let the user fill in the board manually via 9 inputs (row by row, or however you'd like to structure it) — accepting "X", "O", or "" (empty) for each cell, with validation.

&#x20;- Print the board out nicely formatted, like a grid.

&#x20;- Check for a winner:

&#x09;All 3 rows the same (and not empty)

&#x09;All 3 columns the same (and not empty)

&#x09;Both diagonals the same (and not empty)

&#x20;- Print the result: "X wins!", "O wins!", or "No winner yet" if nobody's completed a line.



Bonus:

&#x20;- If nobody wins and every cell is filled, print "It's a draw!" instead of "No winner yet".

&#x20;- Use enumerate() when printing the board with row numbers (1, 2, 3).

&#x20;- Try writing the row-check and column-check using list comprehensions (e.g. checking if len(set(row)) == 1 for a row).

