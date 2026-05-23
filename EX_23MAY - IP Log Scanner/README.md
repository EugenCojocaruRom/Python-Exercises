EX\_23MAY - IP Log Scanner

Imagine your network router dumps a list of raw log strings. Each string contains an IP address and a status code (like 200 for success or 404 for missing).

Your job is to clean up this data, filter out only the problematic IPs, and print them out with their original line positions so a network admin can find them quickly.

Task:

&#x20;- Write a script that takes a list of raw log strings and uses list comprehension and enumerate() to extract only the IP addresses that failed (status code is NOT 200).

