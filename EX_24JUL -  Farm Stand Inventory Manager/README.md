EX\_24JUL - Farm Stand Inventory Manager

Write a function manage\_stand that takes inventory, orders and returns a dictionary summarizing remaining fresh vs. preserved items.



Your farm stand tracks inventory with preservative status and processes customer orders throughout the day.



Logic:



&#x20;   Parse each inventory item from "item:count:preservative" format

&#x20;   Process each order to reduce stock for matching items

&#x20;   Group remaining items by preservative status (fresh vs. artificial)

&#x20;   Calculate totals for each category



Parameters:



&#x20;   inventory (list): Initial stock in "item:count:preservative" format

&#x20;   orders (list): Customer orders in "item:quantity" format



Returns: Dictionary with preservative categories and their item counts. Format: {"fresh": {"item1": count1, "item2": count2}, "artificial": {"item3": count3}}

