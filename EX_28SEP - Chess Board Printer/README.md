EX\_28SEP - Chess Board Printer

Goal: Print an 8x8 chessboard in the terminal using # for dark squares and . for light squares, then highlight a few chosen squares.



Part 1: Draw the board



Write a program that prints this pattern (top-left square is light):



. # . # . # . #

\# . # . # . # .

. # . # . # . #

\# . # . # . # .

. # . # . # . #

\# . # . # . # .

. # . # . # . #

\# . # . # . # .



Hint: A square is dark when (row + col) is odd.



Part 2: Mark squares



Given this list of chess squares:



&#x09;marked = \["a1", "c3", "h8", "e5"]



Print the board again, but replace those squares with X.



Use standard chess notation:



&#x09;The letter is the column: a = first column ... h = last column

&#x09;The number is the row, with row 1 at the bottom of the printed board and row 8 at the top



So a1 is the bottom-left corner, and h8 is the top-right corner.



Part 3: Summary



After the board, print:



&#x20;- how many squares are dark and how many are light (as counted from the board, not hard-coded)

&#x20;- the marked squares that landed on dark squares, e.g. Marked on dark squares: \['c3', 'e5']



Requirements

&#x20;- Use enumerate() at least once

&#x20;- Use at least one list comprehension

&#x20;- Don't type the board by hand. Generate it with loops.



Bonus (optional):

&#x20;- Ask the user to type squares (like b2 d4 g7) and validate them. Reject anything that isn't a letter a-h followed by a number 1-8.

