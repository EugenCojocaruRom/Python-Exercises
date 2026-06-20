EX\_20JUN - Inventory Restocker

You're managing a small shop's inventory. Each item has a name, a current stock count, and a restock threshold (the minimum amount you want on hand).

Requirements:

&#x20;- Store your inventory data however makes sense to you (list of tuples, dict, list of dicts — your call).

&#x20;- Use a list comprehension to find all items that are below their threshold (need restocking).

&#x20;- For each item that needs restocking, calculate how many units to order to bring it back up to double the threshold (so it has a buffer).

&#x20;- Print a formatted restock report showing: item name, current stock, threshold, and units to order — aligned in columns using f-string width formatting.

&#x20;- Use enumerate() somewhere — for example, numbering each line item in the report (1, 2, 3...).

&#x20;- Print a final summary: total number of items restocked, and total units ordered across all items.

Stretch goal (optional): sort the restock report so the most urgently needed items (furthest below threshold) appear first.

