EX\_24AUG - Class Attendance Roll Call

Tasks:

&#x20;- Start with a list of student names (hardcode a few, or take dynamic input — your call).

&#x20;- Ask the user, for each student, whether they were present (y/n).

&#x20;- Store the results as tuples: (name, status) where status is "Present" or "Absent".

&#x20;- Using enumerate() starting at 1, print a numbered roll call like:

&#x20;  1. Alina - Present

&#x20;  2. Mihai - Absent

&#x20;  3. Cristina - Present

&#x20;- Use a list comprehension to build a list of just the absent students' names.

&#x20;- Print a summary: how many present, how many absent, and the attendance rate as a percentage (e.g. Attendance rate: 66.7%).

&#x20;- Handle singular/plural properly in the absentee message (e.g. "1 student was absent" vs "2 students were absent" vs "No students were absent").



Bonus (optional):

&#x20;- Track a running list of absence counts per student across multiple "days" (a small dictionary aggregation, sorted() descending) — i.e. simulate calling roll for 3 days in a row and show who's been absent the most.

