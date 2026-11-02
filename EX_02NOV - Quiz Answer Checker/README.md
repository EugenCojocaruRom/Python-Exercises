EX\_02NOV - Quiz Answer Checker

Scenario: A teacher has an answer key and a student’s answers for a 10-question quiz. Write a program that checks the answers and prints a short report.



Starting data:

&#x09;answer\_key = \["B", "A", "D", "C", "A", "B", "C", "D", "A", "B"]

&#x09;student\_answers = \["B", "A", "C", "C", "A", "D", "C", "D", "B", "B"]



Tasks:

&#x20;- Check each answer. Use enumerate() to go through student\_answers. For each question, print the question number (starting at 1), the student’s answer, and whether it’s correct, like this:

&#x20;  Question 1: B - Correct

&#x20;  Question 3: C - Wrong (correct answer: D)

&#x20;- Count the score. Use a list comprehension to build a list of the question numbers the student got wrong. Then work out how many answers were correct.

&#x20;- Print a summary with:

&#x09;The score as 7/10

&#x09;The percentage

&#x09;The list of wrong question numbers

&#x20;- Pass or fail. If the percentage is 60 or higher, print Result: Pass, otherwise print Result: Fail.



Expected summary output (for the data above):

&#x09;Score: 7/10

&#x09;Percentage: 70.0%

&#x09;Wrong questions: \[3, 6, 9]

&#x09;Result: Pass



Bonus (optional): Change student\_answers to use lowercase letters for a few answers, and make your program still count them as correct. Hint: look at the .upper() string method.

