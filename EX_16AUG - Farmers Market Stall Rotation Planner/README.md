EX\_16AUG - Farmers Market Stall Rotation Planner

A farmers market wants a tool to help assign vendors to daily stall time slots.



Requirements:

&#x20;- Ask how many vendors are signing up for the day.

&#x20;- For each vendor, collect:

&#x09;Vendor name

&#x09;Product category (e.g., "produce", "baked goods", "flowers")

&#x09;Requested hours (a number, how many hours they want to sell)

&#x20;- Store each vendor as a tuple: (name, category, hours)

&#x20;- Using enumerate() starting at 1, print the full sign-up list

&#x20;- Using a list comprehension, build a list of vendors requesting more than 5 hours (they'll need the "extended stall" pricing). Print the count with correct singular/plural wording.

&#x20;- Find the vendor(s) with the longest requested hours. Print their name(s), category, and hours — handle ties (more than one vendor with the same max).



Bonus:

&#x20;- Using a dictionary, count how many vendors fall into each product category, then print a summary sorted by category count, descending (most common category first).

