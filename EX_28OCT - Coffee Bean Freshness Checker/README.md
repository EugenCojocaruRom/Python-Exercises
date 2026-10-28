EX\_28OCT - Coffee Bean Freshness Checker

Scenario: A small café keeps track of how many days ago each bag of coffee beans was roasted. Beans are only good for serving within a certain window.



Starting data:



bags = \[

&#x20;   ("Ethiopia", 3),

&#x20;   ("Colombia", 12),

&#x20;   ("Brazil", 25),

&#x20;   ("Kenya", 8),

&#x20;   ("Guatemala", 40),

&#x20;   ("Sumatra", 15),

]



Each tuple is (origin, days\_since\_roasting).



Rules:

&#x09;0 to 7 days: “Fresh”

&#x09;8 to 20 days: “Good”

&#x09;21 to 30 days: “Use soon”

&#x09;Over 30 days: “Expired”



Tasks:

&#x20;- Loop through the bags using enumerate(), starting the numbering at 1, and print each line in this format:

&#x09;1. Ethiopia - 3 days - Fresh

&#x20;- Use a list comprehension to build a list of the origins that are “Expired” and print it.

&#x20;- Use a list comprehension to build a list of the origins that are “Fresh” or “Good” and print it.

&#x20;- Calculate and print the average age of all the bags, rounded to 1 decimal place.

&#x20;- Print the name of the oldest bag and how many days old it is.



Expected output (roughly):



1\. Ethiopia - 3 days - Fresh

2\. Colombia - 12 days - Good

3\. Brazil - 25 days - Use soon

4\. Kenya - 8 days - Good

5\. Guatemala - 40 days - Expired

6\. Sumatra - 15 days - Good

Expired: \['Guatemala']

Ready to serve: \['Ethiopia', 'Colombia', 'Kenya', 'Sumatra']

Average age: 17.2 days

Oldest bag: Guatemala (40 days)



Bonus (optional): Wrap the freshness rules in a small function called get\_status(days) that returns the label, and use it in your loop and comprehensions.

