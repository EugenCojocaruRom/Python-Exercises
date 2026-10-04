EX\_04OCT - Pascal's Triangle Printer

Goal: Write a program that builds and prints the first n rows of Pascal's Triangle.



Each row starts and ends with 1, and every number in between is the sum of the two numbers directly above it:



&#x20;       1

&#x20;      1 1

&#x20;     1 2 1

&#x20;    1 3 3 1

&#x20;   1 4 6 4 1



Requirements

&#x20;- Ask the user for the number of rows n (or hard-code n = 6 to start).

&#x20;- Write a function next\_row(row) that takes one row (a list) and returns the next row.

&#x09;Example: next\_row(\[1, 3, 3, 1]) returns \[1, 4, 6, 4, 1]

&#x20;- Build the full triangle as a list of lists, starting from \[1].

&#x20;- Print the triangle with each row centered, so it looks like a triangle. Hint: build each row as a string with " ".join(...), then use .center(width).

&#x20;- After printing, show the sum of each row using enumerate():

&#x20;  Row 0 sum: 1

&#x20;  Row 1 sum: 2

&#x20;  Row 2 sum: 4



Bonus challenges (optional)

&#x20;- Write next\_row as a list comprehension. Hint: pad the row with zeros on both sides (\[0] + row and row + \[0]) and add the two lists together element by element with zip().

&#x20;- Print only the rows where the sum is greater than 10.

&#x20;- Find and print the largest number in the whole triangle.

