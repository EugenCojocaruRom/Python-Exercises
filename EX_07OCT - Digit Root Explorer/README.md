EX\_07OCT - Digit Root Explorer

The digital root of a number is found by adding up its digits repeatedly until only a single digit remains.



&#x09;Example: 9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2. So the digital root of 9875 is 2.



Task -> Write a program that does the following:

&#x20;- Create a function digit\_sum(n) that returns the sum of the digits of a number. For example, digit\_sum(9875) returns 29.

&#x09;Hint: you can convert the number to a string and use a list comprehension.

&#x20;-Create a function digital\_root(n) that keeps calling digit\_sum until the result is a single digit. It should also return the number of steps it took.

&#x09;Example: digital\_root(9875) returns (2, 2), meaning root 2 after 2 steps.

&#x20;- Take this list of numbers:

&#x20;  	numbers = \[9875, 38, 7, 456, 99999, 1024, 5, 777]

&#x20;- Use enumerate() to print a numbered report, one line per number, like this:

&#x20;  1. 9875 -> root 2 (2 steps)

&#x20;  2. 38 -> root 2 (2 steps)

&#x20;  ...

&#x20;- Use a list comprehension to build a list of only the numbers whose digital root is odd, and print it.

&#x20;- Print which number in the list took the most steps.



Bonus (optional): Add a final line showing how many numbers fall into each root (1 to 9), for example Root 2: 2 numbers. Only print the roots that actually appear.

