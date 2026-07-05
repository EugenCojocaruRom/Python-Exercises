EX\_05JUL - Parking Garage Spot Assigner

A small parking garage has a fixed number of spots, numbered starting from 1. Cars arrive one at a time and get assigned to the first available spot. Some spots might already be occupied when the day starts.



Requirements:

&#x20;- Start with a list representing the garage, e.g. garage = \[None, "ABC123", None, None, "XYZ789"] — None means empty, otherwise it holds a license plate.

&#x20;- You get a list of new arriving cars, e.g. arrivals = \["CAR001", "CAR002", "CAR003"]

&#x20;- For each arriving car, find the first empty spot (None) and assign the car there. If the garage is full, print a message saying that car couldn't park.

&#x20;- After processing all arrivals, print a nicely formatted list of all spots showing the spot number (starting at 1) and what's parked there (or "Empty").

&#x20;- Also print a summary: how many spots are occupied vs how many are free.



Bonus challenge (optional):

&#x20;- If the garage is full, don't just skip the car — put it on a waiting\_list and try to park waiting cars first whenever a spot frees up (you could simulate a car leaving too).

