EX\_02SEP - Grade Distribution Chart

Ask the user how many students there are, then collect each student's grade (0–100) with validation.

Then:

&#x20;- Print a numbered list of all grades using enumerate() (start=1).

&#x20;- Using a list comprehension, build a list of just the passing grades (say, ≥60).

&#x20;- Print how many passed vs failed, with correct singular/plural wording.

&#x20;- Build a simple ASCII bar chart showing how many grades fall into each bucket: 0-59, 60-69, 70-79, 80-89, 90-100. For each bucket, use a list comprehension to count how many grades fall in that range, then print a row like:

&#x09;0-59  : ### (3)

&#x09;60-69 : ##### (5)

&#x09;70-79 : ####### (7)

&#x09;80-89 : #### (4)

&#x09;90-100: ## (2)



Bonus (optional): find the class average, and print which bucket has the most students (handle a tie if you want).

