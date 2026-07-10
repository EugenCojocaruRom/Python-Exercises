EX\_10JUL - Typing Speed Tracker (WPM Calculator)

The user types out a sentence (as if practicing typing), and your program tells them their typing speed in Words Per Minute (WPM), plus tracks their best attempt across multiple tries.



Requirements:

&#x20;- Ask the user how many typing attempts they want to simulate.

&#x20;-For each attempt:

&#x20; -> Ask them to type a sentence (any text).

&#x20; -> Ask them how many seconds it took them to type it (simulate — no real timer needed).

&#x20; -> Calculate WPM = (number of words / seconds) × 60.

&#x20;- Use enumerate() to number and display each attempt's results (e.g., "Attempt 1: 45.0 WPM").

&#x20;- Use a list comprehension somewhere — for example, to build a list of word counts per sentence, or to filter out empty sentences.

&#x20;- At the end, show:

&#x20; -> The best (highest) WPM and which attempt number it was.

&#x20; -> The average WPM across all attempts.



Bonus (optional):

&#x20;- Give a "rating" for each attempt (e.g., below 20 WPM = "Beginner", 20–40 = "Average", 40+ = "Fast") using if/elif.

&#x20;- Handle a 0-second input gracefully (avoid division by zero).

