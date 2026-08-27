EX\_27AUG - Smart Contact Manager

Create a function named organize\_contacts that processes a list of contact dictionaries to create a clean contact database.



Each contact dictionary in the input list has these keys:



&#x20;   name: The person's name

&#x20;   email: The person's email address

&#x20;   phone: The person's phone number



The function should:



&#x20;   Remove duplicate contacts (contacts with the same email or phone number), keeping the first occurrence

&#x20;   Standardize all emails to lowercase

&#x20;   Filter out contacts with invalid email addresses

&#x20;   Filter out contacts with invalid phone numbers

&#x20;   Return a list of cleaned contact dictionaries



Validation rules:



&#x20;   Valid email: Must contain '@' and '.', and must not have spaces

&#x20;   Valid phone: Must contain exactly 10 digits (ignore non-digit characters like dashes or parentheses)



For cleaning phone numbers, use the str.isdigit() method to extract only the numeric digits from phone numbers. This method returns True if a character is a digit (0-9) and False otherwise, making it perfect for filtering out non-digit characters.

