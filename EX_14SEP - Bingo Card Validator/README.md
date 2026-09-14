EX\_14SEP - Bingo Card Validator

You're given a 5x5 Bingo card (a list of lists, numbers 1–75) and a list of numbers that have been "called" during the game.



Your program should:

&#x20;- Ask the user to input the called numbers one at a time (while True loop, type "done" to stop, with validation that each entry is a valid integer).

&#x20;- Mark which numbers on the card have been called — use a list comprehension (or nested list comprehension) to build a "marked" version of the card (e.g. replace matched numbers with "X", or build a parallel boolean grid).

&#x20;- Use enumerate() to print the card row by row with row numbers (Row 1, Row 2, ...).

&#x20;- Check if there's a BINGO: any full row, any full column, or either diagonal completely marked.

&#x20;- Print a summary: how many numbers have been marked so far, and whether BINGO has been achieved.



Bonus (optional):

&#x20;- Also check if the whole card is fully marked ("BLACKOUT").

&#x20;- Report which specific row/column/diagonal triggered the win.

&#x20;- Instead of hardcoding the card, let it be a hardcoded 5x5 list of lists at the top of your script (no need to randomize it) — but the called numbers should come from user input.

