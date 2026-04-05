#Prompt user to enter a number
number = int(input("Enter a number: "))
#Prompt user for number of rows
rows = int(input("How many rows? "))
#Loop through the range 1 - number of rows
for i in range(1, rows + 1):
    #Print each multiplication
    print(number, 'x', i, '=', number * i)