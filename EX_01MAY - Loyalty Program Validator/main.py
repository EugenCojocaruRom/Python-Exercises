import re  # Import regular expressions to validate username characters

# Read the customer information
username = input("Enter username: ")  #Read the username
balance = input("Enter balance: ")  #Read the account balance as string
queue_position = int(input("Enter queue position: "))  #Read the queue position as integer

    # Validate the username
#Check if length is between 3 and 15 characters
length_ok = 3 <= len(username) <= 15
#Check if it doesn't start with a number --> since the length must be at least 3, it is OK to access username[0]
start_ok = not username[0].isdigit()
#Check if it contains only letters, numbers, and underscores --> r'^\w+$' matches the start to end of the string, \w includes [a-zA-Z0-9_]
chars_ok = bool(re.match(r'^\w+$', username))

#The username is valid only if all three conditions are met
username_valid = length_ok and start_ok and chars_ok

# Validate the balance --> attempt to convert the balance to a float; if it fails, it is not a valid number
try:
    float(balance)  # Attempt to convert the string to a decimal
    balance_valid = True  # Conversion succeeded
except ValueError:
    balance_valid = False  # Conversion failed, so string is not a valid number

#Calculate estimated wait time --> 5 minutes per customer ahead in queue
wait_time = queue_position * 5

#Print section separator
print("------------------")
    # Print the results
# Display "Valid" or "Invalid" for the username
if username_valid:
    print("Username: Valid")
else:
    print("Username: Invalid")

# Display "Valid" or "Invalid" for the balance
if balance_valid:
    print("User balance: Valid")
else:
    print("User balance: Invalid")

# Print the calculated wait time
print(f"Waiting time for {username}: {wait_time} minutes")
