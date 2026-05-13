#Read the exhibition name
exhibition_name = input("Enter exhibition name: ")
#Read the number of display cases
n = int(input("Enter the number of display cases: "))
#Read the display case sizes (space-separated numbers on one line)
case_sizes = list(map(int, input("Enter the sizes of the display cases (separate by space): ").split()))
#Read the visitor's age
age = int(input("Enter the visitor's age: "))
#Generate password from first 3 characters of exhibition name (uppercase)
password = exhibition_name[:3].upper()
#Find the largest display case size
largest_case = max(case_sizes)
#Determine ticket price based on age
if age < 12:
    ticket_price = 5
elif age <= 17 or age >= 65:
    ticket_price = 8
else:
    ticket_price = 12

# Print the results
print("The password is:", password)
print(f"The largest case is: {largest_case}")
print(f"Ticket price: {ticket_price}")
