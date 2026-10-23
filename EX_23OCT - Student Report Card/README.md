EX\_23OCT - Student Report Card



Starting data:

&#x09;scores = {

&#x20;   		"Ana": \[88, 92, 79],

&#x20;   		"Bogdan": \[55, 61, 48],

&#x20;   		"Carmen": \[100, 95, 98],

&#x20;   		"Dan": \[72, 68, 75],

&#x20;   		"Elena": \[],

&#x09;}



Tasks:

&#x20;- Write calculate\_average(marks). It takes a list of numbers and returns the average rounded to 1 decimal place. If the list is empty, return 0.

&#x20;- Write letter\_grade(average). It takes an average and returns a letter:

&#x09;90 or above: "A"

&#x09;80 or above: "B"

&#x09;70 or above: "C"

&#x09;60 or above: "D"

&#x09;anything lower: "F"

&#x20;- Write build\_report\_card(all\_scores). It returns a dictionary where each student’s name maps to another dictionary with their average and grade:

&#x20;  {"Ana": {"average": 86.3, "grade": "B"}, ...}



&#x20;- Use your two functions inside it.

&#x20;- Print a ranking. Sort the students by average, highest first, and use enumerate() starting at 1 to print:

&#x20;  1. Carmen - 97.7 (A)

&#x20;  2. Ana - 86.3 (B)

&#x20;  ...

&#x20;- Use a list comprehension to build a list of the names of students who passed (any grade except "F"), and print it.



Bonus (optional):

&#x20;- Print the class average, ignoring students with no marks.

&#x20;- Count how many students got each letter grade, using a dictionary.



Hint for step 4: sorted() accepts a key= argument, and a lambda can pick the average out of each dictionary.

