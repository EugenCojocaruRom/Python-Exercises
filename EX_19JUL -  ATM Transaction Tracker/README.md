EX\_19JUL - ATM Transaction Tracker

Simulate a simple bank account. The user starts with a balance, then makes a series of deposits and withdrawals. At the end, print a formatted transaction statement and a summary.



Requirements:

&#x20;- Start with a balance (e.g. 500).

&#x20;- Let the user enter transactions in a loop — each one is an amount (positive = deposit, negative = withdrawal). Typing done ends the loop.

&#x20;- Reject any withdrawal that would overdraw the account (print a warning, don't apply it).

&#x20;- Store every accepted transaction in a list (as a tuple: (type, amount, resulting\_balance) — type being "deposit" or "withdrawal").

&#x20;- After the loop, print a numbered statement using enumerate(), e.g.:



&#x20;  1. Deposit    +200.00 -> Balance: 700.00

&#x20;  2. Withdrawal -150.00 -> Balance: 550.00



&#x20;- Using list comprehension, calculate and print:

&#x20;  Total deposited

&#x20;  Total withdrawn

&#x20;  Number of rejected withdrawal attempts (you'll need a counter for this one, since it's outside the accepted list)



Bonus (optional):

&#x20;- Flag any single withdrawal over 300 as "⚠️ Large withdrawal" next to it in the statement.

&#x20;- At the end, find and print the transaction that had the biggest single impact (positive or negative) on the balance, using max() with a key=lambda.

