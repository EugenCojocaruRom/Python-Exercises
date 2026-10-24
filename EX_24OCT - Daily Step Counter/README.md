EX\_24OCT - Daily Step Counter

You wear a fitness band and recorded your steps for one week:

&#x09;steps = \[4200, 8500, 12000, 6700, 9300, 3100, 10400]

&#x09;days = \["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

Tasks:

&#x20;- Print each day with its steps using enumerate(), numbered from 1.

&#x09;Example: 1. Mon: 4200 steps

&#x20;- Find the goal days. Using a list comprehension, build a list of the day names where you reached 8000 steps or more. Print it.

&#x20;- Calculate the weekly total and the daily average. Print the average rounded to 1 decimal place.

&#x20;- Find the best and worst day. Print the name of the day with the most steps and the day with the fewest.

&#x20;- Print a verdict:

&#x09;If you reached the goal on 4 or more days: Great week!

&#x09;If on 2 or 3 days: Not bad, keep going!

&#x09;Otherwise: Time to get moving!



Expected output (approximately)

1\. Mon: 4200 steps

2\. Tue: 8500 steps

...

Goal days: \['Tue', 'Wed', 'Fri', 'Sun']

Total steps: 54200

Average: 7742.9

Best day: Wed

Worst day: Sat

Great week!



Bonus (optional)

&#x20;- Using a list comprehension, create a list of the steps still missing to reach 8000 on each day (use 0 for days where the goal was reached).

