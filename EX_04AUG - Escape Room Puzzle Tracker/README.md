EX\_04JUL - Escape Room Puzzle Tracker

A team is attempting an escape room with several puzzle stations. For each puzzle, track the puzzle name and the time (in minutes) it took the team to solve it.



Requirements:

&#x20;- Let the user enter puzzle data one at a time (name + time in minutes) using a while True loop that stops when they type done (or similar).

&#x20;- Store each entry as a tuple in a list.

&#x20;- Print a numbered list of all puzzles using enumerate(start=1).

&#x20;- Calculate the total time spent across all puzzles.

&#x20;- Use a list comprehension to find all puzzles that took longer than 5 minutes (or your own threshold) — call these "tricky puzzles."

&#x20;- Use min() with a lambda to find the fastest-solved puzzle.

&#x20;- Print a summary: total puzzles solved, total time, list of tricky puzzles, and the fastest one.



Bonus:

&#x20;- Add a countdown: if the team has a 60-minute time limit, calculate and display how much time is left after each puzzle is logged.

&#x20;- Handle the edge case where the list is empty when computing min().

