EX\_12OCT - Student Attendance Streak Report

Scenario 1: A teacher keeps a record of attendance for a week. Each student has a list of "P" (present) or "A" (absent) for Monday to Friday. You will write a small report.



Starting data:



attendance = {

&#x20;   "Ana":    \["P", "P", "A", "P", "P"],

&#x20;   "Bogdan": \["A", "P", "P", "P", "P"],

&#x20;   "Carmen": \["P", "A", "A", "P", "A"],

&#x20;   "Dan":    \["P", "P", "P", "P", "P"],

&#x20;   "Elena":  \["A", "A", "P"],

&#x20;   "Maria":  \["P", "X", "P", "P", "A"],

&#x20;   "Tudor":  \["P", "A", "P", "P", "A", "A"],

&#x20;   "Mihai":  \[],

}

days = \["Mon", "Tue", "Wed", "Thu", "Fri"]



Tasks:

&#x20;- attendance\_rate(records): write a function that takes one student’s list and returns the percentage of days present (for example, 80.0).

&#x20;- longest\_streak(records): write a function that returns the longest run of consecutive "P" days for one student. For example, \["P", "P", "A", "P", "P", "P"] gives 3.

&#x20;- Per-student report: loop over the dictionary and print one line per student, like this:

&#x20;  	Ana: 80.0% present, longest streak: 2

&#x20;- Perfect attendance: use a list comprehension to build a list of the students whose rate is 100.0.

&#x20;- Worst day: use enumerate() to find which day of the week had the most absences across all students. Print the day name and the number of absences.

&#x20;- Needs attention: print the names of students with an attendance rate below 50%, sorted alphabetically.

&#x09;Expected output (for the data above)

&#x09;Ana: 80.0% present, longest streak: 2

&#x09;Bogdan: 80.0% present, longest streak: 4

&#x09;Carmen: 40.0% present, longest streak: 1

&#x09;Dan: 100.0% present, longest streak: 5

&#x09;Elena: 20.0% present, longest streak: 1



&#x09;Perfect attendance: \['Dan']

&#x09;Worst day: Wed (2 absences)

&#x09;Needs attention: \['Carmen', 'Elena']

\*\*Note that Mon, Wed and Fri each have 2 absences in this data. Your program should decide what to do with a tie, so pick a rule (for example, the first day found) and keep it consistent.



Scenario 2: The teacher’s data is messy. Some records have the wrong number of days, and some contain values other than "P" or "A". Instead of crashing or silently ignoring them, your program must reject bad records with a clear message and still report on the good ones.



Tasks:

&#x20;- validate\_records(name, records): write a function that checks one student’s list and raises a ValueError with a clear message if something is wrong:

&#x09;-> If the length is not len(days), the message is "<name>: expected 5 days, got <n>".

&#x09;-> If a value is not "P" or "A", the message is "<name>: invalid value '<value>' on <day>".

&#x09;-> Check the length first, then the values.

&#x20;- Main loop: for each student, call validate\_records inside a try block. If it passes, calculate the attendance rate (reuse your attendance\_rate) and store the line in a list called valid\_lines. If it raises a ValueError, catch it with except ValueError as error: and store str(error) in a list called errors.

&#x20;- Print the results: first the valid students, then the errors, then a one-line summary.



Hints:

&#x20;- For longest\_streak, keep two variables: current and best. Add 1 to current on "P", reset it to 0 on "A", and update best each time.

&#x20;- For the worst day, you can build a list of absence counts per day with a list comprehension, then use enumerate() to find the index of the largest one.

&#x20;- To raise an error: raise ValueError(f"{name}: expected {len(days)} days, got {len(records)}")

&#x20;- For the value check, zip(days, records) gives you the day name and the record together, so you can name the day in the message.

&#x20;- validate\_records doesn’t need to return anything. It either finishes silently (valid) or raises (invalid).



Bonus (optional):

&#x20;- Add a student with a different number of days and see whether your code still works, or rewrite the report so it prints the days each student missed (for example, Carmen missed: Tue, Wed, Fri).

&#x20;- Make the day names and allowed values easy to change by keeping the allowed values in a variable, such as allowed = ("P", "A"), and checking record not in allowed.

&#x20;- Add a student whose record is None instead of a list.

