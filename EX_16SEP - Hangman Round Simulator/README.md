EX\_16SEP - Hangman Round Simulator

You're given a secret word and a list of letters the player has already guessed.



Your program should:

&#x20;- Ask the user to input a secret word (or hardcode one to start, then make it dynamic).

&#x20;- Ask the user to enter guessed letters one at a time in a loop (while True), stopping when they type "done".

&#x20;- After each guess, display the current state of the word as a masked string — revealed letters shown, unguessed letters shown as \_. (Hint: this is a great spot for a list comprehension over the secret word's letters, checking membership against the guesses so far.)

&#x20;- Track and display how many wrong guesses have been made (letters guessed that aren't in the word), and end the game early with a "you lose" message if wrong guesses hit a limit (e.g. 6).

&#x20;- If all letters get revealed before the limit, print a win message.



Bonus:

&#x20;- Use enumerate() to show the guess number alongside each guess in a summary at the end (e.g. Guess 1: 'a' → correct, Guess 2: 'z' → wrong).

Bonus 2:

&#x20;-Handle repeated guesses (same letter guessed twice) without double-counting them as wrong guesses.

