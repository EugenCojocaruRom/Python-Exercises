EX\_15AUG - Pottery Studio Kiln Firing Tracker

A local pottery studio wants a simple tracker for pieces going into the kiln for a firing session.



Requirements:

&#x20;- Ask the user how many pieces are in this firing batch.

&#x20;- For each piece, collect:

&#x09;Artist name

&#x09;Piece type (e.g., "mug", "bowl", "vase")

&#x09;Height in centimeters (a number)

&#x20;- Store each piece as a tuple: (artist, piece\_type, height)

&#x20;- Using enumerate() starting at 1, print a numbered list of all pieces in the batchUsing a list comprehension, build a list of all pieces taller than 15 cm (these need the "tall shelf" in the kiln). Print how many there are, with correct singular/plural wording (e.g., "1 tall piece" vs. "3 tall pieces").

&#x20;- Find the tallest piece in the batch and print who made it and its height. Handle the case where there might be a tie (more than one piece sharing the max height).



Bonus:

&#x20;- Using a dictionary, count how many pieces each artist submitted, then print a leaderboard sorted by piece count, descending (most active artist first).

