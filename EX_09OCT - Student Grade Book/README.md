EX\_09OCT - Student Grade Book (functions + dictionary)

Scenario: You store student grades in a dictionary, where each key is a student's name and each value is a list of grades.



e.g. grades = {

&#x20;   	"Ana": \[9, 10, 8],

&#x20;   	"Mihai": \[7, 6, 8, 9],

&#x20;   	"Elena": \[10, 10, 9],

&#x20;   	"Radu": \[5, 6]

&#x09;}



Write these functions:

&#x20;- average(grade\_list) returns the average of a list, rounded to 2 decimals.

&#x20;- add\_grade(book, name, grade) adds a grade to a student. If the student doesn't exist yet, create them with a new list.

&#x20;- best\_student(book) returns the name of the student with the highest average.



The program should:

&#x20;- Print every student with their average, using a for name, marks in grades.items() loop.

&#x20;- Add a few grades with add\_grade(), including one for a new student.

&#x20;- Print the best student.

&#x20;- Use a list comprehension at least once, for example to list the students with an average of 8 or more.



Hints:

&#x20;- max(book, key=lambda name: average(book\[name])) finds the best student. If lambda feels new, a regular loop that tracks the best average so far works just as well.

&#x20;- To add to a dictionary list safely, book.setdefault(name, \[]).append(grade) is a handy one-liner. The longer version with if name not in book: is also fine.



Bonus (optional):

&#x20;- Validate that a grade is between 1 and 10 before adding it.

&#x20;- Print the students sorted by average, highest first, using sorted() with key=.

