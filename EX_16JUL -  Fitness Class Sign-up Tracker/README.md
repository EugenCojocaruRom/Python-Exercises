EX\_16JUL - Fitness Class Signup Tracker

A gym runs several fitness classes, each with a maximum capacity. You'll track sign-ups and figure out who's in, who's waitlisted, and print a clean summary.



Requirements:

&#x20;- Store classes as a dictionary, where each class has a name and a max capacity

&#x20;- Store sign-ups as a list of tuples: (person\_name, class\_name)

&#x20;- For each class, process sign-ups in order and:

&#x20;  -> Assign people to spots until the class hits its max capacity

&#x20;  -> Anyone after that goes to a waitlist for that class

&#x20;-Print a summary for each class showing:

&#x20;  -> Confirmed attendees, numbered (hint: enumerate())

&#x20;  -> Waitlisted people, numbered separately

&#x20;  -> If a class has zero sign-ups, print something like "No sign-ups yet."



Bonus (optional):

&#x20;- Use a list comprehension somewhere — e.g., to build the list of confirmed names for a class, or to find which classes are completely full

&#x20;- Print a final line: how many classes are full vs. how many still have open spots

