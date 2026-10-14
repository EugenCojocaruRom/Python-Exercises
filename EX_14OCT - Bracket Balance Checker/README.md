EX\_14OCT - Bracket Balance Checker

Goal: Write a program that checks whether the brackets in a piece of text are balanced, and if not, reports where the first problem is.



Rules

&#x20;- Three bracket types count: (), \[], {}.

&#x20;- Every opening bracket must be closed by the matching type, in the correct order.

&#x20;- All other characters (letters, digits, spaces) are ignored.



Step 1: Basic checker

&#x20;- Write a function check\_brackets(text) that returns True if the text is balanced and False otherwise.



&#x09;Hint: use a list as a “stack”. When you see an opening bracket, append() it. When you see a closing bracket, pop() the last opening 	bracket and check that it matches. At the end, the stack should be empty.



Step 2: Report the position

&#x20;- Use enumerate() to improve the function so it returns a message with the index of the first problem:

&#x09;"Balanced" if everything is fine

&#x09;"Unexpected ')' at position 5" if a closing bracket has no matching opener

&#x09;"Mismatch: expected ']' but found ')' at position 8" if the types don’t match

&#x09;"Unclosed '(' at position 0" if an opener is never closed



Step 3: Test it

&#x20;- Run your function on a list of test strings using a for loop, for example:

&#x09;tests = \[

&#x20;   		"(a + b) \* \[c - d]",

&#x20;   		"{\[()]}",

&#x20;   		"(]",

&#x20;   		"((3 + 4)",

&#x20;   		"x + y)",

&#x20;   		"",

&#x09;]



Expected results:

&#x09;"(a + b) \* \[c - d]" → Balanced

&#x09;"{\[()]}" → Balanced

&#x09;"(]" → Mismatch: expected ‘)’ but found ‘]’ at position 1

&#x09;"((3 + 4)" → Unclosed ‘(’ at position 0

&#x09;"x + y)" → Unexpected ‘)’ at position 5

&#x09;"" → Balanced



Bonus (optional)

&#x20;- Use a list comprehension to print only the test strings that are not balanced.

&#x20;- Store the matching pairs in a dictionary ({")": "(", "]": "\[", "}": "{"}) instead of using many if statements.

&#x20;- Count how many strings were balanced vs. unbalanced and print a short summary.

