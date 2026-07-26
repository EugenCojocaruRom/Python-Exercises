EX\_26JUL - Taxi Fare Calculator

A taxi company wants to calculate fares for a day's worth of rides. Each ride has a distance (in km) and a duration (in minutes).

Each tuple is (ride\_name, ride\_distance, ride\_duration).



Pricing rules:

&#x20;- Base fare: 3.50

&#x20;- Plus 1.20 per km

&#x20;- Plus 0.25 per minute

&#x20;- If distance is over 15 km, apply a 10% surcharge on the total fare for that ride



Requirements:

&#x20;- Using enumerate(), print each ride with its calculated fare, formatted like: Ride 1: Ride A - $XX.XX

&#x20;- Calculate and print the total revenue from all rides combined

&#x20;- Using a list comprehension, build a list of ride names where the fare exceeded $20

&#x20;- Find the most expensive ride and the cheapest ride (name + fare) using max()/min() with lambda



Bonus: count how many rides qualified for the long-distance surcharge, using a list comprehension

