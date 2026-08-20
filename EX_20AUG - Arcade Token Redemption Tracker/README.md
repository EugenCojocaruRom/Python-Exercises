EX\_20AUG - Arcade Token Redemption Tracker

At an arcade, kids trade tickets/tokens for prizes. Build a tracker for a shift:



&#x20;- Ask how many players visited (validate positive integer with try/except).

&#x20;- For each player, ask for:

&#x09;their name

&#x09;how many tokens they spent (validate positive number)

&#x20;- Store each entry as a tuple, e.g. (name, tokens\_spent).

&#x20;- Print a numbered list of all players using enumerate() starting at 1.

&#x20;- Use a list comprehension to find "big spenders" — anyone who spent more than 50 tokens. Print how many there are, with singular/plural wording (e.g. "1 big spender" vs. "3 big spenders", or "No big spenders today" if none).

&#x20;- Use max() with a lambda to find the player who spent the most tokens overall. Guard against an empty list.

&#x20;- Print a total tokens spent across all players (sum, or a list comprehension + sum()).



Optional bonus: ask each player which prize category they redeemed (e.g. "plush", "candy", "toy"), and build a dictionary aggregating total tokens spent per category, then print it as a sorted() leaderboard, most popular category first.

