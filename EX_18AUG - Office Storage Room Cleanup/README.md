EX\_18AUG - Office Storage Room Cleanup

Write a function clean\_storage\_room that takes items and returns a dictionary with categorized storage items.



The function processes office storage items, reversing their names to decode labels and categorizing them based on their condition tags.



Logic:



&#x20;   Process each item in the list sequentially

&#x20;   Skip items tagged as "skip" using continue

&#x20;   Stop processing entirely when encountering "stop" using break

&#x20;   For valid items, reverse the item name to decode the label

&#x20;   Items tagged as "good" go to "keep" list, "bad" items go to "throw" list

&#x20;   Items without tags are ignored (continue to next item)



Parameters:



&#x20;   items (list): List of strings in format "itemname:tag" or just "itemname"



Returns: Dictionary with "keep" and "throw" keys, each containing a list of reversed item names. Format: {"keep": \["reversed\_name1", "reversed\_name2"], "throw": \["reversed\_name3"]}

