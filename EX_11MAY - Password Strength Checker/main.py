#Prompt user to enter password
password = input("Enter your password: ")
#Declare variable (counter) for rules
rules = 0

#Set condition for length of password
if len(password) >= 8:
    #Increment counter
    rules += 1

#Check if the 'password' string contains at least one digit
has_digit = any(ch.isdigit() for ch in password)
#Check if the 'password' string contains at least one upper character
has_upper_char = any(ch.isupper() for ch in password)
#Check if the 'password' string contains at least one special character
has_special_char = any(ch in "!@#$%^&*" for ch in password)

#Set condition for digits
if has_digit:
    #Increment counter
    rules += 1
#Set condition for upper character
if has_upper_char:
    #Increment counter
    rules += 1
#Set condition for special character
if has_special_char:
    #Increment counter
    rules += 1

#Create list to store the rules and corresponding messages
rules_list = [
    (len(password) >= 8, "Must be at least 8 characters"),
    (has_digit, "Must contain at least one digit"),
    (has_upper_char, "Must contain at least one uppercase letter"),
    (has_special_char, "Must contain at least one special character"),
]

#Filter the failed rules
failed_rules = [message for condition, message in rules_list if not condition]
#Loop through the failed rules list
for rule in failed_rules:
    #Print each failed rule
    print(" ->", rule)

#Define variable for passed rules
passed_rules = 4 - len(failed_rules)
#Set condition for highest number of passed rules (i.e. 4)
if passed_rules == 4:
    #Print message
    print("Strong password")
#Set condition for 2-3 passed rules
elif passed_rules >= 2:
    #Print message
    print("Medium strength password")
#Set condition for 0-1 passed rules
else:
    #Print message
    print("Weak password")