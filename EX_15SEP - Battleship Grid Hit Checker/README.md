EX\_15SEP - Battleship Grid Hit Checker

You have a 5x5 grid representing a player's board. Each cell is either:

&#x09;"." → empty water

&#x09;"S" → a ship segment

&#x09;"X" → a hit (already fired at)

&#x09;"O" → a miss (already fired at)

Requirements:

&#x20;- Display the grid nicely with row and column numbers (use enumerate()).

&#x20;- Let the player take shots in a loop: ask for a row and column (with your usual while True / try-except validation for valid integers and valid range 0–4).

&#x20;- When a shot lands on "S", mark it "X" and tell the player "Hit!". When it lands on ".", mark it "O" and tell them "Miss!". If they shoot a cell already marked "X" or "O", tell them they've already fired there — don't let them fire again.

&#x20;- After each shot, redisplay the grid.

&#x20;- Use a list comprehension (with nested iteration, flattening the grid) to count how many "S" cells remain — this tells you if the game is over.

&#x20;- When there are no "S" cells left, print a "You sank all the ships!" message and end the game.



Bonus (optional):

&#x20;- Track and display the number of shots taken and hit/miss ratio.

&#x20;- Instead of a hardcoded grid, randomly place 3 ships of length 1 (single cells) using random.sample() on flattened coordinates.

